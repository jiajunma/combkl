---
id: kl.detail.ordered_graph
title: Ordered graphs, reflection edges, and labels
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

# Ordered graphs, reflection edges, and labels

An ordered graph consists of a partially ordered vertex set \(V\), a set \(E\) of edges, and maps
\[
s,t:E\to V
\]
with \(s(e)<t(e)\) for every edge. The maps specify the lower and upper endpoint. A finite directed path therefore gives a strictly increasing chain, so a directed cycle would contradict irreflexivity of \(<\).

Edges have their own identities. For example, two distinct elements of \(E\) can both have source \(x\) and target \(y\). The sheaf data then supply a module and two restriction maps for each of those edges.

The outgoing and incoming edges at \(x\) are
\[
E_x^+=\{e:s(e)=x\},\qquad E_x^-=\{e:t(e)=x\}.
\]
A label system is an additional map \(\alpha:E\to A\) into a coefficient algebra.

## A simple ordered-graph example

For vertices \(x<y<z\), take edges \(x\to y\), \(y\to z\), and \(x\to z\). The first two follow consecutive vertices in the chain; the third connects the same outer endpoints directly. All three satisfy the strict-order field.

The labelled Bruhat-graph construction uses this framework with reflection edges and polynomial root labels. Its defining interval, edge set, and label map are developed in [[node:kl.detail.polynomial_labels]].

## References

The local source declaration below gives the graph data.

## Lean formalization

The fields `source`, `target`, `increasing` give the endpoint maps and strict-order condition.

`OAI.KLInvariance.MomentGraph.OrderedGraph`: [Sheaves.lean:21](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L21).
