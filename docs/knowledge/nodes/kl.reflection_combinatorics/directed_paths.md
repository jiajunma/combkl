---
id: kl.paths.directed_paths
title: Directed edge lists, path weights and selected path sets
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses: []
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.SchedulePaths.IsPath
  - OAI.KLInvariance.SchedulePaths.pathTerm
  - OAI.KLInvariance.SchedulePaths.subpaths
  - OAI.KLInvariance.SchedulePaths.mem_subpaths
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1161
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.IsPath
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1166
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.pathTerm
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1784
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.subpaths
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1787
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.mem_subpaths
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the graph, scalar, list, label-order and interval hypotheses explicit,
    with the exact path sets and source proof?
  verdict: Read IsPath, pathTerm and subpaths with their arbitrary graph and semiring
    parameters. Explained endpoint recursion, delta vectors, position-sublist multiplicity
    and finite-set membership without assuming finite vertex or edge types.
tags:
- Kazhdan-Lusztig
- reflection_orders
---

# Directed edge lists, path weights and selected path sets

Let \(V\) be a set of vertices and \(E\) a set of edges, with source and target maps \(s,r:E\to V\). The edge set may contain more than one edge with the same endpoints. The constructions below use finite lists of actual edges.

## A directed path as an edge list

For vertices \(x,y\), the predicate \(\operatorname{Path}(x,y;p)\) is defined recursively by
\[
\operatorname{Path}(x,y;[])\ \Longleftrightarrow\ x=y,
\]
\[
\operatorname{Path}(x,y;e::q)\
\Longleftrightarrow\ s(e)=x\ \text{ and }\operatorname{Path}(r(e),y;q).
\]
This is `SchedulePaths.IsPath`. For a nonempty list \(p=[e_1,\ldots,e_m]\), it says
\[
s(e_1)=x,\qquad r(e_i)=s(e_{i+1})\ (1\le i<m),
\qquad r(e_m)=y.
\]
Its length \(|p|=m\) counts edges. The empty list is the length-zero path at each vertex.

For edges \(e:x\to y\), \(f:y\to z\), the list \([e,f]\) is a path from \(x\) to \(z\). The list \([f,e]\) is a path only when its endpoints satisfy the corresponding reversed incidence equations.

## A weighted path term

Let \(R\) be a semiring, \(T\in R\), and \(v:V\to R\) a vector. Define
\[
P_{[],T}(v)_x=v_x,
\qquad
P_{e::q,T}(v)_x=
\begin{cases}
T P_{q,T}(v)_{r(e)},&s(e)=x,\\
0,&s(e)\ne x.
\end{cases}
\]
This is `SchedulePaths.pathTerm`. If \(p\) is a path from \(x\) to \(y\), each recursive step contributes a left factor \(T\), and the final step reads \(v_y\), giving \(T^{|p|}v_y\). A failed incidence equation makes the corresponding recursive value zero and hence makes the whole term zero.

For a fixed endpoint \(y\), define the delta vector
\[
(\delta_y)_z=\begin{cases}1,&z=y,\\0,&z\ne y.\end{cases}
\]
Then the path term is \(T^{|p|}\) for a path from \(x\) to \(y\), and zero otherwise. The [[node:kl.notes.path_product|path-sum expansion]] proves this identity by induction, including the empty list.

## Sublists and position choices

A list \(q\) is a sublist of \(p\), written \(q\preceq_{\mathrm{sub}}p\), when it is obtained by deleting some positions and keeping the order of the remaining positions. Consecutive positions need not be retained.

Lean's `p.sublists'` lists the results of all choices of retained positions. A list with \(m\) entries has \(2^m\) such position choices. Equal edge values at different positions can give the same resulting list more than once. For \(p=[e,e]\), the four choices give
\[
[],\quad[e],\quad[e],\quad[e,e].
\]
For \(p=[e,f]\) with \(e\ne f\), the four resulting lists are distinct.

## The finite set of selected paths

For a schedule list \(p\), define
\[
\mathcal P_p(x,y)
=\{q:q\preceq_{\mathrm{sub}}p,\ \operatorname{Path}(x,y;q)\}.
\]
This is `SchedulePaths.subpaths`. The source constructs it by converting `p.sublists'` to a finite set, which removes repetitions, and then retaining precisely the directed paths.
Thus
\[
q\in\mathcal P_p(x,y)
\Longleftrightarrow
q\preceq_{\mathrm{sub}}p\ \text{ and }\operatorname{Path}(x,y;q).
\]
The set is finite because all its elements arise from the finitely many position choices.

For distinct \(x,y,z\), edges \(e:x\to y\), \(f:y\to z\), and schedule \([e,f]\), the selected path set from \(x\) to \(z\) consists of \([e,f]\); its weight is \(T^2\). The schedule \([f,e]\) selects no path from \(x\) to \(z\). This is the path-set form of the two-edge transfer calculation.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Position sublists and the finite selected-path set.**

**OpenAI notes:** The notes expand the elementary matrix product into weighted directed paths and use a schedule listing each edge once. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275), [eq:comparison](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L298).

**Lean (primary):** The generic semiring identity first sums over all position sublists, retaining their multiplicities. Delta evaluation makes each term a path-length weight or zero. A separate theorem uses absence of repeated schedule edges to pass to the finite set of actual path lists. [ReflectionSchedules:1161](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1161), [ReflectionSchedules:1166](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1166), [ReflectionSchedules:1183](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1183), [ReflectionSchedules:1200](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1200), [DyerPaths:1784](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1784), [DyerPaths:1794](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1794).

**Role in the proof:** The Blueprint defines the path predicate, path term, delta vector and selected path set before proving the expansion. A repeated-edge calculation explains the multiplicity distinction.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.SchedulePaths.IsPath`: [ReflectionSchedules.lean:1161](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1161).

`OAI.KLInvariance.SchedulePaths.pathTerm`: [ReflectionSchedules.lean:1166](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1166).

`OAI.KLInvariance.SchedulePaths.subpaths`: [DyerPaths.lean:1784](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1784).

`OAI.KLInvariance.SchedulePaths.mem_subpaths`: [DyerPaths.lean:1787](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1787).
