---
id: kl.paths.simple_rotation
title: Simple-labelled edges, avoidance, and edge rotation
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.paths.bruhat_path_polynomial
- kl.coxeter.simple_edge_transport
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.AdaptedDyer.rootLabel_simple_iff
  - OAI.KLInvariance.AdaptedDyer.rotateEdge
  - OAI.KLInvariance.AdaptedDyer.Nonsimple
  - OAI.KLInvariance.AdaptedDyer.nonsimplePaths
  - OAI.KLInvariance.AdaptedDyer.mem_nonsimplePaths
  - OAI.KLInvariance.AdaptedDyer.simpleEdge
  - OAI.KLInvariance.AdaptedDyer.simpleEdge_source
  - OAI.KLInvariance.AdaptedDyer.simpleEdge_target
  - OAI.KLInvariance.AdaptedDyer.simpleEdge_root
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2078
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.rootLabel_simple_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2091
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.rotateEdge
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2160
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.Nonsimple
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2268
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.nonsimplePaths
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2271
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.mem_nonsimplePaths
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2309
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.simpleEdge
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2313
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.simpleEdge_source
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2317
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.simpleEdge_target
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2320
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.simpleEdge_root
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the chamber, positivity, simple-label exclusions, two orders and exact
    induction hypotheses retained?
  verdict: Read the root-label/endpoint equivalence, total rotateEdge definition,
    Nonsimple on arbitrary lists, filtered nonsimplePaths and simpleEdge data. Kept
    the chosen-label meaning and the separate hypotheses for a simple prefix and the
    non-simple endpoint map.
tags:
- Kazhdan-Lusztig
- reflection_orders
---

# Simple-labelled edges, avoidance, and edge rotation

Fix a finite-generator Coxeter system \(W\), a simple generator \(s=s_i\), and its positive simple root \(\alpha_i\). Use the actual directed reflection-edge graph of \(W\); an edge \(e:x\to y\) has positive left root label \(\alpha_e\).

## Edges with the chosen simple label

The label condition is equivalent to an endpoint equation:
\[
\alpha_e=\alpha_i\Longleftrightarrow y=sx.
\]
Indeed, the reflection labelling \(e\) is \(yx^{-1}\). Equality of the roots gives this reflection as \(s\), yielding \(y=sx\). Conversely, \(y=sx\) gives reflection \(s\), whose unique positive root is \(\alpha_i\).

If \(\ell(x)<\ell(sx)\), define the simple edge
\[
\epsilon_{i,x}:x\longrightarrow sx.
\]
It is `simpleEdge`. Its endpoints and root label are \(x,sx,\alpha_i\), respectively.

## The total edge rotation

Define \(g_i:E\to E\) by
\[
g_i(e)=
\begin{cases}
e,&\alpha_e=\alpha_i,\\
(sx\to sy),&\alpha_e\ne\alpha_i,\quad e:x\to y.
\end{cases}
\]
This is `rotateEdge`. In the second case, the endpoint equation above gives \(y\ne sx\). The [[node:kl.coxeter.simple_edge_transport|simple-edge transport theorem]] says that an upward reflection edge \(x\to y\) satisfying this inequality is sent to the upward reflection edge \(sx\to sy\). Hence the second case is an actual edge.

The map fixes edges with the chosen simple label. On every other edge it is left multiplication of both endpoints by \(s\). The [[node:kl.paths.simple_rotation_transport|simple-root path transport]] theorem proves its involution and root-label formulas.

## Lists avoiding the chosen label

For any finite edge list \(q\), define
\[
\operatorname{Avoid}_i(q)
\Longleftrightarrow
\alpha_e\ne\alpha_i\quad\text{for every edge }e\text{ occurring in }q.
\]
Lean calls this predicate `Nonsimple i q`. It is a predicate on lists; the directed-path condition is supplied separately. Edges labelled by another simple root are allowed.

For a ratio order \(O\), let
\[
\mathcal N_{O,i}(x,y)
=\{q\in\operatorname{Paths}_O(x,y):\operatorname{Avoid}_i(q)\}.
\]
This is the finite set `nonsimplePaths`. Its membership condition is exactly the conjunction of selected increasing-path membership and avoidance of \(\alpha_i\).

On a list satisfying \(\operatorname{Avoid}_i\), every edge uses the second case of \(g_i\). The endpoint formulas therefore match the same vertex map \(z\mapsto sz\) throughout the list. This lets the edgewise rotation transport a path from \(x\) to \(y\) to one from \(sx\) to \(sy\).

## The simple prefix used in path splitting

When \(\alpha_i\) is the least root label and \(\ell(x)<\ell(sx)\), an increasing path containing \(\alpha_i\) begins with \(\epsilon_{i,x}\).
Its tail starts at \(sx\), ends at the original endpoint, and avoids the chosen label. The [[node:kl.paths.simple_prefix_split|simple-prefix decomposition]] proves the resulting bijection and accounts for the extra factor \(X\) in the polynomial recursion.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Actual edge rotation and the two path-sum bijections.**

**OpenAI notes:** The notes present the increasing-path expression as the normalized R-polynomial and cite Dyer for the formula. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [eq:bg-path-formula](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L191).

**Lean (primary):** The independent path proof partitions actual finite path sets by avoidance of one chosen simple label. Rotating the avoiding paths gives a full target path set because the chosen label is greatest there and the rotated endpoint is an ascent. Paths containing the least label are obtained by prefixing the uniquely determined simple edge. [DyerPaths:2091](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2091), [DyerPaths:2160](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2160), [DyerPaths:2268](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2268), [DyerPaths:2174](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2174), [DyerPaths:2184](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2184), [DyerPaths:2198](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2198), [DyerPaths:2247](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2247), [DyerPaths:2276](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2276), [DyerPaths:2340](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2340), [DyerPaths:2376](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2376).

**Role in the proof:** The Blueprint defines the exact avoidance predicate and total edge map, proves both finite bijections and identifies the extra polynomial factor with the prefixed edge.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.AdaptedDyer.rootLabel_simple_iff`: [DyerPaths.lean:2078](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2078).

`OAI.KLInvariance.AdaptedDyer.rotateEdge`: [DyerPaths.lean:2091](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2091).

`OAI.KLInvariance.AdaptedDyer.Nonsimple`: [DyerPaths.lean:2160](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2160).

`OAI.KLInvariance.AdaptedDyer.nonsimplePaths`: [DyerPaths.lean:2268](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2268).

`OAI.KLInvariance.AdaptedDyer.mem_nonsimplePaths`: [DyerPaths.lean:2271](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2271).

`OAI.KLInvariance.AdaptedDyer.simpleEdge`: [DyerPaths.lean:2309](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2309).

`OAI.KLInvariance.AdaptedDyer.simpleEdge_source`: [DyerPaths.lean:2313](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2313).

`OAI.KLInvariance.AdaptedDyer.simpleEdge_target`: [DyerPaths.lean:2317](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2317).

`OAI.KLInvariance.AdaptedDyer.simpleEdge_root`: [DyerPaths.lean:2320](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2320).
