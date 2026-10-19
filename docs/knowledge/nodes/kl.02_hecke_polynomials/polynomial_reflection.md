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
  - CanonicalKL
  - Hecke
  - OrdinaryR
  declarations:
  - OAI.KLInvariance.eval₂_reflect_unit
  - OAI.KLInvariance.reflect_finset_sum
  - OAI.KLInvariance.CanonicalP.lowPart_solution
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
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:43
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.lowPart_solution
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the exact domain, degree conventions and source
    argument?
  verdict: Read the coefficient cases in lowPart_solution, including revAt above the
    chosen degree. Extended the earlier bounded definition to the actual full operation
    and retained bounds on reciprocal evaluation and products.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Polynomial reflection in a fixed degree

Let \(d\in\mathbb N\) and \(p(q)=\sum_{i\ge0}c_iq^i\in\mathbb Z[q]\), with only finitely many nonzero coefficients. Polynomial reflection in degree \(d\) reverses the coefficient positions from zero through \(d\) and fixes the positions above \(d\):
\[
\operatorname{reflect}_dp
=\sum_{i=0}^d c_iq^{d-i}+\sum_{i>d}c_iq^i.
\]
Equivalently its coefficient at \(n\) is
\[
(\operatorname{reflect}_dp)_n=
\begin{cases}
c_{d-n},&n\le d,\\
c_n,&n>d.
\end{cases}
\]
These are the two coefficient cases used in Lean's lower-half solution proof.

For example,
\[
\operatorname{reflect}_2(2+3q)=3q+2q^2,
\]
\[
\operatorname{reflect}_2(2+3q+5q^3)=3q+2q^2+5q^3.
\]
The number \(d\) is part of the operation.

## The bounded reciprocal formula

If \(\operatorname{natDegree}(p)\le d\), the second sum is zero. At any invertible parameter \(q_0\) in a commutative coefficient ring,
\[
(\operatorname{reflect}_dp)(q_0)=q_0^dp(q_0^{-1}).
\]
The coefficient map from \(\mathbb Z\) is understood. A term \(c_iq_0^dq_0^{-i}\) equals \(c_iq_0^{d-i}\), so summing proves the equality.

Lean uses \(\operatorname{natDegree}(0)=0\). A bound by \(d\ge0\) thus includes the zero polynomial and every nonzero polynomial supported in degrees at most \(d\).

## Linearity and involutivity

Reflection permutes coefficient positions. It therefore preserves sums, differences and scalar multiples. Applying it twice sends \(i\le d\) to \(d-i\) and back to \(i\), while positions \(i>d\) are fixed both times. Hence
\[
\operatorname{reflect}_d(\operatorname{reflect}_dp)=p.
\]

If \(\deg p\le a\) and \(\deg r\le b\), then
\[
\operatorname{reflect}_{a+b}(pr)
=(\operatorname{reflect}_ap)(\operatorname{reflect}_br).
\]
Indeed, a product monomial in degree \(i+j\) moves to
\(a+b-i-j=(a-i)+(b-j)\). Summing the coefficient products proves the identity. These degree hypotheses are the ones checked before reflecting a product in the KL recursion.

## Reciprocal and anti-reciprocal polynomials

A polynomial is reciprocal in degree \(d\) if \(\operatorname{reflect}_dp=p\), and anti-reciprocal in degree \(d\) if \(\operatorname{reflect}_dp=-p\).

For an anti-reciprocal integral polynomial, every coefficient above \(d\) satisfies \(c_i=-c_i\), so \(2c_i=0\) and \(c_i=0\). Its degree is therefore at most \(d\). Within the range, \(c_{d-i}=-c_i\). When \(d=2m\), the middle coefficient also vanishes, since \(c_m=-c_m\).

For instance \(q^3+2q^2-2q-1\) is anti-reciprocal in degree three. Its low coefficients determine the high coefficients by the displayed sign relation.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.eval₂_reflect_unit`: [Hecke.lean:1101](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L1101).

`OAI.KLInvariance.reflect_finset_sum`: [OrdinaryR.lean:236](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L236).

`OAI.KLInvariance.CanonicalP.lowPart_solution`: [CanonicalKL.lean:43](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L43).
