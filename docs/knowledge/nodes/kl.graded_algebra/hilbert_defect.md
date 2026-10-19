---
id: kl.algebra.hilbert_defect
title: Degreewise quotient defects of a subspace inclusion
kind: definition
status: formalized
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.detail.hilbert_values
- kl.algebra.homogeneous_subquotients
lean:
  repository: openai-kl
  modules:
  - ModuleAlgebra
  declarations:
  - OAI.KLInvariance.Hilbert.defectPiece
  - OAI.KLInvariance.Hilbert.defectTerm
source:
  spans:
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
  prompt: Are the grading, scalar, finiteness and convergence hypotheses retained?
  verdict: Read defectPiece and defectTerm. Explained the actual comap denominator
    for arbitrary S,T, its simplification under inclusion and the homogeneous quotient
    interpretation.
tags:
- Kazhdan-Lusztig
- graded-algebra
---

# Degreewise quotient defects of a subspace inclusion

Fix ambient homogeneous pieces \(M_n\) and subspaces \(S,T\subseteq M\). Write
\[
S_n=S\cap M_n,\qquad T_n=T\cap M_n.
\]
The source's degree-\(n\) defect space is
\[
D_n=T_n/(S_n\cap T_n),
\]
where the denominator is viewed as a subspace of \(T_n\).

For an inclusion \(S\subseteq T\), this simplifies to
\[
D_n=T_n/S_n.
\]
When \(S,T\) are homogeneous, these are the degree pieces of the quotient \(T/S\).

## Weighted defect terms

For finite-dimensional pieces and a positive real parameter \(q\), define
\[
\operatorname{defectTerm}(S,T;q,n)=\dim_k(D_n)q^n.
\]
The dimension is a nonnegative integer, and \(q^n>0\). A nonzero defect space therefore gives a strictly positive term.

For \(S\subseteq T\), the finite-dimensional quotient formula gives
\[
\dim_kD_n=\dim_kT_n-\dim_kS_n.
\]
The [[node:kl.sheaves.hilbert_detection|defect theorem]] proves convergence of its weighted series from convergence of the larger Hilbert series, then identifies
\[
\sum_n\dim_kD_nq^n=H_T(q)-H_S(q).
\]

## A defect concentrated in degree zero

Let \(A=k[X,Y]\), \(T=A\), and \(S=(X,Y)\). Every positive-degree monomial belongs to \(S\), while the constant \(1\) does not. Hence
\[
D_0=k,\qquad D_n=0\quad(n\ne0).
\]
The defect value is one at every positive \(q\).

The Hilbert values are
\[
H_T(q)=\frac1{(1-q)^2},\qquad
H_S(q)=\frac1{(1-q)^2}-1
\quad(0<q<1).
\]
This example records exactly the missing constant component.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Hilbert.defectPiece`: [ModuleAlgebra.lean:571](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L571).

`OAI.KLInvariance.Hilbert.defectTerm`: [ModuleAlgebra.lean:574](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L574).
