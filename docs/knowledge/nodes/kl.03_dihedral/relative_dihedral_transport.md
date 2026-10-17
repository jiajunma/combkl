---
id: kl.notes.relative_dihedral_transport
title: Relative dihedral intervals and their transport
kind: theorem
status: proved
primary_topic: kl.03_dihedral
topics:
- kl.03_dihedral
uses:
- kl.notes.relative_dihedral_intervals
- kl.paths.graph_invariance
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.transport_interval
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:736
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.transport_interval
  - artifact: openai-kl-paper
    locator: 3. Dihedral intervals and transported reflection orders; dih:transport
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the mathematical hypotheses and scope retained from the referenced declarations?
  verdict: The exposition follows the fixed Lean source; worked calculations explain
    the constructions.
tags:
- Kazhdan-Lusztig
- dihedral
---

# Relative dihedral intervals and their transport

A root plane \(\Pi\) determines a maximal dihedral reflection subgroup \(D_\Pi\). This subgroup has its own canonical Coxeter generators and its own Bruhat order. On a coset \(Da_0\), use a representative \(a_0\) of minimal ambient length to transfer this relative order.

Relative comparability implies ambient comparability. The construction does not identify the relative order with the entire order induced from the ambient group.

Let a relative interval \([x,c]_D\) of rank at least two lie inside \([u,b]\). If \(\phi:[u,b]\simeq[u',b']\), there is a target root-plane subgroup \(D'\) such that
\[
\phi([x,c]_D)=[\phi(x),\phi(c)]_{D'}.
\]
The restriction preserves relative order, relative rank differences, and directed reflection edges.

*Proof.*

The two relative atoms above \(x\) give two distinct reflection labels after transport. They determine a target root plane. Moving through successive ranks, the equality of the two reflection products around each diamond forces all the next labels into this same plane. Hence every image vertex lies in one dihedral coset.

Next consider two vertices at relative distance two. Exactly two ambient directed two-edge paths join them, and all intermediate vertices belong to the ambient interval. Graph reconstruction transports this precise path count. In the target dihedral coset it forces relative distance two as well. Iterating recovers consecutive ranks and both directions of relative order.

The image therefore has the full relative interval as its range, rather than merely an embedded dihedral-shaped subgraph. This range statement is what permits later-edge sums to be transported without losing vertices.

## References

[3. Dihedral intervals and transported reflection orders](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L276).

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.transport_interval`: [DyerPaths.lean:736](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L736).
