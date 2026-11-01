---
id: kl.notes.path_product
title: Ordered transfer products enumerate paths
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.comparison.positive_transfer
- kl.paths.directed_paths
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.SchedulePaths.dispatch_eq_path_sum
  - OAI.KLInvariance.SchedulePaths.pathTerm_delta
  - OAI.KLInvariance.SchedulePaths.entry_eq_weighted_paths
  - OAI.KLInvariance.SchedulePaths.dispatch_eq_subpaths_sum
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1183
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.dispatch_eq_path_sum
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1200
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.pathTerm_delta
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1217
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.entry_eq_weighted_paths
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
  prompt: Are the graph, scalar, list, label-order and interval hypotheses explicit,
    with the exact path sets and source proof?
  verdict: Followed dispatch_eq_path_sum, delta evaluation and the no-duplicate conversion
    to subpaths. Kept arbitrary graph types and semiring scalars, position multiplicities,
    empty paths and the exact product orientation.
tags:
- Kazhdan-Lusztig
- background
---

# Ordered transfer products enumerate paths

Let \(V,E\) be sets with source and target maps \(s,r:E\to V\), let \(R\) be a semiring, and let \(T\in R\). For a finite edge list \(p\), write \(\mathcal D_p(T)\) for the ordered transfer product, and \(P_{q,T}\), \(\delta_y\) and \(\mathcal P_p(x,y)\) for the [[node:kl.paths.directed_paths|directed-path definitions]].

For any vector \(v:V\to R\),
\[
\bigl(\mathcal D_p(T)v\bigr)_x
=\sum_{q\in p.\mathrm{sublists}'}P_{q,T}(v)_x.
\tag{1}
\]
The sum on the right counts position choices with their multiplicities.
With the delta initial vector,
\[
\bigl(\mathcal D_p(T)\delta_y\bigr)_x
=\sum_{q\in p.\mathrm{sublists}'}
\begin{cases}
T^{|q|},&\operatorname{Path}(x,y;q),\\
0,&\text{otherwise}.
\end{cases}
\tag{2}
\]
If \(p\) has no repeated edge, then
\[
\bigl(\mathcal D_p(T)\delta_y\bigr)_x
=\sum_{q\in\mathcal P_p(x,y)}T^{|q|}.
\tag{3}
\]
The left side is the \((x,y)\) matrix entry when the vertex set is finite; the formulas also define it directly for arbitrary \(V\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Position sublists and the finite selected-path set.**

**OpenAI notes:** The notes expand the elementary matrix product into weighted directed paths and use a schedule listing each edge once. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275), [eq:comparison](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L298).

**Lean (primary):** The generic semiring identity first sums over all position sublists, retaining their multiplicities. Delta evaluation makes each term a path-length weight or zero. A separate theorem uses absence of repeated schedule edges to pass to the finite set of actual path lists. [ReflectionSchedules:1161](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1161), [ReflectionSchedules:1166](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1166), [ReflectionSchedules:1183](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1183), [ReflectionSchedules:1200](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1200), [DyerPaths:1784](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1784), [DyerPaths:1794](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1794).

**Role in the proof:** The Blueprint defines the path predicate, path term, delta vector and selected path set before proving the expansion. A repeated-edge calculation explains the multiplicity distinction.
<!-- source-comparison:end -->

*Proof.*

### Step 1. The empty product and its one position choice

For \(p=[]\), dispatch is the identity, so the left side of (1) is \(v_x\). The only sublist is \([]\), and \(P_{[],T}(v)_x=v_x\). This proves the induction base.

### Step 2. Separation of the head position

Write \(p=e::h\). Each choice of positions either omits the head or retains it. The omitted-head terms are \(P_{q,T}(v)_x\), one for each position sublist \(q\) of \(h\). The retained-head terms are \(P_{e::q,T}(v)_x\), with the same tail choices.

By definition,
\[
\bigl(\mathcal D_{e::h}(T)v\bigr)_x
=\bigl(\mathcal D_h(T)v\bigr)_x
 \begin{cases}
 T\bigl(\mathcal D_h(T)v\bigr)_{r(e)},&s(e)=x,\\
 0,&s(e)\ne x.
 \end{cases}
\]
Apply the induction hypothesis at \(x\) to the first summand. This gives exactly the omitted-head terms.
If \(s(e)=x\), apply it at \(r(e)\) to the second summand and distribute left multiplication by \(T\):
\[
T\sum_q P_{q,T}(v)_{r(e)}
=\sum_q T P_{q,T}(v)_{r(e)}
=\sum_q P_{e::q,T}(v)_x.
\]
If \(s(e)\ne x\), all retained-head terms are zero by definition. This proves (1) in both cases and completes the list induction.

### Step 3. Evaluation on a delta vector

For \(q=[]\), \(P_{[],T}(\delta_y)_x\) is one if \(x=y\) and zero otherwise. This agrees with the empty-path predicate and \(T^0=1\).

For \(q=e::h\), first consider \(s(e)\ne x\). Both the path term and the path predicate vanish at that source. If \(s(e)=x\), the recursion gives \(T P_{h,T}(\delta_y)_{r(e)}\). By induction, this is \(T\cdot T^{|h|}=T^{|h|+1}\) when \(h\) is a path from \(r(e)\) to \(y\), and zero otherwise. The path recursion says precisely that this is the condition for \(e::h\) to be a path from \(x\) to \(y\). This proves the delta formula for every list.

Substituting it into every summand of (1) proves (2).

### Step 4. Passage from position choices to a finite path set

Assume \(p\) has no repeated edge. Each edge of a chosen sublist then identifies its unique position in \(p\), so different position choices give different resulting lists. Hence `p.sublists'` has no repetitions.

We can therefore replace its list sum by the sum over the corresponding finite set. All terms whose lists fail the path predicate are zero, so deleting them leaves precisely \(\mathcal P_p(x,y)\). Each retained term is \(T^{|q|}\), proving (3).

### Step 5. Empty paths and a two-edge contribution

The empty list belongs to \(\mathcal P_p(x,y)\) exactly when \(x=y\), and contributes one. For distinct vertices \(x,y,z\) and composable edges \(e:x\to y\), \(f:y\to z\), the product \(U_e(T)U_f(T)\) has a contribution \(T^2\) in its \((x,z)\) entry, from the sublist \([e,f]\).

The operator order is the list order in \(\mathcal D_{[e,f]}\). Chronologically \(f\) acts first, placing its contribution at \(y\), and then \(e\) reads that coordinate into \(x\). This gives the same \(T^2\) term in the direct coordinate calculation.

### Step 6. Multiplicity for a repeated edge

For a single edge \(e:x\to y\) with \(x\ne y\), take \(p=[e,e]\). The two one-position choices both give \([e]\). The two-edge list \([e,e]\) fails the incidence equation \(y=x\), and the empty list does not connect \(x\) to \(y\). Thus (2) gives
\[
\bigl(U_e(T)U_e(T)\delta_y\bigr)_x=T+T.
\]
The finite set \(\mathcal P_p(x,y)\) contains only \([e]\), whose single weight is \(T\). This calculation explains the no-repetition hypothesis in the passage from (2) to (3). The actual sorted Bruhat schedules satisfy that hypothesis.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.SchedulePaths.dispatch_eq_path_sum`: [ReflectionSchedules.lean:1183](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1183).

`OAI.KLInvariance.SchedulePaths.pathTerm_delta`: [ReflectionSchedules.lean:1200](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1200).

`OAI.KLInvariance.SchedulePaths.entry_eq_weighted_paths`: [ReflectionSchedules.lean:1217](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1217).

`OAI.KLInvariance.SchedulePaths.dispatch_eq_subpaths_sum`: [DyerPaths.lean:1794](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1794).
