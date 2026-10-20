---
id: kl.detail.transported_schedule
title: Transported edge scores, schedules and remaining conditions
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.paths.graph_invariance
- kl.order.root_slopes
- kl.foundations.interval
lean:
  repository: openai-kl
  modules:
  - EdgeLocalization
  - PositiveTransfer
  - ReflectionOrders
  declarations:
  - OAI.KLInvariance.SchedulePaths.sortedSchedule
  - OAI.KLInvariance.SchedulePaths.mem_sortedSchedule
  - OAI.KLInvariance.SchedulePaths.sortedSchedule_nodup
  - OAI.KLInvariance.SchedulePaths.sortedSchedule_pairwise
  - OAI.KLInvariance.BruhatGraph.transportedEdge
  - OAI.KLInvariance.BruhatGraph.transportedEdge_injective
  - OAI.KLInvariance.BruhatGraph.transportedEdge_lift
  - OAI.KLInvariance.BruhatGraph.transportedScore
  - OAI.KLInvariance.BruhatGraph.transportedSlope
  - OAI.KLInvariance.BruhatGraph.transportedScore_eq
  - OAI.KLInvariance.BruhatGraph.transportedSchedule
  - OAI.KLInvariance.BruhatGraph.transportedSchedule_nodup
  - OAI.KLInvariance.BruhatGraph.transportedSchedule_full
  - OAI.KLInvariance.BruhatGraph.transportedSchedule_pairwise
  - OAI.KLInvariance.BruhatGraph.chronologicalSchedule
  - OAI.KLInvariance.BruhatGraph.chronologicalSchedule_pairwise
  - OAI.KLInvariance.BruhatGraph.chronologicalSchedule_nodup
  - OAI.KLInvariance.BruhatGraph.chronologicalSchedule_full
  - OAI.KLInvariance.BruhatGraph.remainingConditions
  - OAI.KLInvariance.BruhatGraph.remainingConditions_nil
  - OAI.KLInvariance.BruhatGraph.remainingConditions_cons_source
  - OAI.KLInvariance.BruhatGraph.remainingConditions_cons_other
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionOrders:582
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.sortedSchedule
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionOrders:585
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.mem_sortedSchedule
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionOrders:588
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.sortedSchedule_nodup
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionOrders:592
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.sortedSchedule_pairwise
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:23
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.transportedEdge
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:28
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.transportedEdge_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:62
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.transportedEdge_lift
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:35
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.transportedScore
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1222
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.transportedSlope
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1228
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.transportedScore_eq
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:40
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.transportedSchedule
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:45
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.transportedSchedule_nodup
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:50
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.transportedSchedule_full
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:56
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.transportedSchedule_pairwise
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1225
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.chronologicalSchedule
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1234
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.chronologicalSchedule_pairwise
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1244
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.chronologicalSchedule_nodup
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1248
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.chronologicalSchedule_full
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1089
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.remainingConditions
  - artifact: openai-kl-paper
    locator: Related paper context; sec:dihedral
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1093
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.remainingConditions_nil
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1097
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.remainingConditions_cons_source
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1105
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.remainingConditions_cons_other
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, finiteness and freeness hypotheses, original embedded
    submodules, localization multipliers and schedule assumptions explicit?
  verdict: Expanded exact target-edge transport and its inverse construction, the
    diagonal lex score, merge-sort membership/no-duplication/order, reversal, and
    the basic outgoing remaining-condition definition. Kept weak sorting separate
    from the strict endpoint suffix theorem.
tags:
- Kazhdan-Lusztig
- global-inclusion
---

# Transported edge scores, schedules and remaining conditions

Fix finite-generator real Coxeter systems \(W,W'\) and an interval order isomorphism
\[
\varphi:[u,b]_W\simeq[u',b']_{W'}.
\]
Let \(E\) be the finite set of source-interval reflection edges.

## The transported edge and its score

For \(e:x\to_Wy\), reflection-graph invariance gives the target edge
\[
\varphi_*e:\varphi(x)\to_{W'}\varphi(y).
\]
Its positive target root is \(\alpha'_e\). Define the transported slope
\[
s(e)=\sigma'(\alpha'_e),
\]
where \(\sigma'\) is the target geometric slope.

The edge map is injective: equality of target edges gives equality of both target endpoints, and injectivity of \(\varphi\) gives equality of both source endpoints. It also reaches every target edge between vertices of \([u',b']\): apply \(\varphi^{-1}\) to both endpoints and use reflection-graph invariance in reverse.

Lean's `transportedScore` is a lexicographic pair of real numbers. For its chosen geometric functional, evaluation on a normalized positive root is its geometric slope, so the pair is
\[
\operatorname{score}(e)=(s(e),s(e)).
\]
Thus comparison of these pairs agrees with comparison of the real transported slopes.

## Sorting the full edge set

For a finite set \(F\) and a score in any linearly ordered set, `sortedSchedule` converts \(F\) to a list and applies merge sort using the comparison
\[
\operatorname{score}(f)\le\operatorname{score}(e)
\]
to place \(e\) before \(f\). Merge sort preserves the entries of the original list, so the result contains each member of \(F\) exactly once. Its scores are weakly decreasing.

The transported schedule \(\mathcal T\) uses the full edge set \(E\) and the transported score. Hence it contains every source-interval edge once, and for positions \(i<j\),
\[
s(\mathcal T_i)\ge s(\mathcal T_j).
\]
The chronological schedule is its reverse,
\[
\mathcal C=\operatorname{reverse}(\mathcal T).
\]
It also contains every edge once, with weakly increasing slopes.

For example, if two edges have score \(1\) and another has score \(3\), the chronological score list is \(1,1,3\). The two equal-scored edges occupy adjacent positions; each edge still occurs once.

## The two list directions

An elementary edge operator acts on a vector of vertex values. In a written product, the rightmost operator acts first. The decreasing transported schedule describes the written outermost-first product. Its reversed chronological schedule describes successive removal of edge conditions from the vertices.

## Remaining outgoing conditions

For any list \(p\) of interval edges and vertex \(x\), define
\[
\mathcal R_p(x)=
\{f\in\operatorname{Out}(x):f\text{ occurs in }p\}.
\]
This is `remainingConditions`. The empty list gives the empty selection. If \(p\) contains every edge, it gives the full outgoing selection.

For any list beginning with \(e:x\to y\) and followed by \(q\), the source selection is
\[
\mathcal R_{e::q}(x)=\{e\}\cup\mathcal R_q(x).
\]
Selections at vertices other than \(x\) are unchanged by removing the first entry. In particular the condition set at \(y\) is unchanged because an upward edge has distinct endpoints.

For a duplicate-free list, \(e\) does not occur in \(q\), so removing the first entry deletes exactly that source condition. This applies to the chronological schedule.

For a suffix consisting of the current edge \(e\) followed by a list \(q\), the [[node:kl.paths.schedule_suffixes|schedule-suffix theorem]] identifies \(\mathcal R_q(x)\) and \(\mathcal R_q(y)\) with strict later-score conditions at the two endpoints.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Exact suffix conditions specialize the ambient inclusion.**

**OpenAI notes:** The notes formulate the current endpoint conditions as the edges strictly later than the current edge in a transported reflection order. [dih:count](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L464), [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The actual schedule is a complete duplicate-free sorted list with a diagonal lexicographic score; its reverse is chronological. Two sorted-list lemmas, same-source score injectivity and consecutive-edge score inequality identify both suffix selections with the ambient later-edge set. Upper-interval restriction then transfers both kernels and the upper freeness hypothesis. [EdgeLocalization:40](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L40), [PositiveTransfer:1228](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1228), [PositiveTransfer:1225](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1225), [PositiveTransfer:1306](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1306), [PositiveTransfer:1315](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1315), [TerminalKernels:1126](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1126).

**Role in the proof:** The Blueprint states the exact suffix assumption and distinguishes weak list ordering from the strict score test at the two current endpoints.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.SchedulePaths.sortedSchedule`: [ReflectionOrders.lean:582](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionOrders.lean#L582).

`OAI.KLInvariance.SchedulePaths.mem_sortedSchedule`: [ReflectionOrders.lean:585](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionOrders.lean#L585).

`OAI.KLInvariance.SchedulePaths.sortedSchedule_nodup`: [ReflectionOrders.lean:588](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionOrders.lean#L588).

`OAI.KLInvariance.SchedulePaths.sortedSchedule_pairwise`: [ReflectionOrders.lean:592](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionOrders.lean#L592).

`OAI.KLInvariance.BruhatGraph.transportedEdge`: [EdgeLocalization.lean:23](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L23).

`OAI.KLInvariance.BruhatGraph.transportedEdge_injective`: [EdgeLocalization.lean:28](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L28).

`OAI.KLInvariance.BruhatGraph.transportedEdge_lift`: [EdgeLocalization.lean:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L62).

`OAI.KLInvariance.BruhatGraph.transportedScore`: [EdgeLocalization.lean:35](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L35).

`OAI.KLInvariance.BruhatGraph.transportedSlope`: [PositiveTransfer.lean:1222](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1222).

`OAI.KLInvariance.BruhatGraph.transportedScore_eq`: [PositiveTransfer.lean:1228](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1228).

`OAI.KLInvariance.BruhatGraph.transportedSchedule`: [EdgeLocalization.lean:40](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L40).

`OAI.KLInvariance.BruhatGraph.transportedSchedule_nodup`: [EdgeLocalization.lean:45](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L45).

`OAI.KLInvariance.BruhatGraph.transportedSchedule_full`: [EdgeLocalization.lean:50](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L50).

`OAI.KLInvariance.BruhatGraph.transportedSchedule_pairwise`: [EdgeLocalization.lean:56](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L56).

`OAI.KLInvariance.BruhatGraph.chronologicalSchedule`: [PositiveTransfer.lean:1225](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1225).

`OAI.KLInvariance.BruhatGraph.chronologicalSchedule_pairwise`: [PositiveTransfer.lean:1234](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1234).

`OAI.KLInvariance.BruhatGraph.chronologicalSchedule_nodup`: [PositiveTransfer.lean:1244](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1244).

`OAI.KLInvariance.BruhatGraph.chronologicalSchedule_full`: [PositiveTransfer.lean:1248](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1248).

`OAI.KLInvariance.BruhatGraph.remainingConditions`: [PositiveTransfer.lean:1089](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1089).

`OAI.KLInvariance.BruhatGraph.remainingConditions_nil`: [PositiveTransfer.lean:1093](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1093).

`OAI.KLInvariance.BruhatGraph.remainingConditions_cons_source`: [PositiveTransfer.lean:1097](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1097).

`OAI.KLInvariance.BruhatGraph.remainingConditions_cons_other`: [PositiveTransfer.lean:1105](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1105).
