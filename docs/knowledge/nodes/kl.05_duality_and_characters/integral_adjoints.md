---
id: kl.detail.integral_adjoints
title: Integral adjoints for a perfect pairing
kind: definition
status: formalized
primary_topic: kl.05_duality_and_characters
topics:
- kl.05_duality_and_characters
uses:
- kl.notes.perfect_pairings
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.PerfectAdjoint.adjoint
  - OAI.PerfectAdjoint.pairing
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2220
    format: lean-location
    note: OAI.PerfectAdjoint.adjoint
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2223
    format: lean-location
    note: OAI.PerfectAdjoint.pairing
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

# Integral adjoints for a perfect pairing

Let \(R\) be commutative, and let \(d:M\xrightarrow{\sim}\operatorname{Hom}_R(M,R)\) be a perfect bilinear pairing, written \(\langle m,n\rangle=d(m)(n)\). For an \(R\)-linear endomorphism \(f\), define
\[
f^*=d^{-1}\circ f^\vee\circ d,qquad
f^\vee(\lambda)=\lambda\circ f.
\]
Thus \(\langle f^*m,n\rangle=\langle m,fn\rangle\). Perfection supplies the inverse \(d^{-1}\), so the construction is over \(R\) itself. No passage to a fraction field is required.

Composition reverses: \((fg)^*=g^*f^*\). In particular, the adjoint of an idempotent is idempotent. If the pairing is symmetric, \((f^*)^*=f\). If an operator \(t\) is self-adjoint for the pairing and commutes with \(f\), the adjoint \(f^*\) also commutes with \(t\), by evaluating both sides against arbitrary vectors.

For a word-sheaf projector, further balance, grading, and support arguments prove that this module adjoint descends to stalks and edge modules. The definition of a module adjoint alone does not supply those sheaf maps.

## References

The precise Lean sources are listed below.

## Lean formalization

`OAI.PerfectAdjoint.adjoint`: [IntegralPairings.lean:2220](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2220).

`OAI.PerfectAdjoint.pairing`: [IntegralPairings.lean:2223](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2223).
