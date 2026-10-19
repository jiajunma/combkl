---
id: kl.foundations.scaled_kl
title: Normalized KL reciprocity in the square parameter
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.foundations.rtilde
- kl.foundations.canonical_kl
- kl.hecke.recursive_p_degree
- kl.hecke.scaled_polynomials
- kl.hecke.polynomial_reflection
lean:
  repository: openai-kl
  modules:
  - Dihedral
  declarations:
  - OAI.KLInvariance.scaledKL_reciprocity_inverse
  - OAI.KLInvariance.scaledKL_reciprocity
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:737
    format: lean-location
    note: OAI.KLInvariance.scaledKL_reciprocity_inverse
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:790
    format: lean-location
    note: OAI.KLInvariance.scaledKL_reciprocity
  - artifact: openai-kl-paper
    locator: 1. Introduction and conventions; sec:introduction
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the exact domain, degree conventions and source
    argument?
  verdict: Read both scaledKL reciprocity proofs. Checked weak-degree reflection evaluation
    at v squared, finite sums, rank additivity, exact exponent cancellation and the
    final inverse substitution.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Normalized KL reciprocity in the square parameter

Let \(t\ne0\) lie in a field and let \(x\le b\). Write
\[
p_x(t)=t^{-d(x,b)}P_{x,b}(t^2).
\]
Then
\[
p_x(t)=\sum_{z\in[x,b]}
 \widetilde R_{x,z}(t^{-1}-t)\,p_z(t^{-1}).
\]
For real \(0<t<1\), the parameter \(t^{-1}-t\) is positive.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Equivalent parameter conventions.**

**OpenAI notes:** The comparison uses \(0<q<1\), scale \(q^{-d/2}(1-q)^N\), and transfer coefficient \(q^{-1/2}-q^{1/2}\). [eq:state](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L243), [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275).

**Lean (primary):** The comparison uses \(0<t<1\) and substitutes \(q=t^2\). Its scale is \(t^{-d}(1-t^2)^N\) and its transfer coefficient is \(t^{-1}-t\). [Dihedral:730](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L730), [PositiveTransfer:591](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L591), [PositiveTransfer:621](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L621), [EdgeLocalization:377](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L377), [EdgeLocalization:423](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L423).

**Role in the proof:** The substitution \(q=t^2\) identifies the two normalizations. Linear root labels have degree one throughout the calculation.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Evaluate the canonical reciprocity equation

Take a nonzero field element \(v\). The canonical normalization gives
\[
\operatorname{reflect}_{d(x,b)}P_{x,b}
=\sum_{z\in[x,b]}R_{x,z}P_{z,b}.
\]
The canonical P-value equals the recursive P-value, whose weak degree bound is at most \(d(x,b)\). The bounded reflection evaluation theorem therefore applies at the unit \(v^2\), giving
\[
v^{2d(x,b)}P_{x,b}(v^{-2})
=\sum_{z\in[x,b]}R_{x,z}(v^2)P_{z,b}(v^2).
\]
Evaluation preserves the finite sum and each product.

### Step 2. Multiply by the scale

Multiply both sides by \(v^{-d(x,b)}\). On the left the exponents add:
\[
v^{-d(x,b)}v^{2d(x,b)}P_{x,b}(v^{-2})
=v^{d(x,b)}P_{x,b}(v^{-2})
=p_x(v^{-1}).
\]
The final equality uses \((v^{-1})^{-d}=v^d\) and \((v^{-1})^2=v^{-2}\).

### Step 3. Convert each R-factor and combine the powers

For each \(x\le z\le b\), the [[node:kl.foundations.rtilde|square-parameter normalization]] gives
\[
R_{x,z}(v^2)=v^{d(x,z)}
 \widetilde R_{x,z}(v-v^{-1}).
\]
Length differences add:
\(d(x,b)=d(x,z)+d(z,b)\).
Thus the corresponding scaled summand becomes
\[
\begin{aligned}
v^{-d(x,b)}R_{x,z}(v^2)P_{z,b}(v^2)
&=\widetilde R_{x,z}(v-v^{-1})
  v^{-d(x,b)+d(x,z)}P_{z,b}(v^2)\\
&=\widetilde R_{x,z}(v-v^{-1})\,p_z(v).
\end{aligned}
\]
This proves the inverse-direction formula
\[
p_x(v^{-1})=\sum_z\widetilde R_{x,z}(v-v^{-1})p_z(v).
\]

### Step 4. Substitute the inverse parameter

Set \(v=t^{-1}\), which is nonzero. Then \(v^{-1}=t\) and \(v-v^{-1}=t^{-1}-t\). Substitution gives the stated formula.

For real \(0<t<1\), division of \(t<1\) by \(t>0\) gives \(1<t^{-1}\). Hence \(t^{-1}>1>t\), proving \(t^{-1}-t>0\).

### Step 5. Evaluate the rank-one example

For \([1,s]\), the scaled values are \(p_1(t)=t^{-1}\), \(p_s(t)=1\), and \(\widetilde R_{1,s}(T)=T\). The equation reads
\[
t^{-1}=t+(t^{-1}-t)\cdot1.
\]
Its two terms correspond to the bottom and top vertices in the reciprocal interval sum.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.scaledKL_reciprocity_inverse`: [Dihedral.lean:737](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L737).

`OAI.KLInvariance.scaledKL_reciprocity`: [Dihedral.lean:790](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L790).
