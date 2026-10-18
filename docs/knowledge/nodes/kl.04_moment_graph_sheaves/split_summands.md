---
id: kl.detail.split_summands
title: Split sheaf summands and their projectors
kind: definition
status: formalized
primary_topic: kl.04_moment_graph_sheaves
topics:
- kl.04_moment_graph_sheaves
uses:
- kl.detail.sheaf_morphism
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  - BalancedPairings
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn
  - OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.projector
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

## References

The precise Lean sources are listed below.

## Lean formalization

The fields `inclusion`, `projection`, `vertex_split`, and `edge_split` supply the two sheaf morphisms and the two families of splitting identities.

`OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn`: [SheafMorphisms.lean:1354](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1354).

`OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.projector`: [BalancedPairings.lean:1314](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1314).
