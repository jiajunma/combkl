---
id: kl.geometry.plane_inversion_change
title: Plane weights measure the change of the plane inversion count
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.plane_length
- kl.geometry.plane_weight_sum
- kl.realization.root_planes
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.TitsSpace.rootPlane_grouped_erase
  - OAI.KLInvariance.TitsSpace.planeDefect_eq_relative_difference
  - OAI.KLInvariance.TitsSpace.planeWeight_relative_degree
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:708
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.rootPlane_grouped_erase
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:733
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.planeDefect_eq_relative_difference
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:742
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.planeWeight_relative_degree
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

# Plane weights measure the change of the plane inversion count

Let \(a,b\) be distinct positive roots, let \(P=P(a,b)\), and suppose \(x^{-1}a\) is positive. Put \(y=r_a x\). Then
\[
L_P(y)-L_P(x)=1+2k_P(x,a),
\]
where \(k_P(x,a)\) is the geometric plane weight.

*Proof.*

### Step 1. Express the count difference by inversion indicators

By definition,
\[
L_P(y)-L_P(x)
=\sum_{c\in\Phi^+\cap P}\bigl(n_y(c)-n_x(c)\bigr).
\]
Only finitely many summands are nonzero, because both inversion sets are finite.

The hypothesis gives \(n_x(a)=0\). Since
\(y^{-1}a=x^{-1}r_a(a)=-x^{-1}a\),
we have \(n_y(a)=1\). Thus the distinguished root contributes one.

### Step 2. Identify the remaining terms with the plane defect

For every positive \(c\ne a\), the root-span criterion gives
\[
c\in P\quad\Longleftrightarrow\quad P(a,c)=P.
\]
Therefore, after removing the distinguished root, the remaining sum is precisely
\[
D_P(x,y;a)
=\sum_{\substack{c\ne a\\ P(a,c)=P}}\bigl(n_y(c)-n_x(c)\bigr).
\]
Hence \(L_P(y)-L_P(x)-1=D_P(x,y;a)\).

### Step 3. Substitute the partner-pair count

The [[node:kl.geometry.plane_weight_sum|plane-weight theorem]] applies to the ascent root \(a\). It groups the remaining inversion changes into partner pairs inside \(P\) and proves
\[
D_P(x,y;a)=2k_P(x,a).
\]
Substitution gives the required equality.

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.TitsSpace.rootPlane_grouped_erase`: [ReflectionSchedules.lean:708](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L708).

`OAI.KLInvariance.TitsSpace.planeDefect_eq_relative_difference`: [ReflectionSchedules.lean:733](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L733).

`OAI.KLInvariance.TitsSpace.planeWeight_relative_degree`: [ReflectionSchedules.lean:742](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L742).
