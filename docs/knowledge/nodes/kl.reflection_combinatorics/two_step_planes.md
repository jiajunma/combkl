---
id: kl.dihedral.two_step_planes
title: Two-edge root planes and confinement to a plane coset
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.realization.common_reflection_plane
- kl.realization.root_planes
- kl.realization.plane_reflection_membership
- kl.detail.plane_basis
- kl.foundations.bruhat_step
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.TitsSpace.graphRoot_ne_of_same_source
  - OAI.KLInvariance.TitsSpace.graphRoot_ne_of_path
  - OAI.KLInvariance.TitsSpace.graphRoot_square_plane
  - OAI.KLInvariance.TitsSpace.graphRoot_mem_of_coset
  - OAI.KLInvariance.TitsSpace.mem_coset_of_graphRoot
  - OAI.KLInvariance.TitsSpace.PlaneBasis.graphRoot_mem
  - OAI.KLInvariance.TitsSpace.PlaneBasis.graphRoot_path_plane
  - OAI.KLInvariance.TitsSpace.PlaneBasis.twoStep_mem_coset
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1432
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.graphRoot_ne_of_same_source
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1440
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.graphRoot_ne_of_path
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1447
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.graphRoot_square_plane
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:381
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.graphRoot_mem_of_coset
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:388
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.mem_coset_of_graphRoot
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:265
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.graphRoot_mem
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:274
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.graphRoot_path_plane
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:283
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.twoStep_mem_coset
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient/coset domains, intrinsic ranks, injectivity, full-range
    and exact-intermediate hypotheses explicit?
  verdict: Checked square-plane equality through the nondegenerate extension and projection,
    both root-distinctness arguments, membership propagation and coset confinement
    without imposing a minimal-representative hypothesis.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Two-edge root planes and confinement to a plane coset

Let \(W\) be a finite-generator real Coxeter system. For an upward reflection edge \(p\to q\), denote its positive ambient root by \(\alpha_{pq}\); its left reflection is \(qp^{-1}\). Write \(P(a,b)=\operatorname{span}_{\mathbb R}\{a,b\}\).

Suppose there are two paths
\[
x\longrightarrow a\longrightarrow z,\qquad
x\longrightarrow b\longrightarrow z,\qquad a\ne b.
\]
Then
\[
P(\alpha_{xa},\alpha_{az})
=P(\alpha_{xa},\alpha_{xb})
=P(\alpha_{xb},\alpha_{bz}).
\]
In particular all four roots lie in one plane, and the two outgoing roots at \(x\) span it.

Now fix a root plane \(P\), a plane basis \(B\), its subgroup \(D\), and any \(a_0\in W\). If
\[
ga_0\longrightarrow ha_0\longrightarrow ka_0
\qquad(g,h,k\in D),
\]
then every other two-edge path \(ga_0\to z\to ka_0\) has its intermediate vertex in the same coset:
\[
z a_0^{-1}\in D.
\]
This confinement assertion holds for every coset representative \(a_0\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The common-plane argument in the actual ambient realization.**

**OpenAI notes:** The notes identify the root plane of two paths by equality of their two-reflection products. In the transport proof, diamonds propagate the initial plane through all relative ranks. [dih:plane](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L20), [dih:transport](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L276).

**Lean (primary):** The product argument is applied in the nondegenerate extended realization and projected to the original root space. Coset membership propagates along a root in that plane. dihedral_image_in_plane organizes the propagation as strong induction on the absolute source length, selecting one vertex two ranks below and two vertices one rank below. [ReflectionSchedules:1447](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1447), [DyerPaths:283](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L283), [DyerPaths:400](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L400).

**Role in the proof:** The Blueprint states the plane equality, the coset-confinement result and the entire graph-image induction separately, including the first two ranks and the boundary case for the predecessor.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Distinguish the roots used to form the planes

Two edges \(x\to a,x\to b\) with the same positive root would have the same reflection. Then \(ax^{-1}=bx^{-1}\), so \(a=b\). Thus their roots are distinct when the endpoints are distinct.

For consecutive edges \(x\to a\to z\), equal roots would give a common reflection \(r\) with \(a=rx\) and \(z=ra=r^2x=x\). This contradicts the strict increase of length along the path. Their roots are also distinct.

Distinct positive real roots are linearly independent. Each pair in the statement therefore spans a two-dimensional root plane.

### Step 2. Use the two equal products of reflections

The two paths give the group identity
\[
(za^{-1})(ax^{-1})=zx^{-1}=(zb^{-1})(bx^{-1}).
\]
Apply the [[node:kl.realization.common_reflection_plane|common-reflection-plane theorem]] to these two products. It applies in the nondegenerate extended realization: each embedded root has square \(2\) under the extended bilinear form, and the consecutive pairs are independent by Step 1. It gives
\[
\operatorname{span}\{\widetilde\alpha_{az},\widetilde\alpha_{xa}\}
=\operatorname{span}\{\widetilde\alpha_{bz},\widetilde\alpha_{xb}\}.
\]
Projection from the extended space to the original root space sends each embedded root to the original root and sends a span to the span of its images. Hence
\[
P(\alpha_{xa},\alpha_{az})=P(\alpha_{xb},\alpha_{bz}).
\]

The first plane contains \(\alpha_{xa}\) and, by this equality, \(\alpha_{xb}\). These two roots are independent by Step 1, so they already span the two-dimensional plane. This proves the middle equality in the statement as well.

### Step 3. Locate roots of edges between vertices of a plane coset

An edge \(pa_0\to qa_0\), with \(p,q\in D\), has reflection
\[
(qa_0)(pa_0)^{-1}=qp^{-1}\in D.
\]
The [[node:kl.realization.plane_reflection_membership|plane-reflection membership theorem]] says that its positive root belongs to \(P\).

Conversely, if \(x a_0^{-1}\in D\) and the root of an edge \(x\to y\) lies in \(P\), that theorem gives \(yx^{-1}\in D\). Multiplication yields
\[
y a_0^{-1}=(yx^{-1})(x a_0^{-1})\in D.
\]
This is the propagation of coset membership along an edge whose root lies in the plane.

### Step 4. Confine every alternative intermediate vertex

In the given path \(ga_0\to ha_0\to ka_0\), Step 3 puts both roots in \(P\). They are independent by Step 1 and therefore span all of \(P\).

If the alternative intermediate is \(z=ha_0\), its coset membership is already known. Otherwise apply Step 2 to the two paths. The root of \(ga_0\to z\) belongs to their common plane \(P\). The converse direction of Step 3, starting from \(ga_0\), gives \(z a_0^{-1}\in D\), as required.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.graphRoot_ne_of_same_source`: [ReflectionSchedules.lean:1432](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1432).

`OAI.KLInvariance.TitsSpace.graphRoot_ne_of_path`: [ReflectionSchedules.lean:1440](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1440).

`OAI.KLInvariance.TitsSpace.graphRoot_square_plane`: [ReflectionSchedules.lean:1447](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1447).

`OAI.KLInvariance.TitsSpace.graphRoot_mem_of_coset`: [DyerPaths.lean:381](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L381).

`OAI.KLInvariance.TitsSpace.mem_coset_of_graphRoot`: [DyerPaths.lean:388](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L388).

`OAI.KLInvariance.TitsSpace.PlaneBasis.graphRoot_mem`: [DyerPaths.lean:265](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L265).

`OAI.KLInvariance.TitsSpace.PlaneBasis.graphRoot_path_plane`: [DyerPaths.lean:274](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L274).

`OAI.KLInvariance.TitsSpace.PlaneBasis.twoStep_mem_coset`: [DyerPaths.lean:283](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L283).
