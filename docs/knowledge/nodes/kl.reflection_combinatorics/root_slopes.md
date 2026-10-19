---
id: kl.order.root_slopes
title: Heights, normalized positive roots, and geometric slopes
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.detail.positive_roots
- kl.realization.tits_form
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.TitsSpace.height
  - OAI.KLInvariance.TitsSpace.PositiveRoot.height_pos
  - OAI.KLInvariance.TitsSpace.normalizedRoot
  - OAI.KLInvariance.TitsSpace.normalizedRoot_injective
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:86
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.height
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:93
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PositiveRoot.height_pos
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:103
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.normalizedRoot
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:105
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.normalizedRoot_injective
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

# Heights, normalized positive roots, and geometric slopes

In the original real root space \(V_0=\mathbb R^I\), define the height functional by
\[
h(v)=\sum_{i\in I}v_i.
\]
A positive root \(a\) is nonzero with nonnegative coordinates, so at least one coordinate is positive and \(h(a)>0\).

Its normalized root is
\[
\widehat a=\frac{a}{h(a)}.
\]
It lies on the affine hyperplane \(h=1\). For a linear functional \(f:V_0\to\mathbb R\), define the slope
\[
s_f(a)=f(\widehat a)=\frac{f(a)}{h(a)}.
\]

## Injectivity of normalization

If \(\widehat a=\widehat b\), then \(a=(h(a)/h(b))b\). The scalar is positive. Both roots have squared Tits norm \(2\), so its square is one and it equals one. Hence \(a=b\).

Thus normalization keeps the positive roots distinct, even when the Tits form is degenerate.

## Generic slope functions on a root plane

A functional is generic on the positive roots when its slope function is injective. Comparing its slopes then gives a total order.

For a root plane \(P\), normalized roots lie on the affine line
\(P\cap\{h=1\}\). A generic slope function distinguishes their normalized points. The [[node:kl.detail.geometric_functional|generic-functional theorem]] proves existence, and the geometric-reflection-order entry describes the fixed choice used in Lean.

## An A2 example

Let \(a,b\) be the two simple roots, so \(h(a)=h(b)=1\) and \(h(a+b)=2\). Choose \(f(a)=0,f(b)=1\). Then
\[
s(a)=0,\qquad s(a+b)=\frac12,\qquad s(b)=1.
\]
The normalized middle root is \((a+b)/2\), the midpoint of the two normalized simple roots.

## References

The local source declarations below give the definitions and their properties.

## Lean formalization

`OAI.KLInvariance.TitsSpace.height`: [ReflectionSchedules.lean:86](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L86).

`OAI.KLInvariance.TitsSpace.PositiveRoot.height_pos`: [ReflectionSchedules.lean:93](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L93).

`OAI.KLInvariance.TitsSpace.normalizedRoot`: [ReflectionSchedules.lean:103](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L103).

`OAI.KLInvariance.TitsSpace.normalizedRoot_injective`: [ReflectionSchedules.lean:105](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L105).
