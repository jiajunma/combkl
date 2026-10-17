---
id: kl.comparison.rtilde_row_comparison
title: Extracting the bottom R-tilde row from character comparison
kind: theorem
status: proved
primary_topic: kl.09_combinatorial_invariance
topics:
- kl.09_combinatorial_invariance
uses:
- kl.comparison.global_comparison
- kl.duality.actual_character_reciprocity
lean:
  repository: openai-kl
  modules:
  - SimultaneousInvariance
  declarations:
  - OAI.KLInvariance.BruhatGraph.rTilde_eval_le_of_upper_freeness
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SimultaneousInvariance:444
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.rTilde_eval_le_of_upper_freeness
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

# Extracting the bottom R-tilde row from character comparison

Suppose two intervals are isomorphic and, for every \(z\) strictly below the top,
\[
\widetilde R_{u,z}=\widetilde R'_{u',\phi(z)}.
\]
If all upper kernels needed in the current schedule are free, then
\[
\widetilde R_{u,b}(t^{-1}-t)
\le \widetilde R'_{u',b'}(t^{-1}-t)
\qquad(0<t<1).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different proof route.**

**OpenAI notes:** The simultaneous induction compares normalized KL vectors, obtains P-invariance from the strict half-degree bound, and then recovers bottom terminal-kernel freeness from endpoint equality. [sec:induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194), [eq:comparison](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L298), [eq:reciprocal-vector](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L311).

**Lean (primary):** The simultaneous induction first proves normalized R-invariance together with suffix-kernel freeness in both transported directions. It cancels known bottom R-row entries against one actual source-character vector. Canonical KL equality is proved afterwards in a separate induction using the now common R-matrix and the canonical degree bound. [Invariance:136](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L136), [Invariance:190](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L190), [Invariance:427](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L427).

**How to read this entry:** The detailed proof on this page follows Lean. Its induction inputs, the vector being compared, and the point where endpoint equality becomes available must be read in that order; they are not interchangeable with the preprint’s P-first steps.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Define the vector and both matrices on the same index set

Fix \(0<t<1\) and \(T=t^{-1}-t\). Let \(X=[a,b]\). Using the actual source sheaf, set
\[
v_z=c_z(t^{-1}),\qquad
A_{x,z}=\widetilde R_{x,z}(T),\qquad
A'_{x,z}=\widetilde R'_{\phi(x),\phi(z)}(T).
\]
Both matrices and the vector are indexed by \(X\). In particular, \(v\) is not changed to a target-system character vector when \(A'\) is used.

### Step 2. Write the two identities to be compared

The source character reciprocity gives the exact equality \(c(t)=Av\). Upper-kernel freeness supplies the image inclusions required for [[node:kl.comparison.global_comparison]], giving \(c(t)\le A'v\).

Substitute the first equality into the second and take coordinate \(a\):
\[
\sum_{z\in X}A_{a,z}v_z\le\sum_{z\in X}A'_{a,z}v_z.
\]
The interval is finite, so these are ordinary finite sums.

### Step 3. Cancel the already known entries explicitly

The row hypothesis says \(A_{a,z}=A'_{a,z}\) for every \(z\ne b\). Put
\(S=\sum_{z\in X,\ z\ne b}A_{a,z}v_z\).
Splitting both sums into their top term and the remaining terms gives
\[
S+A_{a,b}v_b\le S+A'_{a,b}v_b.
\]
Subtracting the same real number \(S\) from both sides gives
\(A_{a,b}v_b\le A'_{a,b}v_b\).
There is no sign assumption on the canceled summands.

### Step 4. Compute the remaining scalar

The top stalk is \(A\) generated in degree zero, so \(C_{b,b}(q)=1\). Its normalization exponent is \(\ell(b)-\ell(b)=0\). Hence
\[
v_b=c_b(t^{-1})=(t^{-1})^0C_{b,b}(t^{-2})=1.
\]
An interval order isomorphism takes the unique bottom to the unique bottom and the unique top to the unique top; thus \(\phi(a)=a'\), \(\phi(b)=b'\).
The inequality from Step 3 is precisely
\[
\widetilde R_{a,b}(T)\le\widetilde R'_{a',b'}(T).
\]

The argument isolated one matrix entry using the same source vector on both sides. It did not require identifying source and target stalk characters.

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.rTilde_eval_le_of_upper_freeness`: [SimultaneousInvariance.lean:444](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SimultaneousInvariance.lean#L444).
