---
id: kl.paths.simple_prefix_split
title: A least simple label splits off one edge from increasing paths
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.paths.simple_rotation
- kl.paths.extremal_label_paths
- kl.paths.bruhat_path_selection
- kl.paths.bruhat_path_polynomial
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.AdaptedDyer.cons_simple_mem
  - OAI.KLInvariance.AdaptedDyer.not_nonsimple_iff_cons
  - OAI.KLInvariance.AdaptedDyer.polynomial_split
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2325
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.cons_simple_mem
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2340
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.not_nonsimple_iff_cons
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2376
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.polynomial_split
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the chamber, positivity, simple-label exclusions, two orders and exact
    induction hypotheses retained?
  verdict: Read the prefix membership proof, both directions of not_nonsimple_iff_cons
    and polynomial_split. Retained the least-label and initial-ascent hypotheses,
    actual-edge equality by endpoints, unique tail recovery and the exact one-edge
    weight factor.
tags:
- Kazhdan-Lusztig
- reflection_orders
---

# A least simple label splits off one edge from increasing paths

Fix a finite-generator Coxeter system, a ratio order \(O\), and a simple generator \(s=s_i\). Assume
\[
\sigma_O(\alpha_i)<\sigma_O(a)\quad(a\ne\alpha_i),
\qquad \ell(x)<\ell(sx).
\]
For any endpoint \(y\), prefixing the simple edge \(\epsilon_{i,x}:x\to sx\) gives a bijection
\[
\mathcal N_{O,i}(sx,y)
\longrightarrow
\{p\in\operatorname{Paths}_O(x,y):\neg\operatorname{Avoid}_i(p)\},
\qquad q\longmapsto\epsilon_{i,x}::q.
\tag{1}
\]
Consequently,
\[
F_O(x,y;X)
=\sum_{p\in\mathcal N_{O,i}(x,y)}X^{|p|}
+X\sum_{q\in\mathcal N_{O,i}(sx,y)}X^{|q|}.
\tag{2}
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Actual edge rotation and the two path-sum bijections.**

**OpenAI notes:** The notes present the increasing-path expression as the normalized R-polynomial and cite Dyer for the formula. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [eq:bg-path-formula](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L191).

**Lean (primary):** The independent path proof partitions actual finite path sets by avoidance of one chosen simple label. Rotating the avoiding paths gives a full target path set because the chosen label is greatest there and the rotated endpoint is an ascent. Paths containing the least label are obtained by prefixing the uniquely determined simple edge. [DyerPaths:2091](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2091), [DyerPaths:2160](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2160), [DyerPaths:2268](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2268), [DyerPaths:2174](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2174), [DyerPaths:2184](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2184), [DyerPaths:2198](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2198), [DyerPaths:2247](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2247), [DyerPaths:2276](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2276), [DyerPaths:2340](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2340), [DyerPaths:2376](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2376).

**Role in the proof:** The Blueprint defines the exact avoidance predicate and total edge map, proves both finite bijections and identifies the extra polynomial factor with the prefixed edge.
<!-- source-comparison:end -->

*Proof.*

### Step 1. A prefix gives a directed increasing path

Take \(q\in\mathcal N_{O,i}(sx,y)\). Its directed path begins at \(sx\), which is the target of \(\epsilon_{i,x}\), so prefixing gives a directed path from \(x\) to \(y\).

The tail is strictly increasing and avoids \(\alpha_i\). The prefixed edge has label \(\alpha_i\), whose slope is strictly below every tail label. Thus all comparisons involving the new head are strict in the required direction, and all remaining comparisons hold in the tail.
The [[node:kl.paths.bruhat_path_selection|Bruhat path-selection theorem]] places the resulting list in \(\operatorname{Paths}_O(x,y)\). It contains the chosen label at its first edge, so it belongs to the codomain in (1).

### Step 2. Recovery of the unique prefix

Take an increasing path \(p\) in that codomain. It contains an edge labelled \(\alpha_i\), so it is nonempty. Write it as \(e::q\).
By the least-label part of the [[node:kl.paths.extremal_label_paths|extremal-label theorem]], the tail avoids \(\alpha_i\). Therefore the occurrence of the chosen label must be the head \(e\).

The path begins at \(x\), and the label/endpoint equation gives \(r(e)=sx\). An actual Bruhat edge is determined by its two endpoints, so \(e=\epsilon_{i,x}\).
The tail \(q\) is a directed path from \(sx\) to \(y\), inherits strict increase, and avoids \(\alpha_i\). Hence \(q\in\mathcal N_{O,i}(sx,y)\).

### Step 3. The inverse maps

Deleting the first edge of \(\epsilon_{i,x}::q\) recovers \(q\). Conversely, Step 2 shows that every path containing the chosen label recovers exactly such a tail and has the prescribed simple head.
Thus deletion and prefixing are inverse maps, proving (1).

### Step 4. The partition and its two weighted sums

Partition \(\operatorname{Paths}_O(x,y)\) into paths avoiding \(\alpha_i\) and paths containing it.
The sum over the first subset is the first term in (2).
Use the bijection (1) in the second subset. Since
\[
|\epsilon_{i,x}::q|=1+|q|,
\qquad X^{1+|q|}=X\,X^{|q|},
\]
that sum is
\[
\sum_{q\in\mathcal N_{O,i}(sx,y)}X\,X^{|q|}
=X\sum_{q\in\mathcal N_{O,i}(sx,y)}X^{|q|}.
\]
Adding the two parts proves (2).

For the rank-one interval \(1\to s\), the first subset is empty and the second consists of the simple edge. Its tail is the empty path at \(s\). Formula (2) becomes \(F_O(1,s;X)=0+X\cdot1=X\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.AdaptedDyer.cons_simple_mem`: [DyerPaths.lean:2325](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2325).

`OAI.KLInvariance.AdaptedDyer.not_nonsimple_iff_cons`: [DyerPaths.lean:2340](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2340).

`OAI.KLInvariance.AdaptedDyer.polynomial_split`: [DyerPaths.lean:2376](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2376).
