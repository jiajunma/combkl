---
id: kl.definitions.hecke_operators
title: Left and right Hecke operators
kind: definition
status: formalized
primary_topic: kl.01_introduction
topics:
- kl.01_introduction
uses:
- kl.foundations.bruhat_order
lean:
  repository: openai-kl
  modules:
  - Hecke
  declarations:
  - OAI.KLInvariance.Hecke.left
  - OAI.KLInvariance.Hecke.right
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:39
    format: lean-location
    note: OAI.KLInvariance.Hecke.left
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:44
    format: lean-location
    note: OAI.KLInvariance.Hecke.right
  - artifact: openai-kl-paper
    locator: 1. Introduction and conventions; sec:introduction
    format: section
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does this definition retain the implemented conventions?
  verdict: Normalized and unnormalized parameters, operators, and semilinearity are
    distinguished explicitly.
tags:
- Kazhdan-Lusztig
- definitions
- Hecke
---

# Left and right Hecke operators

Let \(C\) be a commutative ring, let \(a\in C\), and let
\[
\mathcal H_C=\bigoplus_{w\in W} C H_w
\]
be the free module with standard basis indexed by the Coxeter group. A left Hecke operator \(L_s\), for \(s\in S\), is the \(C\)-linear map determined by
\[
L_s(H_w)=
\begin{cases}
H_{sw},&\ell(sw)>\ell(w),\\
H_{sw}+aH_w,&\ell(sw)<\ell(w).
\end{cases}
\]
The right Hecke operator \(R_s\) is defined by replacing \(sw\) with \(ws\).

An operator here is a linear endomorphism of \(\mathcal H_C\). The formula on basis vectors determines it on every vector by linearity. The simple generator \(s\) is a group element; \(L_s\) is the associated linear operator. Their squares obey different formulas.

For instance, on the pair \(H_1,H_s\), the matrix of \(L_s\) is
\[
\begin{pmatrix}0&1\\1&a\end{pmatrix}.
\]
The two possible length comparisons give its two columns. This model is the regular-action description of the Hecke algebra used by the implementation.

The usual normalized parameter is \(a=v-v^{-1}\). The unnormalized operators on the basis \(T_w\) use \(q\) and have descent rule \(T_sT_w=qT_{sw}+(q-1)T_w\).

## References

[Paper conventions](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L215).

## Lean formalization

`OAI.KLInvariance.Hecke.left`: [Hecke.lean:39](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L39).

`OAI.KLInvariance.Hecke.right`: [Hecke.lean:44](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L44).
