---
id: "kl.comparison.reciprocal_rigidity"
title: "Rigidity below the middle degree"
kind: "theorem"
status: "proved"
primary_topic: "kl.06_induction"
topics: ["kl.06_induction"]
uses: []
lean: {"repository":"openai-kl","modules":["Comparison"],"declarations":["OAI.KLInvariance.Comparison.low_degree_zero_of_eval_reciprocal","OAI.KLInvariance.Comparison.eq_of_eval_difference_reciprocal"]}
source: {"spans":[{"artifact":"openai-kl-source","locator":"OAI.RepresentationTheory.KazhdanLusztig.Comparison:24","format":"lean-location","note":"OAI.KLInvariance.Comparison.low_degree_zero_of_eval_reciprocal"},{"artifact":"openai-kl-source","locator":"OAI.RepresentationTheory.KazhdanLusztig.Comparison:50","format":"lean-location","note":"OAI.KLInvariance.Comparison.eq_of_eval_difference_reciprocal"},{"artifact":"openai-kl-paper","locator":"6. Reciprocity and simultaneous induction; sec:induction","format":"section","note":"Chapter organization follows the paper; Lean references identify the precise formal statements."}]}
verification: {"statement":"accepted","proof":"accepted","alignment":"aligned"}
generality: {"reviewed":true,"prompt":"Does the exposition preserve the mathematical scope of its Lean declarations?","verdict":"The stated hypotheses and conclusion follow the fixed source; explanatory derivations retain the original proof route."}
tags: ["Kazhdan-Lusztig","induction"]
---

# Rigidity below the middle degree

Let \(f\in\mathbb R[q]\) with \(2\deg f<d\). If
\[
f(q)=q^d f(q^{-1})\qquad(0<q<1),
\]
then \(f=0\). Consequently, two integral polynomials satisfying the strict half-degree bound are equal if their difference obeys this reciprocal identity.

*Proof.*

Equality at infinitely many points of an open interval identifies \(f\) with its \(d\)-reflection. If \(f\ne0\), compare its highest nonzero coefficient: reflection matches it with a coefficient strictly above the original degree, which must vanish. This is a contradiction.

For two integral polynomials, apply the result to their difference after mapping to real coefficients, then use injectivity of the coefficient embedding.

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.Comparison.low_degree_zero_of_eval_reciprocal`: [Comparison.lean:24](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L24).

`OAI.KLInvariance.Comparison.eq_of_eval_difference_reciprocal`: [Comparison.lean:50](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L50).
