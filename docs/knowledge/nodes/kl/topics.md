# Lecture notes on combinatorial invariance

These notes explain the completed Lean development of ordinary Kazhdan–Lusztig combinatorial invariance. The paper supplies the six-chapter organization; the definitions, intermediate constructions, and proof steps are linked to their precise Lean declarations.

The starting background is the definition of a Coxeter system and the basic Hecke-algebra conventions. The notes develop the additional graded algebra, moment-graph sheaves, word-object dualities, dihedral combinatorics, and localization used by the proof.

## Reading the argument

The target is [[node:kl.main.combinatorial_invariance]]. A first pass can follow these milestones:

1. [[node:kl.foundations.normalized_kl]] fixes the polynomial being compared.
2. [[node:kl.notes.extended_realization]] and [[node:kl.sheaves.boundary_existence]] supply the geometric-algebraic model.
3. [[node:kl.paths.graph_invariance]], [[node:kl.notes.relative_dihedral_transport]], and [[node:kl.paths.later_count]] recover the required rank-two information.
4. [[node:kl.local.localized_decomposition]] and [[node:kl.local.edge_inclusion]] compare actual edge images.
5. [[node:kl.comparison.global_comparison]] and [[node:kl.comparison.rtilde_invariance]] close the simultaneous comparison and freeness induction.
6. [[node:kl.main.kl_finite]] and [[node:kl.main.finite_model_transport]] give the final theorem.

For a detailed reading, use the ordered introductions on the six chapter pages below. Each entry contains its statement or definition, explanatory calculations or proof, and source references. The dependency graph records mathematical prerequisites.

## Paper and formalization

The paper uses the KL character identification in its background normalization. The implementation also develops an R-first route: actual sheaf characters provide reciprocal test vectors, R-tilde invariance is established first, and the canonical KL polynomials are compared afterwards. The notes preserve this distinction instead of relabelling one route as the other.

Source files are not separate mathematical topics. The Lean panels give the declarations supporting an entry, and the complete fixed source snapshot remains available for following further formal details.
