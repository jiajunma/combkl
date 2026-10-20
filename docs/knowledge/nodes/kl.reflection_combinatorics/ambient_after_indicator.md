---
id: kl.paths.ambient_after_indicator
title: The ambient after-indicator for a root threshold
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.foundations.bruhat_step
- kl.detail.root_reflection_correspondence
- kl.order.root_slopes
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.TitsSpace.ambientAfterIndicator
  - OAI.KLInvariance.TitsSpace.ambientAfterIndicator_of_le
  - OAI.KLInvariance.TitsSpace.ambientAfterIndicator_edge_self
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:2107
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.ambientAfterIndicator
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:2113
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.ambientAfterIndicator_of_le
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:2120
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.ambientAfterIndicator_edge_self
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient/coset domains, intrinsic ranks, injectivity, full-range
    and exact-intermediate hypotheses explicit?
  verdict: Separated the general ambient threshold predicate from the later coset
    selections, retained the arbitrary positive threshold and strict comparison, and
    explained both zero lemmas directly from their source proofs.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# The ambient after-indicator for a root threshold

Let \(W\) be a finite-generator real Coxeter system with geometric slope \(\sigma\) on its positive roots. For \(x,z\in W\) and a positive root \(\alpha\), define the ambient after-indicator
\[
\varepsilon_W(x,\alpha,z)=
\begin{cases}
1,&x\to_Wz\text{ and }\sigma(\alpha)<\sigma(\alpha_{xz}),\\
0,&\text{otherwise}.
\end{cases}
\]
Here \(\alpha_{xz}\) is the unique positive root representing the left reflection \(zx^{-1}\) of the edge. The definition first tests whether the edge exists, then compares its root to the threshold \(\alpha\). It is Lean's `TitsSpace.ambientAfterIndicator`.

A finite sum of these natural numbers counts outgoing edges with root slope strictly later than \(\alpha\). In a transported schedule, \(x,z,\alpha\) are evaluated in the target Coxeter system.

## The two zero cases used at rank one

If \(z\le_Wx\), then
\[
\varepsilon_W(x,\alpha,z)=0.
\]
Indeed, an upward edge \(x\to_Wz\) would imply \(\ell_W(x)<\ell_W(z)\), whereas the given comparison gives \(\ell_W(z)\le\ell_W(x)\). Thus the edge test fails.

For an actual edge \(e:x\to_Wy\) with root \(\alpha_e\),
\[
\varepsilon_W(x,\alpha_e,y)=0.
\]
The edge test succeeds, but the remaining strict inequality is
\(\sigma(\alpha_e)<\sigma(\alpha_e)\), which is false.

These facts give all terms for a two-vertex interval with current edge \(x\to y\): at source \(x\), the target \(x\) fails the edge test and the target \(y\) equals the threshold; at source \(y\), both targets are at or below the source. Hence both later-edge counts are zero.

## Restriction to a plane-subgroup coset

The native later-edge count uses an intrinsic dihedral edge predicate and its actual ambient root. The [[node:kl.dihedral.indicator_transport|coset-count transport theorem]] identifies the ambient and intrinsic indicators under multiplication by a least coset representative.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Root equality and a bijection of the full interval index sets.**

**OpenAI notes:** The later-edge proof identifies the transported schedule with the actual target root order after identifying the target coset with its dihedral group. [dih:count](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L464).

**Lean (primary):** edgeRoot_coset checks the unchanged left reflection under multiplication by the representative. The indicator equality treats edges and nonedges. interval_map_count constructs a bijection from injectivity and full range alone, reindexes the finite sum, and then uses the zero terms outside the relative interval to obtain the native lower-ideal count. [DihedralIntervals:2107](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2107), [DihedralIntervals:2048](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2048), [DihedralIntervals:2128](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2128), [DihedralIntervals:2064](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2064).

**Role in the proof:** The Blueprint explains the actual threshold predicate, each root and indicator identity, and the finite reindexing map with their separate hypotheses.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.ambientAfterIndicator`: [DihedralIntervals.lean:2107](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2107).

`OAI.KLInvariance.TitsSpace.ambientAfterIndicator_of_le`: [DihedralIntervals.lean:2113](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2113).

`OAI.KLInvariance.TitsSpace.ambientAfterIndicator_edge_self`: [DihedralIntervals.lean:2120](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2120).
