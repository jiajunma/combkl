---
id: kl.dihedral.inversion_descent_bridge
title: Ambient root signs and intrinsic dihedral descents
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.prefix_roots
- kl.dihedral.induced_inversions
- kl.dihedral.minimal_plane_cosets
- kl.dihedral.induced_system
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  - DyerPaths
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.simpleRoot_inverted_coset_iff
  - OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_inverted_iff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1079
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.simpleRoot_inverted_coset_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1091
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_inverted_iff
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient and intrinsic systems, root signs, signed lengths, finite
    representative bounds and counting domains explicit?
  verdict: Verified the least ambient-length hypothesis, inverse-action direction,
    false/true generator roots, and the reflection hypothesis in the edge bridge;
    kept intrinsic length distinct from ambient length.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Ambient root signs and intrinsic dihedral descents

Let \(B=(a_L,a_R)\) be a plane basis in a finite-generator real Coxeter system \(W\). Let \(D\) be its induced dihedral group, with generators \(s,t\), intrinsic length \(\ell_D\), and ambient length denoted by \(\ell_W\). Put \(a_s=a_L\) and \(a_t=a_R\). Write \(\operatorname{Inv}_W(g,a)\) when the inverse ambient action \(g^{-1}a\) is a negative root.

Suppose \(a_0\in W\) is least in its left coset:
\[
\ell_W(a_0)\le\ell_W(za_0)\qquad(z\in D).
\]
For every \(w\in D\) and \(r\in\{s,t\}\),
\[
\operatorname{Inv}_W(wa_0,a_r)
\quad\Longleftrightarrow\quad
\ell_D(rw)<\ell_D(w).
\]
Thus the ambient sign is the intrinsic left-descent test.

For an intrinsic edge \(e:x\to_Dy\), its actual plane edge root also satisfies, for every \(w\in D\),
\[
\operatorname{Inv}_W(w,\alpha_e)
\quad\Longleftrightarrow\quad
\ell_D((yx^{-1})w)<\ell_D(w).
\]
Both formulas use the action of the inverse ambient element in the definition of \(\operatorname{Inv}_W\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Ambient inversion cuts in place of a root-coordinate recurrence.**

**OpenAI notes:** The notes set \(\kappa=-(a_L,a_R)/2\), where the parentheses denote the ambient Tits form. The midpoint-order lemma writes prefix roots using \(p_0=0\), \(p_1=1\) and \(p_{n+1}=2\kappa p_n-p_{n-1}\). It obtains \(\kappa=\cos(\pi/m)\) in finite type and \(\kappa\ge1\) in infinite type, then compares the resulting coordinate ratios. The functional ratio gives that angular order or its reverse. [dih:midpoint-order](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L358).

**Lean (primary):** PlaneBasis chooses its endpoint roots in increasing geometric slope. Convexity of inversion signs gives a middle-descent test, which orders the two actual ambient prefix-root sequences. A separating element \(w_{k+1}\) compares the two rays. Unbounded lengths give the signed Before order; a maximum length gives the odd residue order modulo 2m. [DyerPaths:923](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L923), [DyerPaths:1106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1106), [DihedralIntervals:832](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L832), [DihedralIntervals:844](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L844), [DihedralIntervals:1101](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1101), [DihedralIntervals:1143](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1143), [DihedralIntervals:1251](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1251).

**Role in the proof:** The ordering conclusion is developed along Lean’s inversion and length proof. The additional classification of \(\kappa\) in the notes is not a conclusion of these Lean angular-order declarations.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Remove the least coset representative from the sign test

The [[node:kl.dihedral.minimal_plane_cosets|least-coset sign theorem]] states that \(a_0^{-1}\) preserves the sign of every root in \(P\). The subgroup \(D\) preserves \(P\), so \(w^{-1}a_r\) remains a root of \(P\). The equality
\[
(wa_0)^{-1}a_r=a_0^{-1}(w^{-1}a_r)
\]
therefore gives
\[
\operatorname{Inv}_W(wa_0,a_r)
\Longleftrightarrow
\operatorname{Inv}_W(w,a_r).
\]

### Step 2. Apply the induced inversion correspondence

The generator \(r\) is the ambient reflection represented by the positive root \(a_r\in P\). The [[node:kl.dihedral.induced_inversions|induced inversion theorem]] identifies
\[
\operatorname{Inv}_W(w,a_r)
\Longleftrightarrow r\in N_D(w),
\]
where \(N_D(w)\) is the intrinsic left-inversion set: its members are intrinsic reflections \(q\) with \(\ell_D(qw)<\ell_D(w)\).

A simple generator is a reflection. For \(q=r\), membership is exactly the displayed left-descent inequality. Combining this with Step 1 proves the coset formula. Taking \(a_0=1\) is valid, since \(\ell_W(1)=0\) is a lower bound for every length.

### Step 3. Apply the same correspondence to an edge label

For \(e:x\to_Dy\), the element \(q=yx^{-1}\) is an intrinsic reflection by the definition of Bruhat edge. Its positive ambient representing root is \(\alpha_e\), and this root belongs to \(P\).

The same [[node:kl.dihedral.induced_inversions|induced inversion theorem]] gives
\[
\operatorname{Inv}_W(w,\alpha_e)
\Longleftrightarrow
\bigl(q\text{ is an intrinsic reflection and }\ell_D(qw)<\ell_D(w)\bigr).
\]
The reflection condition already holds for \(q=yx^{-1}\), so the remaining condition is precisely the second formula. This proves the bridge from an ambient root sign to an intrinsic length calculation.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.simpleRoot_inverted_coset_iff`: [DyerPaths.lean:1079](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1079).

`OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_inverted_iff`: [DihedralIntervals.lean:1091](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1091).
