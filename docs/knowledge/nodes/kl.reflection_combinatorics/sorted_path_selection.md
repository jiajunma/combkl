---
id: kl.paths.sorted_path_selection
title: Strict paths selected by a weakly sorted schedule
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.paths.directed_paths
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.SchedulePaths.decreasing_of_schedule_path
  - OAI.KLInvariance.SchedulePaths.sublist_of_decreasing_subset
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1233
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.decreasing_of_schedule_path
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1260
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.sublist_of_decreasing_subset
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the graph, scalar, list, label-order and interval hypotheses explicit,
    with the exact path sets and source proof?
  verdict: Read both generic list proofs, including the strict-label membership argument
    when the containing head differs. Preserved the separate tie condition for path
    strictness and the weaker hypotheses for strict-subset sublist recovery.
tags:
- Kazhdan-Lusztig
- reflection_orders
---

# Strict paths selected by a weakly sorted schedule

Let \(V,E\) be a directed graph with source and target maps \(s,r\), and let \(\lambda:E\to\Lambda\) take values in a linearly ordered set.
A list \([e_1,\ldots,e_m]\) is weakly decreasing when
\(\lambda(e_j)\le\lambda(e_i)\) for every \(i<j\); it is strictly decreasing when all these inequalities are strict.

Assume equal labels cannot occur on composable edges:
\[
\lambda(e)=\lambda(f)\quad\Longrightarrow\quad r(e)\ne s(f).
\tag{1}
\]
Then every weakly decreasing directed path is strictly decreasing.

There is also a list statement independent of (1): if \(q\) is strictly decreasing, \(p\) is weakly decreasing, and every edge occurring in \(q\) occurs in \(p\), then \(q\preceq_{\mathrm{sub}}p\).

Together they give the following description for a weakly decreasing schedule \(p\) satisfying (1):
\[
q\in\mathcal P_p(x,y)
\Longleftrightarrow
\begin{cases}
\operatorname{Path}(x,y;q),\\
q\text{ is strictly decreasing},\\
\text{every edge in }q\text{ occurs in }p.
\end{cases}
\tag{2}
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Local comparisons determine the selected path transport.**

**OpenAI notes:** The notes use strict reflection-label paths and observe that equal-label reflection edges are disjoint. Relative graph identifications transport the underlying directed edges. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [dih:relative-paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L148).

**Lean (primary):** The list lemmas separate weak sorting, strict path order and sublist recovery. A graph map transports incidence, and comparisons only on composable adjacent edges imply the full strict order on a mapped path. An edge involution with both path-membership directions preserves lengths and reindexes the two finite path sums. [ReflectionSchedules:1233](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1233), [ReflectionSchedules:1260](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1260), [DyerPaths:1659](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1659), [DyerPaths:1684](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1684), [DyerPaths:1828](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1828), [DyerPaths:1803](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1803).

**Role in the proof:** Each map, membership condition and order hypothesis is explicit. The path-set transport supplies the finite bijection used in the root-plane reversal calculation.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Strictness for the first composable pair

Use induction on the path list. Empty and one-edge lists have no pair of positions to compare. For \(q=e::f::h\), the path predicate gives \(r(e)=s(f)\).
Weak decrease gives \(\lambda(f)\le\lambda(e)\). Equality would contradict (1), so
\[
\lambda(f)<\lambda(e).
\]

### Step 2. Strictness between the head and every later edge

The tail \(f::h\) is a weakly decreasing path from \(r(e)\) to the final vertex. The induction hypothesis makes its comparisons strict.
For an edge \(g\) occurring in \(h\), weak decrease of the tail gives
\[
\lambda(g)\le\lambda(f)<\lambda(e).
\]
Thus every later label is strictly below the head label. This establishes all pairs in \(e::f::h\), completing the first assertion.

### Step 3. The base cases for sublist recovery

Induct on the weakly sorted containing list \(p\), allowing the strict list \(q\) to vary.
If \(p=[]\), the membership assumption forces \(q=[]\).
If \(q=[]\), it is a sublist of every \(p\).
For the remaining case, write \(p=e::h\) and \(q=f::k\).

### Step 4. Matching the two heads

Suppose \(e=f\). Every edge \(g\) of \(k\) occurs in \(e::h\). Strict decrease in \(f::k\) gives \(\lambda(g)<\lambda(f)\), so \(g\ne f=e\). Therefore every such edge occurs in \(h\).

Both sorting hypotheses restrict to the tails. Induction gives \(k\preceq_{\mathrm{sub}}h\). Retain the common head to obtain \(f::k\preceq_{\mathrm{sub}}e::h\).

### Step 5. Discarding a different containing head

Suppose \(e\ne f\). Since \(f\) occurs in \(e::h\), it must occur in \(h\). Weak decrease of \(e::h\) gives \(\lambda(f)\le\lambda(e)\).

The edge \(e\) cannot occur in \(q=f::k\): it is not the head, and occurrence in \(k\) would give \(\lambda(e)<\lambda(f)\) by strict decrease, contradicting \(\lambda(f)\le\lambda(e)\).
Consequently every edge of \(q\) occurs in \(h\). Induction gives \(q\preceq_{\mathrm{sub}}h\); deleting the initial \(e\) from \(e::h\) proves \(q\preceq_{\mathrm{sub}}p\).

### Step 6. The selected-path characterization

If \(q\in\mathcal P_p(x,y)\), it is a sublist of \(p\) and a directed path. It inherits weak decrease from \(p\), and Steps 1–2 make it strict. Sublist membership also gives the edge-membership condition in (2).

Conversely, the last two conditions in (2) and Steps 3–5 give \(q\preceq_{\mathrm{sub}}p\). Together with the path predicate, this puts \(q\) in \(\mathcal P_p(x,y)\).

Thus two weakly decreasing schedules containing the same edges select the same directed paths, whenever (1) holds. Their internal ordering of equal-label edges has no effect on the selected path set. Reversing the order on \(\Lambda\) gives the corresponding statements for increasing lists.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.SchedulePaths.decreasing_of_schedule_path`: [ReflectionSchedules.lean:1233](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1233).

`OAI.KLInvariance.SchedulePaths.sublist_of_decreasing_subset`: [ReflectionSchedules.lean:1260](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1260).
