---
id: kl.sheaves.projector_image
title: Image sheaves and the splitting of a projector
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.sheaf_morphism
- kl.algebra.homogeneous_subquotients
lean:
  repository: openai-kl
  modules:
  - BalancedPairings
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.image
  - OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.imageInclusion
  - OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.imageProjection
  - OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.imageSplit
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:873
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.image
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:879
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.imageInclusion
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:885
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.imageProjection
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:891
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.imageSplit
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

# Image sheaves and the splitting of a projector

Let \(B\) be a graded sheaf over a Noetherian coefficient algebra \(A\), and let \(h:B\to B\) be a graded sheaf endomorphism. Its image sheaf has modules
\[
(\operatorname{im}h)^x=\operatorname{im}h_x,\qquad
(\operatorname{im}h)^e=\operatorname{im}h_e,
\]
with the induced gradings.

The restrictions are those of \(B\), restricted to these submodules. For example,
\[
\rho^-_e(h_x(v))=h_e(\rho^-_e(v))
\]
lies in the edge image. The upper commuting square gives the same conclusion for the upper restriction. Thus both maps have the required codomains.

## Inclusion and projection

The component inclusions give a sheaf morphism
\[
i:\operatorname{im}h\to B.
\]
The maps \(v\mapsto h_x(v)\), viewed in their images, give
\[
p:B\to\operatorname{im}h.
\]
The sheaf-morphism equations for \(p\) are the commuting equations for \(h\). All maps preserve degree.

Suppose \(h\) is a projector: \(h_x^2=h_x\) and \(h_e^2=h_e\) at every component. If \(v=h_x(w)\), then \(h_x(v)=h_x^2(w)=h_x(w)=v\). Thus \(pi\) is the identity on each image stalk; the same calculation works on each edge. Hence \(i,p\) define a split inclusion, and \(ip=h\).

## The complementary summand

The endomorphism \(1-h\) is another projector. Componentwise,
\[
B^x=\operatorname{im}h_x\oplus\ker h_x.
\]
The explicit map sends \(v\) to \((h_xv,v-h_xv)\). The second component belongs to the kernel because \(h_x(v-h_xv)=h_xv-h_x^2v=0\). Its inverse adds the two components.

If a vector lies both in the image and kernel, write it \(h_xw\); applying \(h_x\) fixes it by idempotence and also gives zero, so the vector is zero. This proves directness. The restrictions commute with both \(h\) and \(1-h\), so the decompositions assemble into a decomposition of sheaves.

## The adjoint image

For a word-sheaf projector \(h\), the descended adjoint \(h^*\) is again a projector. Its image sheaf is built from the actual component images by this construction. The induced split maps will identify its global sections with the image of the adjoint on the word module.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.image`: [BalancedPairings.lean:873](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L873).

`OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.imageInclusion`: [BalancedPairings.lean:879](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L879).

`OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.imageProjection`: [BalancedPairings.lean:885](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L885).

`OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.imageSplit`: [BalancedPairings.lean:891](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L891).
