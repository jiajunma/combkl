---
id: kl.realization.positive_root_action
title: The action on positive representatives of root lines
kind: definition
status: formalized
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.detail.root_reflection_correspondence
- kl.detail.positive_roots
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.TitsSpace.positiveAction
  - OAI.KLInvariance.TitsSpace.positiveAction_represents
  - OAI.KLInvariance.TitsSpace.positiveAction_eq_of_nonneg
  - OAI.KLInvariance.TitsSpace.positiveAction_eq_of_nonpos
  - OAI.KLInvariance.TitsSpace.rootReflection_positiveAction
  - OAI.KLInvariance.TitsSpace.positiveAction_mul
  - OAI.KLInvariance.TitsSpace.positiveActionEquiv
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:167
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.positiveAction
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:171
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.positiveAction_represents
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:176
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.positiveAction_eq_of_nonneg
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:182
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.positiveAction_eq_of_nonpos
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:189
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.rootReflection_positiveAction
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:199
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.positiveAction_mul
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:208
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.positiveActionEquiv
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# The action on positive representatives of root lines

For \(w\in W\) and \(a\in\Phi^+\), let \(w\star a\) be the positive root representing the conjugate reflection \(w r_a w^{-1}\).

The root \(w(a)\) represents that conjugate reflection. Uniqueness of the positive representative therefore gives
\[
w\star a=
\begin{cases}
w(a),&w(a)\text{ is positive},\\
-w(a),&w(a)\text{ is negative}.
\end{cases}
\]
This action retains the positive representative of each transformed root line.

## Composition and inverses

Conjugation gives
\[
(wz)r_a(wz)^{-1}
=w(zr_az^{-1})w^{-1}.
\]
Both \((wz)\star a\) and \(w\star(z\star a)\) are the unique positive root representing this reflection. Hence
\[
(wz)\star a=w\star(z\star a).
\]
Likewise \(1\star a=a\). Thus \(a\mapsto w\star a\) is a permutation of the positive roots, with inverse \(a\mapsto w^{-1}\star a\).

The associated reflections satisfy
\[
r_{w\star a}=w r_a w^{-1}.
\]
For \(w=r_b\), this is the partner operation used to group inversion changes.

If \(w\in D_P\) and \(a\in P\), then \(w(a)\in P\), and so does its negative. Consequently the positive-root action restricts to a permutation of \(\Phi^+\cap P\).

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.TitsSpace.positiveAction`: [ReflectionSchedules.lean:167](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L167).

`OAI.KLInvariance.TitsSpace.positiveAction_represents`: [ReflectionSchedules.lean:171](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L171).

`OAI.KLInvariance.TitsSpace.positiveAction_eq_of_nonneg`: [ReflectionSchedules.lean:176](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L176).

`OAI.KLInvariance.TitsSpace.positiveAction_eq_of_nonpos`: [ReflectionSchedules.lean:182](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L182).

`OAI.KLInvariance.TitsSpace.rootReflection_positiveAction`: [ReflectionSchedules.lean:189](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L189).

`OAI.KLInvariance.TitsSpace.positiveAction_mul`: [ReflectionSchedules.lean:199](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L199).

`OAI.KLInvariance.TitsSpace.positiveActionEquiv`: [ReflectionSchedules.lean:208](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L208).
