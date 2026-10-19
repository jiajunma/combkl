---
id: kl.detail.boundary_models
title: Boundary models supported on principal lower ideals
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.boundary_sheaf
- kl.sheaves.lower_extension
- kl.detail.sheaf_isomorphisms
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.BoundaryModels
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:661
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.BoundaryModels
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

# Boundary models supported on principal lower ideals

Fix a nonnegatively graded coefficient algebra \(A\), a labelled ordered graph, and \(J=A_{>0}\). A boundary-model family assigns to every vertex \(c\) a graded sheaf \(O_c\) on the whole graph.

Its data satisfy the following conditions for all centers \(c\):

- Every stalk \(O_c^x\) is free over \(A\).
- Every upper edge map is surjective with kernel \(\alpha_eO_c^{t(e)}\).
- Global sections generate every stalk.
- The sheaf is flabby.
- If \(x\not\le c\), then \(O_c^x=0\).
- A specified \(A\)-linear isomorphism \(O_c^c\simeq A\) preserves grading, with \(1\in A\) in degree zero.
- For every \(x\ne c\), the full outgoing kernel satisfies
  \[
  K_x(O_c)\subseteq JO_c^x.
  \]

The support condition places the sheaf on the principal lower ideal
\(\{x:x\le c\}\). The normalization at \(c\) specifies its top generator, and minimality controls the stalk covers at other vertices.

## The top isomorphism and its grading

The source records the top linear isomorphism and its forward degree condition separately. Its inverse also preserves degree: decompose a preimage into homogeneous components, apply the forward map, and use uniqueness of components and injectivity to eliminate every degree except the prescribed one.

Thus the normalization identifies \(O_c^c\) with the graded unit module in both directions.

## Construction on each lower ideal

Construct the normalized boundary sheaf on the lower graph \(\{x:x\le c\}\), then extend it by zero to the full graph. The extension theorem supplies the free-stalk, quotient, section, and minimality properties above.

If the target of an edge is outside this lower ideal, its edge module is zero. This follows directly from the extension construction and also from the upper-quotient rule applied to its zero upper stalk.

## The two models on one edge

On \(x\to y\) over \(A=\mathbb R[\alpha]\), the model \(O_y\) is the congruence sheaf with stalks \(A,A\) and edge module \(A/(\alpha)\).

The model \(O_x\) has stalks \(A,0\) and zero edge module. It is obtained from the normalized one-vertex sheaf at \(x\) by extension by zero. These two models are the building blocks for a general free flabby sheaf on this graph.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

The fields `sheaf`, `free`, `quotient`, `generated`, `flabby`, `support`, `top`, `top_graded`, and `minimal` record the family and the conditions above.

`OAI.KLInvariance.MomentGraph.GradedSheaf.BoundaryModels`: [MinimalExtensions.lean:661](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L661).
