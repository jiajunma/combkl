---
id: kl.comparison.global_comparison
title: The transported comparison for actual characters
kind: theorem
status: proved
primary_topic: kl.08_comparison_and_freeness
topics:
- kl.08_comparison_and_freeness
uses:
- kl.comparison.edge_increment
- kl.paths.dyer_paths
- kl.duality.actual_character_reciprocity
- kl.detail.schedule_comparison
lean:
  repository: openai-kl
  modules:
  - SimultaneousInvariance
  declarations:
  - OAI.KLInvariance.BruhatGraph.actual_comparison_of_upper_freeness
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SimultaneousInvariance:264
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.actual_comparison_of_upper_freeness
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

# The transported comparison for actual characters

Assume that every upper-endpoint kernel needed during the schedule is free. Let \(c_x(t)\) be the normalized square-parameter value of the actual boundary-sheaf character. Then, coordinatewise,
\[
c(t)\le \widetilde R'(t^{-1}-t)c(t^{-1}),
\]
where the matrix comes from the target system.

*Proof.*

Compose [[node:kl.comparison.edge_increment]] along the schedule. Monotonicity propagates every bound to the final state. The actual kernel and stalk character formulas identify the full-condition and empty-condition states with \(c(t^{-1})\) and \(c(t)\).

Finally, [[node:kl.paths.dyer_paths]] identifies the transfer product with the target system's R-tilde matrix.

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.actual_comparison_of_upper_freeness`: [SimultaneousInvariance.lean:264](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SimultaneousInvariance.lean#L264).
