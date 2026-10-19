---
id: kl.realization.dominant_functional
title: The strictly dominant coordinate-sum functional
kind: definition
status: formalized
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.realization.extended_action
- kl.realization.simple_root_sign
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.dominant
  - OAI.KLInvariance.TitsSpace.dominant_root
  - OAI.KLInvariance.TitsSpace.dominant_action_root
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:618
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.dominant
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:622
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.dominant_root
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1260
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.dominant_action_root
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are all action, sign, and length conventions retained?
  verdict: Read the finite-rank Tits proofs, the exact two-generator tail convention,
    and both group-action directions; the chosen smaller induction instance is explicit.
tags:
- Kazhdan-Lusztig
- root-geometry
---

# The strictly dominant coordinate-sum functional

Let \(E=V_0\oplus K^*\) be the extended root space, where \(V_0=\mathbb R^I\) and \(I\) is finite. Write \(v=\sum_i v_i\alpha_i\). Define
\[
\lambda:E\to\mathbb R,\qquad
\lambda(v,\phi)=\sum_i v_i.
\]
This is a linear functional, and
\[
\lambda(\widetilde\alpha_i)=1
\]
for every embedded simple root.

A functional is strictly dominant in this convention when its value on every embedded simple root is positive. The coordinate-sum functional supplies an explicit choice.

## Evaluation on root images

The extended action restricts to the original action on the embedded root space, so
\[
\lambda(\rho(w)\widetilde\alpha_i)
=\sum_j(\rho_0(w)\alpha_i)_j.
\]
The sign theorem makes all summands nonnegative in the ascent case or nonpositive in the descent case. In either case the root image is nonzero, so at least one summand has the corresponding strict sign. Its sum therefore has that strict sign.

## The action on functionals

For the dual of the extended representation, define
\[
(w\cdot\lambda)(z)=\lambda(\rho(w^{-1})z).
\]
The inverse is part of the action formula. It gives
\[
((uv)\cdot\lambda)(z)
=\lambda(\rho(v^{-1})\rho(u^{-1})z)
=(u\cdot(v\cdot\lambda))(z).
\]

Evaluating this functional at a simple root gives the expression
\[
(w\cdot\lambda)(\widetilde\alpha_i)
=\lambda(\rho(w^{-1})\widetilde\alpha_i).
\]
The dominant-sign theorem identifies its positivity with a left ascent of \(w\).

## References

The local action and sign calculations are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.dominant`: [Tits.lean:618](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L618).

`OAI.KLInvariance.TitsSpace.dominant_root`: [Tits.lean:622](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L622).

`OAI.KLInvariance.TitsSpace.dominant_action_root`: [Tits.lean:1260](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1260).
