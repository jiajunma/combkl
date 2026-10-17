---
id: kl.duality.bott_character_decomposition
title: Simultaneous decomposition of Bott–Samelson stalk and kernel characters
kind: theorem
status: proved
primary_topic: kl.05_duality_and_characters
topics:
- kl.05_duality_and_characters
uses:
- kl.duality.stalk_character
- kl.sheaves.boundary_existence
- kl.notes.bott_samelson
- kl.notes.word_stalks
- kl.notes.supported_pairings
- kl.detail.model_decomposition
- kl.detail.word_flabbiness
- kl.detail.costalk_reciprocity
- kl.detail.boundary_pairing
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  declarations:
  - OAI.KLInvariance.TitsSpace.bottCharacter_decomposition_both
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:2019
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCharacter_decomposition_both
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

# Simultaneous decomposition of Bott–Samelson stalk and kernel characters

Fix a reduced word with product \(b\). There are polynomials \(m_y(q)\in\mathbb Z[q]\) with nonnegative coefficients such that the associated Bott–Samelson stalk characters and full upward-kernel characters decompose simultaneously as
\[
C^{\mathrm{word}}_x(q)=\sum_{y\le b}m_y(q)C_{x,y}(q),
\]
\[
K^{\mathrm{word}}_x(q)
=\sum_{y\le b}m_y(q)\,q^{d(x,y)}C_{x,y}(q^{-1}).
\]
Character terms outside their lower intervals are interpreted as zero.

*Proof.*

The actual polynomial sheaf attached to the word has free stalks and kernels, the required edge quotients, extension of sections, and global generation. The boundary-model family also has the required kernel freeness.

Apply the graded-sheaf character decomposition theorem with these inputs. Rewrite its two identities using the character descriptions of the word object and of the boundary models. Both identities use the same decomposition multiplicities.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottCharacter_decomposition_both`: [CharacterReciprocity.lean:2019](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L2019).
