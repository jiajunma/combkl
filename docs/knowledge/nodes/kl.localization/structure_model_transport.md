---
id: kl.local.structure_model_transport
title: Structure models under scalar extension and graph pullback
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.detail.structure_sheaves
- kl.detail.base_change
- kl.detail.graph_transport
- kl.detail.sheaf_isomorphisms
- kl.algebra.tensor_scalar_quotient
- kl.sheaves.base_change_properties
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChangeScalar
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChangeScalar_tmul
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChangePiScalar
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChangePiQuotient
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChangePi_natural
  - OAI.KLInvariance.MomentGraph.Sheaf.structureBaseChangeIso
  - OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf_flat_flabby
  - OAI.KLInvariance.MomentGraph.Sheaf.propPiEquiv
  - OAI.KLInvariance.MomentGraph.Sheaf.structurePullbackIso
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1228
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChangeScalar
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1230
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChangeScalar_tmul
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1253
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChangePiScalar
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1259
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChangePiQuotient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1280
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChangePi_natural
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1295
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.structureBaseChangeIso
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1304
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf_flat_flabby
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:621
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.propPiEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:637
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.structurePullbackIso
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the scalar tensor and quotient coordinate maps, baseChangePi_natural,
    structureBaseChangeIso, its separate flat finite-graph flabbiness consequence,
    and structurePullbackIso. Preserved the order-reflection hypothesis and checked
    both endpoint squares on supported and zero coordinates.
tags:
- Kazhdan-Lusztig
- local-model-transport
---

# Structure models under scalar extension and graph pullback

Let \(R\to S\) be a homomorphism of commutative rings, \(G\) an ordered graph, \(\alpha_e\in R\) its labels, and \(c\) a vertex. Write \(\eta:R\to S\) for the scalar map and \(\mathcal O_c(G,\alpha)\) for the structure sheaf below \(c\). There is a sheaf isomorphism
\[
S\otimes_R\mathcal O_c(G,\alpha)
\simeq \mathcal O_c(G,\eta\alpha).
\]
If \(G\) has finitely many vertices and edges, \(S\) is flat over \(R\), and the original model is flabby, then the model on the right is flabby.

There is also a graph-pullback formula. Let \(f:G\to H\) be a graph map satisfying
\[
f_V(x)\le f_V(y)\quad\Longleftrightarrow\quad x\le y,
\]
let \(\beta\) label \(H\), and let \(c\) be a vertex of \(G\). Then
\[
f^*\mathcal O_{f_V(c)}(H,\beta)
\simeq \mathcal O_c(G,\beta\circ f_E).
\]
The two isomorphisms identify the vertex and edge modules and commute with both endpoint restrictions.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Finite-interval construction of the relative models.**

**OpenAI notes:** After the relative-flabbiness lemma, the notes restrict the localized model from the full coset to its finite relative lower ideal. They extend a section by zero outside the model support inside an upward closure, then use model flabbiness. Flat localization preserves the finite-support section conditions. [loc:models](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L125), [loc:relative-flabbiness](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L226).

**Lean (primary):** The finite relative ideal is embedded in a principal dihedral interval using a common upper bound. Explicit scalar-extension and pullback isomorphisms identify the structure models. The outgoing-lift theorem is applied to edges whose targets lie below the chosen model center; canonical positive-root equality identifies the actual labels. [MinimalExtensions:1295](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1295), [DihedralIntervals:667](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L667), [PlaneLocalization:637](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L637), [PlaneLocalization:724](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L724), [PlaneLocalization:761](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L761).

**Role in the proof:** The Blueprint follows the finite-interval construction and verifies the support, outgoing lifts, scalar maps and label equality before assembling the local-model fields.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Identify scalar-extended stalks

If \(x\le c\), the old stalk is \(R\). The scalar tensor isomorphism is
\[
S\otimes_RR\longrightarrow S,\qquad
s\otimes r\longmapsto s\eta(r).
\]
Its inverse sends \(s\) to \(s\otimes1\). The balancing identity gives
\(s\otimes r=s\eta(r)\otimes1\), so the two maps are inverse.

If \(x\not\le c\), both stalks are zero. Lean handles the two cases uniformly using functions from the support index \(\{\star:x\le c\}\): tensoring this zero- or one-coordinate module gives the corresponding module with values in \(S\). The map on a supported coordinate is the formula above.

### Step 2. Identify scalar-extended edge modules

If \(t(e)\le c\), use the [[node:kl.algebra.tensor_scalar_quotient|tensor-quotient theorem]]:
\[
S\otimes_RR/(\alpha_e)\longrightarrow S/(\eta(\alpha_e)),
\qquad s\otimes[r]\longmapsto[s\eta(r)].
\]
Its inverse sends \([s]\) to \(s\otimes[1]\). If the target vertex is outside the support, both edge modules are zero.

These maps give the edge part of the proposed sheaf isomorphism.

### Step 3. Check both restriction squares

On a supported edge, take a pure tensor \(s\otimes r\) in either endpoint stalk. Applying the old quotient restriction and then the edge isomorphism gives \([s\eta(r)]\). Applying the vertex isomorphism and then the new quotient restriction gives the same element.

The lower map uses \(s(e)\le t(e)\le c\) to read the lower support coordinate; the upper map reads its own support coordinate. Thus both squares commute. Tensor elements are sums of pure tensors, and all four maps are linear, so the equalities hold on every element. Zero edge modules make the remaining squares commute as well.

This constructs structureBaseChangeIso for arbitrary commutative scalar extension.

### Step 4. Transfer flabbiness under the stated flatness hypothesis

For a finite graph, the [[node:kl.sheaves.base_change_properties|scalar-extension property theorem]] identifies compatible sections after flat extension and proves that a flabby sheaf remains flabby. Apply it to \(\mathcal O_c(G,\alpha)\).

The isomorphism of Steps 1–3 carries sections and their restrictions to those of \(\mathcal O_c(G,\eta\alpha)\). Transport a prescribed upper-set section through the inverse isomorphism, extend it, and transport the global extension back. This proves the flabbiness assertion.

### Step 5. Identify support under the graph map

For a vertex \(x\) of \(G\), order reflection gives
\[
f_V(x)\le f_V(c)\quad\Longleftrightarrow\quad x\le c.
\]
Thus the pulled-back stalk and the desired stalk are simultaneously \(R\), or simultaneously zero. On the supported coordinate the vertex isomorphism is the identity.

For an edge \(e\), the graph-map identity
\(t_H(f_E(e))=f_V(t_G(e))\) gives the same equivalence for edge support. Both supported edge modules are
\[
R/(\beta_{f_E(e)}),
\]
and their isomorphism is again the identity on this quotient.

### Step 6. Check the pullback restrictions

The graph map identifies each endpoint of \(f_E(e)\) with the image of the corresponding endpoint of \(e\). On supported coordinates, either route around a restriction square sends \(r\) to \([r]\). On unsupported edge coordinates both routes are zero.

The support-index representation expresses these maps as reindexing by equivalent propositions; evaluation gives exactly the same scalar and quotient calculations. This is structurePullbackIso.

Together the formulas allow the native dihedral model to be localized and then restricted to the finite relative coset graph, with its quotient maps retained explicitly.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.baseChangeScalar`: [MinimalExtensions.lean:1228](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1228).

`OAI.KLInvariance.MomentGraph.Sheaf.baseChangeScalar_tmul`: [MinimalExtensions.lean:1230](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1230).

`OAI.KLInvariance.MomentGraph.Sheaf.baseChangePiScalar`: [MinimalExtensions.lean:1253](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1253).

`OAI.KLInvariance.MomentGraph.Sheaf.baseChangePiQuotient`: [MinimalExtensions.lean:1259](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1259).

`OAI.KLInvariance.MomentGraph.Sheaf.baseChangePi_natural`: [MinimalExtensions.lean:1280](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1280).

`OAI.KLInvariance.MomentGraph.Sheaf.structureBaseChangeIso`: [MinimalExtensions.lean:1295](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1295).

`OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf_flat_flabby`: [MinimalExtensions.lean:1304](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1304).

`OAI.KLInvariance.MomentGraph.Sheaf.propPiEquiv`: [PlaneLocalization.lean:621](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L621).

`OAI.KLInvariance.MomentGraph.Sheaf.structurePullbackIso`: [PlaneLocalization.lean:637](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L637).
