---
id: kl.detail.model_decomposition
title: Decomposing a free flabby sheaf into shifted boundary models
kind: theorem
status: proved
primary_topic: kl.04_moment_graph_sheaves
topics:
- kl.04_moment_graph_sheaves
uses:
- kl.detail.boundary_models
- kl.detail.morphism_extension
- kl.detail.top_splitting
- kl.notes.minimal_cover_existence
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.exists_modelSumIso
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1642
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.exists_modelSumIso
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

# Decomposing a free flabby sheaf into shifted boundary models

Let \(A\) be a connected nonnegatively graded Noetherian domain and let the labelled ordered graph be finite. Fix a boundary-model family \(O_c\). Every graded sheaf \(B\) with free stalks, the upper quotient rule, flabbiness, and global generation admits a graded isomorphism
\[
B\simeq\bigoplus_{c,i}O_c(d_{c,i}),\qquad d_{c,i}\in\mathbb N,
\]
with finitely many summands.

*Proof.*

Proceed downward through the vertices, maintaining a model sum already identified with \(B\) above the next vertex \(x\). The boundary is thereby fixed. A minimal free cover of this boundary splits out of the free stalk \(B^x\). The remaining free generators determine nonnegative shifts of the model supported below \(x\).

Add these shifted copies to the current model sum. The stalk splitting and the upper quotient rule extend the isomorphism over the newly added vertex and its edges. Iterate over the finite vertex set.

This is an isomorphism of graded sheaves, so it controls stalks and restriction kernels simultaneously. The character decomposition later uses this same collection of shifts for both families; choosing two unrelated polynomial decompositions would not suffice.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization



`OAI.KLInvariance.MomentGraph.GradedSheaf.exists_modelSumIso`: [SheafMorphisms.lean:1642](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1642).
