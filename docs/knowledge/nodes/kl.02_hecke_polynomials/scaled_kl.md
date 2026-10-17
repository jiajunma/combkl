---
id: kl.foundations.scaled_kl
title: Normalized KL reciprocity in the square parameter
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.foundations.rtilde
- kl.foundations.normalized_kl
lean:
  repository: openai-kl
  modules:
  - Dihedral
  declarations:
  - OAI.KLInvariance.scaledKL
  - OAI.KLInvariance.scaledKL_reciprocity
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:730
    format: lean-location
    note: OAI.KLInvariance.scaledKL
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:790
    format: lean-location
    note: OAI.KLInvariance.scaledKL_reciprocity
  - artifact: openai-kl-paper
    locator: 1. Introduction and conventions; sec:introduction
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- introduction
---

# Normalized KL reciprocity in the square parameter

For a nonzero field element \(t\), define
\[
p_x(t)=t^{\ell(x)-\ell(b)}P_{x,b}(t^2).
\]
Then
\[
p_x(t)=\sum_{z\in[x,b]}
 \widetilde R_{x,z}(t^{-1}-t)\,p_z(t^{-1}).
\]
Over the real interval \(0<t<1\), the common transfer coefficient is \(T=t^{-1}-t>0\).

*Proof.*

Evaluate KL reciprocity at \(t^2\), substitute [[node:kl.foundations.rtilde]], and combine the length exponents. This first gives the identity with the reciprocal parameter; replacing \(t\) by \(t^{-1}\) gives the displayed formula.

## References

[1. Introduction and conventions](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization

`OAI.KLInvariance.scaledKL`: [Dihedral.lean:730](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L730).

`OAI.KLInvariance.scaledKL_reciprocity`: [Dihedral.lean:790](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L790).
