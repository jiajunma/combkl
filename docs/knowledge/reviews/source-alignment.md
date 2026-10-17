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
summary: "English lecture notes organized by mathematical dependencies in the completed Lean development, with paper correspondence."
---

# Exposition and source correspondence

The user specifies the completed proof as the input to an exposition task. The notes explain its mathematical content rather than replace it with a new proof plan.

The nine chapters follow the library's mathematical constructions and proof
dependencies. The user's later clarification supersedes the earlier six-paper-
section organization. File boundaries alone do not determine topics: the Tits
development contains both realization geometry and parabolic transport, while
duality and sheaf decomposition span several modules.

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

The structure review adds explicit nodes for the R-kernel and lower-half KL
construction, graded sheaves and quotient maps, downward extension and
uniqueness, morphism extension and top splitting, boundary-model decomposition,
word-sheaf flabbiness, section and costalk duality, root-order construction and
diamond closure, the actual edge factor, filtered edge images, schedule states,
and reverse projectivity. Conditional local-intersection statements retain
their nonzero-diagonal hypotheses and are kept separate from the main R-first
route. The inventory is recorded in structure-review.json.
