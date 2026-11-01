---
title: The proof of combinatorial invariance
primary_topic: kl.invariance
---

An interval order isomorphism is the input to the main theorem: the canonical Kazhdan–Lusztig polynomial of its two endpoints is unchanged. The proof first develops Coxeter length and Bruhat order, then defines the Hecke operators, their bar transform, and the canonical polynomial families. These definitions fix the normalizations used throughout the argument.

The geometric part recovers reflection edges from the interval order and uses target-root scores to order the source edges. The sheaf part constructs actual boundary modules, their pairings and characters. Root-plane localization reduces the comparison of two embedded edge images to dihedral structure models; the [[node:kl.paths.later_count|transported count theorem]] supplies the difference of their label exponents. This gives the [[node:kl.local.edge_inclusion|global edge inclusion]] under the specified upper-kernel freeness hypothesis.

The [[node:kl.comparison.edge_increment|one-edge Hilbert comparison]] turns that inclusion into a numerical step. Iterating the step produces an ordered transfer product; the [[node:kl.paths.dyer_paths|geometric path identity]] identifies it with the target R-matrix. Its adapted part first constructs a chamber order, rotates at a least simple descent and matches the [[node:kl.paths.path_polynomial_recursion|path-polynomial recursion]] with the Hecke recursion. Character reciprocity supplies the endpoint formulas. When the R-data agree, the comparison is exact at its endpoints, forcing equality at every step and recovering free suffix kernels. The [[node:kl.comparison.rtilde_invariance|simultaneous invariance induction]] proves R-invariance together with this freeness. [[node:kl.foundations.canonical_kl|Canonical KL uniqueness]] then gives the KL conclusion, and [[node:kl.main.finite_model_transport|finite-support reduction]] reaches arbitrary Coxeter systems. The sequence below follows these inputs into the final result.

## Reading sequence

1. [[node:kl.foundations.bruhat_order]] — Define the interval order being preserved.
2. [[node:kl.definitions.hecke_operators]] — Define the algebraic operators.
3. [[node:kl.definitions.bar_involution]] — Construct the transform defining the R-data.
4. [[node:kl.foundations.canonical_kl]] — Identify the polynomial family in the conclusion.
5. [[node:kl.detail.polynomial_labels]] — Connect root geometry with coefficient labels.
6. [[node:kl.paths.graph_invariance]] — Recover the reflection edges from the order.
7. [[node:kl.paths.directed_paths]] — Define directed edge lists and their selected path sets.
8. [[node:kl.notes.path_product]] — Expand the transfer entry into weighted paths.
9. [[node:kl.order.rotation_exists]] — Move a least simple root to greatest position at a shorter top.
10. [[node:kl.paths.path_polynomial_recursion]] — Derive the recursion from the two path bijections.
11. [[node:kl.paths.adapted_path_identification]] — Identify the adapted path polynomial with the Hecke R-family.
12. [[node:kl.dihedral.plane_path_reversal]] — Prove the full intrinsic plane-block identity.
13. [[node:kl.paths.dyer_paths]] — Identify the geometric path product with R-data.
14. [[node:kl.sheaves.boundary_sheaf]] — Introduce the actual sheaf used by comparison.
15. [[node:kl.duality.actual_character_reciprocity]] — Obtain the actual sheaf-character identity.
16. [[node:kl.local.localized_decomposition]] — Construct the local models used in comparison.
17. [[node:kl.local.edge_inclusion]] — Obtain the conditional image inclusion.
18. [[node:kl.comparison.edge_increment]] — Convert it into the normalized numerical step.
19. [[node:kl.detail.schedule_comparison]] — Iterate the bound under the upper-freeness hypotheses.
20. [[node:kl.comparison.schedule_upper_freeness]] — Supply image inclusions from the exact upper suffix kernels.
21. [[node:kl.detail.endpoint_equality]] — Make endpoints exact when the R-data agree.
22. [[node:kl.detail.reverse_projectivity]] — Recover projective kernels from the resulting image equalities.
23. [[node:kl.comparison.rtilde_invariance]] — Follow the simultaneous induction.
24. [[node:kl.main.kl_finite]] — Identify the canonical KL polynomials after R-invariance.
25. [[node:kl.main.finite_interval_model]] — Reduce an arbitrary interval to finite support.
26. [[node:kl.main.combinatorial_invariance]] — Read the unrestricted final theorem.
