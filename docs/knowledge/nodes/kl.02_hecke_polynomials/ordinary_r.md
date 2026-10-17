---
id: kl.detail.ordinary_r
title: The ordinary R-polynomial family
kind: definition
status: formalized
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.definitions.hecke_operators
- kl.definitions.bar_involution
- kl.foundations.bruhat_order
lean:
  repository: openai-kl
  modules:
  - OrdinaryR
  declarations:
  - OAI.KLInvariance.OrdinaryR.polynomial
  - OAI.KLInvariance.OrdinaryR.polynomial_recursion
  - OAI.KLInvariance.OrdinaryR.polynomial_degree
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.OrdinaryR:62
    format: lean-location
    note: OAI.KLInvariance.OrdinaryR.polynomial
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.OrdinaryR:80
    format: lean-location
    note: OAI.KLInvariance.OrdinaryR.polynomial_recursion
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.OrdinaryR:125
    format: lean-location
    note: OAI.KLInvariance.OrdinaryR.polynomial_degree
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
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- hecke_polynomials
---

# The ordinary R-polynomial family

For a Coxeter system, the ordinary R-polynomials \(R_{x,y}(q)\in\mathbb Z[q]\) are the integral polynomial coefficients obtained from the unnormalized Hecke bar action. They satisfy
\[
R_{x,x}=1,\qquad R_{x,y}=0\quad(x\not\leq y).
\]
If \(s\) is a simple reflection with \(sy<y\), then
\[
R_{x,y}=
\begin{cases}
R_{sx,sy},&sx<x,\\
(q-1)R_{x,sy}+qR_{sx,sy},&sx>x.
\end{cases}
\]
In particular \(R_{1,s}=q-1\). Their degrees satisfy \(\deg R_{x,y}\leq\ell(y)-\ell(x)\) for comparable endpoints.

The construction first takes coefficients over the Laurent polynomial ring, where the parameter is a unit. Induction on \(\ell(y)\) shows that these coefficients actually lie in its polynomial subring. Taking their polynomial representative therefore loses no terms; the recursion descends along the injective polynomial-to-Laurent map.

These are the ordinary \(R\)-polynomials. The normalized family \(\widetilde R\) uses a different variable and has a different descent recursion.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization



`OAI.KLInvariance.OrdinaryR.polynomial`: [OrdinaryR.lean:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L62).

`OAI.KLInvariance.OrdinaryR.polynomial_recursion`: [OrdinaryR.lean:80](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L80).

`OAI.KLInvariance.OrdinaryR.polynomial_degree`: [OrdinaryR.lean:125](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L125).
