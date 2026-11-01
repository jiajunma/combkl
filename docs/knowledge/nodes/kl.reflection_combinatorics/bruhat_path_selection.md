---
id: kl.paths.bruhat_path_selection
title: Bruhat endpoint bounds and the selected increasing paths
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.paths.bruhat_path_polynomial
- kl.paths.sorted_path_selection
- kl.notes.path_product
- kl.foundations.bruhat_order
- kl.foundations.finite_intervals
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.AdaptedDyer.target_eq_root
  - OAI.KLInvariance.AdaptedDyer.rootLabel_ne_of_join
  - OAI.KLInvariance.AdaptedDyer.score_ties
  - OAI.KLInvariance.AdaptedDyer.mem_edgeFinset
  - OAI.KLInvariance.AdaptedDyer.mem_schedule
  - OAI.KLInvariance.AdaptedDyer.schedule_nodup
  - OAI.KLInvariance.AdaptedDyer.schedule_increasing
  - OAI.KLInvariance.AdaptedDyer.path_le
  - OAI.KLInvariance.AdaptedDyer.path_targets_le
  - OAI.KLInvariance.AdaptedDyer.mem_paths
  - OAI.KLInvariance.AdaptedDyer.polynomial_dispatch
  - OAI.KLInvariance.AdaptedDyer.polynomial_diagonal
  - OAI.KLInvariance.AdaptedDyer.polynomial_zero
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1958
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.target_eq_root
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1963
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.rootLabel_ne_of_join
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1975
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.score_ties
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1987
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.mem_edgeFinset
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2008
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.mem_schedule
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2012
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.schedule_nodup
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2016
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.schedule_increasing
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2023
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.path_le
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2031
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.path_targets_le
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2046
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.mem_paths
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2066
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.polynomial_dispatch
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2447
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.polynomial_diagonal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2451
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.polynomial_zero
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the graph, scalar, list, label-order and interval hypotheses explicit,
    with the exact path sets and source proof?
  verdict: Read finite edge membership and sorting, source path_le and path_targets_le
    inductions, score_ties, both directions of mem_paths and polynomial_dispatch.
    Also read the diagonal and outside-order polynomial lemmas and supplied their
    endpoint-length proofs.
tags:
- Kazhdan-Lusztig
- reflection_orders
---

# Bruhat endpoint bounds and the selected increasing paths

Fix a finite-generator Coxeter system \(W\), a ratio order \(O\), and the actual reflection-edge graph and finite schedules from the [[node:kl.paths.bruhat_path_polynomial|Bruhat path-polynomial definition]].

Every directed path \(q\) from \(x\) to \(y\) satisfies \(x\le_Wy\), and every edge of \(q\) has target at most \(y\). These two endpoint bounds also hold for arbitrary simple-generator sets. For the ratio-order path sets,
\[
q\in\operatorname{Paths}_O(x,y)
\Longleftrightarrow
\operatorname{Path}(x,y;q)
\ \text{ and }\ q\text{ has strictly increasing }O\text{-scores}.
\tag{1}
\]
The increasing Bruhat path polynomial consequently satisfies
\[
F_O(x,y;X)
=\bigl(\mathcal D_{S_O(y)}(X)\delta_y\bigr)_x,
\tag{2}
\]
\[
F_O(x,x;X)=1,\qquad
x\not\le_Wy\Longrightarrow F_O(x,y;X)=0.
\tag{3}
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The increasing path polynomial before the R-family identification.**

**OpenAI notes:** The path-formula statement presents the normalized R-polynomial as the weighted sum of increasing reflection paths and notes that all paths lie in the finite interval between their endpoints. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [eq:bg-path-formula](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L191).

**Lean (primary):** AdaptedDyer first defines a path polynomial from the sorted finite edge list below the final endpoint. Endpoint bounds and noncomposable score ties prove that its selected lists are precisely the strictly increasing directed paths. Its equality to the independently constructed Hecke family is proved afterwards under the adapted chamber hypothesis, followed by order independence. [DyerPaths:1948](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1948), [DyerPaths:1951](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1951), [DyerPaths:1972](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1972), [DyerPaths:1980](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1980), [DyerPaths:2005](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2005), [DyerPaths:2043](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2043), [DyerPaths:2046](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2046), [DyerPaths:2063](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2063), [DyerPaths:2066](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2066), [DyerPaths:2447](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2447), [DyerPaths:2451](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2451).

**Role in the proof:** The path polynomial, its actual edge labels, finite schedule, membership criterion, dispatch identity and diagonal/zero values are developed before the later identification theorem.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Bruhat comparison along a path

For an empty path, \(x=y\), hence \(x\le_Wy\).
For \(q=e::h\), the path starts at \(s(e)=x\). The Bruhat edge gives \(x\le_Wr(e)\), and the induction hypothesis for \(h\) gives \(r(e)\le_Wy\). Transitivity yields \(x\le_Wy\).

Apply this result to the tail after any edge of the path. That tail runs from the edge's target to \(y\), so every such target is at most \(y\). Its source is also at most \(y\), by the edge comparison.

### Step 2. The finite edge list and its sorting

The definition of \(E_b\) lists exactly the reflection edges whose two endpoints lie in \([1,b]\). Step 1 for a single edge shows that this is equivalent to the target condition \(r(e)\le_Wb\).

Each edge appears once in the finite-set enumeration. Sorting permutes that list and therefore preserves membership and absence of repetitions. It produces a weakly increasing list for the score. Thus \(S_O(b)\) contains an edge exactly when its target is at most \(b\), has no repeated edge, and is weakly increasing.

### Step 3. Equal-score edges cannot be composable

Suppose \(e:x\to z\) and \(h:z\to w\) have equal scores. Injectivity of the ratio slope gives equal positive-root labels, hence the same reflection \(\tau\).
The left-label equations give \(z=\tau x\), \(w=\tau z\). Since \(\tau^2=1\), this forces \(w=x\).

The two edge orientations give \(\ell(x)<\ell(z)<\ell(w)\), contradicting \(w=x\). Thus equal scores cannot occur on composable edges.

### Step 4. From a selected sublist to a strict path

If \(q\in\operatorname{Paths}_O(x,y)\), it is a directed path and a sublist of the weakly increasing schedule \(S_O(y)\). Its scores are weakly increasing.

Apply the increasing version of the [[node:kl.paths.sorted_path_selection|sorted-path selection theorem]], using Step 3 to exclude composable ties. The scores of \(q\) become strictly increasing. This proves the forward direction of (1).

### Step 5. From a strict path to the selected sublist

Conversely, suppose \(q\) is a strictly increasing directed path from \(x\) to \(y\). By Step 1, every edge target is at most \(y\), so every edge of \(q\) occurs in \(S_O(y)\).

This schedule is weakly increasing. The strict-subset sublist assertion of the [[node:kl.paths.sorted_path_selection|sorted-path selection theorem]] therefore gives \(q\preceq_{\mathrm{sub}}S_O(y)\). Together with the path predicate, this is exactly membership in \(\operatorname{Paths}_O(x,y)\).

### Step 6. The transfer entry and the path polynomial

The schedule \(S_O(y)\) has no repeated edge by Step 2. Apply the [[node:kl.notes.path_product|path-sum expansion]] over the semiring \(\mathbb Z[X]\), with transfer coefficient \(X\):
\[
\bigl(\mathcal D_{S_O(y)}(X)\delta_y\bigr)_x
=\sum_{q\in\mathcal P_{S_O(y)}(x,y)}X^{|q|}.
\]
The path-set definition makes the sum on the right \(F_O(x,y;X)\), proving (2).

### Step 7. The diagonal and vanishing cases

If \(x\not\le_Wy\), Step 1 rules out every directed path from \(x\) to \(y\). The finite path set is empty, and its sum is zero.

For a path from \(x\) to itself, a first edge would have target \(z\) with \(\ell(x)<\ell(z)\). The remaining tail would give \(z\le_Wx\), hence \(\ell(z)\le\ell(x)\), a contradiction. Thus only the empty path remains on the diagonal, and its weight is \(X^0=1\). This proves (3).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.AdaptedDyer.target_eq_root`: [DyerPaths.lean:1958](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1958).

`OAI.KLInvariance.AdaptedDyer.rootLabel_ne_of_join`: [DyerPaths.lean:1963](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1963).

`OAI.KLInvariance.AdaptedDyer.score_ties`: [DyerPaths.lean:1975](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1975).

`OAI.KLInvariance.AdaptedDyer.mem_edgeFinset`: [DyerPaths.lean:1987](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1987).

`OAI.KLInvariance.AdaptedDyer.mem_schedule`: [DyerPaths.lean:2008](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2008).

`OAI.KLInvariance.AdaptedDyer.schedule_nodup`: [DyerPaths.lean:2012](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2012).

`OAI.KLInvariance.AdaptedDyer.schedule_increasing`: [DyerPaths.lean:2016](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2016).

`OAI.KLInvariance.AdaptedDyer.path_le`: [DyerPaths.lean:2023](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2023).

`OAI.KLInvariance.AdaptedDyer.path_targets_le`: [DyerPaths.lean:2031](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2031).

`OAI.KLInvariance.AdaptedDyer.mem_paths`: [DyerPaths.lean:2046](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2046).

`OAI.KLInvariance.AdaptedDyer.polynomial_dispatch`: [DyerPaths.lean:2066](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2066).

`OAI.KLInvariance.AdaptedDyer.polynomial_diagonal`: [DyerPaths.lean:2447](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2447).

`OAI.KLInvariance.AdaptedDyer.polynomial_zero`: [DyerPaths.lean:2451](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2451).
