---
id: kl.dihedral.coset_interval_embedding
title: The coset interval embedding into an ambient interval
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.notes.relative_dihedral_intervals
- kl.dihedral.plane_coset_graph
- kl.foundations.interval
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetIntervalMap
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:676
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetIntervalMap
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient/coset domains, intrinsic ranks, injectivity, full-range
    and exact-intermediate hypotheses explicit?
  verdict: Specified every ambient endpoint and least-representative condition, multiplication
    direction, membership proof, cancellation, graph equivalence and the source definition’s
    possible empty domain.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# The coset interval embedding into an ambient interval

Let \(W\) be a finite-generator real Coxeter system, \(B\) a plane basis, and \(D\) its induced dihedral subgroup. Choose \(a_0\in W\) satisfying
\[
\ell_W(a_0)\le\ell_W(da_0)\qquad(d\in D).
\]
Fix ambient endpoints \(u,b\in W\) and intrinsic endpoints \(g,k\in D\), with
\[
u\le_Wga_0,\qquad ka_0\le_Wb.
\]
The coset interval embedding is
\[
\iota_{a_0}:[g,k]_D\hookrightarrow[u,b]_W,\qquad
\iota_{a_0}(z)=za_0.
\]
In Lean this map is `PlaneBasis.cosetIntervalMap`. Its construction is defined even if the source interval is empty; the transport theorem separately assumes \(g\le_Dk\).

## The endpoint bounds make the map well-defined

For \(z\in[g,k]_D\), the [[node:kl.dihedral.plane_coset_graph|least-coset graph comparison]] transfers \(g\le_Dz\le_Dk\) to
\[
ga_0\le_Wza_0\le_Wka_0.
\]
Combining this with the displayed ambient bounds gives \(u\le_Wza_0\le_Wb\). Thus the product belongs to the stated ambient interval.

## Injectivity and the graph comparison

If \(za_0=wa_0\), right cancellation gives \(z=w\). This proves injectivity.

The [[node:kl.dihedral.plane_coset_graph|coset graph theorem]] also identifies upward reflection edges:
\[
z\to_Dw\quad\Longleftrightarrow\quad za_0\to_Wwa_0.
\]
A relative Bruhat comparison is a chain of these edges, so the embedding preserves relative order. The source rank is measured by \(\ell_D\), and the codomain's ambient rank by \(\ell_W\).

The example of a relative simple reflection with ambient length three in the [[node:kl.notes.relative_dihedral_intervals|relative-interval definition]] shows how these two ranks can differ. Full interval transport constructs a target relative rank correspondence after composing \(\iota_{a_0}\) with an ambient interval order isomorphism.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit coordinates, affine lengths and full target range.**

**OpenAI notes:** The proposition describes the image directly as a full relative interval in a target plane coset. Its proof recovers covers from rank-two intervals and exhausts each internal target rank with two image vertices. [dih:transport](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L276).

**Lean (primary):** The construction chooses a least target representative and writes F(z) as the ambient image multiplied on the right by its inverse. Rank-two preservation gives consecutive-rank preservation, then an affine length identity by induction. Injectivity and the two-element internal ranks give the exact full range. The theorem returns all coordinate, order, edge and length properties explicitly. [DyerPaths:676](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L676), [DyerPaths:504](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L504), [DyerPaths:536](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L536), [DyerPaths:567](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L567), [DyerPaths:736](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L736).

**Role in the proof:** The Blueprint uses the intrinsic coordinate map F and retains every ambient endpoint bound. The source and target bottom lengths may differ by the constant prescribed by the affine identity.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetIntervalMap`: [DyerPaths.lean:676](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L676).
