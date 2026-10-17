#!/usr/bin/env python3
"""Build and check the source-faithful KL knowledge base with mdblueprint.

This program never invokes Lean, Lake, Comparator, or a browser. Run it only
in an execution environment authorized for the current task.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import subprocess
import sys
import posixpath
from collections import Counter, defaultdict
from datetime import datetime, timezone
from graphlib import TopologicalSorter
from html.parser import HTMLParser
from html import escape
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "docs" / "knowledge"
SNAPSHOT = ROOT / "sources" / "openai-math"
LEAN = SNAPSHOT / "lean" / "OAI" / "RepresentationTheory" / "KazhdanLusztig"
REVISION = "adc7f1241b42e322a6451854ab7e4b4c146bf78a"
PAPER = SNAPSHOT / "preprints" / "Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026"


def verify_snapshot() -> int:
    manifest = ROOT / "sources" / "openai-math.manifest.tsv"
    with manifest.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    expected = set()
    for row in rows:
        path = SNAPSHOT / row["upstream_path"]
        data = path.read_bytes()
        digest = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        if digest != row["git_blob_sha1"]:
            raise ValueError(f"Source snapshot changed: {row['upstream_path']}")
        expected.add(path.relative_to(SNAPSHOT).as_posix())
    actual = {p.relative_to(SNAPSHOT).as_posix() for p in SNAPSHOT.rglob("*") if p.is_file()}
    if actual != expected:
        raise ValueError(f"Snapshot file set differs: {sorted(actual ^ expected)}")
    return len(rows)


def declaration_inventory(index, nodes) -> list[dict]:
    linked_nodes = defaultdict(list)
    for node in nodes:
        if node.lean:
            for name in node.lean.declarations:
                linked_nodes[name].append(node.id)
    inventory = []
    for decl in sorted(index.declarations.values(), key=lambda d: (d.module or "", d.line)):
        inventory.append({
            "declaration": decl.qualified_name,
            "kind": decl.kind,
            "module": "OAI.RepresentationTheory.KazhdanLusztig." + decl.module,
            "line": decl.line,
            "source_url": decl.source_url,
            "blueprint_nodes": sorted(linked_nodes[decl.qualified_name]),
        })
    return inventory


def validate_blueprint_hierarchy(nodes, index, config) -> dict:
    """Check the mathematical chapter registry and source correspondence."""
    registered = {topic.id for topic in config.topics if topic.id != "kl"}
    labels = {}
    for path in (PAPER / "build").glob("*.tex"):
        for line, text in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for match in re.finditer(r"\\label\{([^}]+)\}", text):
                labels[match.group(1)] = {"file": path.name, "line": line}
    chapters = {}
    for node in nodes:
        expected_status = "proved" if node.kind == "theorem" else "formalized"
        if node.status != expected_status:
            raise ValueError(f"Completed Lean development has inconsistent blueprint status: {node.id}: {node.status}")
        if node.primary_topic not in registered:
            raise ValueError(f"Node has an unregistered mathematical chapter: {node.id}")
        if node.id.startswith("code."):
            raise ValueError(f"Separate code topic is not part of this blueprint: {node.id}")
        if re.search(r"[\u3400-\u4dbf\u4e00-\u9fff]", node.title + node.body):
            raise ValueError(f"Non-English authored content: {node.id}")
        paper_spans = [s for s in node.source.spans if s.artifact == "openai-kl-paper"]
        if not node.lean or not node.lean.declarations:
            raise ValueError(f"Missing primary Lean correspondence: {node.id}")
        for span in paper_spans:
            label = span.locator.rsplit(";", 1)[-1].strip()
            if label not in labels:
                raise ValueError(f"Unknown paper label {label!r}: {node.id}")
        chapters.setdefault(node.primary_topic, []).append(node.id)
    if set(chapters) != registered:
        raise ValueError(f"Empty or missing mathematical chapters: {registered ^ set(chapters)}")
    imports = {}
    for module, path in sorted(index.modules.items()):
        dependencies = re.findall(
            r"^import OAI\.RepresentationTheory\.KazhdanLusztig\.(\w+)$",
            path.read_text(encoding="utf-8"), re.MULTILINE,
        )
        if not set(dependencies) <= index.modules.keys():
            raise ValueError(f"Missing imported source module: {module}")
        imports[module] = dependencies
    source_order = list(TopologicalSorter(imports).static_order())
    # Record explicit calls on the main route. These are source-text witnesses,
    # not a claim to have extracted the elaborated Lean dependency closure.
    prefix = "OAI.KLInvariance."
    route = {
        prefix + "combinatorial_invariance": ["exists_finiteIntervalModel", "klPolynomial_invariance_finite"],
        prefix + "BruhatGraph.klPolynomial_invariance_finite": ["bottom_eq_of_comparisons", "scaledKL_eq_transported"],
        prefix + "BruhatGraph.rTilde_invariance_and_freeness": ["rTilde_freeness_of_below"],
        prefix + "BruhatGraph.rTilde_freeness_of_below": ["rTilde_eq_of_smaller_data", "actual_freeSuffixes_of_rTilde_eq"],
        prefix + "BruhatGraph.rTilde_eq_of_smaller_data": ["rTilde_eval_le_of_upper_freeness"],
        prefix + "BruhatGraph.actual_freeSuffixes_of_rTilde_eq": ["schedule_kernels_free_of_endpoint_eq", "actual_endpoint_of_rTilde_eq"],
        prefix + "BruhatGraph.schedule_comparison_of_upper_freeness": ["scheduleState_le", "schedule_edge_image_le"],
        prefix + "BruhatGraph.schedule_edge_image_le": ["boundary_edge_image_le"],
        prefix + "BruhatGraph.stalkCharacter_reciprocity": ["bottCharacter_decomposition_both", "finite_character_cancellation"],
    }
    witnesses = []
    for name, callees in route.items():
        decl = index.declarations[name]
        lines = decl.file.read_text(encoding="utf-8").splitlines()
        following = [d.line for d in index.declarations.values() if d.file == decl.file and d.line > decl.line]
        end = min(following) - 1 if following else len(lines)
        body = "\n".join(lines[decl.line - 1:end])
        for callee in callees:
            if not re.search(r"(?<![\w'])" + re.escape(callee) + r"(?![\w'])", body):
                raise ValueError(f"Missing expected proof-route call: {name} -> {callee}")
        witnesses.append({"caller": name, "calls": callees, "file": decl.file.name, "line": decl.line})
    return {
        "organization_basis": "Mathematical constructions and proof dependencies in the Lean library",
        "chapters": {k: sorted(v) for k, v in sorted(chapters.items())},
        "module_imports": imports,
        "source_topological_order": source_order,
        "paper_labels_verified": len(labels),
        "main_route_source_witnesses": witnesses,
        "node_correspondence": [
            {"id": n.id, "chapter": n.primary_topic,
             "lean_declarations": n.lean.declarations if n.lean else [],
             "paper_locations": [s.locator for s in n.source.spans if s.artifact == "openai-kl-paper"]}
            for n in sorted(nodes, key=lambda n: n.id)
        ],
    }


def export_redirects(output, nodes, config):
    """Preserve published URLs after a chapter move without changing node IDs."""
    import yaml
    from tools.knowledge.export import home_topic_for_node, topic_path

    registry = KNOWLEDGE / "redirects.yml"
    if not registry.exists():
        return 0
    by_id = {node.id: node for node in nodes}
    topics = {topic.id for topic in config.topics}
    redirects = yaml.safe_load(registry.read_text(encoding="utf-8"))["redirects"]
    for old, target in sorted(redirects.items()):
        path = output / old
        if not path.resolve().is_relative_to(output.resolve()) or not old.endswith(".html"):
            raise ValueError(f"Unsafe legacy URL: {old}")
        if path.exists():
            raise ValueError(f"Legacy URL collides with a current page: {old}")
        if "node" in target:
            node = by_id[target["node"]]
            destination = topic_path(home_topic_for_node(node)) + "/" + node.id.replace(".", "_") + ".html"
        elif target.get("topic") in topics:
            destination = topic_path(target["topic"]) + "/index.html"
        else:
            raise ValueError(f"Unknown redirect target: {target}")
        if not (output / destination).is_file():
            raise ValueError(f"Missing redirect destination: {destination}")
        href = escape(posixpath.relpath(destination, posixpath.dirname(old)), quote=True)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            '<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta http-equiv="refresh" content="0;url={href}">'
            f'<link rel="canonical" href="{href}"><title>Entry moved</title></head>'
            f'<body><p>This entry has moved to its mathematical chapter. <a href="{href}">Continue reading</a>.</p></body></html>\n',
            encoding="utf-8",
        )
    return len(redirects)


def export_source_assets(output: Path, index, hierarchy) -> int:
    destination = output / "_sources"
    destination.mkdir()
    for module, source in sorted(index.modules.items()):
        target = destination / f"{module}.lean"
        shutil.copyfile(source, target)
        if source.read_bytes() != target.read_bytes():
            raise ValueError(f"Bundled source differs from snapshot: {module}")
    shutil.copyfile(PAPER / "paper.pdf", destination / "paper.pdf")
    (output / "module-imports.json").write_text(
        json.dumps(hierarchy["module_imports"], indent=2) + "\n", encoding="utf-8"
    )
    return len(index.modules)


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []
        self.definition_links = []
        self.text_parts = []
        self.code_blocks = []
        self._skipped = Counter()
        self._pre_depth = 0
        self._pre_chunks = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "a" and "definition-ref" in attributes.get("class", "").split():
            self.definition_links.append((attributes.get("data-node-id"), attributes.get("href", "")))
        if tag in {"pre", "code", "script", "style"}:
            self._skipped[tag] += 1
        if tag == "pre":
            if self._pre_depth == 0:
                self._pre_chunks = []
            self._pre_depth += 1
        for key, value in attrs:
            if key in {"href", "src"} and value:
                self.targets.append(value)

    def handle_endtag(self, tag):
        if tag == "pre" and self._pre_depth:
            self._pre_depth -= 1
            if self._pre_depth == 0:
                self.code_blocks.append("".join(self._pre_chunks))
        if self._skipped[tag]:
            self._skipped[tag] -= 1
        if tag in {"p", "div", "li", "h1", "h2", "h3", "td", "th"}:
            self.text_parts.append("\n")

    def handle_data(self, data):
        if self._pre_depth:
            self._pre_chunks.append(data)
        if not any(self._skipped.values()):
            self.text_parts.append(data)


def inspect_site(site: Path, nodes, home_topic_for_node, topic_path) -> dict:
    from tools.knowledge.renderer import TEX_MATH_RE

    missing_pages = []
    for node in nodes:
        path = site / topic_path(home_topic_for_node(node)) / (node.id.replace(".", "_") + ".html")
        if not path.is_file():
            missing_pages.append(str(path.relative_to(site)))
    if missing_pages:
        raise ValueError(f"Missing node pages: {missing_pages}")
    by_id = {node.id: node for node in nodes}
    broken_links = []
    definition_occurrences = Counter()
    formulas = []
    pages = sorted(site.rglob("*.html"))

    def inspect_fragment(html, label, base, *, extract_formulas=False):
        if "Unresolved" in html:
            raise ValueError(f"Unresolved Lean link in {label}")
        parser = Links()
        parser.feed(html)
        visible = "".join(parser.text_parts)
        prose = TEX_MATH_RE.sub("", visible)
        if re.search(r"\[\[(?:node:)?[a-zA-Z][\w.-]*(?:\|[^\]\n]*)?\]\]", prose):
            raise ValueError(f"Unrendered node reference in {label}")
        if extract_formulas:
            for match in TEX_MATH_RE.finditer(visible):
                raw = match.group()
                width = 2 if raw.startswith((r"\(", r"\[", "$$")) else 1
                formulas.append({
                    "page": label, "tex": raw[width:-width],
                    "display": raw.startswith((r"\[", "$$")),
                })
        for node_id, href in parser.definition_links:
            node = by_id.get(node_id)
            if node is None or node.kind != "definition":
                raise ValueError(f"Invalid definition target {node_id!r} in {label}")
            expected = site / topic_path(home_topic_for_node(node)) / (node_id.replace(".", "_") + ".html")
            url = urlsplit(href)
            if url.scheme or url.netloc or (base / unquote(url.path)).resolve() != expected.resolve():
                raise ValueError(f"Wrong definition destination for {node_id} in {label}: {href}")
            definition_occurrences[node_id] += 1
        for href in parser.targets:
            url = urlsplit(href)
            if url.scheme or url.netloc or not url.path or url.path.startswith("/"):
                continue
            target = (base / unquote(url.path)).resolve()
            if not target.exists():
                broken_links.append((label, href))

    for page in pages:
        inspect_fragment(page.read_text(encoding="utf-8"), page.relative_to(site).as_posix(),
                         page.parent, extract_formulas=True)
    payloads = sorted((site / "node_payloads").glob("*.json"))
    for path in payloads:
        payload = json.loads(path.read_text(encoding="utf-8"))
        label = path.relative_to(site).as_posix()
        for key in ("body_html", "proof_html"):
            inspect_fragment(payload.get(key) or "", f"{label}:{key}", site)
        for entry in [payload, *payload.get("deps", []), *payload.get("dependents", [])]:
            href = entry.get("href")
            if href and not (site / unquote(urlsplit(href).path)).is_file():
                broken_links.append((label, href))
    if broken_links:
        raise ValueError(f"Broken local links: {broken_links[:30]}")
    formula_path = site.parent / "knowledge-formulas.json"
    formula_path.write_text(json.dumps(formulas, ensure_ascii=False) + "\n", encoding="utf-8")
    return {
        "html_pages_checked": len(pages), "node_pages_checked": len(nodes),
        "graph_detail_payloads_checked": len(payloads),
        "generated_definition_links_checked": sum(definition_occurrences.values()),
        "definition_link_occurrences": dict(sorted(definition_occurrences.items())),
        "math_occurrences_extracted": len(formulas), "broken_links": [],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mdblueprint", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=ROOT / "build" / "knowledge")
    parser.add_argument("--katex-module", type=Path, help="Optional KaTeX 0.16.46 package for non-browser formula checks")
    args = parser.parse_args()
    tool_root = args.mdblueprint.resolve()
    output = args.output.resolve()
    # The upstream publisher replaces its output directory. Confine that action
    # to this project's dedicated build tree, never an arbitrary user directory.
    if output == ROOT / "build" or not output.is_relative_to(ROOT / "build"):
        raise ValueError("Output must be a subdirectory of this project's build/ directory")
    sys.path.insert(0, str(tool_root))
    from tools.knowledge.check import check_knowledge_base
    from tools.knowledge.config import load_project_config
    from tools.knowledge.export import home_topic_for_node, topic_path
    from tools.knowledge.kb_lean_field_audit import audit_node, render_report
    from tools.knowledge.lean_index import index_lean_project
    from tools.knowledge.parser import scan_directory
    from tools.knowledge.publish import publish
    from tools.knowledge.definition_links import DefinitionLinks

    snapshot_files = verify_snapshot()
    config = load_project_config(KNOWLEDGE)
    repository = config.lean.repositories["openai-kl"]
    index = index_lean_project(LEAN, repository=repository)
    if len(index.modules) != 34:
        raise ValueError(f"Expected 34 solution modules, got {len(index.modules)}")
    if index.warnings:
        raise ValueError("Declaration indexing warnings:\n" + "\n".join(index.warnings))
    nodes = scan_directory(KNOWLEDGE / "nodes")
    navigation = DefinitionLinks.load(KNOWLEDGE, nodes).summary()
    hierarchy = validate_blueprint_hierarchy(nodes, index, config)
    inventory = declaration_inventory(index, nodes)
    diagnostics = check_knowledge_base(KNOWLEDGE, strict_lean_placeholders=True)
    for diagnostic in diagnostics:
        print(diagnostic, flush=True)
    errors = [d for d in diagnostics if d.level == "error"]
    if errors:
        raise ValueError(f"Knowledge check failed with {len(errors)} errors")
    field_findings = [finding for node in nodes for finding in audit_node(node, index)]
    print(render_report(field_findings), flush=True)
    if field_findings:
        raise ValueError(f"Uncovered structure fields: {len(field_findings)}")
    publish(KNOWLEDGE, output)
    source_files = export_source_assets(output, index, hierarchy)
    redirected_pages = export_redirects(output, nodes, config)
    checks = inspect_site(output, nodes, home_topic_for_node, topic_path)
    if args.katex_module is not None:
        katex_result = subprocess.check_output([
            "node", str(ROOT / "scripts" / "check_knowledge_math.cjs"),
            str(output.parent / "knowledge-formulas.json"),
            str(args.katex_module.resolve()),
        ], text=True)
        checks["katex"] = json.loads(katex_result)
    (output / "declarations.json").write_text(
        json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    tool_revision = subprocess.check_output(
        ["git", "-C", str(tool_root), "rev-parse", "HEAD"], text=True
    ).strip()
    report = {
        "agent": "source-to-md",
        "target": {"path": "docs/knowledge"},
        "decision": "extracted",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "inputs": [f"agoramachina/openai-math@{REVISION}"],
        "summary": "Source-faithful knowledge base built and structurally checked.",
        "source_revision": REVISION,
        "mdblueprint_revision": tool_revision,
        "snapshot_files_verified": snapshot_files,
        "solution_modules": len(index.modules),
        "named_declarations_indexed": len(inventory),
        "mdblueprint_runtime_overrides": [],
        "code_link_repository": repository.web_url,
        "code_link_revision": repository.revision,
        "uncovered_structure_fields": len(field_findings),
        "node_count": len(nodes),
        "definition_navigation": navigation,
        "chapter_count": len(hierarchy["chapters"]),
        "legacy_page_redirects": redirected_pages,
        "bundled_source_files_verified": source_files,
        "node_kinds": dict(Counter(node.kind for node in nodes)),
        "node_statuses": dict(Counter(node.status for node in nodes)),
        "diagnostics": [str(d) for d in diagnostics],
        "browser_automation_used": False,
        **checks,
    }
    report_dir = KNOWLEDGE / "reviews"
    report_dir.mkdir(parents=True, exist_ok=True)
    (report_dir / "hierarchy-evidence.json").write_text(
        json.dumps(hierarchy, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (report_dir / "build-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    # Publish only the generated mathematical site and its build evidence.
    (output / ".nojekyll").touch()
    (output / "build-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    source_commit = subprocess.check_output(
        ["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True
    ).strip()
    (output / "build-info.json").write_text(json.dumps({
        "site_url": "https://jiajunma.github.io/combkl/",
        "blueprint_commit": source_commit,
        "mdblueprint_commit": tool_revision,
        "upstream_source_commit": REVISION,
        "built_at": report["created_at"],
        "node_statuses": report["node_statuses"],
    }, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    print(f"Knowledge base: {output / 'index.html'}")


if __name__ == "__main__":
    main()
