---
id: kl.paths.schedule_suffixes
title: A chronological suffix gives the strict later conditions at both endpoints
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.detail.transported_schedule
- kl.paths.graph_invariance
- kl.local.ambient_later_edges
- kl.detail.root_reflection_correspondence
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.SchedulePaths.mem_suffix_iff_score_lt
  - OAI.KLInvariance.SchedulePaths.mem_suffix_iff_score_lt_injective
  - OAI.KLInvariance.BruhatGraph.transportedSlope_source_unique
  - OAI.KLInvariance.BruhatGraph.transportedSlope_path_ne
  - OAI.KLInvariance.BruhatGraph.suffix_source_iff
  - OAI.KLInvariance.BruhatGraph.suffix_target_iff
  - OAI.KLInvariance.BruhatGraph.ambientLater_upperInclusion
  - OAI.KLInvariance.BruhatGraph.remainingConditions_source_ambient
  - OAI.KLInvariance.BruhatGraph.remainingConditions_target_ambient
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:220
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.mem_suffix_iff_score_lt
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:236
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.mem_suffix_iff_score_lt_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1252
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.transportedSlope_source_unique
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1264
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.transportedSlope_path_ne
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1272
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.suffix_source_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1280
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.suffix_target_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1287
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.ambientLater_upperInclusion
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1306
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.remainingConditions_source_ambient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1315
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.remainingConditions_target_ambient
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, finiteness and freeness hypotheses, original embedded
    submodules, localization multipliers and schedule assumptions explicit?
  verdict: Checked both generic sorted-list cases, no-duplicate use for a current-source
    tie, target-root injectivity and consecutive-edge inequality, full-schedule membership
    and the exact ambient set/source-bound identification.
tags:
- Kazhdan-Lusztig
- global-inclusion
---

# A chronological suffix gives the strict later conditions at both endpoints

Fix finite-generator real Coxeter systems \(W,W'\) and an interval order isomorphism
\(\varphi:[u,b]_W\simeq[u',b']_{W'}\).
Let \(\mathcal C\) be the chronological schedule of source-interval edges, with transported slope \(s\). Suppose the list consisting of an edge \(e:x\to y\) followed by \(q\) is a suffix of \(\mathcal C\).

For every edge \(f\) leaving \(x\) or leaving \(y\),
\[
f\in q\quad\Longleftrightarrow\quad s(e)<s(f).
\]
Let \(\iota:[u,b]_W\hookrightarrow[1,b]_W\) be the upper-interval inclusion, acting identically on underlying group elements and edge pairs. If \(\alpha'_e\) is the positive root of the target image of \(e\), then, at \(v=x\) and at \(v=y\),
\[
\mathcal R_q(v)
=
\{f\in\operatorname{Out}_{[u,b]}(v):
\iota_E(f)\in T_{\varphi,\alpha'_e}\}.
\]
The right side is the pullback of the ambient later-edge set.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Exact suffix conditions specialize the ambient inclusion.**

**OpenAI notes:** The notes formulate the current endpoint conditions as the edges strictly later than the current edge in a transported reflection order. [dih:count](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L464), [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The actual schedule is a complete duplicate-free sorted list with a diagonal lexicographic score; its reverse is chronological. Two sorted-list lemmas, same-source score injectivity and consecutive-edge score inequality identify both suffix selections with the ambient later-edge set. Upper-interval restriction then transfers both kernels and the upper freeness hypothesis. [EdgeLocalization:40](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L40), [PositiveTransfer:1228](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1228), [PositiveTransfer:1225](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1225), [PositiveTransfer:1306](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1306), [PositiveTransfer:1315](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1315), [TerminalKernels:1126](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1126).

**Role in the proof:** The Blueprint states the exact suffix assumption and distinguishes weak list ordering from the strict score test at the two current endpoints.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Compare a suffix with a strict score inequality

Consider a finite list whose scores are nondecreasing, and write it as a prefix followed by \(e\) and then \(q\). Let \(f\) occur somewhere in the list and assume \(s(e)\ne s(f)\).

If \(f\in q\), sortedness gives \(s(e)\le s(f)\). The unequal scores make the inequality strict.

Conversely, suppose \(s(e)<s(f)\). The element \(f\) cannot occur in the prefix, because sortedness would give \(s(f)\le s(e)\). It cannot be the current element \(e\), whose score is equal to itself. Thus it occurs in \(q\).

If the list has no repetitions and equality of scores would force \(f=e\), the same equivalence holds without an unequal-score assumption: in that equality case \(e\notin q\), and the strict score inequality is also false.

### Step 2. Equal scores at a common source force equal edges

Suppose \(e,f\) both leave \(x\), and \(s(e)=s(f)\). Injectivity of the target geometric slope identifies their positive target roots, hence their target left reflections. If \(f:x\to z\), this gives
\[
\varphi(y)\varphi(x)^{-1}
=\varphi(z)\varphi(x)^{-1}.
\]
Right cancellation gives \(\varphi(y)=\varphi(z)\), and injectivity of \(\varphi\) gives \(y=z\). Thus the endpoint pairs of \(e,f\) agree, so \(e=f\).

### Step 3. Consecutive edges have unequal scores

Now let \(f:y\to z\). If \(s(e)=s(f)\), their target roots and reflections would agree. Denote this reflection by \(t\). Then
\[
\varphi(y)=t\varphi(x),\qquad
\varphi(z)=t\varphi(y)=t^2\varphi(x)=\varphi(x).
\]
The two target edges are upward, so their lengths strictly increase along the path. The displayed equality contradicts that strict increase. Hence \(s(e)\ne s(f)\).

### Step 4. Apply the list argument to both endpoint selections

The chronological schedule contains every edge once and is nondecreasing in \(s\). For an edge leaving \(x\), Step 2 supplies the equality-implies-same-edge hypothesis of the final part of Step 1. For an edge leaving \(y\), Step 3 supplies the unequal-score hypothesis of its first part.

Step 1 therefore gives \(f\in q\) exactly when \(s(e)<s(f)\) at both endpoints.

### Step 5. Identify strict score comparison with the ambient selection

For any source-interval edge \(f:p\to z\), its ambient inclusion has source \(p\ge_Wu\). Reflection-graph invariance gives the target edge \(\varphi(p)\to\varphi(z)\).

Consequently its target after-indicator with threshold \(\alpha'_e\) equals one precisely when
\[
\sigma'(\alpha'_e)<\sigma'(\alpha'_f),
\]
which is \(s(e)<s(f)\). The source-above-\(u\) witness required by the ambient later-edge set is provided by \(p\in[u,b]\).

Thus \(\iota_E(f)\in T_{\varphi,\alpha'_e}\) is equivalent to that strict score inequality. Combining with Step 4 at \(x,y\) gives the two asserted equalities of outgoing condition sets.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.SchedulePaths.mem_suffix_iff_score_lt`: [PositiveTransfer.lean:220](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L220).

`OAI.KLInvariance.SchedulePaths.mem_suffix_iff_score_lt_injective`: [PositiveTransfer.lean:236](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L236).

`OAI.KLInvariance.BruhatGraph.transportedSlope_source_unique`: [PositiveTransfer.lean:1252](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1252).

`OAI.KLInvariance.BruhatGraph.transportedSlope_path_ne`: [PositiveTransfer.lean:1264](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1264).

`OAI.KLInvariance.BruhatGraph.suffix_source_iff`: [PositiveTransfer.lean:1272](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1272).

`OAI.KLInvariance.BruhatGraph.suffix_target_iff`: [PositiveTransfer.lean:1280](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1280).

`OAI.KLInvariance.BruhatGraph.ambientLater_upperInclusion`: [PositiveTransfer.lean:1287](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1287).

`OAI.KLInvariance.BruhatGraph.remainingConditions_source_ambient`: [PositiveTransfer.lean:1306](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1306).

`OAI.KLInvariance.BruhatGraph.remainingConditions_target_ambient`: [PositiveTransfer.lean:1315](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1315).
