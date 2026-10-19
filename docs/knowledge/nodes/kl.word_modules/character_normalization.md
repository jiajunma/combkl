---
id: kl.word.character_normalization
title: Zero, top and empty-word character values
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.detail.word_characters
- kl.word.stalk_hilbert_formula
- kl.word.top_stalk
- kl.algebra.hilbert_numerators
- kl.algebra.polynomial_hilbert
- kl.word.weight_support
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.bottStalkCharacter_zero
  - OAI.KLInvariance.TitsSpace.bottTopPolynomialEquiv
  - OAI.KLInvariance.TitsSpace.bottTopPolynomialEquiv_homogeneous
  - OAI.KLInvariance.TitsSpace.bottStalkCharacter_top
  - OAI.KLInvariance.TitsSpace.bottStalkCharacter_nil
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:237
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkCharacter_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:248
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottTopPolynomialEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:254
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottTopPolynomialEquiv_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:260
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkCharacter_top
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:279
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkCharacter_nil
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the gradings, scalar actions, coefficient variables and formal polynomial
    conclusions explicit?
  verdict: Read the zero numerator, top polynomial equivalence, homogeneous dimensions
    and empty-word branch proof. Used Hilbert numerator uniqueness as in the source
    and stated the reducedness needed for top/support normalization.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Zero, top and empty-word character values

Fix a finite-generator Coxeter system and a finite basis of its extended realization. Let \(N\) be the size of this basis.

If a word stalk \(M_{\mathbf t}^x\) is zero, then \(C_x^{\mathbf t}(q)=0\).
If \(\mathbf t\) is reduced with product \(b\), then
\[
C_b^{\mathbf t}(q)=1.
\]
In particular, the empty-word values are
\[
C_x^\varnothing(q)=
\begin{cases}
1,&x=1,\\
0,&x\ne1.
\end{cases}
\]
For a reduced word with product \(b\), weights \(x\not\le b\) have zero character.

*Proof.*

### Step 1. Compute the character of a zero stalk

Every homogeneous piece of a zero stalk has dimension zero, so its Hilbert sum is zero. The [[node:kl.word.stalk_hilbert_formula|word-stalk Hilbert formula]] expresses that same sum as
\(C_x^{\mathbf t}(t)(1-t)^{-N}\) for every \(0<t<1\).

The zero polynomial also represents it with this common factor. Since
\((1-t)^{-N}\ne0\), uniqueness of the [[node:kl.algebra.hilbert_numerators|polynomial Hilbert numerator]] gives
\(C_x^{\mathbf t}=0\).

### Step 2. Identify the top stalk with the polynomial coefficient module

For a reduced word, the [[node:kl.word.top_stalk|top-stalk theorem]] gives a degree-preserving real-linear isomorphism
\[
M_{\mathbf t}^{b}\xrightarrow{\sim}A.
\]
Composing with the coefficient isomorphism \(A\to P=\mathbb R[X_i]\) gives bottTopPolynomialEquiv.

It induces isomorphisms of the homogeneous pieces, so
\[
\dim_{\mathbb R}(M_{\mathbf t}^{b})_n=\dim_{\mathbb R}P_n
\]
for every integer \(n\).

### Step 3. Recover the top numerator

The coefficient Hilbert series has sum \((1-t)^{-N}\). Thus the top stalk's dimension sequence has numerator \(1\).

The [[node:kl.word.stalk_hilbert_formula|word-stalk Hilbert formula]] gives numerator \(C_b^{\mathbf t}\) for the same sequence and factor. [[node:kl.algebra.hilbert_numerators|Polynomial numerator uniqueness]] therefore gives \(C_b^{\mathbf t}=1\).

### Step 4. Specialize to the empty word and to absent weights

The empty word is reduced, with product \(1\), so Step 3 gives its character \(1\) at weight \(1\). Every other empty-word stalk is zero, giving the other values by Step 1.

More generally, reduced-word support gives a zero stalk at each \(x\not\le b\), so Step 1 proves the final assertion.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottStalkCharacter_zero`: [IntegralPairings.lean:237](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L237).

`OAI.KLInvariance.TitsSpace.bottTopPolynomialEquiv`: [IntegralPairings.lean:248](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L248).

`OAI.KLInvariance.TitsSpace.bottTopPolynomialEquiv_homogeneous`: [IntegralPairings.lean:254](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L254).

`OAI.KLInvariance.TitsSpace.bottStalkCharacter_top`: [IntegralPairings.lean:260](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L260).

`OAI.KLInvariance.TitsSpace.bottStalkCharacter_nil`: [IntegralPairings.lean:279](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L279).
