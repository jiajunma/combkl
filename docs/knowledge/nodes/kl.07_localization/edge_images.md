---
id: kl.detail.edge_images
title: Lower and upper images in the same edge module
kind: definition
status: formalized
primary_topic: kl.07_localization
topics:
- kl.07_localization
uses:
- kl.sheaves.upward_kernel
- kl.detail.graded_sheaf
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.lowerImage
  - OAI.KLInvariance.MomentGraph.GradedSheaf.upperImage
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:362
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.lowerImage
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:366
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.upperImage
  - artifact: openai-kl-paper
    locator: Related paper context; edge:lattice
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- localization
---

# Lower and upper images in the same edge module

For an edge \(e:x\to y\), choose sets \(F\) and \(H\) of outgoing conditions at \(x\) and \(y\). Let \(K_x(F)\subseteq B^x\) and \(K_y(H)\subseteq B^y\) be the intersections of the corresponding restriction kernels. Define
\[
L_e(F)=\rho_{x,e}(K_x(F)),\qquad
U_e(H)=\rho_{y,e}(K_y(H)).
\]
Both are submodules of the same module \(B^e\). Their embeddings are part of the definition.

The global comparison seeks an inclusion
\(L_e(F)\subseteq f_eU_e(H)\), followed later by equality. An isomorphism of the two abstract modules would not establish this inclusion. Nor would equality after tensoring with the fraction field: a quotient supported in higher codimension could remain.

As the schedule changes, the sets \(F,H\) change, so these are images of filtered kernels rather than simply the images of the entire two stalks.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L26).

## Lean formalization



`OAI.KLInvariance.MomentGraph.GradedSheaf.lowerImage`: [PositiveTransfer.lean:362](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L362).

`OAI.KLInvariance.MomentGraph.GradedSheaf.upperImage`: [PositiveTransfer.lean:366](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L366).
