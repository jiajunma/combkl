---
id: kl.detail.sheaf_isomorphisms
title: Sheaf isomorphisms and isomorphisms above a vertex
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
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.Iso
  - OAI.KLInvariance.MomentGraph.Sheaf.AboveIso
  - OAI.KLInvariance.MomentGraph.GradedSheaf.Iso
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:521
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.Iso
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:692
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.AboveIso
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:210
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.Iso
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# Sheaf isomorphisms and isomorphisms above a vertex

An isomorphism \(j:B\xrightarrow{\sim}C\) of sheaves on the same graph consists of linear isomorphisms \(j_x:B^x\to C^x\) and \(j_e:B^e\to C^e\) satisfying
\[
j_e\rho^B_{e,s}=\rho^C_{e,s}j_{s(e)},\qquad
j_e\rho^B_{e,t}=\rho^C_{e,t}j_{t(e)}.
\]
Thus it identifies the actual restriction maps, as well as the modules. Applying \(j_x\) componentwise gives an isomorphism of assignments and compatible sections. The equations also identify the boundary images and the kernels of corresponding outgoing conditions.

An isomorphism above \(x\) specifies \(j_y\) only for \(y>x\), but specifies \(j_e\) for every edge with \(t(e)>x\). Its lower compatibility equation is required when \(s(e)>x\), and its upper equation whenever \(t(e)>x\). In particular, edge modules of arrows starting at \(x\) are already available even though a map on the stalk at \(x\) has not yet been constructed. This is the exact data needed in a descending extension argument.

A graded isomorphism adds preservation of the homogeneous pieces. An abstract isomorphism of two free stalks is insufficient to identify their images inside an edge module: the commuting equations above are needed.

## References

The precise Lean sources are listed below.

## Lean formalization

The fields `vertex`, `edge`, `lower`, and `upper` are respectively the local isomorphisms and the two commuting-square conditions, with the stated domains in `AboveIso`.

`OAI.KLInvariance.MomentGraph.Sheaf.Iso`: [GradedSheaves.lean:521](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L521).

`OAI.KLInvariance.MomentGraph.Sheaf.AboveIso`: [GradedSheaves.lean:692](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L692).

The additional fields `vertex_graded` and `edge_graded` preserve the homogeneous pieces; `toIso` contains the underlying ungraded isomorphism.

`OAI.KLInvariance.MomentGraph.GradedSheaf.Iso`: [MinimalExtensions.lean:210](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L210).
