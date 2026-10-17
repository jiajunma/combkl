---
id: kl.detail.indecomposable_boundary
title: Indecomposability of the normalized boundary sheaf
kind: theorem
status: proved
primary_topic: kl.04_moment_graph_sheaves
topics:
- kl.04_moment_graph_sheaves
uses:
- kl.sheaves.boundary_sheaf
- kl.detail.sheaf_morphism
- kl.notes.graded_nakayama
lean:
  repository: openai-kl
  modules:
  - BalancedPairings
  declarations:
  - OAI.KLInvariance.MomentGraph.BoundarySheaf.primitive_identity
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1974
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.BoundarySheaf.primitive_identity
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

# Indecomposability of the normalized boundary sheaf

Over a nonnegatively graded domain, the normalized minimal-boundary sheaf on a finite ordered graph has no nontrivial graded idempotent endomorphism:
\[
p^2=p\quad\Longrightarrow\quad p=0\ \text{or}\ p=1.
\]
Equivalently, its identity is a primitive projector, so the sheaf cannot split into two nonzero graded direct summands.

*Proof.*

At the rank-one top stalk, an idempotent is multiplication by an idempotent scalar. A domain has only the scalars \(0\) and \(1\) with that property. The minimal-boundary conditions propagate this choice down the graph: the induced maps on the boundary and then on the minimal generator quotient determine which of the two complementary projectors can have a nonzero image at the next stalk. Graded Nakayama eliminates the other image.

Iterating over the finite vertex order makes the same projector vanish everywhere. The commuting restriction maps and upper surjectivity determine the corresponding edge maps as well. The result is a statement about the entire sheaf, not merely its top stalk.

This primitive-projector property is later used when recognizing the adjoint of a boundary summand in a word sheaf.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization



`OAI.KLInvariance.MomentGraph.BoundarySheaf.primitive_identity`: [BalancedPairings.lean:1974](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1974).
