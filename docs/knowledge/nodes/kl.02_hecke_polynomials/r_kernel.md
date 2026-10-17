---
id: kl.detail.r_kernel
title: The reciprocal convolution identity for R-polynomials
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.detail.ordinary_r
- kl.definitions.bar_involution
- kl.foundations.finite_intervals
lean:
  repository: openai-kl
  modules:
  - OrdinaryR
  declarations:
  - OAI.KLInvariance.OrdinaryR.polynomial_kernel_reverse
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.OrdinaryR:245
    format: lean-location
    note: OAI.KLInvariance.OrdinaryR.polynomial_kernel_reverse
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

# The reciprocal convolution identity for R-polynomials

Write \(d(x,z)=\ell(z)-\ell(x)\) for comparable endpoints and
\[
\overline R_{x,z}(q)=q^{d(x,z)}R_{x,z}(q^{-1}).
\]
For every finite Bruhat interval,
\[
\sum_{x\leq z\leq y}\overline R_{x,z}(q)R_{z,y}(q)=\delta_{x,y}.
\]
Terms with noncomparable endpoints vanish. The degree bound on \(R\) ensures that the displayed reflection is a polynomial.

*Proof.*

The two bar transforms, with inverted parameter conventions, compose to the identity. Their triangular coefficients give the R-kernel convolution identity. Apply polynomial reflection to that identity and distribute reflection over the finite sum. For a nonzero summand, rank differences add:
\(d(x,z)+d(z,y)=d(x,y)\).
Reflection of a product therefore splits into the two appropriate reflected factors, and reflecting twice returns the original polynomial.

The identity supplies the cancellation used to prove that the defect in the canonical KL recursion is anti-reciprocal.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization



`OAI.KLInvariance.OrdinaryR.polynomial_kernel_reverse`: [OrdinaryR.lean:245](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L245).
