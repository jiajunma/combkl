---
id: kl.local.factor_relative_degree
title: A plane weight equals the intrinsic dihedral edge degree
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.geometry.plane_inversion_change
- kl.geometry.plane_weights
- kl.dihedral.plane_coset_graph
- kl.realization.root_planes
- kl.detail.root_reflection_correspondence
- kl.detail.root_inversion_count
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  - DyerPaths
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot
  - OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_plane
  - OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_coset
  - OAI.KLInvariance.TitsSpace.PlaneBasis.planeWeight_coset_edge
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1094
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1097
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_plane
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:2048
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_coset
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1096
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.planeWeight_coset_edge
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read edgeRoot and its plane membership and coset equality, then the complete
    planeWeight_coset_edge proof. Verified the second-root choice, plane equality,
    ambient noninversion, reflection endpoint identity, both coset inversion-count
    substitutions and the natural-number division.
tags:
- Kazhdan-Lusztig
- correction-factors
---

# A plane weight equals the intrinsic dihedral edge degree

Fix a finite-generator ambient Coxeter system \(W\), a root subspace \(P\) with a plane basis, and its induced dihedral subgroup \(D\), with intrinsic length \(\ell_D\). Choose a least-length coset representative \(a_0\), meaning
\[
\ell(a_0)\le\ell(da_0)\qquad(d\in D).
\]

Let \(x\to_Dy\) be an intrinsic reflection edge. Let \(a\) be its positive ambient root, representing \(yx^{-1}\); this is the source's edgeRoot. Write \(k_P(w,a)\) for the geometric plane weight. Then
\[
2k_P(xa_0,a)=\ell_D(y)-\ell_D(x)-1.
\]
In particular its natural-number exponent is
\[
(k_P(xa_0,a))_{\mathbb N}
=\frac{\ell_D(y)-\ell_D(x)-1}{2}.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The same root product with explicit weight and coordinate constructions.**

**OpenAI notes:** The notes assign each plane its half-excess relative dihedral length, choose an independent root whenever that weight is positive, and multiply its reduced linear form to that power in the edge quotient. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The weights are first constructed by grouping half-root indicators. planeWeight_coset_edge identifies them with the relative dihedral length formula. planeRoot chooses a positive root with the required plane, edgeFactor is a product in the symmetric quotient, and edgeFactorLift is its explicit product before the polynomial quotient. The definitions and nonvanishing hold for every x; noninversion is used for the length-degree formula. [ReflectionSchedules:908](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L908), [ReflectionSchedules:944](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L944), [ReflectionSchedules:985](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L985), [ReflectionSchedules:993](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L993), [PlaneLocalization:1389](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1389), [PlaneLocalization:1413](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1413), [PlaneLocalization:1096](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1096).

**Role in the proof:** The Blueprint keeps the chosen representatives, all scalar maps and the natural/integer exponent conversion explicit. The quotient of the polynomial lift is exactly the constructed edge factor.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Complete the edge root to a basis of its plane

The reflection \(yx^{-1}\) belongs to \(D\), so its positive ambient root \(a\) lies in \(P\).

The plane basis supplies two distinct positive roots in \(P\). Choose one of them, say \(b\), different from \(a\): use the right one if \(a\) is the left one, and otherwise use the left one.

The distinct positive roots \(a,b\) are independent. Their two-dimensional span is contained in the two-dimensional plane \(P\), so
\[
\operatorname{span}\{a,b\}=P.
\]

### Step 2. Identify the root of the ambient coset edge

The least-coset comparison sends the intrinsic edge to
\[
xa_0\to_Wya_0.
\]
Its left reflection is
\[
(ya_0)(xa_0)^{-1}=yx^{-1}.
\]
The canonical positive root of this reflection is therefore the same \(a\). This is edgeRoot_coset.

In particular,
\[
r_a(xa_0)=ya_0.
\]
The upward ambient edge implies that \(a\) is not inverted at \(xa_0\): by the [[node:kl.detail.root_inversion_count|root-sign length criterion]], an inverted representing root would make its reflection decrease the ambient length, contradicting this edge.

### Step 3. Apply the plane inversion-change formula

Let \(L_P(w)\) count the ambient inversions of \(w\) whose positive roots lie in \(P\). The [[node:kl.geometry.plane_inversion_change|plane inversion-change theorem]], applied to \(xa_0,a,b\), gives
\[
2k_P(xa_0,a)
=L_P(r_a(xa_0))-L_P(xa_0)-1.
\]
Its hypotheses hold by Steps 1–2. Substitute \(r_a(xa_0)=ya_0\).

### Step 4. Replace plane inversion counts by intrinsic lengths

For the least representative \(a_0\), the [[node:kl.dihedral.plane_coset_graph|coset inversion-count theorem]] gives
\[
L_P(za_0)=\ell_D(z)\qquad(z\in D).
\]
Apply it at \(z=y\) and \(z=x\). The formula in Step 3 becomes
\[
2k_P(xa_0,a)=\ell_D(y)-\ell_D(x)-1.
\]

### Step 5. Recover the natural exponent

The plane weight is nonnegative, so its natural-number conversion has the same integer value. The intrinsic edge has \(\ell_D(y)>\ell_D(x)\), so the displayed length difference minus one is nonnegative.

The integer identity says that this difference is exactly twice the natural exponent. Therefore division by two gives the stated natural-number formula. This is the source's planeWeight_coset_edge theorem.

Thus the half-root weight used to construct the polynomial factor agrees with the relative dihedral length formula used for that plane in the notes.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot`: [DyerPaths.lean:1094](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1094).

`OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_plane`: [DyerPaths.lean:1097](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1097).

`OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_coset`: [DihedralIntervals.lean:2048](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2048).

`OAI.KLInvariance.TitsSpace.PlaneBasis.planeWeight_coset_edge`: [PlaneLocalization.lean:1096](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1096).
