# Lecture notes on KL combinatorial invariance

These English notes explain the completed OpenAI Lean development. The paper supplies the chapter organization; the actual definitions, hypotheses, constructions, proof steps, and declaration references supply the exposition.

Start with the [online reading guide](http://127.0.0.1:8765/kl/) when the local preview is running. The Markdown guide is [nodes/kl/topics.md](nodes/kl/topics.md).

## Chapters

1. [Introduction and conventions](nodes/kl/01_introduction/topics.md)
2. [Real realizations and moment-graph sheaves](nodes/kl/02_background/topics.md)
3. [Dihedral intervals and transported reflection orders](nodes/kl/03_dihedral/topics.md)
4. [Localization at a root plane](nodes/kl/04_localization/topics.md)
5. [Comparison of edge images](nodes/kl/05_edge_images/topics.md)
6. [Reciprocity and simultaneous induction](nodes/kl/06_induction/topics.md)

Each chapter introduction gives an ordered reading sequence. The entries contain mathematical exposition and supporting Lean references. Worked calculations include rank-one normalization, the \(A_2\) reflection graph, lower-half truncation, a one-edge sheaf, Hilbert normalization, the edge transfer coefficient, and higher-codimension detection.

The supplementary background explains minimal covers, graded Nakayama, graded projectivity, Frobenius pairings, Bott–Samelson word objects, supported sections, and character cancellation.

The paper and Lean implementation organize the final comparison differently. The notes explicitly distinguish the paper's KL-character presentation from the implementation's R-first route, then explain how canonical KL equality is recovered.

## Source correspondence

The fixed upstream commit is adc7f1241b42e322a6451854ab7e4b4c146bf78a. Source references identify exact declarations and paper labels. All 34 Lean files and the original PDF are retained in the source snapshot.

The [public snapshot in combkl](https://github.com/jiajunma/combkl/tree/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math)
is pinned at commit 108243e05ed46235bf82dc30d4d90c794579776f. Generated code
links use that commit and the `sources/openai-math/` prefix; the upstream
revision remains the provenance identifier. The link updater validates all
81 Git blob hashes before changing source destinations:

    python3 scripts/update_source_links.py 108243e05ed46235bf82dc30d4d90c794579776f

The completed development is represented by 45 `proved` theorem entries and
29 `formalized` definitions/concepts. There are no `admitted` entries. Worked
teaching examples are explanatory prose unless linked to a separate theorem.

Source inventories and imports are supporting data, not separate mathematical topics. The generated site provides declarations.json, module-imports.json, and unchanged files under _sources/. The dependency graph is the mathematical graph of the notes.

## Build

In an environment authorized to run documentation tools:

    python3 scripts/build_knowledge.py --mdblueprint /path/to/mdblueprint

Use [mdblueprint commit dd0743a](https://github.com/gametheoryinlean/mdblueprint/commit/dd0743a94b709220f9411964a781da6b2fc61d5b)
or a compatible later version. To reproduce the documented build:

    git clone https://github.com/gametheoryinlean/mdblueprint ../mdblueprint
    git -C ../mdblueprint checkout dd0743a94b709220f9411964a781da6b2fc61d5b
    python3 -m venv build/docs-venv
    build/docs-venv/bin/python -m pip install ../mdblueprint
    build/docs-venv/bin/python scripts/build_knowledge.py --mdblueprint ../mdblueprint

The builder verifies the 81-file source manifest, indexes declarations, checks chapter assignments against paper labels, checks the node graph and Lean references, audits structured-definition field coverage, generates the site with mdblueprint, and checks every HTML page and local link. It also records explicit source-text calls on the main proof route. These are documentation checks, not an invocation of Lean or Comparator.

For KaTeX checks matching the site's renderer:

    npm install --prefix build/document-tools --ignore-scripts --no-audit --no-fund --save-exact katex@0.16.46
    python3 scripts/build_knowledge.py --mdblueprint /path/to/mdblueprint --katex-module build/document-tools/node_modules/katex

This checks the published formulas through KaTeX's string renderer without browser automation.

The output is build/knowledge/. Exact check results are recorded in [reviews/build-report.json](reviews/build-report.json), and paper/declaration correspondence in [reviews/hierarchy-evidence.json](reviews/hierarchy-evidence.json).

## Local reading

Serve the generated site from the repository root:

    python3 -m http.server 8765 --bind 127.0.0.1 --directory build/knowledge

Open [the lecture notes](http://127.0.0.1:8765/kl/) or [the dependency graph](http://127.0.0.1:8765/dep_graph_document.html). The graph needs HTTP to load its generated data.

## Maintenance

The mathematical Markdown entries are authoritative exposition. The original Lean snapshot is preserved separately. Rebuild generated HTML and graphs rather than editing them.

Definition links are generated by Python during the build, using
[concept-links.yml](concept-links.yml). That registry associates terms and
aliases with definition IDs and optional chapter scopes. Write ordinary prose
such as “the operators, their quadratic relation, and the bar involution”; the
builder creates the three definition links automatically. Mathematical meaning
is curated in the registry; occurrence matching and URL construction use no LLM.
Unregistered terms are left unchanged rather than assigned a guessed definition.

Matching is case-insensitive, respects word boundaries, and prefers the longest
registered phrase. Formulas, code, headings, existing links, and self-references
are preserved. Missing definitions and conflicting aliases stop the build.
Explicit reading-order references use `[[node:ID]]`; Python resolves their
destinations from the node's current chapter. Definition navigation does not add
edges to the mathematical dependency graph. Both node pages and graph details
are checked after generation.

Definition matching, current-chapter routing, graph-detail links, and
noncomputable-section indexing are implemented in mdblueprint itself. Combkl
has no runtime overrides of mdblueprint. Project regression checks are in
scripts/test_blueprint_navigation.py and scripts/test_knowledge_build.py.

The current task has explicit permission for local documentation construction and checks. That permission does not authorize Lean execution, mathematical experiments, browser automation, or screen capture.
