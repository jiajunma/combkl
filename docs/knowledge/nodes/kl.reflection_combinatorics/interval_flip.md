---
id: kl.dihedral.interval_flip
title: Internal-rank flips of a dihedral interval and its edges
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.signed_lengths
- kl.coxeter.dihedral_bruhat_order
- kl.dihedral.odd_reflection_edges
- kl.dihedral.induced_system
- kl.order.root_slopes
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.Dihedral.rankFlip
  - OAI.KLInvariance.Dihedral.length_rankFlip
  - OAI.KLInvariance.Dihedral.rankFlip_involutive
  - OAI.KLInvariance.Dihedral.rankFlip_lower
  - OAI.KLInvariance.Dihedral.rankFlip_upper
  - OAI.KLInvariance.Dihedral.rankFlip_bruhat_iff
  - OAI.KLInvariance.Dihedral.rankFlip_step_iff
  - OAI.KLInvariance.Dihedral.intervalFlip
  - OAI.KLInvariance.Dihedral.intervalFlip_involutive
  - OAI.KLInvariance.Dihedral.edgeFlip
  - OAI.KLInvariance.Dihedral.edgeFlip_source
  - OAI.KLInvariance.Dihedral.edgeFlip_target
  - OAI.KLInvariance.Dihedral.edgeFlip_involutive
  - OAI.KLInvariance.TitsSpace.PlaneBasis.intervalEdgeSlope
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1563
    format: lean-location
    note: OAI.KLInvariance.Dihedral.rankFlip
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1566
    format: lean-location
    note: OAI.KLInvariance.Dihedral.length_rankFlip
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1571
    format: lean-location
    note: OAI.KLInvariance.Dihedral.rankFlip_involutive
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1577
    format: lean-location
    note: OAI.KLInvariance.Dihedral.rankFlip_lower
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1580
    format: lean-location
    note: OAI.KLInvariance.Dihedral.rankFlip_upper
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1583
    format: lean-location
    note: OAI.KLInvariance.Dihedral.rankFlip_bruhat_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1588
    format: lean-location
    note: OAI.KLInvariance.Dihedral.rankFlip_step_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1594
    format: lean-location
    note: OAI.KLInvariance.Dihedral.intervalFlip
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1616
    format: lean-location
    note: OAI.KLInvariance.Dihedral.intervalFlip_involutive
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1620
    format: lean-location
    note: OAI.KLInvariance.Dihedral.edgeFlip
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1633
    format: lean-location
    note: OAI.KLInvariance.Dihedral.edgeFlip_source
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1638
    format: lean-location
    note: OAI.KLInvariance.Dihedral.edgeFlip_target
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1643
    format: lean-location
    note: OAI.KLInvariance.Dihedral.edgeFlip_involutive
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1752
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.intervalEdgeSlope
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the graph, scalar, list, label-order and interval hypotheses explicit,
    with the exact path sets and source proof?
  verdict: Read the rank-cut definition and its length/involution identities, order
    and odd-step equivalences, interval and edge equivalence constructors, endpoint
    equations and induced actual-root slope definition. Checked the A2 example as
    an explanatory calculation.
tags:
- Kazhdan-Lusztig
- reflection_orders
---

# Internal-rank flips of a dihedral interval and its edges

Let \(D\) be a Coxeter system with two simple generators \(s_0,s_1\), and write \(\ell_D\) for its length. Let \(\theta:D\to D\) be the diagram involution that exchanges \(s_0\) and \(s_1\). The [[node:kl.dihedral.signed_lengths|signed-representative theorem]] constructs it from the Coxeter relations and proves
\[
\theta^2=\operatorname{id},\qquad \ell_D(\theta w)=\ell_D(w).
\]

## The rank-cut map

For natural numbers \(L,H\), define
\[
F_{L,H}(w)=
\begin{cases}
\theta w,&L<\ell_D(w)<H,\\
w,&\text{otherwise}.
\end{cases}
\]
This is `rankFlip`. Its deciding condition uses only length, which \(\theta\) preserves. Applying the same rule twice therefore either applies \(\theta\) twice or leaves the element unchanged twice. Thus
\[
\ell_D(F_{L,H}(w))=\ell_D(w),\qquad
F_{L,H}^2=\operatorname{id}.
\]
In particular \(F_{L,H}\) is a bijection.

## The order isomorphism of a full interval

For endpoints \(\mathrm{lo},\mathrm{hi}\in D\), set
\[
L=\ell_D(\mathrm{lo}),\qquad H=\ell_D(\mathrm{hi}),\qquad F=F_{L,H}.
\]
Both endpoints are fixed because neither lies strictly between the two cutoff lengths.

The [[node:kl.coxeter.dihedral_bruhat_order|dihedral Bruhat-order theorem]] gives
\[
x\le_D y
\Longleftrightarrow
\ell_D(x)<\ell_D(y)\ \text{ or }\ x=y.
\]
The map \(F\) preserves the lengths and, being injective, preserves equality in both directions. Consequently
\[
F(x)\le_D F(y)\Longleftrightarrow x\le_D y.
\]
It carries \([\mathrm{lo},\mathrm{hi}]_D\) into itself because it preserves both comparisons with the fixed endpoints. Its restriction
\[
\iota:[\mathrm{lo},\mathrm{hi}]_D
\xrightarrow{\sim}[\mathrm{lo},\mathrm{hi}]_D
\]
is the order isomorphism `intervalFlip`, with inverse \(\iota\) itself.

## The map on reflection edges

The [[node:kl.dihedral.odd_reflection_edges|odd-gap edge criterion]] says
\[
x\to_D y
\Longleftrightarrow
\ell_D(x)<\ell_D(y)
\ \text{ and }\ \ell_D(y)-\ell_D(x)\text{ is odd}.
\]
Length preservation therefore makes \(F\) preserve directed reflection edges in both directions. Define
\[
g(x\to y)=(\iota x\to\iota y).
\]
This is `edgeFlip`, an involution on the edge set of the interval. It satisfies
\[
s(g(e))=\iota(s(e)),\qquad r(g(e))=\iota(r(e)),\qquad g^2(e)=e.
\]
These equations make edgewise application of \(g\) a map on directed paths.

## A three-rank example

In type \(A_2\), the full interval from \(1\) to \(w_0=s_0s_1s_0\) has ranks \(0,1,2,3\). Its interval flip acts by
\[
1\mapsto1,\quad
s_0\leftrightarrow s_1,\quad
s_0s_1\leftrightarrow s_1s_0,\quad
w_0\mapsto w_0.
\]
For example, the directed path
\[
1\to s_0\to s_1s_0\to w_0
\]
maps to
\[
1\to s_1\to s_0s_1\to w_0.
\]
Both paths have three edges and the same fixed endpoints.

## Actual slopes in an induced root plane

Now let \(W\) be a finite-generator Coxeter system, \(P\) a root plane, and \(B\) its plane-basis datum. Its intrinsic two-generator system is \(D=B.\mathrm{system}\). For an intrinsic edge \(e\), \(B.\mathrm{edgeRoot}(e)\) is the actual positive ambient root labelling that edge.

On a full intrinsic interval, define
\[
\lambda_B(e)=
\operatorname{geometricSlope}\bigl(B.\mathrm{edgeRoot}(e)\bigr).
\]
This is `PlaneBasis.intervalEdgeSlope`. The [[node:kl.dihedral.plane_path_reversal|plane-path reversal theorem]] shows that the edge flip reverses comparisons of these slopes on composable pairs and then transports the selected decreasing paths to the reversed schedule.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**A complete intrinsic interval supplies the root-plane identity.**

**OpenAI notes:** The notes state the increasing and decreasing path formulas and develop the two-vertex internal ranks and angular comparisons in the dihedral section. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [dih:shape](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L112), [dih:midpoint-order](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L358).

**Lean (primary):** The local identity fixes the two endpoints of a full intrinsic interval and switches its internal-rank vertices. The middle-descent test proves reversal of adjacent actual-root slope comparisons. A length-preserving involution then identifies the two endpoint entries for a full sorted edge list and its reverse. [DyerPaths:1563](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1563), [DyerPaths:1594](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1594), [DyerPaths:1620](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1620), [DyerPaths:1048](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1048), [DyerPaths:1722](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1722), [DyerPaths:1752](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1752), [DyerPaths:1889](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1889).

**Role in the proof:** The Blueprint gives the interval and edge maps, verifies both directions of sorted path transport and states the precise endpoint-entry equality. The later ambient plane-block application uses this intrinsic identity through the coset graph.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.rankFlip`: [DyerPaths.lean:1563](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1563).

`OAI.KLInvariance.Dihedral.length_rankFlip`: [DyerPaths.lean:1566](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1566).

`OAI.KLInvariance.Dihedral.rankFlip_involutive`: [DyerPaths.lean:1571](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1571).

`OAI.KLInvariance.Dihedral.rankFlip_lower`: [DyerPaths.lean:1577](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1577).

`OAI.KLInvariance.Dihedral.rankFlip_upper`: [DyerPaths.lean:1580](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1580).

`OAI.KLInvariance.Dihedral.rankFlip_bruhat_iff`: [DyerPaths.lean:1583](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1583).

`OAI.KLInvariance.Dihedral.rankFlip_step_iff`: [DyerPaths.lean:1588](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1588).

`OAI.KLInvariance.Dihedral.intervalFlip`: [DyerPaths.lean:1594](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1594).

`OAI.KLInvariance.Dihedral.intervalFlip_involutive`: [DyerPaths.lean:1616](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1616).

`OAI.KLInvariance.Dihedral.edgeFlip`: [DyerPaths.lean:1620](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1620).

`OAI.KLInvariance.Dihedral.edgeFlip_source`: [DyerPaths.lean:1633](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1633).

`OAI.KLInvariance.Dihedral.edgeFlip_target`: [DyerPaths.lean:1638](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1638).

`OAI.KLInvariance.Dihedral.edgeFlip_involutive`: [DyerPaths.lean:1643](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1643).

`OAI.KLInvariance.TitsSpace.PlaneBasis.intervalEdgeSlope`: [DyerPaths.lean:1752](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1752).
