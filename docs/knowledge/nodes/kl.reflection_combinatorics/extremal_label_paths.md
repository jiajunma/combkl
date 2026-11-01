---
id: kl.paths.extremal_label_paths
title: Extremal simple labels on increasing paths
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.paths.simple_rotation
- kl.paths.bruhat_path_selection
- kl.notes.reflection_order
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.AdaptedDyer.nonsimple_of_greatest
  - OAI.KLInvariance.AdaptedDyer.nonsimple_tail_of_least
  - OAI.KLInvariance.AdaptedDyer.nonsimple_of_least_descent
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2198
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.nonsimple_of_greatest
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2233
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.nonsimple_tail_of_least
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2247
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.nonsimple_of_least_descent
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the chamber, positivity, simple-label exclusions, two orders and exact
    induction hypotheses retained?
  verdict: Read all three extremal-label exclusion lemmas. Preserved the arbitrary-list
    scope of the least-label tail statement, the initial descent condition and the
    exact negated final descent condition for a greatest label.
tags:
- Kazhdan-Lusztig
- reflection_orders
---

# Extremal simple labels on increasing paths

Fix a finite-generator Coxeter system, a simple generator \(s=s_i\), and a ratio order \(O\).
Use the avoidance predicate and increasing path sets from the [[node:kl.paths.simple_rotation|simple-root path definitions]].

If \(\alpha_i\) has strictly smaller slope than every other positive root, then:

- the tail of any nonempty strictly increasing edge list avoids \(\alpha_i\);
- if \(\ell(sx)<\ell(x)\), every increasing path from \(x\) to any \(y\) avoids \(\alpha_i\).

If \(\alpha_i\) has strictly greater slope than every other positive root and \(s\) is not a left descent at \(y\), meaning
\[
\neg\bigl(\ell(sy)<\ell(y)\bigr),
\]
then every increasing path ending at \(y\) avoids \(\alpha_i\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Actual edge rotation and the two path-sum bijections.**

**OpenAI notes:** The notes present the increasing-path expression as the normalized R-polynomial and cite Dyer for the formula. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [eq:bg-path-formula](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L191).

**Lean (primary):** The independent path proof partitions actual finite path sets by avoidance of one chosen simple label. Rotating the avoiding paths gives a full target path set because the chosen label is greatest there and the rotated endpoint is an ascent. Paths containing the least label are obtained by prefixing the uniquely determined simple edge. [DyerPaths:2091](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2091), [DyerPaths:2160](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2160), [DyerPaths:2268](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2268), [DyerPaths:2174](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2174), [DyerPaths:2184](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2184), [DyerPaths:2198](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2198), [DyerPaths:2247](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2247), [DyerPaths:2276](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2276), [DyerPaths:2340](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2340), [DyerPaths:2376](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2376).

**Role in the proof:** The Blueprint defines the exact avoidance predicate and total edge map, proves both finite bijections and identifies the extra polynomial factor with the prefixed edge.
<!-- source-comparison:end -->

*Proof.*

### Step 1. A least label can occur only at the first position

Let \(e::q\) be strictly increasing, and suppose an edge \(h\) in the tail has label \(\alpha_i\). Strict increase gives
\[
\operatorname{score}_O(e)
<\operatorname{score}_O(h)=\sigma_O(\alpha_i).
\]
But every edge label has slope at least \(\sigma_O(\alpha_i)\): equality holds for the chosen root, and every other root has larger slope. This contradicts the displayed inequality. Thus the tail avoids \(\alpha_i\).

### Step 2. The descent at the initial vertex excludes the first position

Take an increasing path from \(x\) to \(y\) with \(\ell(sx)<\ell(x)\).
If it is empty, avoidance is vacuous.
If its first edge has label \(\alpha_i\), the label/endpoint identity forces it to be \(x\to sx\). Its upward orientation would give \(\ell(x)<\ell(sx)\), contradicting the hypothesis.
Thus the first edge also avoids the label; Step 1 treats every later edge.

### Step 3. A greatest label can occur only at the last position

Suppose now that \(\alpha_i\) has greatest slope. If an edge with that label had a later edge in a strictly increasing list, the later score would have to exceed \(\sigma_O(\alpha_i)\).
Every positive-root score is at most this maximum, so this is impossible. An occurrence of the chosen label must therefore be last.

### Step 4. The final-vertex condition excludes the last position

For an increasing path ending at \(y\), a last edge with label \(\alpha_i\) has target \(y\) and source \(sy\): its endpoint equation is \(y=s\,s(e)\), so \(s(e)=sy\).
The upward orientation gives \(\ell(sy)<\ell(y)\). This contradicts the assumed absence of that descent.
Step 3 excludes the label at every earlier position, proving avoidance of the whole path.

In the [[node:kl.paths.rotated_path_sum|rotated path-sum theorem]], the new endpoint is \(sy\), where the original hypothesis \(\ell(sy)<\ell(y)\) implies that \(s\) is not a descent: \(s(sy)=y\) has greater length. The greatest-label assertion therefore applies to every path in the rotated target path set.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.AdaptedDyer.nonsimple_of_greatest`: [DyerPaths.lean:2198](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2198).

`OAI.KLInvariance.AdaptedDyer.nonsimple_tail_of_least`: [DyerPaths.lean:2233](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2233).

`OAI.KLInvariance.AdaptedDyer.nonsimple_of_least_descent`: [DyerPaths.lean:2247](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2247).
