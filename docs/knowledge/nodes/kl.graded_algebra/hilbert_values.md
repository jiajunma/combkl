---
id: kl.detail.hilbert_values
title: Hilbert values and degreewise defects of submodules
kind: definition
status: formalized
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.sheaves.graded_module
- kl.algebra.grading_components
lean:
  repository: openai-kl
  modules:
  - ModuleAlgebra
  declarations:
  - OAI.KLInvariance.Hilbert.piece
  - OAI.KLInvariance.Hilbert.term
  - OAI.KLInvariance.Hilbert.value
  - OAI.KLInvariance.Hilbert.defectPiece
  - OAI.KLInvariance.Hilbert.defectTerm
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
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:571
    format: lean-location
    note: OAI.KLInvariance.Hilbert.defectPiece
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:574
    format: lean-location
    note: OAI.KLInvariance.Hilbert.defectTerm
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# Hilbert series, numerical values, and degreewise defects

Let \(M=\bigoplus_{n\in\mathbb Z}M_n\) be a graded vector space over \(k\), with finite-dimensional pieces. Its Hilbert function is
\[
h_M(n)=\dim_k M_n.
\]
For a nonnegative grading, its formal Hilbert series is
\[
\operatorname{Hilb}(M;q)=\sum_{n\ge0}h_M(n)q^n.
\]
Here \(q\) is a formal symbol: specifying the series means specifying each coefficient. A grading bounded below gives the analogous formal Laurent series, with finitely many possible negative exponents.

## Numerical evaluation

To compare real numbers, choose a positive real \(q\) for which the series converges and put
\[
H_M(q)=\sum_{n\in\mathbb Z}h_M(n)q^n.
\]
For a finite graded free module over a polynomial ring, the series converges when \(0<q<1\). The proof computes it as a finite sum of shifted geometric-series products.

For \(A=k[X_1,\ldots,X_N]\) and a homogeneous free basis of \(M\) with degrees \(d_j\),
\[
H_M(q)=\frac{\sum_jq^{d_j}}{(1-q)^N}
       =\frac{\operatorname{grk}_A(M;q)}{(1-q)^N}.
\]
The numerator counts homogeneous basis generators. The denominator counts the monomials that can multiply each generator. The theorem [[node:kl.sheaves.hilbert_free]] proves this identity, including convergence.

For \(A=k[X]\), the module \(A\oplus A(2)\) has component dimensions \(1,1,2,2,\ldots\). Therefore
\[
H_{A\oplus A(2)}(q)=1+q+2q^2+2q^3+\cdots
                  =\frac{1+q^2}{1-q}.
\]
The quotient \(A/(X)\) has Hilbert value one, since only its degree-zero piece survives.

## Subspaces of a fixed ambient grading

For a subspace \(S\subseteq M\), define \(S_n=S\cap M_n\). Its term and numerical value are
\[
h_{S,n}(q)=\dim_k(S_n)q^n,\qquad
H_S(q)=\sum_{n\in\mathbb Z}h_{S,n}(q),
\]
at convergent parameters. These definitions use the fixed ambient components. When \(S\) is homogeneous, those components decompose \(S\) itself.

If \(S\subseteq T\), then \(S_n\subseteq T_n\), so \(h_{S,n}(q)\le h_{T,n}(q)\) for \(q>0\). Convergence of the larger nonnegative series implies convergence of the smaller one.

## The defect of an inclusion

Define
\[
D_n=T_n/S_n,\qquad d_n(q)=\dim_k(D_n)q^n.
\]
Finite-dimensional rank–nullity gives
\[
d_n(q)=h_{T,n}(q)-h_{S,n}(q).
\]
Summing at a convergent positive parameter gives
\[
\sum_n d_n(q)=H_T(q)-H_S(q).
\]
Every summand is nonnegative. If one quotient \(D_n\) is nonzero, its summand is strictly positive, so the Hilbert values differ.

When \(T\) is homogeneous and the two Hilbert values are equal, every \(S_n=T_n\). Each element of \(T\) is a finite sum of those components and therefore belongs to \(S\). This is the equality-detection mechanism used in the edge-image comparison.

## References

The precise Lean sources are listed below.

## Lean formalization

`OAI.KLInvariance.Hilbert.piece`: [ModuleAlgebra.lean:500](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L500).

`OAI.KLInvariance.Hilbert.term`: [ModuleAlgebra.lean:503](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L503).

`OAI.KLInvariance.Hilbert.value`: [ModuleAlgebra.lean:506](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L506).

`OAI.KLInvariance.Hilbert.defectPiece`: [ModuleAlgebra.lean:571](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L571).

`OAI.KLInvariance.Hilbert.defectTerm`: [ModuleAlgebra.lean:574](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L574).
