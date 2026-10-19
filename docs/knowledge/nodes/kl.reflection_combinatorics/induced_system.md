---
id: kl.dihedral.induced_system
title: The Coxeter system induced by the angular roots of a plane
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.detail.plane_basis
- kl.dihedral.plane_generation
- kl.dihedral.two_involutions
lean:
  repository: openai-kl
  modules:
  - Decomposition
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.matrix
  - OAI.KLInvariance.TitsSpace.PlaneBasis.system
  - OAI.KLInvariance.TitsSpace.PlaneBasis.simpleRoot
  - OAI.KLInvariance.TitsSpace.PlaneBasis.system_simple
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:901
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.matrix
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:906
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.system
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:915
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.simpleRoot
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:927
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.system_simple
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

# The Coxeter system induced by the angular roots of a plane

Let \(P\) be a root plane, and let \(\mathcal B=(a,b)\) be its plane basis. Write
\[
s=r_a,\qquad t=r_b.
\]
The [[node:kl.dihedral.plane_generation|endpoint-generation theorem]] identifies
\(D_P=\langle s,t\rangle\).

The two reflections are distinct: equality of their reflections would give equality of their unique positive roots. Each is nonidentity because it sends its root to its negative. Both square to one.

## The induced Coxeter matrix

Put
\[
m=\operatorname{ord}(st).
\]
The value \(0\) denotes infinite order in the Lean Coxeter-matrix convention. The induced matrix, indexed by two elements, is
\[
M_P=\begin{pmatrix}1&m\\ m&1\end{pmatrix}.
\]
The [[node:kl.dihedral.two_involutions|two-involution theorem]] supplies a Coxeter system on \(\langle s,t\rangle\). Transporting it through the subgroup equality gives the induced system on the actual subgroup \(D_P\).

The source uses the indices \(\mathrm{false},\mathrm{true}\):
\[
s_{\mathrm{false}}=r_a,\qquad s_{\mathrm{true}}=r_b,
\]
with corresponding ambient simple positive roots \(a,b\).

## Length and order

This Coxeter system has its own length function \(\ell_P\) and strong Bruhat order. Length is the minimum number of these two simple reflections needed to express an element.

The sign and inversion theorems identify this length with the ambient inversion count inside the plane. They also identify its reflection edges with the ambient reflection edges on \(D_P\). These comparisons connect the newly constructed system to the original root geometry.

In the \(A_2\) plane, \(m=3\). In an infinite-dihedral simple-root plane, \(m=0\), recording an infinite product order.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same plane subgroup, different construction.**

**OpenAI notes:** The plane lemma invokes the reflection-subgroup theorem to obtain a canonical Coxeter system, then uses positivity in the plane to show that its rank is two. [dih:plane](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L20).

**Lean (primary):** Finite ambient inversion sets produce angular endpoints. Their plane-simple sign criterion and the plane inversion count prove generation by two endpoint reflections through a count-decreasing conjugation. A two-involution presentation constructs the Coxeter system; the induced signed relation then identifies its inversions. [Decomposition:627](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L627), [Decomposition:869](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L869), [Decomposition:906](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L906), [Decomposition:1010](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1010).

**Role in the proof:** The Blueprint follows the endpoint-existence, generation, presentation, and signed-inversion proofs in that order.
<!-- source-comparison:end -->

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.matrix`: [Decomposition.lean:901](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L901).

`OAI.KLInvariance.TitsSpace.PlaneBasis.system`: [Decomposition.lean:906](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L906).

`OAI.KLInvariance.TitsSpace.PlaneBasis.simpleRoot`: [Decomposition.lean:915](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L915).

`OAI.KLInvariance.TitsSpace.PlaneBasis.system_simple`: [Decomposition.lean:927](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L927).
