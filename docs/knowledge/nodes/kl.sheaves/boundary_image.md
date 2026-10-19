---
id: kl.notes.boundary_image
title: Boundary values supplied by upper sections
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.graph_sheaf
- kl.detail.graded_sheaf
- kl.detail.compatible_sections
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  - Sheaves
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.Boundary
  - OAI.KLInvariance.MomentGraph.Sheaf.stalkMap
  - OAI.KLInvariance.MomentGraph.Sheaf.boundaryMap
  - OAI.KLInvariance.MomentGraph.GradedSheaf.boundaryHom
  - OAI.KLInvariance.MomentGraph.GradedSheaf.boundaryImage
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Sheaves:180
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.Boundary
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Sheaves:183
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.stalkMap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Sheaves:189
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.boundaryMap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:74
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.boundaryHom
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:81
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.boundaryImage
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; bg:bmp
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the mathematical hypotheses and scope retained from the referenced declarations?
  verdict: The exposition follows the fixed Lean source; worked calculations explain
    the constructions.
tags:
- Kazhdan-Lusztig
- background
---

# Boundary values supplied by upper sections

For a vertex \(x\), let \(E_x^+=\{e:s(e)=x\}\) be its outgoing edges. Define the boundary module
\[
\partial_xB=\prod_{e\in E_x^+}B^e.
\]
For a finite graph this is a finite product, equivalently a finite direct sum.

The outgoing stalk map is
\[
r_x:B^x\to\partial_xB,\qquad
r_x(v)=(\rho^-_e(v))_{e\in E_x^+}.
\]
Its kernel is the full outgoing kernel.

## The upper-section map

Let \(U_x=\{y:x<y\}\). Every outgoing edge has target in \(U_x\). A section compatible on \(U_x\) supplies the tuple
\[
b_x(m)=(\rho^+_e(m_{t(e)}))_{e\in E_x^+}.
\]
This defines a linear map
\[
b_x:\Gamma(U_x,B)\to\partial_xB.
\]
Its image is the boundary image
\[
B^{\delta x}=\operatorname{im}b_x.
\]

In the ambient section convention, \(m\) also has coordinates outside \(U_x\). The displayed formula reads only its upper-endpoint coordinates.

## A labelled diamond

Take vertices \(x<y,z<t\), edges \(x\to y,x\to z,y\to t,z\to t\), and modules \(A\) at vertices and \(A/(\alpha)\) at edges, with quotient restrictions.

Above \(x\), compatibility gives \(m_y\equiv m_t\) and \(m_z\equiv m_t\) modulo \(\alpha\). Therefore
\[
B^{\delta x}=\{(\overline a,\overline a):\overline a\in A/(\alpha)\}
\subseteq (A/(\alpha))^2.
\]
Every diagonal tuple occurs by choosing equal upper values lifting \(\overline a\). Thus the upper edge equations determine the boundary image explicitly.

A free cover \(A\to B^{\delta x}\), \(a\mapsto(\overline a,\overline a)\), supplies the new stalk at \(x\). Its two coordinate maps are the outgoing restrictions.

## Graded boundary data

For finite vertex and edge sets, all restrictions have degree zero, so \(b_x\) is a homogeneous map between the section and boundary modules. Over the Noetherian polynomial coefficient ring, its image is finite graded module data.

The boundary-sheaf construction takes a minimal graded free cover of this image. Global generation and flabbiness later identify the image of \(r_x\) with the same boundary image.

## References

The local definitions and constructions are listed below.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.Boundary`: [Sheaves.lean:180](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L180).

`OAI.KLInvariance.MomentGraph.Sheaf.stalkMap`: [Sheaves.lean:183](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L183).

`OAI.KLInvariance.MomentGraph.Sheaf.boundaryMap`: [Sheaves.lean:189](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L189).

`OAI.KLInvariance.MomentGraph.GradedSheaf.boundaryHom`: [GradedSheaves.lean:74](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L74).

`OAI.KLInvariance.MomentGraph.GradedSheaf.boundaryImage`: [GradedSheaves.lean:81](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L81).
