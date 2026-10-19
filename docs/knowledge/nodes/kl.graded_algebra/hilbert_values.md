---
id: kl.detail.hilbert_values
title: Hilbert functions, formal series and numerical values
kind: definition
status: formalized
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.grading_components
- kl.algebra.homogeneous_subquotients
lean:
  repository: openai-kl
  modules:
  - HilbertSeries
  - ModuleAlgebra
  declarations:
  - OAI.KLInvariance.Hilbert.piece
  - OAI.KLInvariance.Hilbert.term
  - OAI.KLInvariance.Hilbert.value
  - OAI.KLInvariance.Hilbert.subPieceEquiv
  - OAI.KLInvariance.Hilbert.term_subPiece
  - OAI.KLInvariance.Hilbert.value_subPiece
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:500
    format: lean-location
    note: OAI.KLInvariance.Hilbert.piece
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:503
    format: lean-location
    note: OAI.KLInvariance.Hilbert.term
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:506
    format: lean-location
    note: OAI.KLInvariance.Hilbert.value
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:434
    format: lean-location
    note: OAI.KLInvariance.Hilbert.subPieceEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:443
    format: lean-location
    note: OAI.KLInvariance.Hilbert.term_subPiece
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:447
    format: lean-location
    note: OAI.KLInvariance.Hilbert.value_subPiece
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the grading, scalar, finiteness and convergence hypotheses retained?
  verdict: Read Hilbert.piece/term/value and the subPiece equivalence. Separated formal
    coefficient notation from the actual real-valued implementation, and stated its
    finite-piece/summability scope.
tags:
- Kazhdan-Lusztig
- graded-algebra
---

# Hilbert functions, formal series and numerical values

Fix a \(k\)-vector space \(M\) with integer-indexed homogeneous subspaces \(M_n\). For a \(k\)-subspace \(S\subseteq M\), the source defines
\[
\operatorname{piece}(S,n)=\{m\in M_n:m\in S\}.
\]
This is a subspace of the fixed ambient component \(M_n\). Its underlying vectors form \(S\cap M_n\).

The code uses the natural-number finite rank of each intersection piece. When these pieces are finite-dimensional, this is their usual vector-space dimension, giving the Hilbert function
\[
h_S(n)=\dim_k(S\cap M_n).
\]
For \(S=M\), this is the usual component dimension \(h_M(n)=\dim_kM_n\).

## Formal series

For a nonnegative grading, write
\[
\operatorname{Hilb}(M;z)=\sum_{n\ge0}h_M(n)z^n.
\]
The symbol \(z\) is formal: the series specifies a sequence of coefficients. A grading bounded below gives a formal Laurent series, with only finitely many possible negative exponents.

If \(S\) is homogeneous, its intersection pieces form the grading of \(S\), so they define its Hilbert series in the same way. The local piece construction also applies to arbitrary subspaces of the ambient vector space.

## Numerical terms and values

For a real parameter \(q\), the local definitions are
\[
\operatorname{term}(S,q,n)=h_S(n)q^n,\qquad
\operatorname{value}(S,q)=\sum_{n\in\mathbb Z}h_S(n)q^n.
\]
The implementation uses a real infinite sum for value. Summability means that finite partial sums approach a fixed real number as their finite index sets increase. For nonnegative terms this is equivalent to boundedness of those finite sums. The comparison theorems supply positivity and summability hypotheses.

We write \(H_S(q)\) for this numerical Hilbert value when using those theorems. For finite graded modules over \(k[X_1,\ldots,X_N]\), convergence and finite-dimensional pieces are proved for every \(0<q<1\). Homogeneous free bases give an explicit formula; finite homogeneous free covers give convergence for general finite modules.

The OpenAI notes use \(\operatorname{Hilb}(M;q)\) in these convergent numerical comparisons. Formal coefficient identities can also be evaluated at such a \(q\).

## The running module

For \(A=k[X]\) and \(M=A\oplus A(2)\),
\[
M_n=A_n\oplus A_{n-2}.
\]
The dimensions are \(1,1,2,2,\ldots\). Thus
\[
\operatorname{Hilb}(M;z)=1+z+2z^2+2z^3+\cdots,
\]
and, for \(0<q<1\),
\[
H_M(q)=\frac{1+q^2}{1-q}.
\]
The numerator counts the two module generators in degrees zero and two. The full Hilbert function also counts their polynomial multiples.

For \(A/(X)\), only the constant class survives, so its Hilbert function is one at degree zero and zero elsewhere, and its value is one.

## Two presentations of a submodule piece

For an \(A\)-submodule \(S\), the family of intersections can be represented inside \(S\) itself or inside the fixed ambient pieces \(M_n\). The corresponding degree-\(n\) vector spaces identify by retaining the same vector and exchanging the two membership conditions \(m\in S\), \(m\in M_n\).

Thus their finite dimensions, terms and Hilbert values agree. This is the source's subPieceEquiv and value_subPiece conversion.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit convergence and degreewise comparison.**

**OpenAI notes:** The graded-rank paragraph gives \(\operatorname{Hilb}(M;q)=\operatorname{grk}_A(M;q)/(1-q)^N\) for a homogeneous free basis. The comparison evaluates Hilbert series at \(0<q<1\), uses the factor \(1-q\) for a degree-one scalar quotient, and detects equality through a positive quotient deficit. [sec:background](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2), [eq:state](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L243), [eq:image-equality](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L370).

**Lean (primary):** The implementation defines real integer-indexed terms from the finite ranks of intersections with ambient pieces. Finite homogeneous covers prove piece finiteness and summability. Degreewise exactness proves the scalar-quotient factor, and inclusion plus homogeneity of the larger subspace turns one equal positive Hilbert value into equality. [ModuleAlgebra:506](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L506), [HilbertSeries:245](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L245), [Support:1186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1186), [ModuleAlgebra:549](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L549).

**Role in the proof:** The KB distinguishes the formal coefficient series, its convergent real value and the free-module basis-degree polynomial. The factor \((1-q)^N\) removes the coefficient-ring contribution; \(1-q\) records quotienting by a regular degree-one label.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Hilbert.piece`: [ModuleAlgebra.lean:500](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L500).

`OAI.KLInvariance.Hilbert.term`: [ModuleAlgebra.lean:503](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L503).

`OAI.KLInvariance.Hilbert.value`: [ModuleAlgebra.lean:506](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L506).

`OAI.KLInvariance.Hilbert.subPieceEquiv`: [HilbertSeries.lean:434](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L434).

`OAI.KLInvariance.Hilbert.term_subPiece`: [HilbertSeries.lean:443](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L443).

`OAI.KLInvariance.Hilbert.value_subPiece`: [HilbertSeries.lean:447](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L447).
