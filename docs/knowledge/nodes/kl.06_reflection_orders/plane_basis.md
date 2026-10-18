---
id: kl.detail.plane_basis
title: Angular boundary roots of a root plane
kind: definition
status: formalized
primary_topic: kl.06_reflection_orders
topics:
- kl.06_reflection_orders
uses:
- kl.detail.positive_roots
- kl.notes.reflection_order
lean:
  repository: openai-kl
  modules:
  - Decomposition
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:619
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis
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

# Angular boundary roots of a root plane

Fix the geometric slope order on positive roots, and let \(P\subseteq V_0\) be a root plane. A plane basis consists of two positive roots \(a,b\) satisfying all of the following conditions:

- \(a\ne b\).
- \(\operatorname{span}_{\mathbb R}\{a,b\}=P\).
- For every positive root \(r\in P\), \(s(a)\le s(r)\).
- For every positive root \(r\in P\), \(s(r)\le s(b)\).

These are the two angular boundary roots, not an arbitrary vector-space basis. The conditions identify the first and last roots of the plane in the chosen order.

This datum does not itself assert that their reflections give a Coxeter system. The formal development subsequently proves that assertion using sign and inversion criteria, then constructs the dihedral system and relative intervals. Thus using the induced system requires the proved construction, not just the existence of two independent vectors.

## References

The precise Lean sources are listed below.

## Lean formalization

The fields `left`, `right`, `distinct`, `plane_eq`, `left_min`, and `right_max` record the two roots and exactly the four conditions above.

`OAI.KLInvariance.TitsSpace.PlaneBasis`: [Decomposition.lean:619](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L619).
