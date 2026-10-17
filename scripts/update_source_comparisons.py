#!/usr/bin/env python3
"""Resolve source-comparison citations deterministically from the preserved sources."""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

BEGIN = "<!-- source-comparison:start -->"
END = "<!-- source-comparison:end -->"
BLOCK = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n*", re.S)


def comparison_blocks(root, index, repository):
    project = root.parents[1]
    paper = project / "sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build"
    labels = {}
    for path in sorted(paper.glob("*.tex")):
        for line, text in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for label in re.findall(r"\\label\{([^}]+)\}", text):
                labels[label] = (path.relative_to(project).as_posix(), line)
    data = yaml.safe_load((root / "source-comparisons.yml").read_text(encoding="utf-8"))
    blocks = defaultdict(list)
    for item in data["comparisons"]:
        paper_links = []
        for label in item["paper_labels"]:
            path, line = labels[label]
            url = f"{repository.web_url}/blob/{repository.revision}/{path}#L{line}"
            paper_links.append(f"[{label}]({url})")
        lean_links = []
        for name in item["lean_declarations"]:
            declaration = index.declarations[name]
            if not declaration.source_url:
                raise ValueError(f"Missing source URL for {name}")
            lean_links.append(f"[{declaration.module}:{declaration.line}]({declaration.source_url})")
        text = (
            f"**{item['kind']}.**\n\n"
            f"**OpenAI notes:** {item['paper']} " + ", ".join(paper_links) + ".\n\n"
            f"**Lean (primary):** {item['lean']} " + ", ".join(lean_links) + ".\n\n"
            f"**How to read this entry:** {item['consequence']}"
        )
        for node_id in item["nodes"]:
            blocks[node_id].append(text)
    return {node_id: BEGIN + "\n## Relation to the OpenAI notes\n\n" + "\n\n".join(parts) + "\n" + END
            for node_id, parts in blocks.items()}


def update_comparisons(root, nodes, index, repository, *, check=False):
    blocks = comparison_blocks(root, index, repository)
    by_id = {node.id: node for node in nodes}
    unknown = set(blocks) - set(by_id)
    if unknown:
        raise ValueError(f"Unknown source-comparison nodes: {sorted(unknown)}")
    changed = 0
    for node in nodes:
        original = node.file_path.read_text(encoding="utf-8")
        expected = blocks.get(node.id)
        if check:
            found = BLOCK.search(original)
            if (expected is not None and (found is None or found.group().rstrip() != expected)) or (expected is None and found):
                raise ValueError(f"Stale source comparison: {node.id}; run update_source_comparisons.py")
            continue
        text = BLOCK.sub("", original)
        if expected:
            marker = "*Proof.*" if "*Proof.*" in text else "## References"
            if marker not in text:
                raise ValueError(f"No source-comparison insertion point in {node.id}")
            text = text.replace(marker, expected + "\n\n" + marker, 1)
        if text != original:
            node.file_path.write_text(text, encoding="utf-8")
            changed += 1
    return {"authority": "Lean", "entries_with_explicit_source_comparison": len(blocks), "changed_files": changed}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mdblueprint", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    sys.path.insert(0, str(args.mdblueprint.resolve()))
    from tools.knowledge.config import load_project_config
    from tools.knowledge.lean_index import index_lean_project
    from tools.knowledge.parser import scan_directory

    root = Path(__file__).resolve().parents[1] / "docs/knowledge"
    repository = load_project_config(root).lean.repositories["openai-kl"]
    index = index_lean_project(repository.local_path, repository=repository)
    print(update_comparisons(root, scan_directory(root / "nodes"), index, repository, check=args.check))


if __name__ == "__main__":
    main()
