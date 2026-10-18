---
id: kl.sheaves.hilbert_free
title: The Hilbert series of a finite graded free module
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.detail.hilbert_values
- kl.algebra.grading_components
lean:
  repository: openai-kl
  modules:
  - HilbertSeries
  declarations:
  - OAI.KLInvariance.Hilbert.hasSum_homogeneous_basis
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:321
    format: lean-location
    note: OAI.KLInvariance.Hilbert.hasSum_homogeneous_basis
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
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
- background
---

# The Hilbert series of a finite graded free module

Let \(A=k[x_1,\ldots,x_N]\), with every variable in degree one. Suppose that a finite graded free \(A\)-module \(M\) has a homogeneous basis \(e_i\) of degrees \(d_i\). For \(0<q<1\),
\[
\sum_{n\in\mathbb Z}\dim_k M_n\,q^n
=\frac{\sum_i q^{d_i}}{(1-q)^N}.
\]

*Proof.*

### Step 1. Describe one homogeneous piece using the basis

Let \(m_i\) be a finite homogeneous basis with \(\deg m_i=d_i\). Every \(m\in M\) has a unique expression \(\sum_i a_im_i\). The expression is homogeneous of degree \(n\) precisely when \(a_i\) is homogeneous of degree \(n-d_i\) for every \(i\).

To verify the reverse implication, decompose each \(a_i\) by degree. Components of total degree different from \(n\) must sum to zero. Linear independence of the \(m_i\) forces the corresponding coefficients to vanish separately. Hence
\[
M_n\simeq\bigoplus_i A_{n-d_i},
\qquad \dim_kM_n=\sum_i\dim_kA_{n-d_i}.
\]

### Step 2. Compute the polynomial-ring series

Monomials \(X_1^{a_1}\cdots X_N^{a_N}\), with \(a_j\ge0\), form a basis of \(A\). Their degree is \(a_1+\cdots+a_N\). For \(0<q<1\),
\[
\sum_n\dim_k(A_n)q^n
=\sum_{a_1,\ldots,a_N\ge0}q^{a_1+\cdots+a_N}
=\left(\sum_{a\ge0}q^a\right)^N
=(1-q)^{-N}.
\]
The geometric series converges, and its finite product gives the required convergent monomial sum.

### Step 3. Account for the basis shifts

For a fixed \(i\), change the summation index \(m=n-d_i\):
\[
\sum_{n\in\mathbb Z}\dim_k(A_{n-d_i})q^n
=q^{d_i}\sum_{m\ge0}\dim_k(A_m)q^m
=q^{d_i}(1-q)^{-N}.
\]
This works even for an integer shift \(d_i<0\), because \(q>0\), and the degrees remain bounded below for each shifted summand.

### Step 4. Sum the finitely many basis contributions

Use the dimension equality in Step 1 and interchange a finite sum with the convergent series:
\[
H_M(q)=\sum_iq^{d_i}(1-q)^{-N}
=\frac{\sum_iq^{d_i}}{(1-q)^N}.
\]
Thus a generator of positive degree contributes a positive exponent in the numerator, as required by the grading convention.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.Hilbert.hasSum_homogeneous_basis`: [HilbertSeries.lean:321](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L321).
