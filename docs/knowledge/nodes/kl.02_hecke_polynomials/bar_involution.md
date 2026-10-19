---
id: kl.definitions.bar_involution
title: The Hecke bar involution
kind: definition
status: formalized
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.definitions.hecke_operators
- kl.definitions.hecke_quadratic_relation
lean:
  repository: openai-kl
  modules:
  - Hecke
  declarations:
  - OAI.KLInvariance.Hecke.barBasis
  - OAI.KLInvariance.Hecke.barLinear
  - OAI.KLInvariance.Hecke.barLinear_inverse
  - OAI.KLInvariance.HeckeQ.barBasis
  - OAI.KLInvariance.HeckeQ.barLinear
  - OAI.KLInvariance.HeckeQ.barLinear_left
  - OAI.KLInvariance.HeckeQ.barLinear_inverse
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:303
    format: lean-location
    note: OAI.KLInvariance.Hecke.barBasis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:339
    format: lean-location
    note: OAI.KLInvariance.Hecke.barLinear
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:381
    format: lean-location
    note: OAI.KLInvariance.Hecke.barLinear_inverse
  - artifact: openai-kl-paper
    locator: 1. Introduction and conventions; sec:introduction
    format: section
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:790
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.barBasis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:833
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.barLinear
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:841
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.barLinear_left
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:876
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.barLinear_inverse
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does this definition retain the implemented conventions?
  verdict: Normalized and unnormalized parameters, operators, and semilinearity are
    distinguished explicitly.
tags:
- Kazhdan-Lusztig
- definitions
- Hecke
---

# The Hecke bar involution

Over the Laurent coefficient ring \(\mathbb Z[v,v^{-1}]\), the Hecke bar involution is the semilinear map characterized by
\[
\overline v=v^{-1},\qquad
\overline{H_w}=H_{w^{-1}}^{-1},\qquad
\overline{fh}=\overline f\,\overline h.
\]
It preserves products and satisfies \(\overline{\overline h}=h\). Semilinearity transforms scalar coefficients by the involution on the Laurent ring.

For a simple reflection, \(a=v-v^{-1}\) changes to \(-a\), and
\[
\overline{H_s}=H_s^{-1}=H_s-a.
\]
Applying bar a second time gives \(H_s\), since the second application also reverses the sign of \(a\).

The implementation first works over a general coefficient ring with a chosen parameter. Its linear inverse-basis transforms satisfy
\[
\operatorname{barLinear}_a\circ\operatorname{barLinear}_{-a}=I.
\]
The Laurent coefficient involution changes the parameter from a to its negative between the two linear transforms. Their displayed composition therefore gives the square of the semilinear involution.

A bar-invariant element is one satisfying \(\overline h=h\). Canonical KL basis elements are specified by bar invariance together with a leading term and a strict triangular degree condition. The bar normalization is the choice of parameter and basis convention used in these formulas.

## The linear transform in the unnormalized q convention

For a unit \(q\) in a commutative coefficient ring, let \(T_w\) be the standard basis of the unnormalized Hecke module. The linear bar transform \(B_q\) is defined on a basis vector by applying the inverse standard word operator for \(w^{-1}\) to \(T_1\):
\[
B_q(T_w)=T_{w^{-1}}^{-1}.
\]
This formula denotes the corresponding inverse-operator vector in the module.

For a simple reflection,
\[
B_q(T_s)=T_s^{-1}
=q^{-1}\bigl(T_s-(q-1)T_1\bigr).
\]
The transform is coefficient-linear. Its operator identities are
\[
B_qL_s(q^{-1})=L_s(q)^{-1}B_q,\qquad
B_qB_{q^{-1}}=1.
\]
The word-character calculation uses this form of the transform.

Over Laurent coefficients, composing the linear transform with coefficient inversion \(q\mapsto q^{-1}\) gives the semilinear bar operation in this convention. The relation \(q=v^2\) connects it with the normalized \(v\)-convention above.

## References

[Paper conventions](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L215).

## Lean formalization

`OAI.KLInvariance.Hecke.barBasis`: [Hecke.lean:303](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L303).

`OAI.KLInvariance.Hecke.barLinear`: [Hecke.lean:339](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L339).

`OAI.KLInvariance.Hecke.barLinear_inverse`: [Hecke.lean:381](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L381).

`OAI.KLInvariance.HeckeQ.barBasis`: [Hecke.lean:790](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L790).

`OAI.KLInvariance.HeckeQ.barLinear`: [Hecke.lean:833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L833).

`OAI.KLInvariance.HeckeQ.barLinear_left`: [Hecke.lean:841](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L841).

`OAI.KLInvariance.HeckeQ.barLinear_inverse`: [Hecke.lean:876](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L876).
