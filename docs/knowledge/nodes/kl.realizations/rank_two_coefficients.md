---
id: kl.realization.rank_two_coefficients
title: Chebyshev coefficients for rank-two root calculations
kind: definition
status: formalized
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.realization.tits_form
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.rootCoeff
  - OAI.KLInvariance.TitsSpace.rootCoeff_zero
  - OAI.KLInvariance.TitsSpace.rootCoeff_neg_one
  - OAI.KLInvariance.TitsSpace.rootCoeff_succ
  - OAI.KLInvariance.TitsSpace.rootCoeff_nonneg
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:813
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.rootCoeff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:817
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.rootCoeff_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:821
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.rootCoeff_neg_one
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:826
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.rootCoeff_succ
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:867
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.rootCoeff_nonneg
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the calculation preserve the local statement and proof route?
  verdict: Checked the general linear-functional hypotheses, even/odd Chebyshev vanishings,
    rank-one normal form, and arbitrary-rank coordinate action.
tags:
- Kazhdan-Lusztig
- realization
---

# Chebyshev coefficients for rank-two root calculations

Define polynomials \(S_n(z)\), indexed by integers, by
\[
S_{-1}(z)=0,\qquad S_0(z)=1,\qquad
S_{n+1}(z)=zS_n(z)-S_{n-1}(z).
\]
The recurrence determines all indices: it can also be solved for \(S_{n-1}\). For example,
\[
S_1=z,\quad S_2=z^2-1,\quad S_3=z^3-2z,\quad S_{-2}=-1.
\]
This fixes the normalization of the Chebyshev polynomials used in the root calculations.

## Trigonometric evaluation

For a real angle \(\theta\) with \(\sin\theta\ne0\),
\[
S_n(2\cos\theta)=\frac{\sin((n+1)\theta)}{\sin\theta}.
\]
The right side has values zero and one at indices \(-1\) and zero. The addition formulas for sine give
\[
\sin((n+2)\theta)
=2\cos\theta\sin((n+1)\theta)-\sin(n\theta).
\]
Thus these values satisfy the same recurrence, in both directions, which proves the formula.

At \(z=2\), the values are \(S_n(2)=n+1\). The sequence \(n+1\) has the required initial values and satisfies \(n+2=2(n+1)-n\), so the recurrence again proves the assertion.

## Coefficients for a Coxeter pair

For simple generators \(s_i,s_j\), define
\[
c_n(i,j)=S_n\!\left(2\cos\frac{\pi}{m_{ij}}\right).
\]
For an infinite exponent the argument is two, so \(c_n(i,j)=n+1\).

For distinct generators with finite exponent \(m=m_{ij}\ge2\), put \(\theta=\pi/m\). Then
\[
c_n(i,j)=\frac{\sin((n+1)\theta)}{\sin\theta}.
\]
If \(-1\le n\) and \(n+1\le m\), the numerator has angle in \([0,\pi]\) and is nonnegative; the denominator is positive. Hence \(c_n(i,j)\ge0\) in this range.

For \(m=3\), the argument is one and the first values are
\[
c_{-1}=0,\qquad c_0=1,\qquad c_1=1,\qquad c_2=0.
\]
For an infinite exponent they are \(0,1,2,3,\ldots\).

The alternating-root formula uses these coefficients for the two simple-root coordinates. The finite reflection-relation proof uses the same polynomials at the angle \(2\pi/m\), where their vanishing gives the required powers of the two-reflection operator.

## References

The local source statements and calculations are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.rootCoeff`: [Tits.lean:813](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L813).

`OAI.KLInvariance.TitsSpace.rootCoeff_zero`: [Tits.lean:817](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L817).

`OAI.KLInvariance.TitsSpace.rootCoeff_neg_one`: [Tits.lean:821](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L821).

`OAI.KLInvariance.TitsSpace.rootCoeff_succ`: [Tits.lean:826](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L826).

`OAI.KLInvariance.TitsSpace.rootCoeff_nonneg`: [Tits.lean:867](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L867).
