---
id: kl.hecke.scaled_polynomials
title: Scaled polynomial evaluations and KL vectors
kind: definition
status: formalized
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.hecke.selected_families
- kl.foundations.interval
lean:
  repository: openai-kl
  modules:
  - Dihedral
  - SimultaneousInvariance
  declarations:
  - OAI.KLInvariance.Comparison.scaledPolynomial
  - OAI.KLInvariance.scaledKL
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SimultaneousInvariance:325
    format: lean-location
    note: OAI.KLInvariance.Comparison.scaledPolynomial
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:730
    format: lean-location
    note: OAI.KLInvariance.scaledKL
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the exact domain, degree conventions and source
    argument?
  verdict: Read scaledPolynomial and scaledKL. Distinguished the real general-polynomial
    interface from the field-valued KL interface, retained the integer exponent, and
    expanded coefficient exponents and linearity.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Scaled polynomial evaluations and KL vectors

For an integral polynomial \(p\), a natural number \(d\), and a real parameter \(t\), define
\[
S_d(p;t)=t^{-d}p(t^2).
\]
Integer coefficients are evaluated in \(\mathbb R\). This is Comparison.scaledPolynomial in the source.

For a Coxeter system and a parameter \(t\) in any field \(C\), the source also defines
\[
p_{x,b}(t)
=t^{\ell(x)-\ell(b)}P_{x,b}(t^2),
\]
using the selected canonical KL polynomial. This is scaledKL. Its exponent is the integer difference of lengths.

The source formulas use field integer powers at every \(t\); their reciprocal identities assume \(t\ne0\). For \(x\le b\) and real \(t\ne0\), the two definitions agree with \(d=d(x,b)\).

## The exponent of each coefficient

If \(p(q)=\sum_i a_iq^i\) and \(t\ne0\), then
\[
S_d(p;t)=\sum_i a_i t^{2i-d}.
\]
Thus twice the polynomial degree appears in the exponent. The strict bound \(2\,\operatorname{natDegree}(p)<d\) puts every nonzero term at a negative exponent.

Under parameter inversion,
\[
S_d(p;t^{-1})=t^dp(t^{-2})
=\sum_i a_i t^{d-2i}.
\]
It reverses the signs of the exponents.

For \(p=1+2q\) and \(d=3\),
\[
S_3(p;t)=t^{-3}+2t^{-1},\qquad
S_3(p;t^{-1})=t^3+2t.
\]
For the rank-one KL value \(P_{1,s}=1\), the scaled value is \(t^{-1}\), while the top value \(p_{s,s}\) is one.

## Linearity at a fixed rank

For fixed \(d,t\), evaluation and multiplication by \(t^{-d}\) preserve sums and differences:
\[
S_d(p-p';t)=S_d(p;t)-S_d(p';t).
\]
The [[node:kl.hecke.scaled_difference_rigidity|reciprocal-difference rigidity theorem]] uses this identity to pass from equality of two scaled differences to equality of their underlying integral polynomials.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Comparison.scaledPolynomial`: [SimultaneousInvariance.lean:325](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SimultaneousInvariance.lean#L325).

`OAI.KLInvariance.scaledKL`: [Dihedral.lean:730](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L730).
