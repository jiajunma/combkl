---
id: kl.local.ambient_later_edges
title: Ambient later-edge selections and their coset pullbacks
kind: definition
status: formalized
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.paths.ambient_after_indicator
- kl.paths.graph_invariance
- kl.local.coset_graph
- kl.local.coset_later_selections
- kl.dihedral.plane_coset_graph
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.BruhatGraph.upperSource
  - OAI.KLInvariance.BruhatGraph.upperTarget
  - OAI.KLInvariance.BruhatGraph.mappedEdgeRoot
  - OAI.KLInvariance.BruhatGraph.ambientLater
  - OAI.KLInvariance.TitsSpace.PlaneBasis.scheduledOutgoing_eq
  - OAI.KLInvariance.TitsSpace.PlaneBasis.mappedCosetRoot_eq
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1696
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.upperSource
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1698
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.upperTarget
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1700
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.mappedEdgeRoot
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1215
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.ambientLater
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1237
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.scheduledOutgoing_eq
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1744
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.mappedCosetRoot_eq
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the coefficient actions, actual modules, interval bounds, selected sets,
    finite-basis assumptions and support cases explicit?
  verdict: Defined the endpoint interval data, mapped root and ambient edge set with
    the existential source bound; checked both membership directions of scheduledOutgoing_eq
    and the exact coincidence of mapped coset and ambient roots.
tags:
- Kazhdan-Lusztig
- embedded-images
- local-comparison
---

# Ambient later-edge selections and their coset pullbacks

Let \(W,W'\) be finite-generator real Coxeter systems, and let
\[
\varphi:[u,b]_W\simeq[u',b']_{W'}
\]
be an interval order isomorphism. Work with the ambient reflection graph \(G\) on \([1,b]_W\). Write \(\sigma'\) for geometric slope in the target root system.

## The mapped edge root

For an edge \(e:p\to_Wq\) of \(G\) with \(u\le_Wp\), both endpoints belong to \([u,b]_W\): the upper endpoint satisfies \(u\le_Wp\le_Wq\le_Wb\).

The source's `upperSource` and `upperTarget` are these endpoints regarded as members of \([u,b]_W\), with these bounds. Reflection-graph invariance makes
\(\varphi(p)\to_{W'}\varphi(q)\) an edge. Define its mapped edge root
\[
\alpha'_{\varphi,e}
=\text{the positive root representing }\varphi(q)\varphi(p)^{-1}.
\]
This is `mappedEdgeRoot`.

## A later-edge set on the full ambient graph

For any positive target root \(\alpha'\), define
\[
T_{\varphi,\alpha'}
=
\{f:p\to_Wq\text{ in }G:
u\le_Wp,\qquad
\varepsilon_{W'}(\varphi(p),\alpha',\varphi(q))=1\}.
\]
Here \(\varepsilon_{W'}\) is the ambient after-indicator. The lower-bound condition makes both arguments of \(\varphi\) well-defined. Equivalently, an eligible edge belongs to this set when
\[
\sigma'(\alpha')<\sigma'(\alpha'_{\varphi,f}).
\]
This set is `ambientLater`.

At a vertex \(p\), use
\[
T_{\varphi,\alpha'}(p)=
\{f\in\operatorname{Out}_G(p): f\text{ belongs to }T_{\varphi,\alpha'}\}
\]
as the outgoing selection for a selected kernel. For a current edge \(e\), its endpoint selections use the common threshold \(\alpha'_{\varphi,e}\).

## Pullback to the relative coset graph

Choose a plane basis \(B\), its induced subgroup \(D\), and a least coset representative \(a_0\). Let
\(K=\{d\in D:da_0\le_Wb\}\),
with graph map
\[
j_V(d)=da_0,\qquad j_E(d\to_Dc)=(da_0\to_Wca_0).
\]
For a relative vertex \(x\) with \(u\le_Wxa_0\), the coset outgoing selection satisfies
\[
\mathcal F_{\alpha'}(x)
=\{f\in\operatorname{Out}_K(x):j_E(f)\in T_{\varphi,\alpha'}\}.
\]
This is `scheduledOutgoing_eq`.

Indeed, the definition of \(\mathcal F_{\alpha'}(x)\) asks for the target after-indicator to equal one. The definition of the ambient set asks for the same equality and a witness of \(u\le_Wxa_0\). The given bound supplies that witness in one direction. In the other direction, membership supplies the same indicator equality; the endpoints are the same elements of the interval in both expressions, so both evaluate \(\varphi\) at the same elements.

## The current root agrees in both graph descriptions

For a relative edge \(d:x\to_Dy\) with \(u\le_Wxa_0\), the mapped coset root is the positive root of
\[
\varphi(xa_0)\to_{W'}\varphi(ya_0).
\]
The mapped edge root of \(j_E(d)\) is defined by exactly this target edge. Thus
\[
\alpha'_{\mathrm{coset},d}=\alpha'_{\varphi,j_E(d)}.
\]
This is `mappedCosetRoot_eq`. Consequently both coset endpoint selections are pullbacks of the single ambient later-edge set with this common threshold.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The full ambient edge set and its relative-coset restriction.**

**OpenAI notes:** The local comparison uses the plane-subgroup coset through the current ambient edge and restricts the transported later-edge conditions to that coset. [dih:plane](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L20), [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** ambientLater is an edge set on the full graph [1,b], with an explicit source-above-u witness. scheduledOutgoing_eq is its inverse-image identity on the coset graph. Least coset coordinates for the source and multiplication by the actual edge reflection construct the relative edge, and both mapped-root definitions evaluate the same target edge. [PlaneLocalization:1215](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1215), [PlaneLocalization:1237](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1237), [PlaneLocalization:1700](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1700), [PlaneLocalization:1715](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1715), [PlaneLocalization:1744](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1744).

**Role in the proof:** The Blueprint defines the ambient selection before transferring the two endpoint kernels, and constructs the relative coordinates with both endpoint bounds and the exact equality of edges.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.upperSource`: [PlaneLocalization.lean:1696](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1696).

`OAI.KLInvariance.BruhatGraph.upperTarget`: [PlaneLocalization.lean:1698](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1698).

`OAI.KLInvariance.BruhatGraph.mappedEdgeRoot`: [PlaneLocalization.lean:1700](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1700).

`OAI.KLInvariance.BruhatGraph.ambientLater`: [PlaneLocalization.lean:1215](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1215).

`OAI.KLInvariance.TitsSpace.PlaneBasis.scheduledOutgoing_eq`: [PlaneLocalization.lean:1237](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1237).

`OAI.KLInvariance.TitsSpace.PlaneBasis.mappedCosetRoot_eq`: [PlaneLocalization.lean:1744](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1744).
