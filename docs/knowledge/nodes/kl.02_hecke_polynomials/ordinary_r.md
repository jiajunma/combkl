---
id: kl.detail.ordinary_r
title: The ordinary integral R-polynomial family
kind: definition
status: formalized
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.hecke.r_values
lean:
  repository: openai-kl
  modules:
  - OrdinaryR
  declarations:
  - OAI.KLInvariance.OrdinaryR.variableUnit
  - OAI.KLInvariance.OrdinaryR.polynomial
  - OAI.KLInvariance.OrdinaryR.toLaurent_polynomial
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.OrdinaryR:24
    format: lean-location
    note: OAI.KLInvariance.OrdinaryR.variableUnit
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.OrdinaryR:62
    format: lean-location
    note: OAI.KLInvariance.OrdinaryR.polynomial
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.OrdinaryR:65
    format: lean-location
    note: OAI.KLInvariance.OrdinaryR.toLaurent_polynomial
  - artifact: openai-kl-paper
    locator: Related paper context; sec:introduction
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual coefficient hypotheses, conventions and source proof retained?
  verdict: Read variableUnit, polynomial and toLaurent_polynomial. Defined Laurent
    coefficients and truncation, and kept polynomiality and evaluation as linked supporting
    theorems.
tags:
- Kazhdan-Lusztig
- Hecke
---

# The ordinary integral R-polynomial family

Let \(Q\) be the Laurent indeterminate in \(\mathbb Z[Q,Q^{-1}]\). A Laurent polynomial is a finite sum \(\sum_{n\in\mathbb Z}a_nQ^n\). The element \(Q\) is a unit with inverse \(Q^{-1}\), so the Hecke R-value \(r_Q(x,y)\) is defined.

The polynomiality theorem proves that every exponent occurring in \(r_Q(x,y)\) is nonnegative. Thus there is a unique polynomial
\[
R_{x,y}(q)\in\mathbb Z[q]
\]
whose Laurent image is \(r_Q(x,y)\). The source defines it by the truncation map retaining the nonnegative coefficients, after proving polynomiality. In symbols,
\[
R_{x,y}(Q)=r_Q(x,y).
\]
Uniqueness follows because the inclusion of polynomials into Laurent polynomials is injective: it retains every coefficient.

## Evaluation at a unit

For a commutative ring \(C\) and a unit \(q_0\in C\), evaluate integer coefficients through the canonical map \(\mathbb Z\to C\). The specialization theorem gives
\[
R_{x,y}(q_0)=r_{q_0}(x,y).
\]
The polynomial also has a well-defined value at nonunits, since polynomial evaluation uses only nonnegative powers. The inverse-operator description uses units.

## Initial values and recurrence

The source proves
\[
R_{x,x}=1,\qquad R_{x,y}=0\quad(x\not\le y),
\]
and, for any \(sy<y\),
\[
R_{x,y}=
\begin{cases}
R_{sx,sy},&sx<x,\\
(q-1)R_{x,sy}+qR_{sx,sy},&sx>x.
\end{cases}
\]
Polynomiality, specialization and this recurrence are developed together in the construction theorem. The separate degree theorem proves the bound by the length difference.

For distinct simple reflections \(s,t\), the reduced word \(st\) gives
\[
R_{1,st}=(q-1)R_{1,t}+qR_{s,t}=(q-1)^2.
\]
Here \(R_{s,t}=0\): comparable elements of the same length must be equal, and \(s\ne t\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.OrdinaryR.variableUnit`: [OrdinaryR.lean:24](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L24).

`OAI.KLInvariance.OrdinaryR.polynomial`: [OrdinaryR.lean:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L62).

`OAI.KLInvariance.OrdinaryR.toLaurent_polynomial`: [OrdinaryR.lean:65](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L65).
