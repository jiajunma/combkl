---
id: kl.local.induced_flow_down
title: Interpolation produces the prescribed flow-down sections
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.notes.dihedral_models
- kl.local.dihedral_interpolation
- kl.local.flow_down
- kl.coxeter.external_vertices
- kl.coxeter.dihedral_bruhat_order
- kl.dihedral.odd_reflection_edges
- kl.detail.structure_sheaves
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.Dihedral.external_step
  - OAI.KLInvariance.Dihedral.step_external
  - OAI.KLInvariance.Dihedral.externalEdge
  - OAI.KLInvariance.Dihedral.externalEdge_mem
  - OAI.KLInvariance.Dihedral.outgoingEquiv
  - OAI.KLInvariance.Dihedral.interpolation_product
  - OAI.KLInvariance.Dihedral.hasFlowDown
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:470
    format: lean-location
    note: OAI.KLInvariance.Dihedral.external_step
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:480
    format: lean-location
    note: OAI.KLInvariance.Dihedral.step_external
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:491
    format: lean-location
    note: OAI.KLInvariance.Dihedral.externalEdge
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:496
    format: lean-location
    note: OAI.KLInvariance.Dihedral.externalEdge_mem
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:503
    format: lean-location
    note: OAI.KLInvariance.Dihedral.outgoingEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:521
    format: lean-location
    note: OAI.KLInvariance.Dihedral.interpolation_product
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:531
    format: lean-location
    note: OAI.KLInvariance.Dihedral.hasFlowDown
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read both external-step directions, externalEdge, the inverse maps in outgoingEquiv,
    exact canonical-label product reindexing and the construction of the supported
    assignment from F. Preserved all order, parity and support cases.
tags:
- Kazhdan-Lusztig
- interpolation
---

# Interpolation produces the prescribed flow-down sections

Let \(H\) be a two-generator Coxeter system and let \(\phi:H\to W\) be an injective homomorphism to a finite-generator Coxeter system, carrying reflections to reflections. On \([1,b]_H\), use the induced ambient polynomial labels.

For every model center \(c\le_Hb\), the structure model \(\mathcal O_c\) has flow-down sections:
\[
\forall x\le_Hc,\quad
\exists\theta_x\text{ global},\qquad
\theta_x(x)=P_c(x),\qquad
\theta_x(y)=0\ (y\not\le_Hx).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same model properties, different justification.**

**OpenAI notes:** The induced-model lemma justifies applying the character theorem to the restricted reflection-faithful realization and uses the dihedral character calculation to identify the rank-one model. [loc:models](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L125).

**Lean (primary):** The direct construction first proves parity matching in arbitrary lower Bruhat intervals by a simple-reflection involution. In the dihedral application, orbit-spline factors supply the prescribed values and zeros; their product gives flow-down sections. A finite induction on prescribed upper sets proves flabbiness, while generation and quotient maps follow from the structure-sheaf construction. [DihedralIntervals:616](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L616), [DihedralIntervals:622](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L622), [DihedralIntervals:626](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L626), [SheafMorphisms:252](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L252), [SheafMorphisms:288](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L288), [DihedralIntervals:176](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L176), [DihedralIntervals:251](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L251), [DihedralIntervals:372](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L372).

**Role in the proof:** The Blueprint follows the parity, normal-form prescription, spline product and flow-down correction arguments. Injectivity of the reflection-preserving group map provides distinct factor data and pairwise relatively prime incident labels. These model properties feed the later local-ring decomposition.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Turn an opposite-parity external vertex into an outgoing edge

Take \(y\in Y(x,c)\). It satisfies \(y\le_Hc\) and \(y\not\le_Hx\).

If \(\ell_H(y)<\ell_H(x)\), the [[node:kl.coxeter.dihedral_bruhat_order|dihedral Bruhat comparison theorem]] would give \(y\le_Hx\). Thus \(\ell_H(y)\ge\ell_H(x)\). Their parities differ, so the inequality is strict.

The [[node:kl.dihedral.odd_reflection_edges|odd-gap edge theorem]] now gives \(x\to_Hy\). Since \(y\le_Hc\le_Hb\), this is an edge of the ambient interval whose target is supported in \(\mathcal O_c\).

### Step 2. Construct the inverse correspondence

Conversely, take a supported outgoing edge \(e:x\to_Hy\) with \(y\le_Hc\). Its strict length increase implies \(y\not\le_Hx\). Its odd length gap gives opposite parity. Therefore \(y\in Y(x,c)\).

The maps \(y\mapsto(x,y)\) and \(e\mapsto t(e)\) are inverse: the outgoing source is fixed at \(x\), and interval edges are pairs with their reflection-step property. This is outgoingEquiv.

### Step 3. Identify the exact label products

For the edge attached to \(y\), both the interpolation root and induced edge root are the canonical positive ambient root of
\(\phi(yx^{-1})\). Their polynomial labels are equal.

Reindexing by the bijection of Step 2 gives
\[
\prod_{y\in Y(x,c)}\lambda(a_y)
=\prod_{e\in\operatorname{Out}_c(x)}\alpha_e
=P_c(x).
\]
This is interpolation_product.

### Step 4. Restrict the interpolating function to the model

Choose \(F:H\to A\) from the [[node:kl.local.dihedral_interpolation|dihedral interpolation theorem]]. At a supported vertex \(v\le_Hc\), set \(\theta_x(v)=F(v)\); at an unsupported vertex use its zero stalk.

For a supported edge \(e:v\to_Hw\), its reflection label satisfies \(w=\tau_ev\). The interpolation congruence for \(\tau_e\) says
\[
\alpha_e\mid F(v)-F(w).
\]
This is exactly structure-sheaf compatibility on that edge. Unsupported edge modules are zero, so \(\theta_x\) is a global section.

### Step 5. Check the normalization and support

Since \(x\le_Hc\), the value at \(x\) is \(F(x)\). The interpolation theorem and Step 3 give
\[
\theta_x(x)=F(x)=P_c(x).
\]

If \(v\not\le_Hx\) and \(v\le_Hc\), the interpolating function vanishes at \(v\). If \(v\not\le_Hc\), its model stalk is zero. Thus \(\theta_x\) vanishes at every vertex outside the lower ideal of \(x\).

These are all clauses of HasFlowDown.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.external_step`: [DihedralIntervals.lean:470](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L470).

`OAI.KLInvariance.Dihedral.step_external`: [DihedralIntervals.lean:480](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L480).

`OAI.KLInvariance.Dihedral.externalEdge`: [DihedralIntervals.lean:491](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L491).

`OAI.KLInvariance.Dihedral.externalEdge_mem`: [DihedralIntervals.lean:496](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L496).

`OAI.KLInvariance.Dihedral.outgoingEquiv`: [DihedralIntervals.lean:503](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L503).

`OAI.KLInvariance.Dihedral.interpolation_product`: [DihedralIntervals.lean:521](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L521).

`OAI.KLInvariance.Dihedral.hasFlowDown`: [DihedralIntervals.lean:531](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L531).
