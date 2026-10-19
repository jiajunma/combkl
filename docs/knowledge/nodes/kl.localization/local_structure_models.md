---
id: kl.local.local_structure_models
title: Local model data from structure sheaves
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.detail.local_models
- kl.local.structure_sheaf_properties
- kl.local.structure_model_transport
- kl.detail.dihedral_model_properties
- kl.local.plane_prime_membership
- kl.dihedral.induced_system
- kl.realization.plane_reflection_membership
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.structureLocalModels
  - OAI.KLInvariance.TitsSpace.PlaneBasis.localModels
  - OAI.KLInvariance.TitsSpace.PlaneBasis.modelLabel_mem_maximal
  - OAI.KLInvariance.TitsSpace.PlaneBasis.localizedModels
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:289
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.structureLocalModels
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:317
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.localModels
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:408
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.modelLabel_mem_maximal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:415
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.localizedModels
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read structureLocalModels field by field, the general flat local-algebra
    hypotheses of localModels, and modelLabel_mem_maximal/localizedModels. Explained
    the outgoing-below path and kept the general local-ring label condition separate
    from its plane-ring verification.
tags:
- Kazhdan-Lusztig
- local-model-transport
---

# Local model data from structure sheaves

Let \(R\) be a commutative local ring with maximal ideal \(\mathfrak m\), and let \(G\) be an ordered graph labelled by \(\alpha_e\in R\). Suppose:

- every label belongs to \(\mathfrak m\);
- whenever \(x<c\), there is an edge \(e\) with source \(x\) and target at most \(c\);
- every structure sheaf \(\mathcal O_c(G,\alpha)\) is flabby.

Then the family \(c\mapsto\mathcal O_c\), with its canonical top-stalk coordinates, is a family of local boundary models. This is structureLocalModels.

In the root-plane application, fix a finite-generator ambient Coxeter system, a root subspace \(P\) with plane basis \(B\), its induced dihedral group \(D\), the ambient polynomial algebra \(A\), and a principal interval \([1,d]_D\). Let \(A\to R\) be a flat scalar extension into a commutative local ring. If every induced model label maps into its maximal ideal, the scalar-extended structure sheaves on this interval give local model data. This is localModels. For \(R=R_P=A_{\mathfrak p_P}\), the label condition holds and gives localizedModels.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Finite-interval construction of the relative models.**

**OpenAI notes:** After the relative-flabbiness lemma, the notes restrict the localized model from the full coset to its finite relative lower ideal. They extend a section by zero outside the model support inside an upward closure, then use model flabbiness. Flat localization preserves the finite-support section conditions. [loc:models](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L125), [loc:relative-flabbiness](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L226).

**Lean (primary):** The finite relative ideal is embedded in a principal dihedral interval using a common upper bound. Explicit scalar-extension and pullback isomorphisms identify the structure models. The outgoing-lift theorem is applied to edges whose targets lie below the chosen model center; canonical positive-root equality identifies the actual labels. [MinimalExtensions:1295](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1295), [DihedralIntervals:667](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L667), [PlaneLocalization:637](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L637), [PlaneLocalization:724](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L724), [PlaneLocalization:761](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L761).

**Role in the proof:** The Blueprint follows the finite-interval construction and verifies the support, outgoing lifts, scalar maps and label equality before assembling the local-model fields.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Supply the stalk and quotient conditions

The [[node:kl.local.structure_sheaf_properties|basic structure-sheaf properties theorem]] gives finite free stalks, generation, and the upper-quotient rule. The support condition holds because \(\mathcal O_c^x=0\) when \(x\not\le c\).

At the center \(c\), evaluation at its supported coordinate gives
\(\mathcal O_c^c\simeq R\). Choose this as the top isomorphism.

These constructions supply the free, finite, quotient, generated, support and top fields.

### Step 2. Supply minimality and flabbiness

For \(x\ne c\), an unsupported stalk is zero. At a supported proper vertex \(x<c\), the outgoing-edge hypothesis supplies a supported outgoing edge.

If a vector lies in the full outgoing kernel, its scalar coordinate lies in the principal ideal of that edge label. Since the label belongs to \(\mathfrak m\), the vector lies in \(\mathfrak m\mathcal O_c^x\). This is exactly the minimality field, as proved in the [[node:kl.local.structure_sheaf_properties|basic structure-sheaf properties theorem]].

The assumed flabbiness supplies the final field. All local-model conditions now hold.

### Step 3. Obtain the fields on a scalar-extended dihedral interval

The intrinsic interval \([1,d]_D\) is finite, and its edges form a subset of the finite square of its vertices. Native induced models are flabby by the [[node:kl.detail.dihedral_model_properties|dihedral model theorem]].

The [[node:kl.local.structure_model_transport|structure-model transport theorem]] and flatness of \(R\) over \(A\) give flabbiness after mapping the labels into \(R\). For \(x<c\), a nonempty Bruhat reflection path from \(x\) to \(c\) has a first edge \(x\to y\) with \(y\le c\). This supplies the outgoing-edge condition.

The maximal-ideal label condition is assumed. Steps 1–2 therefore construct localModels over \(R\).

### Step 4. Verify the label condition in the plane ring

An intrinsic edge reflection \(\tau_e\) lies in \(D\). Its canonical ambient positive root \(\beta_e\) represents that reflection.

The [[node:kl.realization.plane_reflection_membership|plane-subgroup membership theorem]] says that a representing root belongs to \(P\) exactly when its reflection belongs to the plane subgroup. Hence \(\beta_e\in P\).

The [[node:kl.local.plane_prime_membership|plane-prime membership theorem]] then gives
\[
\eta_P\bigl(\Lambda(i_0\beta_e)\bigr)\in\mathfrak m_P.
\]
This is precisely the scalar-extended model label. Localization is flat, so all hypotheses of Step 3 hold for \(R_P\). The resulting family is localizedModels.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.structureLocalModels`: [PlaneLocalization.lean:289](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L289).

`OAI.KLInvariance.TitsSpace.PlaneBasis.localModels`: [PlaneLocalization.lean:317](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L317).

`OAI.KLInvariance.TitsSpace.PlaneBasis.modelLabel_mem_maximal`: [PlaneLocalization.lean:408](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L408).

`OAI.KLInvariance.TitsSpace.PlaneBasis.localizedModels`: [PlaneLocalization.lean:415](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L415).
