---
id: kl.comparison.edge_increment
title: The uniform positive bound for a single edge increment
kind: theorem
status: proved
primary_topic: kl.08_comparison_and_freeness
topics:
- kl.08_comparison_and_freeness
uses:
- kl.local.edge_inclusion
- kl.comparison.normalized_kernel
- kl.detail.kernel_exact_sequence
- kl.detail.edge_images
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.BruhatGraph.normalized_edge_increment_le
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:621
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.normalized_edge_increment_le
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

# The uniform positive bound for a single edge increment

Under the hypotheses of [[node:kl.local.edge_inclusion]], removing the condition at \(e:x\to y\) changes only the \(x\) coordinate, and
\[
D_x^{\mathrm{after}}\le D_x^{\mathrm{before}}
 +(t^{-1}-t)D_y,\qquad 0<t<1.
\]

*Proof.*

Removing one condition gives a short exact sequence with quotient the lower edge image. Its Hilbert value is therefore the increment. Bound it using the edge-image inclusion, then apply the degree shift from the edge factor and the quotient by the edge label.

After multiplying by the state normalization, the edge-degree identity cancels the endpoint length powers. The remaining coefficient is \(t^{-1}-t\).

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.normalized_edge_increment_le`: [PositiveTransfer.lean:621](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L621).
