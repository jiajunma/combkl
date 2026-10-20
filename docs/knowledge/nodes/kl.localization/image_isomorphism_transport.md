---
id: kl.local.image_isomorphism_transport
title: Selected kernels and scaled images under sheaf isomorphisms
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.detail.edge_images
- kl.detail.scaled_images
- kl.detail.sheaf_isomorphisms
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.Iso.upwardKernel_iff
  - OAI.KLInvariance.MomentGraph.Sheaf.Iso.map_upwardKernel
  - OAI.KLInvariance.MomentGraph.Sheaf.Iso.map_lowerImage
  - OAI.KLInvariance.MomentGraph.Sheaf.Iso.map_upperImage
  - OAI.KLInvariance.MomentGraph.Sheaf.Iso.scaledImages
  - OAI.KLInvariance.EmbeddedModule.map_scaled
  - OAI.KLInvariance.EmbeddedModule.map_eq_scaled_iff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:609
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.Iso.upwardKernel_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:620
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.Iso.map_upwardKernel
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:631
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.Iso.map_lowerImage
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:639
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.Iso.map_upperImage
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:19
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.Iso.scaledImages
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:657
    format: lean-location
    note: OAI.KLInvariance.EmbeddedModule.map_scaled
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:665
    format: lean-location
    note: OAI.KLInvariance.EmbeddedModule.map_eq_scaled_iff
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read selected-kernel transport and both endpoint image lemmas, EmbeddedModule.map_scaled/map_eq_scaled_iff
    and Iso.scaledImages. Expanded both kernel containments, both image containments,
    scalar commutation and inverse transport; retained arbitrary coefficients and
    no grading, quotient or finiteness hypothesis.
tags:
- Kazhdan-Lusztig
- embedded-images
---

# Selected kernels and scaled images under sheaf isomorphisms

Let \(R\) be a commutative ring, \(G\) an ordered graph, and
\(j:B\simeq C\) an \(R\)-linear sheaf isomorphism. Write \(j_x\) for its vertex maps and \(j_e\) for its edge maps.

For any vertex \(x\) and outgoing selection \(F\),
\[
j_x(K_x^B(F))=K_x^C(F).
\]
For an edge \(e:x\to y\) and selections \(F,H\) at its endpoints,
\[
j_e(L_e^B(F))=L_e^C(F),\qquad
j_e(U_e^B(H))=U_e^C(H).
\]
Consequently, for every scalar \(r\in R\),
\[
L_e^B(F)=rU_e^B(H)
\quad\Longleftrightarrow\quad
L_e^C(F)=rU_e^C(H).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The same embedded images through one edge component.**

**OpenAI notes:** The model decomposition carries both localized kernels and their endpoint images into the model summands. Its single edge component carries both comparison submodules, and linearity carries the correction scalar through that same map. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** Selected-kernel membership and both image equalities are proved for arbitrary sheaf isomorphisms over a commutative ring. ScaledImages is an elementwise witness equivalence, identified with submodule equality. Coordinatewise witness transport proves the product and model-sum statements with one common scalar. [PositiveTransfer:362](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L362), [PositiveTransfer:366](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L366), [CharacterReciprocity:443](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L443), [GradedSheaves:631](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L631), [GradedSheaves:639](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L639), [TerminalKernels:19](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L19), [CharacterReciprocity:548](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L548).

**Role in the proof:** The Blueprint defines the actual submodules and witnesses before transporting them. The generic ungraded transport is the one applied to the local model decomposition.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Transport a selected zero restriction

For an outgoing edge \(f\) from \(x\), the lower restriction square is
\[
\rho^{C,-}_f(j_xv)=j_f(\rho^{B,-}_fv).
\]
If \(\rho^{B,-}_f(v)=0\), linearity makes the right side and hence the left restriction zero.

Conversely, if the left restriction is zero, injectivity of \(j_f\) forces \(\rho^{B,-}_fv=0\). Applying this to every \(f\in F\) gives
\[
j_xv\in K_x^C(F)\quad\Longleftrightarrow\quad v\in K_x^B(F).
\]

### Step 2. Prove equality of the transported kernel submodules

Step 1 gives the containment
\(j_x(K_x^B(F))\subseteq K_x^C(F)\).

For the reverse containment, take \(w\in K_x^C(F)\) and put \(v=j_x^{-1}w\). Step 1 puts \(v\) in \(K_x^B(F)\), and \(j_xv=w\). Thus the two submodules are equal.

### Step 3. Transport both endpoint images

A value in \(L_e^B(F)\) has the form \(\rho^{B,-}_e(v)\) with \(v\in K_x^B(F)\). The lower square gives
\[
j_e(\rho^{B,-}_e(v))=\rho^{C,-}_e(j_xv).
\]
Step 2 places \(j_xv\) in the corresponding selected kernel of \(C\). This proves one containment of lower images. Using \(j_x^{-1}\) for a lower witness in \(C\) proves the reverse containment.

The upper square
\[
j_e(\rho^{B,+}_e(w))=\rho^{C,+}_e(j_yw)
\]
gives the same argument at \(y\), proving the upper-image equality. Both equalities use the single edge map \(j_e\).

### Step 4. Commute a scalar image with a linear isomorphism

For any \(R\)-linear isomorphism \(T:M\simeq N\), scalar \(r\) and submodule \(J\subseteq M\),
\[
T(rJ)=rT(J).
\]
Indeed \(T(rw)=rT(w)\) gives the forward containment. Every value \(rT(w)\), with \(w\in J\), is the image of \(rw\in rJ\), giving the reverse containment.

For another submodule \(I\subseteq M\), if \(T(I)=rT(J)\), apply \(T^{-1}\) and the same identity to obtain \(I=rJ\). The forward implication follows by applying \(T\). These are the generic EmbeddedModule scalar-transport formulas.

### Step 5. Transfer the scaled equality in both directions

Apply Step 4 to \(T=j_e\). If
\(L_e^B(F)=rU_e^B(H)\), then Step 3 gives
\[
L_e^C(F)
=j_e(L_e^B(F))
=j_e(rU_e^B(H))
=rj_e(U_e^B(H))
=rU_e^C(H).
\]
Apply the same argument to the inverse sheaf isomorphism for the converse. This proves invariance of the ScaledImages proposition.

For the local model decomposition, \(j_e\) is the actual edge component of its sheaf isomorphism. Its \(R_P\)-linearity is exactly the scalar compatibility used in Step 4.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.Iso.upwardKernel_iff`: [GradedSheaves.lean:609](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L609).

`OAI.KLInvariance.MomentGraph.Sheaf.Iso.map_upwardKernel`: [GradedSheaves.lean:620](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L620).

`OAI.KLInvariance.MomentGraph.Sheaf.Iso.map_lowerImage`: [GradedSheaves.lean:631](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L631).

`OAI.KLInvariance.MomentGraph.Sheaf.Iso.map_upperImage`: [GradedSheaves.lean:639](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L639).

`OAI.KLInvariance.MomentGraph.Sheaf.Iso.scaledImages`: [TerminalKernels.lean:19](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L19).

`OAI.KLInvariance.EmbeddedModule.map_scaled`: [GradedSheaves.lean:657](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L657).

`OAI.KLInvariance.EmbeddedModule.map_eq_scaled_iff`: [GradedSheaves.lean:665](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L665).
