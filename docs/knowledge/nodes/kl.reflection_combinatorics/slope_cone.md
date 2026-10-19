---
id: kl.order.slope_cone
title: Slope betweenness is equivalent to a positive root combination
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.order.root_slopes
- kl.realization.root_planes
- kl.detail.root_inversions
lean:
  repository: openai-kl
  modules:
  - Decomposition
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.TitsSpace.functionalRatio_between
  - OAI.KLInvariance.TitsSpace.positive_combination_of_slope_between
  - OAI.KLInvariance.TitsSpace.noninverted_of_positive_combination
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:138
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.functionalRatio_between
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:395
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.positive_combination_of_slope_between
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:434
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.noninverted_of_positive_combination
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

# Slope betweenness is equivalent to a positive root combination

Fix the injective geometric slope on positive roots of a finite-generator Coxeter system. Let \(a,b,c\) be positive roots, with \(c\in P(a,b)\) and \(s(a)<s(b)\). Then
\[
s(a)<s(c)<s(b)
\quad\Longleftrightarrow\quad
c=ra+tb\text{ for some }r,t>0.
\]

A second positivity statement will be used with this cone: if \(c=ra+tb\) with \(r,t\ge0\), and \(w^{-1}a,w^{-1}b\) are positive, then \(w^{-1}c\) is positive.

*Proof.*

### Step 1. Normalize the linear combination

Since \(c\in P(a,b)\), write \(c=ra+tb\) for real \(r,t\). Applying height gives
\(h(c)=rh(a)+th(b)\). Put
\[
u=\frac{rh(a)}{h(c)},\qquad v=\frac{th(b)}{h(c)}.
\]
Then \(u+v=1\), and applying the numerator functional gives
\[
s(c)=u\,s(a)+v\,s(b).
\]

### Step 2. Derive positive coefficients from strict betweenness

Let \(\delta=s(b)-s(a)>0\). Solving the two equations in Step 1 gives
\[
v=\frac{s(c)-s(a)}{\delta},\qquad
u=\frac{s(b)-s(c)}{\delta}.
\]
If \(s(a)<s(c)<s(b)\), both are positive. All heights are positive, so
\(r=u h(c)/h(a)>0\) and \(t=v h(c)/h(b)>0\).

### Step 3. Derive betweenness from positive coefficients

Conversely, if \(r,t>0\), then \(u,v>0\) and \(u+v=1\). Hence
\[
s(c)-s(a)=v\delta>0,\qquad
s(b)-s(c)=u\delta>0.
\]
This gives strict betweenness.

### Step 4. Preserve positivity under a common inverse action

For the final assertion, linearity gives
\[
w^{-1}c=r\,w^{-1}a+t\,w^{-1}b.
\]
Each coordinate is a sum of nonnegative terms. The vector is a nonzero root, since the group action is invertible and \(c\ne0\). It is therefore positive, as asserted.

This convexity statement makes the two boundary roots of a plane sufficient for detecting an inversion of a positive root inside their cone.

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.TitsSpace.functionalRatio_between`: [ReflectionSchedules.lean:138](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L138).

`OAI.KLInvariance.TitsSpace.positive_combination_of_slope_between`: [Decomposition.lean:395](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L395).

`OAI.KLInvariance.TitsSpace.noninverted_of_positive_combination`: [Decomposition.lean:434](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L434).
