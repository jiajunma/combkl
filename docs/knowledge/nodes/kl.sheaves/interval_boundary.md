---
id: kl.sheaves.interval_boundary
title: The boundary-sheaf family obtained by upper-interval restriction
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.boundary_pullback
- kl.sheaves.boundary_existence
- kl.detail.boundary_uniqueness
- kl.foundations.interval
lean:
  repository: openai-kl
  modules:
  - EdgeLocalization
  - SimultaneousInvariance
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.BruhatGraph.upperInclusion
  - OAI.KLInvariance.BruhatGraph.upperInclusion_injective
  - OAI.KLInvariance.BruhatGraph.upperInclusion_outgoing
  - OAI.KLInvariance.BruhatGraph.restrictBoundary
  - OAI.KLInvariance.BruhatGraph.intervalBoundary
  - OAI.KLInvariance.BruhatGraph.upperGraphInclusion
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:300
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.upperInclusion
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:308
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.upperInclusion_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:313
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.upperInclusion_outgoing
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:332
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.restrictBoundary
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:1123
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.intervalBoundary
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SimultaneousInvariance:44
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.upperGraphInclusion
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

# The boundary-sheaf family obtained by upper-interval restriction

Fix a finite-generator Coxeter system, a real basis of its extended realization, and the resulting polynomial coefficient algebra. Fix \(b\in W\), and let \(B(b)\) be the chosen normalized boundary sheaf on \([1,b]\).

For \(u\le b\), the upper-interval inclusion sends a vertex or reflection edge of \([u,b]\) to the same group element or pair in \([1,b]\). Define
\[
\mathcal I_{u,b}=B(b)|_{[u,b]}
\]
by pulling back along this graph map. This is the source's interval-boundary family.

## Boundary data under the inclusion

The vertex map is injective. Every ambient outgoing edge from \(z\in[u,b]\) has target \(y\) with
\[
u\le z<y\le b.
\]
It therefore lies in the upper interval and has the required outgoing lift. The top vertex maps to \(b\), and the polynomial labels are unchanged.

The boundary-pullback theorem makes \(\mathcal I_{u,b}\) a normalized boundary sheaf on \([u,b]\). Boundary uniqueness also gives a graded isomorphism to the normalized sheaf chosen independently on that interval.

## One fixed stalk module across upper restrictions

At \(z\in[u,b]\),
\[
\mathcal I_{u,b}^{\,z}=B(b)^z.
\]
For a further upper interval \([x,b]\subseteq[u,b]\), its stalk at \(z\ge x\) is the same module. The restrictions on each retained edge are the same maps.

This common family is used in the simultaneous-induction argument: matching a set of outgoing edges gives equal kernel submodules inside a fixed stalk.

## Relation to lower-supported models

The upper-interval family keeps the top \(b\) fixed and restricts \(B(b)\).

A lower-supported model centered at \(c\) is constructed from the normalized sheaf \(B(c)\) on \([1,c]\), then extended by zero to \([1,b]\). Its top normalization is at \(c\).

Thus the two constructions have explicit stalk descriptions:
\[
\mathcal I_{u,b}^{\,z}=B(b)^z,\qquad
O_c^z=
\begin{cases}
B(c)^z,&z\le c,\\
0,&z\not\le c.
\end{cases}
\]
The first supports restriction in rank induction; the second supplies the model summands and their character terms.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.upperInclusion`: [EdgeLocalization.lean:300](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L300).

`OAI.KLInvariance.BruhatGraph.upperInclusion_injective`: [EdgeLocalization.lean:308](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L308).

`OAI.KLInvariance.BruhatGraph.upperInclusion_outgoing`: [EdgeLocalization.lean:313](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L313).

`OAI.KLInvariance.BruhatGraph.restrictBoundary`: [EdgeLocalization.lean:332](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L332).

`OAI.KLInvariance.BruhatGraph.intervalBoundary`: [TerminalKernels.lean:1123](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1123).

`OAI.KLInvariance.BruhatGraph.upperGraphInclusion`: [SimultaneousInvariance.lean:44](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SimultaneousInvariance.lean#L44).
