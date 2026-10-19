---
id: kl.local.factor_roots
title: Chosen roots for the supported plane factors
kind: definition
status: formalized
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.geometry.plane_weights
- kl.realization.root_planes
- kl.algebra.edge_coefficient_ring
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.TitsSpace.planeWeight_support_root
  - OAI.KLInvariance.TitsSpace.planeRoot
  - OAI.KLInvariance.TitsSpace.planeRoot_ne
  - OAI.KLInvariance.TitsSpace.planeRoot_plane
  - OAI.KLInvariance.TitsSpace.reducedPlaneRoot
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:895
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.planeWeight_support_root
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:908
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.planeRoot
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:912
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.planeRoot_ne
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:916
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.planeRoot_plane
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:933
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.reducedPlaneRoot
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read planeWeight_support_root and the exact existential properties retained
    by planeRoot, then reducedPlaneRoot. Distinguished the chosen positive root from
    a claim of a canonical representative or a retained half-root property, and kept
    the original-root embedding and symmetric quotient map explicit.
tags:
- Kazhdan-Lusztig
- correction-factors
---

# Chosen roots for the supported plane factors

Fix a finite-generator real Coxeter system \(W\), its original root space \(V_0\), the extended realization \(V\), and the embedding \(i_0:V_0\to V\). Fix \(x\in W\) and a positive root \(a\).

Let \(k_P=k_P(x,a)\) be the geometric plane weights and
\[
\mathcal P(x,a)=\{P:k_P\ne0\}
\]
their finite support. The weights count half-roots grouped by the plane they span with \(a\), so \(k_P\ge0\).

For each \(P\in\mathcal P(x,a)\), choose a positive root \(b_P\) satisfying
\[
b_P\ne a,\qquad \operatorname{span}_{\mathbb R}\{a,b_P\}=P.
\]
The source calls this chosen **factor representative root** planeRoot.

## Existence of the representative

A nonzero coefficient in the grouped plane-weight function comes from at least one root in the support of the half-root indicator. Such a root is different from \(a\), and the grouping map sends it to its span with \(a\).

This gives a witness \(b\ne a\) with \(\operatorname{span}\{a,b\}=P\). The definition planeRoot chooses a witness to precisely these two properties. The theorems planeRoot_ne and planeRoot_plane retain them for every supported plane.

## Reduction to the edge coefficient ring

Write
\[
S=\operatorname{Sym}_{\mathbb R}(V),\qquad
\iota:V\to S,\qquad
E_a=S/(\iota(i_0a)),
\]
and let \(q_a:S\to E_a\) be the quotient map. The **reduced plane root** attached to \(P\) is
\[
r_P=q_a(\iota(i_0b_P)).
\]
This is reducedPlaneRoot.

Since distinct positive roots are independent, \(i_0b_P\) is not in the line \(\mathbb R i_0a\). The linear-quotient identification
\[
E_a\simeq\operatorname{Sym}_{\mathbb R}(V/\mathbb R i_0a)
\]
therefore sends \(r_P\) to the linear generator of a nonzero quotient vector. The [[node:kl.local.edge_factor_properties|edge-factor properties theorem]] proves that each \(r_P\) is nonzero and has degree one in quotient polynomial coordinates.

These finite representative data are the factors used in the reduced-root product and in its polynomial lift.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The same root product with explicit weight and coordinate constructions.**

**OpenAI notes:** The notes assign each plane its half-excess relative dihedral length, choose an independent root whenever that weight is positive, and multiply its reduced linear form to that power in the edge quotient. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The weights are first constructed by grouping half-root indicators. planeWeight_coset_edge identifies them with the relative dihedral length formula. planeRoot chooses a positive root with the required plane, edgeFactor is a product in the symmetric quotient, and edgeFactorLift is its explicit product before the polynomial quotient. The definitions and nonvanishing hold for every x; noninversion is used for the length-degree formula. [ReflectionSchedules:908](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L908), [ReflectionSchedules:944](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L944), [ReflectionSchedules:985](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L985), [ReflectionSchedules:993](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L993), [PlaneLocalization:1389](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1389), [PlaneLocalization:1413](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1413), [PlaneLocalization:1096](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1096).

**Role in the proof:** The Blueprint keeps the chosen representatives, all scalar maps and the natural/integer exponent conversion explicit. The quotient of the polynomial lift is exactly the constructed edge factor.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.planeWeight_support_root`: [ReflectionSchedules.lean:895](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L895).

`OAI.KLInvariance.TitsSpace.planeRoot`: [ReflectionSchedules.lean:908](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L908).

`OAI.KLInvariance.TitsSpace.planeRoot_ne`: [ReflectionSchedules.lean:912](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L912).

`OAI.KLInvariance.TitsSpace.planeRoot_plane`: [ReflectionSchedules.lean:916](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L916).

`OAI.KLInvariance.TitsSpace.reducedPlaneRoot`: [ReflectionSchedules.lean:933](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L933).
