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

### Step 1. Expand one transfer into its two summands

For \(e:x\to y\), the transfer is \(M_e=1+TE_{xy}\). In a product \(M_{e_1}\cdots M_{e_r}\), distributivity chooses either \(1\) or \(TE_e\) from each factor. Therefore terms are indexed by ordered sublists of the original list.

Selecting \(m\) edges contributes \(T^m\) times their ordered product of matrix units. No edge is selected twice, and the schedule has no repeated edge.

### Step 2. Determine exactly when a matrix-unit product survives

For vertices \(a,b,c,d\),
\[
E_{ab}E_{cd}=\begin{cases}E_{ad},&b=c,\\0,&b\ne c.\end{cases}
\]
Indeed, \(E_{cd}\) reads coordinate \(d\) into coordinate \(c\), and \(E_{ab}\) can read that result only when \(b=c\).

Inductively, \(E_{x_0x_1}\cdots E_{x_{m-1}x_m}=E_{x_0x_m}\), while a broken incidence makes the product zero. Thus the \((x,y)\)-entry receives precisely the selected sublists that form a directed path from \(x\) to \(y\). The empty selection contributes the identity entry \(\delta_{x,y}\).

### Step 3. Check that each path occurs exactly once

The schedule lists each edge once. A path whose edges occur in that list order determines a unique set of selected positions. Conversely, every surviving selection determines that path. This is a bijection, and its weight is \(T^{\text{number of edges}}\). Hence the entry is the stated finite path sum.

### Step 4. Relate product order to chronological processing

If the edges are applied chronologically as \(e_1,\ldots,e_r\), the resulting operator is \(M_{e_r}\cdots M_{e_1}\), because \(M_{e_1}\) acts first. Thus increasing chronological scores produce decreasing scores along the matrix-unit path.

Tied reflection labels do not create an ambiguity: two edges with the same reflection label cannot be composable, since that reflection would immediately undo itself. Their cross matrix-unit products vanish in both orders, so their transfers commute.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185).

## Lean formalization

`dispatch` applies a list recursively from its tail. Its matrix product is written in the list's left-to-right order; the chronological processing order is handled separately in the invariance construction.

`OAI.KLInvariance.SchedulePaths.dispatch`: [ReflectionSchedules.lean:1177](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1177).

`OAI.KLInvariance.SchedulePaths.dispatch_eq_subpaths_sum`: [DyerPaths.lean:1794](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1794).
