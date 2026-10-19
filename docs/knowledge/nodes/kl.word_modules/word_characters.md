---
id: kl.detail.word_characters
title: Polynomial characters of word stalks
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.notes.word_stalks
- kl.detail.graded_character
- kl.detail.word_standard_stalks
- kl.detail.coefficient_change
- kl.notes.graded_projective_free
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  declarations:
  - OAI.KLInvariance.TitsSpace.bottPolynomialStalkData
  - OAI.KLInvariance.TitsSpace.bottStalkCharacter
  - OAI.KLInvariance.TitsSpace.bottPolynomialStalk_finrank
  - OAI.KLInvariance.TitsSpace.bottStalkCharacter_hasSum
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1924
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottPolynomialStalkData
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1934
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkCharacter
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1938
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottPolynomialStalk_finrank
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1945
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkCharacter_hasSum
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the gradings, scalar actions, coefficient variables and formal polynomial
    conclusions explicit?
  verdict: Read the actual polynomial coefficient transport, Graded.character definition
    and Hilbert interpretation. Defined the coefficient variables, formal character
    variable and real evaluation parameter separately, with finite homogeneous bases
    belonging to the image stalk.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Polynomial characters of word stalks

Fix a finite-generator Coxeter system and a finite basis indexed by \(\sigma\) of its extended real realization \(V\). Put
\[
A=\operatorname{Sym}_{\mathbb R}(V),\qquad
P=\mathbb R[X_i:i\in\sigma],\qquad N=|\sigma|.
\]
The chosen basis gives a graded algebra isomorphism \(e:A\to P\). The variables \(X_i\) are coefficient-algebra generators of degree one.

We use \(q\) for a separate formal character variable, and \(t\in(0,1)\) for a real value at which such a polynomial is evaluated.

## The polynomial presentation of a stalk

For a word \(\mathbf t\) and \(x\in W\), let \(M_{\mathbf t}^x\) be the actual evaluation image stalk with its coordinatewise grading. Transport its coefficients through \(e\):
\[
p\cdot m=e^{-1}(p)m\qquad(p\in P).
\]
The underlying real vectors and homogeneous pieces are unchanged. This finite nonnegatively graded \(P\)-module is bottPolynomialStalkData.

The word-stalk theorem proves freeness over \(A\), and coefficient transport gives freeness over \(P\). The homogeneous-basis theorem therefore supplies a finite homogeneous \(P\)-basis \(b_j\) with nonnegative degrees \(d_j\).

## The character polynomial

Define
\[
C_x^{\mathbf t}(q)=\sum_j q^{d_j}\in\mathbb Z[q].
\]
This is bottStalkCharacter, obtained by applying Graded.character to the polynomial stalk data. Basis independence makes the polynomial intrinsic to that graded stalk.

Its coefficient at \(q^d\) counts homogeneous basis generators of degree \(d\), and \(C_x^{\mathbf t}(1)\) counts the number of basis vectors. For generator degrees \(0,1,1\), the polynomial is \(1+2q\).

## The Hilbert numerator

Write
\[
H_{\mathbf t,x}(t)
=\sum_{n\in\mathbb Z}
\dim_{\mathbb R}(M_{\mathbf t}^x)_n\,t^n.
\]
The [[node:kl.word.stalk_hilbert_formula|word-stalk Hilbert theorem]] proves convergence for \(0<t<1\) and gives
\[
H_{\mathbf t,x}(t)=C_x^{\mathbf t}(t)(1-t)^{-N}.
\]
Here \(C_x^{\mathbf t}(t)\) means the integer polynomial evaluated in \(\mathbb R\). The factor \((1-t)^{-N}\) counts all coefficient monomials multiplying each basis generator.

## Relation to a positive Hecke word

In the unnormalized Hecke module over \(\mathbb Z[q]\), let
\[
H_\varnothing=T_1,\qquad
H_{s\mathbf t}=(I+L_s(q))H_{\mathbf t}.
\]
The [[node:kl.detail.word_character_formula|word-character theorem]] identifies \(C_x^{\mathbf t}(q)\) with the coefficient of \(T_x\) in \(H_{\mathbf t}\). Its proof compares the graded kernel recursions with the positive Hecke-word recurrence.

The word characters then enter the decomposition of a word sheaf into shifted boundary models.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate objects.**

**OpenAI notes:** The normalization discussion identifies indecomposable boundary-sheaf characters with KL polynomials by the cited character theorem. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The word-stalk character is proved to equal a positive Hecke-word coefficient. Its R-convolution is then proved before model decomposition and cancellation. The separate boundary-character identification is exposed as StalkCharacterObligation. [IntegralPairings:289](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L289), [CharacterReciprocity:1134](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1134), [SheafMorphisms:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219), [BottSamelson:1924](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1924), [BottSamelson:1945](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1945), [IntegralPairings:104](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L104), [IntegralPairings:120](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L120), [CharacterReciprocity:915](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L915).

**Role in the proof:** The word formula and R-convolution describe the tensor word. A common decomposition into boundary models then supplies the character identities used in the cancellation argument.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottPolynomialStalkData`: [BottSamelson.lean:1924](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1924).

`OAI.KLInvariance.TitsSpace.bottStalkCharacter`: [BottSamelson.lean:1934](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1934).

`OAI.KLInvariance.TitsSpace.bottPolynomialStalk_finrank`: [BottSamelson.lean:1938](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1938).

`OAI.KLInvariance.TitsSpace.bottStalkCharacter_hasSum`: [BottSamelson.lean:1945](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1945).
