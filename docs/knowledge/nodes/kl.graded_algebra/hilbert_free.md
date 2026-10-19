---
id: kl.sheaves.hilbert_free
title: Hilbert series and values of a homogeneous free basis
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.polynomial_hilbert
- kl.algebra.module_operations
- kl.algebra.component_transport
- kl.detail.hilbert_values
lean:
  repository: openai-kl
  modules:
  - HilbertSeries
  declarations:
  - OAI.KLInvariance.Hilbert.shiftedPieceEquiv
  - OAI.KLInvariance.Hilbert.shiftedPiece_finrank
  - OAI.KLInvariance.Hilbert.hasSum_shifted_polynomial
  - OAI.KLInvariance.Hilbert.hasSum_shiftedFree
  - OAI.KLInvariance.Hilbert.finrank_homogeneous_basis
  - OAI.KLInvariance.Hilbert.hasSum_homogeneous_basis
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:127
    format: lean-location
    note: OAI.KLInvariance.Hilbert.shiftedPieceEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:142
    format: lean-location
    note: OAI.KLInvariance.Hilbert.shiftedPiece_finrank
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:147
    format: lean-location
    note: OAI.KLInvariance.Hilbert.hasSum_shifted_polynomial
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:160
    format: lean-location
    note: OAI.KLInvariance.Hilbert.hasSum_shiftedFree
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:301
    format: lean-location
    note: OAI.KLInvariance.Hilbert.finrank_homogeneous_basis
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
  prompt: Are the grading, scalar, finiteness and convergence hypotheses retained?
  verdict: 'Read shiftedPieceEquiv, shifted-free HasSum and homogeneous-basis finrank/HasSum.
    Followed the source order: polynomial series, integer translation, finite coordinate
    sum and degreewise basis bijection.'
tags:
- Kazhdan-Lusztig
- graded-algebra
---

# Hilbert series and values of a homogeneous free basis

Let \(k\) be a field and \(A=k[X_1,\ldots,X_N]\), and let a graded \(A\)-module \(M\) have a finite homogeneous basis \(e_i\) with integer degrees \(d_i\). Then
\[
\operatorname{Hilb}(M;z)=\frac{\sum_i z^{d_i}}{(1-z)^N}.
\]
For every \(0<q<1\), the numerical series converges and
\[
H_M(q)=\frac{\sum_i q^{d_i}}{(1-q)^N}.
\]

*Proof.*

### Step 1. Compute the pieces of the shifted free coordinate module

Let \(F=A^I\), with the basis coordinate \(i\) placed in degree \(d_i\). Its degree-\(n\) piece identifies with
\[
F_n\simeq\prod_{i\in I}A_{n-d_i}
\]
by viewing each coordinate together with its degree-membership condition. The inverse assembles those coordinates into one tuple.

The polynomial pieces are finite-dimensional, and \(I\) is finite. Therefore
\[
\dim_kF_n=\sum_i\dim_kA_{n-d_i}.
\]

### Step 2. Evaluate one shifted contribution

For a fixed integer \(d_i\), set \(m=n-d_i\). The map \(m\mapsto m+d_i\) is a bijection of \(\mathbb Z\). Since \(q>0\),
\(q^{m+d_i}=q^{d_i}q^m\).
Thus the polynomial-ring series gives
\[
\sum_{n\in\mathbb Z}\dim_kA_{n-d_i}\,q^n
=q^{d_i}\sum_{m\in\mathbb Z}\dim_kA_m\,q^m
=\frac{q^{d_i}}{(1-q)^N}.
\]
Translation of the convergent series proves convergence of this shifted contribution, including when \(d_i<0\).

### Step 3. Sum the finitely many coordinates

Use Step 1 and add the finitely many convergent series from Step 2:
\[
H_F(q)=\sum_i\frac{q^{d_i}}{(1-q)^N}
=\frac{\sum_iq^{d_i}}{(1-q)^N}.
\]
The same degree identities yield the formal Laurent-series formula.

### Step 4. Transfer the pieces through the homogeneous basis

The basis gives an \(A\)-linear bijection
\[
F\longrightarrow M,\qquad (a_i)\longmapsto\sum_i a_ie_i.
\]
A degree-\(n\) tuple has \(a_i\in A_{n-d_i}\), so each product \(a_ie_i\) has degree \(n\). The bijection preserves degree.

It is surjective on each degree by the [[node:kl.algebra.component_transport|homogeneous-preimage theorem]]. It is injective there because it is injective on the whole module. Thus \(F_n\simeq M_n\) for every \(n\), preserving all the dimensions and transferring Step 3 to \(M\).

For \(M=A\oplus A(2)\), the basis degrees give numerator \(1+q^2\). If \(N=1\), its numerical Hilbert value is \((1+q^2)/(1-q)\); if \(N=2\), it is \((1+q^2)/(1-q)^2\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Hilbert.shiftedPieceEquiv`: [HilbertSeries.lean:127](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L127).

`OAI.KLInvariance.Hilbert.shiftedPiece_finrank`: [HilbertSeries.lean:142](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L142).

`OAI.KLInvariance.Hilbert.hasSum_shifted_polynomial`: [HilbertSeries.lean:147](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L147).

`OAI.KLInvariance.Hilbert.hasSum_shiftedFree`: [HilbertSeries.lean:160](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L160).

`OAI.KLInvariance.Hilbert.finrank_homogeneous_basis`: [HilbertSeries.lean:301](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L301).

`OAI.KLInvariance.Hilbert.hasSum_homogeneous_basis`: [HilbertSeries.lean:321](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L321).
