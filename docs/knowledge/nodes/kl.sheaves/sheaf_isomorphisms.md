---
id: kl.detail.sheaf_isomorphisms
title: Sheaf isomorphisms and their partial forms
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.sheaf_morphism
- kl.detail.compatible_sections
- kl.algebra.grading_components
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.Iso
  - OAI.KLInvariance.MomentGraph.Sheaf.OnIso
  - OAI.KLInvariance.MomentGraph.Sheaf.AboveIso
  - OAI.KLInvariance.MomentGraph.GradedSheaf.Iso
  - OAI.KLInvariance.MomentGraph.GradedSheaf.OnIso
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:521
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.Iso
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:970
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.OnIso
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:692
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.AboveIso
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:210
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.Iso
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:214
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.OnIso
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

# Sheaf isomorphisms and their partial forms

An isomorphism \(j:B\to C\) of sheaves on the same graph consists of linear isomorphisms on all stalks and edge modules such that
\[
j_e\rho^{B,-}_e=\rho^{C,-}_ej_{s(e)},\qquad
j_e\rho^{B,+}_e=\rho^{C,+}_ej_{t(e)}.
\]
Applying inverses to these equalities gives the commuting equations for \(j^{-1}\).

The component maps identify full assignments. The equations identify compatible assignments on every subset, so they give isomorphisms of the corresponding ambient section modules. They also identify the images and kernels formed from the restriction maps.

## Isomorphisms on a subset

An isomorphism on \(U\subseteq V\) supplies \(j_x\) for \(x\in U\) and \(j_e\) for \(t(e)\in U\). Its upper commuting equation holds whenever \(t(e)\in U\), and its lower equation holds when both endpoints belong to \(U\).

It therefore identifies compatible tuples indexed on \(U\). In the ambient-assignment convention, this is the identification of the coordinates belonging to \(U\).

For \(U=V\), the data give a full isomorphism. For \(U=\{y:x<y\}\), they give an isomorphism above \(x\). Edges starting at \(x\) already have their edge isomorphisms because their targets lie above \(x\). The stalk isomorphism at \(x\) is the next object constructed in a descending extension.

## Graded isomorphisms

A graded isomorphism requires
\[
j_x(B^x_n)\subseteq C^x_n,\qquad
j_e(B^e_n)\subseteq C^e_n
\]
for every degree and every component on which the maps are defined.

The inverse maps preserve degree as well. For a homogeneous \(c\in C_n\), write \(j^{-1}c=\sum_m b_m\) in homogeneous components. Then \(c=\sum_mj(b_m)\), with \(j(b_m)\in C_m\). Uniqueness of the homogeneous decomposition gives \(j(b_m)=0\) for \(m\ne n\). Injectivity of \(j\) gives \(b_m=0\) in those degrees, so \(j^{-1}c=b_n\).

This argument applies separately at each vertex and edge. Hence the stored forward grading conditions provide degree-preserving isomorphisms in both directions.

## A one-edge partial isomorphism

For \(x\to y\), an isomorphism on \(\{y\}\) consists of \(j_y,j_e\) and the upper square. To extend it to the whole graph, choose \(j_x\) satisfying
\[
j_e\rho^{B,-}_e=\rho^{C,-}_ej_x.
\]
The partial edge map makes this a specified equation for \(j_x\), which is solved by the boundary-cover argument.

## References

The local definitions and constructions are listed below.

## Lean formalization

The fields `vertex`, `edge`, `lower`, and `upper` describe the local isomorphisms and squares. The inherited `toIso` and `toOnIso` fields hold the ungraded data; `vertex_graded` and `edge_graded` assert the forward degree conditions.

`OAI.KLInvariance.MomentGraph.Sheaf.Iso`: [GradedSheaves.lean:521](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L521).

`OAI.KLInvariance.MomentGraph.Sheaf.OnIso`: [GradedSheaves.lean:970](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L970).

`OAI.KLInvariance.MomentGraph.Sheaf.AboveIso`: [GradedSheaves.lean:692](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L692).

`OAI.KLInvariance.MomentGraph.GradedSheaf.Iso`: [MinimalExtensions.lean:210](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L210).

`OAI.KLInvariance.MomentGraph.GradedSheaf.OnIso`: [MinimalExtensions.lean:214](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L214).
