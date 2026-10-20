---
id: kl.local.coset_later_selections
title: Later-edge selections for the coset model comparison
kind: definition
status: formalized
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.coset_graph
- kl.dihedral.plane_coset_graph
- kl.paths.graph_invariance
- kl.notes.reflection_order
- kl.detail.transported_schedule
- kl.detail.root_reflection_correspondence
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  - PlaneLocalization
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.TitsSpace.ambientAfterIndicator
  - OAI.KLInvariance.TitsSpace.ambientAfterIndicator_edge_self
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetUpperVertex
  - OAI.KLInvariance.TitsSpace.PlaneBasis.outgoing_upper
  - OAI.KLInvariance.TitsSpace.PlaneBasis.scheduledOutgoing
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetEdge_target_upper
  - OAI.KLInvariance.TitsSpace.PlaneBasis.mappedCosetRoot
  - OAI.KLInvariance.TitsSpace.PlaneBasis.scheduledLower
  - OAI.KLInvariance.TitsSpace.PlaneBasis.scheduledUpper
  - OAI.KLInvariance.TitsSpace.PlaneBasis.scheduledLower_self
  - OAI.KLInvariance.TitsSpace.PlaneBasis.scheduledLower_root_ne
  - OAI.KLInvariance.TitsSpace.PlaneBasis.outgoingUpper_root_ne
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:2107
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.ambientAfterIndicator
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:2120
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.ambientAfterIndicator_edge_self
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1001
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetUpperVertex
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1013
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.outgoing_upper
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1018
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.scheduledOutgoing
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1148
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetEdge_target_upper
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1152
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.mappedCosetRoot
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1159
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.scheduledLower
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1163
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.scheduledUpper
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1168
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.scheduledLower_self
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:123
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.scheduledLower_root_ne
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:138
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.outgoingUpper_root_ne
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read ambientAfterIndicator and its self-edge value, both interval endpoint
    membership checks, mappedCosetRoot, scheduledOutgoing/Lower/Upper, strict self-exclusion
    and the two distinct-root arguments. Preserved the source lower bound u<=x*a0,
    the target geometric slope and the one common threshold; kept these local model
    selections separate from the global schedule construction.
tags:
- Kazhdan-Lusztig
- embedded-images
---

# Later-edge selections for the coset model comparison

Fix finite-generator real Coxeter systems \(W,W'\), an interval order isomorphism
\[
\varphi:[u,b]_W\xrightarrow{\sim}[u',b']_{W'},
\]
and the target system's geometric slope function \(s'\) on its positive roots.

In \(W\), fix a root plane \(P\) with a chosen plane basis, its induced dihedral subgroup \(D\), and a representative \(a_0\) satisfying
\[
\ell(a_0)\le\ell(da_0)\qquad(d\in D).
\]
Let \(K=\{d\in D:da_0\le_W b\}\) be the finite relative coset graph.

For \(x\in K\) with \(u\le_Wxa_0\), write
\[
\widehat x=xa_0\in[u,b]_W.
\]
This is cosetUpperVertex. The [[node:kl.paths.graph_invariance|reflection-edge transport theorem]] makes the image under \(\varphi\) of every relevant ambient reflection edge another reflection edge.

## The target after-indicator

For \(p,q\in W'\) and a positive target root \(\alpha'\), define
\[
\varepsilon(p,\alpha',q)=
\begin{cases}
1,&p\to q\text{ and }s'(\alpha')<s'(a_{p,q}),\\
0,&\text{otherwise},
\end{cases}
\]
where \(a_{p,q}\) is the canonical positive root of the left reflection \(qp^{-1}\) when \(p\to q\). This is ambientAfterIndicator.

For a reflection edge \(p\to q\), using its own root as threshold gives
\(\varepsilon(p,a_{p,q},q)=0\), because the required slope inequality is strict.

## Selected outgoing edges at a relative vertex

For a threshold \(\alpha'\), define
\[
\mathcal F_{\alpha'}(x)
=\{f:x\to_Dz\text{ in }K:
 \varepsilon(\varphi(\widehat x),\alpha',\varphi(\widehat z))=1\}.
\]
This is scheduledOutgoing.

Every \(\widehat z\) in this formula belongs to \([u,b]_W\). Indeed, the relative edge gives \(\widehat x\le_W\widehat z\), so \(u\le_W\widehat z\); membership of \(z\) in \(K\) supplies \(\widehat z\le_Wb\).

## The common threshold for the current edge

Fix \(e:x\to_Dy\) with \(u\le_Wxa_0\). Let
\[
\alpha'_e=a_{\varphi(\widehat x),\varphi(\widehat y)}
\]
be the positive target root of its image edge. This is mappedCosetRoot.

The two endpoint selections are
\[
F_e=\mathcal F_{\alpha'_e}(x),\qquad
H_e=\mathcal F_{\alpha'_e}(y).
\]
They are scheduledLower and scheduledUpper. Both use the same target root as the threshold.

The current edge is absent from \(F_e\), since its target after-indicator with its own threshold is zero.

## Distinct roots in the selected conditions

A selected lower edge \(f\in F_e\) has a different positive source root from \(e\). If the roots were equal, their reflections would be equal. Their sources are both \(x\), so their targets would also agree, making \(f=e\). The strict threshold excludes this edge.

Every outgoing edge from \(y\) has a root different from the root of \(e\). Otherwise the two successive edges \(x\to y\to z\) would use the same reflection \(t\). Then \(z=ty=t^2x=x\), contradicting strict increase of intrinsic length along the two edges.

The same reflection arguments in the target system show that the other incident image edges have roots different from \(\alpha'_e\). Injectivity of the geometric slope gives distinct scores there, so each endpoint selection is determined by the displayed strict comparison.

Selection uses the target roots and their slopes. Reduction uses the source roots of the selected edges. The source root distinctions above ensure that these labels survive reduction by the current edge root. The [[node:kl.local.coset_edge_reduction|actual coset edge-reduction theorem]] turns them into associated reduced labels, which is one input of the structure-model comparison.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Endpoint selections and their finite indicator sums.**

**OpenAI notes:** The notes select outgoing edges strictly later than the current edge in the transported target label order, then count the supported selections in the full relative interval. Incident image labels have no ties. [dih:count](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L464), [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** A target after-indicator tests an upward reflection edge and a strict geometric-slope comparison. Both endpoint selections use the mapped current root as one threshold. supported_card_count proves an explicit target-vertex bijection between supported selected edges and the nonzero terms of the finite indicator sum. [DihedralIntervals:2107](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2107), [PlaneLocalization:1018](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1018), [PlaneLocalization:1152](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1152), [PlaneLocalization:1159](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1159), [PlaneLocalization:1163](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1163), [PlaneLocalization:1031](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1031).

**Role in the proof:** This reindexing identifies the sums to which the transported dihedral count theorem applies. It supplies the edge-set interpretation of that theorem without replacing its numerical count argument.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.ambientAfterIndicator`: [DihedralIntervals.lean:2107](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2107).

`OAI.KLInvariance.TitsSpace.ambientAfterIndicator_edge_self`: [DihedralIntervals.lean:2120](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2120).

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetUpperVertex`: [PlaneLocalization.lean:1001](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1001).

`OAI.KLInvariance.TitsSpace.PlaneBasis.outgoing_upper`: [PlaneLocalization.lean:1013](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1013).

`OAI.KLInvariance.TitsSpace.PlaneBasis.scheduledOutgoing`: [PlaneLocalization.lean:1018](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1018).

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetEdge_target_upper`: [PlaneLocalization.lean:1148](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1148).

`OAI.KLInvariance.TitsSpace.PlaneBasis.mappedCosetRoot`: [PlaneLocalization.lean:1152](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1152).

`OAI.KLInvariance.TitsSpace.PlaneBasis.scheduledLower`: [PlaneLocalization.lean:1159](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1159).

`OAI.KLInvariance.TitsSpace.PlaneBasis.scheduledUpper`: [PlaneLocalization.lean:1163](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1163).

`OAI.KLInvariance.TitsSpace.PlaneBasis.scheduledLower_self`: [PlaneLocalization.lean:1168](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1168).

`OAI.KLInvariance.TitsSpace.PlaneBasis.scheduledLower_root_ne`: [TerminalKernels.lean:123](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L123).

`OAI.KLInvariance.TitsSpace.PlaneBasis.outgoingUpper_root_ne`: [TerminalKernels.lean:138](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L138).
