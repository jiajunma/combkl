---
id: kl.notes.reflection_order
title: Geometric reflection orders
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.order.root_slopes
- kl.detail.geometric_functional
- kl.detail.positive_roots
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.TitsSpace.RatioOrder
  - OAI.KLInvariance.TitsSpace.RatioOrder.slope
  - OAI.KLInvariance.TitsSpace.RatioOrder.denominator_pos
  - OAI.KLInvariance.TitsSpace.RatioOrder.Adapted
  - OAI.KLInvariance.TitsSpace.geometricFunctional
  - OAI.KLInvariance.TitsSpace.geometricSlope
  - OAI.KLInvariance.TitsSpace.geometricSlope_injective
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1181
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.RatioOrder
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1190
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.RatioOrder.slope
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1192
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.RatioOrder.denominator_pos
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1198
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.RatioOrder.Adapted
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:503
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.geometricFunctional
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:505
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.geometricSlope
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:507
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.geometricSlope_injective
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the source hypotheses retained?
  verdict: The statement and proof follow the fixed formal development and its paper
    counterpart.
tags:
- Kazhdan-Lusztig
- background
---

# Geometric reflection orders

Fix a finite-generator Coxeter system and its positive roots in the original real root space \(V_0\). A ratio-order datum consists of two linear functionals
\[
h,f:V_0\to\mathbb R
\]
such that \(h\) is positive on every simple root and the ratios
\[
s(a)=\frac{f(a)}{h(a)}\qquad(a\in\Phi^+)
\]
are all distinct.

The denominator is positive on every positive root. Indeed, write
\(a=\sum_i a_i\alpha_i\), where \(a_i\ge0\) and at least one coefficient is positive. Then
\[
h(a)=\sum_i a_i h(\alpha_i)>0.
\]
Thus every ratio is defined, and their comparison gives a total order on the positive roots.

## The angular-order condition

If \(c=ra+tb\) with \(r,t>0\), then
\[
s(c)=
\frac{rh(a)}{rh(a)+th(b)}s(a)
+\frac{th(b)}{rh(a)+th(b)}s(b).
\]
The two coefficients are positive and sum to one. Hence \(s(c)\) lies strictly between \(s(a)\) and \(s(b)\) whenever those endpoint slopes are ordered.

This is the reflection-order betweenness condition. In a fixed root plane, normalizing roots by \(h\) places them on the affine line \(h=1\); the numerator \(f\) orders those points in one of the two angular directions.

## The fixed geometric order in Lean

Lean uses the height functional \(h(v)=\sum_i v_i\) for its fixed geometric order. The [[node:kl.detail.geometric_functional|generic-functional theorem]] chooses \(f\) separating every normalized positive root. The resulting functions are the geometric functional and geometric slope.

The more general ratio-order structure also records other positive denominators and generic numerators. Its four fields are the denominator, numerator, positivity on simple roots, and injectivity of the ratio function.

## An order adapted to an element

A ratio order is adapted to \(y\in W\) when
\[
s(a)<0\quad\Longleftrightarrow\quad y^{-1}a\text{ is negative},
\qquad s(a)\ne0
\]
for every positive root \(a\). The zero cut then separates the inversion set of \(y\) from the other positive roots.

In type \(A_2\), take simple roots \(a,b\), use height as denominator, and choose
\(f(a)=-1,f(b)=3\). The slopes of \(a,a+b,b\) are \(-1,1,3\). The sole negative slope is that of \(a\), so the order is adapted to the simple reflection \(r_a\).

## Ordering edges of a finite interval

Each reflection edge has a positive-root label. Restricting the order to the finitely many edge labels in a Bruhat interval gives an edge schedule.

Two edges with the same reflection label cannot share a vertex: the reflection sends a vertex \(w\) to the unique other endpoint \(tw\). Thus repeated labels occur on disjoint pairs of vertices.

An interval isomorphism also transports an edge schedule from a target interval to its source. The dihedral transport theorems establish the local order and counting properties used by that transported schedule.

## References

The local source declarations below give the definitions and their properties.

## Lean formalization

The fields `denominator`, `numerator`, `positive`, and `generic` record the two functionals and the two conditions above. The predicate `Adapted` records the zero-cut inversion condition.

`OAI.KLInvariance.TitsSpace.RatioOrder`: [DyerPaths.lean:1181](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1181).

`OAI.KLInvariance.TitsSpace.RatioOrder.slope`: [DyerPaths.lean:1190](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1190).

`OAI.KLInvariance.TitsSpace.RatioOrder.denominator_pos`: [DyerPaths.lean:1192](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1192).

`OAI.KLInvariance.TitsSpace.RatioOrder.Adapted`: [DyerPaths.lean:1198](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1198).

`OAI.KLInvariance.TitsSpace.geometricFunctional`: [ReflectionSchedules.lean:503](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L503).

`OAI.KLInvariance.TitsSpace.geometricSlope`: [ReflectionSchedules.lean:505](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L505).

`OAI.KLInvariance.TitsSpace.geometricSlope_injective`: [ReflectionSchedules.lean:507](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L507).
