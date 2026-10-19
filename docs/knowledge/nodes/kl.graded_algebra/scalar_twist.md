---
id: kl.algebra.scalar_twist
title: Twisting a scalar action by an automorphism
kind: definition
status: formalized
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.detail.coefficient_change
- kl.algebra.projective_presentations
lean:
  repository: openai-kl
  modules:
  - Frobenius
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.ReflectionPairTranslation.Twist
  - OAI.KLInvariance.ReflectionPairTranslation.Twist.equiv
  - OAI.KLInvariance.ReflectionPairTranslation.Twist.equivVal
  - OAI.KLInvariance.ReflectionPairTranslation.Twist.projective
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:2045
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.Twist
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:2063
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.Twist.equiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:2053
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.Twist.equivVal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1001
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.Twist.projective
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, coordinate sets, kernel maps and induction hypotheses
    explicit?
  verdict: Read the local definitions and supporting proof bodies; stated the scalar
    direction, degree convention, and finite-generation hypotheses explicitly.
tags:
- Kazhdan-Lusztig
- graded-algebra
---

# Twisting a scalar action by an automorphism

Let \(R\) be a commutative ring, let \(\tau:R\to R\) be a ring automorphism, and let \(Y\) be an \(R\)-module. The twisted module \({}^{\tau}Y\) has the same additive group as \(Y\), with scalar multiplication
\[
r\star y=\tau(r)y.
\]
The module laws follow from the ring-homomorphism laws. For example,
\[
r\star(s\star y)=\tau(r)\tau(s)y=\tau(rs)y=(rs)\star y.
\]

## The underlying identification and semilinearity

Write \(j:Y\to{}^\tau Y\) for the identity on underlying elements. Then
\[
j(ry)=\tau^{-1}(r)\star j(y).
\]
Indeed, the right-hand side is \(\tau(\tau^{-1}(r))y=ry\). Thus \(j\) is an invertible semilinear map for the automorphism \(\tau^{-1}\).

Conversely, the underlying-value map \({}^\tau Y\to Y\) satisfies \(r\star y\mapsto\tau(r)y\), so it is semilinear for \(\tau\). These two directions specify exactly how coefficients must be changed in a coordinate formula.

If \(b_i\) is a basis of \(Y\), the same vectors form a basis of \({}^\tau Y\). An old expansion \(y=\sum_i a_i b_i\) becomes
\[
y=\sum_i\tau^{-1}(a_i)\star b_i.
\]
This proves spanning, and applying \(\tau\) to a vanishing twisted coefficient combination proves independence.

## Projectivity under a scalar twist

A scalar twist also preserves projectivity. One way to expand the source's semilinear transport is to transport the lifting problem itself.

Let \(Y\) be projective, let \(q:E\to F\) be a surjective \(R\)-linear map, and let \(h:{}^\tau Y\to F\) be \(R\)-linear. Apply the inverse twist to the two targets. The underlying function \(h\) becomes an \(R\)-linear map
\[
h':Y\to{}^{\tau^{-1}}F,
\]
because
\(h(ry)=h(\tau^{-1}(r)\star y)=\tau^{-1}(r)h(y)\).
The same underlying \(q\) is a surjection
\({}^{\tau^{-1}}E\to{}^{\tau^{-1}}F\).

Projectivity of \(Y\) gives a lift \(\ell:Y\to{}^{\tau^{-1}}E\).
Its underlying function, viewed as \(\widetilde\ell:{}^\tau Y\to E\), is linear:
\[
\widetilde\ell(r\star y)
=\ell(\tau(r)y)
=\tau^{-1}(\tau(r))\ell(y)
=r\widetilde\ell(y).
\]
It satisfies \(q\widetilde\ell=h\), proving the projectivity of the twist.

## Reflection example

Let \(R=\mathbb R[\alpha]\), with \(\tau(\alpha)=-\alpha\). In the twisted copy of \(R\),
\[
\alpha\star1=-\alpha.
\]
Since \(\tau^{-1}=\tau\), the identity map on elements is semilinear for the same reflection.

The pair-lattice construction uses an ordinary first coordinate and a twisted second coordinate. Scalar multiplication on a pair is
\[
r\cdot(x,y)=(rx,\tau(r)y).
\]
This is the scalar action that must preserve the relation defining the two-stalk image.

When \(R\) is a \(k\)-algebra and \(\tau\) fixes its base-field scalars, it is a \(k\)-algebra automorphism. In that setting the twist is coefficient transport with \(e=\tau^{-1}\), since the transported action uses \(e^{-1}=\tau\).

If \(\tau\) preserves the coefficient grading, the same homogeneous pieces grade the twist: for \(r\in R_i\) and \(y\in Y_j\), \(\tau(r)y\in Y_{i+j}\).

The [[node:kl.word.twisted_pair_lattice|twisted pair-lattice definition]] states the divisibility and lifting hypotheses that make the two-coordinate relation closed under this action. Its explicit correction vector supplies the closure calculation.

## References

The local source declarations below define the constructions and prove the stated properties.

## Lean formalization

The field `val` is the underlying element; the new scalar action is composed with the ring automorphism.

`OAI.KLInvariance.ReflectionPairTranslation.Twist`: [Frobenius.lean:2045](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2045).

`OAI.KLInvariance.ReflectionPairTranslation.Twist.equiv`: [Frobenius.lean:2063](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2063).

`OAI.KLInvariance.ReflectionPairTranslation.Twist.equivVal`: [Frobenius.lean:2053](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2053).

`OAI.KLInvariance.ReflectionPairTranslation.Twist.projective`: [IntegralPairings.lean:1001](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1001).
