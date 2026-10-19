---
id: kl.duality.character_identity_condition
title: The stalk-character identification condition
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
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

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate statement.**

**OpenAI notes:** The grading-normalization proposition identifies the stalk graded rank with the canonical KL polynomial and uses the Elias–Williamson character theorem through the cited moment-graph bridges. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The development defines the equality of actual stalk characters and canonical KL polynomials as StalkCharacterObligation. The unconditional theorem used in the main route is R-reciprocity for the actual character. The local strict half-degree implication retains an explicit nonzero-diagonal hypothesis. [SheafMorphisms:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219), [DyerPaths:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L62), [PositiveTransfer:186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L186), [CharacterReciprocity:1807](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1807), [TerminalKernels:1273](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1273), [TerminalKernels:1284](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1284).

**Role in the proof:** The comparison uses the actual character C and its proved R-reciprocity. Canonical P is handled by the later polynomial-rigidity induction. The local degree result applies to a diagonal coefficient satisfying its stated nonvanishing hypothesis.
<!-- source-comparison:end -->

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`StalkCharacterObligation` defines this proposition. Interfaces taking it as an argument retain that argument. The main proof instead uses the actual character's R-reciprocity to establish R-tilde invariance before treating the canonical KL polynomials.

`OAI.KLInvariance.BruhatGraph.StalkCharacterObligation`: [SheafMorphisms.lean:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219).
