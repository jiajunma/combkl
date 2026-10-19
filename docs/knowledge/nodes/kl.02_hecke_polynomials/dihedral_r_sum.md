---
id: kl.hecke.dihedral_r_sum
title: The dihedral interval sum of ordinary R-polynomials
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.hecke.dihedral_bar_sum
- kl.hecke.r_parameter_reciprocity
- kl.hecke.ordinary_r_construction
- kl.hecke.lower_interval_sums
lean:
  repository: openai-kl
  modules:
  - Dihedral
  declarations:
  - OAI.KLInvariance.Dihedral.rValue_sum
  - OAI.KLInvariance.Dihedral.rPolynomial_sum
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:576
    format: lean-location
    note: OAI.KLInvariance.Dihedral.rValue_sum
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:605
    format: lean-location
    note: OAI.KLInvariance.Dihedral.rPolynomial_sum
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the reduced-word, coefficient and interval
    hypotheses?
  verdict: Read rValue_sum and rPolynomial_sum. Expanded the inverse-parameter coefficient
    extraction, bottom-power factor, comparable-length cancellation and injective
    return from Laurent coefficients.
tags:
- Kazhdan-Lusztig
- dihedral
---

# The dihedral interval sum of ordinary R-polynomials

In a rank-two Coxeter system, for every \(x\le y\) and every unit \(q\),
\[
\sum_{z\le y}r_q(x,z)=q^{d(x,y)}.
\]
For the integral ordinary R-polynomials,
\[
\sum_{x\le z\le y}R_{x,z}(q)=q^{d(x,y)}.
\]

*Proof.*

### Step 1. Take a coefficient of the inverse-parameter bar sum

Apply the [[node:kl.hecke.dihedral_bar_sum|bar-sum theorem]] at \(q^{-1}\):
\[
B_{q^{-1}}S_y=q^{\ell(y)}S_y.
\]
Since \(x\le y\), the \(x\)-coefficient of \(S_y\) is one.

Expand \(S_y=\sum_{z\le y}T_z\). Linearity and the definition of bar-basis vectors give
\[
\sum_{z\le y}b_z(q^{-1})(x)=q^{\ell(y)}.
\]

### Step 2. Insert the R-value coefficient identity

The [[node:kl.hecke.r_parameter_reciprocity|inverse-parameter coefficient theorem]] gives
\[
r_q(x,z)=q^{-\ell(x)}b_z(q^{-1})(x).
\]
Multiplying Step 1 by the common factor \(q^{-\ell(x)}\) yields
\[
\sum_{z\le y}r_q(x,z)
=q^{-\ell(x)}q^{\ell(y)}.
\]

### Step 3. Reduce the exponent to the interval rank

Comparison \(x\le y\) gives
\(\ell(y)=\ell(x)+d(x,y)\).
Thus
\[
q^{-\ell(x)}q^{\ell(y)}
=q^{-\ell(x)}q^{\ell(x)}q^{d(x,y)}
=q^{d(x,y)}.
\]
This proves the ring-valued identity.

### Step 4. Recover the integral polynomial identity

Take \(q=Q\), the Laurent indeterminate. Each \(r_Q(x,z)\) is the Laurent image of \(R_{x,z}\), by the ordinary R construction.

The inclusion of integral polynomials into Laurent polynomials preserves this finite sum and the power \(q^{d(x,y)}\). Its injectivity therefore gives
\[
\sum_{z\le y}R_{x,z}(q)=q^{d(x,y)}
\]
as an equality of integral polynomials.

Terms with \(x\not\le z\) have \(R_{x,z}=0\). Removing them restricts the sum to \([x,y]\).

### Step 5. Compute the two-letter example

For \(x=1,y=st\), the interval elements are \(1,s,t,st\), with R-values
\(1,q-1,q-1,(q-1)^2\). Their sum is
\[
1+2(q-1)+(q-1)^2=q^2,
\]
equal to the power predicted by the rank \(d(1,st)=2\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.rValue_sum`: [Dihedral.lean:576](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L576).

`OAI.KLInvariance.Dihedral.rPolynomial_sum`: [Dihedral.lean:605](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L605).
