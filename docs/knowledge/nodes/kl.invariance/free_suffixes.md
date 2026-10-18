---
id: kl.comparison.free_suffixes
title: Freeness of all terminal kernels in a transported schedule
kind: definition
status: formalized
primary_topic: kl.invariance
topics:
- kl.invariance
uses:
- kl.sheaves.upward_kernel
- kl.foundations.interval
lean:
  repository: openai-kl
  modules:
  - SimultaneousInvariance
  declarations:
  - OAI.KLInvariance.BruhatGraph.FreeSuffixes
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SimultaneousInvariance:118
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.FreeSuffixes
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

# Freeness of all terminal kernels in a transported schedule

For an interval isomorphism and the edge-processing order transported from the target reflection order, terminal-kernel freeness means the following:

For every suffix of the processing order and every vertex \(x\) in the interval, retain exactly the upward conditions at \(x\) belonging to that suffix. The resulting module \(L_x(F)\) is free over the coefficient polynomial ring.

The condition quantifies every vertex and every suffix. It is therefore compatible with induction through smaller upper intervals.

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.FreeSuffixes`: [SimultaneousInvariance.lean:118](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SimultaneousInvariance.lean#L118).
