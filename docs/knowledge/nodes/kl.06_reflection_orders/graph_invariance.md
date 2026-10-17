---
id: kl.paths.graph_invariance
title: Unlabelled interval isomorphisms preserve reflection edges
kind: theorem
status: proved
primary_topic: kl.06_reflection_orders
topics:
- kl.06_reflection_orders
uses:
- kl.foundations.bruhat_step
- kl.foundations.interval
- kl.foundations.finite_support
- kl.detail.diamond_reconstruction
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.intervalIso_bruhatStep_iff_general
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:234
    format: lean-location
    note: OAI.KLInvariance.intervalIso_bruhatStep_iff_general
  - artifact: openai-kl-paper
    locator: 3. Dihedral intervals and transported reflection orders; sec:dihedral
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- dihedral
---

# Unlabelled interval isomorphisms preserve reflection edges

For an interval isomorphism \(\phi:[u,b]\simeq[u',b']\) in arbitrary Coxeter systems,
\[
x\longrightarrow y
\quad\Longleftrightarrow\quad
\phi(x)\longrightarrow\phi(y).
\]

*Proof.*

Characterize reflection edges by a diamond-closure relation defined solely from the partial order. Reflection edges satisfy the closure relation; rank-two reflection calculations establish the converse.

For systems with infinitely many generators, use finite generator support to pass to a standard parabolic system and transport the characterization back. Since diamond closure is preserved by an order isomorphism, reflection edges are preserved in both directions.

## References

[3. Dihedral intervals and transported reflection orders](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L2).

## Lean formalization

`OAI.KLInvariance.intervalIso_bruhatStep_iff_general`: [DyerPaths.lean:234](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L234).
