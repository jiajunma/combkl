---
id: kl.detail.ordered_graph
title: Ordered graphs and directed edge incidence
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses: []
lean:
  repository: openai-kl
  modules:
  - Sheaves
  declarations:
  - OAI.KLInvariance.MomentGraph.OrderedGraph
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Sheaves:21
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.OrderedGraph
  - artifact: openai-kl-paper
    locator: Related paper context; bg:bmp
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- moment_graph_sheaves
---

# Ordered graphs and directed edge incidence

An ordered graph consists of a partially ordered vertex set \(V\), an edge set \(E\), and maps
\[
s,t:E\longrightarrow V,\qquad s(e)<t(e).
\]
An edge is part of the data; it need not be a cover in the vertex order. Distinct edges may also share endpoints in the abstract definition. The strict inequality orients every edge upward and excludes directed cycles.

For a Bruhat interval, the relevant edges are all upward reflection edges. For example, a reflection can raise Coxeter length by three, so retaining only Hasse-diagram covers would discard genuine moment-graph constraints.

Outgoing edges at \(x\) are those with \(s(e)=x\); incoming edges have \(t(e)=x\). Edge labels and modules are additional data introduced later. The distinction matters when localization makes some edge modules zero while the underlying vertex order remains unchanged.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization

The three fields are `source`, `target`, and `increasing`.

`OAI.KLInvariance.MomentGraph.OrderedGraph`: [Sheaves.lean:21](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L21).
