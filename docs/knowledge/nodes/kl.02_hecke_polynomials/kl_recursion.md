---
id: kl.detail.kl_recursion
title: Why the lower-half construction satisfies reciprocity
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.detail.kl_defect
- kl.detail.r_kernel
- kl.foundations.low_half
lean:
  repository: openai-kl
  modules:
  - CanonicalKL
  declarations:
  - OAI.KLInvariance.CanonicalP.lowPart_solution
  - OAI.KLInvariance.CanonicalP.polynomial_reciprocity
  - OAI.KLInvariance.CanonicalP.polynomial_strict_degree
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:43
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.lowPart_solution
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:162
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.polynomial_reciprocity
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:104
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.polynomial_strict_degree
  - artifact: openai-kl-paper
    locator: Related paper context; sec:introduction
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- hecke_polynomials
---

# Why the lower-half construction satisfies reciprocity

The recursively constructed family satisfies
\[
q^{d(x,y)}P_{x,y}(q^{-1})
=\sum_{x\leq z\leq y}R_{x,z}(q)P_{z,y}(q),
\qquad
2\deg P_{x,y}<d(x,y)\quad(x<y).
\]

*Proof.*

Induct on \(d=d(x,y)\). The diagonal case is immediate. For \(x<y\), expand the reflection of the defect using the already established reciprocity equations on \([z,y]\). Interchange the finite sums and apply reciprocal R-kernel cancellation. The result is
\(\operatorname{reflect}_d D_{x,y}=-D_{x,y}\).

For any anti-reciprocal polynomial \(D\), coefficient comparison gives
\[
\operatorname{reflect}_d(-\operatorname{low}_dD)
=-\operatorname{low}_dD+D.
\]
Below the middle degree this uses the retained coefficients; above the middle it uses their negatives under reflection. When \(d\) is even, the middle coefficient vanishes because it equals its own negative over \(\mathbb Z\). Substituting the recursive definition proves reciprocity. The strict degree bound follows from the truncation itself.

This separates the construction of \(P\) from the later uniqueness argument that identifies it with the selected canonical KL family.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization



`OAI.KLInvariance.CanonicalP.lowPart_solution`: [CanonicalKL.lean:43](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L43).

`OAI.KLInvariance.CanonicalP.polynomial_reciprocity`: [CanonicalKL.lean:162](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L162).

`OAI.KLInvariance.CanonicalP.polynomial_strict_degree`: [CanonicalKL.lean:104](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L104).
