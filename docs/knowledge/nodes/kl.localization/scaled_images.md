---
id: kl.detail.scaled_images
title: Scaled equality of embedded edge images
kind: definition
status: formalized
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.detail.edge_images
- kl.sheaves.upward_kernel
- kl.algebra.linear_ideals
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  - GradedSheaves
  declarations:
  - OAI.KLInvariance.EmbeddedModule.scaled
  - OAI.KLInvariance.MomentGraph.Sheaf.ScaledImages
  - OAI.KLInvariance.MomentGraph.Sheaf.scaledImages_iff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:654
    format: lean-location
    note: OAI.KLInvariance.EmbeddedModule.scaled
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:443
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.ScaledImages
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:450
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.scaledImages_iff
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
  verdict: Read EmbeddedModule.scaled, ScaledImages and both directions of scaledImages_iff.
    Defined the scalar image for arbitrary modules, expanded both layers of membership
    witnesses, kept the arbitrary commutative ring and scalar, and distinguished the
    local equality, global inclusion and later global equality without changing the
    underlying images.
tags:
- Kazhdan-Lusztig
- embedded-images
---

# Scaled equality of embedded edge images

Let \(R\) be a commutative ring, \(M\) an \(R\)-module and \(J\subseteq M\) a submodule. For \(r\in R\), the **scalar image** of \(J\) is
\[
rJ=\{rw:w\in J\}.
\]
It is the image of \(J\) under the linear map \(w\mapsto rw\). The source calls this construction EmbeddedModule.scaled.

Now let \(B\) be a sheaf of \(R\)-modules on an ordered graph, fix \(e:x\to y\), and choose outgoing selections \(F,H\) at the two endpoints. **Scaled image equality** means
\[
L_e(F)=r\,U_e(H)\quad\text{as submodules of }B^e.
\]
The source's ScaledImages proposition states it through witnesses: for every \(z\in B^e\),
\[
\bigl(\exists v\in K_x(F),\ \rho^-_e(v)=z\bigr)
\quad\Longleftrightarrow\quad
\bigl(\exists w\in K_y(H),\ r\rho^+_e(w)=z\bigr).
\]

## Equivalence with the submodule equality

Membership in \(L_e(F)\) is exactly the left witness statement.

Membership in \(rU_e(H)\) means that \(z=rt\) for some \(t\in U_e(H)\). Write \(t=\rho^+_e(w)\), with \(w\in K_y(H)\). This gives the right witness statement.

Conversely a witness \(w\) on the right supplies \(t=\rho^+_e(w)\in U_e(H)\), with \(rt=z\). Thus the witness equivalence for every \(z\) is precisely equality of the two submodules. This is scaledImages_iff.

## The two-edge example

Use the two-edge sheaf over \(R=k[a,b]\), with current edge \(e:x\to y\) labelled by \(a\), second edge \(f:x\to z\) labelled by \(b\), and quotient restrictions from rank-one stalks.

For \(F=\{f\}\), \(H=\varnothing\), the current edge module is \(E=R/(a)\), and
\[
L_e(F)=\overline b\,E=b\,U_e(H).
\]
A value \(\overline b\,[u]\) has lower witness \(bu\in bR\) and upper witness \(u\in R\), with the scalar \(r=b\). These witnesses realize both sides of the defining equivalence.

## The role of the coefficient action

The scalar \(r\) acts through the coefficient ring of the current sheaf. In a localized coset model this ring is \(R_P\), and the edge module carries the quotient action through \(R_P/(\gamma_e)\). The correction scalar is the image in \(R_P\) of the polynomial edge-factor lift.

Local comparison proves a scaled equality after localization. The global membership argument then gives an inclusion in the original edge module, and the later Hilbert equality argument makes that global inclusion an equality. The same definitions of the embedded images are used at each stage.

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

`OAI.KLInvariance.EmbeddedModule.scaled`: [GradedSheaves.lean:654](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L654).

`OAI.KLInvariance.MomentGraph.Sheaf.ScaledImages`: [CharacterReciprocity.lean:443](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L443).

`OAI.KLInvariance.MomentGraph.Sheaf.scaledImages_iff`: [CharacterReciprocity.lean:450](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L450).
