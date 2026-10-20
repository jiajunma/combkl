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
  - DyerPaths
  declarations:
  - OAI.KLInvariance.TitsSpace.functionalRatio_between
  - OAI.KLInvariance.TitsSpace.positive_combination_of_slope_between
  - OAI.KLInvariance.TitsSpace.noninverted_of_positive_combination
  - OAI.KLInvariance.TitsSpace.inverted_of_positive_combination
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
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:844
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.inverted_of_positive_combination
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient and intrinsic systems, root signs, signed lengths, finite
    representative bounds and counting domains explicit?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- background
---

# Slope betweenness is equivalent to a positive root combination

Fix a finite-generator real Coxeter system. Let \(h\) be its positive height functional and \(f\) the chosen separating linear functional; its injective geometric slope is \(s(a)=f(a)/h(a)\) on positive roots. All such roots have \(h(a)>0\). Let \(a,b,c\) be positive roots, with \(c\in P(a,b)\) and \(s(a)<s(b)\). Then
\[
s(a)<s(c)<s(b)
\quad\Longleftrightarrow\quad
c=ra+tb\text{ for some }r,t>0.
\]

The same cone also controls inversion signs. If \(c=ra+tb\) with \(r,t\ge0\), and \(w^{-1}a,w^{-1}b\) are positive, then \(w^{-1}c\) is positive. If instead both transformed roots are negative, then \(w^{-1}c\) is negative. Equivalently, nonnegative combinations preserve a common noninversion or a common inversion sign.

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

For the noninverted assertion, linearity gives
\[
w^{-1}c=r\,w^{-1}a+t\,w^{-1}b.
\]
Each coordinate is a sum of nonnegative terms. The vector is a nonzero root, since the group action is invertible and \(c\ne0\). It is therefore positive, as asserted.

### Step 5. Preserve a common inverted sign

If \(w^{-1}a,w^{-1}b\) are negative, their coordinates are nonpositive. For each coordinate \(j\),
\[
(w^{-1}c)_j=r(w^{-1}a)_j+t(w^{-1}b)_j\le0
\]
because \(r,t\ge0\). Again \(w^{-1}c\) is a nonzero root. It is therefore negative, proving the inverted version.

These two closure statements combine with the endpoint bounds of a plane basis to determine the inversion cuts in that plane.

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.TitsSpace.functionalRatio_between`: [ReflectionSchedules.lean:138](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L138).

`OAI.KLInvariance.TitsSpace.positive_combination_of_slope_between`: [Decomposition.lean:395](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L395).

`OAI.KLInvariance.TitsSpace.noninverted_of_positive_combination`: [Decomposition.lean:434](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L434).

`OAI.KLInvariance.TitsSpace.inverted_of_positive_combination`: [DyerPaths.lean:844](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L844).
