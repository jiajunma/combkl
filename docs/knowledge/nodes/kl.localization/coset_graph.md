---
id: kl.local.coset_graph
title: The finite relative coset graph inside a Bruhat interval
kind: definition
status: formalized
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.dihedral.induced_system
- kl.dihedral.plane_coset_graph
- kl.foundations.interval
- kl.detail.graph_transport
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.CosetVertex
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetOrder
  - OAI.KLInvariance.TitsSpace.PlaneBasis.CosetEdge
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetGraph
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetAmbient
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetEdgeAmbient
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetGraphMap
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:439
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.CosetVertex
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:442
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetOrder
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:461
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.CosetEdge
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:464
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetGraph
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:448
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetAmbient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:472
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetEdgeAmbient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:476
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetGraphMap
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read all finite coset graph definitions and incidence fields. Kept the
    induced order, the ambient cutoff, the precise least-coset hypothesis for the
    edge map and the actual left-reflection label.
tags:
- Kazhdan-Lusztig
- localization
---

# The finite relative coset graph inside a Bruhat interval

Fix a finite-generator Coxeter system \(W\), a root plane \(P\), and a plane basis determining the induced dihedral Coxeter system on the reflection subgroup \(D=D_P\). Write \(\le_D\) for its Bruhat order and \(\le_W\) for ambient Bruhat order. Choose \(a_0,b\in W\).

The relative vertex set is
\[
K_{a_0,b}
=\{d\in D:1\le_D d,\ da_0\le_W b\}.
\]
This is CosetVertex. Its partial order is the restriction of \(\le_D\), recorded as cosetOrder.

An edge is a pair \((d,c)\) of these vertices with a directed reflection step \(d\to_D c\). These edges form CosetEdge. The ordered graph cosetGraph has source \(d\), target \(c\), and strict increase follows because a reflection step increases intrinsic length.

## The ambient vertex map

The map
\[
j_V:K_{a_0,b}\longrightarrow[1,b]_W,\qquad d\longmapsto da_0
\]
is cosetAmbient. Every group element is above \(1\) in Bruhat order, and the upper inequality is part of the vertex definition.

Its image is \(Da_0\cap[1,b]_W\). A point in this intersection can be written \(da_0\), and \(1\le_D d\) holds in the induced Coxeter system. Right cancellation proves that \(j_V\) is injective.

## The graph map from a least coset representative

Assume now
\[
\ell_W(a_0)\le\ell_W(za_0)\qquad(z\in D).
\]
The [[node:kl.dihedral.plane_coset_graph|coset reflection-graph theorem]] gives
\[
d\to_D c\quad\Longleftrightarrow\quad da_0\to_W ca_0.
\]
Hence cosetEdgeAmbient sends an edge \((d,c)\) to \((da_0,ca_0)\), and cosetGraphMap is
\[
j=(j_V,j_E):\operatorname{cosetGraph}(a_0,b)\longrightarrow
\operatorname{BruhatGraph}([1,b]).
\]
Its two endpoint identities follow directly from these formulas.

Under the same least-length hypothesis, the [[node:kl.local.coset_outgoing_lifts|coset outgoing-lift theorem]] proves that \(K_{a_0,b}\) is a finite relative lower ideal and that every outgoing ambient edge labelled by a reflection in \(D\) lifts to this graph.

## Labels of the corresponding edges

For \(a:d\to_D c\), the ambient left reflection label is
\[
(ca_0)(da_0)^{-1}=cd^{-1}.
\]
Thus both edges use the same ambient reflection in \(D\). The localized coset sheaf uses the ambient polynomial root label of \(j_E(a)\), mapped into the root-plane localization ring.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Relative extension through an explicit graph map.**

**OpenAI notes:** The coset intersection is a finite relative lower ideal. A relative upper subset is closed under the surviving plane-labelled edges. Descending ambient extension gives relative flabbiness after localization. [loc:relative-flabbiness](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L226).

**Lean (primary):** The same descending extension is factored into extend_closedUnder and a graph-pullback theorem. The coset map supplies vertex injectivity and explicit outgoing lifts; the root/unit criterion makes all outside edge modules zero. A separate theorem records selected-kernel equality under that pullback. [Sheaves:106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L106), [MinimalExtensions:1520](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1520), [PlaneLocalization:497](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L497), [PlaneLocalization:591](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L591), [TerminalKernels:393](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L393).

**Role in the proof:** Relative order determines the upper subsets on the coset, while the ambient graph supplies the extension. The localized stalks and edge maps remain the actual tensor-extended ambient modules, so selected kernels and their edge images retain their embeddings.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.CosetVertex`: [PlaneLocalization.lean:439](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L439).

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetOrder`: [PlaneLocalization.lean:442](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L442).

`OAI.KLInvariance.TitsSpace.PlaneBasis.CosetEdge`: [PlaneLocalization.lean:461](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L461).

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetGraph`: [PlaneLocalization.lean:464](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L464).

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetAmbient`: [PlaneLocalization.lean:448](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L448).

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetEdgeAmbient`: [PlaneLocalization.lean:472](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L472).

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetGraphMap`: [PlaneLocalization.lean:476](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L476).
