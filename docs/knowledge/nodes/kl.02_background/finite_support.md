---
id: "kl.foundations.finite_support"
title: "Finite generator support of a lower Bruhat ideal"
kind: "theorem"
status: "proved"
primary_topic: "kl.02_background"
topics: ["kl.02_background"]
uses: ["kl.foundations.subword"]
lean: {"repository":"openai-kl","modules":["Bruhat"],"declarations":["OAI.KLInvariance.lower_ideal_finite_generator_support"]}
source: {"spans":[{"artifact":"openai-kl-source","locator":"OAI.RepresentationTheory.KazhdanLusztig.Bruhat:452","format":"lean-location","note":"OAI.KLInvariance.lower_ideal_finite_generator_support"},{"artifact":"openai-kl-paper","locator":"2. Real realizations and moment-graph sheaves; sec:background","format":"section","note":"Chapter organization follows the paper; Lean references identify the precise formal statements."}]}
verification: {"statement":"accepted","proof":"accepted","alignment":"aligned"}
generality: {"reviewed":true,"prompt":"Does the exposition preserve the mathematical scope of its Lean declarations?","verdict":"The stated hypotheses and conclusion follow the fixed source; explanatory derivations retain the original proof route."}
tags: ["Kazhdan-Lusztig","background"]
---

# Finite generator support of a lower Bruhat ideal

For every \(b\in W\), there is a finite subset \(J\subseteq S\) such that every \(x\le b\) is a product of generators from \(J\).

*Proof.*

Choose a reduced expression \(\omega\) for \(b\), and let \(J\) be the set of its letters. By [[node:kl.foundations.subword]], every \(x\le b\) has a reduced expression that is a subword of \(\omega\). Every letter of that expression belongs to \(J\).

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.lower_ideal_finite_generator_support`: [Bruhat.lean:452](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L452).
