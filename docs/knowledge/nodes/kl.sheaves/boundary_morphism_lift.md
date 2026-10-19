---
id: kl.sheaves.boundary_morphism_lift
title: Lifting a partial morphism through the boundary image
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.sheaf_morphism
- kl.sheaves.boundary_image_identity
- kl.algebra.homogeneous_lifts
- kl.algebra.homogeneous_subquotients
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.mapAssignment
  - OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.compatible
  - OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.boundary
  - OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.boundaryMap
  - OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.map_stalk_image_le
  - OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.extend_stalk
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:613
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.mapAssignment
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:625
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.compatible
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:639
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.boundary
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:648
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.boundaryMap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:658
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.map_stalk_image_le
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:675
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.extend_stalk
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the partial assignment, boundary map and image-containment constructions,
    then the exact graded-range lift. Retained finite edges, the arbitrary subset
    containing all vertices above x, only source-stalk freeness at x, and both sheaves’
    flabbiness/generation.
tags:
- Kazhdan-Lusztig
- sheaf-operations
---

# Lifting a partial morphism through the boundary image

Let \(k\) be a field and \(A\) a connected nonnegatively graded Noetherian domain over \(k\). Let \(B,C\) be graded sheaves on an ordered graph with finitely many edges. Assume both underlying sheaves are flabby and globally generated.

Let \(j\) be a degree-zero partial morphism on a vertex subset \(U\). Fix a vertex \(x\) with
\[
\{y:x<y\}\subseteq U,
\]
and assume \(B^x\) is free. Write
\[
r_B:B^x\to\partial B_x,\qquad r_C:C^x\to\partial C_x
\]
for the combined outgoing stalk maps, where
\(\partial B_x=\prod_{e:x\to y}B^e\) and
\(\partial C_x=\prod_{e:x\to y}C^e\).
The known edge maps define
\[
j_{\partial x}:\partial B_x\to\partial C_x,\qquad
(v_e)_e\longmapsto(j_e(v_e))_e.
\]

There exists a degree-zero map \(l_x:B^x\to C^x\) satisfying
\[
r_C l_x=j_{\partial x}r_B.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Graded extension preceding local decomposition.**

**OpenAI notes:** The local-ring decomposition descends through the coset vertices, lifting stalk maps over the common boundary image and retaining both endpoint restrictions. [loc:decomposition](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L285).

**Lean (primary):** The graded morphism-extension theorem works over a connected nonnegatively graded Noetherian domain. A homogeneous free-basis lift constructs the next stalk map, upper quotients construct the incoming edge maps, and finite-complement induction extends the partial morphism. [SheafMorphisms:675](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L675), [SheafMorphisms:723](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L723), [SheafMorphisms:834](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L834).

**Role in the proof:** This graded extension is used in boundary recognition and splitting. The ungraded local-ring decomposition is a later construction with its own local-ring and model hypotheses.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Map compatible assignments strictly above the new vertex

Every edge whose source is strictly above \(x\) also has target strictly above \(x\). Both vertices lie in \(U\).

For a section \(f\) above \(x\), define an ambient assignment \(g\) by
\[
g_y=
\begin{cases}
j_y(f_y),&x<y,\\
0,&x\not<y.
\end{cases}
\]
On an edge \(e:y\to z\) with \(x<y\), the two partial-morphism squares give
\[
\rho^{C,-}_e(j_yf_y)
=j_e(\rho^{B,-}_ef_y)
=j_e(\rho^{B,+}_ef_z)
=\rho^{C,+}_e(j_zf_z).
\]
Thus \(g\) is a section of \(C\) strictly above \(x\).

### Step 2. Map boundary tuples componentwise

Every outgoing target of \(x\) lies in \(U\), so its edge map \(j_e\) is part of the existing partial morphism. Applying these maps componentwise defines \(j_{\partial x}\).

Each \(j_e\) has degree zero, so \(j_{\partial x}\) preserves the product grading. Let \(b_B\) and \(b_C\) be the boundary maps from sections strictly above \(x\): their \(e\)-coordinates are the upper restrictions of the value at \(t(e)\). For the section \(f\) from Step 1 and its image \(g\), the upper commuting squares give
\[
j_{\partial x}(b_B(f))=b_C(g).
\]
Hence \(j_{\partial x}\) sends the boundary image of \(B\) into that of \(C\).

### Step 3. Replace the boundary images by the stalk-map images

The [[node:kl.sheaves.boundary_image_identity|boundary-image theorem]] applies to each sheaf because both are flabby and globally generated. It gives
\[
\operatorname{im}r_B=\operatorname{im}b_B,
\qquad
\operatorname{im}r_C=\operatorname{im}b_C.
\]
Together with Step 2, this yields
\[
j_{\partial x}(\operatorname{im}r_B)\subseteq\operatorname{im}r_C.
\]

### Step 4. Restrict the target to a graded image

Let \(T=\operatorname{im}r_C\), with its induced grading. The inclusion from Step 3 defines a degree-zero map
\[
g:B^x\to T,\qquad g(v)=j_{\partial x}(r_Bv).
\]
Also let
\[
\pi:C^x\twoheadrightarrow T
\]
be \(r_C\) with its codomain restricted to its image. Every vector of \(T\) has an \(r_C\)-preimage, so \(\pi\) is surjective.

### Step 5. Lift using a homogeneous free basis

The connected nonnegative Noetherian-domain assumptions supply a finite homogeneous basis \((m_i)\) of the free stalk \(B^x\). If \(m_i\) has degree \(d_i\), choose a preimage of \(g(m_i)\) under \(\pi\), then take its degree-\(d_i\) component. Since \(\pi\) preserves degree, the resulting vector \(v_i\) still satisfies
\[
\pi(v_i)=g(m_i).
\]
Extend \(m_i\mapsto v_i\) linearly. The [[node:kl.algebra.homogeneous_lifts|homogeneous lifting theorem]] proves that the resulting \(l_x\) has degree zero and \(\pi l_x=g\).

Finally, include \(T\) into \(\partial C_x\). This changes the last equation into
\(r_C l_x=j_{\partial x}r_B\), as required.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.mapAssignment`: [SheafMorphisms.lean:613](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L613).

`OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.compatible`: [SheafMorphisms.lean:625](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L625).

`OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.boundary`: [SheafMorphisms.lean:639](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L639).

`OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.boundaryMap`: [SheafMorphisms.lean:648](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L648).

`OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.map_stalk_image_le`: [SheafMorphisms.lean:658](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L658).

`OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.extend_stalk`: [SheafMorphisms.lean:675](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L675).
