---
id: kl.detail.primitive_projectors
title: Primitive sheaf projectors
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.split_summands
lean:
  repository: openai-kl
  modules:
  - BalancedPairings
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.PrimitiveProjector
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1648
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.PrimitiveProjector
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

# Primitive sheaf projectors

A sheaf endomorphism \(e\) is a primitive projector if \(e^2=e\) and every idempotent \(f\) satisfying
\[
f^2=f,\qquad fe=f,\qquad ef=f
\]
is either zero or \(e\). The last two equations say that \(f\) acts within the summand selected by \(e\).

For \(e=1_B\), the condition says that every idempotent endomorphism of \(B\) is zero or the identity. Thus a decomposition of \(B\) into two nonzero split sheaf summands is impossible: the projection onto either would be a forbidden idempotent.

The formal predicate does not separately impose \(e\ne0\); the zero projector satisfies it. Nonzero stalk hypotheses are therefore stated explicitly when primitivity is used to conclude that a split inclusion is an isomorphism. For the boundary sheaf, the normalized rank-one top stalk supplies this nonzero condition.

## References

The precise Lean sources are listed below.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.PrimitiveProjector`: [BalancedPairings.lean:1648](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1648).
