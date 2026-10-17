# Lecture notes on combinatorial invariance

These notes explain the completed Lean development of ordinary Kazhdan–Lusztig combinatorial invariance. The chapter structure follows the mathematical objects and proof dependencies in the Lean library. The preprint supplies context and source correspondence.

Start with [[node:kl.main.combinatorial_invariance]] for the goal. For a full reading, follow the nine chapters below: Bruhat order; Hecke polynomials; realization and graded algebra; graph sheaves; duality and characters; reflection orders; localization; comparison and freeness; simultaneous invariance.

The construction of minimal-boundary sheaves is separated from the morphism, uniqueness, decomposition, and duality theorems that make them useful. Likewise, the reflection schedule, its Hilbert-state vector, one-edge exact sequence, global comparison, endpoint equality, and reverse freeness are distinct stages.

## Main proof route

1. Define the polynomial families and prove canonical reciprocity.
2. Construct the actual boundary sheaf and its reciprocal stalk/costalk characters.
3. Reconstruct reflection edges and transport a geometric schedule through an interval isomorphism.
4. Compare embedded edge images by root-plane localization inside a free target.
5. Convert these inclusions into positive Hilbert-state inequalities.
6. Prove the new R entry using smaller intervals; identify the full R matrix.
7. Exact endpoints eliminate every deficit and recover terminal-kernel freeness.
8. Deduce canonical KL equality, then transport through finite-support models.

Definitions and constructions are marked formalized; theorem entries are marked proved. The distinction describes their mathematical roles in the completed development. The conditional local character-identification interface is kept separate from the unconditional R-first proof route.

## Using the notes

Technical terms link automatically to definitions. The graph records mathematical prerequisites, while Lean panels link to the unchanged source snapshot. Old published node URLs redirect to their current chapter locations.
