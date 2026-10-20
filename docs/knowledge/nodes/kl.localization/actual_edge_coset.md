---
id: kl.local.actual_edge_coset
title: An actual ambient edge has coordinates in a least plane coset
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.coset_graph
- kl.dihedral.minimal_plane_cosets
- kl.dihedral.plane_coset_graph
- kl.realization.plane_reflection_membership
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.exists_coset_edge
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1715
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.exists_coset_edge
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the coefficient actions, actual modules, interval bounds, selected sets,
    finite-basis assumptions and support cases explicit?
  verdict: Checked arbitrary actual edge/root membership, least source coordinates,
    target=t*g, both upper bounds and identity lower bounds, intrinsic edge recovery
    and exact equality of endpoint-pair edges.
tags:
- Kazhdan-Lusztig
- embedded-images
- local-comparison
---

# An actual ambient edge has coordinates in a least plane coset

Let \(W\) be a finite-generator real Coxeter system, \(P\) a root plane with a plane basis \(B\), and \(D\) its induced dihedral subgroup. Let \(e:x\to_Wy\) be an edge of the ambient interval graph on \([1,b]_W\), and suppose its positive root \(a_e\) lies in \(P\).

There are a least coset representative \(a_0\), vertices \(g,h\) of
\[
K=\{d\in D:da_0\le_Wb\},
\]
and an intrinsic edge \(d:g\to_Dh\) of \(K\) such that
\[
ga_0=x,\qquad ha_0=y,\qquad j_E(d)=e.
\]
Here \(j_E\) is the coset graph map, and least means
\[
\ell_W(a_0)\le\ell_W(za_0)\qquad(z\in D).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The full ambient edge set and its relative-coset restriction.**

**OpenAI notes:** The local comparison uses the plane-subgroup coset through the current ambient edge and restricts the transported later-edge conditions to that coset. [dih:plane](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L20), [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** ambientLater is an edge set on the full graph [1,b], with an explicit source-above-u witness. scheduledOutgoing_eq is its inverse-image identity on the coset graph. Least coset coordinates for the source and multiplication by the actual edge reflection construct the relative edge, and both mapped-root definitions evaluate the same target edge. [PlaneLocalization:1215](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1215), [PlaneLocalization:1237](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1237), [PlaneLocalization:1700](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1700), [PlaneLocalization:1715](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1715), [PlaneLocalization:1744](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1744).

**Role in the proof:** The Blueprint defines the ambient selection before transferring the two endpoint kernels, and constructs the relative coordinates with both endpoint bounds and the exact equality of edges.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Choose least coset coordinates for the source

The [[node:kl.dihedral.minimal_plane_cosets|least-coset representative theorem]], applied to the source \(x\), gives \(a_0\) and \(g\in D\) such that
\[
x=ga_0,\qquad
\ell_W(a_0)\le\ell_W(za_0)\quad(z\in D).
\]
The ambient bound \(x\le_Wb\) makes \(g\) a vertex of \(K\).

### Step 2. Use the edge reflection to construct the target coordinate

The left reflection of \(e\) is \(t=yx^{-1}\), represented by the positive root \(a_e\). Since \(a_e\in P\), the [[node:kl.realization.plane_reflection_membership|plane-reflection membership theorem]] gives \(t\in D\).

Set \(h=tg\in D\). Then
\[
ha_0=tga_0=tx=y.
\]
The bound \(y\le_Wb\) makes \(h\) a vertex of \(K\). In the source's full CosetVertex data, the additional inequalities \(1\le_Dg\) and \(1\le_Dh\) hold because the identity is below every element.

### Step 3. Recover the intrinsic edge

The ambient edge \(x\to_Wy\) can now be written \(ga_0\to_Wha_0\). The representative \(a_0\) is least, so the [[node:kl.dihedral.plane_coset_graph|coset graph theorem]] gives
\[
g\to_Dh.
\]
Together with the two vertex memberships, this defines the relative coset edge \(d\).

### Step 4. Identify the actual ambient edge

The graph map sends \(d\) to the ambient edge with source \(ga_0=x\) and target \(ha_0=y\). Ambient Bruhat graph edges are endpoint pairs satisfying the reflection-step condition. Both endpoints therefore agree with those of \(e\), giving \(j_E(d)=e\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.exists_coset_edge`: [PlaneLocalization.lean:1715](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1715).
