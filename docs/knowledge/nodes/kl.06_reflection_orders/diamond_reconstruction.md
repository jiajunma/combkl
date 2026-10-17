---
id: kl.detail.diamond_reconstruction
title: Recovering every reflection edge from the interval order
kind: theorem
status: proved
primary_topic: kl.06_reflection_orders
topics:
- kl.06_reflection_orders
uses:
- kl.detail.diamond_closure
- kl.foundations.finite_support
- kl.notes.relative_dihedral_intervals
- kl.realization.reflection_plane
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.diamondEdges_of_bruhatStep_general
  - OAI.KLInvariance.diamondEdges_bruhatStep_general
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:175
    format: lean-location
    note: OAI.KLInvariance.diamondEdges_of_bruhatStep_general
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:204
    format: lean-location
    note: OAI.KLInvariance.diamondEdges_bruhatStep_general
  - artifact: openai-kl-paper
    locator: Related paper context; sec:dihedral
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
- reflection_orders
---

# Recovering every reflection edge from the interval order

For vertices \(x,y\) in any Bruhat interval, including intervals in Coxeter systems with infinitely many generators,
\[
D(x,y)\quad\Longleftrightarrow\quad x\longrightarrow y
\]
is an upward reflection edge. Thus the full directed reflection graph is recoverable from the unlabelled interval order.

*Proof.*

For one direction, covers are reflection edges and the eight-edge diamond rule is valid for reflection edges. Induction on the diamond-closure derivation proves \(D(x,y)\Rightarrow x\to y\).

For the converse in finite-generator systems, analyze a non-cover reflection edge in a suitable rank-two reflection subgroup. The dihedral interval supplies a diamond whose component edges have smaller rank difference. Apply induction to those edges and then the closure rule.

For arbitrary generating sets, place the finite lower ideal below the interval's top in a finitely generated standard parabolic subgroup. Its inclusion preserves the relevant Bruhat order and reflection edges. Apply the finite-generator result there and transport the diamond derivation back.

The labels themselves are not recovered by this argument. What is recovered is precisely the edge relation needed to transport schedules.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L2).

## Lean formalization



`OAI.KLInvariance.diamondEdges_of_bruhatStep_general`: [DyerPaths.lean:175](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L175).

`OAI.KLInvariance.diamondEdges_bruhatStep_general`: [DyerPaths.lean:204](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L204).
