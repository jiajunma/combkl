---
id: kl.detail.structure_sheaves
title: Structure sheaves on principal lower ideals
kind: definition
status: formalized
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.sheaves.graph_sheaf
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf
  - OAI.KLInvariance.MomentGraph.Sheaf.structureVertexIso
  - OAI.KLInvariance.MomentGraph.Sheaf.structureCompatible_iff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:891
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:908
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.structureVertexIso
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:359
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.structureCompatible_iff
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the PLift-indexed structureSheaf fields and structureVertexIso, together
    with structureCompatible_iff. Explained the singleton/empty coordinate modules,
    both restrictions and the exact supported-edge congruences.
tags:
- Kazhdan-Lusztig
- interpolation
---

# Structure sheaves on principal lower ideals

Let \(R\) be a commutative ring, \(G\) an ordered graph, \(\alpha_e\in R\) its edge labels, and \(c\) a vertex. The **structure sheaf supported below \(c\)** is
\[
\mathcal O_c^x=
\begin{cases}
R,&x\le c,\\
0,&x\not\le c,
\end{cases}
\qquad
\mathcal O_c^e=
\begin{cases}
R/(\alpha_e),&t(e)\le c,\\
0,&t(e)\not\le c.
\end{cases}
\]
This is structureSheaf.

If \(t(e)\le c\), the inequality \(s(e)<t(e)\) also puts the lower endpoint below \(c\). Both restrictions are then the quotient map \(R\to R/(\alpha_e)\). If \(t(e)\not\le c\), the edge module is zero and both restrictions are zero.

## The source's support-indexed representation

Lean represents the supported stalk as functions
\[
\{\star:x\le c\}\longrightarrow R.
\]
The index type is PLift of the proposition \(x\le c\). When that proposition holds, there is one coordinate: evaluation at it identifies the module with \(R\), with inverse the constant function. When it fails, the empty function module is the zero module.

The edge representation uses the same construction for \(t(e)\le c\), with values in \(R/(\alpha_e)\). The lower map uses \(s(e)\le t(e)\le c\) to select the corresponding lower-stalk coordinate.

## Sections as scalar congruences

On a supported edge, compatibility is
\[
f_{s(e)}\equiv f_{t(e)}\pmod{\alpha_e},
\]
equivalently
\[
\alpha_e\mid f_{s(e)}-f_{t(e)}.
\]
For a section over a vertex subset \(\Omega\), impose this condition on supported edges whose two endpoints belong to \(\Omega\). On every other edge with zero module, compatibility is automatic.

For a single supported edge \(x\to c\), a section is a pair \((r,s)\in R^2\) with \(r-s\in(\alpha_e)\).

The [[node:kl.local.structure_sheaf_properties|basic structure-sheaf properties theorem]] proves free finite stalks, generation and upper quotients. The [[node:kl.local.flow_down_flabbiness|flow-down criterion]] gives flabbiness from sections with specified lower support, and the [[node:kl.local.dihedral_interpolation|dihedral interpolation theorem]] constructs those sections for the induced root labels.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf`: [MinimalExtensions.lean:891](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L891).

`OAI.KLInvariance.MomentGraph.Sheaf.structureVertexIso`: [MinimalExtensions.lean:908](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L908).

`OAI.KLInvariance.MomentGraph.Sheaf.structureCompatible_iff`: [DihedralIntervals.lean:359](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L359).
