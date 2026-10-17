---
id: "kl.sheaves.graded_module"
title: "Finite nonnegatively graded modules"
kind: "definition"
status: "formalized"
primary_topic: "kl.02_background"
topics: ["kl.02_background"]
uses: []
lean: {"repository":"openai-kl","modules":["GradedModules"],"declarations":["OAI.KLInvariance.Graded.ModuleData"]}
source: {"spans":[{"artifact":"openai-kl-source","locator":"OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1051","format":"lean-location","note":"OAI.KLInvariance.Graded.ModuleData"},{"artifact":"openai-kl-paper","locator":"2. Real realizations and moment-graph sheaves; sec:background","format":"section","note":"Chapter organization follows the paper; Lean references identify the precise formal statements."}]}
verification: {"definition":"accepted","proof":"not_applicable","alignment":"aligned"}
generality: {"reviewed":true,"prompt":"Does the exposition preserve the mathematical scope of its Lean declarations?","verdict":"The stated hypotheses and conclusion follow the fixed source; explanatory derivations retain the original proof route."}
tags: ["Kazhdan-Lusztig","background"]
---

# Finite nonnegatively graded modules

Let \(k\) be a field and \(A\) an integer-graded commutative \(k\)-algebra. The graded module data consist of a finitely generated \(A\)-module \(M\), a compatible \(k\)-vector space structure, and a decomposition
\[
M=\bigoplus_{n\in\mathbb Z}M_n
\]
into \(k\)-subspaces. The conditions are \(A_iM_j\subseteq M_{i+j}\) and \(M_n=0\) for \(n<0\).

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

The fields `obj`, `kModule`, `tower`, `piece`, `decomposition`, `graded`, `nonneg`, and `finite` record the underlying module, scalar structures and their compatibility, graded pieces, direct-sum decomposition, graded multiplication, nonnegativity, and finite generation.

`OAI.KLInvariance.Graded.ModuleData`: [GradedModules.lean:1051](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1051).
