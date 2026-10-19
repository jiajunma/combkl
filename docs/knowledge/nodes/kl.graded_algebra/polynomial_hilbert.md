---
id: kl.algebra.polynomial_hilbert
title: The polynomial-ring Hilbert series from monomial degrees
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.grading_components
- kl.detail.hilbert_values
lean:
  repository: openai-kl
  modules:
  - HilbertSeries
  declarations:
  - OAI.KLInvariance.Hilbert.hasSum_monomials
  - OAI.KLInvariance.Hilbert.polynomial_finrank_nat
  - OAI.KLInvariance.Hilbert.hasSum_finsupp_monomials
  - OAI.KLInvariance.Hilbert.hasSum_polynomial_nat
  - OAI.KLInvariance.Hilbert.hasSum_polynomial
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:14
    format: lean-location
    note: OAI.KLInvariance.Hilbert.hasSum_monomials
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:62
    format: lean-location
    note: OAI.KLInvariance.Hilbert.polynomial_finrank_nat
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:68
    format: lean-location
    note: OAI.KLInvariance.Hilbert.hasSum_finsupp_monomials
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:81
    format: lean-location
    note: OAI.KLInvariance.Hilbert.hasSum_polynomial_nat
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:100
    format: lean-location
    note: OAI.KLInvariance.Hilbert.hasSum_polynomial
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the grading, scalar, finiteness and convergence hypotheses retained?
  verdict: Read the monomial sum, degree-fiber and polynomial HasSum proofs. Expanded
    the empty-variable base, one-variable product induction, finite degree fibers
    and integer-index extension.
tags:
- Kazhdan-Lusztig
- graded-algebra
---

# The polynomial-ring Hilbert series from monomial degrees

Let \(k\) be a field and \(A=k[X_i:i\in I]\), where \(I\) is finite with cardinality \(N\), and give every variable degree one. Every homogeneous piece is finite-dimensional, and
\[
\operatorname{Hilb}(A;z)=\frac1{(1-z)^N}.
\]
For every real \(0\le q<1\), the corresponding numerical series converges and has value \((1-q)^{-N}\).

*Proof.*

### Step 1. Identify a basis in each degree

A monomial is determined by exponents \(a_i\in\mathbb N\):
\[
X^a=\prod_{i\in I}X_i^{a_i},\qquad |a|=\sum_{i\in I}a_i.
\]
The monomials with \(|a|=n\) form a \(k\)-basis of \(A_n\). For \(n\ge0\), each exponent lies between zero and \(n\), so only finitely many such exponent tuples exist.

For \(n<0\), there are no such tuples and \(A_n=0\). Therefore the dimension in degree \(n\ge0\) is exactly the number of exponent tuples of total degree \(n\).

### Step 2. Compute the ungrouped monomial sum

With no variables, there is one exponent tuple, the empty tuple, giving the sum one.

Add one variable to an already considered finite set. An exponent tuple becomes a pair consisting of its exponent \(a\ge0\) in the new variable and the old tuple \(b\). Its weight factors:
\[
q^{a+|b|}=q^a q^{|b|}.
\]
For \(0\le q<1\), the geometric series \(\sum_{a\ge0}q^a=(1-q)^{-1}\) converges. The old tuple series converges by induction.

Both series have nonnegative terms, so their product is the convergent double sum of these products. Induction on the number of variables gives
\[
\sum_{a\in\mathbb N^I}q^{|a|}=(1-q)^{-N}.
\]

### Step 3. Group the monomials by total degree

Group the convergent nonnegative sum according to \(n=|a|\). The degree-\(n\) group has \(h_A(n)\) terms, each equal to \(q^n\). Hence
\[
\sum_{n\ge0}h_A(n)q^n=(1-q)^{-N}.
\]
The integer-indexed version adds the zero terms in negative degrees and gives the same sum.

### Step 4. Read the formal series coefficientwise

The product of \(N\) formal geometric series has degree-\(n\) coefficient equal to the number of exponent tuples with total degree \(n\). Only finitely many tuples contribute to that coefficient, as shown in Step 1.

These coefficients are exactly those of \(\operatorname{Hilb}(A;z)\), proving the formal identity as well.

For one variable, every nonnegative piece has dimension one. For two variables, degree \(n\) has basis \(X^n,X^{n-1}Y,\ldots,Y^n\), so its dimension is \(n+1\) and
\[
1+2z+3z^2+4z^3+\cdots=(1-z)^{-2}.
\]

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Hilbert.hasSum_monomials`: [HilbertSeries.lean:14](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L14).

`OAI.KLInvariance.Hilbert.polynomial_finrank_nat`: [HilbertSeries.lean:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L62).

`OAI.KLInvariance.Hilbert.hasSum_finsupp_monomials`: [HilbertSeries.lean:68](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L68).

`OAI.KLInvariance.Hilbert.hasSum_polynomial_nat`: [HilbertSeries.lean:81](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L81).

`OAI.KLInvariance.Hilbert.hasSum_polynomial`: [HilbertSeries.lean:100](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L100).
