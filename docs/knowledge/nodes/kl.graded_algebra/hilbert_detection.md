---
id: kl.sheaves.hilbert_detection
title: Equality and strict inclusion detected by Hilbert values
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.detail.hilbert_values
- kl.algebra.hilbert_defect
- kl.algebra.hilbert_convergence
lean:
  repository: openai-kl
  modules:
  - HilbertSeries
  - ModuleAlgebra
  declarations:
  - OAI.KLInvariance.Hilbert.piece_mono
  - OAI.KLInvariance.Hilbert.term_mono
  - OAI.KLInvariance.Hilbert.summable_of_le
  - OAI.KLInvariance.Hilbert.pieces_eq_of_value_eq
  - OAI.KLInvariance.Hilbert.eq_of_value_eq
  - OAI.KLInvariance.Hilbert.value_mono
  - OAI.KLInvariance.Hilbert.defectTerm_eq_sub
  - OAI.KLInvariance.Hilbert.defect_value_eq_sub
  - OAI.KLInvariance.Hilbert.defect_value_pos
  - OAI.KLInvariance.Hilbert.polynomial_eq_of_value_eq
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:509
    format: lean-location
    note: OAI.KLInvariance.Hilbert.piece_mono
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:517
    format: lean-location
    note: OAI.KLInvariance.Hilbert.term_mono
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:523
    format: lean-location
    note: OAI.KLInvariance.Hilbert.summable_of_le
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:530
    format: lean-location
    note: OAI.KLInvariance.Hilbert.pieces_eq_of_value_eq
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:549
    format: lean-location
    note: OAI.KLInvariance.Hilbert.eq_of_value_eq
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:565
    format: lean-location
    note: OAI.KLInvariance.Hilbert.value_mono
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:577
    format: lean-location
    note: OAI.KLInvariance.Hilbert.defectTerm_eq_sub
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:590
    format: lean-location
    note: OAI.KLInvariance.Hilbert.defect_value_eq_sub
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:603
    format: lean-location
    note: OAI.KLInvariance.Hilbert.defect_value_pos
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
  prompt: Are the grading, scalar, finiteness and convergence hypotheses retained?
  verdict: Read the generic piece/value comparison and defect lemmas, then polynomial_eq_of_value_eq.
    Preserved arbitrary k-subspaces, homogeneity of the target only, positive q and
    the exact summability hypothesis.
tags:
- Kazhdan-Lusztig
- graded-algebra
---

# Equality and strict inclusion detected by Hilbert values

Let \(M=\bigoplus_nM_n\) be a graded vector space over a field \(k\), with finite-dimensional pieces, and let \(S\subseteq T\) be \(k\)-subspaces. Fix \(q>0\), assume the Hilbert series for \(T\) converges, and suppose \(T\) is closed under homogeneous components.

Then
\[
H_S(q)=H_T(q)\quad\Longrightarrow\quad S=T.
\]
The defect series converges and satisfies
\[
\sum_n\dim_k(T_n/S_n)q^n=H_T(q)-H_S(q).
\]
If \(S\ne T\), this difference is strictly positive.

For a finite graded polynomial module and \(0<q<1\), the finite-piece and convergence hypotheses are supplied by the [[node:kl.algebra.hilbert_convergence|convergence theorem]].

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit convergence and degreewise comparison.**

**OpenAI notes:** The graded-rank paragraph gives \(\operatorname{Hilb}(M;q)=\operatorname{grk}_A(M;q)/(1-q)^N\) for a homogeneous free basis. The comparison evaluates Hilbert series at \(0<q<1\), uses the factor \(1-q\) for a degree-one scalar quotient, and detects equality through a positive quotient deficit. [sec:background](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2), [eq:state](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L243), [eq:image-equality](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L370).

**Lean (primary):** The implementation defines real integer-indexed terms from the finite ranks of intersections with ambient pieces. Finite homogeneous covers prove piece finiteness and summability. Degreewise exactness proves the scalar-quotient factor, and inclusion plus homogeneity of the larger subspace turns one equal positive Hilbert value into equality. [ModuleAlgebra:506](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L506), [HilbertSeries:245](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L245), [Support:1186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1186), [ModuleAlgebra:549](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L549).

**Role in the proof:** The KB distinguishes the formal coefficient series, its convergent real value and the free-module basis-degree polynomial. The factor \((1-q)^N\) removes the coefficient-ring contribution; \(1-q\) records quotienting by a regular degree-one label.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Compare the terms and obtain convergence for S

In each degree, \(S_n\subseteq T_n\), so
\[
0\le\dim_kS_n\,q^n\le\dim_kT_n\,q^n.
\]
The larger series converges by hypothesis. Nonnegative comparison proves convergence of the smaller series and \(H_S(q)\le H_T(q)\).

### Step 2. Sum the degreewise defect identity

Finite-dimensional rank–nullity for the quotient \(T_n/S_n\) gives
\[
\dim_k(T_n/S_n)q^n
=\dim_kT_nq^n-\dim_kS_nq^n.
\]
Both series on the right converge by Step 1. Their difference therefore converges and sums to \(H_T(q)-H_S(q)\).

### Step 3. Use equality of values to identify every piece

Assume \(H_S(q)=H_T(q)\). Fix a degree \(n\). Nonnegativity of all terms gives
\[
0\le\dim_k(T_n/S_n)q^n
\le\sum_j\dim_k(T_j/S_j)q^j=0.
\]
Thus every defect term is zero.

Since \(q^n>0\), the quotient \(T_n/S_n\) has dimension zero. Its finite-dimensional spaces therefore satisfy \(S_n=T_n\). Equivalently, a basis of \(S_n\) extends to a basis of \(T_n\), and the zero dimension difference leaves no extra basis vectors.

### Step 4. Recover equality of the whole subspaces

Take \(m\in T\). Homogeneity of \(T\) places every component \(\pi_n(m)\) in \(T_n=S_n\subseteq S\).

The homogeneous decomposition of \(m\) is finite. Since \(S\) is a subspace, its sum belongs to \(S\). This proves \(T\subseteq S\), and hence \(S=T\).

### Step 5. Obtain strict positivity and the polynomial-module form

Step 1 gives \(H_S(q)\le H_T(q)\). If \(S\ne T\), Step 4 rules out equality, so \(H_S(q)<H_T(q)\). The defect identity from Step 2 is therefore strictly positive.

Finally, a finite graded polynomial module has finite pieces and convergent intersection series at every \(0<q<1\). Substituting those facts proves the polynomial-module version used in image comparison.

The homogeneous closure assumption in Step 4 concerns \(T\). The smaller subspace enters through its intersections and closure under finite sums.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Hilbert.piece_mono`: [ModuleAlgebra.lean:509](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L509).

`OAI.KLInvariance.Hilbert.term_mono`: [ModuleAlgebra.lean:517](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L517).

`OAI.KLInvariance.Hilbert.summable_of_le`: [ModuleAlgebra.lean:523](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L523).

`OAI.KLInvariance.Hilbert.pieces_eq_of_value_eq`: [ModuleAlgebra.lean:530](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L530).

`OAI.KLInvariance.Hilbert.eq_of_value_eq`: [ModuleAlgebra.lean:549](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L549).

`OAI.KLInvariance.Hilbert.value_mono`: [ModuleAlgebra.lean:565](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L565).

`OAI.KLInvariance.Hilbert.defectTerm_eq_sub`: [ModuleAlgebra.lean:577](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L577).

`OAI.KLInvariance.Hilbert.defect_value_eq_sub`: [ModuleAlgebra.lean:590](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L590).

`OAI.KLInvariance.Hilbert.defect_value_pos`: [ModuleAlgebra.lean:603](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L603).

`OAI.KLInvariance.Hilbert.polynomial_eq_of_value_eq`: [HilbertSeries.lean:273](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L273).
