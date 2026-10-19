---
id: kl.sheaves.flabbiness
title: Flabbiness and closure under directed edges
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.graph_sheaf
- kl.detail.compatible_sections
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  - Sheaves
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.Flabby
  - OAI.KLInvariance.MomentGraph.Sheaf.ClosedUnder
  - OAI.KLInvariance.MomentGraph.GradedSheaf.EdgeFlabby
  - OAI.KLInvariance.MomentGraph.GradedSheaf.EdgeFlabby.flabby
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Sheaves:48
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.Flabby
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Sheaves:54
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.ClosedUnder
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:37
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.EdgeFlabby
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:42
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.EdgeFlabby.flabby
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

# Flabbiness and closure under directed edges

A subset \(U\) of a partially ordered vertex set is upper when \(x\in U\) and \(x\le y\) imply \(y\in U\).

A graph sheaf \(B\) is flabby when every assignment compatible on an upper set \(U\) extends to a global section agreeing with it at every vertex of \(U\). Written explicitly,
\[
\forall U\text{ upper},\ \forall f\text{ compatible on }U,
\exists g\text{ global},\quad g_x=f_x\ (x\in U).
\]
The given assignment is indexed on the whole vertex set, as in the section-module definition; the agreement requirement concerns its coordinates on \(U\).

## Closure under a chosen set of edges

For a set \(L\) of edges, say \(U\) is closed under \(L\) when
\[
e\in L,\ s(e)\in U\Longrightarrow t(e)\in U.
\]
When \(L\) is the entire edge set, this is closure under the directed edges.

An edge-flabby graded sheaf has the extension property for every subset closed under all its directed edges. Every upper set has that closure because \(s(e)<t(e)\). Thus edge flabbiness implies flabbiness.

For example, take an ordered chain \(x<y<z\) with just one edge \(x\to z\). The subset \(\{x,z\}\) is closed under the edge. It omits \(y>x\), so it is not upper. This displays the two classes of subsets explicitly.

For a finite vertex set, the relative extension theorem proves that flabbiness gives extension from every subset closed under the surviving edges, provided the other edge modules are zero. Taking all edges as surviving gives edge flabbiness.

## Global generation

Global generation requires, for each vertex \(x\) and each \(v\in B^x\), a global section taking value \(v\) at \(x\). Equivalently, evaluation \(\Gamma(V,B)\to B^x\) is surjective.

Flabbiness extends a prescribed compatible pattern on an upper set. Global generation prescribes a value at one stalk. Together they identify the image of the outgoing stalk map with the boundary image supplied by upper sections.

On the one-edge congruence sheaf, a value \(v\) at the upper vertex extends by \((v,v)\), and any value at either stalk is attained by this same diagonal section.

## References

The local definitions and constructions are listed below.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.Flabby`: [Sheaves.lean:48](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L48).

`OAI.KLInvariance.MomentGraph.Sheaf.ClosedUnder`: [Sheaves.lean:54](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L54).

`OAI.KLInvariance.MomentGraph.GradedSheaf.EdgeFlabby`: [GradedSheaves.lean:37](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L37).

`OAI.KLInvariance.MomentGraph.GradedSheaf.EdgeFlabby.flabby`: [GradedSheaves.lean:42](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L42).
