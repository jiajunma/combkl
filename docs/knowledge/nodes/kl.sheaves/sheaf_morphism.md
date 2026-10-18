---
id: kl.detail.sheaf_morphism
title: Morphisms of graded graph sheaves
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.graded_sheaf
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.Hom
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:570
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.Hom
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

# Morphisms of graded graph sheaves

A morphism \(f:B\to C\) consists of degree-zero \(A\)-linear maps on every vertex and every edge,
\[
f_x:B^x\to C^x,\qquad f_e:B^e\to C^e,
\]
such that both restriction squares commute:
\[
f_e\rho^B_{x,e}=\rho^C_{x,e}f_x,\qquad
f_e\rho^B_{y,e}=\rho^C_{y,e}f_y.
\]
Composition is componentwise. A graded sheaf isomorphism has invertible component maps with degree-preserving inverses.

A map on an upper set is partial sheaf-morphism data: vertex maps are specified on that upper set and the relevant edge maps commute with all already specified restrictions. Extending such data downward requires a lifting theorem; assigning arbitrary stalk maps would generally destroy the restriction squares.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization

The fields `vertex`, `edge`, `lower`, and `upper` record the component maps and the two commutation conditions.

`OAI.KLInvariance.MomentGraph.GradedSheaf.Hom`: [SheafMorphisms.lean:570](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L570).
