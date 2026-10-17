---
id: kl.comparison.positive_transfer
title: Elementary edge transfers
kind: definition
status: formalized
primary_topic: kl.08_comparison_and_freeness
topics:
- kl.08_comparison_and_freeness
uses: []
lean:
  repository: openai-kl
  modules:
  - Comparison
  declarations:
  - OAI.KLInvariance.Comparison.transfer
  - OAI.KLInvariance.Comparison.transfer_monotone
  - OAI.KLInvariance.Comparison.transfer_injective
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Comparison:74
    format: lean-location
    note: OAI.KLInvariance.Comparison.transfer
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Comparison:77
    format: lean-location
    note: OAI.KLInvariance.Comparison.transfer_monotone
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Comparison:85
    format: lean-location
    note: OAI.KLInvariance.Comparison.transfer_injective
  - artifact: openai-kl-paper
    locator: 6. Reciprocity and simultaneous induction; sec:induction
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
- induction
---

# Elementary edge transfers

For vertices \(x,y\), a real number \(T\), and a vector \(v\), define
\[
(\tau_{x,y,T}v)_z=v_z+\mathbf 1_{\{z=x\}}T v_y.
\]
If \(T\ge0\), this map is monotone for the coordinatewise order. If \(x\ne y\), it is injective.

Monotonicity follows because addition and multiplication by a nonnegative scalar preserve order. For injectivity, first recover \(v_y\) from its unchanged coordinate, then subtract \(Tv_y\) at \(x\); every other coordinate is unchanged.

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.Comparison.transfer`: [Comparison.lean:74](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L74).

`OAI.KLInvariance.Comparison.transfer_monotone`: [Comparison.lean:77](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L77).

`OAI.KLInvariance.Comparison.transfer_injective`: [Comparison.lean:85](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L85).
