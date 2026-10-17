---
id: kl.foundations.finite_intervals
title: Finiteness of Bruhat intervals
kind: theorem
status: proved
primary_topic: kl.01_bruhat_order
topics:
- kl.01_bruhat_order
uses:
- kl.foundations.interval
lean:
  repository: openai-kl
  modules:
  - Bruhat
  declarations:
  - OAI.KLInvariance.interval_finite
  - OAI.KLInvariance.finite_bruhat_lower
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:106
    format: lean-location
    note: OAI.KLInvariance.interval_finite
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:86
    format: lean-location
    note: OAI.KLInvariance.finite_bruhat_lower
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
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
- background
---

# Finiteness of Bruhat intervals

Every interval \([u,b]\) in an arbitrary Coxeter system is finite. The set of simple generators need not be finite.

*Proof.*

Choose a reduced expression for \(b\). Every incoming reflection edge is represented by a reflection in its finite left inversion sequence, so \(b\) has finitely many reflection predecessors.

Use strong induction on \(\ell(b)\). Every \(x\le b\) is either \(b\) itself or lies below a reflection predecessor \(z\) of \(b\). The lower ideal of \(b\) is therefore contained in a singleton together with finitely many lower ideals of shorter elements. Induction makes this union finite. The interval \([u,b]\) is a subset of that lower ideal.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.interval_finite`: [Bruhat.lean:106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L106).

`OAI.KLInvariance.finite_bruhat_lower`: [Bruhat.lean:86](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L86).
