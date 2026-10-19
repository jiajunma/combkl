---
id: kl.hecke.bar_triangularity
title: Bruhat support and diagonal coefficients of the bar basis
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.definitions.bar_involution
- kl.hecke.bar_interchange
- kl.detail.bruhat_lifting
- kl.detail.simple_envelopes
lean:
  repository: openai-kl
  modules:
  - Hecke
  declarations:
  - OAI.KLInvariance.Hecke.leftInv_coeff
  - OAI.KLInvariance.Hecke.simple_mul_le_ascent
  - OAI.KLInvariance.Hecke.barBasis_zero
  - OAI.KLInvariance.Hecke.barBasis_diagonal
  - OAI.KLInvariance.HeckeQ.leftInv_coeff
  - OAI.KLInvariance.HeckeQ.barBasis_zero
  - OAI.KLInvariance.HeckeQ.barBasis_diagonal
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:424
    format: lean-location
    note: OAI.KLInvariance.Hecke.leftInv_coeff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:431
    format: lean-location
    note: OAI.KLInvariance.Hecke.simple_mul_le_ascent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:441
    format: lean-location
    note: OAI.KLInvariance.Hecke.barBasis_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:466
    format: lean-location
    note: OAI.KLInvariance.Hecke.barBasis_diagonal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:895
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.leftInv_coeff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:941
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.barBasis_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:966
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.barBasis_diagonal
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual coefficient hypotheses, conventions and source proof retained?
  verdict: Read both inverse-coefficient and triangularity proofs; included the upper-envelope
    implication for sx, the all-bottom induction and separate normalized/q diagonal
    calculations.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Bruhat support and diagonal coefficients of the bar basis

Write \(b_y(x)\) for the coefficient of \(e_x\) in \(b_y\). In both Hecke conventions,
\[
b_y(x)=0\qquad\text{if }x\not\le y.
\]
The diagonal values are
\[
b_y(a)(y)=1,\qquad b_y(q)(y)=q^{-\ell(y)}.
\]

*Proof.*

### Step 1. Extract coefficients of inverse operators

For \(f=\sum_w f(w)e_w\), only \(w=sx\) and \(w=x\) can contribute to the \(x\)-coefficient after applying a simple inverse.

In the normalized convention, its basis formula gives
\[
(L_s(a)^{-1}f)(x)=
\begin{cases}
f(sx),&sx<x,\\
f(sx)-af(x),&sx>x.
\end{cases}
\]
The coefficient of \(f(sx)\) is one in both cases. The subtraction of \(af(x)\) remains only when \(x\) is an ascent.

In the unnormalized convention, the inverse basis formula is
\[
L_s(q)^{-1}T_w=
\begin{cases}
T_{sw},&sw<w,\\
q^{-1}T_{sw}+(q^{-1}-1)T_w,&sw>w.
\end{cases}
\]
Substituting \(w=sx\) reverses the ascent/descent condition. Consequently
\[
(L_s(q)^{-1}f)(x)=
\begin{cases}
q^{-1}f(sx),&sx<x,\\
f(sx)+(q^{-1}-1)f(x),&sx>x.
\end{cases}
\]

### Step 2. Locate both possible source coefficients in Bruhat order

Let \(y=sv\) with \(v<sv\). If \(x\not\le y\), then \(x\not\le v\), since \(v\le y\).

Also \(sx\not\le v\). Indeed, if \(sx\le v\), monotonicity of the upper simple envelope would give
\[
U_s(sx)\le U_s(v)=sv=y.
\]
Since \(U_s(sx)=U_s(x)\) and \(x\le U_s(x)\), this would imply \(x\le y\), a contradiction.

Thus both \(x\) and \(sx\) lie outside the lower ideal of \(v\).

### Step 3. Prove triangular support by induction

Induct on a reduced word for \(y\), with the assertion for every \(x\). For \(y=1\), the vector is \(e_1\), so every coefficient outside \(x=1\) is zero.

For a reduced word \(s\omega\) with tail product \(v\), the ascent formula gives \(b_y=L_s^{-1}b_v\). If \(x\not\le y\), Step 2 and the induction hypothesis give
\[
b_v(x)=b_v(sx)=0.
\]
Every branch in Step 1 is therefore zero. This proves support in \(\{x:x\le y\}\).

### Step 4. Compute the normalized diagonal

Use the same reduced-tail induction. At \(y=1\), the diagonal coefficient is one.

At \(y=sv\), we have \(sy=v<y\). The normalized coefficient formula in Step 1 therefore gives
\[
b_y(a)(y)=b_v(a)(v)=1
\]
by induction.

### Step 5. Compute the unnormalized diagonal

Again the base value is one. At \(y=sv\), Step 1 gives
\[
b_y(q)(y)=q^{-1}b_v(q)(v).
\]
Induction makes this \(q^{-1}q^{-\ell(v)}=q^{-\ell(y)}\), because \(\ell(y)=\ell(v)+1\).

For the two-element lower interval, the full vector is
\(b_s(q)=q^{-1}T_s+(q^{-1}-1)T_1\): its support and diagonal exhibit both assertions directly.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Hecke.leftInv_coeff`: [Hecke.lean:424](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L424).

`OAI.KLInvariance.Hecke.simple_mul_le_ascent`: [Hecke.lean:431](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L431).

`OAI.KLInvariance.Hecke.barBasis_zero`: [Hecke.lean:441](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L441).

`OAI.KLInvariance.Hecke.barBasis_diagonal`: [Hecke.lean:466](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L466).

`OAI.KLInvariance.HeckeQ.leftInv_coeff`: [Hecke.lean:895](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L895).

`OAI.KLInvariance.HeckeQ.barBasis_zero`: [Hecke.lean:941](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L941).

`OAI.KLInvariance.HeckeQ.barBasis_diagonal`: [Hecke.lean:966](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L966).
