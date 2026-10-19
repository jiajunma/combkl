---
id: kl.algebra.character_basis_independence
title: Independence of the basis-degree polynomial
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.detail.graded_character
- kl.sheaves.hilbert_free
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.Graded.NonnegativeBasis.hasSum
  - OAI.KLInvariance.Graded.NonnegativeBasis.polynomial_eq
  - OAI.KLInvariance.Graded.character_eq
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:64
    format: lean-location
    note: OAI.KLInvariance.Graded.NonnegativeBasis.hasSum
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:72
    format: lean-location
    note: OAI.KLInvariance.Graded.NonnegativeBasis.polynomial_eq
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:98
    format: lean-location
    note: OAI.KLInvariance.Graded.character_eq
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the grading, scalar, finiteness and convergence hypotheses retained?
  verdict: Read NonnegativeBasis.polynomial_eq and character_eq. Expanded equality
    of the two convergent sums, nonzero denominator cancellation, infinitely many
    evaluations and injectivity of integer coefficients.
tags:
- Kazhdan-Lusztig
- graded-algebra
---

# Independence of the basis-degree polynomial

Let \(A=k[X_1,\ldots,X_N]\), with \(k\) a field and variables of degree one. Any two finite homogeneous bases of the same nonnegatively graded polynomial module give the same basis-degree polynomial. Consequently Graded.character equals the polynomial computed from every such basis.

*Proof.*

### Step 1. Compute the same Hilbert sum from both bases

Let \(e_i\) have degrees \(d_i\), and let \(f_j\) have degrees \(c_j\). Put
\[
p(z)=\sum_i z^{d_i},\qquad r(z)=\sum_j z^{c_j}.
\]
For every real \(0<q<1\), the [[node:kl.sheaves.hilbert_free|homogeneous-free Hilbert theorem]] gives
\[
H_M(q)=p(q)(1-q)^{-N}=r(q)(1-q)^{-N}.
\]
Both are sums of the same component-dimension sequence of \(M\).

### Step 2. Cancel the common denominator

Since \(q<1\), we have \(1-q>0\). Its inverse and every natural power are nonzero, so cancellation gives
\(p(q)=r(q)\)
for every \(0<q<1\).

### Step 3. Recover the polynomial coefficients

Map integer coefficients into \(\mathbb R\). The polynomial \(p-r\) vanishes at all points of an infinite real interval.

A nonzero polynomial has at most its degree many distinct roots: each root divides out a linear factor, and the degree falls by one. Hence \(p-r\) is zero over \(\mathbb R\). Injectivity of \(\mathbb Z\to\mathbb R\) gives \(p=r\) over \(\mathbb Z\).

### Step 4. Identify the selected character

Graded.character is the polynomial of one chosen nonnegative homogeneous basis. Apply the first part to that basis and any other one. Their polynomials agree, so the chosen definition computes the intrinsic graded-rank polynomial.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Graded.NonnegativeBasis.hasSum`: [SheafMorphisms.lean:64](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L64).

`OAI.KLInvariance.Graded.NonnegativeBasis.polynomial_eq`: [SheafMorphisms.lean:72](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L72).

`OAI.KLInvariance.Graded.character_eq`: [SheafMorphisms.lean:98](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L98).
