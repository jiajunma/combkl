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
It preserves products and satisfies \(\overline{\overline h}=h\). Semilinearity means that scalar coefficients are transformed as well; the map is not linear over the Laurent ring with its scalars held fixed.

For a simple reflection, \(a=v-v^{-1}\) changes to \(-a\), and
\[
\overline{H_s}=H_s^{-1}=H_s-a.
\]
Applying bar a second time gives \(H_s\), since the second application also reverses the sign of \(a\).

The implementation first works over a general coefficient ring with a chosen parameter. Its linear inverse-basis transforms satisfy
\[
\operatorname{barLinear}_a\circ\operatorname{barLinear}_{-a}=I.
\]
After the Laurent coefficient involution is included, this is the involution above. One should not replace it by the assertion that the fixed-parameter linear transform squares to the identity.

A bar-invariant element is one satisfying \(\overline h=h\). Canonical KL basis elements are specified by bar invariance together with a leading term and a strict triangular degree condition. The bar normalization is the choice of parameter and basis convention used in these formulas.

## References

[Paper conventions](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L215).

## Lean formalization

`OAI.KLInvariance.Hecke.barBasis`: [Hecke.lean:303](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L303).

`OAI.KLInvariance.Hecke.barLinear`: [Hecke.lean:339](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L339).

`OAI.KLInvariance.Hecke.barLinear_inverse`: [Hecke.lean:381](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L381).
