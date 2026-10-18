---
id: kl.detail.graph_transport
title: Graph maps, graph equivalences, and sheaf pullback
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.ordered_graph
- kl.sheaves.graph_sheaf
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  - GradedSheaves
  declarations:
  - OAI.KLInvariance.MomentGraph.GraphMap
  - OAI.KLInvariance.MomentGraph.GraphEquiv
  - OAI.KLInvariance.MomentGraph.Sheaf.pullback
  - OAI.KLInvariance.MomentGraph.GradedSheaf.reindex
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1457
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GraphMap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:270
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GraphEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1473
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.pullback
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:279
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.reindex
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# Graph maps, graph equivalences, and sheaf pullback

For directed ordered graphs \(G,H\), a graph map consists of a vertex map \(f_V\) and an edge map \(f_E\) preserving both endpoints:
\[
f_V(s_G(e))=s_H(f_E(e)),\qquad
f_V(t_G(e))=t_H(f_E(e)).
\]
A graph equivalence requires both maps to be bijections. The data preserve directed incidence; an order-preservation condition on all vertex comparisons is specified separately when needed.

Given a sheaf \(B\) on \(H\), its pullback has stalk \(B^{f_V(x)}\) at \(x\) and edge module \(B^{f_E(e)}\) at \(e\). Its two restriction maps are the original restriction maps with endpoints identified by the displayed equations. An assignment pulls back by \((f^*m)_x=m_{f_V(x)}\); compatibility follows on each mapped edge. A graph equivalence gives reindexing, with an inverse reindexing.

Freeness and quotient formulas transport directly at the indicated stalks and edges. Extension statements involving upper sets use the order or outgoing-edge hypotheses stated in the corresponding theorem.

## References

The precise Lean sources are listed below.

## Lean formalization

For both structures, `vertex` and `edge` are the two maps, while `source` and `target` are their incidence-preservation conditions.

`OAI.KLInvariance.MomentGraph.GraphMap`: [MinimalExtensions.lean:1457](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1457).

`OAI.KLInvariance.MomentGraph.GraphEquiv`: [GradedSheaves.lean:270](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L270).

`OAI.KLInvariance.MomentGraph.Sheaf.pullback`: [MinimalExtensions.lean:1473](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1473).

`OAI.KLInvariance.MomentGraph.GradedSheaf.reindex`: [GradedSheaves.lean:279](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L279).
