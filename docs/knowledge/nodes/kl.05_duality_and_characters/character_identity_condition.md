---
id: kl.duality.character_identity_condition
title: The stalk-character identification condition
kind: definition
status: formalized
primary_topic: kl.05_duality_and_characters
topics:
- kl.05_duality_and_characters
uses:
- kl.duality.stalk_character
- kl.foundations.canonical_kl
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.BruhatGraph.StalkCharacterObligation
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:219
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.StalkCharacterObligation
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  definition: accepted
  proof: not_applicable
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

# The stalk-character identification condition

For a fixed boundary sheaf on an interval, the stalk-character identification condition is
\[
\forall x\in[u,b],\qquad C_{x,b}(q)=P_{x,b}(q).
\]
It relates the character defined by graded stalks to the KL polynomials defined by normalization and recursion.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`StalkCharacterObligation` defines this proposition. Interfaces taking it as an argument retain that argument. The main proof instead uses the actual character's R-reciprocity to establish R-tilde invariance before treating the canonical KL polynomials.

`OAI.KLInvariance.BruhatGraph.StalkCharacterObligation`: [SheafMorphisms.lean:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219).
