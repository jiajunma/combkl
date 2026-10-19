---
id: kl.hecke.recursive_p
title: The recursive polynomial family on Bruhat intervals
kind: definition
status: formalized
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.detail.ordinary_r
- kl.foundations.low_half
- kl.foundations.finite_intervals
- kl.foundations.interval
lean:
  repository: openai-kl
  modules:
  - CanonicalKL
  declarations:
  - OAI.KLInvariance.CanonicalP.polynomial
  - OAI.KLInvariance.CanonicalP.polynomial_diagonal
  - OAI.KLInvariance.CanonicalP.polynomial_zero
  - OAI.KLInvariance.CanonicalP.polynomial_recursion
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:70
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.polynomial
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:86
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.polynomial_diagonal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:91
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.polynomial_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:98
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.polynomial_recursion
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the exact domain, degree conventions and source
    argument?
  verdict: Read polynomial and its termination proof. Explained all branches, attached
    finite-index evidence, strict rank decrease, the negative lower-half choice and
    explicit first-rank computations.
tags:
- Kazhdan-Lusztig
- Hecke
---

# The recursive polynomial family on Bruhat intervals

Fix a Coxeter system, and let \(R_{x,y}\) be its constructed ordinary R-polynomials. Define \(P_{x,y}\in\mathbb Z[q]\) for every pair \(x,y\) by
\[
P_{x,y}=
\begin{cases}
0,&x\not\le y,\\
1,&x=y,\\
-\operatorname{low}_{d(x,y)}
 \displaystyle\sum_{x<z\le y}R_{x,z}P_{z,y},&x<y,
\end{cases}
\qquad d(x,y)=\ell(y)-\ell(x).
\]
This is the source's CanonicalP.polynomial. The word “recursive” refers to the smaller intervals \([z,y]\) used in the third branch.

## The recursive calls have smaller rank

If \(x<z\le y\), strict Bruhat comparison gives \(\ell(x)<\ell(z)\), while \(\ell(z)\le\ell(y)\). Consequently
\[
d(z,y)=\ell(y)-\ell(z)
<\ell(y)-\ell(x)=d(x,y).
\]
Thus every recursive call has a strictly smaller natural-number rank difference. The sum is finite because \([x,y]\) is finite.

The source uses the finite set of \(z\) satisfying \(x<z\le y\), together with the membership evidence needed for its termination check. The resulting polynomial is exactly the displayed finite sum and truncation.

## The sign chosen by the lower coefficients

The desired equation is
\[
\operatorname{reflect}_dP_{x,y}
=P_{x,y}+\sum_{x<z\le y}R_{x,z}P_{z,y}.
\]
A polynomial strictly below degree \(d/2\) contributes nothing to the lower half after reflection. Its lower coefficients must therefore be the negatives of those in the sum. This is the minus sign in the definition.

The [[node:kl.hecke.recursive_p_degree|strict degree theorem]] follows directly from the truncation. The [[node:kl.detail.kl_recursion|reciprocity theorem]] proves that the high coefficients also satisfy the equation, using the R-kernel identity.

## The first two ranks

On \([1,s]\), only \(z=s\) occurs in the sum. Thus
\[
D_{1,s}=R_{1,s}P_{s,s}=q-1,\qquad
P_{1,s}=-\operatorname{low}_1(q-1)=1.
\]

For distinct simple reflections \(s,t\), the interval \([1,st]\) has vertices \(1,s,t,st\), by [[node:kl.foundations.subword|the reduced-subword criterion]] applied to its two-letter expression. The ordinary R recurrence gives
\[
R_{s,st}=R_{1,t}=q-1,\qquad
R_{t,st}=(q-1)R_{t,t}+qR_{st,t}=q-1.
\]
The last R-value is zero by length and support. Each of these upper intervals has rank one, so applying its negative lower-half construction gives \(P_{s,st}=P_{t,st}=1\). Therefore
\[
D_{1,st}=(q-1)+(q-1)+(q-1)^2=q^2-1,
\]
and
\[
P_{1,st}=-\operatorname{low}_2(q^2-1)=1.
\]
The reciprocal identity in this example is \(q^2=1+(q^2-1)\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.CanonicalP.polynomial`: [CanonicalKL.lean:70](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L70).

`OAI.KLInvariance.CanonicalP.polynomial_diagonal`: [CanonicalKL.lean:86](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L86).

`OAI.KLInvariance.CanonicalP.polynomial_zero`: [CanonicalKL.lean:91](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L91).

`OAI.KLInvariance.CanonicalP.polynomial_recursion`: [CanonicalKL.lean:98](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L98).
