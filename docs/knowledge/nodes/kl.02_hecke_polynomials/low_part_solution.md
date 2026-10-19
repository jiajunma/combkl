---
id: kl.hecke.low_part_solution
title: Solving an anti-reciprocal defect by its lower half
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.hecke.polynomial_reflection
- kl.foundations.low_half
- kl.hecke.low_part_properties
lean:
  repository: openai-kl
  modules:
  - CanonicalKL
  declarations:
  - OAI.KLInvariance.CanonicalP.lowPart_solution
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:43
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.lowPart_solution
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the exact domain, degree conventions and source
    argument?
  verdict: Read the four coefficient cases of lowPart_solution. The proof retains
    its unrestricted d and derives high-degree vanishing from integer anti-reciprocity
    rather than assuming a degree bound.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Solving an anti-reciprocal defect by its lower half

Let \(D\in\mathbb Z[q]\) and \(d\in\mathbb N\) satisfy
\(\operatorname{reflect}_dD=-D\).
Then
\[
P=-\operatorname{low}_dD
\quad\text{satisfies}\quad
\operatorname{reflect}_dP=P+D.
\]
If \(d>0\), it also satisfies \(2\,\operatorname{natDegree}(P)<d\).

*Proof.*

### Step 1. Write the coefficient relations, including high degrees

Let \(a_n=D_n\). Anti-reciprocity gives
\[
a_{d-n}=-a_n\quad(0\le n\le d),\qquad
a_n=-a_n\quad(n>d).
\]
Because the coefficients are integers, the second relation implies \(a_n=0\) for \(n>d\).

If \(2n=d\), the first relation becomes \(a_n=-a_n\), so the middle coefficient is zero as well.

### Step 2. Compare coefficients below the midpoint

Suppose \(2n<d\). The coefficient of \(P\) at \(n\) is \(-a_n\). The reflected position \(d-n\) lies above the midpoint, so \(P_{d-n}=0\).

Hence the coefficient of \(\operatorname{reflect}_dP\) at \(n\) is zero, and the coefficient of \(P+D\) is \(-a_n+a_n=0\).

### Step 3. Compare the middle and upper coefficients

At \(2n=d\), the truncation excludes the middle degree and \(a_n=0\) by Step 1. Both sides therefore have coefficient zero.

For \(n\le d\) with \(2n>d\), the coefficient \(P_n\) is zero, while \(d-n\) is strictly below the midpoint. Thus
\[
(\operatorname{reflect}_dP)_n=P_{d-n}=-a_{d-n}=a_n=(P+D)_n.
\]

### Step 4. Compare coefficients beyond d

For \(n>d\), the truncation gives \(P_n=0\), and reflection fixes that position. Step 1 gives \(D_n=0\), so both sides again have coefficient zero.

The four cases exhaust every coefficient index. Equality of coefficients proves the polynomial equation.

### Step 5. Read off the strict degree bound

For \(d>0\), the [[node:kl.hecke.low_part_properties|lower-half bound]] gives
\(2\,\operatorname{natDegree}(\operatorname{low}_dD)<d\).
Negation preserves natural degree, proving the assertion for \(P\).

The equation itself includes \(d=0\): anti-reciprocity then forces every coefficient of \(D\) to vanish, and the empty lower half gives \(P=0\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.CanonicalP.lowPart_solution`: [CanonicalKL.lean:43](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L43).
