---
agent: alignment-verifier
target:
  path: docs/knowledge/nodes
decision: aligned
created_at: "2026-10-17"
inputs:
  - sources/openai-math.manifest.tsv
  - sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig
  - sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build
summary: "English lecture-note exposition organized by the paper and linked to the actual Lean development."
---

# Exposition and source correspondence

The user specifies the completed proof as the input to an exposition task. The notes explain its mathematical content rather than replace it with a new proof plan.

The paper's six sections determine the chapter hierarchy. File boundaries do not determine mathematical topics: Tits.lean includes both realization geometry and parabolic transport, and 05-comparison.tex contains both paper sections 5 and 6.

The former separate code branch has been removed. Definitions, lemmas, worked calculations, and proofs form a single mathematical hierarchy. Chapter introductions give the reading sequence. Complete source files and import information are supplementary assets.

## Correspondence reviewed

- Strong Bruhat edges, order, intervals, and finite support retain their actual definitions and scopes.
- R/P normalization, the square parameter, and the lower-half construction are kept distinct.
- The realization includes the nondegenerate extension and independent root/normal data.
- Graded module, cover, sheaf, and pairing fields are explained rather than treated as unnamed assumptions.
- Word objects are tensor constructions; their stalks are images of weight evaluations, not assumed full coordinate products.
- Actual-character reciprocity comes from simultaneous stalk/kernel decomposition and cancellation.
- Dihedral transport preserves the relative interval, its order, ranks, edges, and range.
- Plane localization compares embedded edge images through the same sheaf isomorphism.
- The edge inclusion uses upper-kernel freeness; the reverse filtration supplies new freeness after equality.
- The Lean main route first proves R-tilde invariance and terminal-kernel freeness, then compares the canonical KL polynomials and applies finite support.

The paper's KL-character normalization and the implementation's R-first organization are explicitly distinguished. StalkCharacterObligation remains the definition of the stated condition rather than being silently inserted into the unconditional main theorem.

The builder verifies paper labels, declaration locations, the mathematical DAG, module import closure, structure-field coverage, and explicit source-text calls on the main route. The hierarchy-evidence.json report records these checks. Source-text call witnesses are not represented as a kernel-extracted dependency closure.

Teaching examples are explanatory calculations, not claims that each example is a separate Lean declaration. Exact mechanical and rendering results are recorded in build-report.json.
