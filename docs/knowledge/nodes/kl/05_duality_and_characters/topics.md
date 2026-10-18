# 5. Word objects, duality, and characters

This chapter proves the character identity that connects sheaf geometry with the R-polynomials. Starting from the coefficient algebra and the sheaf machinery, it constructs tensor words, calculates their characters, and extracts the corresponding identity for the actual minimal-boundary sheaf.

There are two distinct character objects: the stalk character of a tensor word and the stalk character \(C_{x,b}\) of the boundary sheaf with top \(b\). The word character has a direct Hecke formula. Passing to the boundary character requires splitting, duality, and cancellation of lower summands.

## Tensor induction and the word sheaf

The reflection Frobenius extension provides a rank-two tensor step and a perfect pairing. Iterating it along a word gives the Bott–Samelson module. Full evaluation at its subexpressions is injective, so its image coordinates faithfully retain the original module. Grouping coordinates by weight gives the actual stalk images.

The pair-projection construction turns these stalks into a graph sheaf. Its edge relation records whether two endpoint values lift simultaneously from a word element. The free-stalk and exact-edge-kernel theorem proves that each stalk is free and that the upper edge kernel is multiplication by the label. These are proved properties of the image construction.

The character formula follows from the two possible exact sequences when a letter is prepended. Their kernels carry a degree-one shift, producing the same recurrence as multiplication by \(1+T_s\) in the unnormalized Hecke module. Thus a word-stalk character is a coefficient of the positive Hecke word. Flabbiness is proved separately by lifting compatible data over upper sets; pairwise edge compatibility alone does not establish that global lifting property.

1. [[node:kl.notes.perfect_pairings]]
2. [[node:kl.notes.reflection_frobenius]]
3. [[node:kl.notes.tensor_pairing]]
4. [[node:kl.notes.bott_samelson]]
5. [[node:kl.detail.word_evaluation_injective]]
6. [[node:kl.notes.word_stalks]]
7. [[node:kl.detail.word_sheaf]]
8. [[node:kl.detail.word_standard_stalks]]
9. [[node:kl.detail.word_characters]]
10. [[node:kl.detail.word_character_formula]]
11. [[node:kl.detail.word_flabbiness]]

## Global duality and costalk grading

A perfect pairing on global sections must interact correctly with support in order to give stalk–costalk duality. Supported sections and the incoming-label product identify the full outgoing kernel with a shifted dual of the stalk. The shift combines the degree of the section pairing with the number of incoming roots.

For a reduced word with top \(b\), the normalized boundary sheaf splits into the word sheaf by chapter 4. To obtain a perfect pairing on that particular summand, take the integral adjoint of its projector. The adjoint reverses composition and preserves primitivity. Its image can therefore be recognized as another copy of the boundary sheaf by the nonzero top stalk and the splitting theorem.

The canonical comparison with that adjoint image is an isomorphism. This is what justifies perfection of the resulting symmetric boundary pairing. Restricting a perfect form to an arbitrary summand would not suffice. Once the pairing is established, the stalk–costalk theorem converts a generator degree \(d_i\) into a kernel generator degree \(\ell(b)-\ell(x)-d_i\), giving the reciprocal character expression.

1. [[node:kl.notes.supported_pairings]]
2. [[node:kl.detail.section_duality]]
3. [[node:kl.detail.integral_adjoints]]
4. [[node:kl.detail.adjoint_primitivity]]
5. [[node:kl.detail.costalk_duality]]
6. [[node:kl.detail.boundary_pairing]]
7. [[node:kl.detail.costalk_reciprocity]]
8. [[node:kl.duality.stalk_character]]

## Character identities used by the proof

Two identities for a word sheaf meet here. The Hecke bar action and the word-character formula give an R-convolution for its outgoing-kernel character. Independently, one decomposition of the word sheaf into shifted boundary models gives both its stalk-character decomposition and its kernel-character decomposition, with the same multiplicity polynomials.

Substitute these decompositions into the word convolution. For a model with top \(y<b\), the character reciprocity at \(y\) is already known by induction. The finite cancellation lemma removes those lower-model terms. The top multiplicity is one because the reduced-word top stalk has character one. The remaining equality is
\[
q^{\ell(b)-\ell(x)}C_{x,b}(q^{-1})
=\sum_{x\le z\le b}R_{x,z}(q)C_{z,b}(q).
\]
This explains the division of labor among the results below: word reciprocity supplies the initial identity, decomposition supplies common coefficients, and cancellation isolates the actual boundary character.

1. [[node:kl.duality.bott_character_decomposition]]
2. [[node:kl.detail.word_character_reciprocity]]
3. [[node:kl.notes.character_cancellation]]
4. [[node:kl.duality.actual_character_reciprocity]]

## Local intersection maps and the conditional character interface

The local intersection map takes a stalk dual into the stalk through the established duality construction. Its symmetry and image describe additional local structure. The strict half-degree conclusion in the corresponding theorem requires a nonzero diagonal value; that hypothesis must remain visible.

The condition identifying the actual stalk character with the canonical KL polynomial is also stated separately. The main R-first invariance route uses the proved reciprocity displayed above. It does not replace \(C\) by \(P\). The source-comparison sections explain how this route differs from the character-normalization presentation in the OpenAI notes.

1. [[node:kl.detail.local_intersection]]
2. [[node:kl.detail.local_diagonal_degree]]
3. [[node:kl.duality.character_identity_condition]]

## How later chapters use these results

Chapter 8 uses the actual stalk and costalk characters to identify the two ends of its Hilbert-state comparison. Chapter 9 uses their R-reciprocity to cancel already-known R-entries and isolate the new bottom entry. The canonical KL polynomials return only after the simultaneous R/freeness induction is complete.

When following the main proof, read through actual-character reciprocity before moving to the comparison chapters. The local intersection entries can then be read as a related branch with their own explicit hypotheses.
