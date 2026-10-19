---
id: kl.algebra.hilbert_convergence
title: Finite graded polynomial modules have convergent Hilbert values
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.finite_graded_cover
- kl.sheaves.hilbert_free
- kl.algebra.component_transport
- kl.detail.hilbert_values
lean:
  repository: openai-kl
  modules:
  - HilbertSeries
  declarations:
  - OAI.KLInvariance.Hilbert.degreeMap
  - OAI.KLInvariance.Hilbert.degreeMap_surjective
  - OAI.KLInvariance.Hilbert.polynomialModule_piece_finite
  - OAI.KLInvariance.Hilbert.summable_polynomialModule
  - OAI.KLInvariance.Hilbert.summable_term
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:196
    format: lean-location
    note: OAI.KLInvariance.Hilbert.degreeMap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:202
    format: lean-location
    note: OAI.KLInvariance.Hilbert.degreeMap_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:232
    format: lean-location
    note: OAI.KLInvariance.Hilbert.polynomialModule_piece_finite
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:245
    format: lean-location
    note: OAI.KLInvariance.Hilbert.summable_polynomialModule
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:262
    format: lean-location
    note: OAI.KLInvariance.Hilbert.summable_term
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the grading, scalar, finiteness and convergence hypotheses retained?
  verdict: Read polynomialModule_piece_finite, summable_polynomialModule and summable_term.
    Kept arbitrary integer grading and arbitrary k-subspaces; expanded homogeneous
    preimages and termwise domination by a finite shifted free cover.
tags:
- Kazhdan-Lusztig
- graded-algebra
---

# Finite graded polynomial modules have convergent Hilbert values

Let \(k\) be a field and \(A=k[X_1,\ldots,X_N]\), and let \(M\) be any finitely generated \(A\)-module with a compatible integer grading. Then every \(M_n\) is finite-dimensional over \(k\), the grading is bounded below, and
\[
\sum_{n\in\mathbb Z}\dim_kM_n\,q^n
\]
converges for every \(0<q<1\).

For every \(k\)-subspace \(S\subseteq M\), the series of intersection dimensions
\(\sum_n\dim_k(S\cap M_n)q^n\)
also converges.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit convergence and degreewise comparison.**

**OpenAI notes:** The graded-rank paragraph gives \(\operatorname{Hilb}(M;q)=\operatorname{grk}_A(M;q)/(1-q)^N\) for a homogeneous free basis. The comparison evaluates Hilbert series at \(0<q<1\), uses the factor \(1-q\) for a degree-one scalar quotient, and detects equality through a positive quotient deficit. [sec:background](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2), [eq:state](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L243), [eq:image-equality](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L370).

**Lean (primary):** The implementation defines real integer-indexed terms from the finite ranks of intersections with ambient pieces. Finite homogeneous covers prove piece finiteness and summability. Degreewise exactness proves the scalar-quotient factor, and inclusion plus homogeneity of the larger subspace turns one equal positive Hilbert value into equality. [ModuleAlgebra:506](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L506), [HilbertSeries:245](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L245), [Support:1186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1186), [ModuleAlgebra:549](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L549).

**Role in the proof:** The KB distinguishes the formal coefficient series, its convergent real value and the free-module basis-degree polynomial. The factor \((1-q)^N\) removes the coefficient-ring contribution; \(1-q\) records quotienting by a regular degree-one label.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Construct the finite homogeneous cover

The [[node:kl.algebra.finite_graded_cover|finite-cover theorem]] gives a surjective degree-zero map \(f:F\to M\), where
\[
F=A^I,\qquad F_n=\prod_iA_{n-d_i}
\]
for a finite set of integer generator degrees \(d_i\).

### Step 2. Restrict the cover to each homogeneous piece

For \(m\in M_n\), choose any preimage \(v\in F\). Component transport gives
\(f(\pi_n(v))=\pi_n(m)=m\).
Thus \(f_n:F_n\to M_n\) is surjective.

The pieces \(F_n\) are finite-dimensional by the polynomial monomial calculation and finite products. Their quotients \(M_n\) are therefore finite-dimensional, with
\[
0\le\dim_kM_n\le\dim_kF_n.
\]
When \(n\) lies below all the \(d_i\), \(F_n=0\), hence \(M_n=0\). This proves boundedness below.

### Step 3. Compare the nonnegative numerical series

For \(0<q<1\), every \(q^n\) is positive, including for negative \(n\). Multiplying the dimension inequality gives
\[
0\le\dim_kM_n\,q^n\le\dim_kF_n\,q^n.
\]
The [[node:kl.sheaves.hilbert_free|shifted-free Hilbert theorem]] proves that the upper series converges to
\[
\frac{\sum_iq^{d_i}}{(1-q)^N}.
\]
Comparison of nonnegative series proves convergence for \(M\).

### Step 4. Compare an arbitrary ambient subspace

For \(S\subseteq M\), each intersection \(S\cap M_n\) is a subspace of \(M_n\), so
\[
0\le\dim_k(S\cap M_n)q^n\le\dim_kM_nq^n.
\]
Step 3 supplies a convergent upper series. Comparison therefore proves the final assertion.

For example, \(A/(X)\) is generated by the class of one and is covered by \(A\). Its Hilbert value is one. The proof applies through this cover and its degreewise surjections.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Hilbert.degreeMap`: [HilbertSeries.lean:196](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L196).

`OAI.KLInvariance.Hilbert.degreeMap_surjective`: [HilbertSeries.lean:202](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L202).

`OAI.KLInvariance.Hilbert.polynomialModule_piece_finite`: [HilbertSeries.lean:232](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L232).

`OAI.KLInvariance.Hilbert.summable_polynomialModule`: [HilbertSeries.lean:245](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L245).

`OAI.KLInvariance.Hilbert.summable_term`: [HilbertSeries.lean:262](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L262).
