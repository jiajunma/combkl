---
id: kl.notes.hecke_action
title: Hecke operators, the bar map, and normalized R-polynomials
kind: concept
status: formalized
primary_topic: kl.01_introduction
topics:
- kl.01_introduction
uses:
- kl.foundations.bruhat_order
- kl.definitions.hecke_operators
- kl.definitions.hecke_quadratic_relation
- kl.definitions.bar_involution
lean:
  repository: openai-kl
  modules:
  - Hecke
  declarations:
  - OAI.KLInvariance.Hecke.left
  - OAI.KLInvariance.Hecke.left_quadratic
  - OAI.KLInvariance.Hecke.barLinear_left
  - OAI.KLInvariance.Hecke.rTilde
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:39
    format: lean-location
    note: OAI.KLInvariance.Hecke.left
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:83
    format: lean-location
    note: OAI.KLInvariance.Hecke.left_quadratic
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:348
    format: lean-location
    note: OAI.KLInvariance.Hecke.barLinear_left
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:482
    format: lean-location
    note: OAI.KLInvariance.Hecke.rTilde
  - artifact: openai-kl-paper
    locator: 1. Introduction and conventions; sec:introduction
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the mathematical hypotheses and scope retained from the referenced declarations?
  verdict: The exposition follows the fixed Lean source; worked calculations explain
    the constructions.
tags:
- Kazhdan-Lusztig
- introduction
---

# Hecke operators, the bar map, and normalized R-polynomials

Let \(C\) be a commutative coefficient ring and let \(a\in C\). On the free \(C\)-module with basis \(\{H_w:w\in W\}\), define the operator associated with a simple reflection \(s\) by
\[
H_sH_w=
\begin{cases}
H_{sw},&\ell(sw)>\ell(w),\\
H_{sw}+aH_w,&\ell(sw)<\ell(w).
\end{cases}
\]
There is a corresponding right operator, using \(ws\). The left and right operators commute. The quadratic relation is
\[
H_s^2=1+aH_s,\qquad H_s^{-1}=H_s-a.
\]
For the usual Laurent normalization, take \(a=v-v^{-1}\).

To see the quadratic relation directly, pair the two basis elements \(H_w,H_{sw}\), with \(\ell(sw)=\ell(w)+1\). The operator sends the first to the second and the second to the first plus \(a\) times the second. Its matrix on this pair is
\[
\begin{pmatrix}0&1\\1&a\end{pmatrix},
\]
whose square is the identity plus \(a\) times the matrix. The braid relations make products along reduced expressions independent of the chosen reduced word.

The bar construction uses inverse operators and changes \(a\) to \(-a\). In Laurent coefficients this is the familiar semilinearity \(v\mapsto v^{-1}\). Its coefficients are triangular for Bruhat order. The normalized R-polynomial \(\widetilde R_{x,y}(T)\) is the coefficient of \(H_x\) in the inverse-basis expression for \(H_y\), evaluated with parameter \(-T\).

For one simple reflection, \(H_s^{-1}=H_s-a\); substituting \(a=-T\) gives \(\widetilde R_{1,s}(T)=T\). Combining this with the square-parameter normalization gives \(R_{1,s}(q)=q-1\). This elementary case fixes the sign convention used in every later path and transfer formula.

## References

[1. Introduction and conventions](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization

`OAI.KLInvariance.Hecke.left`: [Hecke.lean:39](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L39).

`OAI.KLInvariance.Hecke.left_quadratic`: [Hecke.lean:83](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L83).

`OAI.KLInvariance.Hecke.barLinear_left`: [Hecke.lean:348](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L348).

`OAI.KLInvariance.Hecke.rTilde`: [Hecke.lean:482](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L482).
