---
id: kl.hecke.polynomial_reflection
title: Polynomial reflection in a fixed degree
kind: definition
status: formalized
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses: []
lean:
  repository: openai-kl
  modules:
  - Hecke
  - OrdinaryR
  declarations:
  - OAI.KLInvariance.eval₂_reflect_unit
  - OAI.KLInvariance.reflect_finset_sum
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:1101
    format: lean-location
    note: OAI.KLInvariance.eval₂_reflect_unit
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.OrdinaryR:236
    format: lean-location
    note: OAI.KLInvariance.reflect_finset_sum
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Is the bounded-degree domain used by the local source explicit?
  verdict: Explains reflection on polynomials of degree at most d, the domain of the
    reciprocal evaluation identity used locally.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Polynomial reflection in a fixed degree

Let \(d\ge0\), and let \(p(q)\) be a polynomial of degree at most \(d\), written with zero coefficients added as needed:
\[
p(q)=\sum_{i=0}^d c_iq^i.
\]
Its reflection in degree \(d\) is
\[
\operatorname{reflect}_d p=\sum_{i=0}^d c_iq^{d-i}.
\]
The coefficient in degree \(i\) moves to degree \(d-i\). The number \(d\) specifies the reflection and can exceed the degree of \(p\).

For example,
\[
\operatorname{reflect}_1(2+3q)=3+2q,\qquad
\operatorname{reflect}_2(2+3q)=3q+2q^2.
\]
In particular \(\operatorname{reflect}_d1=q^d\) and \(\operatorname{reflect}_d0=0\).

## Reciprocal evaluation

At an invertible parameter \(q_0\) in a commutative ring,
\[
(\operatorname{reflect}_d p)(q_0)
=q_0^d p(q_0^{-1}).
\]
Each summand on the right is \(c_iq_0^d q_0^{-i}=c_iq_0^{d-i}\), giving the equality term by term. The degree bound makes \(d-i\) nonnegative for every nonzero coefficient. The local theorem states this after mapping integer coefficients into the target ring.

## Linearity and a second reflection

If \(p,r\) have degree at most \(d\), coefficient addition gives
\[
\operatorname{reflect}_d(p+r)
=\operatorname{reflect}_dp+\operatorname{reflect}_dr.
\]
The same argument gives scalar compatibility and reflection of a finite sum.

Reflecting twice moves \(i\) to \(d-i\), then to \(d-(d-i)=i\). Hence
\[
\operatorname{reflect}_d(\operatorname{reflect}_dp)=p.
\]

## Products and added bounds

If \(\deg p\le a\) and \(\deg r\le b\), write
\(p=\sum_i c_iq^i\), \(r=\sum_j d_jq^j\). Each product monomial satisfies
\[
q^{a+b-(i+j)}=q^{a-i}q^{b-j}.
\]
Multiplying and summing the coefficients gives
\[
\operatorname{reflect}_{a+b}(pr)
=(\operatorname{reflect}_ap)(\operatorname{reflect}_br).
\]
The R-kernel proof uses this with \(a=d(x,z)\), \(b=d(z,y)\). The additivity of Bruhat interval rank makes \(a+b=d(x,y)\).

## The zero-polynomial degree convention

Lean uses natural degree, with \(\operatorname{natDegree}(0)=0\). A bound \(\operatorname{natDegree}(p)\le d\) therefore includes the zero polynomial as well as every nonzero polynomial supported in degrees at most \(d\). All formulas above apply to that bounded domain.

## References

The local source uses the bounded reflection operation through the following identities.

## Lean formalization

`OAI.KLInvariance.eval₂_reflect_unit`: [Hecke.lean:1101](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L1101).

`OAI.KLInvariance.reflect_finset_sum`: [OrdinaryR.lean:236](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L236).
