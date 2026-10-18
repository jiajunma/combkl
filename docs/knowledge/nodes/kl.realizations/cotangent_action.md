---
id: kl.realization.cotangent_action
title: The coordinate-dual action in arbitrary generator rank
kind: definition
status: formalized
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.coxeter.word_data
- kl.realization.finite_reflection_relations
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.Cotangent.root
  - OAI.KLInvariance.Cotangent.simple
  - OAI.KLInvariance.Cotangent.action
  - OAI.KLInvariance.Cotangent.action_simple
  - OAI.KLInvariance.Cotangent.pairing
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1314
    format: lean-location
    note: OAI.KLInvariance.Cotangent.root
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1319
    format: lean-location
    note: OAI.KLInvariance.Cotangent.simple
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1339
    format: lean-location
    note: OAI.KLInvariance.Cotangent.action
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1342
    format: lean-location
    note: OAI.KLInvariance.Cotangent.action_simple
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1370
    format: lean-location
    note: OAI.KLInvariance.Cotangent.pairing
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the calculation preserve the local statement and proof route?
  verdict: Checked the general linear-functional hypotheses, even/odd Chebyshev vanishings,
    rank-one normal form, and arbitrary-rank coordinate action.
tags:
- Kazhdan-Lusztig
- realization
---

# The coordinate-dual action in arbitrary generator rank

Let \(I\) be the simple-generator set of a Coxeter system; it can be infinite. Work on the space \(\mathbb R^I\) of all real-valued functions on \(I\). For each \(i\), define the row vector
\[
\gamma_i(j)=-2\cos(\pi/m_{ij}),
\]
with value \(-2\) at an infinite exponent, and let \(\epsilon_i(\lambda)=\lambda_i\) be coordinate evaluation. Then \(\epsilon_i(\gamma_i)=2\).

The coordinate-dual simple operator is
\[
s_i^\vee(\lambda)=\lambda-\lambda_i\gamma_i,
\]
or, coordinate by coordinate,
\[
(s_i^\vee\lambda)_j=\lambda_j-\lambda_i\gamma_i(j).
\]
This formula uses one coordinate evaluation, so it is defined on all of \(\mathbb R^I\) for any \(I\).

## The group action

Each simple operator is a reflection associated with the pair \((\gamma_i,\epsilon_i)\). For a finite exponent \(m_{ij}\), the cross-evaluations are
\[
\epsilon_i(\gamma_j)=\epsilon_j(\gamma_i)
=-2\cos(\pi/m_{ij}),
\]
by symmetry of the Coxeter matrix. The finite linear-reflection relation therefore applies. The presentation gives a homomorphism
\[
\rho^\vee:W\to\operatorname{GL}(\mathbb R^I)
\]
with these simple operators.

## Duality in finite rank

When \(I\) is finite, regard \(\lambda\in\mathbb R^I\) as the functional
\[
v\longmapsto\lambda\cdot v=\sum_i\lambda_iv_i
\]
on the ordinary root space. For a simple generator, put \(a=\lambda_i\) and \(b=B(\alpha_i,v)\). Since
\[
\gamma_i\cdot v=b,\qquad
\lambda\cdot\alpha_i=a,\qquad
\gamma_i\cdot\alpha_i=2,
\]
expansion gives
\[
(\lambda-a\gamma_i)\cdot(v-b\alpha_i)
=\lambda\cdot v-ab-ab+2ab
=\lambda\cdot v.
\]
Applying this along a word yields
\[
\rho^\vee(w)\lambda\cdot\rho_0(w)v=\lambda\cdot v.
\]
Replacing \(v\) by \(\rho_0(w^{-1})v\) identifies the action as the dual action:
\[
(\rho^\vee(w)\lambda)(v)=\lambda(\rho_0(w^{-1})v).
\]

Coordinate restriction to a subset of generators respects these simple formulas for the generators belonging to that subset. The standard-parabolic construction uses that restriction, together with finite-rank faithfulness, to prove injectivity of its inclusion.

## References

The local source statements and calculations are listed below.

## Lean formalization

`OAI.KLInvariance.Cotangent.root`: [Tits.lean:1314](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1314).

`OAI.KLInvariance.Cotangent.simple`: [Tits.lean:1319](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1319).

`OAI.KLInvariance.Cotangent.action`: [Tits.lean:1339](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1339).

`OAI.KLInvariance.Cotangent.action_simple`: [Tits.lean:1342](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1342).

`OAI.KLInvariance.Cotangent.pairing`: [Tits.lean:1370](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1370).
