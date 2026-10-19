---
id: kl.detail.dihedral_model_properties
title: Flabbiness of the induced dihedral structure models
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.notes.dihedral_models
- kl.local.structure_sheaf_properties
- kl.local.induced_flow_down
- kl.local.induced_label_primes
- kl.local.flow_down_flabbiness
- kl.dihedral.induced_reflections_length
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.Dihedral.model_flabby
  - OAI.KLInvariance.TitsSpace.PlaneBasis.model_flabby
  - OAI.KLInvariance.TitsSpace.PlaneBasis.model_generated
  - OAI.KLInvariance.TitsSpace.PlaneBasis.model_quotient
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:580
    format: lean-location
    note: OAI.KLInvariance.Dihedral.model_flabby
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:616
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.model_flabby
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:622
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.model_generated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:626
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.model_quotient
  - artifact: openai-kl-paper
    locator: Dihedral models; loc:models
    format: section
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: 'Replaced the compressed model proof by the source dependency chain: basic
    structure properties, fixed-source label coprimality, explicit HasFlowDown construction,
    the finite upper-set induction and the PlaneBasis inclusion specialization. Preserved
    the general reflection-preserving map and its separate injectivity requirement.'
tags:
- Kazhdan-Lusztig
- interpolation
---

# Flabbiness of the induced dihedral structure models

Let \(H\) be a two-generator Coxeter system, \(W\) a finite-generator ambient Coxeter system, and \(\phi:H\to W\) a homomorphism carrying reflections to reflections. Use the induced ambient polynomial labels on \([1,b]_H\), and let \(c\le_Hb\).

The structure model \(\mathcal O_c\) has finite free stalks, is globally generated and satisfies the upper-quotient rule. If \(\phi\) is injective, it is also flabby for the intrinsic Bruhat order.

In particular these properties hold for the inclusion of the induced plane subgroup \(D_P\) into \(W\), with the source's modelLabel.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same model properties, different justification.**

**OpenAI notes:** The induced-model lemma justifies applying the character theorem to the restricted reflection-faithful realization and uses the dihedral character calculation to identify the rank-one model. [loc:models](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L125).

**Lean (primary):** The direct construction first proves parity matching in arbitrary lower Bruhat intervals by a simple-reflection involution. In the dihedral application, orbit-spline factors supply the prescribed values and zeros; their product gives flow-down sections. A finite induction on prescribed upper sets proves flabbiness, while generation and quotient maps follow from the structure-sheaf construction. [DihedralIntervals:616](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L616), [DihedralIntervals:622](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L622), [DihedralIntervals:626](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L626), [SheafMorphisms:252](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L252), [SheafMorphisms:288](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L288), [DihedralIntervals:176](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L176), [DihedralIntervals:251](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L251), [DihedralIntervals:372](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L372).

**Role in the proof:** The Blueprint follows the parity, normal-form prescription, spline product and flow-down correction arguments. Injectivity of the reflection-preserving group map provides distinct factor data and pairwise relatively prime incident labels. These model properties feed the later local-ring decomposition.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Apply the basic structure-sheaf construction

Every supported stalk is \(A\), and every unsupported stalk is zero. The [[node:kl.local.structure_sheaf_properties|basic structure-sheaf properties theorem]] gives finite free stalks, global generation and upper quotients.

Generation uses a constant scalar on the lower support. On supported edges the two restrictions are the same quotient map, and on the other edges the target module is zero.

### Step 2. Verify relative primality at each outgoing set

Assume now that \(\phi\) is injective. The [[node:kl.local.induced_label_primes|induced-label primality theorem]] proves that distinct outgoing edges at any fixed source have relatively prime labels.

Every \(\operatorname{Out}_c(x)\) is a subset of those edges, so it has exactly the pairwise relative-primality property required by the [[node:kl.local.flow_down_flabbiness|flow-down criterion]].

### Step 3. Supply the normalized lower-supported sections

The [[node:kl.local.induced_flow_down|induced flow-down theorem]] constructs, for every \(x\le_Hc\), a global section \(\theta_x\) with
\[
\theta_x(x)=P_c(x),\qquad
\theta_x(y)=0\quad(y\not\le_Hx).
\]
Its construction uses the general lower-interval parity matching, normalized orbit-spline factors, and the exact bijection between opposite external vertices and supported outgoing edges.

### Step 4. Apply the flabbiness criterion

The lower Bruhat interval \([1,b]_H\) is finite. Its edge set is a subset of the finite square of the vertex set, hence finite.

The coefficient algebra is a polynomial ring over \(\mathbb R\), so it has the product-divisibility structure used in the [[node:kl.local.flow_down_flabbiness|flow-down flabbiness theorem]]. Steps 2 and 3 supply that theorem's other hypotheses. It follows that every section on an intrinsic upper subset extends globally.

This is the source's general Dihedral.model_flabby theorem.

### Step 5. Specialize to the actual plane subgroup

A plane basis supplies the induced Coxeter system on \(D_P\). Its subgroup inclusion is injective, and the [[node:kl.dihedral.induced_reflections_length|intrinsic-reflection theorem]] says that every reflection of that system is an ambient reflection.

Thus the inclusion satisfies all hypotheses above. The induced labels are exactly modelLabel by definition. The three exported PlaneBasis theorems give flabbiness, generation and the upper-quotient rule for these actual labels.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.model_flabby`: [DihedralIntervals.lean:580](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L580).

`OAI.KLInvariance.TitsSpace.PlaneBasis.model_flabby`: [DihedralIntervals.lean:616](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L616).

`OAI.KLInvariance.TitsSpace.PlaneBasis.model_generated`: [DihedralIntervals.lean:622](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L622).

`OAI.KLInvariance.TitsSpace.PlaneBasis.model_quotient`: [DihedralIntervals.lean:626](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L626).
