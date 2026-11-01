---
id: kl.paths.simple_rotation_transport
title: Rotation transports paths avoiding a simple label
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.paths.simple_rotation
- kl.paths.bruhat_path_selection
- kl.realization.positive_root_action
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.AdaptedDyer.rotateEdge_val
  - OAI.KLInvariance.AdaptedDyer.rotateEdge_root
  - OAI.KLInvariance.AdaptedDyer.rotateEdge_nonsimple
  - OAI.KLInvariance.AdaptedDyer.rotateEdge_involutive
  - OAI.KLInvariance.AdaptedDyer.path_map_of_mem
  - OAI.KLInvariance.AdaptedDyer.path_rotate
  - OAI.KLInvariance.AdaptedDyer.nonsimple_map
  - OAI.KLInvariance.AdaptedDyer.path_map_twice
  - OAI.KLInvariance.AdaptedDyer.path_rotate_iff
  - OAI.KLInvariance.AdaptedDyer.paths_rotate_iff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2096
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.rotateEdge_val
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2100
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.rotateEdge_root
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2112
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.rotateEdge_nonsimple
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2117
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.rotateEdge_involutive
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2132
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.path_map_of_mem
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2144
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.path_rotate
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2163
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.nonsimple_map
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2169
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.path_map_twice
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2174
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.path_rotate_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2184
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.paths_rotate_iff
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the chamber, positivity, simple-label exclusions, two orders and exact
    induction hypotheses retained?
  verdict: Read actual endpoint/root-label rotation, exclusion preservation and total
    involution. Explained path_map_of_mem with hypotheses only on the list and used
    both directions of the exact two-order slope comparison before applying mem_paths.
tags:
- Kazhdan-Lusztig
- reflection_orders
---

# Rotation transports paths avoiding a simple label

Fix a finite-generator Coxeter system, \(s=s_i\), and the edge rotation \(g_i\) from the [[node:kl.paths.simple_rotation|simple-root path definitions]].
It is an involution. For an edge \(e:x\to y\) with \(\alpha_e\ne\alpha_i\),
\[
g_i(e):sx\to sy,\qquad
\alpha_{g_i(e)}=s\star\alpha_e\ne\alpha_i.
\tag{1}
\]
Consequently, for a list \(q\) avoiding \(\alpha_i\),
\[
\operatorname{Path}(x,y;q)
\Longleftrightarrow
\operatorname{Path}(sx,sy;g_i(q)).
\tag{2}
\]
The image list also avoids \(\alpha_i\), has the same length, and satisfies \(g_i(g_i(q))=q\).

Let \(O,O'\) be ratio orders satisfying, for \(a,b\ne\alpha_i\),
\[
\sigma_{O'}(s\star a)<\sigma_{O'}(s\star b)
\Longleftrightarrow
\sigma_O(a)<\sigma_O(b).
\tag{3}
\]
For every list \(q\) avoiding \(\alpha_i\),
\[
g_i(q)\in\operatorname{Paths}_{O'}(sx,sy)
\Longleftrightarrow
q\in\operatorname{Paths}_O(x,y).
\tag{4}
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Actual edge rotation and the two path-sum bijections.**

**OpenAI notes:** The notes present the increasing-path expression as the normalized R-polynomial and cite Dyer for the formula. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [eq:bg-path-formula](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L191).

**Lean (primary):** The independent path proof partitions actual finite path sets by avoidance of one chosen simple label. Rotating the avoiding paths gives a full target path set because the chosen label is greatest there and the rotated endpoint is an ascent. Paths containing the least label are obtained by prefixing the uniquely determined simple edge. [DyerPaths:2091](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2091), [DyerPaths:2160](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2160), [DyerPaths:2268](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2268), [DyerPaths:2174](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2174), [DyerPaths:2184](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2184), [DyerPaths:2198](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2198), [DyerPaths:2247](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2247), [DyerPaths:2276](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2276), [DyerPaths:2340](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2340), [DyerPaths:2376](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2376).

**Role in the proof:** The Blueprint defines the exact avoidance predicate and total edge map, proves both finite bijections and identifies the extra polynomial factor with the prefixed edge.
<!-- source-comparison:end -->

*Proof.*

### Step 1. The transformed reflection and its positive root

For \(\alpha_e\ne\alpha_i\), the definition gives endpoints \(sx,sy\). The new left reflection is
\[
(sy)(sx)^{-1}
=s(yx^{-1})s^{-1}
=s r_{\alpha_e}s^{-1}.
\]
The [[node:kl.realization.positive_root_action|positive-root action]] identifies the unique positive root of this conjugate as \(s\star\alpha_e\). This proves the root-label formula.

The action \(s\star-\) is a bijection fixing \(\alpha_i\). Therefore \(\alpha_e\ne\alpha_i\) implies \(s\star\alpha_e\ne\alpha_i\), proving the last part of (1).

### Step 2. The involution on all edges

If an edge has label \(\alpha_i\), the definition fixes it on both applications.
Otherwise Step 1 keeps its rotated label different from \(\alpha_i\), so both applications use left multiplication of the endpoints. Since \(s^2=1\), the endpoints return to \(x,y\), hence the edge returns to \(e\).

Applying this edge identity in every position proves \(g_i(g_i(q))=q\). Positionwise application preserves list length and, by Step 1, preserves avoidance.

### Step 3. The path predicate along an avoiding list

For the empty list, a path means \(x=y\), which implies \(sx=sy\). For \(q=e::h\), the head begins at \(x\), and its tail is a path from \(r(e)\) to \(y\).
Avoidance makes the rotated head begin at \(sx\) and end at \(s r(e)\). By induction, the rotated tail runs from \(s r(e)\) to \(sy\). They therefore form a path from \(sx\) to \(sy\).

Only endpoint equations for the edges actually occurring in \(q\) were needed. This is the source's `path_map_of_mem` argument used by `path_rotate`.
For the converse, apply the same result to the rotated list, which still avoids \(\alpha_i\), and then use the involution from Step 2 and \(s^2=1\). This proves (2).

### Step 4. The two strict label orders

Take two positions in \(q\), with edges \(e,h\), the first preceding the second. Both labels avoid \(\alpha_i\), so (1) and (3) give
\[
\operatorname{score}_{O'}(g_i(e))
<\operatorname{score}_{O'}(g_i(h))
\Longleftrightarrow
\operatorname{score}_O(e)<\operatorname{score}_O(h).
\]
Applying this equivalence to every pair of positions shows that \(q\) is strictly increasing for \(O\) exactly when its rotated list is strictly increasing for \(O'\).

### Step 5. Membership in the actual finite path sets

The [[node:kl.paths.bruhat_path_selection|Bruhat path-selection theorem]] characterizes membership by the directed-path predicate and strict score order. Step 3 gives the equivalence of the path predicates, and Step 4 gives the equivalence of the order conditions.
Combining them proves (4), including for empty lists and endpoints outside Bruhat comparability.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.AdaptedDyer.rotateEdge_val`: [DyerPaths.lean:2096](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2096).

`OAI.KLInvariance.AdaptedDyer.rotateEdge_root`: [DyerPaths.lean:2100](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2100).

`OAI.KLInvariance.AdaptedDyer.rotateEdge_nonsimple`: [DyerPaths.lean:2112](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2112).

`OAI.KLInvariance.AdaptedDyer.rotateEdge_involutive`: [DyerPaths.lean:2117](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2117).

`OAI.KLInvariance.AdaptedDyer.path_map_of_mem`: [DyerPaths.lean:2132](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2132).

`OAI.KLInvariance.AdaptedDyer.path_rotate`: [DyerPaths.lean:2144](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2144).

`OAI.KLInvariance.AdaptedDyer.nonsimple_map`: [DyerPaths.lean:2163](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2163).

`OAI.KLInvariance.AdaptedDyer.path_map_twice`: [DyerPaths.lean:2169](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2169).

`OAI.KLInvariance.AdaptedDyer.path_rotate_iff`: [DyerPaths.lean:2174](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2174).

`OAI.KLInvariance.AdaptedDyer.paths_rotate_iff`: [DyerPaths.lean:2184](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2184).
