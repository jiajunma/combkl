---
id: kl.dihedral.induced_signed
title: Signed ambient roots for the induced plane system
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.induced_system
- kl.realization.signed_root_representation
- kl.coxeter.signed_reflection_action
lean:
  repository: openai-kl
  modules:
  - Decomposition
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.InducedSigned
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:965
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.InducedSigned
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

# Signed ambient roots for the induced plane system

Let \(P\) be a root plane with its induced Coxeter system on \(D_P\). A signed pair consists of \(t\in D_P\) and \(z\in\mathbb Z/2\mathbb Z\).

An ambient vector \(v\in V_0\) realizes the induced signed datum \((t,z)\) when:

1. \(v\) represents the ambient reflection given by the inclusion of \(t\) in \(W\);
2. \(v\in P\);
3. its coordinates have the sign recorded by \(z\):
   \[
   \bigl(z=0\text{ and }v_i\ge0\text{ for every }i\bigr)
   \quad\text{or}\quad
   \bigl(z=1\text{ and }v_i\le0\text{ for every }i\bigr).
   \]

The representation condition makes \(v\) a nonzero normalized root. Thus sign zero means a positive root, and sign one means a negative root.

For a positive plane root \(a\), the vector \(a\) realizes \((r_a,0)\), while \(-a\) realizes \((r_a,1)\). Both signs represent the same reflection.

## The two actions compared by this relation

The induced Coxeter system acts on signed pairs. For a simple reflection \(s\),
\[
s\cdot(t,z)=(sts,\ z+1_{t=s}),
\]
where the sign coordinate is added modulo two.

The ambient geometric action sends \(v\) to \(s(v)\). The signed-action theorem proves that these two actions preserve the displayed relation: conjugation describes the new reflection, plane preservation keeps the vector in \(P\), and the plane-simple sign criterion supplies exactly the sign toggle.

This relation is the input to the theorem identifying intrinsic inversions with signs of the original ambient roots.

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

The fields `represents`, `plane_mem`, and `sign` are respectively the ambient reflection representation, membership in the plane, and the two-case sign condition.

`OAI.KLInvariance.TitsSpace.PlaneBasis.InducedSigned`: [Decomposition.lean:965](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L965).
