---
id: kl.duality.actual_character_reciprocity
title: R-reciprocity for the actual boundary-sheaf character
kind: theorem
status: proved
primary_topic: kl.05_duality_and_characters
topics:
- kl.05_duality_and_characters
uses:
- kl.duality.bott_character_decomposition
- kl.duality.stalk_character
- kl.foundations.rtilde
- kl.notes.character_cancellation
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.BruhatGraph.stalkCharacter_reciprocity
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:62
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.stalkCharacter_reciprocity
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
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
- background
---

# R-reciprocity for the actual boundary-sheaf character

In a finite-generator real realization, let \(C_{x,b}(q)\) be the stalk character of the constructed minimal-boundary sheaf. Then
\[
q^{d(x,b)}C_{x,b}(q^{-1})
=\sum_{x\le z\le b}R_{x,z}(q)C_{z,b}(q).
\]

*Proof.*

Choose a reduced word for \(b\). Decompose its Bott–Samelson stalk and kernel characters simultaneously into boundary-sheaf characters at lower vertices. The top decomposition coefficient is one.

The word object's kernel character already satisfies the R-convolution formula. Apply induction to the shorter vertices and cancel every lower term in the two finite sums. The remaining top term is the required reciprocal identity.

This theorem concerns the actually constructed characters. The main argument uses it to compare R-tilde polynomials; the canonical KL polynomials are handled later.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.stalkCharacter_reciprocity`: [DyerPaths.lean:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L62).
