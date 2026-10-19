---
id: kl.hecke.r_values
title: R-values extracted from the unnormalized bar basis
kind: definition
status: formalized
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.definitions.bar_involution
- kl.hecke.bar_triangularity
lean:
  repository: openai-kl
  modules:
  - Hecke
  declarations:
  - OAI.KLInvariance.HeckeQ.rValue
  - OAI.KLInvariance.HeckeQ.rValue_diagonal
  - OAI.KLInvariance.HeckeQ.rValue_zero
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:986
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.rValue
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:989
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.rValue_diagonal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:994
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.rValue_zero
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual coefficient hypotheses, conventions and source proof retained?
  verdict: Read rValue and its diagonal/support lemmas. Retained the exact sign and
    top-power normalization and separated ring-valued coefficients from ordinary integral
    polynomials.
tags:
- Kazhdan-Lusztig
- Hecke
---

# R-values extracted from the unnormalized bar basis

Let \(C\) be a commutative ring and \(q\in C^\times\). Let \(b_y(q)(x)\) denote the \(T_x\)-coefficient of the unnormalized inverse-basis vector \(b_y(q)\). Define
\[
r_q(x,y)=(-1)^{\ell(x)}(-q)^{\ell(y)}b_y(q)(x).
\]
This is the source's R-value at the unit parameter \(q\). It is an element of \(C\); the ordinary integral polynomial will be constructed by taking \(q\) to be a Laurent indeterminate.

## Diagonal and support

The [[node:kl.hecke.bar_triangularity|bar diagonal]] gives \(b_x(q)(x)=q^{-\ell(x)}\), so
\[
r_q(x,x)
=(-1)^{\ell(x)}(-q)^{\ell(x)}q^{-\ell(x)}
=\bigl((-1)(-q)q^{-1}\bigr)^{\ell(x)}=1.
\]
If \(x\not\le y\), [[node:kl.hecke.bar_triangularity|bar triangularity]] gives \(r_q(x,y)=0\).

## The simple-reflection value

Since
\[
b_s(q)=q^{-1}T_s+(q^{-1}-1)T_1,
\]
the off-diagonal normalization gives
\[
r_q(1,s)=(-q)(q^{-1}-1)=q-1,
\]
and the diagonal gives \(r_q(s,s)=1\).

The sign and top power in the definition are chosen in the source before the recurrence is proved. The recurrence theorem derives the coefficients \(q-1\) and \(q\) from the inverse-operator coefficient formula.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.HeckeQ.rValue`: [Hecke.lean:986](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L986).

`OAI.KLInvariance.HeckeQ.rValue_diagonal`: [Hecke.lean:989](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L989).

`OAI.KLInvariance.HeckeQ.rValue_zero`: [Hecke.lean:994](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L994).
