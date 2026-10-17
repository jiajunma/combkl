---
id: kl.definitions.hecke_quadratic_relation
title: The quadratic relation for a Hecke generator
kind: definition
status: formalized
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.definitions.hecke_operators
lean:
  repository: openai-kl
  modules:
  - Hecke
  declarations:
  - OAI.KLInvariance.Hecke.left_quadratic
  - OAI.KLInvariance.HeckeQ.left_quadratic
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:83
    format: lean-location
    note: OAI.KLInvariance.Hecke.left_quadratic
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:569
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.left_quadratic
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

# The quadratic relation for a Hecke generator

The normalized Hecke quadratic relation is the operator identity
\[
L_s^2=I+aL_s.
\]
It says that \(L_s\) satisfies the degree-two polynomial \(X^2-aX-1\). It also gives the inverse formula
\[
L_s^{-1}=L_s-aI.
\]

To derive it, take \(w\) with \(\ell(sw)=\ell(w)+1\). On the span of \(H_w,H_{sw}\), the operator matrix is \(\begin{pmatrix}0&1\\1&a\end{pmatrix}\). Squaring it gives the identity plus \(a\) times the original matrix. These pairs account for every basis vector.

In the unnormalized convention the relation is
\[
T_s^2=qI+(q-1)T_s,
\qquad (T_s+I)(T_s-qI)=0.
\]
Setting \(q=v^2\) and \(H_s=v^{-1}T_s\) converts it to
\(H_s^2=I+(v-v^{-1})H_s\).

This quadratic relation concerns one generator. The braid relations compare alternating products of two different generators; together, the two types of relation determine the Hecke multiplication.

## References

[Paper conventions](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L215).

## Lean formalization

`OAI.KLInvariance.Hecke.left_quadratic`: [Hecke.lean:83](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L83).

`OAI.KLInvariance.HeckeQ.left_quadratic`: [Hecke.lean:569](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L569).
