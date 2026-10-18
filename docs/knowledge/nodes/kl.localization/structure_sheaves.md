---
id: kl.detail.structure_sheaves
title: Rank-one structure sheaves on principal lower ideals
kind: definition
status: formalized
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.sheaves.graph_sheaf
- kl.detail.upper_quotient
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:891
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf
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

# Rank-one structure sheaves on principal lower ideals

Let \(G\) be an ordered graph with edge labels \(\alpha_e\in R\), and fix a vertex \(c\). Its structure sheaf supported below \(c\) has
\[
O_c^x=\begin{cases}R&x\le c,\\0&x\not\le c,\end{cases}
\qquad
O_c^e=\begin{cases}R/(\alpha_e)&t(e)\le c,\\0&t(e)\not\le c.\end{cases}
\]
For an edge with \(t(e)\le c\), both endpoints are below \(c\), and both restriction maps are the quotient map. For an edge with \(t(e)\not\le c\), the target edge module is zero, so both restrictions are zero.

Its sections are tuples of coefficients satisfying the congruences \(m_{s(e)}\equiv m_{t(e)}\pmod{\alpha_e}\) on the supported edges. The vertex modules are finite free, and the upper restriction has kernel \(\alpha_e O_c^{t(e)}\).

Flabbiness is an additional theorem for the induced dihedral models; it is not asserted for an arbitrary labelled graph. Likewise, this definition alone does not identify the structure sheaf with a minimal-boundary sheaf in higher rank.

## References

The precise Lean sources are listed below.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf`: [MinimalExtensions.lean:891](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L891).
