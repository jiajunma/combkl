---
id: kl.foundations.normalized_kl
title: The normalization data for ordinary R and KL polynomials
kind: definition
status: formalized
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.foundations.interval
- kl.foundations.finite_intervals
- kl.hecke.polynomial_reflection
lean:
  repository: openai-kl
  modules:
  - Model
  declarations:
  - OAI.KLInvariance.PolynomialFamilies
  - OAI.KLInvariance.NormalizedKL
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Model:48
    format: lean-location
    note: OAI.KLInvariance.PolynomialFamilies
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Model:55
    format: lean-location
    note: OAI.KLInvariance.NormalizedKL
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
  prompt: Does the exposition preserve the exact domain, degree conventions and source
    argument?
  verdict: Read all seven NormalizedKL fields and PolynomialFamilies. Preserved every-descent
    quantification, the natural degree convention, interval subtype sum and reflected
    polynomial form.
tags:
- Kazhdan-Lusztig
- Hecke
---

# The normalization data for ordinary R and KL polynomials

Fix a Coxeter system. A polynomial-family pair consists of two functions
\[
R,P:W\times W\longrightarrow\mathbb Z[q].
\]
For comparable endpoints put \(d(x,y)=\ell(y)-\ell(x)\). The predicate NormalizedKL says that this pair has the following seven properties.

| Lean field | Mathematical condition |
|---|---|
| `R_diagonal` | \(R_{x,x}=1\) for every \(x\). |
| `R_zero` | \(R_{x,y}=0\) whenever \(x\not\le y\). |
| `R_recursion` | The ordinary left-descent recurrence below holds for every left descent of the upper endpoint. |
| `P_diagonal` | \(P_{x,x}=1\) for every \(x\). |
| `P_zero` | \(P_{x,y}=0\) whenever \(x\not\le y\). |
| `P_degree` | If \(x<y\), then \(2\,\operatorname{natDegree}(P_{x,y})<d(x,y)\). |
| `reciprocity` | The reflected P-value equals its finite R-weighted interval sum. |

## The R recurrence

For every simple reflection \(s\) with \(sy<y\),
\[
R_{x,y}=
\begin{cases}
R_{sx,sy},&sx<x,\\
(q-1)R_{x,sy}+qR_{sx,sy},&sx>x.
\end{cases}
\]
The quantifier over \(s\) includes every left descent of \(y\). The normalized pair thus records one family satisfying all these equations.

## The degree and reciprocity conditions

The degree uses natural degree, with \(\operatorname{natDegree}(0)=0\). On a strict interval, \(d(x,y)>0\), so the zero polynomial satisfies the strict bound.

For each \(x\le y\), reciprocity is
\[
\operatorname{reflect}_{d(x,y)}P_{x,y}
=\sum_{z\in[x,y]}R_{x,z}P_{z,y}.
\]
The interval consists of elements \(z\) equipped with \(x\le z\le y\). Its finiteness makes the source's finitely supported sum an ordinary finite sum.

The strict bound on a nondiagonal pair implies the weak bound
\(\operatorname{natDegree}(P_{x,y})\le d(x,y)\). On the diagonal \(P_{x,x}=1\) and \(d=0\), so the same weak bound holds. Therefore the reflected expression can be written as
\[
q^{d(x,y)}P_{x,y}(q^{-1}).
\]
The formal polynomial equation is the reflection identity; evaluation at inverse powers is its bounded-degree interpretation.

## The two-element interval

For \([1,s]\), the R recurrence gives \(R_{1,s}=q-1\). The strict degree bound makes \(P_{1,s}\) a constant \(c\). Reciprocity becomes
\[
qc=c+(q-1).
\]
Comparing constant coefficients gives \(c=1\), and comparing degree one gives the same value.

The [[node:kl.foundations.canonical_kl|construction theorem]] supplies every field using the ordinary R-family and the recursive P-family. The [[node:kl.hecke.normalization_unique|uniqueness theorem]] proves that these conditions determine the pair.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.PolynomialFamilies`: [Model.lean:48](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Model.lean#L48).

`OAI.KLInvariance.NormalizedKL`: [Model.lean:55](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Model.lean#L55).
