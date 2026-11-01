---
id: kl.paths.bruhat_path_polynomial
title: The increasing Bruhat path polynomial of a ratio order
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.paths.directed_paths
- kl.notes.reflection_order
- kl.foundations.bruhat_step
- kl.foundations.finite_intervals
- kl.detail.root_reflection_correspondence
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.AdaptedDyer.Edge
  - OAI.KLInvariance.AdaptedDyer.source
  - OAI.KLInvariance.AdaptedDyer.target
  - OAI.KLInvariance.AdaptedDyer.rootLabel
  - OAI.KLInvariance.AdaptedDyer.score
  - OAI.KLInvariance.AdaptedDyer.edgeFinset
  - OAI.KLInvariance.AdaptedDyer.schedule
  - OAI.KLInvariance.AdaptedDyer.paths
  - OAI.KLInvariance.AdaptedDyer.polynomial
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1948
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.Edge
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1949
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.source
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1950
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.target
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1951
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.rootLabel
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1972
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.score
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1980
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.edgeFinset
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2005
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.schedule
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2043
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.paths
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2063
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.polynomial
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the graph, scalar, list, label-order and interval hypotheses explicit,
    with the exact path sets and source proof?
  verdict: Read the actual global Bruhat-edge type, positive-root label, ratio score,
    finite lower edge set, increasing sorted schedule and path-polynomial definition.
    Preserved finite-generator context, left labels, reflection edges beyond covers
    and the use of y as the schedule top.
tags:
- Kazhdan-Lusztig
- reflection_orders
---

# The increasing Bruhat path polynomial of a ratio order

Fix a Coxeter system \(W\) with finitely many simple generators and a ratio order \(O\) on its positive roots. Write \(\sigma_O(\alpha)\) for the root slope, the ratio of its numerator and positive denominator functionals.

## Actual reflection edges and their scores

The edge type in `AdaptedDyer` consists of pairs \(e=(x,y)\) satisfying the directed Bruhat-step condition: \(y=\tau x\) for a reflection \(\tau\), and \(\ell(x)<\ell(y)\). Its source and target are \(x,y\).

Its root label \(\alpha_e\) is the unique positive root corresponding to the left reflection
\[
\tau_e=yx^{-1}.
\]
Thus \(y=r_{\alpha_e}x\). These edges include reflection steps with length difference greater than one.
Define the real edge score
\[
a_O(e)=\sigma_O(\alpha_e).
\]
This is `AdaptedDyer.score`.

## A finite schedule below a top element

For \(b\in W\), let
\[
E_b=\{e:r(e)\le_W b\}.
\]
Every such edge also has \(s(e)\le_W r(e)\le_W b\). Hence both endpoints lie in the finite lower Bruhat interval \([1,b]\), and \(E_b\) is finite. The source's `edgeFinset` constructs it from pairs of elements of that interval, retaining precisely the directed Bruhat edges.

The list
\[
S_O(b)=\operatorname{schedule}(O,b)
\]
enumerates \(E_b\) once, in weakly increasing order of \(a_O\). Lean constructs it by sorting the finite edge list. Equal-score edges retain some order within the list; their path-selection properties follow from the [[node:kl.paths.bruhat_path_selection|Bruhat path-selection theorem]].

## Selected increasing paths and their polynomial

For \(x,y\in W\), define
\[
\operatorname{Paths}_O(x,y)
=\mathcal P_{S_O(y)}(x,y).
\]
This is `AdaptedDyer.paths`. The top used to form the schedule is the final endpoint \(y\).
The [[node:kl.paths.bruhat_path_selection|Bruhat path-selection theorem]] identifies this finite set with the directed paths from \(x\) to \(y\) whose root scores are strictly increasing.

The increasing Bruhat path polynomial is
\[
F_O(x,y;X)=
\sum_{q\in\operatorname{Paths}_O(x,y)}X^{|q|}
\in\mathbb Z[X].
\]
This is `AdaptedDyer.polynomial`, with the formal indeterminate denoted \(X\). Its coefficient of \(X^m\) counts the selected paths with \(m\) edges.

For a real or semiring parameter \(T\), the same finite path sum is obtained by replacing \(X^{|q|}\) with \(T^{|q|}\). The polynomial is defined directly from paths; its identification with the Hecke-defined normalized R-family is the later [[node:kl.paths.dyer_paths|geometric path identity]].

## The rank-one example

For \(W=\{1,s\}\), the sole upward reflection edge is \(1\to s\).
There is one increasing path from \(1\) to \(s\), consisting of this edge, so
\[
F_O(1,s;X)=X.
\]
The only paths from either vertex to itself are empty, giving
\[
F_O(1,1;X)=F_O(s,s;X)=1.
\]
There is no upward path from \(s\) to \(1\), so \(F_O(s,1;X)=0\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The increasing path polynomial before the R-family identification.**

**OpenAI notes:** The path-formula statement presents the normalized R-polynomial as the weighted sum of increasing reflection paths and notes that all paths lie in the finite interval between their endpoints. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [eq:bg-path-formula](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L191).

**Lean (primary):** AdaptedDyer first defines a path polynomial from the sorted finite edge list below the final endpoint. Endpoint bounds and noncomposable score ties prove that its selected lists are precisely the strictly increasing directed paths. Its equality to the independently constructed Hecke family is proved afterwards under the adapted chamber hypothesis, followed by order independence. [DyerPaths:1948](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1948), [DyerPaths:1951](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1951), [DyerPaths:1972](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1972), [DyerPaths:1980](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1980), [DyerPaths:2005](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2005), [DyerPaths:2043](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2043), [DyerPaths:2046](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2046), [DyerPaths:2063](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2063), [DyerPaths:2066](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2066), [DyerPaths:2447](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2447), [DyerPaths:2451](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2451).

**Role in the proof:** The path polynomial, its actual edge labels, finite schedule, membership criterion, dispatch identity and diagonal/zero values are developed before the later identification theorem.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.AdaptedDyer.Edge`: [DyerPaths.lean:1948](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1948).

`OAI.KLInvariance.AdaptedDyer.source`: [DyerPaths.lean:1949](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1949).

`OAI.KLInvariance.AdaptedDyer.target`: [DyerPaths.lean:1950](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1950).

`OAI.KLInvariance.AdaptedDyer.rootLabel`: [DyerPaths.lean:1951](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1951).

`OAI.KLInvariance.AdaptedDyer.score`: [DyerPaths.lean:1972](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1972).

`OAI.KLInvariance.AdaptedDyer.edgeFinset`: [DyerPaths.lean:1980](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1980).

`OAI.KLInvariance.AdaptedDyer.schedule`: [DyerPaths.lean:2005](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2005).

`OAI.KLInvariance.AdaptedDyer.paths`: [DyerPaths.lean:2043](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2043).

`OAI.KLInvariance.AdaptedDyer.polynomial`: [DyerPaths.lean:2063](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2063).
