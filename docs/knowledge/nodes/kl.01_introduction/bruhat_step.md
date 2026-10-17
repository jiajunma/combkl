---
id: "kl.foundations.bruhat_step"
title: "Upward reflection edges"
kind: "definition"
status: "formalized"
primary_topic: "kl.01_introduction"
topics: ["kl.01_introduction"]
uses: []
lean: {"repository":"openai-kl","modules":["Model"],"declarations":["OAI.KLInvariance.BruhatStep"]}
source: {"spans":[{"artifact":"openai-kl-source","locator":"OAI.RepresentationTheory.KazhdanLusztig.Model:14","format":"lean-location","note":"OAI.KLInvariance.BruhatStep"},{"artifact":"openai-kl-paper","locator":"1. Introduction and conventions; sec:introduction","format":"section","note":"Chapter organization follows the paper; Lean references identify the precise formal statements."}]}
verification: {"definition":"accepted","proof":"not_applicable","alignment":"aligned"}
generality: {"reviewed":true,"prompt":"Does the exposition preserve the mathematical scope of its Lean declarations?","verdict":"The stated hypotheses and conclusion follow the fixed source; explanatory derivations retain the original proof route."}
tags: ["Kazhdan-Lusztig","introduction"]
---

# Upward reflection edges

Let \((W,S)\) be a Coxeter system with length function \(\ell\). An upward reflection edge is a pair \(x,y\in W\) such that
\[
x\longrightarrow y
\quad\Longleftrightarrow\quad
\ell(x)<\ell(y)\ \text{and}\ y=tx
\text{ for some reflection }t.
\]
Reflections act on the left. An edge may cross several ranks; it need not be a cover.

## References

[1. Introduction and conventions](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization

`OAI.KLInvariance.BruhatStep`: [Model.lean:14](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Model.lean#L14).
