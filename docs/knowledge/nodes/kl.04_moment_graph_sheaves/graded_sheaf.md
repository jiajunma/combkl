---
id: kl.detail.graded_sheaf
title: Graded sheaves and homogeneous restriction maps
kind: definition
status: formalized
primary_topic: kl.04_moment_graph_sheaves
topics:
- kl.04_moment_graph_sheaves
uses:
- kl.sheaves.graph_sheaf
- kl.sheaves.graded_module
- kl.detail.graded_maps_shifts
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:20
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf
  - artifact: openai-kl-paper
    locator: Related paper context; bg:bmp
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
- moment_graph_sheaves
---

# Graded sheaves and homogeneous restriction maps

Let \(A=\bigoplus_n A_n\) be a graded algebra over a field \(k\). A graded sheaf assigns a finite nonnegatively graded \(A\)-module \(B^x\) to every vertex and such a module \(B^e\) to every edge. Its lower and upper restriction maps have degree zero:
\[
\rho_{x,e}(B^x_n)\subseteq B^e_n.
\]
Forgetting the grading gives an ordinary graph sheaf.

Because all restrictions preserve degree, the homogeneous components of a compatible section remain compatible. The section space, boundary image, and intersections of outgoing restriction kernels therefore inherit gradings. These inherited gradings are what make subsequent Hilbert-series comparisons meaningful.

A graded sheaf does not, by definition, have free stalks, quotient edge maps, or extension of sections. Those are separate properties imposed on minimal-boundary sheaves and proved for the word constructions.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization

The fields `vertex` and `edge` are graded module data; `lower` and `upper` are degree-zero graded homomorphisms.

`OAI.KLInvariance.MomentGraph.GradedSheaf`: [GradedSheaves.lean:20](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L20).
