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
- kl.foundations.normalized_kl
lean:
  repository: openai-kl
  modules:
  - Dihedral
  declarations:
  - OAI.KLInvariance.scaledKL
  - OAI.KLInvariance.scaledKL_reciprocity
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:730
    format: lean-location
    note: OAI.KLInvariance.scaledKL
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
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- introduction
---

# Normalized KL reciprocity in the square parameter

For a nonzero field element \(t\), define
\[
p_x(t)=t^{\ell(x)-\ell(b)}P_{x,b}(t^2).
\]
Then
\[
p_x(t)=\sum_{z\in[x,b]}
 \widetilde R_{x,z}(t^{-1}-t)\,p_z(t^{-1}).
\]
Over the real interval \(0<t<1\), the common transfer coefficient is \(T=t^{-1}-t>0\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Equivalent parameter conventions.**

**OpenAI notes:** The comparison uses \(0<q<1\), scale \(q^{-d/2}(1-q)^N\), and transfer coefficient \(q^{-1/2}-q^{1/2}\). [eq:state](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L243), [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275).

**Lean (primary):** The comparison uses \(0<t<1\) and substitutes \(q=t^2\). Its scale is \(t^{-d}(1-t^2)^N\) and its transfer coefficient is \(t^{-1}-t\). [Dihedral:730](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L730), [PositiveTransfer:591](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L591), [PositiveTransfer:621](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L621).

**How to read this entry:** The substitution \(q=t^2\) identifies the two normalizations. Linear root labels have degree one throughout the calculation.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Start from polynomial reciprocity

Let \(d(x,b)=\ell(b)-\ell(x)\) and \(v\ne0\). The canonical identity, evaluated at \(q=v^2\), is
\[
v^{2d(x,b)}P_{x,b}(v^{-2})
=\sum_{x\le z\le b}R_{x,z}(v^2)P_{z,b}(v^2).
\]
The degree bound ensures that evaluating polynomial reflection gives exactly the expression on the left.

### Step 2. Multiply by the scale and identify the left side

Multiply by \(v^{-d(x,b)}\). The left side becomes
\[
v^{d(x,b)}P_{x,b}(v^{-2})=k_x(v^{-1}),
\]
where \(k_x(v)=v^{-d(x,b)}P_{x,b}(v^2)\).

### Step 3. Simplify each summand on the right

Use square-parameter normalization
\(R_{x,z}(v^2)=v^{d(x,z)}\widetilde R_{x,z}(v-v^{-1})\).
Rank additivity gives \(d(x,b)=d(x,z)+d(z,b)\). Therefore
\[
v^{-d(x,b)}R_{x,z}(v^2)P_{z,b}(v^2)
=\widetilde R_{x,z}(v-v^{-1})\,v^{-d(z,b)}P_{z,b}(v^2).
\]
The final factor is \(k_z(v)\). We have proved
\[
k_x(v^{-1})=\sum_z\widetilde R_{x,z}(v-v^{-1})k_z(v).
\]

### Step 4. Invert the parameter

Replace \(v\) by \(t^{-1}\), which is nonzero whenever \(t\ne0\). Then \(v-v^{-1}=t^{-1}-t\), and
\[
k_x(t)=\sum_z\widetilde R_{x,z}(t^{-1}-t)k_z(t^{-1}).
\]
For \(0<t<1\), this parameter is positive. The positive sign comes from applying reciprocity at the inverted parameter; it is not an independent change in the definition of \(\widetilde R\).

## References

[1. Introduction and conventions](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization

`OAI.KLInvariance.scaledKL`: [Dihedral.lean:730](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L730).

`OAI.KLInvariance.scaledKL_reciprocity`: [Dihedral.lean:790](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L790).
