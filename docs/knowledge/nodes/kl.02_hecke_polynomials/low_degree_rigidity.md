---
id: kl.hecke.low_degree_rigidity
title: A reciprocal polynomial strictly below the midpoint is zero
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.hecke.polynomial_reflection
lean:
  repository: openai-kl
  modules:
  - Bruhat
  declarations:
  - OAI.KLInvariance.low_degree_reflect_eq_self
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:141
    format: lean-location
    note: OAI.KLInvariance.low_degree_reflect_eq_self
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the exact domain, degree conventions and source
    argument?
  verdict: Read low_degree_reflect_eq_self in Bruhat; used its decisive coefficient
    at natural degree and derived uniqueness of a low-degree defect solution by subtraction.
tags:
- Kazhdan-Lusztig
- Hecke
---

# A reciprocal polynomial strictly below the midpoint is zero

Let \(f\in\mathbb Z[q]\). If
\[
2\,\operatorname{natDegree}(f)<d,\qquad
\operatorname{reflect}_df=f,
\]
then \(f=0\).

Consequently, for \(d>0\), at most one polynomial supported strictly below \(d/2\) solves an equation
\(\operatorname{reflect}_dP=P+D\).

*Proof.*

### Step 1. Choose the highest nonzero coefficient

Suppose \(f\ne0\), and let \(m=\operatorname{natDegree}(f)\). Then \(f_m\ne0\). The strict bound implies \(m<d-m\) and \(m\le d\).

### Step 2. Read the reciprocal identity at degree m

The coefficient of \(\operatorname{reflect}_df\) at \(m\) is \(f_{d-m}\). Since \(d-m>m\), this coefficient is zero by maximality of \(m\).

But the identity says it equals \(f_m\ne0\), a contradiction. Thus \(f=0\).

### Step 3. Apply the result to two solutions

If \(P,P'\) solve the same defect equation, subtract them. Linearity of reflection gives
\[
\operatorname{reflect}_d(P-P')=P-P'.
\]
The natural degree of a difference is at most the maximum of the two natural degrees. Therefore the strict midpoint bounds for \(P,P'\) imply the same bound for \(P-P'\). The first part gives \(P-P'=0\), hence \(P=P'\).

The strict inequality singles out the lower half. In degree \(d=2m\), the middle monomial \(q^m\) is reciprocal and nonzero.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.low_degree_reflect_eq_self`: [Bruhat.lean:141](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L141).
