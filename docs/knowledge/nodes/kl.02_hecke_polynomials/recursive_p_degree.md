---
id: kl.hecke.recursive_p_degree
title: Degree bounds for the recursively constructed family
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.hecke.recursive_p
- kl.hecke.low_part_properties
- kl.foundations.bruhat_order
lean:
  repository: openai-kl
  modules:
  - CanonicalKL
  declarations:
  - OAI.KLInvariance.CanonicalP.polynomial_diagonal
  - OAI.KLInvariance.CanonicalP.polynomial_zero
  - OAI.KLInvariance.CanonicalP.polynomial_strict_degree
  - OAI.KLInvariance.CanonicalP.polynomial_degree
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:86
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.polynomial_diagonal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:91
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.polynomial_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:104
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.polynomial_strict_degree
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:113
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.polynomial_degree
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the exact domain, degree conventions and source
    argument?
  verdict: Read polynomial_strict_degree and polynomial_degree. The bound is obtained
    before reciprocity; included positive rank, the zero natural degree and all three
    endpoint cases.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Degree bounds for the recursively constructed family

The recursive family satisfies
\[
P_{x,x}=1,\qquad P_{x,y}=0\quad(x\not\le y),
\]
and, for \(x<y\),
\[
2\,\operatorname{natDegree}(P_{x,y})<d(x,y).
\]
For every pair, with the source's natural rank difference
\(\delta(x,y)=\max\{\ell(y)-\ell(x),0\}\),
\[
\operatorname{natDegree}(P_{x,y})\le\delta(x,y).
\]

*Proof.*

### Step 1. Read the two initial branches

For \(x=y\), Bruhat reflexivity selects the diagonal branch of the definition, giving one.

For \(x\not\le y\), the first branch gives zero. These values have natural degree zero.

### Step 2. Establish positive rank for a strict interval

If \(x<y\), strict Bruhat comparison gives \(\ell(x)<\ell(y)\). Hence \(d=d(x,y)>0\).

The recursive branch has the form
\(P_{x,y}=-\operatorname{low}_dD_{x,y}\).
The [[node:kl.hecke.low_part_properties|lower-half degree theorem]] applies because \(d>0\), and negation preserves natural degree. Therefore
\[
2\,\operatorname{natDegree}(P_{x,y})
=2\,\operatorname{natDegree}(\operatorname{low}_dD_{x,y})<d.
\]

### Step 3. Deduce the weak bound for all pairs

On a strict comparable pair, the strict inequality implies
\(\operatorname{natDegree}(P_{x,y})\le d(x,y)\).

On the diagonal, the natural degree and rank difference are both zero. When \(x\not\le y\), the polynomial is zero, and \(0\le\delta(x,y)\). These cases prove the all-pair weak bound.

The weak bound supplies the degree hypothesis when a later proof reflects a product \(R_{x,z}P_{z,y}\). The strict bound supplies uniqueness.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.CanonicalP.polynomial_diagonal`: [CanonicalKL.lean:86](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L86).

`OAI.KLInvariance.CanonicalP.polynomial_zero`: [CanonicalKL.lean:91](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L91).

`OAI.KLInvariance.CanonicalP.polynomial_strict_degree`: [CanonicalKL.lean:104](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L104).

`OAI.KLInvariance.CanonicalP.polynomial_degree`: [CanonicalKL.lean:113](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L113).
