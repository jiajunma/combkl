---
id: kl.sheaves.graph_sheaf
title: Module-valued sheaves on an ordered graph
kind: definition
status: formalized
primary_topic: kl.04_moment_graph_sheaves
topics:
- kl.04_moment_graph_sheaves
uses:
- kl.detail.ordered_graph
lean:
  repository: openai-kl
  modules:
  - Sheaves
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Sheaves:28
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
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
- background
---

# Module-valued sheaves on an ordered graph

Fix an ordered graph \(G\) and a commutative coefficient ring \(A\).
A module-valued graph sheaf consists of vertex modules \(B^x\), edge modules \(B^e\),
and two \(A\)-linear restriction maps at each edge \(e:x\to y\):
\[
\rho_{x,e}:B^x\longrightarrow B^e,\qquad
\rho_{y,e}:B^y\longrightarrow B^e.
\]
No injectivity, surjectivity, freeness, or quotient presentation is included in
this definition. Each is an additional property to be established when needed.

The edge module is a common target in which the two stalk values can be
compared. A compatible section requires their images to agree. Flabbiness
concerns extending these compatible assignments, while global generation
concerns surjectivity of evaluation at a single stalk.

For a one-edge example with label \(\alpha\), take both stalks equal to \(A\),
the edge module equal to \(A/(\alpha)\), and both restrictions to be quotient
maps. Compatibility says that the stalk values differ by a multiple of
\(\alpha\). More complicated sheaves retain this same incidence pattern,
with higher-rank vertex modules and coupled boundary conditions.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

The graph fields are `source`, `target`, and `increasing`. The sheaf fields are `vertex`, `edge`, `lower`, and `upper`. `CompatibleOn` tests edges with both endpoints in the specified subset.

`OAI.KLInvariance.MomentGraph.OrderedGraph`: [Sheaves.lean:21](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L21).

`OAI.KLInvariance.MomentGraph.Sheaf`: [Sheaves.lean:28](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L28).

`OAI.KLInvariance.MomentGraph.Sheaf.CompatibleOn`: [Sheaves.lean:41](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L41).
