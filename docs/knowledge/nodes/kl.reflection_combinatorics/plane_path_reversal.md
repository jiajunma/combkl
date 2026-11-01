---
id: kl.dihedral.plane_path_reversal
title: Reversal of the full path product in an induced dihedral interval
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.interval_flip
- kl.dihedral.internal_ranks
- kl.dihedral.middle_vertex_order
- kl.paths.path_transport
- kl.paths.path_involution
- kl.paths.sorted_path_selection
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.Dihedral.descent_swap
  - OAI.KLInvariance.Dihedral.unique_leftDescent
  - OAI.KLInvariance.Dihedral.descent_swap_false_iff_not
  - OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_ne_of_path
  - OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_slopes_rankFlip
  - OAI.KLInvariance.TitsSpace.PlaneBasis.intervalEdgeSlope_flip
  - OAI.KLInvariance.TitsSpace.PlaneBasis.intervalEdgeSlope_ties
  - OAI.KLInvariance.TitsSpace.PlaneBasis.intervalEdgeSlope_flip_reverse
  - OAI.KLInvariance.TitsSpace.PlaneBasis.dispatch_reverse_endpoints
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1011
    format: lean-location
    note: OAI.KLInvariance.Dihedral.descent_swap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1019
    format: lean-location
    note: OAI.KLInvariance.Dihedral.unique_leftDescent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1048
    format: lean-location
    note: OAI.KLInvariance.Dihedral.descent_swap_false_iff_not
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1715
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_ne_of_path
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1722
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_slopes_rankFlip
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1757
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.intervalEdgeSlope_flip
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1865
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.intervalEdgeSlope_ties
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1875
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.intervalEdgeSlope_flip_reverse
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1889
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.dispatch_reverse_endpoints
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the graph, scalar, list, label-order and interval hypotheses explicit,
    with the exact path sets and source proof?
  verdict: Read the actual middle-descent and flipped-slope proofs, including strict
    internal-rank hypotheses and slope distinctness. Verified both signed-label applications
    of subpaths_map_of_sorted, endpoint fixing, fullness/Nodup and the final involution
    reindexing. The result is the fixed endpoint entry of a full intrinsic interval.
tags:
- Kazhdan-Lusztig
- reflection_orders
---

# Reversal of the full path product in an induced dihedral interval

Let \(W\) be a finite-generator Coxeter system, \(P\) an actual root plane, and \(B\) a plane-basis datum with induced two-generator system \(D\). Choose
\(\mathrm{lo}\le_D\mathrm{hi}\), and let \(V=[\mathrm{lo},\mathrm{hi}]_D\), \(E\) be its directed reflection edges.

Let \(\iota:V\to V\) and \(g:E\to E\) be the interval and edge flips, and let
\(\lambda(e)=\lambda_B(e)\) be the actual geometric root slope from the [[node:kl.dihedral.interval_flip|interval-flip construction]].
For composable edges \(e,h\),
\[
\lambda(e)<\lambda(h)
\Longleftrightarrow
\lambda(g(h))<\lambda(g(e)).
\tag{1}
\]

Let \(p\) be a list containing every edge of \(E\) exactly once, weakly decreasing for \(\lambda\). For any semiring \(R\) and coefficient \(T\in R\),
\[
\bigl(\mathcal D_p(T)\delta_{\mathrm{hi}}\bigr)_{\mathrm{lo}}
=
\bigl(\mathcal D_{p^{\mathrm{rev}}}(T)\delta_{\mathrm{hi}}\bigr)_{\mathrm{lo}}.
\tag{2}
\]
This is `PlaneBasis.dispatch_reverse_endpoints`.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**A complete intrinsic interval supplies the root-plane identity.**

**OpenAI notes:** The notes state the increasing and decreasing path formulas and develop the two-vertex internal ranks and angular comparisons in the dihedral section. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [dih:shape](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L112), [dih:midpoint-order](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L358).

**Lean (primary):** The local identity fixes the two endpoints of a full intrinsic interval and switches its internal-rank vertices. The middle-descent test proves reversal of adjacent actual-root slope comparisons. A length-preserving involution then identifies the two endpoint entries for a full sorted edge list and its reverse. [DyerPaths:1563](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1563), [DyerPaths:1594](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1594), [DyerPaths:1620](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1620), [DyerPaths:1048](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1048), [DyerPaths:1722](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1722), [DyerPaths:1752](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1752), [DyerPaths:1889](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1889).

**Role in the proof:** The Blueprint gives the interval and edge maps, verifies both directions of sorted path transport and states the precise endpoint-entry equality. The later ambient plane-block application uses this intrinsic identity through the coset graph.
<!-- source-comparison:end -->

*Proof.*

### Step 1. The internal middle vertex

Take composable edges \(e:x\to y\) and \(h:y\to z\) in the full interval. Let
\(L=\ell_D(\mathrm{lo})\), \(H=\ell_D(\mathrm{hi})\).
Since \(x,z\) belong to the interval and the two edges strictly increase length,
\[
L\le\ell_D(x)<\ell_D(y)<\ell_D(z)\le H.
\]
Thus \(L<\ell_D(y)<H\), and the interval flip sends \(y\) to \(\theta y\).
The [[node:kl.dihedral.interval_flip|interval-flip construction]] sends the two edges to a composable pair
\(\iota x\to\theta y\to\iota z\).

### Step 2. The change of simple descent

The [[node:kl.dihedral.internal_ranks|internal-rank theorem]] applies to \(y\): its length is positive, and the element \(\mathrm{hi}\) has greater length. Hence \(y\) has exactly one of the two simple left descents.

For either simple generator \(s_i\), the identities
\[
s_i\theta(y)=\theta(s_{1-i}y),\qquad
\ell_D(\theta w)=\ell_D(w)
\]
give
\[
\ell_D(s_i\theta y)<\ell_D(\theta y)
\Longleftrightarrow
\ell_D(s_{1-i}y)<\ell_D(y).
\]
For \(i=0\), uniqueness of the descent therefore gives
\[
s_0\text{ descends at }\theta y
\Longleftrightarrow
s_0\text{ does not descend at }y.
\tag{3}
\]
These are the source's `descent_swap` and `descent_swap_false_iff_not`.

### Step 3. The [[node:kl.dihedral.middle_vertex_order|middle-vertex slope test]]

The [[node:kl.dihedral.middle_vertex_order|middle-vertex slope test]] for the plane basis gives
\[
\lambda(e)<\lambda(h)
\Longleftrightarrow s_0\text{ descends at }y.
\tag{4}
\]
Apply the same test to the flipped composable pair:
\[
\lambda(g(e))<\lambda(g(h))
\Longleftrightarrow s_0\text{ descends at }\theta y.
\tag{5}
\]
The two roots labelling a composable upward pair are distinct. Indeed, equal roots would give the same reflection \(\tau\), so the two successive reflections would return the last vertex to the first, contradicting the two strict length increases. Geometric slope is injective on positive roots, so the two slopes in each pair are also distinct.

By (3)–(5), the comparison in (5) holds exactly when the comparison in (4) fails. For two distinct real numbers, failure of one strict comparison gives the opposite strict comparison. Hence (4) is equivalent to
\(\lambda(g(h))<\lambda(g(e))\), proving (1).

### Step 4. The reverse implication in the other orientation

The edge flip preserves composability and is an involution. Apply (1) to \(g(e),g(h)\), and use \(g^2=\operatorname{id}\). This gives
\[
\lambda(h)<\lambda(e)
\Longleftrightarrow
\lambda(g(e))<\lambda(g(h)).
\tag{6}
\]
Equations (1) and (6) are the local comparison statements needed in the two path-map directions.

### Step 5. The two sorted schedules

The schedule \(p\) is weakly decreasing for \(\lambda\). Its reverse is weakly decreasing for the label \(-\lambda\): if \(e\) precedes \(h\) in the reverse list, then \(h\) precedes \(e\) in \(p\), so
\[
\lambda(e)\le\lambda(h)
\quad\Longrightarrow\quad
-\lambda(h)\le-\lambda(e).
\]
Both lists contain every edge exactly once.

Equal \(\lambda\)-labels cannot occur on composable edges by the distinctness argument in Step 3. Equality of \(-\lambda\)-labels is equivalent to equality of \(\lambda\)-labels, so the same property holds for \(-\lambda\).

### Step 6. Forward transport to the reverse schedule

Use [[node:kl.paths.path_transport|sorted path transport]] with source labels \(\lambda\), target labels \(-\lambda\), schedules \(p,p^{\mathrm{rev}}\), vertex map \(\iota\), and edge map \(g\).
The endpoint-map equations hold by the [[node:kl.dihedral.interval_flip|interval-flip construction]], and \(\iota\) fixes \(\mathrm{lo},\mathrm{hi}\).
For a composable pair with \(\lambda(h)<\lambda(e)\), (6) gives
\(\lambda(g(e))<\lambda(g(h))\), or equivalently
\[
-\lambda(g(h))<-\lambda(g(e)).
\]
This is the required local comparison for the target labels. All sorting, fullness and tie hypotheses were verified in Step 5. Therefore
\[
q\in\mathcal P_p(\mathrm{lo},\mathrm{hi})
\Longrightarrow
g(q)\in\mathcal P_{p^{\mathrm{rev}}}(\mathrm{lo},\mathrm{hi}).
\tag{7}
\]

### Step 7. Backward transport

Now exchange the two schedules and labels. A composable pair decreasing for \(-\lambda\) satisfies \(\lambda(e)<\lambda(h)\). Equation (1) gives
\(\lambda(g(h))<\lambda(g(e))\), the decreasing comparison for the target label \(\lambda\).
The same endpoint equations, fullness and tie properties apply. [[node:kl.paths.path_transport|Sorted path transport]] gives
\[
q\in\mathcal P_{p^{\mathrm{rev}}}(\mathrm{lo},\mathrm{hi})
\Longrightarrow
g(q)\in\mathcal P_p(\mathrm{lo},\mathrm{hi}).
\tag{8}
\]

### Step 8. Equality of the endpoint entries

The map \(g\) is an involution, so its edgewise action has the same property and preserves path length. The two schedules have no repeated edge, and (7)–(8) give the two path-membership directions.
The [[node:kl.paths.path_involution|path-involution theorem]] now applies and proves (2).

If \(\mathrm{lo}=\mathrm{hi}\), there are no upward interval edges and both endpoint entries are the empty-path contribution one. For positive-rank intervals, the same argument pairs the selected paths with paths of the same number of edges in the opposite schedule. This is the intrinsic root-plane block identity used in the later geometric order-independence proof.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.descent_swap`: [DyerPaths.lean:1011](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1011).

`OAI.KLInvariance.Dihedral.unique_leftDescent`: [DyerPaths.lean:1019](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1019).

`OAI.KLInvariance.Dihedral.descent_swap_false_iff_not`: [DyerPaths.lean:1048](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1048).

`OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_ne_of_path`: [DyerPaths.lean:1715](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1715).

`OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_slopes_rankFlip`: [DyerPaths.lean:1722](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1722).

`OAI.KLInvariance.TitsSpace.PlaneBasis.intervalEdgeSlope_flip`: [DyerPaths.lean:1757](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1757).

`OAI.KLInvariance.TitsSpace.PlaneBasis.intervalEdgeSlope_ties`: [DyerPaths.lean:1865](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1865).

`OAI.KLInvariance.TitsSpace.PlaneBasis.intervalEdgeSlope_flip_reverse`: [DyerPaths.lean:1875](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1875).

`OAI.KLInvariance.TitsSpace.PlaneBasis.dispatch_reverse_endpoints`: [DyerPaths.lean:1889](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1889).
