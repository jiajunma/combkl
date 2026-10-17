---
id: kl.main.kl_finite
title: KL invariance for finite-generator Coxeter systems
kind: theorem
status: proved
primary_topic: kl.09_combinatorial_invariance
topics:
- kl.09_combinatorial_invariance
uses:
- kl.comparison.rtilde_invariance
- kl.foundations.scaled_kl
- kl.comparison.reciprocal_rigidity
- kl.foundations.rank_preservation
lean:
  repository: openai-kl
  modules:
  - Invariance
  declarations:
  - OAI.KLInvariance.BruhatGraph.klPolynomial_invariance_finite
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Invariance:427
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.klPolynomial_invariance_finite
  - artifact: openai-kl-paper
    locator: 6. Reciprocity and simultaneous induction; sec:induction
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
- induction
---

# KL invariance for finite-generator Coxeter systems

If the simple-generator sets of two Coxeter systems are finite and \([u,b]\simeq[u',b']\), then
\[
P_{u,b}(q)=P'_{u',b'}(q).
\]
The groups themselves may be infinite.

*Proof.*

[[node:kl.comparison.rtilde_invariance]] applied to every subinterval identifies the transfer matrices. Normalized KL reciprocity supplies the exact comparison relation in each system.

Induct on the rank difference from the bottom to the fixed top. Corresponding polynomials at strictly higher vertices already agree. At the bottom, the two comparisons leave only a normalized difference and its reciprocal. The two directions force reciprocal equality; the strict half-degree bound and [[node:kl.comparison.reciprocal_rigidity]] make the difference zero.

## The final degree argument

Let
\[
\Delta(t)=t^{-d}\bigl(P_{u,b}(t^2)-P'_{u',b'}(t^2)\bigr).
\]
Once the higher polynomials agree, the two reciprocal comparisons give
\(\Delta(t)=\Delta(t^{-1})\) on \(0<t<1\).

Every exponent on the left is of the form \(2j-d<0\), by the strict KL degree bound. Every exponent of its reciprocal is positive. A Laurent polynomial supported in strictly negative exponents cannot equal one supported in strictly positive exponents unless both are zero. Therefore the two ordinary KL polynomials agree.

The strict degree bound is applied here to the canonical polynomials. Earlier R-tilde comparison used actual sheaf characters and their reciprocity without making this identification.

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.klPolynomial_invariance_finite`: [Invariance.lean:427](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L427).
