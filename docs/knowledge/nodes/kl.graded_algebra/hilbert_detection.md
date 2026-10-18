---
id: kl.sheaves.hilbert_detection
title: Equality detected by Hilbert values
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.sheaves.hilbert_free
- kl.detail.hilbert_values
lean:
  repository: openai-kl
  modules:
  - HilbertSeries
  declarations:
  - OAI.KLInvariance.Hilbert.polynomial_eq_of_value_eq
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:273
    format: lean-location
    note: OAI.KLInvariance.Hilbert.polynomial_eq_of_value_eq
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

# Equality detected by Hilbert values

Let \(M\) be a finitely generated graded polynomial module, and let \(S\subseteq T\) be subspaces of \(M\), with \(T\) closed under homogeneous components. If their Hilbert values, computed from the dimensions of their intersections with the graded pieces, agree at some \(0<q<1\), then \(S=T\).

*Proof.*

### Step 1. Compare the finite-dimensional pieces

Write \(M=\bigoplus_nM_n\), and put \(S_n=S\cap M_n\) and \(T_n=T\cap M_n\). The containment \(S\subseteq T\) gives \(S_n\subseteq T_n\), hence
\[
a_n=\dim T_n-\dim S_n\ge0.
\]
Each dimension is finite. Indeed, choose finite homogeneous generators of \(M\). In each degree, monomials times those generators span a finite-dimensional space. The same finite-dimensional bound applies to its subspaces \(S_n,T_n\).

### Step 2. Justify the convergent difference series

A generator of degree \(d\) contributes at most the Hilbert series \(q^d/(1-q)^N\), where \(N\) is the number of variables. A finite sum of these expressions bounds both \(H_S(q)\) and \(H_T(q)\) for \(0<q<1\). Thus subtraction of their convergent series is legitimate:
\[
H_T(q)-H_S(q)=\sum_n a_nq^n.
\]
The hypothesis makes the left-hand side zero.

### Step 3. Prove every coefficient difference is zero

Fix a degree \(m\). Every summand on the right is nonnegative, so
\(0\le a_mq^m\le\sum_n a_nq^n=0\).
Since \(q^m>0\), \(a_m=0\). This works for every \(m\).
Therefore \(S_m\subseteq T_m\) are finite-dimensional subspaces of the same dimension, and hence \(S_m=T_m\).

This last implication follows by extending a basis of \(S_m\) to a basis of \(T_m\): the equality of dimensions leaves no additional basis vectors.

### Step 4. Recover the whole subspace

Take \(v\in T\). Its homogeneous decomposition is a finite sum \(v=\sum_m v_m\). The assumed closure of \(T\) under homogeneous components gives \(v_m\in T_m\). Step 3 gives \(v_m\in S_m\subseteq S\). Because \(S\) is a subspace, the finite sum \(v\) lies in \(S\).

Thus \(T\subseteq S\), and the original containment proves equality. Closure of \(S\) under homogeneous components was not needed. The argument detects a nonzero difference in any degree, including one supported in higher codimension.

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.Hilbert.polynomial_eq_of_value_eq`: [HilbertSeries.lean:273](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L273).
