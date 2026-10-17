---
id: kl.comparison.rtilde_step
title: The R-tilde induction step from smaller intervals
kind: theorem
status: proved
primary_topic: kl.09_combinatorial_invariance
topics:
- kl.09_combinatorial_invariance
uses:
- kl.comparison.rtilde_row_comparison
- kl.comparison.free_suffixes
- kl.foundations.rank_preservation
lean:
  repository: openai-kl
  modules:
  - Invariance
  declarations:
  - OAI.KLInvariance.BruhatGraph.rTilde_eq_of_smaller_data
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Invariance:95
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.rTilde_eq_of_smaller_data
  - artifact: openai-kl-paper
    locator: 6. Reciprocity and simultaneous induction; sec:induction
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
- induction
---

# The R-tilde induction step from smaller intervals

Consider isomorphic intervals in two finite-generator Coxeter systems. Suppose the shorter bottom-row R-tilde entries agree in both directions, and every strictly higher upper interval already has terminal-kernel freeness. Then
\[
\widetilde R_{u,b}=\widetilde R'_{u',b'}.
\]

*Proof.*

Transport the terminal-kernel freeness of the smaller upper intervals to the current upper endpoints. Apply [[node:kl.comparison.rtilde_row_comparison]] in each direction. The two polynomials agree at every \(t^{-1}-t\) with \(0<t<1\).

This parameter map is strictly monotone and has infinitely many values. Polynomial equality follows.

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.rTilde_eq_of_smaller_data`: [Invariance.lean:95](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L95).
