---
id: kl.word.reflection_trace
title: The reflection trace and its normalization
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.reflection_coordinates
lean:
  repository: openai-kl
  modules:
  - Decomposition
  declarations:
  - OAI.KLInvariance.ReflectionFrobenius.trace
  - OAI.KLInvariance.ReflectionFrobenius.trace_expand
  - OAI.KLInvariance.ReflectionFrobenius.square_fixed
  - OAI.KLInvariance.ReflectionFrobenius.trace_mul
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1517
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.trace
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1520
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.trace_expand
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1527
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.square_fixed
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1530
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.trace_mul
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Checked the second-coordinate definition, trace_expand and trace_mul. Explained
    the exact normalization t(alpha)=1 and the divided-difference notation through
    the integral coordinate construction.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# The reflection trace and its normalization

Assume the reflection data over a characteristic-zero field and commutative domain that give
\[
A=R\oplus\alpha R,\qquad R=A^\tau.
\]
The reflection trace extracts the second invariant coordinate:
\[
t:A\to R,\qquad t(a_0+\alpha a_1)=a_1.
\]
It is \(R\)-linear because the reflection coordinate map is \(R\)-linear. This is the source's `trace`, the second projection after `coordinates`.

Its normalization is
\[
t(1)=0,\qquad t(\alpha)=1,\qquad t(\alpha^2)=0.
\]
For the last identity, \(\tau(\alpha^2)=(-\alpha)^2=\alpha^2\), so \(\alpha^2\in R\) has coordinates \((\alpha^2,0)\). More generally,
\[
t(r)=0,\qquad t(\alpha r)=r\qquad(r\in R).
\]

## The trace of a product

Write \(a=a_0+\alpha a_1\) and \(b=b_0+\alpha b_1\), with coefficients in \(R\). Multiplication gives
\[
ab=(a_0b_0+\alpha^2a_1b_1)
   +\alpha(a_0b_1+a_1b_0).
\]
Both parenthesized coefficients are invariant, since \(\alpha^2\in R\). Uniqueness of coordinates gives
\[
t(ab)=a_0b_1+a_1b_0.
\]
This is the formula used to prove the trace pairing perfect.

## Computing the trace from the reflection

Subtracting the reflected coordinate expression gives
\[
a-\tau(a)=2\alpha a_1=2\alpha t(a).
\]
One may write \(t(a)=(a-\tau(a))/(2\alpha)\): the division denotes the unique element obtained from the divisibility hypothesis and cancellation. Its value lies in \(R\).

For example, in \(A=k[X]\) with \(\alpha=X\),
\[
t(3+2X+5X^2+7X^3)=2+7X^2.
\]
The constants and even powers form the first coordinate; the remaining odd polynomial is \(X(2+7X^2)\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ReflectionFrobenius.trace`: [Decomposition.lean:1517](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1517).

`OAI.KLInvariance.ReflectionFrobenius.trace_expand`: [Decomposition.lean:1520](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1520).

`OAI.KLInvariance.ReflectionFrobenius.square_fixed`: [Decomposition.lean:1527](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1527).

`OAI.KLInvariance.ReflectionFrobenius.trace_mul`: [Decomposition.lean:1530](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1530).
