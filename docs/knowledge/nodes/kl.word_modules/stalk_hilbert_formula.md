---
id: kl.word.stalk_hilbert_formula
title: The convergent Hilbert formula for a word-stalk character
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.detail.word_characters
- kl.sheaves.hilbert_free
- kl.detail.coefficient_change
- kl.algebra.character_basis_independence
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  declarations:
  - OAI.KLInvariance.TitsSpace.bottPolynomialStalk_finrank
  - OAI.KLInvariance.TitsSpace.bottStalkCharacter_hasSum
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1938
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottPolynomialStalk_finrank
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1945
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkCharacter_hasSum
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the gradings, scalar actions, coefficient variables and formal polynomial
    conclusions explicit?
  verdict: Read bottPolynomialStalk_finrank and bottStalkCharacter_hasSum. Expanded
    the real-linear degreewise transport, nonnegative basis and finite sum of shifted
    polynomial coefficient series.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# The convergent Hilbert formula for a word-stalk character

Fix a finite-generator Coxeter system and a basis with \(N\) elements of the extended real realization. For every word \(\mathbf t\), weight \(x\), and real \(0<t<1\),
\[
\sum_{n\in\mathbb Z}
\dim_{\mathbb R}(M_{\mathbf t}^x)_n\,t^n
=C_x^{\mathbf t}(t)(1-t)^{-N}.
\]
The series converges, and its terms use the actual symmetric-coordinate stalk pieces.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate objects.**

**OpenAI notes:** The normalization discussion identifies indecomposable boundary-sheaf characters with KL polynomials by the cited character theorem. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The word-stalk character is proved to equal a positive Hecke-word coefficient. Its R-convolution is then proved before model decomposition and cancellation. The separate boundary-character identification is exposed as StalkCharacterObligation. [IntegralPairings:289](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L289), [CharacterReciprocity:1134](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1134), [SheafMorphisms:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219), [BottSamelson:1924](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1924), [BottSamelson:1945](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1945), [IntegralPairings:104](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L104), [IntegralPairings:120](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L120), [CharacterReciprocity:915](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L915).

**Role in the proof:** The word formula and R-convolution describe the tensor word. A common decomposition into boundary models then supplies the character identities used in the cancellation argument.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Compare the two coefficient presentations

Let \(S\) be the polynomial stalk data obtained from \(M_{\mathbf t}^x\) by the graded isomorphism \(A\to P\). Coefficient transport is real-linear on the underlying vectors and sends each old homogeneous piece onto the corresponding piece of \(S\).

It therefore gives, degree by degree,
\[
\dim_{\mathbb R}S_n=\dim_{\mathbb R}(M_{\mathbf t}^x)_n.
\]
This is bottPolynomialStalk_finrank.

### Step 2. Use a finite nonnegative homogeneous basis

Choose a finite homogeneous \(P\)-basis \(b_j\) of \(S\), with degrees \(d_j\ge0\). The source's character is the polynomial of a chosen such basis, and basis independence gives
\[
C_x^{\mathbf t}(q)=\sum_jq^{d_j}
\]
for this basis as well.

### Step 3. Sum the shifted coefficient pieces

The [[node:kl.sheaves.hilbert_free|homogeneous-free Hilbert theorem]] gives
\[
S_n\simeq\bigoplus_j P_{n-d_j}
\]
as real vector spaces. Each summand is the coefficient module shifted by its generator degree.

For \(0<t<1\), the coefficient series converges to \((1-t)^{-N}\). The contribution of \(b_j\) is therefore
\(t^{d_j}(1-t)^{-N}\). There are finitely many basis vectors, so their convergent sums add:
\[
\sum_n\dim_{\mathbb R}S_n\,t^n
=\left(\sum_jt^{d_j}\right)(1-t)^{-N}
=C_x^{\mathbf t}(t)(1-t)^{-N}.
\]

### Step 4. Return to the original stalk pieces

Replace every dimension on the left using Step 1. This preserves the terms and the sum, giving the asserted formula for the actual stalk.

The common coefficient factor depends on the fixed realization dimension \(N\). Prepending letters changes the stalk character while keeping that same factor.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottPolynomialStalk_finrank`: [BottSamelson.lean:1938](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1938).

`OAI.KLInvariance.TitsSpace.bottStalkCharacter_hasSum`: [BottSamelson.lean:1945](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1945).
