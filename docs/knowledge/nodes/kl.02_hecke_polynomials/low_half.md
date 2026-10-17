---
id: kl.foundations.low_half
title: The strict lower-half truncation
kind: definition
status: formalized
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses: []
lean:
  repository: openai-kl
  modules:
  - CanonicalKL
  declarations:
  - OAI.KLInvariance.CanonicalP.lowPart
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:23
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.lowPart
  - artifact: openai-kl-paper
    locator: 1. Introduction and conventions; sec:introduction
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  definition: accepted
  proof: not_applicable
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

# The strict lower-half truncation

For \(d\in\mathbb N\) and \(p(q)=\sum_n a_nq^n\in\mathbb Z[q]\), set
\[
\operatorname{low}_d(p)=\sum_{2n<d}a_nq^n.
\]
When \(d>0\), this polynomial satisfies the strict half-degree bound. If the \(d\)-reflection of \(p\) is \(-p\), the negative lower-half truncation supplies the low-degree solution to the reciprocal defect equation used in the canonical KL recursion.

## Solving a reciprocal defect

At a nontrivial interval, write the contribution from the already constructed upper terms as
\[
D(q)=\sum_{x<z\le y}R_{x,z}(q)P_{z,y}(q).
\]
The reciprocal equation for the unknown polynomial is
\[
q^dP(q^{-1})=P(q)+D(q).
\]
The construction proves the required anti-reciprocity of the defect and chooses \(P=-\operatorname{low}_d(D)\).

As a polynomial calculation, take \(d=3\) and
\(D=q^3+2q^2-2q-1\). Its strict lower half is \(-1-2q\), so \(P=1+2q\). Directly,
\[
q^3P(q^{-1})=q^3+2q^2=P(q)+D(q).
\]
This calculation illustrates the truncation operation; it does not assert that this chosen defect comes from a particular Bruhat interval.

## References

[1. Introduction and conventions](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization

`OAI.KLInvariance.CanonicalP.lowPart`: [CanonicalKL.lean:23](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L23).
