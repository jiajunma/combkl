---
id: kl.sheaves.hilbert_free
title: The Hilbert series of a finite graded free module
kind: theorem
status: proved
primary_topic: kl.03_realizations_and_grading
topics:
- kl.03_realizations_and_grading
uses: []
lean:
  repository: openai-kl
  modules:
  - HilbertSeries
  declarations:
  - OAI.KLInvariance.Hilbert.hasSum_homogeneous_basis
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:321
    format: lean-location
    note: OAI.KLInvariance.Hilbert.hasSum_homogeneous_basis
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
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
- background
---

# The Hilbert series of a finite graded free module

Let \(A=k[x_1,\ldots,x_N]\), with every variable in degree one. Suppose that a finite graded free \(A\)-module \(M\) has a homogeneous basis \(e_i\) of degrees \(d_i\). For \(0<q<1\),
\[
\sum_{n\in\mathbb Z}\dim_k M_n\,q^n
=\frac{\sum_i q^{d_i}}{(1-q)^N}.
\]

*Proof.*

First sum the geometric series over monomials, inducting on the number of variables, to compute the Hilbert series of the polynomial ring. Each graded piece of a shifted free module decomposes into the corresponding shifted polynomial pieces. The graded linear equivalence supplied by a homogeneous basis then reduces the formula to a finite sum of shifted free-module formulas.

## Reading degrees from the series

Let \(A=k[x,y]\), and take a free module with generators in degrees zero and one. Its Hilbert series is
\[
\frac{1+q}{(1-q)^2}.
\]
The coefficient of \(q^n\) counts a copy of \(A_n\) and, for \(n\ge1\), a copy of \(A_{n-1}\). Multiplying by \((1-q)^2\) removes the polynomial-ring contribution and leaves the generator-degree polynomial \(1+q\).

This normalization explains the factor \((1-q)^N\) in the global state. It does not imply that every intermediate kernel is free. For a general finite graded module the Hilbert series still converges at \(0<q<1\), and can be compared before a free basis has been established.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.Hilbert.hasSum_homogeneous_basis`: [HilbertSeries.lean:321](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L321).
