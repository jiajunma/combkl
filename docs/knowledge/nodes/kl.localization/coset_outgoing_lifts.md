---
id: kl.local.coset_outgoing_lifts
title: Finiteness and outgoing lifts of the relative coset graph
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.coset_graph
- kl.dihedral.plane_coset_graph
- kl.foundations.interval
- kl.foundations.bruhat_order
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetAmbient_injective
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetFinite
  - OAI.KLInvariance.TitsSpace.PlaneBasis.coset_lower
  - OAI.KLInvariance.TitsSpace.PlaneBasis.coset_outgoing_below
  - OAI.KLInvariance.TitsSpace.PlaneBasis.coset_lift_live
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:451
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetAmbient_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:457
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetFinite
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:483
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.coset_lower
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:488
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.coset_outgoing_below
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:497
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.coset_lift_live
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the injectivity/finite instance, lower-closure argument, explicit
    t*x target in coset_lift_live and the first-step extraction in coset_outgoing_below.
    All ambient/relative order and label directions are explicit.
tags:
- Kazhdan-Lusztig
- localization
---

# Finiteness and outgoing lifts of the relative coset graph

Fix a finite-generator Coxeter system, a root plane with induced subgroup \(D\), and a representative \(a_0\) of least ambient length in \(Da_0\). For \(b\in W\), let
\[
K=\{d\in D:1\le_Dd,\ da_0\le_Wb\},
\qquad j_V(d)=da_0.
\]
Let \(j_E\) be the coset edge map.

Then \(j_V\) is injective, \(K\) is finite and lower closed in \(\le_D\), and every ambient edge \(e\) starting at \(j_V(d)\), whose left reflection label \(\tau_e\) belongs to \(D\), has a lift \(a\) starting at \(d\) with \(j_E(a)=e\).

Furthermore, if \(d<c\) in \(K\), there is a relative edge \(d\to_D y\) in this graph with \(y\le_D c\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Relative extension through an explicit graph map.**

**OpenAI notes:** The coset intersection is a finite relative lower ideal. A relative upper subset is closed under the surviving plane-labelled edges. Descending ambient extension gives relative flabbiness after localization. [loc:relative-flabbiness](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L226).

**Lean (primary):** The same descending extension is factored into extend_closedUnder and a graph-pullback theorem. The coset map supplies vertex injectivity and explicit outgoing lifts; the root/unit criterion makes all outside edge modules zero. A separate theorem records selected-kernel equality under that pullback. [Sheaves:106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L106), [MinimalExtensions:1520](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1520), [PlaneLocalization:497](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L497), [PlaneLocalization:591](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L591), [TerminalKernels:393](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L393).

**Role in the proof:** Relative order determines the upper subsets on the coset, while the ambient graph supplies the extension. The localized stalks and edge maps remain the actual tensor-extended ambient modules, so selected kernels and their edge images retain their embeddings.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Prove injectivity and finiteness

If \(j_V(d)=j_V(c)\), then \(da_0=ca_0\). Right cancellation gives \(d=c\).

The ambient interval \([1,b]_W\) is finite. An injective map into it makes \(K\) finite. The edge set is a subset of \(K\times K\), so it is finite as well.

### Step 2. Prove lower closure in the induced order

Let \(z\le_D d\) with \(d\in K\). The [[node:kl.dihedral.plane_coset_graph|least-coset comparison theorem]] sends this relation to
\[
za_0\le_W da_0.
\]
Combining it with \(da_0\le_W b\) gives \(za_0\le_W b\). Also \(1\le_D z\), so \(z\in K\). This is coset_lower.

### Step 3. Construct the target of a surviving edge lift

Let \(e\) start at \(da_0\) and have reflection label \(\tau_e\in D\). By the ambient edge-label identity, its target is
\[
\tau_e(da_0)=(\tau_e d)a_0.
\]
Set \(c=\tau_e d\in D\).

The ambient target belongs to \([1,b]\), so \(ca_0\le_W b\). Together with \(1\le_D c\), this shows \(c\in K\).

### Step 4. Verify the relative edge and its image

The source and target of \(e\) are \(da_0,ca_0\). The [[node:kl.dihedral.plane_coset_graph|coset reflection-step equivalence]] therefore gives \(d\to_D c\).

Take \(a=(d,c)\) with this step. Its source is \(d\), and its ambient image has the same source and target as \(e\). Ambient Bruhat edges are pairs equipped with their reflection-step property, so this proves \(j_E(a)=e\).

### Step 5. Find an outgoing step below a prescribed upper vertex

Suppose \(d<c\) in the relative order. Bruhat order is generated by reflection steps, so a nonconstant path from \(d\) to \(c\) has a first step
\[
d\to_D y,\qquad y\le_D c.
\]
Step 2 puts \(y\) in \(K\). Thus this first step is an edge of the finite relative coset graph and has target at most \(c\).

This last property supplies the outgoing edge used when constructing lower-supported models on the finite coset graph.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetAmbient_injective`: [PlaneLocalization.lean:451](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L451).

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetFinite`: [PlaneLocalization.lean:457](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L457).

`OAI.KLInvariance.TitsSpace.PlaneBasis.coset_lower`: [PlaneLocalization.lean:483](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L483).

`OAI.KLInvariance.TitsSpace.PlaneBasis.coset_outgoing_below`: [PlaneLocalization.lean:488](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L488).

`OAI.KLInvariance.TitsSpace.PlaneBasis.coset_lift_live`: [PlaneLocalization.lean:497](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L497).
