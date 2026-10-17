---
id: kl.detail.top_splitting
title: Extending a split top stalk to a sheaf summand
kind: theorem
status: proved
primary_topic: kl.04_moment_graph_sheaves
topics:
- kl.04_moment_graph_sheaves
uses:
- kl.detail.morphism_extension
- kl.sheaves.boundary_sheaf
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.MomentGraph.BoundarySheaf.splitIn_of_top_split
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1380
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.BoundarySheaf.splitIn_of_top_split
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

# Extending a split top stalk to a sheaf summand

Let \(B\) be the normalized minimal-boundary sheaf on a finite labelled graph with greatest vertex \(b\), over a connected nonnegatively graded Noetherian domain. Let \(C\) be a graded sheaf with free stalks, the same upper quotient rule, flabbiness, and global generation. If graded maps
\[
i_b:B^b\to C^b,\qquad p_b:C^b\to B^b,\qquad p_bi_b=1
\]
split the top stalk, then \(B\) is a graded direct summand of \(C\).

*Proof.*

Extend \(i_b\) and \(p_b\) to sheaf morphisms \(i\) and \(p\). The composite \(f=pi\) is the identity at the top. Minimality propagates invertibility of an endomorphism downward: at each next stalk its induced map on the minimal generator quotient is invertible, and graded Nakayama completes the step. Hence \(f\) is a sheaf automorphism.

Replace \(i\) by \(if^{-1}\). Then \(p(if^{-1})=1\) on every stalk and edge. This correction is essential: arbitrary extensions of a split pair at the top need not initially compose to the identity everywhere.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization



`OAI.KLInvariance.MomentGraph.BoundarySheaf.splitIn_of_top_split`: [SheafMorphisms.lean:1380](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1380).
