---
id: kl.notes.path_product
title: Ordered transfer products enumerate paths
kind: theorem
status: proved
primary_topic: kl.06_reflection_orders
topics:
- kl.06_reflection_orders
uses:
- kl.comparison.positive_transfer
- kl.notes.reflection_order
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  - DyerPaths
  declarations:
  - OAI.KLInvariance.SchedulePaths.dispatch
  - OAI.KLInvariance.SchedulePaths.dispatch_eq_subpaths_sum
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1177
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.dispatch
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1794
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.dispatch_eq_subpaths_sum
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; bg:paths
    format: section
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the source hypotheses retained?
  verdict: The statement and proof follow the fixed formal development and its paper
    counterpart.
tags:
- Kazhdan-Lusztig
- background
---

# Ordered transfer products enumerate paths

For an edge \(e:x\to y\), write \(M_e=1+T E_{xy}\). For a list of distinct edges, the \(x,y\) entry of its ordered product is the sum of \(T^r\) over composable \(r\)-edge subpaths in that list. The empty path contributes the identity entry.

*Proof.*

Expand each factor as the sum of the identity and its edge term. A chosen sublist contributes a product of matrix units. Since
\[
E_{ab}E_{cd}=
\begin{cases}
E_{ad},&b=c,\\
0,&b\ne c,
\end{cases}
\]
the contribution vanishes unless the selected edges are composable. A path of \(r\) edges contributes exactly \(T^r\).

For example, with \(x<y<z\),
\[
(1+T E_{xy})(1+T E_{yz})
=1+T E_{xy}+T E_{yz}+T^2E_{xz}.
\]
The quadratic term records the path \(x\to y\to z\). Reversing these two factors loses this term. Thus the order in the product contains mathematical information.

When vectors are updated chronologically, the upper edge must contribute to the \(y\)-coordinate before the lower edge can use that coordinate at \(x\). This explains why increasing chronological processing corresponds to decreasing labels along the contributing path. Dyer's theorem identifies the resulting path polynomial with \(\widetilde R\).

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185).

## Lean formalization

`dispatch` applies a list recursively from its tail. Its matrix product is written in the list's left-to-right order; the chronological processing order is handled separately in the invariance construction.

`OAI.KLInvariance.SchedulePaths.dispatch`: [ReflectionSchedules.lean:1177](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1177).

`OAI.KLInvariance.SchedulePaths.dispatch_eq_subpaths_sum`: [DyerPaths.lean:1794](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1794).
