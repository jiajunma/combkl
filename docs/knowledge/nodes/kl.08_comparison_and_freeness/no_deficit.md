---
id: kl.comparison.no_deficit
title: Endpoint equality forces equality at every transfer step
kind: theorem
status: proved
primary_topic: kl.08_comparison_and_freeness
topics:
- kl.08_comparison_and_freeness
uses:
- kl.comparison.positive_transfer
- kl.detail.transfer_properties
lean:
  repository: openai-kl
  modules:
  - Comparison
  declarations:
  - OAI.KLInvariance.Comparison.every_step_eq_of_endpoint_eq
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Comparison:119
    format: lean-location
    note: OAI.KLInvariance.Comparison.every_step_eq_of_endpoint_eq
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

# Endpoint equality forces equality at every transfer step

Suppose \(T\ge0\), the endpoints satisfy \(x_k\ne y_k\), and
\[
D_{k+1}\le\tau_{x_k,y_k,T}(D_k).
\]
If the final state equals the exact composite of these transfers applied to \(D_0\), every step is an equality.

*Proof.*

Induct on the number of steps. Monotonicity puts each actual intermediate state below its ideal counterpart. At the last step, final equality traps the actual transfer between equal vectors, so that step is exact. Injectivity of the last transfer then identifies the preceding actual and ideal states. Apply induction.

## The accumulated-deficit identity

Writing \(M_k=1+T E_{x_ky_k}\), define the actual deficit
\[
\delta_k=M_kD_{k-1}-D_k\ge0.
\]
Successive substitution gives
\[
M_r\cdots M_1D_0-D_r
=\sum_{k=1}^r M_r\cdots M_{k+1}\delta_k.
\]
Each factor is nonnegative with diagonal one. A positive coordinate of a deficit remains positive in its corresponding summand, so it cannot disappear through subsequent nonnegative transfers.

At an edge, the deficit is a positive normalization factor times the Hilbert value of \((f_eJ_e)/I_e\). A nonzero graded quotient has a positive value at \(0<q<1\). Consequently a vanishing deficit proves equality of actual edge images, including possible differences supported in higher codimension.

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.Comparison.every_step_eq_of_endpoint_eq`: [Comparison.lean:119](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L119).
