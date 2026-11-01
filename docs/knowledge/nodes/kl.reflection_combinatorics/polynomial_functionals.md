---
id: kl.order.polynomial_functionals
title: Coordinate polynomials and a polynomial family of functionals
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses: []
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.ReflectionSchedules.coordinatePolynomial
  - OAI.KLInvariance.ReflectionSchedules.coordinatePolynomial_coeff
  - OAI.KLInvariance.ReflectionSchedules.coordinatePolynomial_injective
  - OAI.KLInvariance.ReflectionSchedules.momentFunctional
  - OAI.KLInvariance.ReflectionSchedules.coordinatePolynomial_eval
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:18
    format: lean-location
    note: OAI.KLInvariance.ReflectionSchedules.coordinatePolynomial
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:21
    format: lean-location
    note: OAI.KLInvariance.ReflectionSchedules.coordinatePolynomial_coeff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:33
    format: lean-location
    note: OAI.KLInvariance.ReflectionSchedules.coordinatePolynomial_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:39
    format: lean-location
    note: OAI.KLInvariance.ReflectionSchedules.momentFunctional
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:44
    format: lean-location
    note: OAI.KLInvariance.ReflectionSchedules.coordinatePolynomial_eval
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the chamber, positivity, simple-label exclusions, two orders and exact
    induction hypotheses retained?
  verdict: Read the finite-coordinate polynomial, coefficient recovery, injectivity,
    momentFunctional linearity and evaluation identity. Explained the exact f0+tau*momentFunctional(tau)
    perturbation used by chamber existence.
tags:
- Kazhdan-Lusztig
- reflection_orders
---

# Coordinate polynomials and a polynomial family of functionals

Let \(I\) be a finite coordinate set of size \(N\), and choose an enumeration
\(\nu:I\simeq\{0,\ldots,N-1\}\). A vector \(v\in\mathbb R^I\) has coordinates \(v_i\).
Its coordinate polynomial is
\[
P_v(X)=\sum_{i\in I}v_i X^{\nu(i)}\in\mathbb R[X].
\]
Lean calls this `ReflectionSchedules.coordinatePolynomial` and uses its chosen finite enumeration of \(I\).

## Recovery of the vector

Different coordinates have different exponents. The coefficient of \(X^{\nu(j)}\) in \(P_v\) is therefore exactly \(v_j\): the \(j\)-term contributes this coefficient, and all other monomials have different degrees.
Consequently \(P_v=P_w\) implies \(v_j=w_j\) for each \(j\), hence \(v=w\). In particular,
\[
P_v=0\Longleftrightarrow v=0.
\]
This gives the coefficient and injectivity lemmas used in the functional constructions.

## Evaluation as a linear functional

For a real parameter \(\tau\), define
\[
m_\tau(v)=\sum_{i\in I}v_i\tau^{\nu(i)}=P_v(\tau).
\]
The source calls \(m_\tau\) the `momentFunctional`. At fixed \(\tau\), it is linear in \(v\): distributing the coordinate sum gives
\[
m_\tau(v+w)=m_\tau(v)+m_\tau(w),\qquad
m_\tau(c v)=c\,m_\tau(v).
\]
Thus \(\tau\mapsto m_\tau\) is a one-parameter family of real linear functionals.

## A prescribed functional with polynomial perturbation

For a fixed real linear functional \(f_0\), put
\[
f_\tau=f_0+\tau m_\tau.
\]
At a fixed vector \(v\),
\[
f_\tau(v)=f_0(v)+\tau P_v(\tau).
\]
The right side is a polynomial in \(\tau\), so it is continuous. This continuity lets finitely many strict positivity conditions persist near \(\tau=0\).

If \(v\ne0\), the polynomial
\[
d_v(X)=f_0(v)+X P_v(X)
\]
is nonzero. Indeed, \(d_v=0\) would give \(f_0(v)=d_v(0)=0\), then \(XP_v=0\), then \(P_v=0\), contradicting \(v\ne0\).
It therefore has only finitely many real roots. The [[node:kl.order.chamber_existence|prescribed-chamber existence theorem]] applies this observation to differences of normalized roots.

For example, with two coordinates and \(v=(2,-1)\), one has
\[
P_v(X)=2-X,\qquad m_\tau(v)=2-\tau.
\]
If \(f_0(v)=3\), then \(f_\tau(v)=3+2\tau-\tau^2\). This example illustrates the distinction between linearity in the vector and polynomial dependence on the parameter.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**An actual chamber numerator and the inversion-sign order.**

**OpenAI notes:** The notes cite the reflection-order path formula and construct separating ratios of linear functionals for the geometric orders used in comparison. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [sec:background](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

**Lean (primary):** The path proof chooses a numerator positive on the transformed simple roots of a prescribed chamber. It implies the inversion-sign condition and supplies a least simple descent. Existence uses height composed with the inverse action, a polynomial perturbation preserving finitely many strict inequalities, and avoidance of countably many root-tie polynomials. [DyerPaths:1240](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1240), [DyerPaths:1198](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1198), [DyerPaths:1242](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1242), [DyerPaths:1220](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1220), [DyerPaths:1266](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1266), [ReflectionSchedules:18](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L18), [ReflectionSchedules:39](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L39).

**Role in the proof:** The Blueprint distinguishes the Chamber and Adapted predicates and explains the coordinate-polynomial family used to satisfy genericity and chamber positivity together.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ReflectionSchedules.coordinatePolynomial`: [ReflectionSchedules.lean:18](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L18).

`OAI.KLInvariance.ReflectionSchedules.coordinatePolynomial_coeff`: [ReflectionSchedules.lean:21](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L21).

`OAI.KLInvariance.ReflectionSchedules.coordinatePolynomial_injective`: [ReflectionSchedules.lean:33](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L33).

`OAI.KLInvariance.ReflectionSchedules.momentFunctional`: [ReflectionSchedules.lean:39](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L39).

`OAI.KLInvariance.ReflectionSchedules.coordinatePolynomial_eval`: [ReflectionSchedules.lean:44](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L44).
