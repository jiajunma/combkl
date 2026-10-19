---
id: kl.detail.plane_basis
title: Angular boundary roots of a root plane
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.realization.root_planes
- kl.order.root_slopes
- kl.notes.reflection_order
lean:
  repository: openai-kl
  modules:
  - Decomposition
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis
  - OAI.KLInvariance.TitsSpace.PlaneBasis.left_mem
  - OAI.KLInvariance.TitsSpace.PlaneBasis.right_mem
  - OAI.KLInvariance.TitsSpace.PlaneBasis.positive_cone
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:619
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:638
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.left_mem
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:642
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.right_mem
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:653
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.positive_cone
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

Fix a root plane \(P\) and the injective geometric slope \(s\). A plane basis is a pair of positive roots \((a,b)\) with
\[
a\ne b,\qquad P=\operatorname{span}_{\mathbb R}\{a,b\},
\]
and the endpoint inequalities
\[
s(a)\le s(c)\le s(b)\qquad(c\in\Phi^+\cap P).
\]
Thus \(a,b\) are the first and last positive roots of the plane in the chosen slope order.

Since slopes are injective and \(a\ne b\), the endpoint slopes satisfy \(s(a)<s(b)\). The span condition and root independence make \(a,b\) a vector-space basis of \(P\).

## The positive cone determined by the endpoints

Every positive root \(c\in P\) is a nonnegative combination of \(a,b\). At an endpoint the coefficients are \((1,0)\) or \((0,1)\). For any other \(c\), injectivity turns the endpoint inequalities into
\[
s(a)<s(c)<s(b).
\]
The [[node:kl.order.slope_cone|slope-cone theorem]] then gives \(c=ra+tb\) with \(r,t>0\).

The [[node:kl.dihedral.angular_extremes_simple|angular-extreme theorem]] makes both endpoints plane-simple. Their reflections are the two generators used to construct the induced dihedral Coxeter system.

## The fields of the datum

The two root fields choose \(a,b\). The distinctness field distinguishes their rays, the plane-equality field identifies their span with \(P\), and the two extremality fields impose the lower and upper slope inequalities on every positive root of \(P\).

For the \(A_2\) order \(a<a+b<b\), the plane basis is \((a,b)\); the middle root is the positive combination \(a+b\). The existence theorem constructs such endpoint data for every root plane, including planes with infinitely many positive roots.

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

The fields `left`, `right`, `distinct`, `plane_eq`, `left_min`, and `right_max` are the two roots and the four displayed conditions.

`OAI.KLInvariance.TitsSpace.PlaneBasis`: [Decomposition.lean:619](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L619).

`OAI.KLInvariance.TitsSpace.PlaneBasis.left_mem`: [Decomposition.lean:638](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L638).

`OAI.KLInvariance.TitsSpace.PlaneBasis.right_mem`: [Decomposition.lean:642](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L642).

`OAI.KLInvariance.TitsSpace.PlaneBasis.positive_cone`: [Decomposition.lean:653](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L653).
