---
id: kl.detail.split_summands
title: Split sheaf summands and their projectors
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.sheaf_morphism
lean:
  repository: openai-kl
  modules:
  - BalancedPairings
  - EdgeLocalization
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn
  - OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.projector
  - OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.comparison_bijective
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1354
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1314
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.projector
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:785
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.comparison_bijective
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# Split sheaf summands and their projectors

A split inclusion of graded sheaves \(B\) in \(C\) is a pair of degree-zero sheaf morphisms
\[
i:B\longrightarrow C,\qquad p:C\longrightarrow B,\qquad pi=1_B.
\]
The identity is required at every stalk and every edge module. It implies that each \(i_x,i_e\) is injective and each \(p_x,p_e\) is surjective.

The associated projector is \(e=ip\), an endomorphism of \(C\) satisfying
\[
e^2=i(pi)p=ip=e.
\]
Its stalk and edge images form a subsheaf because \(e\) commutes with the restriction maps. The inclusion and projection identify this image sheaf with \(B\). Componentwise, \(C\) decomposes as \(\operatorname{im}e\oplus\ker e\), and both summands respect the grading and restrictions.

A split inclusion includes its actual maps. In the perfect-pairing construction the adjoint projector acts on the same word sheaf, so these maps determine the embedded images whose duality is being compared.

## Comparison of two summands in one sheaf

Suppose \(B\) and \(D\) both split into a sheaf \(C\), with maps
\[
i:B\to C,\ p:C\to B,\qquad
j:D\to C,\ q:C\to D.
\]
The comparison from the first summand to the second is
\[
h=qi:B\to D.
\]
After inclusion in \(C\), it is \(jh=(jq)i\): include a vector from \(B\), then apply the projector selecting \(D\).

At a vertex where both projectors \(ip\) and \(jq\) are the identity on \(C^x\), the reverse map \(g=pj\) satisfies
\[
gh=pjqi=pi=1,\qquad hg=qipj=qj=1.
\]
Thus the comparison is bijective at that vertex.

For the word-sheaf splitting and its adjoint image, this is the canonical comparison map used in the perfect boundary-pairing construction.

## References

The precise Lean sources are listed below.

## Lean formalization

The fields `inclusion`, `projection`, `vertex_split`, and `edge_split` supply the two sheaf morphisms and the two families of splitting identities.

`OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn`: [SheafMorphisms.lean:1354](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1354).

`OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.projector`: [BalancedPairings.lean:1314](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1314).

`OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.comparison_bijective`: [EdgeLocalization.lean:785](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L785).
