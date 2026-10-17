---
id: kl.detail.boundary_uniqueness
title: Uniqueness of the minimal-boundary sheaf up to graded isomorphism
kind: theorem
status: proved
primary_topic: kl.04_moment_graph_sheaves
topics:
- kl.04_moment_graph_sheaves
uses:
- kl.sheaves.boundary_sheaf
- kl.detail.boundary_extension
- kl.notes.graded_nakayama
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.BoundarySheaf.exists_gradedIso
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:829
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.BoundarySheaf.exists_gradedIso
  - artifact: openai-kl-paper
    locator: Related paper context; bg:bmp
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- moment_graph_sheaves
---

# Uniqueness of the minimal-boundary sheaf up to graded isomorphism

Let \(A\) be a connected nonnegatively graded Noetherian domain over a field, and let a finite labelled ordered graph have a greatest vertex \(b\). Two minimal-boundary sheaves with the same labels and top normalization are graded-isomorphic.

The assertion is existence of an isomorphism, not uniqueness of that isomorphism.

*Proof.*

Construct an isomorphism by descending through the vertex order. At \(b\), both stalks are the normalized rank-one module. Suppose it is already constructed on an upper set. The quotient rules induce compatible isomorphisms on the adjacent edge modules, and hence on the next boundary image.

Both new stalks are minimal graded free covers of the identified boundary image. Lift the comparison through the covers. Their maps on the quotient by the positive-degree ideal are isomorphisms; graded Nakayama upgrades the lift to an isomorphism. The upper quotient property supplies the corresponding edge maps. Continue until every vertex has been added.

This result justifies making choices of minimal covers in the construction. It identifies the resulting graded sheaf independently of those choices; it does not identify its character with a KL polynomial.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization



`OAI.KLInvariance.MomentGraph.BoundarySheaf.exists_gradedIso`: [MinimalExtensions.lean:829](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L829).
