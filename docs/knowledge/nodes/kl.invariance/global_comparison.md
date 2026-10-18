---
id: kl.comparison.global_comparison
title: The transported comparison for actual characters
kind: theorem
status: proved
primary_topic: kl.invariance
topics:
- kl.invariance
uses:
- kl.comparison.edge_increment
- kl.paths.dyer_paths
- kl.duality.actual_character_reciprocity
- kl.detail.schedule_comparison
- kl.detail.costalk_reciprocity
- kl.local.edge_inclusion
lean:
  repository: openai-kl
  modules:
  - SimultaneousInvariance
  declarations:
  - OAI.KLInvariance.BruhatGraph.actual_comparison_of_upper_freeness
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SimultaneousInvariance:264
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.actual_comparison_of_upper_freeness
  - artifact: openai-kl-paper
    locator: 6. Reciprocity and simultaneous induction; sec:induction
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- induction
---

# The transported comparison for actual characters

Assume that every upper-endpoint kernel needed during the schedule is free. Let \(c_x(t)\) be the normalized square-parameter value of the actual boundary-sheaf character. Then, coordinatewise,
\[
c(t)\le \widetilde R'(t^{-1}-t)c(t^{-1}),
\]
where the matrix comes from the target system.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different proof route.**

**OpenAI notes:** The simultaneous induction compares normalized KL vectors, obtains P-invariance from the strict half-degree bound, and then recovers bottom terminal-kernel freeness from endpoint equality. [sec:induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194), [eq:comparison](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L298), [eq:reciprocal-vector](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L311).

**Lean (primary):** The simultaneous induction first proves normalized R-invariance together with suffix-kernel freeness in both transported directions. It cancels known bottom R-row entries against one actual source-character vector. Canonical KL equality is proved afterwards in a separate induction using the now common R-matrix and the canonical degree bound. [Invariance:136](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L136), [Invariance:190](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L190), [Invariance:427](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L427).

**How to read this entry:** Proper upper intervals supply kernel freeness, and proper initial intervals supply known R-entries. The new R-equality gives exact endpoints and then current-rank suffix freeness. The canonical degree bound enters the subsequent P-induction.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Use one fixed actual sheaf

Let \(\phi:[a,b]\simeq[a',b']\), and take the actual boundary sheaf with top \(b\) in the source Coxeter system, restricted to \([a,b]\). Let \(C_{x,b}(q)\) be its actual stalk character, and define
\[
c_x(t)=t^{\ell(x)-\ell(b)}C_{x,b}(t^2).
\]
No target-system stalk character enters this vector.

Let \(p\) be the chronological schedule obtained from the target reflection order through \(\phi\). Its reversal is the transported decreasing list used in the matrix product.

### Step 2. Obtain every local image inclusion

The hypothesis provides freeness of the upper terminal kernel at the target of each edge, for the exact suffix currently being processed. The edge-image theorem [[node:kl.local.edge_inclusion]] therefore applies at every suffix and gives \(I_e\subseteq f_eJ_e\). The lower partial kernel is not required to be free.

Apply [[node:kl.detail.schedule_comparison]] to this complete list of inclusions:
\[
D_{[]}(t)\le\operatorname{Dispatch}_{p^{\mathrm{rev}}}(t^{-1}-t)D_p(t).
\]

### Step 3. Identify the final state explicitly

At the empty schedule, the kernel at \(x\) is the whole stalk. Its Hilbert value is
\(C_{x,b}(t^2)/(1-t^2)^N\).
Multiplying by the state scale cancels the denominator:
\[
D_{[]}(t)_x=(1-t^2)^N t^{\ell(x)-\ell(b)}
\frac{C_{x,b}(t^2)}{(1-t^2)^N}=c_x(t).
\]

### Step 4. Identify the initial state explicitly

The full schedule contains every outgoing edge, so its kernel is the full costalk. Stalk–costalk reciprocity gives its Hilbert value as
\[
(t^2)^{\ell(b)-\ell(x)}C_{x,b}(t^{-2})(1-t^2)^{-N}.
\]
After multiplying by the same scale, the exponent of \(t\) becomes
\(\ell(x)-\ell(b)+2(\ell(b)-\ell(x))=\ell(b)-\ell(x)\).
Thus \(D_p(t)_x=c_x(t^{-1})\).

### Step 5. Substitute the endpoints

Replace the two state vectors in Step 2 by the expressions from Steps 3–4. This yields
\[
c(t)\le\operatorname{Dispatch}_{p^{\mathrm{rev}}}(t^{-1}-t)c(t^{-1}).
\]
The path formula identifies that dispatch operator with the target R-matrix transported by \(\phi\). Its appearance changes the matrix, not the source vector on which it acts.

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.actual_comparison_of_upper_freeness`: [SimultaneousInvariance.lean:264](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SimultaneousInvariance.lean#L264).
