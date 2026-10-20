---
id: kl.detail.edge_images
title: Lower and upper images in the same edge module
kind: definition
status: formalized
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.sheaves.upward_kernel
- kl.detail.graded_sheaf
- kl.algebra.homogeneous_subquotients
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.upwardSubmodule
  - OAI.KLInvariance.MomentGraph.GradedSheaf.lowerImage
  - OAI.KLInvariance.MomentGraph.GradedSheaf.upperImage
  - OAI.KLInvariance.MomentGraph.GradedSheaf.upperImage_homogeneous
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:31
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.upwardSubmodule
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:362
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.lowerImage
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:366
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.upperImage
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:371
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.upperImage_homogeneous
  - artifact: openai-kl-paper
    locator: 5. Comparison of edge images; edge:bound
    format: section
    note: Selected endpoint images, local scaled equality and the global edge-image
      bound.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the actual polynomial graded lowerImage/upperImage definitions and
    upwardSubmodule as the underlying ungraded selected kernel. Expanded the membership
    witnesses, both homogeneous-component arguments and a complete two-edge example.
    Preserved the general ungraded notation used in the transport lemmas.
tags:
- Kazhdan-Lusztig
- embedded-images
---

# Lower and upper images in the same edge module

Let \(R\) be a commutative ring, \(G\) an ordered graph, and \(B\) a sheaf of \(R\)-modules on \(G\). Fix an edge \(e:x\to y\), and choose outgoing-edge sets
\[
F\subseteq\operatorname{Out}(x),\qquad
H\subseteq\operatorname{Out}(y).
\]
The selected kernels are
\[
K_x(F)=\{v\in B^x:\rho^-_f(v)=0\text{ for every }f\in F\},
\]
and the corresponding kernel \(K_y(H)\) at \(y\).

The **lower edge image** and **upper edge image** are
\[
L_e(F)=\rho^-_e(K_x(F)),\qquad
U_e(H)=\rho^+_e(K_y(H)).
\]
Both are submodules of \(B^e\). Membership records an actual stalk preimage:
\[
z\in L_e(F)\ \Longleftrightarrow
\exists v\in K_x(F),\ \rho^-_e(v)=z,
\]
\[
z\in U_e(H)\ \Longleftrightarrow
\exists w\in K_y(H),\ \rho^+_e(w)=z.
\]

## The named graded constructions

The source's lowerImage and upperImage implement these formulas for a graded sheaf over the polynomial coefficient algebra. Its upwardSubmodule is exactly the selected kernel of the underlying ungraded sheaf, typed as a submodule of the graded stalk.

Thus forgetting grading preserves the same sets, restrictions and embedded images. A later ungraded sheaf decomposition acts on these very submodules.

## Homogeneous components

For a graded sheaf whose restrictions have degree zero, every selected kernel is closed under homogeneous components. If \(v\in K_x(F)\), then for any selected edge \(f\),
\[
\rho^-_f(v_n)=(\rho^-_f(v))_n=0.
\]
Hence \(v_n\in K_x(F)\).

If \(z=\rho^-_e(v)\), its degree-\(n\) component is
\[
z_n=\rho^-_e(v_n)\in L_e(F).
\]
The upper map gives the same argument for \(U_e(H)\). This is the component calculation behind upperImage_homogeneous and the graded image constructions used in Hilbert comparison.

## Two outgoing conditions in polynomial coordinates

Take \(R=k[a,b]\) over a field \(k\), and a graph with two edges
\[
e:x\to y\text{ labelled }a,\qquad
f:x\to z\text{ labelled }b.
\]
Put \(R\) at each vertex, \(R/(a)\) on \(e\), \(R/(b)\) on \(f\), and use quotient maps at both endpoints.

Choose \(F=\{f\}\) and \(H=\varnothing\) at \(y\). Then
\[
K_x(F)=bR,\qquad K_y(H)=R.
\]
Inside the current edge module \(E=R/(a)\),
\[
L_e(F)=\overline b\,E,\qquad U_e(H)=E.
\]
The extra condition along \(f\) has become a divisibility condition in the quotient belonging to \(e\). These are the two embedded images compared by a scalar equality.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The same embedded images through one edge component.**

**OpenAI notes:** The model decomposition carries both localized kernels and their endpoint images into the model summands. Its single edge component carries both comparison submodules, and linearity carries the correction scalar through that same map. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** Selected-kernel membership and both image equalities are proved for arbitrary sheaf isomorphisms over a commutative ring. ScaledImages is an elementwise witness equivalence, identified with submodule equality. Coordinatewise witness transport proves the product and model-sum statements with one common scalar. [PositiveTransfer:362](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L362), [PositiveTransfer:366](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L366), [CharacterReciprocity:443](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L443), [GradedSheaves:631](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L631), [GradedSheaves:639](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L639), [TerminalKernels:19](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L19), [CharacterReciprocity:548](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L548).

**Role in the proof:** The Blueprint defines the actual submodules and witnesses before transporting them. The generic ungraded transport is the one applied to the local model decomposition.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.upwardSubmodule`: [MinimalExtensions.lean:31](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L31).

`OAI.KLInvariance.MomentGraph.GradedSheaf.lowerImage`: [PositiveTransfer.lean:362](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L362).

`OAI.KLInvariance.MomentGraph.GradedSheaf.upperImage`: [PositiveTransfer.lean:366](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L366).

`OAI.KLInvariance.MomentGraph.GradedSheaf.upperImage_homogeneous`: [PositiveTransfer.lean:371](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L371).
