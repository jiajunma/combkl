---
id: kl.detail.positive_roots
title: Real roots, positive roots, and represented reflections
kind: definition
status: formalized
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.realization.geometric_action
- kl.realization.simple_root_sign
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.IsRoot
  - OAI.KLInvariance.TitsSpace.Represents
  - OAI.KLInvariance.TitsSpace.PositiveRoot
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1657
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.IsRoot
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1660
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.Represents
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1799
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PositiveRoot
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

# Real roots, positive roots, and represented reflections

Let \((W,S)\) have finitely many simple generators, with geometric action \(\rho_0\) on \(V_0=\mathbb R^I\). The real roots are
\[
\Phi=\{\rho_0(w)\alpha_i:w\in W,\ i\in I\}.
\]
A vector \(a\) represents a reflection \(t\) when one pair \(w,i\) gives both
\[
a=\rho_0(w)\alpha_i,\qquad t=ws_iw^{-1}.
\]
Thus a representing pair records the vector and the conjugated simple reflection together.

## Norm, negation, and group action

The action preserves the Tits form, so every real root has squared norm
\[
B(\rho_0(w)\alpha_i,\rho_0(w)\alpha_i)=B(\alpha_i,\alpha_i)=2.
\]
In particular it is nonzero.

Negating a root preserves the root set, since
\[
-\rho_0(w)\alpha_i=\rho_0(ws_i)\alpha_i.
\]
This changes the representing vector's sign and retains its reflection. Applying \(u\in W\) sends the represented pair \((t,a)\) to
\[
(utu^{-1},\rho_0(u)a).
\]

## Positive roots

A positive real root has nonnegative coordinates in the simple-root basis:
\[
\Phi^+=\{a\in\Phi:a_j\ge0\text{ for every }j\}.
\]
The simple-root sign theorem applies to each expression \(a=\rho_0(w)\alpha_i\). It proves that every real root is positive or the negative of a positive root. These alternatives are exclusive because a nonzero vector cannot have all coordinates both nonnegative and nonpositive.

For the exponent-three pair, \(s_i\alpha_j=\alpha_j+\alpha_i\), which is a positive root. Also \(s_i\alpha_i=-\alpha_i\), a negative root.

The root–reflection correspondence [[node:kl.detail.root_reflection_correspondence]] proves that each reflection has a unique positive representative. It also proves that the reflection attached to a root is independent of its chosen expression as a translate.

## References

The local definitions are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.IsRoot`: [Tits.lean:1657](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1657).

`OAI.KLInvariance.TitsSpace.Represents`: [Tits.lean:1660](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1660).

`OAI.KLInvariance.TitsSpace.PositiveRoot`: [Tits.lean:1799](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1799).
