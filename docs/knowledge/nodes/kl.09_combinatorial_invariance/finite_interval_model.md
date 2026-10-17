---
id: kl.main.finite_interval_model
title: Finite-support interval models in standard parabolic systems
kind: definition
status: formalized
primary_topic: kl.09_combinatorial_invariance
topics:
- kl.09_combinatorial_invariance
uses:
- kl.foundations.interval
- kl.foundations.finite_support
lean:
  repository: openai-kl
  modules:
  - Invariance
  declarations:
  - OAI.KLInvariance.FiniteIntervalModel
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Invariance:476
    format: lean-location
    note: OAI.KLInvariance.FiniteIntervalModel
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- background
---

# Finite-support interval models in standard parabolic systems

Fix an arbitrary Coxeter system and endpoints \(u,b\). A finite-support interval model consists of:

- a finite subset \(J\subseteq S\);
- two elements \(\bar u,\bar b\) of the standard parabolic Coxeter system defined by the restricted matrix on \(J\);
- equalities identifying their images under the standard inclusion with \(u,b\).

This places the interval in a finite-generator system without requiring that parabolic group to be finite.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

The fields are `indices`, `finite`, `lower`, `upper`, `lower_eq`, and `upper_eq`.

`OAI.KLInvariance.FiniteIntervalModel`: [Invariance.lean:476](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L476).
