---
id: kl.dihedral.angular_extremes_simple
title: An extreme positive root is simple in its subspace
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.plane_simple
- kl.order.slope_cone
- kl.geometry.plane_weights
lean:
  repository: openai-kl
  modules:
  - Decomposition
  declarations:
  - OAI.KLInvariance.TitsSpace.planeSimple_of_extreme
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:507
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.planeSimple_of_extreme
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

# An extreme positive root is simple in its subspace

Fix the geometric slope in a finite-generator Coxeter system. Let \(P\) be a root-space subspace and \(a\in\Phi^+\cap P\). Suppose \(a\) has minimum or maximum slope among all positive roots in \(P\). Then \(a\) is plane-simple:
\[
r_a(c)\text{ is negative},\quad c\in\Phi^+\cap P
\quad\Longleftrightarrow\quad c=a.
\]

*Proof.*

### Step 1. Pair a root whose sign changes

Suppose \(c\in\Phi^+\cap P\) is inverted by \(r_a\), and put
\[
c'=-r_a(c).
\]
The root \(c'\) is positive. The reflection formula makes
\[
c+c'=B(a,c)a.
\]
It also places \(c'\) in \(P\).

Apply height to the equality. Both roots on the left have positive height, so
\[
B(a,c)=\frac{h(c)+h(c')}{h(a)}>0.
\]

### Step 2. Exclude a fixed partner when c differs from a

Assume \(c\ne a\). If \(c'=c\), then
\(c=(B(a,c)/2)a\) with positive scalar. Comparing the squared norms \(2\) gives that scalar equal to one, contradicting \(c\ne a\). Therefore \(c,c'\) are distinct and their slopes are distinct.

### Step 3. Place a strictly between the partners

The equality in Step 1 can be rewritten as
\[
a=\frac1{B(a,c)}c+\frac1{B(a,c)}c'.
\]
Both coefficients are strictly positive. The [[node:kl.order.slope_cone|slope-cone theorem]] therefore places \(s(a)\) strictly between \(s(c)\) and \(s(c')\).

If \(a\) is a minimum, the smaller partner slope contradicts minimality. If \(a\) is a maximum, the larger partner slope contradicts maximality. Hence every positive root of \(P\) inverted by \(r_a\) must equal \(a\).

### Step 4. Verify the remaining inversion

The root norm is \(B(a,a)=2\), so
\(r_a(a)=a-2a=-a\).
Thus \(a\) itself is inverted, completing the criterion.

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.TitsSpace.planeSimple_of_extreme`: [Decomposition.lean:507](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L507).
