# Lecture notes on KL combinatorial invariance

These English notes explain the completed OpenAI Lean development. Chapters
follow its mathematical constructions and proof dependencies. The preprint
provides context and correspondence without fixing the chapter boundaries.

Start with the [published reading guide](https://jiajunma.github.io/combkl/kl/)
or the [dependency graph](https://jiajunma.github.io/combkl/dep_graph_document.html).
The website requires no installation. The Markdown guide is [nodes/kl/topics.md](nodes/kl/topics.md).

## Chapters

1. [Coxeter systems and Bruhat order](nodes/kl/01_bruhat_order/topics.md)
2. [Hecke operators and canonical polynomials](nodes/kl/02_hecke_polynomials/topics.md)
3. [Real realizations and graded algebra](nodes/kl/03_realizations_and_grading/topics.md)
4. [Moment-graph sheaves and minimal extensions](nodes/kl/04_moment_graph_sheaves/topics.md)
5. [Word objects, duality, and characters](nodes/kl/05_duality_and_characters/topics.md)
6. [Reflection orders and dihedral geometry](nodes/kl/06_reflection_orders/topics.md)
7. [Localization and embedded edge images](nodes/kl/07_localization/topics.md)
8. [Hilbert comparisons and kernel freeness](nodes/kl/08_comparison_and_freeness/topics.md)
9. [Simultaneous induction and combinatorial invariance](nodes/kl/09_combinatorial_invariance/topics.md)

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

The completed development is represented by 69 `proved` theorem entries and
49 `formalized` definitions/concepts. There are no `admitted` entries. Worked
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

The builder verifies the 81-file source manifest, indexes declarations, checks
the mathematical chapter registry and any supplied paper labels, checks the
node graph and Lean references, audits structured-definition field coverage,
generates the site with mdblueprint, and checks every HTML page and local link.
It also records explicit source-text calls on the main proof route. These are
documentation checks, not an invocation of Lean or Comparator.

For KaTeX checks matching the site's renderer:

    npm install --prefix build/document-tools --ignore-scripts --no-audit --no-fund --save-exact katex@0.16.46
    python3 scripts/build_knowledge.py --mdblueprint /path/to/mdblueprint --katex-module build/document-tools/node_modules/katex

This checks the published formulas through KaTeX's string renderer without browser automation.

The output is build/knowledge/. Exact check results are recorded in [reviews/build-report.json](reviews/build-report.json), and paper/declaration correspondence in [reviews/hierarchy-evidence.json](reviews/hierarchy-evidence.json).

## Local reading

Serve the generated site from the repository root:

    python3 -m http.server 8765 --bind 127.0.0.1 --directory build/knowledge

Open [the lecture notes](http://127.0.0.1:8765/kl/) or [the dependency graph](http://127.0.0.1:8765/dep_graph_document.html). The graph needs HTTP to load its generated data.

## Public website

The built site is hosted at [jiajunma.github.io/combkl](https://jiajunma.github.io/combkl/).
The workflow in `.github/workflows/blueprint-pages.yml` builds on pushes to
`codex/kl-source-snapshot` and `main`, and also supports manual runs once the
workflow is on the default branch. It uses the pinned mdblueprint revision,
runs the project tests and complete document checks, and uploads only the
generated `build/knowledge/` directory for deployment. A failed build does not
replace the public site.

The [public build information](https://jiajunma.github.io/combkl/build-info.json)
identifies the exact blueprint, tooling, and upstream source revisions.
The [build report](https://jiajunma.github.io/combkl/build-report.json) records
the page, link, formula, and status checks. The deployed artifact also includes
the original paper PDF and all 34 Lean modules under `_sources/`.

## Maintenance

The mathematical Markdown entries are authoritative exposition. The original Lean snapshot is preserved separately. Rebuild generated HTML and graphs rather than editing them.

The structure review separated 44 definitions and intermediate results that
were previously implicit or folded into broad pages. Its machine-readable
inventory is [reviews/structure-review.json](reviews/structure-review.json).
The chapter registry is open to mathematically justified changes; the builder
does not enforce the preprint's six-section outline. Stable node IDs remain
unchanged, and [redirects.yml](redirects.yml) generates redirects for all 80
previous chapter and node URLs affected by this reorganization.

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
