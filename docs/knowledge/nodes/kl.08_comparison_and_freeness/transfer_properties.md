---
id: kl.detail.transfer_properties
title: Monotonicity and injectivity of elementary transfers
kind: theorem
status: proved
primary_topic: kl.08_comparison_and_freeness
topics:
- kl.08_comparison_and_freeness
uses:
- kl.comparison.positive_transfer
lean:
  repository: openai-kl
  modules:
  - Comparison
  declarations:
  - OAI.KLInvariance.Comparison.transfer_monotone
  - OAI.KLInvariance.Comparison.transfer_injective
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Comparison:77
    format: lean-location
    note: OAI.KLInvariance.Comparison.transfer_monotone
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Comparison:85
    format: lean-location
    note: OAI.KLInvariance.Comparison.transfer_injective
  - artifact: openai-kl-paper
    locator: Related paper context; sec:induction
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
- comparison_and_freeness
---

# Monotonicity and injectivity of elementary transfers

For \(x\ne y\), define \(\tau_{x,y,T}=1+TE_{xy}\) on real vectors indexed by vertices. Then:

- If \(T\geq0\), \(\tau_{x,y,T}\) preserves the coordinatewise order.
- For every real \(T\), \(\tau_{x,y,T}\) is injective; its inverse is \(1-TE_{xy}\).

*Proof.*

Only coordinate \(x\) changes, by adding \(T v_y\). If \(v\leq w\) and \(T\geq0\), both the original \(x\)-coordinate and the added contribution are ordered, proving monotonicity.

Since \(x\ne y\), coordinate \(y\) is unchanged. Recover it first, then subtract \(T v_y\) from coordinate \(x\). All other coordinates are unchanged. Equivalently \(E_{xy}^2=0\), so
\((1-TE_{xy})(1+TE_{xy})=1\).

These two properties serve different purposes: monotonicity propagates one-sided inequalities through a schedule, while injectivity permits equality to be traced backward from an exact endpoint.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization



`OAI.KLInvariance.Comparison.transfer_monotone`: [Comparison.lean:77](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L77).

`OAI.KLInvariance.Comparison.transfer_injective`: [Comparison.lean:85](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L85).
