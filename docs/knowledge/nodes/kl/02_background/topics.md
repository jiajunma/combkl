# 2. Real realizations and moment-graph sheaves

This chapter supplies the objects on which the comparison acts. It follows the paper's background section, while expanding the algebra and sheaf constructions implemented in Lean.

## Finite support and real realizations

Begin with [[node:kl.foundations.finite_intervals]] and [[node:kl.foundations.subword]]. The finite-support argument is [[node:kl.foundations.finite_support]]. Its eventual use is made precise in [[node:kl.main.finite_interval_model]] and [[node:kl.main.finite_model_transport]]: finite generator rank is sufficient, even when the groups are infinite. [[node:kl.foundations.rank_preservation]] explains why interval rank can serve as the induction parameter.

Next read [[node:kl.notes.extended_realization]], [[node:kl.notes.reflection_faithfulness]], and [[node:kl.realization.reflection_plane]]. The ambient form is made nondegenerate by enlarging the Tits space. This does not impose nondegeneracy on every root plane.

The reflection-order input is developed in [[node:kl.notes.reflection_order]], [[node:kl.notes.path_product]], and [[node:kl.paths.dyer_paths]]. Chapter 3 develops the relative dihedral combinatorics used when an order is transported.

## Graded modules and the boundary construction

The algebraic starting point is [[node:kl.sheaves.graded_module]]. Read [[node:kl.notes.graded_nakayama]], [[node:kl.sheaves.minimal_cover]], and [[node:kl.notes.minimal_cover_existence]] to understand how a finite graded module is covered with the correct generator degrees.

For the graph side, read [[node:kl.sheaves.graph_sheaf]], [[node:kl.sheaves.flabbiness]], and [[node:kl.notes.boundary_image]]. Then [[node:kl.sheaves.boundary_sheaf]] and [[node:kl.sheaves.boundary_existence]] describe the descending construction. The single-edge example makes the general definition concrete. The intermediate modules that will vary during the proof are [[node:kl.sheaves.upward_kernel]].

[[node:kl.sheaves.hilbert_free]] explains how degrees become Hilbert values. [[node:kl.duality.stalk_character]] records the character of an actual constructed stalk.

## Word objects, pairings, and character reciprocity

The Lean construction develops the character input through word objects. Read:

1. [[node:kl.notes.perfect_pairings]] and [[node:kl.notes.reflection_frobenius]];
2. [[node:kl.notes.tensor_pairing]] and [[node:kl.notes.bott_samelson]];
3. [[node:kl.notes.word_stalks]] and [[node:kl.notes.supported_pairings]];
4. [[node:kl.duality.bott_character_decomposition]];
5. [[node:kl.notes.character_cancellation]] and [[node:kl.duality.actual_character_reciprocity]].

The paper identifies BMP stalk characters with KL polynomials in its normalization input. The implementation's main route instead first uses reciprocity of the actual characters to prove R-tilde invariance. [[node:kl.duality.character_identity_condition]] records the separate identification interface precisely. Chapter 6 explains how the canonical KL polynomial is then recovered.
