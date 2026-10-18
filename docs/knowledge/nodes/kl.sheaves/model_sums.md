---
id: kl.detail.model_sums
title: Finite sums of shifted boundary models
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.boundary_models
- kl.detail.graded_maps_shifts
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:672
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum
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

# Finite sums of shifted boundary models

Let \(O_c\) be a chosen model sheaf for each vertex \(c\), and let \(U\) be a set of allowed centers. A model sum centered in \(U\) is constructed in finitely many stages. Begin with the zero sheaf. At each stage choose \(c\in U\), a finite multiplicity \(m\), and nonnegative shifts \(d_1,\ldots,d_m\), and replace the previous sheaf \(B\) by
\[
B\oplus\bigoplus_{j=1}^{m}O_c(d_j).
\]
Repeated centers and zero multiplicities are permitted. The resulting construction has finitely many summands, even if \(U\) itself is infinite.

The model-sum predicate describes the sheaf produced by these constructions. A decomposition theorem separately supplies an isomorphism from the given sheaf to such a model sum; this distinction retains the restriction maps. Grouping the occurrences of each center gives a multiplicity polynomial \(m_c(q)=\sum_jq^{d_j}\) with nonnegative integer coefficients.

Freeness, the upper quotient rule, global generation, and flabbiness hold componentwise for such a sum when they hold for the models. Kernel minimality at a vertex \(x\) is inherited when \(x\notin U\), so no model is centered at that vertex.

## References

The precise Lean sources are listed below.

## Lean formalization

The constructors `zero` and `add` implement the initial sheaf and the finite shifted block. Their integer shifts are nonnegative.

`OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum`: [MinimalExtensions.lean:672](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L672).
