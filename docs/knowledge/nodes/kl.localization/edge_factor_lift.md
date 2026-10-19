---
id: kl.local.edge_factor_lift
title: The polynomial lift before the edge quotient
kind: definition
status: formalized
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.detail.edge_factor
- kl.local.factor_roots
- kl.algebra.edge_coefficient_ring
- kl.algebra.coefficient_algebra
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.BruhatGraph.polynomialRoot
  - OAI.KLInvariance.BruhatGraph.edgeFactorLift
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1356
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.polynomialRoot
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1389
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edgeFactorLift
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read polynomialRoot and edgeFactorLift in the BruhatGraph namespace. Defined
    the unreduced polynomial product and both quotient presentations; fixed the direction
    of the coordinate map and the induced quotient isomorphism before stating its
    relation to the actual edge-module scalar.
tags:
- Kazhdan-Lusztig
- correction-factors
---

# The polynomial lift before the edge quotient

Fix a finite-generator real Coxeter system \(W\) and a finite basis of its extended realization \(V\). Let \(i_0\) be the original-root embedding and \(\iota\) the symmetric-algebra inclusion. Write
\[
S=\operatorname{Sym}_{\mathbb R}(V),\qquad
\Phi:S\xrightarrow{\sim}A
\]
for the polynomial coordinate isomorphism. For a positive root \(b\), define
\[
\lambda(b)=\Phi(\iota(i_0b)).
\]
This is polynomialRoot.

For \(x\in W\) and a positive root \(a\), use the same finite supported plane set, representative roots \(b_P\), and weights \(k_P\) as in the edge factor. Its **polynomial lift** is
\[
F_{x,a}=\prod_{P\in\mathcal P(x,a)}\lambda(b_P)^{k_P}\in A.
\]
The source calls this edgeFactorLift.

## The two quotient presentations

There are two presentations of the edge coefficient ring:
\[
E_a=S/(\iota(i_0a)),\qquad C_a=A/(\lambda(a)).
\]
Let \(q_a:S\to E_a\) and \(\pi_a:A\to C_a\) be the quotient maps. The inverse coordinate isomorphism induces
\[
\chi_a:C_a\xrightarrow{\sim}E_a,\qquad
\chi_a([h])=q_a(\Phi^{-1}(h)).
\]
Its defining relation is preserved because
\(\Phi^{-1}(\lambda(a))=\iota(i_0a)\).

The lift satisfies
\[
q_a(\Phi^{-1}(F_{x,a}))=f_{x,a},
\]
or equivalently
\[
\chi_a(\pi_a(F_{x,a}))=f_{x,a}.
\]
The [[node:kl.local.edge_factor_lift_properties|polynomial-lift properties theorem]] proves this identity factor by factor.

## The scalar used on an edge module

An actual edge module is an \(A\)-module annihilated by \(\lambda(a)\), hence carries the induced \(C_a\)-action. Multiplication by \(F_{x,a}\) through the \(A\)-action is therefore multiplication by its class \(\pi_a(F_{x,a})\).

The quotient identity identifies that class with the reduced-root product. This is the relation between the polynomial scalar used by Lean's edgeFactorMap and the element of the edge coefficient ring used in the notes.

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

`OAI.KLInvariance.BruhatGraph.polynomialRoot`: [PlaneLocalization.lean:1356](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1356).

`OAI.KLInvariance.BruhatGraph.edgeFactorLift`: [PlaneLocalization.lean:1389](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1389).
