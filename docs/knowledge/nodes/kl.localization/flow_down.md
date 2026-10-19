---
id: kl.local.flow_down
title: Flow-down sections and outgoing label products
kind: definition
status: formalized
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.detail.structure_sheaves
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.modelOutgoing
  - OAI.KLInvariance.MomentGraph.Sheaf.mem_modelOutgoing
  - OAI.KLInvariance.MomentGraph.Sheaf.modelProduct
  - OAI.KLInvariance.MomentGraph.Sheaf.HasFlowDown
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:341
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.modelOutgoing
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:345
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.mem_modelOutgoing
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:350
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.modelProduct
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:352
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.HasFlowDown
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read modelOutgoing, its exact membership condition, modelProduct and every
    clause of HasFlowDown. Distinguished the supported outgoing set from all outgoing
    edges and recorded the global lower-support and prescribed-product conditions.
tags:
- Kazhdan-Lusztig
- interpolation
---

# Flow-down sections and outgoing label products

Let \(G\) be an ordered graph with finitely many edges, labelled by scalars \(\alpha_e\) in a commutative ring \(R\). Fix a model center \(c\).

The **supported outgoing set** at \(x\) is
\[
\operatorname{Out}_c(x)
=\{e:s(e)=x,\ t(e)\le c\}.
\]
These are exactly the outgoing edges whose structure-sheaf edge modules are supported below \(c\). The source calls this finite set modelOutgoing.

Its **supported outgoing label product** is
\[
P_c(x)=\prod_{e\in\operatorname{Out}_c(x)}\alpha_e.
\]
This is modelProduct. An empty supported outgoing set gives \(P_c(x)=1\).

## A normalized section with lower support

A **flow-down section at \(x\le c\)** is a global section \(\theta_x\) of \(\mathcal O_c\) satisfying
\[
\theta_x(x)=P_c(x),\qquad
\theta_x(y)=0\quad\text{if }y\not\le x.
\]
The value at \(x\) is read using the supported-stalk identification with \(R\). HasFlowDown is the proposition that such a section exists for every \(x\le c\).

The support condition says that \(\theta_x\) is supported on the lower ideal of \(x\). It therefore changes a prescribed value at \(x\) without changing values at vertices outside that lower ideal. Multiplying it by \(r\in R\) changes the value at \(x\) by \(rP_c(x)\).

## The one-edge model

For a single edge \(x\to c\) labelled by \(\alpha\),
\[
P_c(x)=\alpha,\qquad P_c(c)=1.
\]
The section \(\theta_x=(\alpha,0)\) is a flow-down section at \(x\), since its two values agree modulo \(\alpha\). The constant section \(\theta_c=(1,1)\) is a flow-down section at \(c\).

The [[node:kl.local.flow_down_flabbiness|flow-down flabbiness theorem]] uses these normalized values together with pairwise relative primality of the supported outgoing labels.

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

`OAI.KLInvariance.MomentGraph.Sheaf.modelOutgoing`: [DihedralIntervals.lean:341](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L341).

`OAI.KLInvariance.MomentGraph.Sheaf.mem_modelOutgoing`: [DihedralIntervals.lean:345](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L345).

`OAI.KLInvariance.MomentGraph.Sheaf.modelProduct`: [DihedralIntervals.lean:350](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L350).

`OAI.KLInvariance.MomentGraph.Sheaf.HasFlowDown`: [DihedralIntervals.lean:352](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L352).
