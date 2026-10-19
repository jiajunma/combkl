---
id: kl.dihedral.plane_simple
title: Simple roots relative to a root subspace
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.realization.root_subgroups
- kl.detail.root_inversions
- kl.detail.root_reflection_correspondence
lean:
  repository: openai-kl
  modules:
  - Decomposition
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneSimple
  - OAI.KLInvariance.TitsSpace.PlaneSimple.partner_val
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:497
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneSimple
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:545
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneSimple.partner_val
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

# Simple roots relative to a root subspace

Let \(P\) be a subspace of the original root space. A positive root \(a\) is plane-simple in \(P\) when
\[
a\in P,\qquad
\{c\in\Phi^+\cap P:r_a(c)\text{ is negative}\}=\{a\}.
\]
Equivalently, \(r_a\) inverts a positive root in \(P\) exactly when that root is \(a\). This is the local simple-root criterion used to construct the induced Coxeter system.

The reflection formula and \(B(a,a)=2\) give \(r_a(a)=-a\). For any other positive root \(c\in P\), the criterion excludes a negative image. The root-sign dichotomy therefore makes \(r_a(c)\) positive.

## The partner operation for a plane-simple root

The partner of \(c\) under \(r_a\) is the positive root on the line of \(r_a(c)\). If \(a\) is plane-simple and \(c\ne a\) lies in \(P\), then the image itself is already positive:
\[
\operatorname{partner}(a,c)=r_a(c).
\]
The reflection preserves \(P\), so this partner remains in the subspace.

## The A2 plane

For simple roots \(a,b\) with \(B(a,b)=-1\), the positive roots are \(a,b,a+b\). The reflection formulas give
\[
r_a(a)=-a,\qquad r_a(b)=a+b,\qquad r_a(a+b)=b.
\]
Thus \(a\) satisfies the criterion; the same calculation with \(a,b\) interchanged proves it for \(b\).

For the middle root \(a+b\),
\[
r_{a+b}(a)=a-B(a+b,a)(a+b)=a-(a+b)=-b.
\]
It therefore inverts a different positive root and fails the plane-simple criterion.

The angular-endpoint theorem proves that the two extreme roots in a root plane satisfy this criterion in general.

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneSimple`: [Decomposition.lean:497](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L497).

`OAI.KLInvariance.TitsSpace.PlaneSimple.partner_val`: [Decomposition.lean:545](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L545).
