---
id: kl.hecke.bar_coefficient_inverse
title: Inverse bar coefficients and the R-value kernel identity
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.hecke.bar_interchange
- kl.hecke.bar_triangularity
- kl.hecke.r_values
- kl.foundations.finite_intervals
lean:
  repository: openai-kl
  modules:
  - Hecke
  declarations:
  - OAI.KLInvariance.HeckeQ.bar_coeff_inverse
  - OAI.KLInvariance.HeckeQ.rValue_inverse_factor
  - OAI.KLInvariance.HeckeQ.rValue_inverse
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:1055
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.bar_coeff_inverse
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:1069
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.rValue_inverse_factor
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:1085
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.rValue_inverse
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual coefficient hypotheses, conventions and source proof retained?
  verdict: Read bar_coeff_inverse, rValue_inverse_factor and rValue_inverse. Expanded
    the finite-support coefficient sum and cancelled signs and q-powers separately
    before evaluating the diagonal.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Inverse bar coefficients and the R-value kernel identity

For a unit \(q\) and every \(x,y\), the inverse bar transforms give
\[
\sum_{z\le y} b_z(q)(x)b_y(q^{-1})(z)=\delta_{x,y}.
\]
The sum is over the finite lower Bruhat ideal of \(y\). In terms of R-values, this becomes
\[
\sum_{z\le y}
r_q(x,z)\,q^{\ell(y)}q^{-\ell(z)}r_{q^{-1}}(z,y)
=\delta_{x,y}.
\]

*Proof.*

### Step 1. Expand the inverse transform on one basis vector

The [[node:kl.hecke.bar_interchange|inverse-transform theorem]] gives \(B_qb_y(q^{-1})=e_y\). Expand the argument in the standard basis:
\[
b_y(q^{-1})=\sum_{z\le y}b_y(q^{-1})(z)e_z.
\]
Triangularity gives its support, and finiteness of the lower ideal makes this a finite sum.

Apply the linear map \(B_q\) and extract the \(x\)-coefficient. This is exactly the first identity.

### Step 2. Substitute both R-value normalizations

For one summand, abbreviate \(m=\ell(x)\), \(n=\ell(z)\), \(p=\ell(y)\). The R-value product is
\[
\bigl((-1)^m(-q)^n b_z(q)(x)\bigr)
q^p q^{-n}
\bigl((-1)^n(-q^{-1})^p b_y(q^{-1})(z)\bigr).
\]
Its sign is \((-1)^{m+2n+p}=(-1)^{m+p}\). Its power of \(q\) is
\(q^n q^p q^{-n}q^{-p}=1\).
Thus the summand equals
\[
(-1)^{\ell(x)+\ell(y)}b_z(q)(x)b_y(q^{-1})(z).
\]
The remaining scalar is independent of \(z\).

### Step 3. Sum and evaluate the diagonal factor

Pull that common scalar out of the finite sum and apply Step 1. If \(x\ne y\), the result is zero. If \(x=y\), the sign is \((-1)^{2\ell(x)}=1\), so the result is one.

This proves the R-value identity. Terms with \(x\not\le z\) vanish by support, so for \(x\le y\) the sum can equivalently be restricted to the interval \([x,y]\).

### Step 4. Compute the rank-one cancellation

For \(x=1,y=s\), the two R-value terms are
\[
1\cdot q\cdot(q^{-1}-1)+(q-1)\cdot1=0.
\]
The two bar-coefficient terms are
\[
b_1(q)(1)b_s(q^{-1})(1)
+b_s(q)(1)b_s(q^{-1})(s)
=(q-1)+(q^{-1}-1)q=0.
\]
These are the same cancellation under the normalization in Step 2.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.HeckeQ.bar_coeff_inverse`: [Hecke.lean:1055](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L1055).

`OAI.KLInvariance.HeckeQ.rValue_inverse_factor`: [Hecke.lean:1069](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L1069).

`OAI.KLInvariance.HeckeQ.rValue_inverse`: [Hecke.lean:1085](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L1085).
