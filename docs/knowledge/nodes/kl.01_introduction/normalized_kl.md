---
id: kl.foundations.normalized_kl
title: Normalization of the ordinary R and KL polynomials
kind: definition
status: formalized
primary_topic: kl.01_introduction
topics:
- kl.01_introduction
uses:
- kl.foundations.interval
- kl.foundations.finite_intervals
lean:
  repository: openai-kl
  modules:
  - Model
  declarations:
  - OAI.KLInvariance.NormalizedKL
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Model:55
    format: lean-location
    note: OAI.KLInvariance.NormalizedKL
  - artifact: openai-kl-paper
    locator: 1. Introduction and conventions; sec:introduction
    format: section
    note: Chapter organization follows the paper; Lean references identify the precise
      formal statements.
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

# Normalization of the ordinary R and KL polynomials

A pair of families \((R_{x,y},P_{x,y})\) of polynomials in \(\mathbb Z[q]\) satisfies the following seven conditions.

1. \(R_{x,x}=1\).
2. \(R_{x,y}=0\) if \(x\not\le y\).
3. If a simple reflection \(s\) satisfies \(sy<y\), then
\[
R_{x,y}=
\begin{cases}
R_{sx,sy},&sx<x,\\
(q-1)R_{x,sy}+qR_{sx,sy},&sx>x.
\end{cases}
\]
4. \(P_{x,x}=1\).
5. \(P_{x,y}=0\) if \(x\not\le y\).
6. For \(x<y\), \(2\deg P_{x,y}<d(x,y)\).
7. For \(x\le y\), reciprocity holds:
\[
q^{d(x,y)}P_{x,y}(q^{-1})
=\sum_{z\in[x,y]}R_{x,z}(q)P_{z,y}(q).
\]

These are the ordinary equal-parameter polynomials. Polynomial reflection expresses the reciprocal identity in Lean; the degree condition there uses the natural-number degree convention for the zero polynomial.

## A rank-one calculation

Suppose \(y=sx\) and \(d(x,y)=1\). The ordinary R-recursion gives \(R_{x,y}=q-1\). The strict degree bound makes \(P_{x,y}\) a constant \(c\). Reciprocity reduces to
\[
qc=c+(q-1),
\]
because the interval has only its two endpoints. Hence \(c=1\).

The normalization therefore determines the simplest case before any geometry is used. For larger intervals, the new polynomial is recovered from previously determined upper-interval polynomials and a degree restriction. The main invariance theorem asserts that this resulting polynomial depends only on the interval, despite the simple-reflection choices used in the construction.

The coefficient ring is \(\mathbb Z[q]\). The strict degree condition is about the degree in \(q\), while several later formulas use the square parameter \(q=t^2\). Keeping these parameters separate prevents a factor-of-two error in the final rigidity argument.

## References

[1. Introduction and conventions](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization

The fields are `R_diagonal`, `R_zero`, `R_recursion`, `P_diagonal`, `P_zero`, `P_degree`, and `reciprocity`. They are conditions supplied when constructing the normalization data.

`OAI.KLInvariance.NormalizedKL`: [Model.lean:55](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Model.lean#L55).
