---
id: kl.detail.word_flabbiness
title: Flabbiness of the actual word sheaf
kind: theorem
status: proved
primary_topic: kl.05_duality_and_characters
topics:
- kl.05_duality_and_characters
uses:
- kl.detail.word_sheaf
- kl.sheaves.flabbiness
- kl.notes.reflection_frobenius
- kl.notes.tensor_pairing
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.bottProjectiveUpper
  - OAI.KLInvariance.TitsSpace.bottFlabby
  - OAI.KLInvariance.TitsSpace.bottProjectionSheaf_flabby
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2109
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottProjectiveUpper
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2114
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottFlabby
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2192
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottProjectionSheaf_flabby
  - artifact: openai-kl-paper
    locator: Related paper context; bg:normalization
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
- duality_and_characters
---

# Flabbiness of the actual word sheaf

For a reduced word \(\mathbf s\) with product \(b\), its pair-projection sheaf on \([1,b]\) is flabby. Thus every compatible section on an upper subset extends to a global section.

*Proof.*

The construction proves two word-module assertions together along the length of the word: projected modules on upper sets are projective, and compatible upper-set coordinates lift to the word module. For the empty word, the only nonzero weight is \(1\), so both statements are immediate.

For a longer word, tensor induction along the rank-two Frobenius extension supplies projective upper projections. The lifting argument first produces compatible local lifts at prime factors. The integral membership argument removes the local denominators and obtains a genuine word-module element realizing the coordinates. This is stronger than a lift in the fraction field.

To pass to the interval sheaf, extend an interval upper-set assignment by zero above the support \([1,b]\). Reducedness ensures that the word stalks outside that lower ideal vanish. The word-module lifting theorem applies to this extended assignment, and its image under the global-section map gives the required extension on the interval.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization



`OAI.KLInvariance.TitsSpace.bottProjectiveUpper`: [IntegralPairings.lean:2109](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2109).

`OAI.KLInvariance.TitsSpace.bottFlabby`: [IntegralPairings.lean:2114](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2114).

`OAI.KLInvariance.TitsSpace.bottProjectionSheaf_flabby`: [IntegralPairings.lean:2192](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2192).
