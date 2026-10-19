---
id: kl.local.orbit_splines
title: Orbit splines in the extended realization
kind: definition
status: formalized
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.realization.extended_action
- kl.notes.extended_realization
- kl.algebra.coefficient_algebra
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.TitsSpace.linearPolynomial
  - OAI.KLInvariance.TitsSpace.orbitSpline
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:137
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.linearPolynomial
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:141
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.orbitSpline
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read linearPolynomial and orbitSpline with their exact action order w*y^-1.
    Distinguished the extended-space coefficient map from the original-root label,
    defined the spline congruence terminology and explained the normal-value parameters.
tags:
- Kazhdan-Lusztig
- interpolation
---

# Orbit splines in the extended realization

Fix a finite-generator Coxeter system \(W\). Let \(V\) be its extended real realization, \(\rho:W\to\operatorname{GL}(V)\) the extended action, and \(A\) the polynomial coefficient algebra from a chosen real basis of \(V\).

Write
\[
\Lambda:V\to A
\]
for the real-linear map sending a vector to its degree-one coordinate polynomial. This is linearPolynomial. For a root \(a\) in the original root space, its polynomial label is
\(\lambda(a)=\Lambda(i_0a)\), where \(i_0\) is the embedding into \(V\).

For \(y\in W\) and \(v_0\in V\), the **orbit spline** is the function
\[
F_{y,v_0}:W\to A,\qquad
F_{y,v_0}(w)=\Lambda\bigl(\rho(wy^{-1})v_0-v_0\bigr).
\]
This is orbitSpline. The parameter \(y\) is the vertex at which the displacement is zero. The parameter \(v_0\) controls its values at other vertices.

A polynomial spline on the reflection graph means a polynomial-valued function whose values at reflection-related vertices agree modulo the corresponding root label. The [[node:kl.local.orbit_spline_congruence|orbit-spline congruence theorem]] proves this condition for \(F_{y,v_0}\).

## The value at the reference vertex

Since \(yy^{-1}=1\) and the identity acts trivially,
\[
F_{y,v_0}(y)=\Lambda(v_0-v_0)=0.
\]

Every value is a linear polynomial, because its argument is a vector of \(V\) and \(\Lambda\) is linear.

## Selecting the normal values

If \(xy^{-1}=t\) and a root \(a\) represents \(t\), the reflection formula gives
\[
F_{y,v_0}(x)
=-\widetilde B(i_0a,v_0)\lambda(a),
\]
where \(\widetilde B\) is the extended bilinear form.

Choosing the normal value \(\widetilde B(i_0a,v_0)=-1\) gives \(F_{y,v_0}(x)=\lambda(a)\). Prescribing a second normal value to be zero gives an additional zero of the same function. The [[node:kl.local.orbit_spline_factors|orbit-spline factor theorem]] constructs both choices from the extended realization.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same model properties, different justification.**

**OpenAI notes:** The induced-model lemma justifies applying the character theorem to the restricted reflection-faithful realization and uses the dihedral character calculation to identify the rank-one model. [loc:models](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L125).

**Lean (primary):** The direct construction first proves parity matching in arbitrary lower Bruhat intervals by a simple-reflection involution. In the dihedral application, orbit-spline factors supply the prescribed values and zeros; their product gives flow-down sections. A finite induction on prescribed upper sets proves flabbiness, while generation and quotient maps follow from the structure-sheaf construction. [DihedralIntervals:616](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L616), [DihedralIntervals:622](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L622), [DihedralIntervals:626](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L626), [SheafMorphisms:252](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L252), [SheafMorphisms:288](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L288), [DihedralIntervals:176](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L176), [DihedralIntervals:251](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L251), [DihedralIntervals:372](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L372).

**Role in the proof:** The Blueprint follows the parity, normal-form prescription, spline product and flow-down correction arguments. Injectivity of the reflection-preserving group map provides distinct factor data and pairwise relatively prime incident labels. These model properties feed the later local-ring decomposition.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.linearPolynomial`: [DihedralIntervals.lean:137](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L137).

`OAI.KLInvariance.TitsSpace.orbitSpline`: [DihedralIntervals.lean:141](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L141).
