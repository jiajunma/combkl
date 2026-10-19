---
id: kl.sheaves.morphism_extension_step
title: Adding one vertex to a partial sheaf morphism
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.sheaf_morphism
- kl.detail.upper_quotient
- kl.algebra.homogeneous_subquotients
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.extend
  - OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.extend_vertex_old
  - OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.extend_vertex_new
  - OAI.KLInvariance.QuotientEdge.descend
  - OAI.KLInvariance.QuotientEdge.descend_apply
  - OAI.KLInvariance.QuotientEdge.kernel_scalar_le
  - OAI.KLInvariance.Graded.ModuleData.quotientHom
  - OAI.KLInvariance.Graded.ModuleData.quotientHom_apply
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:723
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.extend
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:770
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.extend_vertex_old
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:784
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.extend_vertex_new
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:509
    format: lean-location
    note: OAI.KLInvariance.QuotientEdge.descend
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:514
    format: lean-location
    note: OAI.KLInvariance.QuotientEdge.descend_apply
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:520
    format: lean-location
    note: OAI.KLInvariance.QuotientEdge.kernel_scalar_le
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:539
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.quotientHom
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:549
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.quotientHom_apply
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the complete OnHom.extend construction, both preservation lemmas,
    QuotientEdge.descend and the graded quotientHom. Explained kernel containment,
    homogeneous preimages, old/new edge cases and the exact partial-morphism domains
    without adding finiteness or freeness assumptions.
tags:
- Kazhdan-Lusztig
- sheaf-operations
---

# Adding one vertex to a partial sheaf morphism

Let \(k\) be a field and \(B,C\) be graded sheaves over a commutative \(k\)-algebra \(A\) on an ordered graph, and let both satisfy the upper-quotient rule for labels \(\alpha_e\). Let \(U\) be upper, \(x\notin U\), and suppose every vertex strictly above \(x\) lies in \(U\).

Let \(j\) be a partial degree-zero morphism on \(U\). Suppose a degree-zero map \(l_x:B^x\to C^x\) satisfies, for every outgoing edge \(e:x\to y\),
\[
j_e\rho^{B,-}_e=\rho^{C,-}_e l_x.
\]
Then \(j\) extends to a partial morphism on \(U\cup\{x\}\), with vertex map \(l_x\) at \(x\), and with all its old vertex and edge maps retained.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Graded extension preceding local decomposition.**

**OpenAI notes:** The local-ring decomposition descends through the coset vertices, lifting stalk maps over the common boundary image and retaining both endpoint restrictions. [loc:decomposition](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L285).

**Lean (primary):** The graded morphism-extension theorem works over a connected nonnegatively graded Noetherian domain. A homogeneous free-basis lift constructs the next stalk map, upper quotients construct the incoming edge maps, and finite-complement induction extends the partial morphism. [SheafMorphisms:675](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L675), [SheafMorphisms:723](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L723), [SheafMorphisms:834](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L834).

**Role in the proof:** This graded extension is used in boundary recognition and splitting. The ungraded local-ring decomposition is a later construction with its own local-ring and model hypotheses.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Specify the new vertex maps

At \(x\), use \(l_x\). At a vertex of \(U\), keep its old \(j_y\). These cases are disjoint because \(x\notin U\), and every map has degree zero.

For edges with target in \(U\), keep the old \(j_e\). New edge maps are needed exactly for edges \(e:z\to x\).

### Step 2. Descend the new upper stalk map to an incoming edge

For \(e:z\to x\), the upper maps are surjective and satisfy
\[
\ker\rho^{B,+}_e=\alpha_eB^x,\qquad
\ker\rho^{C,+}_e=\alpha_eC^x.
\]
If \(\rho^{B,+}_e(v)=0\), write \(v=\alpha_ew\). Then
\[
\rho^{C,+}_e(l_xv)
=\rho^{C,+}_e(\alpha_el_xw)=0.
\]
Thus the kernel of \(\rho^{B,+}_e\) is contained in the kernel of
\(\rho^{C,+}_e l_x\).

There is consequently a well-defined linear map on the edge modules, characterized by
\[
j'_e(\rho^{B,+}_e(v))=\rho^{C,+}_e(l_xv).
\]
Existence follows by factoring through \(B^x/\ker\rho^{B,+}_e\); surjectivity of the upper map identifies that quotient with \(B^e\). The kernel containment makes the value independent of the preimage.

### Step 3. Check the degree of the descended map

If \(w\in B^e\) has degree \(n\), choose a homogeneous preimage \(v\in B^x_n\) under \(\rho^{B,+}_e\). Such a preimage is obtained by taking the degree-\(n\) component of any preimage.

Both \(l_x\) and \(\rho^{C,+}_e\) preserve degree, so
\[
j'_e(w)=\rho^{C,+}_e(l_xv)\in C^e_n.
\]
This is the graded quotientHom construction in the source.

### Step 4. Verify all upper squares

For an edge ending at \(x\), the defining equation of \(j'_e\) is exactly the upper commuting square.

For an edge ending in \(U\), both its edge map and its upper vertex map are unchanged, so the old upper square applies.

### Step 5. Verify all lower squares

If an edge starts at \(x\), its target is strictly above \(x\), hence lies in \(U\). Its edge map is unchanged, and its lower square is exactly the assumed equation for \(l_x\).

If its source lies in \(U\), upper closure puts its target in \(U\); all relevant maps are old and satisfy the lower square.

Finally, an edge ending at \(x\) has source outside \(U\cup\{x\}\). Its source is different from \(x\) by strict increase. If it belonged to \(U\), upper closure would put \(x\) in \(U\), a contradiction. Thus this edge contributes only the upper square to the new partial-morphism data, already checked in Step 4.

These cases verify every required square and preserve all previously defined maps.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.extend`: [SheafMorphisms.lean:723](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L723).

`OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.extend_vertex_old`: [SheafMorphisms.lean:770](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L770).

`OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.extend_vertex_new`: [SheafMorphisms.lean:784](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L784).

`OAI.KLInvariance.QuotientEdge.descend`: [SheafMorphisms.lean:509](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L509).

`OAI.KLInvariance.QuotientEdge.descend_apply`: [SheafMorphisms.lean:514](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L514).

`OAI.KLInvariance.QuotientEdge.kernel_scalar_le`: [SheafMorphisms.lean:520](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L520).

`OAI.KLInvariance.Graded.ModuleData.quotientHom`: [SheafMorphisms.lean:539](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L539).

`OAI.KLInvariance.Graded.ModuleData.quotientHom_apply`: [SheafMorphisms.lean:549](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L549).
