---
id: kl.dihedral.plane_simple_steps
title: Inverse symmetry and simple steps for the plane inversion count
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.plane_length
- kl.dihedral.plane_simple
- kl.geometry.plane_inversion_change
- kl.realization.plane_reflection_membership
- kl.realization.positive_root_action
lean:
  repository: openai-kl
  modules:
  - Decomposition
  declarations:
  - OAI.KLInvariance.TitsSpace.planeLength_inv
  - OAI.KLInvariance.TitsSpace.PlaneSimple.planeWeight_eq_zero
  - OAI.KLInvariance.TitsSpace.PlaneSimple.planeLength_step
  - OAI.KLInvariance.TitsSpace.PlaneSimple.planeLength_step_down
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:759
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.planeLength_inv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:671
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneSimple.planeWeight_eq_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:691
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneSimple.planeLength_step
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:701
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneSimple.planeLength_step_down
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- background
---

# Inverse symmetry and simple steps for the plane inversion count

Let \(P\) be a subspace of the original root space of a finite-generator Coxeter system. For \(w\in D_P\),
\[
L_P(w^{-1})=L_P(w).
\]
Now suppose \(P\) is a root plane and \(a\) is plane-simple in \(P\). Then for every \(x\in W\),
\[
L_P(r_a x)=
\begin{cases}
L_P(x)+1,&x^{-1}a\text{ is positive},\\
L_P(x)-1,&x^{-1}a\text{ is negative}.
\end{cases}
\]

*Proof.*

### Step 1. Match the inversion sets of w and its inverse

If \(a\in\Phi^+\cap P\) is inverted by \(w\), set \(c=-w^{-1}a\). It is a positive root. The subgroup preserves \(P\), so \(c\in P\). Moreover
\[
w(c)=-a
\]
is negative, making \(c\) an inversion of \(w^{-1}\).

Conversely, for a positive \(c\in P\) inverted by \(w^{-1}\), put \(a=-wc\). This is a positive root in \(P\), and \(w^{-1}a=-c\) is negative. The two constructions are inverse. They give a bijection between the finite plane inversion sets, proving the equality of their counts.

### Step 2. Show that the plane weight of a plane-simple root is zero

A half-root contributing to \(k_P(x,a)\) would be a positive \(c\ne a\) spanning \(P\) together with \(a\), and flipped to negative by \(r_a\). Plane simplicity says that the only positive root of \(P\) flipped by \(r_a\) is \(a\).

There are therefore no contributing half-roots for this plane, and
\(k_P(x,a)=0\).

### Step 3. Obtain the upward step

Choose a positive root \(b\in P\) distinct from \(a\); it exists because \(P\) is a root plane. The two roots span \(P\).

If \(x^{-1}a\) is positive, the [[node:kl.geometry.plane_inversion_change|plane-inversion-change theorem]] gives
\[
L_P(r_a x)-L_P(x)=1+2k_P(x,a)=1.
\]
This is the first case.

### Step 4. Obtain the downward step

If \(x^{-1}a\) is negative, put \(y=r_a x\). Then
\[
y^{-1}a=x^{-1}r_a(a)=-x^{-1}a
\]
is positive. Apply Step 3 to \(y\):
\[
L_P(r_a y)=L_P(y)+1.
\]
Since \(r_a y=x\), this says \(L_P(r_a x)=L_P(x)-1\), proving the second case.

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.TitsSpace.planeLength_inv`: [Decomposition.lean:759](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L759).

`OAI.KLInvariance.TitsSpace.PlaneSimple.planeWeight_eq_zero`: [Decomposition.lean:671](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L671).

`OAI.KLInvariance.TitsSpace.PlaneSimple.planeLength_step`: [Decomposition.lean:691](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L691).

`OAI.KLInvariance.TitsSpace.PlaneSimple.planeLength_step_down`: [Decomposition.lean:701](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L701).
