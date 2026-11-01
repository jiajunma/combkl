---
id: kl.order.chamber_adaptation
title: A chamber determines the inversion signs and a least simple descent
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.notes.reflection_order
- kl.realization.positive_root_action
- kl.detail.root_inversion_count
- kl.coxeter.word_data
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.TitsSpace.RatioOrder.adapted_of_chamber
  - OAI.KLInvariance.TitsSpace.RatioOrder.simple_lower_bound
  - OAI.KLInvariance.TitsSpace.RatioOrder.exists_least_simple
  - OAI.KLInvariance.TitsSpace.RatioOrder.least_simple_descent
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1242
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.RatioOrder.adapted_of_chamber
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1201
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.RatioOrder.simple_lower_bound
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1214
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.RatioOrder.exists_least_simple
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1220
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.RatioOrder.least_simple_descent
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the chamber, positivity, simple-label exclusions, two orders and exact
    induction hypotheses retained?
  verdict: Read adapted_of_chamber and the least-simple lemmas. Preserved the distinct
    chamber and adapted hypotheses, both inverse-root sign cases, the coordinate sum
    argument and the nonempty-generator deduction from y!=1.
tags:
- Kazhdan-Lusztig
- reflection_orders
---

# A chamber determines the inversion signs and a least simple descent

Fix a finite-generator Coxeter system \(W\), its original real root space \(V_0\), simple roots \(\alpha_i\), and root action \(\rho\).
Let \(O=(h,f)\) be a ratio order, with slope
\[
\sigma_O(a)=f(a)/h(a)
\]
on positive roots. The denominator is positive on simple roots and hence on every positive root.

If \(O\) satisfies the chamber condition at \(y\in W\),
\[
f(\rho(y)\alpha_i)>0\quad\text{for every }i,
\tag{1}
\]
then \(O\) is adapted to \(y\):
\[
\sigma_O(a)<0
\Longleftrightarrow
\rho(y^{-1})a\text{ is negative},
\qquad \sigma_O(a)\ne0
\tag{2}
\]
for every positive root \(a\).

For any \(y\ne1\) and any ratio order satisfying the adapted condition (2), there is a simple generator \(s_i\) such that
\[
\ell(s_i y)<\ell(y),\qquad
c:=\sigma_O(\alpha_i)<0,\qquad
c\le\sigma_O(a)\quad(a\in\Phi^+).
\tag{3}
\]
Thus a simple left descent has least slope among all positive roots.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**An actual chamber numerator and the inversion-sign order.**

**OpenAI notes:** The notes cite the reflection-order path formula and construct separating ratios of linear functionals for the geometric orders used in comparison. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [sec:background](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

**Lean (primary):** The path proof chooses a numerator positive on the transformed simple roots of a prescribed chamber. It implies the inversion-sign condition and supplies a least simple descent. Existence uses height composed with the inverse action, a polynomial perturbation preserving finitely many strict inequalities, and avoidance of countably many root-tie polynomials. [DyerPaths:1240](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1240), [DyerPaths:1198](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1198), [DyerPaths:1242](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1242), [DyerPaths:1220](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1220), [DyerPaths:1266](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1266), [ReflectionSchedules:18](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L18), [ReflectionSchedules:39](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L39).

**Role in the proof:** The Blueprint distinguishes the Chamber and Adapted predicates and explains the coordinate-polynomial family used to satisfy genericity and chamber positivity together.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Positivity after transporting the functional

Define \(g=f\circ\rho(y)\). Condition (1) says \(g(\alpha_i)>0\) for every simple root.
A positive root \(a=\sum_i a_i\alpha_i\) has all \(a_i\ge0\), with at least one positive. Therefore
\[
g(a)=\sum_i a_i g(\alpha_i)>0.
\]
The same argument gives \(h(a)>0\) for the denominator.

### Step 2. The two signs of the inverse-transformed root

For any root vector \(v\), the action law gives
\[
g(\rho(y^{-1})v)
=f(\rho(y)\rho(y^{-1})v)=f(v).
\]
The root \(\rho(y^{-1})a\) is either positive or negative.
In the positive case, Step 1 gives \(f(a)>0\). In the negative case, its negative is positive, so
\[
0<g(-\rho(y^{-1})a)=-f(a),
\]
giving \(f(a)<0\).
Division by \(h(a)>0\) preserves these signs. They are strict in both cases, proving (2).

### Step 3. A minimum on simple roots bounds every root

Suppose \(i\) minimizes the slopes of the simple roots, and put \(c=\sigma_O(\alpha_i)\).
For every \(j\),
\[
c\,h(\alpha_j)\le f(\alpha_j),
\]
because \(h(\alpha_j)>0\). Multiply by the nonnegative coefficient \(a_j\) of a positive root and sum:
\[
c\,h(a)
=\sum_j a_j c\,h(\alpha_j)
\le\sum_j a_j f(\alpha_j)=f(a).
\]
Divide by \(h(a)>0\). This proves \(c\le\sigma_O(a)\) for every positive root.

### Step 4. Negativity and the descent condition

Since \(y\ne1\), a reduced expression for \(y\) has a first letter \(s_j\), which is a simple left descent. In particular the simple-generator set is nonempty, so its finite set of slopes has a minimum \(c=\sigma_O(\alpha_i)\).

The [[node:kl.detail.root_inversion_count|root-sign and length criterion]] identifies the descent \(s_j\) with negativity of \(\rho(y^{-1})\alpha_j\). Adaptation gives \(\sigma_O(\alpha_j)<0\), hence
\[
c\le\sigma_O(\alpha_j)<0.
\]
Adaptation applied to \(\alpha_i\) now makes \(\rho(y^{-1})\alpha_i\) negative. The same [[node:kl.detail.root_inversion_count|root-sign and length criterion]] gives \(\ell(s_i y)<\ell(y)\). Step 3 supplies the bound on every positive-root slope, completing (3).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.RatioOrder.adapted_of_chamber`: [DyerPaths.lean:1242](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1242).

`OAI.KLInvariance.TitsSpace.RatioOrder.simple_lower_bound`: [DyerPaths.lean:1201](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1201).

`OAI.KLInvariance.TitsSpace.RatioOrder.exists_least_simple`: [DyerPaths.lean:1214](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1214).

`OAI.KLInvariance.TitsSpace.RatioOrder.least_simple_descent`: [DyerPaths.lean:1220](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1220).
