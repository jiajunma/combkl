---
id: kl.local.coset_structure_models
title: Structure models on the finite relative coset graph
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.coset_graph
- kl.local.local_structure_models
- kl.local.structure_model_transport
- kl.dihedral.finite_common_upper
- kl.sheaves.pullback_live_flabbiness
- kl.local.plane_prime_membership
- kl.dihedral.plane_coset_graph
- kl.detail.local_models
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetInto
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetIntoEdge
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetIntoGraph
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetInto_injective
  - OAI.KLInvariance.TitsSpace.PlaneBasis.coset_label_eq
  - OAI.KLInvariance.TitsSpace.PlaneBasis.coset_modelLabel_eq
  - OAI.KLInvariance.TitsSpace.PlaneBasis.coset_model_flabby
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetModels
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:681
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetInto
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:684
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetIntoEdge
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:688
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetIntoGraph
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:696
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetInto_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:703
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.coset_label_eq
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:708
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.coset_modelLabel_eq
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:724
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.coset_model_flabby
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:761
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetModels
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the common-upper embedding, injectivity, coset_label_eq and canonical-root
    label equality, and every hypothesis in coset_model_flabby and cosetModels. Kept
    intrinsic order distinct from ambient order, lifted only model-supported edges,
    and verified maximal-ideal labels and outgoing-below conditions.
tags:
- Kazhdan-Lusztig
- local-model-transport
---

# Structure models on the finite relative coset graph

Fix a finite-generator ambient Coxeter system \(W\), a root subspace \(P\) with a plane basis, and the induced dihedral subgroup \(D\). Let \(a_0\in W\) satisfy
\[
\ell(a_0)\le\ell(da_0)\qquad(d\in D),
\]
and let \(b\in W\). The finite relative vertex set is
\[
K=\{d\in D:da_0\le_W b\},
\]
with its intrinsic \(D\)-Bruhat order and reflection edges. It is a relative lower ideal. Use the plane ring \(R_P=A_{\mathfrak p_P}\) and the localized ambient root label \(\gamma_e\) on each edge.

For every \(c\in K\), the structure sheaf
\(\mathcal O_c(K,\gamma)\) is flabby. The family of these sheaves, with the canonical top coordinates, gives the source's cosetModels local boundary models.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Finite-interval construction of the relative models.**

**OpenAI notes:** After the relative-flabbiness lemma, the notes restrict the localized model from the full coset to its finite relative lower ideal. They extend a section by zero outside the model support inside an upward closure, then use model flabbiness. Flat localization preserves the finite-support section conditions. [loc:models](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L125), [loc:relative-flabbiness](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L226).

**Lean (primary):** The finite relative ideal is embedded in a principal dihedral interval using a common upper bound. Explicit scalar-extension and pullback isomorphisms identify the structure models. The outgoing-lift theorem is applied to edges whose targets lie below the chosen model center; canonical positive-root equality identifies the actual labels. [MinimalExtensions:1295](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1295), [DihedralIntervals:667](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L667), [PlaneLocalization:637](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L637), [PlaneLocalization:724](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L724), [PlaneLocalization:761](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L761).

**Role in the proof:** The Blueprint follows the finite-interval construction and verifies the support, outgoing lifts, scalar maps and label equality before assembling the local-model fields.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Place the finite graph inside an intrinsic principal interval

The [[node:kl.dihedral.finite_common_upper|finite-common-upper-bound theorem]] gives \(d_0\in D\) with \(x\le_Dd_0\) for every \(x\in K\). Hence the map
\[
f_V:K\longrightarrow[1,d_0]_D,\qquad x\longmapsto x
\]
is defined and injective. It preserves and reflects order because both sides use intrinsic Bruhat order.

An edge \(x\to y\) maps to the same endpoint pair in \([1,d_0]_D\), with the same reflection-step proof. These maps give cosetIntoGraph. Fix a model center \(c\in K\).

### Step 2. Identify the native and ambient root labels

For an edge \(e:x\to y\) of \(K\), its ambient image has endpoints \(xa_0,ya_0\). Its ambient left reflection is
\[
(ya_0)(xa_0)^{-1}
=ya_0a_0^{-1}x^{-1}
=yx^{-1}.
\]
This is also the ambient image of its intrinsic reflection label.

Both root constructions choose the canonical positive ambient root of this same reflection. Hence their roots are equal, and applying the linear polynomial map gives
\[
\alpha^{\mathrm{model}}_{f_E(e)}
=\alpha^{\mathrm{ambient}}_e.
\]
After mapping to \(R_P\), the pulled-back interval label is exactly \(\gamma_e\). This is coset_modelLabel_eq followed by scalar extension.

### Step 3. Choose the flabby interval model

On \([1,d_0]_D\), let
\[
C=\mathcal O_{f_V(c)}
\]
with the induced labels mapped into \(R_P\). The [[node:kl.local.local_structure_models|local structure-model theorem]] gives flabbiness of \(C\).

Its supported edge set is
\[
L=\{e:t(e)\le_D f_V(c)\}.
\]
For an edge outside \(L\), the edge module of \(C\) is zero by the structure-sheaf definition.

### Step 4. Lift every supported outgoing edge

Take an interval edge \(e\in L\) whose source is \(f_V(x)\) for \(x\in K\). Write \(y=t(e)\). Then \(y\le_Dc\).

The relative lower-ideal property of \(K\) puts \(y\) in \(K\). More explicitly, intrinsic comparison gives
\(ya_0\le_Wca_0\le_W b\).
The same reflection step therefore defines an edge \(x\to y\) in \(K\), and its image under \(f_E\) is \(e\).

This proves the outgoing-lift hypothesis for precisely the supported edge set \(L\).

### Step 5. Pull back flabbiness and identify the structure sheaf

The [[node:kl.sheaves.pullback_live_flabbiness|surviving-edge pullback theorem]] applies: the interval graph is finite, \(f_V\) is injective, \(C\) is flabby, the edges outside \(L\) have zero modules, and Step 4 gives all required outgoing lifts. Thus \(f^*C\) is flabby.

The [[node:kl.local.structure_model_transport|structure-model transport theorem]] gives
\[
f^*C\simeq\mathcal O_c(K,\gamma),
\]
using the order equivalence of Step 1 and exact label equality of Step 2. Transporting sections through this isomorphism proves the desired flabbiness.

### Step 6. Verify the maximal-ideal labels

The intrinsic edge reflection \(yx^{-1}\) lies in \(D\). Its canonical ambient root therefore belongs to \(P\), by the plane-subgroup root criterion. The [[node:kl.local.plane_prime_membership|plane-prime membership theorem]] puts its localized polynomial label \(\gamma_e\) in the maximal ideal of \(R_P\).

This verifies the coefficient hypothesis for every edge of the relative graph.

### Step 7. Assemble every local-model field

If \(x<c\) in \(K\), choose the first step of a Bruhat path from \(x\) to \(c\). Its target remains below \(c\), hence in \(K\). This is the required outgoing edge below \(c\).

Step 6 supplies the maximal-ideal labels; Step 5 supplies flabbiness for every center. The [[node:kl.local.local_structure_models|local structure-model theorem]] now packages the finite free stalks, quotient maps, generation, support, top coordinates and local minimality. This gives cosetModels on the actual finite relative graph.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetInto`: [PlaneLocalization.lean:681](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L681).

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetIntoEdge`: [PlaneLocalization.lean:684](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L684).

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetIntoGraph`: [PlaneLocalization.lean:688](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L688).

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetInto_injective`: [PlaneLocalization.lean:696](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L696).

`OAI.KLInvariance.TitsSpace.PlaneBasis.coset_label_eq`: [PlaneLocalization.lean:703](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L703).

`OAI.KLInvariance.TitsSpace.PlaneBasis.coset_modelLabel_eq`: [PlaneLocalization.lean:708](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L708).

`OAI.KLInvariance.TitsSpace.PlaneBasis.coset_model_flabby`: [PlaneLocalization.lean:724](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L724).

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetModels`: [PlaneLocalization.lean:761](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L761).
