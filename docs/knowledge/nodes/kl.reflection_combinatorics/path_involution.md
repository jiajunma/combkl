---
id: kl.paths.path_involution
title: A path involution identifies two transfer-product entries
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.paths.directed_paths
- kl.notes.path_product
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.SchedulePaths.dispatch_eq_of_path_involution
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1803
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.dispatch_eq_of_path_involution
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the graph, scalar, list, label-order and interval hypotheses explicit,
    with the exact path sets and source proof?
  verdict: Read the exact involution theorem with both finite-path membership directions
    and both no-duplicate hypotheses. Explained the inverse bijections, preservation
    of list length and finite-sum reindexing over an arbitrary semiring.
tags:
- Kazhdan-Lusztig
- reflection_orders
---

# A path involution identifies two transfer-product entries

Let \(V,E\) be a directed graph, \(R\) a semiring, \(T\in R\), and \(x,y\in V\). Let \(p,p'\) be finite schedules without repeated edges.
Suppose \(g:E\to E\) is an involution, meaning \(g(g(e))=e\) for every edge, and its edgewise action satisfies
\[
q\in\mathcal P_p(x,y)\Longrightarrow g(q)\in\mathcal P_{p'}(x,y),
\]
\[
q\in\mathcal P_{p'}(x,y)\Longrightarrow g(q)\in\mathcal P_p(x,y).
\tag{1}
\]
Then
\[
\bigl(\mathcal D_p(T)\delta_y\bigr)_x
=\bigl(\mathcal D_{p'}(T)\delta_y\bigr)_x.
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

### Step 1. The map on finite path sets

Define \(G(q)=g(q)\) by replacing every edge of \(q\) with its \(g\)-image, keeping the positions in the same order. The two assumptions (1) make \(G\) a map from each selected path set into the other.

For \(q=[e_1,\ldots,e_m]\), applying \(G\) twice gives
\[
[g(g(e_1)),\ldots,g(g(e_m))]=[e_1,\ldots,e_m]=q.
\]
The same identity holds for the empty list. Thus the restrictions of \(G\) in the two directions are inverse bijections.

### Step 2. Equality of the path weights

Replacing each edge changes no position, so \(|G(q)|=|q|\). Every path therefore has the same weight as its image:
\[
T^{|G(q)|}=T^{|q|}.
\]
This includes the empty path, whose weight is one.

### Step 3. Reindexing the finite sum

The [[node:kl.notes.path_product|path-sum expansion]] applies to both schedules because each has no repeated edge. Hence the two sides of (2) are
\[
\sum_{q\in\mathcal P_p(x,y)}T^{|q|}
\quad\text{and}\quad
\sum_{q'\in\mathcal P_{p'}(x,y)}T^{|q'|}.
\]
Use the bijection \(q'=G(q)\) from Step 1 to reindex the second sum. Step 2 identifies every summand with the corresponding term in the first sum. The sums are equal, proving (2).

In the [[node:kl.dihedral.plane_path_reversal|plane-path reversal theorem]], \(g\) will switch the internal-rank vertices of a dihedral interval, \(p'\) will be \(p^{\mathrm{rev}}\), and [[node:kl.paths.path_transport|sorted path transport]] will establish the two conditions (1).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.SchedulePaths.dispatch_eq_of_path_involution`: [DyerPaths.lean:1803](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1803).
