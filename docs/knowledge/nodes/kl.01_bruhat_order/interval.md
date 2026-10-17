---
id: kl.foundations.interval
title: Unlabelled Bruhat intervals and rank differences
kind: definition
status: formalized
primary_topic: kl.01_bruhat_order
topics:
- kl.01_bruhat_order
uses:
- kl.foundations.bruhat_order
lean:
  repository: openai-kl
  modules:
  - Model
  declarations:
  - OAI.KLInvariance.Interval
  - OAI.KLInvariance.rankDifference
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Model:22
    format: lean-location
    note: OAI.KLInvariance.Interval
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Model:45
    format: lean-location
    note: OAI.KLInvariance.rankDifference
  - artifact: openai-kl-paper
    locator: 1. Introduction and conventions; sec:introduction
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
- introduction
---

# Unlabelled Bruhat intervals and rank differences

For \(u,b\in W\), define
\[
[u,b]=\{x\in W:u\le x\le b\}
\]
with its induced strong Bruhat order. For comparable \(x\le y\), write
\[
d(x,y)=\ell(y)-\ell(x).
\]
An interval isomorphism is a bijection preserving and reflecting the order. Its data contain no group homomorphism, correspondence of simple generators, or correspondence of root labels.

## References

[1. Introduction and conventions](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization

`OAI.KLInvariance.Interval`: [Model.lean:22](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Model.lean#L22).

`OAI.KLInvariance.rankDifference`: [Model.lean:45](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Model.lean#L45).
