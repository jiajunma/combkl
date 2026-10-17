---
id: kl.main.finite_model_transport
title: Existence and transport of finite-support interval models
kind: theorem
status: proved
primary_topic: kl.09_combinatorial_invariance
topics:
- kl.09_combinatorial_invariance
uses:
- kl.main.finite_interval_model
- kl.foundations.finite_support
- kl.foundations.canonical_kl
lean:
  repository: openai-kl
  modules:
  - Invariance
  declarations:
  - OAI.KLInvariance.exists_finiteIntervalModel
  - OAI.KLInvariance.FiniteIntervalModel.orderIso
  - OAI.KLInvariance.FiniteIntervalModel.kl_eq
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Invariance:484
    format: lean-location
    note: OAI.KLInvariance.exists_finiteIntervalModel
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Invariance:505
    format: lean-location
    note: OAI.KLInvariance.FiniteIntervalModel.orderIso
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Invariance:517
    format: lean-location
    note: OAI.KLInvariance.FiniteIntervalModel.kl_eq
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

# Existence and transport of finite-support interval models

For \(u\le b\), a [[node:kl.main.finite_interval_model]] exists. Its standard inclusion induces
\[
[\bar u,\bar b]\simeq[u,b],
\qquad
P_{\bar u,\bar b}=P_{u,b},
\]
and preserves the rank difference.

*Proof.*

Finite generator support gives words for \(u,b\) in a common finite set \(J\). Lift those words to the standard parabolic system. The inclusion preserves word products, yielding the endpoint equalities.

Standard parabolic inclusion preserves Bruhat intervals and length. The restricted polynomial families satisfy the same normalization conditions, so uniqueness preserves the KL polynomials. Rewrite these statements using the endpoint equalities of the model.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.exists_finiteIntervalModel`: [Invariance.lean:484](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L484).

`OAI.KLInvariance.FiniteIntervalModel.orderIso`: [Invariance.lean:505](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L505).

`OAI.KLInvariance.FiniteIntervalModel.kl_eq`: [Invariance.lean:517](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L517).
