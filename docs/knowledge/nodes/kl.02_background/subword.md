---
id: "kl.foundations.subword"
title: "The reduced-subword criterion"
kind: "theorem"
status: "proved"
primary_topic: "kl.02_background"
topics: ["kl.02_background"]
uses: ["kl.foundations.bruhat_order"]
lean: {"repository":"openai-kl","modules":["Bruhat"],"declarations":["OAI.KLInvariance.bruhat_iff_reduced_subword"]}
source: {"spans":[{"artifact":"openai-kl-source","locator":"OAI.RepresentationTheory.KazhdanLusztig.Bruhat:439","format":"lean-location","note":"OAI.KLInvariance.bruhat_iff_reduced_subword"},{"artifact":"openai-kl-paper","locator":"2. Real realizations and moment-graph sheaves; sec:background","format":"section","note":"Chapter organization follows the paper; Lean references identify the precise formal statements."}]}
verification: {"statement":"accepted","proof":"accepted","alignment":"aligned"}
generality: {"reviewed":true,"prompt":"Does the exposition preserve the mathematical scope of its Lean declarations?","verdict":"The stated hypotheses and conclusion follow the fixed source; explanatory derivations retain the original proof route."}
tags: ["Kazhdan-Lusztig","background"]
---

# The reduced-subword criterion

Fix any reduced expression \(\omega\) for \(y\). Then \(x\le y\) if and only if \(\omega\) has a reduced subword, with the original order of letters retained, whose product is \(x\).

*Proof.*

For the forward implication, first consider one downward reflection step. Strong exchange deletes a position from the chosen reduced word; a reduced subword of the resulting word represents the lower endpoint. Induction along a Bruhat path gives the assertion for arbitrary \(x\le y\).

For the converse, induct on the length of the top word. Distinguish whether the chosen subword contains its first simple generator. The monotonicity of the upper simple-lifting operation and the lifting relations place the subword product below the top element in both cases.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.bruhat_iff_reduced_subword`: [Bruhat.lean:439](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L439).
