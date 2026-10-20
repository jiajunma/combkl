---
id: kl.dihedral.inversion_cuts
title: Inversion cuts in a root plane
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.detail.plane_basis
- kl.order.slope_cone
- kl.order.root_slopes
- kl.detail.root_inversions
- kl.realization.root_planes
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.slope_lt_of_inverted_left
  - OAI.KLInvariance.TitsSpace.PlaneBasis.slope_lt_of_inverted_right
  - OAI.KLInvariance.TitsSpace.PlaneBasis.slope_lt_iff_inverted_left
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:881
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.slope_lt_of_inverted_left
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:899
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.slope_lt_of_inverted_right
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:923
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.slope_lt_iff_inverted_left
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient and intrinsic systems, root signs, signed lengths, finite
    representative bounds and counting domains explicit?
  verdict: Checked all three cut statements for arbitrary ambient w, both strict endpoint
    comparisons, the two spanning-pair arguments and the nonnegative-cone argument
    giving the converse.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Inversion cuts in a root plane

Let \(W\) be a finite-generator real Coxeter system, \(P\) a root plane, and \(B=(a_L,a_R)\) a plane basis for the injective geometric slope \(\sigma\). For \(w\in W\) and a positive root \(a\), write
\[
\operatorname{Inv}_W(w,a)\quad\Longleftrightarrow\quad w^{-1}a\text{ is negative}.
\]
Choose positive roots \(a,b\in P\) such that
\(\operatorname{Inv}_W(w,a)\) holds and \(\operatorname{Inv}_W(w,b)\) does not. Then:
\[
\begin{aligned}
\operatorname{Inv}_W(w,a_L)&\ \Longrightarrow\ \sigma(a)<\sigma(b),\\
\operatorname{Inv}_W(w,a_R)&\ \Longrightarrow\ \sigma(b)<\sigma(a),\\
\sigma(a)<\sigma(b)&\ \Longleftrightarrow\ \operatorname{Inv}_W(w,a_L).
\end{aligned}
\]
Here \(w\) is any ambient group element. The assertions describe how the signs at \(w\) divide the slope-ordered roots of this plane.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Ambient inversion cuts in place of a root-coordinate recurrence.**

**OpenAI notes:** The notes set \(\kappa=-(a_L,a_R)/2\), where the parentheses denote the ambient Tits form. The midpoint-order lemma writes prefix roots using \(p_0=0\), \(p_1=1\) and \(p_{n+1}=2\kappa p_n-p_{n-1}\). It obtains \(\kappa=\cos(\pi/m)\) in finite type and \(\kappa\ge1\) in infinite type, then compares the resulting coordinate ratios. The functional ratio gives that angular order or its reverse. [dih:midpoint-order](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L358).

**Lean (primary):** PlaneBasis chooses its endpoint roots in increasing geometric slope. Convexity of inversion signs gives a middle-descent test, which orders the two actual ambient prefix-root sequences. A separating element \(w_{k+1}\) compares the two rays. Unbounded lengths give the signed Before order; a maximum length gives the odd residue order modulo 2m. [DyerPaths:923](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L923), [DyerPaths:1106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1106), [DihedralIntervals:832](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L832), [DihedralIntervals:844](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L844), [DihedralIntervals:1101](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1101), [DihedralIntervals:1143](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1143), [DihedralIntervals:1251](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1251).

**Role in the proof:** The ordering conclusion is developed along Lean’s inversion and length proof. The additional classification of \(\kappa\) in the notes is not a conclusion of these Lean angular-order declarations.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Exclude equal slopes for roots with different signs

If \(\sigma(a)=\sigma(b)\), injectivity gives \(a=b\). The inversion and noninversion assumptions would then contradict each other. Thus their slopes are distinct.

The same reasoning applies to any inverted root and any noninverted root used below.

### Step 2. Use an inverted left endpoint

Assume \(a_L\) is inverted. Suppose the desired inequality fails. Step 1 gives \(\sigma(b)<\sigma(a)\). The endpoint bound \(\sigma(a_L)\le\sigma(b)\) is strict, since \(a_L\) is inverted and \(b\) is not. Consequently
\[
\sigma(a_L)<\sigma(b)<\sigma(a).
\]

In particular \(a_L\ne a\). Distinct positive roots in the root plane are linearly independent, so \(a_L,a\) span \(P\). The [[node:kl.order.slope_cone|slope-cone theorem]] expresses the intermediate root as
\[
b=r a_L+t a,\qquad r,t>0.
\]
Both \(w^{-1}a_L\) and \(w^{-1}a\) have nonpositive coordinates. Linearity gives
\[
w^{-1}b=r\,w^{-1}a_L+t\,w^{-1}a,
\]
also with nonpositive coordinates. This says that \(b\) is inverted, contradicting its chosen sign. Hence \(\sigma(a)<\sigma(b)\).

### Step 3. Use an inverted right endpoint

Assume \(a_R\) is inverted and suppose \(\sigma(b)<\sigma(a)\) fails. Distinctness of slopes gives \(\sigma(a)<\sigma(b)\). The upper endpoint inequality is strict at \(b\), because \(b\) and \(a_R\) have different inversion signs. Thus
\[
\sigma(a)<\sigma(b)<\sigma(a_R).
\]
The roots \(a,a_R\) span \(P\). The [[node:kl.order.slope_cone|slope-cone theorem]] gives \(b=r a+t a_R\) with \(r,t>0\). Applying \(w^{-1}\) again expresses a noninverted root as a nonnegative combination of two inverted roots, a contradiction. This proves \(\sigma(b)<\sigma(a)\).

### Step 4. Recover the endpoint sign from a mixed comparison

Suppose \(\sigma(a)<\sigma(b)\) and \(a_L\) is noninverted. Every positive root in \(P\) belongs to the nonnegative cone of \(a_L,a_R\); in particular
\[
a=r a_L+t a_R,\qquad r,t\ge0.
\]
If \(a_R\) were also noninverted, the noninverted part of the [[node:kl.order.slope_cone|slope-cone theorem]] would make \(a\) noninverted. Therefore \(a_R\) is inverted.

Step 3 would give \(\sigma(b)<\sigma(a)\), contradicting the assumption. Hence \(a_L\) is inverted. The reverse implication is Step 2, proving the equivalence.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.slope_lt_of_inverted_left`: [DyerPaths.lean:881](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L881).

`OAI.KLInvariance.TitsSpace.PlaneBasis.slope_lt_of_inverted_right`: [DyerPaths.lean:899](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L899).

`OAI.KLInvariance.TitsSpace.PlaneBasis.slope_lt_iff_inverted_left`: [DyerPaths.lean:923](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L923).
