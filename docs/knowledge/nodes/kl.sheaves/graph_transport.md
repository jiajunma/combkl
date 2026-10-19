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
- kl.sheaves.flabbiness
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.GraphMap
  - OAI.KLInvariance.MomentGraph.GraphEquiv
  - OAI.KLInvariance.MomentGraph.Sheaf.pullback
  - OAI.KLInvariance.MomentGraph.GradedSheaf.pullback
  - OAI.KLInvariance.MomentGraph.GradedSheaf.reindex
  - OAI.KLInvariance.MomentGraph.GradedSheaf.reindex_edgeFlabby
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
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1650
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.pullback
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:279
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.reindex
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:336
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.reindex_edgeFlabby
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

For ordered graphs \(G\) and \(H\), a graph map consists of maps on vertices and edges,
\[
f_V:V_G\to V_H,\qquad f_E:E_G\to E_H,
\]
satisfying the two endpoint equations
\[
f_V(s_G(e))=s_H(f_E(e)),\qquad
f_V(t_G(e))=t_H(f_E(e)).
\]
A graph equivalence supplies bijections in place of these maps, with the same equations.

These data compare directed incidence. For example, on the chain \(0<1<2<3\) with only the edge \(0\to2\), exchanging the isolated vertices \(1,3\) and fixing the edge preserves incidence. The comparison \(1<2\) is sent to \(3>2\).

## Pulling back a sheaf

For a sheaf \(B\) on \(H\), its pullback has
\[
(f^*B)^x=B^{f_V(x)},\qquad
(f^*B)^e=B^{f_E(e)}.
\]
The restrictions are those of \(B\), with their endpoint modules identified by the two graph-map equations. If \(B\) is graded, these same modules and maps retain their gradings.

An assignment pulls back by
\[
(f^*m)_x=m_{f_V(x)}.
\]
On an edge \(e\), its compatibility equation is the original equation on \(f_E(e)\). Hence a global section pulls back to a global section. A prescribed stalk value can likewise be obtained by pulling back a section that generates the corresponding target stalk.

The label system pulls back as \(\alpha_G(e)=\alpha_H(f_E(e))\).

## Reindexing by a graph equivalence

If both graph maps are bijective, the inverse maps give an inverse reindexing of assignments. They identify compatible assignments on a vertex subset with compatible assignments on its image.

Free stalks and upper quotients transport componentwise. To transport edge flabbiness, take a subset closed under all source edges. Its vertex image is closed under all target edges, because every target edge has a source-edge preimage and the endpoint equations agree. Extend the corresponding assignment there, then pull the extension back.

The finite boundary-existence construction uses this incidence transport when it identifies a formally adjoined bottom vertex with the removed vertex of the original graph.

## Pullback with complete outgoing lifts

For a general graph map, the boundary-pullback theorem uses two additional conditions: \(f_V\) is injective, and every edge of \(H\) starting at \(f_V(x)\) is the image of an edge of \(G\) starting at \(x\).

These conditions make images of edge-closed subsets edge-closed and retain all outgoing kernel conditions. They are satisfied by the inclusion of an upper Bruhat interval.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

For both graph structures, `vertex` and `edge` are the maps, while `source` and `target` are the two incidence-preservation equations.

`OAI.KLInvariance.MomentGraph.GraphMap`: [MinimalExtensions.lean:1457](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1457).

`OAI.KLInvariance.MomentGraph.GraphEquiv`: [GradedSheaves.lean:270](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L270).

`OAI.KLInvariance.MomentGraph.Sheaf.pullback`: [MinimalExtensions.lean:1473](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1473).

`OAI.KLInvariance.MomentGraph.GradedSheaf.pullback`: [MinimalExtensions.lean:1650](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1650).

`OAI.KLInvariance.MomentGraph.GradedSheaf.reindex`: [GradedSheaves.lean:279](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L279).

`OAI.KLInvariance.MomentGraph.GradedSheaf.reindex_edgeFlabby`: [GradedSheaves.lean:336](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L336).
