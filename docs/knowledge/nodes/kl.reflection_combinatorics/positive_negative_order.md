---
id: kl.dihedral.positive_negative_order
title: Positive reflection parameters precede negative parameters
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.prefix_roots
- kl.dihedral.inversion_descent_bridge
- kl.dihedral.inversion_cuts
- kl.dihedral.signed_lengths
- kl.dihedral.signed_reflection_action
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_positive_lt_negative
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1101
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_positive_lt_negative
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient and intrinsic systems, root signs, signed lengths, finite
    representative bounds and counting domains explicit?
  verdict: Followed the source witness w_(k+1), computed both reflected indices and
    intrinsic lengths, checked the simple descent and applied the left cut with actual
    ambient roots.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Positive reflection parameters precede negative parameters

Fix a plane basis \(B=(a_L,a_R)\) in a finite-generator real Coxeter system, with induced dihedral group \(D\) and geometric slope \(\sigma\). Assume intrinsic lengths in \(D\) are unbounded:
\[
\forall N\in\mathbb N,\ \exists v\in D,\quad N\le\ell_D(v).
\]
Let \(e:x\to_Dy\) and \(f:z\to_Dt\) be actual edges with
\[
yx^{-1}=w_{2k+1},\qquad tz^{-1}=w_{-(2l+1)}
\qquad(k,l\in\mathbb N).
\]
Write \(\operatorname{Inv}_W(g,a)\) when \(g^{-1}a\) is negative, and denote the actual plane edge roots of \(e,f\) by \(\alpha_e,\alpha_f\). They satisfy
\[
\sigma(\alpha_e)<\sigma(\alpha_f).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Ambient inversion cuts in place of a root-coordinate recurrence.**

**OpenAI notes:** The notes set \(\kappa=-(a_L,a_R)/2\), where the parentheses denote the ambient Tits form. The midpoint-order lemma writes prefix roots using \(p_0=0\), \(p_1=1\) and \(p_{n+1}=2\kappa p_n-p_{n-1}\). It obtains \(\kappa=\cos(\pi/m)\) in finite type and \(\kappa\ge1\) in infinite type, then compares the resulting coordinate ratios. The functional ratio gives that angular order or its reverse. [dih:midpoint-order](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L358).

**Lean (primary):** PlaneBasis chooses its endpoint roots in increasing geometric slope. Convexity of inversion signs gives a middle-descent test, which orders the two actual ambient prefix-root sequences. A separating element \(w_{k+1}\) compares the two rays. Unbounded lengths give the signed Before order; a maximum length gives the odd residue order modulo 2m. [DyerPaths:923](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L923), [DyerPaths:1106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1106), [DihedralIntervals:832](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L832), [DihedralIntervals:844](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L844), [DihedralIntervals:1101](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1101), [DihedralIntervals:1143](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1143), [DihedralIntervals:1251](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1251).

**Role in the proof:** The ordering conclusion is developed along Lean’s inversion and length proof. The additional classification of \(\kappa\) in the notes is not a conclusion of these Lean angular-order declarations.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Choose the element separating the two inversion signs

Take \(u=w_{k+1}\). Unbounded lengths and the [[node:kl.dihedral.signed_lengths|signed-length theorem]] give
\(\ell_D(w_i)=|i|\) for every integer \(i\): for a specified \(i\), choose a witness of length at least \(|i|\). In particular \(\ell_D(u)=k+1\).

For every odd \(q\), the [[node:kl.dihedral.signed_reflection_action|signed reflection-action formula]] is \(w_qw_i=w_{q-i}\). Apply it to each edge reflection at \(u\).

### Step 2. The positive-parameter root is inverted

The first reflection gives
\[
w_{2k+1}u=w_{(2k+1)-(k+1)}=w_k.
\]
Its intrinsic length is \(k<k+1=\ell_D(u)\). The [[node:kl.dihedral.inversion_descent_bridge|inversion-descent bridge]] for edge roots therefore says
\[
\operatorname{Inv}_W(u,\alpha_e).
\]

### Step 3. The negative-parameter root is noninverted

For the other reflection,
\[
w_{-(2l+1)}u=w_{-(2l+1)-(k+1)}
=w_{-(2l+k+2)}.
\]
Its length is \(2l+k+2>k+1\). The same bridge shows that
\(\operatorname{Inv}_W(u,\alpha_f)\) is false.

### Step 4. The left endpoint is inverted

The positive alternating word \(u=w_{k+1}\) begins with \(s\) and is reduced. Cancelling its first letter gives a left descent at \(u\). The simple-root part of the [[node:kl.dihedral.inversion_descent_bridge|inversion-descent bridge]], with representative \(1\), gives
\(\operatorname{Inv}_W(u,a_L)\).

The [[node:kl.dihedral.inversion_cuts|inversion-cut theorem]] applies to the two actual edge roots in \(P\): the left endpoint and \(\alpha_e\) are inverted, whereas \(\alpha_f\) is noninverted. Its left-cut inequality is exactly
\(\sigma(\alpha_e)<\sigma(\alpha_f)\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_positive_lt_negative`: [DihedralIntervals.lean:1101](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1101).
