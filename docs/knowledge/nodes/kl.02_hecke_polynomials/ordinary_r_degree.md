---
id: kl.hecke.ordinary_r_degree
title: The length-difference bound for ordinary R-polynomials
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.hecke.ordinary_r_construction
- kl.foundations.bruhat_order
lean:
  repository: openai-kl
  modules:
  - OrdinaryR
  declarations:
  - OAI.KLInvariance.OrdinaryR.polynomial_degree
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.OrdinaryR:125
    format: lean-location
    note: OAI.KLInvariance.OrdinaryR.polynomial_degree
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual coefficient hypotheses, conventions and source proof retained?
  verdict: Read polynomial_degree. Preserved natural truncated length difference,
    the zero-polynomial convention, the two descent branches and the support case
    required before subtracting two from the rank.
tags:
- Kazhdan-Lusztig
- Hecke
---

# The length-difference bound for ordinary R-polynomials

For every \(x,y\),
\[
\operatorname{natDegree}R_{x,y}
\le\delta(x,y),\qquad
\delta(x,y)=\max\{\ell(y)-\ell(x),0\}.
\]
Here the difference in the maximum is an integer. Lean's natural-number subtraction gives this \(\delta\), and its \(\operatorname{natDegree}(0)\) is zero. For \(x\le y\), the bound is the ordinary length difference.

*Proof.*

### Step 1. Establish the zero and diagonal cases

Induct strongly on \(\ell(y)\), for all \(x\). If \(x\not\le y\), the polynomial is zero, whose natural degree is zero and hence at most \(\delta(x,y)\).

If \(x=y\), the polynomial is one and has degree zero, equal to \(\delta(x,x)\).

Now assume \(x<y\). Put \(d=\ell(y)-\ell(x)\), so \(d\ge1\).

### Step 2. Use a left descent of the upper endpoint

Since \(y\ne1\), choose \(s\) with \(sy<y\). Write \(v=sy\), so \(\ell(v)=\ell(y)-1\). All recurrence terms have the smaller upper endpoint \(v\).

If \(sx<x\), both endpoint lengths decrease by one. The recurrence is \(R_{x,y}=R_{sx,v}\), and
\[
\delta(sx,v)=\ell(v)-\ell(sx)=d.
\]
The induction hypothesis proves the bound.

### Step 3. Bound the first term in the ascent branch

Suppose \(sx>x\). The recurrence is
\[
R_{x,y}=(q-1)R_{x,v}+qR_{sx,v}.
\]
Since \(d\ge1\), we have \(\delta(x,v)=d-1\). By induction and the product degree inequality,
\[
\operatorname{natDegree}\bigl((q-1)R_{x,v}\bigr)
\le1+\operatorname{natDegree}R_{x,v}
\le1+(d-1)=d.
\]

### Step 4. Bound the second term, including its support case

If \(sx\not\le v\), then \(R_{sx,v}=0\), so this term has natural degree zero.

If \(sx\le v\), the length inequality gives
\[
\ell(x)+1=\ell(sx)\le\ell(v)=\ell(y)-1.
\]
Thus \(d\ge2\), and \(\delta(sx,v)=d-2\). Induction gives
\[
\operatorname{natDegree}(qR_{sx,v})
\le1+(d-2)=d-1\le d.
\]

### Step 5. Combine the two bounds

The degree of a sum is at most the maximum of the degrees of its summands. Steps 3–4 therefore give \(\operatorname{natDegree}R_{x,y}\le d\), completing the induction.

For \(R_{1,s}=q-1\), the bound is one; for \(R_{1,st}=(q-1)^2\), it is two. These examples have the full allowed degree.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.OrdinaryR.polynomial_degree`: [OrdinaryR.lean:125](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L125).
