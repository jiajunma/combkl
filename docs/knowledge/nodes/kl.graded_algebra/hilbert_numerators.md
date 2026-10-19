---
id: kl.algebra.hilbert_numerators
title: Uniqueness and degree shifts of polynomial Hilbert numerators
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses: []
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.Hilbert.hasSum_shift_coeff
  - OAI.KLInvariance.Hilbert.numerator_unique
  - OAI.KLInvariance.Hilbert.numerator_add_shift
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:14
    format: lean-location
    note: OAI.KLInvariance.Hilbert.hasSum_shift_coeff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:24
    format: lean-location
    note: OAI.KLInvariance.Hilbert.numerator_unique
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:38
    format: lean-location
    note: OAI.KLInvariance.Hilbert.numerator_add_shift
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the gradings, scalar actions, coefficient variables and formal polynomial
    conclusions explicit?
  verdict: Read all three Hilbert numerator lemmas. Kept the arbitrary nonzero common
    factor, the integer shift and nonzero real parameter for reindexing, then the
    infinite-evaluation argument over the embedded integer coefficients.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Uniqueness and degree shifts of polynomial Hilbert numerators

Let \(D:\mathbb R\to\mathbb R\) satisfy \(D(t)\ne0\) whenever \(0<t<1\). For a sequence \(f:\mathbb Z\to\mathbb N\), suppose the convergent sum
\[
\mathcal H_f(t)=\sum_{n\in\mathbb Z}f(n)t^n
\]
has the form \(F(t)D(t)\) for an integer polynomial \(F\in\mathbb Z[q]\), at every real \(0<t<1\). Here \(q\) is the polynomial variable and \(F(t)\) means evaluation at \(q=t\).

Convergence here means that the sums over finite subsets of \(\mathbb Z\) converge as those subsets grow by inclusion. This is the source’s `HasSum` convention, and it permits reindexing by a bijection.

The polynomial \(F\) is uniquely determined by these identities.

More generally, suppose \(F,G,H\in\mathbb Z[q]\) give such sums for sequences \(f,g,h\) with the same factor \(D(t)\). If
\[
f(n)=g(n)+h(n-1)\qquad(n\in\mathbb Z),
\]
then
\[
F(q)=G(q)+qH(q).
\]

*Proof.*

### Step 1. Reindex a convergent shifted sum

For any real \(t\ne0\), any integer \(d\), and a convergent sum
\(\sum_n a(n)t^n=c\), reindex by \(n=j+d\):
\[
\sum_n a(n-d)t^n
=\sum_j a(j)t^{j+d}
=t^d\sum_j a(j)t^j=t^dc.
\]
The integer shift is a bijection of \(\mathbb Z\), and the given convergence permits this reindexing. Multiplication by the fixed scalar \(t^d\) preserves convergence. The identity \(t^{j+d}=t^jt^d\) uses \(t\ne0\).

This is hasSum_shift_coeff. In the application \(d=1\), it produces the factor \(t\).

### Step 2. Cancel the common factor for uniqueness

Suppose both \(F\) and \(G\) describe the same sequence \(f\). Uniqueness of the convergent sum gives
\[
F(t)D(t)=G(t)D(t)
\]
for every \(0<t<1\). Since \(D(t)\ne0\), we obtain \(F(t)=G(t)\) throughout that interval.

### Step 3. Recover equality of the polynomials

View the integer coefficients in \(\mathbb R\). The polynomial \(F-G\) vanishes at every point of the infinite interval \((0,1)\).

A nonzero polynomial has only finitely many roots: factoring out the linear factor corresponding to a root reduces its degree by one. Hence \(F-G\) is zero over \(\mathbb R\). Injectivity of \(\mathbb Z\to\mathbb R\) gives equality of every integer coefficient, so \(F=G\) in \(\mathbb Z[q]\).

### Step 4. Sum the degreewise addition formula

Fix \(0<t<1\). By Step 1 with \(d=1\),
\[
\sum_n h(n-1)t^n=tH(t)D(t).
\]
Adding this convergent sum to the one for \(g\), and using the given coefficient identity, gives
\[
F(t)D(t)=G(t)D(t)+tH(t)D(t).
\]
Cancellation of \(D(t)\) yields \(F(t)=G(t)+tH(t)\).

### Step 5. Return to a formal polynomial identity

Apply the argument of Step 3 to \(F-G-qH\). It vanishes at every \(t\in(0,1)\), so it is the zero integer polynomial. This proves the second assertion.

For word stalks, the common factor is \(D(t)=(1-t)^{-N}\), where \(N\) is the number of degree-one coefficient variables. Its nonvanishing on \((0,1)\) allows exactly this passage from homogeneous dimensions to characters.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Hilbert.hasSum_shift_coeff`: [IntegralPairings.lean:14](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L14).

`OAI.KLInvariance.Hilbert.numerator_unique`: [IntegralPairings.lean:24](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L24).

`OAI.KLInvariance.Hilbert.numerator_add_shift`: [IntegralPairings.lean:38](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L38).
