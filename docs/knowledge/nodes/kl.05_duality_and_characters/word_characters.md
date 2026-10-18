---
id: kl.detail.word_characters
title: Word-stalk characters and the positive Hecke word
kind: definition
status: formalized
primary_topic: kl.05_duality_and_characters
topics:
- kl.05_duality_and_characters
uses:
- kl.notes.word_stalks
- kl.detail.graded_character
- kl.definitions.hecke_operators
- kl.detail.word_standard_stalks
- kl.detail.coefficient_change
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.bottStalkCharacter
  - OAI.KLInvariance.HeckeQ.positiveWord
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1934
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkCharacter
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:204
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.positiveWord
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# Word-stalk characters and the positive Hecke word

For a word \(\mathbf s\), let \(B^{\mathbf s}_x\) be the actual image stalk of its tensor module at \(x\). Its word-stalk character \(C^{\mathbf s}_x(q)\) is the graded-rank polynomial of that stalk, transported to polynomial coefficients. For \(N\) degree-one coefficient variables,
\[
H_{B^{\mathbf s}_x}(q)=\frac{C^{\mathbf s}_x(q)}{(1-q)^N},\qquad 0<q<1.
\]
This construction uses the proved graded freeness of the word stalks.

In the unnormalized Hecke module with standard basis \(T_x\), define the positive word recursively by
\[
H_{\varnothing}=T_1,\qquad H_{(s,\mathbf t)}=(1+T_s)H_{\mathbf t}.
\]
Equivalently, apply the left Hecke operator and add the previous vector. This definition is valid for any word; reducedness is not required. The word-character theorem identifies \(C^{\mathbf s}_x\) with the coefficient of \(T_x\) in \(H_{\mathbf s}\).

The character of a word stalk and the character of an indecomposable boundary-sheaf stalk are distinct objects. Identifying the first with a positive Hecke word does not identify the second with a KL polynomial.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate objects.**

**OpenAI notes:** The normalization discussion identifies indecomposable boundary-sheaf characters with KL polynomials by the cited character theorem. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The word-stalk character is proved to equal a positive Hecke-word coefficient. Its R-convolution is then proved before model decomposition and cancellation. The separate boundary-character identification is exposed as StalkCharacterObligation. [IntegralPairings:289](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L289), [CharacterReciprocity:1134](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1134), [SheafMorphisms:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219).

**How to read this entry:** Distinguish a tensor word from its boundary-model summands. The proved word formula and convolution are the inputs used here; they do not assert the separate boundary-character identification.
<!-- source-comparison:end -->

## References

The precise Lean sources are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottStalkCharacter`: [BottSamelson.lean:1934](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1934).

`OAI.KLInvariance.HeckeQ.positiveWord`: [IntegralPairings.lean:204](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L204).
