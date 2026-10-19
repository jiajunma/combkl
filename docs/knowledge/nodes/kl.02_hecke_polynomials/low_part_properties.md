---
id: kl.hecke.low_part_properties
title: Coefficients and the strict degree bound of the lower half
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.foundations.low_half
lean:
  repository: openai-kl
  modules:
  - CanonicalKL
  declarations:
  - OAI.KLInvariance.CanonicalP.coeff_lowPart
  - OAI.KLInvariance.CanonicalP.lowPart_degree
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:26
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.coeff_lowPart
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:34
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.lowPart_degree
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the exact domain, degree conventions and source
    argument?
  verdict: Read coeff_lowPart and lowPart_degree; expanded the finite coefficient
    extraction, both parity cases and the positive-d hypothesis with the natural degree
    convention.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Coefficients and the strict degree bound of the lower half

For every \(d,p,n\),
\[
(\operatorname{low}_dp)_n=
\begin{cases}
p_n,&2n<d,\\
0,&2n\ge d.
\end{cases}
\]
If \(d>0\), then
\[
2\,\operatorname{natDegree}(\operatorname{low}_dp)<d.
\]

*Proof.*

### Step 1. Extract the coefficient from the finite sum

In the defining sum, the summand indexed by \(i\) is the monomial \(p_iq^i\). Its coefficient at \(n\) is zero unless \(i=n\), in which case it is \(p_n\).

Thus the coefficient of the sum is \(p_n\) exactly when
\(n<\lfloor(d+1)/2\rfloor\), and zero otherwise.

### Step 2. Express the index condition by the midpoint

If \(d=2m\), the index condition is \(n<m\), equivalent to \(2n<2m\).

If \(d=2m+1\), it is \(n<m+1\), equivalent to \(n\le m\), hence to \(2n<2m+1\). This proves the coefficient formula.

### Step 3. Bound all possible nonzero exponents

Assume \(d>0\). Put \(r=\lfloor(d-1)/2\rfloor\). Every \(n>r\) satisfies \(2n\ge d\), so Step 2 makes its coefficient zero. Therefore
\[
\operatorname{natDegree}(\operatorname{low}_dp)\le r.
\]
This also holds for the zero result, whose natural degree is zero and for which \(r\ge0\).

Finally \(2r<d\): for \(d=2m\), \(r=m-1\); for \(d=2m+1\), \(r=m\). Hence
\(2\,\operatorname{natDegree}(\operatorname{low}_dp)\le2r<d\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.CanonicalP.coeff_lowPart`: [CanonicalKL.lean:26](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L26).

`OAI.KLInvariance.CanonicalP.lowPart_degree`: [CanonicalKL.lean:34](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L34).
