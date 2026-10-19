---
id: kl.detail.edge_factor
title: The reduced-root product attached to a positive root
kind: definition
status: formalized
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.factor_roots
- kl.geometry.plane_weights
- kl.algebra.edge_coefficient_ring
- kl.algebra.root_quotient_coordinates
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.TitsSpace.edgeFactor
  - OAI.KLInvariance.TitsSpace.edgeFactorDegree
  - OAI.KLInvariance.TitsSpace.edgePolynomial
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:944
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.edgeFactor
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:947
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.edgeFactorDegree
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:950
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.edgePolynomial
  - artifact: openai-kl-paper
    locator: 5. Comparison of edge images; edge:bound
    format: section
    note: Correction-factor construction and its local image comparison.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Replaced the upward-edge-only setup by the exact all-x definition. Read
    edgeFactor, edgeFactorDegree and edgePolynomial, explained the finite support,
    toNat exponents, quotient basis and empty product, and separated the conditional
    length formula from unconditional construction.
tags:
- Kazhdan-Lusztig
- correction-factors
---

# The reduced-root product attached to a positive root

Fix a finite-generator real Coxeter system \(W\), \(x\in W\), and a positive root \(a\). Let \(V\) be its extended realization, \(i_0\) the original-root embedding, and \(\iota\) the symmetric-algebra inclusion. In the edge coefficient ring
\[
E_a=\operatorname{Sym}_{\mathbb R}(V)/(\iota(i_0a)),
\]
use the supported plane set \(\mathcal P(x,a)\), weights \(k_P\ge0\), and reduced plane roots \(r_P\). The **edge factor** is
\[
f_{x,a}=\prod_{P\in\mathcal P(x,a)}r_P^{\,k_P}.
\]
This is edgeFactor. The source stores \(k_P\) as an integer and uses its natural-number conversion in the exponent. Nonnegativity makes that conversion preserve the value.

The associated natural number is
\[
d_{x,a}=\sum_{P\in\mathcal P(x,a)}k_P,
\]
called edgeFactorDegree. Both definitions apply to every \(x\) and positive \(a\).

## Polynomial coordinates on the quotient

Choose a basis of \(V/\mathbb R i_0a\). Composing the symmetric-quotient isomorphism with the symmetric-algebra coordinate map gives
\[
\Psi_a:E_a\xrightarrow{\sim}\mathbb R[Y_1,\ldots,Y_m],
\qquad m=\dim_{\mathbb R}(V/\mathbb R i_0a).
\]
The source's edgePolynomial uses the finite basis selected for that quotient space.

Each \(r_P\) is sent to the degree-one polynomial of the quotient vector \([i_0b_P]\). The [[node:kl.local.edge_factor_properties|edge-factor properties theorem]] proves
\[
f_{x,a}\ne0,\qquad
\Psi_a(f_{x,a})\text{ is homogeneous of degree }d_{x,a}.
\]

## Empty support and the degree formula for an ascent

If every plane weight is zero, the supported set is empty:
\[
f_{x,a}=1,\qquad d_{x,a}=0.
\]
The product over an empty set is the multiplicative identity.

When \(x^{-1}a\) is positive, the [[node:kl.paths.plane_degree|edge-factor degree theorem]] gives
\[
2d_{x,a}=\ell(r_ax)-\ell(x)-1.
\]
Thus the length formula is a property of the product under the ascent hypothesis. Its construction and nonvanishing already make sense for every \(x\).

The polynomial lift of the edge factor supplies a scalar in the original coefficient algebra whose reduction is exactly \(f_{x,a}\). That scalar defines the edge-factor multiplication map on the actual edge module.

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

`OAI.KLInvariance.TitsSpace.edgeFactor`: [ReflectionSchedules.lean:944](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L944).

`OAI.KLInvariance.TitsSpace.edgeFactorDegree`: [ReflectionSchedules.lean:947](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L947).

`OAI.KLInvariance.TitsSpace.edgePolynomial`: [ReflectionSchedules.lean:950](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L950).
