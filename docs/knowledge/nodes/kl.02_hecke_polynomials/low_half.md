---
id: kl.foundations.low_half
title: The strict lower-half truncation
kind: definition
status: formalized
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.hecke.polynomial_reflection
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
  prompt: Does the exposition preserve the exact domain, degree conventions and source
    argument?
  verdict: Read lowPart and its finite range. Explained parity, d=0, the strict coefficient
    cutoff, the minus sign in the candidate and an explicit polynomial example.
tags:
- Kazhdan-Lusztig
- Hecke
---

# The strict lower-half truncation

For \(d\in\mathbb N\) and \(p(q)=\sum_{n\ge0}a_nq^n\in\mathbb Z[q]\), define
\[
\operatorname{low}_d(p)=\sum_{2n<d}a_nq^n.
\]
The inequality is strict. It retains the exponents below the midpoint \(d/2\).

Lean writes the finite index set as
\[
0\le n<\left\lfloor\frac{d+1}{2}\right\rfloor.
\]
For even \(d=2m\), the allowed exponents are \(0,\ldots,m-1\). For odd \(d=2m+1\), they are \(0,\ldots,m\). At \(d=0\), the sum is empty and the result is zero.

For \(p=4-3q+2q^2+7q^3\),
\[
\operatorname{low}_3p=4-3q,\qquad
\operatorname{low}_4p=4-3q,\qquad
\operatorname{low}_5p=4-3q+2q^2.
\]
The operation discards coefficients according to the chosen bound \(d\), independently of their signs.

## The low coefficients of a reciprocity equation

Suppose a polynomial \(P\) is supported strictly below \(d/2\), and
\[
\operatorname{reflect}_dP=P+D.
\]
Every term of the reflected polynomial has degree strictly above \(d/2\). Therefore the coefficient of degree \(n\) with \(2n<d\) on the left is zero. The right coefficient is \(P_n+D_n\), so
\(P_n=-D_n\).

This determines the candidate
\[
P=-\operatorname{low}_dD.
\]
The [[node:kl.hecke.low_part_solution|anti-reciprocal solution theorem]] verifies that this candidate satisfies the whole equation when \(\operatorname{reflect}_dD=-D\).

For the polynomial example \(d=3\),
\(D=q^3+2q^2-2q-1\),
the candidate is \(P=1+2q\). Direct calculation gives
\[
\operatorname{reflect}_3P=q^3+2q^2=P+D.
\]

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.CanonicalP.lowPart`: [CanonicalKL.lean:23](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L23).
