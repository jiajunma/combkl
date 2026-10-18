---
id: kl.detail.positive_roots
title: Real roots, positive roots, and represented reflections
kind: definition
status: formalized
primary_topic: kl.03_realizations_and_grading
topics:
- kl.03_realizations_and_grading
uses:
- kl.notes.extended_realization
- kl.realization.geometric_action
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.IsRoot
  - OAI.KLInvariance.TitsSpace.Represents
  - OAI.KLInvariance.TitsSpace.PositiveRoot
  - OAI.KLInvariance.TitsSpace.positiveRootEquiv
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
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1821
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.positiveRootEquiv
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

Let \((W,S)\) have finitely many simple generators. In its real Tits root space \(V_0\), write \(\alpha_i\) for the simple roots, normalized by \((\alpha_i,\alpha_i)=2\). The set of real roots is
\[
\Phi=\{w\alpha_i:w\in W,\ i\in S\}.
\]
A root \(a\) represents a reflection \(t\) when there are \(w,i\) such that both \(a=w\alpha_i\) and \(t=ws_iw^{-1}\). This specifies a genuine orbit root; it does not permit an arbitrary scalar multiple of a root.

A positive root is a real root all of whose coordinates in the simple-root basis are nonnegative:
\[
\Phi^+=\{a\in\Phi:a_i\ge0\text{ for every }i\}.
\]
Every real root is nonzero and has squared norm two. Its coordinates have one sign, so either it or its negative is positive. The root–reflection correspondence sends a reflection to its unique positive representing root and sends a positive root to its reflection. The existence and uniqueness assertions are proved in the separate correspondence theorem.

The root system may be infinite. Finiteness of the simple-generator set is the finite-dimensional realization assumption, not a finiteness assertion about \(W\) or \(\Phi\).

## References

The precise Lean sources are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.IsRoot`: [Tits.lean:1657](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1657).

`OAI.KLInvariance.TitsSpace.Represents`: [Tits.lean:1660](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1660).

`OAI.KLInvariance.TitsSpace.PositiveRoot`: [Tits.lean:1799](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1799).

`OAI.KLInvariance.TitsSpace.positiveRootEquiv`: [Tits.lean:1821](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1821).
