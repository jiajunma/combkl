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

A graded sheaf endomorphism \(e:C\to C\) is a primitive projector when \(e^2=e\) and every graded endomorphism \(f\) satisfying
\[
f^2=f,\qquad fe=f,\qquad ef=f
\]
equals either zero or \(e\).

The equation \(ef=f\) places the image of \(f\) in the image of \(e\). The equation \(fe=f\) says that \(f\) depends only on the component selected by \(e\): for \(v\in\ker e\), it gives \(f(v)=f(e(v))=0\). Thus the predicate describes idempotents acting within that image summand.

## Identity and zero projectors

For \(e=1_C\), the two support equations hold automatically. Primitivity says that every graded idempotent on \(C\) is zero or the identity. A decomposition into two nonzero graded summands would yield a projection that is neither, so a sheaf with primitive identity is indecomposable.

For \(e=0\), the equation \(fe=f\) forces \(f=0\), so the zero projector satisfies the formal predicate. When a nonzero normalized top stalk is present, it supplies the nonzero vector used to recognize a split summand as the whole sheaf.

## Examples over a domain

On the single-vertex sheaf with stalk \(A\), every \(A\)-linear endomorphism is multiplication by a scalar \(a\). The idempotence equation is \(a(a-1)=0\). If \(A\) is a domain, \(a=0\) or \(a=1\), so the identity is primitive.

On the single-vertex sheaf with stalk \(A\oplus A\), projection onto the first coordinate is a nonzero idempotent different from the identity. Thus the identity of this sheaf is not primitive.

The transfer theorem [[node:kl.sheaves.primitive_image]] relates primitivity of a split summand to primitivity of its projector in the ambient sheaf.

## References

The source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.PrimitiveProjector`: [BalancedPairings.lean:1648](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1648).
