---
id: kl.definitions.hecke_operators
title: The standard module and its left and right Hecke operators
kind: definition
status: formalized
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.coxeter.word_data
lean:
  repository: openai-kl
  modules:
  - Hecke
  declarations:
  - OAI.KLInvariance.Hecke.Space
  - OAI.KLInvariance.Hecke.basis
  - OAI.KLInvariance.Hecke.left
  - OAI.KLInvariance.Hecke.right
  - OAI.KLInvariance.HeckeQ.left
  - OAI.KLInvariance.HeckeQ.right
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:24
    format: lean-location
    note: OAI.KLInvariance.Hecke.Space
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:26
    format: lean-location
    note: OAI.KLInvariance.Hecke.basis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:39
    format: lean-location
    note: OAI.KLInvariance.Hecke.left
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:44
    format: lean-location
    note: OAI.KLInvariance.Hecke.right
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:514
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.left
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:521
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.right
  - artifact: openai-kl-paper
    locator: 1. Introduction and conventions; sec:introduction
    format: section
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual coefficient hypotheses, conventions and source proof retained?
  verdict: Read Space/basis and both left/right definitions. The finite-support description,
    both descent tables and Laurent rescaling retain the actual conventions.
tags:
- Kazhdan-Lusztig
- Hecke
---

# The standard module and its left and right Hecke operators

Fix a Coxeter system \((W,S)\) and a commutative ring \(C\). The standard module is
\[
\mathcal H_C=\bigoplus_{w\in W}Ce_w.
\]
A vector is a function \(f:W\to C\) with finite support, written \(\sum_w f(w)e_w\). Its coefficient at \(w\) is \(f(w)\); \(e_w\) has coefficient one at \(w\) and zero elsewhere. This is the source's finitely supported function type.

An operator is a \(C\)-linear map from this module to itself. Specifying its values on the \(e_w\) defines it on a general vector by
\[
L\left(\sum_w f(w)e_w\right)=\sum_w f(w)L(e_w).
\]
The sum is finite even when \(W\) is infinite.

## The normalized convention

For \(a\in C\), use the basis notation \(H_w=e_w\). The left operator is
\[
L_s(a)H_w=
\begin{cases}
H_{sw},&\ell(sw)>\ell(w),\\
H_{sw}+aH_w,&\ell(sw)<\ell(w).
\end{cases}
\]
The right operator \(D_t(a)\) uses \(wt\) in place of \(sw\). Simple multiplication changes length by exactly one, so these two cases exhaust the possibilities.

The symbols \(L_s,D_t\) name operators; \(H_w\) names a vector. The expression \(H_sH_w\) abbreviates the left operator value in the regular-action notation.

On a pair \(H_w,H_{sw}\) with \(\ell(sw)=\ell(w)+1\), the matrix is
\[
\begin{pmatrix}0&1\\1&a\end{pmatrix}.
\]
The first column says \(H_w\mapsto H_{sw}\); the second says \(H_{sw}\mapsto H_w+aH_{sw}\).

## The unnormalized convention

For \(q\in C\), write \(T_w=e_w\) and use
\[
L_s(q)T_w=
\begin{cases}
T_{sw},&\ell(sw)>\ell(w),\\
qT_{sw}+(q-1)T_w,&\ell(sw)<\ell(w).
\end{cases}
\]
Again \(D_t(q)\) is the right version. On an ascent pair its matrix is
\[
\begin{pmatrix}0&q\\1&q-1\end{pmatrix}.
\]
These operators are defined for every \(q\). Their inverse construction uses an invertible \(q\).

## Conversion over Laurent coefficients

Take \(q=v^2\) with \(v\) invertible, and set \(H_w=v^{-\ell(w)}T_w\). The operator \(v^{-1}L_s(q)\) then has normalized parameter \(a=v-v^{-1}\).

In an ascent, \(v^{-1-\ell(w)}T_{sw}=H_{sw}\). In a descent, \(\ell(sw)=\ell(w)-1\), so
\[
v^{-1-\ell(w)}\bigl(v^2T_{sw}+(v^2-1)T_w\bigr)
=H_{sw}+(v-v^{-1})H_w.
\]
Thus the two tables describe the two coefficient conventions used in the source. Later formulas specify which parameter and basis are being used.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Hecke.Space`: [Hecke.lean:24](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L24).

`OAI.KLInvariance.Hecke.basis`: [Hecke.lean:26](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L26).

`OAI.KLInvariance.Hecke.left`: [Hecke.lean:39](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L39).

`OAI.KLInvariance.Hecke.right`: [Hecke.lean:44](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L44).

`OAI.KLInvariance.HeckeQ.left`: [Hecke.lean:514](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L514).

`OAI.KLInvariance.HeckeQ.right`: [Hecke.lean:521](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L521).
