---
id: kl.notes.dihedral_models
title: Induced ambient labels and dihedral structure models
kind: definition
status: formalized
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.detail.structure_sheaves
- kl.coxeter.external_vertices
- kl.dihedral.odd_reflection_edges
- kl.detail.root_reflection_correspondence
- kl.dihedral.induced_system
- kl.algebra.coefficient_algebra
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.Dihedral.inducedRoot
  - OAI.KLInvariance.Dihedral.inducedLabel
  - OAI.KLInvariance.Dihedral.interpolationRoot
  - OAI.KLInvariance.TitsSpace.PlaneBasis.modelLabel
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:464
    format: lean-location
    note: OAI.KLInvariance.Dihedral.inducedRoot
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:467
    format: lean-location
    note: OAI.KLInvariance.Dihedral.inducedLabel
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:248
    format: lean-location
    note: OAI.KLInvariance.Dihedral.interpolationRoot
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:612
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.modelLabel
  - artifact: openai-kl-paper
    locator: 4. Localization at a root plane; loc:models
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read inducedRoot/inducedLabel for a reflection-preserving group homomorphism,
    the external interpolationRoot, and the PlaneBasis modelLabel specialization.
    Kept injectivity as the later flabbiness hypothesis and the intrinsic graph/order
    separate from ambient coefficient data.
tags:
- Kazhdan-Lusztig
- interpolation
---

# Induced ambient labels and dihedral structure models

Let \(H\) be a two-generator Coxeter system with length \(\ell_H\), and \(W\) a finite-generator ambient Coxeter system. Choose a group homomorphism
\[
\phi:H\to W
\]
that sends every reflection of \(H\) to an ambient reflection. Let \(A\) be the polynomial algebra of the ambient extended realization, with coefficient map \(\Lambda:V\to A\).

## Roots and labels of the induced graph

Fix an interval \([1,b]_H\). For an edge \(e:x\to_Hy\), its left reflection label is
\(\tau_e=yx^{-1}\). Let
\[
\beta_e=\text{the canonical positive ambient root representing }\phi(\tau_e).
\]
This is inducedRoot. Its **induced polynomial label** is
\[
\alpha_e=\Lambda(i_0\beta_e)\in A,
\]
named inducedLabel.

The graph and its order are those of \(H\). The homomorphism \(\phi\) supplies the ambient reflection roots used as coefficients.

## The model centered at a lower vertex

For \(c\le_H b\), use these labels in the structure sheaf
\[
\mathcal O_c^x=
\begin{cases}A,&x\le_Hc,\\0,&x\not\le_Hc,\end{cases}
\]
with edge module \(A/(\alpha_e)\) when \(t(e)\le_Hc\), and zero otherwise. Both restrictions on a supported edge are reduction modulo \(\alpha_e\).

The [[node:kl.local.structure_sheaf_properties|basic structure-sheaf properties]] give finite free stalks, global generation and the upper-quotient rule. When \(\phi\) is injective, the [[node:kl.detail.dihedral_model_properties|dihedral model theorem]] also gives flabbiness by interpolation and flow-down sections.

## Interpolation roots

For \(x,c\in H\) and \(y\in Y(x,c)\), opposite parity makes \(yx^{-1}\) a reflection. Define
\[
a_y=\text{the positive ambient root representing }\phi(yx^{-1}).
\]
This is interpolationRoot. The [[node:kl.local.induced_flow_down|outgoing-index calculation]] identifies \(y\) with the edge \(x\to_Hy\), when used in the interpolation construction; the interpolation label and the induced edge label are then the same polynomial \(\Lambda(i_0a_y)\).

## The root-plane subgroup specialization

For a root plane \(P\) with chosen plane basis, take \(H=D_P\) with its induced Coxeter system and \(\phi\) the subgroup inclusion. The [[node:kl.dihedral.induced_reflections_length|reflection-identification theorem]] proves that this inclusion sends intrinsic reflections to ambient reflections, and the inclusion is injective.

The source calls the resulting polynomial labels modelLabel. The model theorem applies with the full ambient extended realization and these chosen ambient roots.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same model properties, different justification.**

**OpenAI notes:** The induced-model lemma justifies applying the character theorem to the restricted reflection-faithful realization and uses the dihedral character calculation to identify the rank-one model. [loc:models](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L125).

**Lean (primary):** The direct construction first proves parity matching in arbitrary lower Bruhat intervals by a simple-reflection involution. In the dihedral application, orbit-spline factors supply the prescribed values and zeros; their product gives flow-down sections. A finite induction on prescribed upper sets proves flabbiness, while generation and quotient maps follow from the structure-sheaf construction. [DihedralIntervals:616](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L616), [DihedralIntervals:622](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L622), [DihedralIntervals:626](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L626), [SheafMorphisms:252](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L252), [SheafMorphisms:288](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L288), [DihedralIntervals:176](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L176), [DihedralIntervals:251](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L251), [DihedralIntervals:372](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L372).

**Role in the proof:** The Blueprint follows the parity, normal-form prescription, spline product and flow-down correction arguments. Injectivity of the reflection-preserving group map provides distinct factor data and pairwise relatively prime incident labels. These model properties feed the later local-ring decomposition.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.inducedRoot`: [DihedralIntervals.lean:464](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L464).

`OAI.KLInvariance.Dihedral.inducedLabel`: [DihedralIntervals.lean:467](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L467).

`OAI.KLInvariance.Dihedral.interpolationRoot`: [DihedralIntervals.lean:248](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L248).

`OAI.KLInvariance.TitsSpace.PlaneBasis.modelLabel`: [DihedralIntervals.lean:612](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L612).
