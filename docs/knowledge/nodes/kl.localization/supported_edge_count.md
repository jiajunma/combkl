---
id: kl.local.supported_edge_count
title: Counting supported later edges by their target vertices
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.coset_later_selections
- kl.local.selected_model_product
- kl.dihedral.plane_coset_graph
- kl.paths.graph_invariance
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.outgoing_step
  - OAI.KLInvariance.TitsSpace.PlaneBasis.outgoing_target_injective
  - OAI.KLInvariance.TitsSpace.PlaneBasis.supported_card_count
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1004
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.outgoing_step
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1024
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.outgoing_target_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1031
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.supported_card_count
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the complete sum_bij_ne_zero proof of supported_card_count. Expanded
    all interval-domain checks, target injectivity, reconstruction from a nonzero
    target indicator through both edge equivalences, and the zero terms. Preserved
    the general threshold and a<=x hypothesis without inserting x<=c.
tags:
- Kazhdan-Lusztig
- embedded-images
---

# Counting supported later edges by their target vertices

Let \(W,W'\) be finite-generator real Coxeter systems and \(\varphi:[u,b]_W\simeq[u',b']_{W'}\) an interval order isomorphism. In \(W\), choose a root plane \(P\) with a plane basis, its induced subgroup \(D\), and a representative \(a_0\) satisfying \(\ell(a_0)\le\ell(da_0)\) for every \(d\in D\). Let \(K=\{d\in D:da_0\le_Wb\}\) have its intrinsic order and reflection graph. Use the target geometric slope and its after-indicator \(\varepsilon\), which tests for an upward reflection edge with root slope strictly greater than the chosen threshold.

Choose \(a,x,c\in K\) with \(a\le_Dx\) and \(u\le_Waa_0\), and let \(\alpha'\) be any positive root of the target system. Then \(u\le_Wxa_0\), so the selected outgoing set \(\mathcal F_{\alpha'}(x)\) is defined.

Let
\[
S=\{f\in\mathcal F_{\alpha'}(x):t(f)\le_Dc\}
\]
be its supported selection for the model centered at \(c\). Put \(\widehat x=xa_0\), and for \(z\in[a,c]_D\) put \(\widehat z=za_0\). Then
\[
|S|
=\sum_{z\in[a,c]_D}
 \varepsilon(\varphi(\widehat x),\alpha',\varphi(\widehat z)).
\]
Each summand is zero or one, and the relative interval is finite.

## Application to the two endpoint counts

For the current edge \(e:x\to y\) and a model center \(c\) with \(y\le_Dc\), apply the result at \(x\) and at \(y\), using the lower interval endpoint \(a=x\) and the common threshold \(\alpha'_e\). The resulting two sums are the ones compared by the [[node:kl.paths.later_count|transported dihedral count theorem]].

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Endpoint selections and their finite indicator sums.**

**OpenAI notes:** The notes select outgoing edges strictly later than the current edge in the transported target label order, then count the supported selections in the full relative interval. Incident image labels have no ties. [dih:count](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L464), [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** A target after-indicator tests an upward reflection edge and a strict geometric-slope comparison. Both endpoint selections use the mapped current root as one threshold. supported_card_count proves an explicit target-vertex bijection between supported selected edges and the nonzero terms of the finite indicator sum. [DihedralIntervals:2107](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2107), [PlaneLocalization:1018](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1018), [PlaneLocalization:1152](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1152), [PlaneLocalization:1159](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1159), [PlaneLocalization:1163](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1163), [PlaneLocalization:1031](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1031).

**Role in the proof:** This reindexing identifies the sums to which the transported dihedral count theorem applies. It supplies the edge-set interpretation of that theorem without replacing its numerical count argument.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Check the ambient interval coordinates

The comparison \(a\le_Dx\) gives
\(aa_0\le_Wxa_0\), so the lower bound on \(aa_0\) implies the lower bound on \(xa_0\).

For \(z\in[a,c]_D\), relative comparison gives
\[
aa_0\le_Wza_0\le_Wca_0.
\]
The lower bound on \(aa_0\) and the membership \(c\in K\) put \(za_0\) in \([u,b]_W\). Thus every term of the displayed sum is defined.

### Step 2. Map a selected supported edge to its target

Take \(f:x\to_Dz\) in \(S\). The relative step and \(a\le_Dx\) give \(a\le_Dz\). The support condition gives \(z\le_Dc\). Hence \(z\in[a,c]_D\).

Membership in \(\mathcal F_{\alpha'}(x)\) says that the summand indexed by this target is exactly \(1\).

### Step 3. Prove injectivity of the target map

Two outgoing edges at \(x\) with the same target have the same endpoint pair. Coset graph edges are such pairs with a reflection-step property, so the edges are equal.

Thus distinct members of \(S\) give distinct target indices of value \(1\).

### Step 4. Recover an edge from a nonzero summand

Suppose the summand at \(z\in[a,c]_D\) is nonzero. By the definition of the after-indicator, it equals \(1\), and there is a target reflection edge
\[
\varphi(\widehat x)\to\varphi(\widehat z).
\]

Reflection-edge transport under the interval isomorphism gives the ambient edge \(\widehat x\to\widehat z\). The least-coset reflection-step equivalence then gives the intrinsic edge \(x\to_Dz\).

The vertex \(z\) lies in \(K\), because \(z\le_Dc\) implies
\(za_0\le_Wca_0\le_Wb\). Its edge therefore belongs to the coset graph. The after-indicator value places it in \(\mathcal F_{\alpha'}(x)\), and \(z\le_Dc\) makes it supported.

This recovers an element of \(S\) with exactly the prescribed target.

### Step 5. Convert the bijection into the sum

Steps 2–4 give a bijection from \(S\) to the target vertices whose summand is \(1\). Every other summand is zero. The finite sum therefore counts exactly those targets and equals \(|S|\).

The proof also applies when the relative interval or the supported selected set is empty. This is the source's supported_card_count reindexing.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.outgoing_step`: [PlaneLocalization.lean:1004](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1004).

`OAI.KLInvariance.TitsSpace.PlaneBasis.outgoing_target_injective`: [PlaneLocalization.lean:1024](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1024).

`OAI.KLInvariance.TitsSpace.PlaneBasis.supported_card_count`: [PlaneLocalization.lean:1031](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1031).
