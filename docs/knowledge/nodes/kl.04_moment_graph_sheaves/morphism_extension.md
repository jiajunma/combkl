---
id: kl.detail.morphism_extension
title: Extending a sheaf morphism from an upper set
kind: theorem
status: proved
primary_topic: kl.04_moment_graph_sheaves
topics:
- kl.04_moment_graph_sheaves
uses:
- kl.detail.sheaf_morphism
- kl.detail.upper_quotient
- kl.sheaves.flabbiness
- kl.detail.compatible_sections
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.exists_extension
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:834
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.exists_extension
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

# Extending a sheaf morphism from an upper set

Let \(A\) be a connected nonnegatively graded Noetherian domain, and let the labelled ordered graph be finite. Suppose \(B\) and \(C\) satisfy the upper quotient rule, are flabby and globally generated, and every stalk of \(B\) is free. Then a graded sheaf morphism on an upper set \(U\) extends to a graded morphism \(B\to C\) agreeing with all its prescribed vertex maps.

*Proof.*

Choose a maximal vertex \(x\) outside \(U\). All its strict upper neighbors already lie in \(U\). The existing morphism induces a map between boundary images. Freeness of \(B^x\) lets this map lift through the surjective boundary map from \(C^x\). Flabbiness and global generation are what identify the required boundary image and supply that surjection.

For each new edge, the quotient rules ensure that the stalk lift descends to an edge map. The two commuting-square equations then hold by construction. Enlarge \(U\) by \(x\) and repeat. Finiteness guarantees termination.

The source freeness and the target boundary-surjectivity play different roles. The theorem does not require choosing unrelated isomorphisms of the edge modules.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization



`OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.exists_extension`: [SheafMorphisms.lean:834](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L834).
