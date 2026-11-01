---
title: The proof of combinatorial invariance
primary_topic: kl.invariance
---

An interval order isomorphism is the input to the main theorem: the canonical Kazhdan–Lusztig polynomial of its two endpoints is unchanged. The proof first develops Coxeter length and Bruhat order, then defines the Hecke operators, their bar transform, and the canonical polynomial families. These definitions fix the normalizations used throughout the argument.

The geometric part recovers reflection edges from the interval order and uses target-root scores to order the source edges. The sheaf part constructs actual boundary modules, their pairings and characters. Root-plane localization reduces the comparison of two embedded edge images to dihedral structure models; the [[node:kl.paths.later_count|transported count theorem]] supplies the difference of their label exponents. This gives the [[node:kl.local.edge_inclusion|global edge inclusion]] under the specified upper-kernel freeness hypothesis.

The [[node:kl.comparison.edge_increment|one-edge Hilbert comparison]] turns that inclusion into a numerical step. Iterating the step produces an ordered transfer product; the [[node:kl.paths.dyer_paths|geometric path identity]] identifies it with the target R-matrix. Character reciprocity supplies the endpoint formulas. When the R-data agree, the comparison is exact at its endpoints, forcing equality at every step and recovering free suffix kernels. The [[node:kl.comparison.rtilde_invariance|simultaneous invariance induction]] proves R-invariance together with this freeness. [[node:kl.foundations.canonical_kl|Canonical KL uniqueness]] then gives the KL conclusion, and [[node:kl.main.finite_model_transport|finite-support reduction]] reaches arbitrary Coxeter systems. The sequence below follows these inputs into the final result.

## Reading sequence

1. [[node:kl.foundations.bruhat_order]] — Define the interval order being preserved.
2. [[node:kl.definitions.hecke_operators]] — Define the algebraic operators.
3. [[node:kl.definitions.bar_involution]] — Construct the transform defining the R-data.
4. [[node:kl.foundations.canonical_kl]] — Identify the polynomial family in the conclusion.
5. [[node:kl.detail.polynomial_labels]] — Connect root geometry with coefficient labels.
6. [[node:kl.paths.graph_invariance]] — Recover the reflection edges from the order.
7. [[node:kl.paths.dyer_paths]] — Identify the geometric path product with R-data.
8. [[node:kl.sheaves.boundary_sheaf]] — Introduce the actual sheaf used by comparison.
9. [[node:kl.duality.actual_character_reciprocity]] — Obtain the actual sheaf-character identity.
10. [[node:kl.local.localized_decomposition]] — Construct the local models used in comparison.
11. [[node:kl.local.edge_inclusion]] — Obtain the conditional image inclusion.
12. [[node:kl.comparison.edge_increment]] — Convert it into the normalized numerical step.
13. [[node:kl.detail.schedule_comparison]] — Iterate the bound under the upper-freeness hypotheses.
14. [[node:kl.detail.endpoint_equality]] — Make endpoints exact when the R-data agree.
15. [[node:kl.detail.reverse_projectivity]] — Recover projective kernels from the resulting image equalities.
16. [[node:kl.comparison.rtilde_invariance]] — Follow the simultaneous induction.
17. [[node:kl.main.kl_finite]] — Identify the canonical KL polynomials after R-invariance.
18. [[node:kl.main.finite_interval_model]] — Reduce an arbitrary interval to finite support.
19. [[node:kl.main.combinatorial_invariance]] — Read the unrestricted final theorem.
