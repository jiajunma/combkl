---
id: kl.realization.root_planes
title: Root spans and two-dimensional root planes
kind: definition
status: formalized
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.detail.positive_roots
- kl.realization.tits_form
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.TitsSpace.rootPlane
  - OAI.KLInvariance.TitsSpace.positiveRoots_independent
  - OAI.KLInvariance.TitsSpace.rootPlane_finrank
  - OAI.KLInvariance.TitsSpace.rootPlane_eq_iff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:335
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.rootPlane
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:640
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.positiveRoots_independent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:648
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.rootPlane_finrank
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:669
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.rootPlane_eq_iff
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

# Root spans and two-dimensional root planes

Fix a Coxeter system with finitely many simple generators, its original real root space \(V_0=\mathbb R^I\), and its normalized positive roots \(\Phi^+\). Every root is nonzero and has Tits squared norm \(2\).

For \(a,b\in\Phi^+\), define
\[
P(a,b)=\operatorname{span}_{\mathbb R}\{a,b\}.
\]
If \(a=b\), this is the root line \(\mathbb R a\). If \(a\ne b\), it is a two-dimensional root plane.

## Independence of distinct positive roots

Suppose \(a=cb\). Since \(b\) has a positive coordinate and \(a\) has nonnegative coordinates, \(c\ge0\). Nonvanishing of \(a\) gives \(c>0\). The norm equation gives
\[
2=B(a,a)=c^2B(b,b)=2c^2,
\]
so \(c=1\) and \(a=b\). Distinct positive roots are therefore linearly independent, which proves the dimension assertion.

## Changing the spanning pair

If \(c,d\) are distinct positive roots in \(P(a,b)\), their span is contained in \(P(a,b)\). Both spans have dimension two, so
\[
P(c,d)=P(a,b).
\]
In particular, for \(a\ne b\),
\[
P(a,c)=P(a,b)
\quad\Longleftrightarrow\quad
c\ne a\text{ and }c\in P(a,b).
\]

## Two rank-two examples

For type \(A_2\), let \(a,b\) be the simple roots with
\[
B(a,a)=B(b,b)=2,\qquad B(a,b)=-1.
\]
The positive roots are \(a,b,a+b\), and any two distinct ones span the same plane. The restricted form has matrix
\(\begin{pmatrix}2&-1\\ -1&2\end{pmatrix}\).

For infinite dihedral type, the simple-root matrix is
\(\begin{pmatrix}2&-2\\ -2&2\end{pmatrix}\).
The two simple roots still span a two-dimensional vector space. Its restricted form has radical \(\mathbb R(a+b)\). Thus the vector-space dimension and the degeneracy of the restricted bilinear form are separate data.

The induced dihedral construction uses the positive roots contained in this actual span. The extended realization supplies a nondegenerate ambient form when the argument needs to recover a plane from a product of reflections.

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.TitsSpace.rootPlane`: [ReflectionSchedules.lean:335](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L335).

`OAI.KLInvariance.TitsSpace.positiveRoots_independent`: [ReflectionSchedules.lean:640](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L640).

`OAI.KLInvariance.TitsSpace.rootPlane_finrank`: [ReflectionSchedules.lean:648](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L648).

`OAI.KLInvariance.TitsSpace.rootPlane_eq_iff`: [ReflectionSchedules.lean:669](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L669).
