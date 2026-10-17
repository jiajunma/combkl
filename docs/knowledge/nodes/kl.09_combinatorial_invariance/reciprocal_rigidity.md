---
id: kl.comparison.reciprocal_rigidity
title: Rigidity below the middle degree
kind: theorem
status: proved
primary_topic: kl.09_combinatorial_invariance
topics:
- kl.09_combinatorial_invariance
uses: []
lean:
  repository: openai-kl
  modules:
  - Comparison
  declarations:
  - OAI.KLInvariance.Comparison.low_degree_zero_of_eval_reciprocal
  - OAI.KLInvariance.Comparison.eq_of_eval_difference_reciprocal
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Comparison:24
    format: lean-location
    note: OAI.KLInvariance.Comparison.low_degree_zero_of_eval_reciprocal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Comparison:50
    format: lean-location
    note: OAI.KLInvariance.Comparison.eq_of_eval_difference_reciprocal
  - artifact: openai-kl-paper
    locator: 6. Reciprocity and simultaneous induction; sec:induction
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- induction
---

# Rigidity below the middle degree

Let \(f\in\mathbb R[q]\) with \(2\deg f<d\). If
\[
f(q)=q^d f(q^{-1})\qquad(0<q<1),
\]
then \(f=0\). Consequently, two integral polynomials satisfying the strict half-degree bound are equal if their difference obeys this reciprocal identity.

*Proof.*

### Step 1. Turn reciprocal evaluations into a polynomial identity

Let \(p\in\mathbb R[q]\), with \(m=\deg p\) when \(p\ne0\), and assume \(2\operatorname{natDegree}(p)<d\). In particular its degree is at most \(d\), so
\[
p^\vee(q)=q^dp(q^{-1})
\]
is a polynomial: if \(p(q)=\sum_{i=0}^m a_iq^i\), then
\(p^\vee(q)=\sum_{i=0}^m a_iq^{d-i}\).

The hypothesis gives \(p(q)=p^\vee(q)\) for every real \(0<q<1\). The interval contains infinitely many numbers; therefore the polynomial \(p-p^\vee\) has infinitely many roots and is zero. We have obtained the polynomial identity \(p=p^\vee\), not just equality at a selected parameter.

### Step 2. Compare one decisive coefficient

Suppose \(p\ne0\). Its coefficient \(a_m\) is nonzero. Since \(2m<d\), we have \(d-m>m\), so the coefficient of \(q^{d-m}\) in \(p\) is zero.

But the coefficient of \(q^{d-m}\) in \(p^\vee\) is exactly \(a_m\): the term with index \(i=m\) produces that exponent, and no other index does. The identity \(p=p^\vee\) therefore says \(0=a_m\), a contradiction. Hence \(p=0\).

### Step 3. Apply this to a difference of two integral polynomials

Let \(P,P'\in\mathbb Z[q]\), each strictly below the middle degree. Put
\(p=(P-P')\) and view its coefficients in \(\mathbb R\).
Subtraction cannot increase the degree beyond the maximum of the two original degrees, so \(p\) satisfies the same strict half-degree bound.

If the assumed reciprocal-difference equation holds for \(P-P'\), Steps 1–2 give \(p=0\) over \(\mathbb R\). Injectivity of \(\mathbb Z\to\mathbb R\) gives \(P=P'\) over \(\mathbb Z\). No positivity of the coefficients of \(P\) or \(P'\) is used.

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.Comparison.low_degree_zero_of_eval_reciprocal`: [Comparison.lean:24](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L24).

`OAI.KLInvariance.Comparison.eq_of_eval_difference_reciprocal`: [Comparison.lean:50](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L50).
