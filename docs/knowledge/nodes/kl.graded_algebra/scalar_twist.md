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
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.ReflectionPairTranslation.Twist
  - OAI.KLInvariance.ReflectionPairTranslation.Twist.equiv
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
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source assumptions and maps?
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

## Reflection example

Let \(R=k[\alpha]\), with \(\tau(\alpha)=-\alpha\). In the twisted copy of \(R\),
\[
\alpha\star1=-\alpha.
\]
Since \(\tau^{-1}=\tau\), the identity map on elements is semilinear for the same reflection.

The pair-lattice construction uses an ordinary first coordinate and a twisted second coordinate. Scalar multiplication on a pair is
\[
r\cdot(x,y)=(rx,\tau(r)y).
\]
This is the scalar action that must preserve the relation defining the two-stalk image.

Coefficient transport along an algebra isomorphism \(e:A\to B\) uses \(b\cdot m=e^{-1}(b)m\). The twist above is that construction with \(e=\tau^{-1}\).

## References

The local source declarations below define the constructions and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.ReflectionPairTranslation.Twist`: [Frobenius.lean:2045](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2045).

`OAI.KLInvariance.ReflectionPairTranslation.Twist.equiv`: [Frobenius.lean:2063](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2063).

The field `val` is the underlying element of the original module. Scalar multiplication on that element is composed with the automorphism.
