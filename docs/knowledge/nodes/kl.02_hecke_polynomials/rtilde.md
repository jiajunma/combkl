---
id: kl.foundations.rtilde
title: Normalized R-polynomials and the square parameter
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.foundations.canonical_kl
- kl.notes.hecke_action
- kl.detail.rtilde_family
- kl.detail.rtilde_recursion
lean:
  repository: openai-kl
  modules:
  - Hecke
  - Dihedral
  declarations:
  - OAI.KLInvariance.Hecke.rTilde
  - OAI.KLInvariance.rPolynomial_normalization
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:482
    format: lean-location
    note: OAI.KLInvariance.Hecke.rTilde
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:676
    format: lean-location
    note: OAI.KLInvariance.rPolynomial_normalization
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

# Normalized R-polynomials and the square parameter

The normalized polynomial \(\widetilde R_{x,y}(T)\) is constructed from coefficients of the Hecke bar action. For every nonzero element \(v\) of a field,
\[
R_{x,y}(v^2)=v^{\ell(y)-\ell(x)}
 \widetilde R_{x,y}(v-v^{-1}).
\]

*Proof.*

The two polynomial constructions satisfy their respective simple-reflection recursions. Induct on the length of the upper endpoint, handling diagonal pairs, incomparable pairs, and a simple descent of the upper endpoint. Substitute \(q=v^2\) in the ordinary \(R\)-recursion and compare the two branches. Integer exponents allow the identity to include incomparable pairs.

## References

[1. Introduction and conventions](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization

`OAI.KLInvariance.Hecke.rTilde`: [Hecke.lean:482](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L482).

`OAI.KLInvariance.rPolynomial_normalization`: [Dihedral.lean:676](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L676).
