---
id: "kl.sheaves.graph_sheaf"
title: "Sheaves on ordered graphs and compatible sections"
kind: "definition"
status: "formalized"
primary_topic: "kl.02_background"
topics: ["kl.02_background"]
uses: []
lean: {"repository":"openai-kl","modules":["Sheaves"],"declarations":["OAI.KLInvariance.MomentGraph.OrderedGraph","OAI.KLInvariance.MomentGraph.Sheaf","OAI.KLInvariance.MomentGraph.Sheaf.CompatibleOn"]}
source: {"spans":[{"artifact":"openai-kl-source","locator":"OAI.RepresentationTheory.KazhdanLusztig.Sheaves:21","format":"lean-location","note":"OAI.KLInvariance.MomentGraph.OrderedGraph"},{"artifact":"openai-kl-source","locator":"OAI.RepresentationTheory.KazhdanLusztig.Sheaves:28","format":"lean-location","note":"OAI.KLInvariance.MomentGraph.Sheaf"},{"artifact":"openai-kl-source","locator":"OAI.RepresentationTheory.KazhdanLusztig.Sheaves:41","format":"lean-location","note":"OAI.KLInvariance.MomentGraph.Sheaf.CompatibleOn"},{"artifact":"openai-kl-paper","locator":"2. Real realizations and moment-graph sheaves; sec:background","format":"section","note":"Chapter organization follows the paper; Lean references identify the precise formal statements."}]}
verification: {"definition":"accepted","proof":"not_applicable","alignment":"aligned"}
generality: {"reviewed":true,"prompt":"Does the exposition preserve the mathematical scope of its Lean declarations?","verdict":"The stated hypotheses and conclusion follow the fixed source; explanatory derivations retain the original proof route."}
tags: ["Kazhdan-Lusztig","background"]
---

# Sheaves on ordered graphs and compatible sections

Let \(V\) be a partially ordered set and \(E\) a set of edges. An ordered graph specifies a source \(s(e)\) and target \(t(e)\) for each edge, with \(s(e)<t(e)\).

A sheaf \(B\) over a commutative ring \(A\) consists of vertex modules \(B^x\), edge modules \(B^e\), and linear restriction maps
\[
\rho_{s,e}:B^{s(e)}\to B^e,\qquad
\rho_{t,e}:B^{t(e)}\to B^e.
\]
A compatible section on a vertex subset \(\Omega\) is an assignment \((v_x)\) satisfying
\[
\rho_{s,e}(v_{s(e)})=\rho_{t,e}(v_{t(e)})
\]
for every edge whose two endpoints lie in \(\Omega\).

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

The graph fields are `source`, `target`, and `increasing`. The sheaf fields are `vertex`, `edge`, `lower`, and `upper`. `CompatibleOn` tests edges with both endpoints in the specified subset.

`OAI.KLInvariance.MomentGraph.OrderedGraph`: [Sheaves.lean:21](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L21).

`OAI.KLInvariance.MomentGraph.Sheaf`: [Sheaves.lean:28](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L28).

`OAI.KLInvariance.MomentGraph.Sheaf.CompatibleOn`: [Sheaves.lean:41](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L41).
