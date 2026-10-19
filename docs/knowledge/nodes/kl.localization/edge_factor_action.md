---
id: kl.local.edge_factor_action
title: Multiplication by the correction factor on an edge module
kind: definition
status: formalized
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.edge_factor_lift
- kl.detail.polynomial_labels
- kl.sheaves.boundary_sheaf
- kl.sheaves.edge_coefficient_module
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.BruhatGraph.edgeFactorMap
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1449
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edgeFactorMap
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read edgeFactorMap with its BoundarySheaf, interval and coefficient context.
    Defined the actual scalar endomorphism, explained the quotient coefficient action
    from the upper-quotient kernel, and identified its scalar with the symmetric edge
    factor through the exact reduction map.
tags:
- Kazhdan-Lusztig
- correction-factors
---

# Multiplication by the correction factor on an edge module

Fix a finite-generator real Coxeter system \(W\), finite polynomial coordinates \(A\) on the extended realization, and an interval \([u,b]\) with \(u\le b\). Let \(B\) be a boundary sheaf on this labelled interval graph.

For an edge \(e:x\to y\), let \(a_e\) be its canonical positive ambient root. The polynomial label is \(\lambda(a_e)\), and the polynomial lift of its correction factor is
\[
F_e=F_{x,a_e}\in A.
\]
The **edge-factor multiplication map** is
\[
\mu_e:B^e\longrightarrow B^e,\qquad
v\longmapsto F_e v.
\]
This is edgeFactorMap, an \(A\)-linear endomorphism of the actual edge module.

## The quotient coefficient action

The upper restriction
\[
\rho^+_e:B^y\to B^e
\]
is surjective with kernel \(\lambda(a_e)B^y\). For any \(v=\rho^+_e(w)\),
\[
\lambda(a_e)v
=\rho^+_e(\lambda(a_e)w)=0.
\]
Thus the \(A\)-action factors through the edge coefficient ring
\(C_{a_e}=A/(\lambda(a_e))\).

The [[node:kl.local.edge_factor_lift_properties|polynomial-lift reduction identity]] identifies the class of \(F_e\) in this ring with \(f_{x,a_e}\) in the symmetric quotient. Consequently \(\mu_e\) is precisely the action of the reduced-root edge factor on this module.

## Degree and images

Write \(\delta_e=d_{x,a_e}\) for the plane-exponent sum. The [[node:kl.local.edge_factor_action_properties|edge-factor action theorem]] proves
\[
\mu_e(B^e_n)\subseteq B^e_{n+\delta_e}
\]
and proves that \(\mu_e\) is injective.

For a submodule \(J\subseteq B^e\), its scaled image is
\[
\mu_e(J)=\{F_ev:v\in J\}.
\]
The edge comparison uses this embedded submodule as its target. Both the original upper image and its scaled image lie in the same edge module.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The quotient factor through an explicit polynomial scalar.**

**OpenAI notes:** The edge factor is an element of the edge coefficient ring and scales the upper image inside the edge module. Its degree supplies the comparison shift, and its nonzero scalar action retains freeness of the scaled free target. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** Multiplication is defined on the actual edge module using edgeFactorLift in the original coefficient algebra. The source identifies the edge root, proves the grading shift and proves injectivity on the whole edge module from the free upper stalk, scalar quotient kernel and prime-root nondivisibility. [PlaneLocalization:1449](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1449), [PlaneLocalization:1440](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1440), [PlaneLocalization:1453](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1453), [PlaneLocalization:1462](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1462).

**Role in the proof:** The polynomial lift, its quotient class and the module endomorphism have separate definitions. The actual scalar action carries the degree shift used later in Hilbert comparison.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.edgeFactorMap`: [PlaneLocalization.lean:1449](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1449).
