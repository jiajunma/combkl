---
id: kl.foundations.finite_support
title: Finite generator support of a lower Bruhat ideal
kind: theorem
status: proved
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.foundations.subword
lean:
  repository: openai-kl
  modules:
  - Bruhat
  declarations:
  - OAI.KLInvariance.lower_ideal_finite_generator_support
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:452
    format: lean-location
    note: OAI.KLInvariance.lower_ideal_finite_generator_support
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

# Finite generator support of a lower Bruhat ideal

For every \(b\in W\), there is a finite subset \(J\subseteq S\) such that every \(x\le b\) is a product of generators from \(J\).

*Proof.*

### Step 1. Choose the generator set from one reduced word

Choose a reduced expression \(b=s_1\cdots s_n\), and let
\(J=\{s_i:1\le i\le n\}\).
This is a finite set, regardless of the size of the ambient simple-generator set. Repetitions in the word do not create additional elements of \(J\).

### Step 2. Treat an arbitrary lower element using the same set

Take any \(x\le b\). The fixed-word version of the subword criterion provides a reduced expression for \(x\) obtained by retaining selected positions of this same word for \(b\). Every retained letter therefore belongs to \(J\).

Thus, for every \(x\le b\), there is a word in the alphabet \(J\) whose product is \(x\). The set \(J\) was chosen before \(x\); it works simultaneously for the whole lower ideal.

## Notes

This proves the finite-generator-support assertion. It does not yet identify the canonical polynomials in the parabolic subgroup with the ambient ones. That additional transport is established in [[node:kl.main.finite_model_transport]] from the parabolic recursions. Keeping the two assertions separate prevents using combinatorial invariance in its own reduction.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.lower_ideal_finite_generator_support`: [Bruhat.lean:452](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L452).
