---
id: kl.paths.rotated_path_sum
title: The avoiding-path sum becomes a full path polynomial after rotation
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.paths.simple_rotation
- kl.paths.simple_rotation_transport
- kl.paths.extremal_label_paths
- kl.paths.bruhat_path_polynomial
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.AdaptedDyer.sum_nonsimple_rotate
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2276
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.sum_nonsimple_rotate
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the chamber, positivity, simple-label exclusions, two orders and exact
    induction hypotheses retained?
  verdict: Read sum_nonsimple_rotate and every finite-bijection clause. Retained only
    the source greatest-label/comparison hypotheses and top descent, explicitly proved
    avoidance at the rotated endpoint and constructed the inverse using the same two-order
    equivalence.
tags:
- Kazhdan-Lusztig
- reflection_orders
---

# The avoiding-path sum becomes a full path polynomial after rotation

Fix a finite-generator Coxeter system, a simple generator \(s=s_i\), and ratio orders \(O,O'\).
Assume \(\alpha_i\) is greatest for \(O'\), and that the two orders satisfy
\[
\sigma_{O'}(s\star a)<\sigma_{O'}(s\star b)
\Longleftrightarrow
\sigma_O(a)<\sigma_O(b)
\quad(a,b\ne\alpha_i).
\tag{1}
\]
Let \(x,y\in W\) satisfy \(\ell(sy)<\ell(y)\). Then
\[
\sum_{q\in\mathcal N_{O,i}(x,y)}X^{|q|}
=F_{O'}(sx,sy;X),
\tag{2}
\]
where \(\mathcal N_{O,i}\) is the finite selected path set avoiding \(\alpha_i\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Actual edge rotation and the two path-sum bijections.**

**OpenAI notes:** The notes present the increasing-path expression as the normalized R-polynomial and cite Dyer for the formula. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [eq:bg-path-formula](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L191).

**Lean (primary):** The independent path proof partitions actual finite path sets by avoidance of one chosen simple label. Rotating the avoiding paths gives a full target path set because the chosen label is greatest there and the rotated endpoint is an ascent. Paths containing the least label are obtained by prefixing the uniquely determined simple edge. [DyerPaths:2091](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2091), [DyerPaths:2160](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2160), [DyerPaths:2268](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2268), [DyerPaths:2174](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2174), [DyerPaths:2184](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2184), [DyerPaths:2198](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2198), [DyerPaths:2247](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2247), [DyerPaths:2276](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2276), [DyerPaths:2340](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2340), [DyerPaths:2376](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2376).

**Role in the proof:** The Blueprint defines the exact avoidance predicate and total edge map, proves both finite bijections and identifies the extra polynomial factor with the prefixed edge.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Rotation maps into the target path set

Let \(G(q)=g_i(q)\), the edgewise rotation. For \(q\in\mathcal N_{O,i}(x,y)\), the list is an increasing path for \(O\) and avoids \(\alpha_i\). The [[node:kl.paths.simple_rotation_transport|simple-root path transport]] theorem applies using (1), and gives
\[
G(q)\in\operatorname{Paths}_{O'}(sx,sy).
\]
The same theorem gives \(|G(q)|=|q|\).

### Step 2. Injectivity of the list map

The edge rotation is an involution, so \(G(G(q))=q\). If \(G(q)=G(q')\), applying \(G\) to both sides gives \(q=q'\). Thus the map in Step 1 is injective.

### Step 3. Every target path avoids the chosen label

Take \(r\in\operatorname{Paths}_{O'}(sx,sy)\).
The hypothesis \(\ell(sy)<\ell(y)\) and the equality \(s(sy)=y\) give
\[
\neg\bigl(\ell(s(sy))<\ell(sy)\bigr).
\]
Thus \(s\) is not a left descent at the new endpoint \(sy\).
The label \(\alpha_i\) is greatest for \(O'\), so the final-endpoint part of the [[node:kl.paths.extremal_label_paths|extremal-label theorem]] proves that \(r\) avoids \(\alpha_i\).

### Step 4. The inverse map and surjectivity

Put \(q=G(r)\). Avoidance is preserved by rotation, and \(G(q)=r\).
Apply the selected-path equivalence in the [[node:kl.paths.simple_rotation_transport|simple-root path transport]] theorem to this avoiding list \(q\). Since
\[
G(q)=r\in\operatorname{Paths}_{O'}(sx,sy),
\]
it follows that \(q\in\operatorname{Paths}_O(x,y)\). Together with avoidance, this places \(q\) in \(\mathcal N_{O,i}(x,y)\), and its image is the original \(r\).
This proves surjectivity onto the full target path set.

### Step 5. Reindexing the weights

Steps 1–4 give a bijection from \(\mathcal N_{O,i}(x,y)\) to \(\operatorname{Paths}_{O'}(sx,sy)\), preserving the length of every list.
Reindexing the finite sum therefore gives
\[
\sum_{q\in\mathcal N_{O,i}(x,y)}X^{|q|}
=\sum_{r\in\operatorname{Paths}_{O'}(sx,sy)}X^{|r|}
=F_{O'}(sx,sy;X).
\]
The endpoint ascent in Step 3 is the condition that makes the target the full selected path set.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.AdaptedDyer.sum_nonsimple_rotate`: [DyerPaths.lean:2276](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2276).
