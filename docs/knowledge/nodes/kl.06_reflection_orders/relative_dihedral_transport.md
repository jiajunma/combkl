---
id: kl.notes.relative_dihedral_transport
title: Relative dihedral intervals and their transport
kind: theorem
status: proved
primary_topic: kl.06_reflection_orders
topics:
- kl.06_reflection_orders
uses:
- kl.notes.relative_dihedral_intervals
- kl.paths.graph_invariance
- kl.detail.plane_basis
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

### Step 1. Transport the relative interval as an actual graph

Choose a minimal representative \(a_0\) of the source dihedral coset. The map \(z\mapsto za_0\) identifies relative reflection edges with ambient ones. Compose it with the given interval order isomorphism \(\phi\), obtaining an injective vertex map \(f\) that sends every relative edge to an ambient target edge by graph invariance.

The assumed relative rank is at least two, so the interval has two distinct atoms above its bottom. Their image edge labels give two distinct reflections and hence two independent root directions.

### Step 2. Show that all images lie in one target root plane coset

Let \(P'\) be the plane spanned by these initial roots. Around a rank-two diamond, both two-edge paths have the same product of reflections. The moving-image identity identifies the plane spanned by each pair of labels. Since the two initial directions are independent, that plane is \(P'\).

Apply this successively through the two-vertex internal ranks: once the labels entering a rank lie in \(P'\), the diamonds to the next rank place their outgoing labels in \(P'\) too. Every image vertex is therefore reached from the bottom by reflections in the same maximal plane subgroup \(D'\).

Choose a minimal representative \(a'\) of this target coset and define
\(F(z)=f(z)(a')^{-1}\in D'\).
Then \(F(z)a'=f(z)\), and injectivity of \(f\) implies injectivity of \(F\).

### Step 3. Detect relative rank two from the number of paths

Take source vertices at relative rank distance two. The relative interval between them has exactly two middle vertices, and its ambient directed two-edge paths have precisely these intermediates. Graph invariance transports that exact two-path count: every target intermediate lies in the ambient interval and pulls back.

In a dihedral coset, if endpoints have positive even relative difference \(r\), the internal odd ranks supply exactly \(r\) two-edge paths. All such paths are ambient paths, and the common-plane calculation places all ambient intermediates back in this coset. The transported count is two, so \(r=2\).

### Step 4. Recover the consecutive ranks

Every consecutive-rank edge in an interval of rank at least two lies in a consecutive two-edge path. Step 3 makes the target total gap two. Its two edge gaps are positive integers, so both are one. Thus every relative cover is sent to a relative cover.

Following a saturated chain yields
\[
\ell_{D'}(F(z))-\ell_{D'}(F(x))
=\ell_D(z)-\ell_D(x).
\]

### Step 5. Prove surjectivity onto the full relative interval

The image contains the two endpoints and two distinct vertices in every internal rank. A dihedral interval of the same rank has exactly those numbers of vertices. There is therefore no additional target vertex at any rank, and the image is the whole interval.

Relative order is determined by strict length comparison or equality; relative reflection edges are determined by positive odd length difference. Injectivity and the rank identity preserve and reflect both predicates. This proves every part of the claimed transport, including its range statement.

## References

[3. Dihedral intervals and transported reflection orders](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L276).

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.transport_interval`: [DyerPaths.lean:736](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L736).
