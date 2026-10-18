---
id: kl.realization.geometric_action
title: The geometric action of a Coxeter system
kind: definition
status: formalized
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.realization.tits_form
- kl.realization.linear_reflection
- kl.coxeter.word_data
- kl.realization.finite_reflection_relations
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.Realization.geometricAction
  - OAI.KLInvariance.Realization.geometricSimple_liftable
  - OAI.KLInvariance.Realization.geometricAction_simple
  - OAI.KLInvariance.TitsSpace.action
  - OAI.KLInvariance.TitsSpace.action_simple
  - OAI.KLInvariance.TitsSpace.action_preserves
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:332
    format: lean-location
    note: OAI.KLInvariance.Realization.geometricAction
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:314
    format: lean-location
    note: OAI.KLInvariance.Realization.geometricSimple_liftable
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:335
    format: lean-location
    note: OAI.KLInvariance.Realization.geometricAction_simple
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:418
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.action
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:422
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.action_simple
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:428
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.action_preserves
  - artifact: openai-kl-paper
    locator: Real realizations; bg:realization
    format: section
    note: Construction and normalization of the realization.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition retain the local source hypotheses and construction?
  verdict: Source statements and construction read directly; dimensions, normalization,
    and orthogonality direction stated explicitly.
tags:
- Kazhdan-Lusztig
- realization
---

# The geometric action of a Coxeter system

Let \((W,S)\) have finite simple-generator set \(I\), and let \(V_0\), \(B\), and \(\alpha_i\) be its Tits space, form, and simple roots. Put
\[
r_i(v)=v-B(\alpha_i,v)\alpha_i.
\]
The geometric action is the homomorphism
\[
\rho_0:W\longrightarrow\operatorname{GL}(V_0)
\]
sending \(s_i\) to \(r_i\). For a word \(w=s_{i_1}\cdots s_{i_m}\), it is
\[
\rho_0(w)=r_{i_1}\circ\cdots\circ r_{i_m}.
\]
The rightmost operator acts first.

## The role of the defining relations

To define a homomorphism from a presented group, the proposed images must satisfy its defining relations. Each \(r_i^2=1\), by the linear-reflection calculation. For finite \(m_{ij}\), the rank-two reflection-relation theorem gives
\[
(r_ir_j)^{m_{ij}}=1.
\]
The proof is [[node:kl.realization.finite_reflection_relations]], which calculates powers using the normalized Chebyshev recurrence and treats both parities of the exponent. Consequently equivalent words give the same linear map, and the universal property of the Coxeter presentation supplies \(\rho_0\).

The same construction works on any real vector space with a bilinear form and root vectors satisfying the specified pairings. The extended action applies it to the extended root space.

## Action on basis vectors and on the form

Substituting \(v=\alpha_j\) yields
\[
r_i(\alpha_j)=\alpha_j-g_{ij}\alpha_i.
\]
For \(m_{st}=3\), this gives
\[
r_s(\alpha_s)=-\alpha_s,\qquad r_s(\alpha_t)=\alpha_t+\alpha_s.
\]
Linearity then determines the action on the root plane.

The reflection preservation identity gives \(B(r_i v,r_i z)=B(v,z)\). Successive applications along a word give
\[
B(\rho_0(w)v,\rho_0(w)z)=B(v,z).
\]

The real roots are the vectors \(\rho_0(w)\alpha_i\). Thus this action supplies the root system whose signs describe Coxeter inversions.

## References

[Realizations in the OpenAI notes](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L34).

## Lean formalization

`OAI.KLInvariance.Realization.geometricAction`: [Tits.lean:332](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L332).

`OAI.KLInvariance.Realization.geometricSimple_liftable`: [Tits.lean:314](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L314).

`OAI.KLInvariance.Realization.geometricAction_simple`: [Tits.lean:335](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L335).

`OAI.KLInvariance.TitsSpace.action`: [Tits.lean:418](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L418).

`OAI.KLInvariance.TitsSpace.action_simple`: [Tits.lean:422](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L422).

`OAI.KLInvariance.TitsSpace.action_preserves`: [Tits.lean:428](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L428).
