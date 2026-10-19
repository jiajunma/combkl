---
id: kl.word.upper_image_induction
title: Projective upper images and compatible lifts for every word
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.upper_image_properties
- kl.word.upper_image_lifting
- kl.word.upper_projectivity_step
- kl.word.evaluation_maps
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.bottSetProjection_nil_injective
  - OAI.KLInvariance.TitsSpace.bottSetImage_nil_subsingleton
  - OAI.KLInvariance.TitsSpace.bottSetImage_nil_projective
  - OAI.KLInvariance.TitsSpace.bottProjectiveUpper
  - OAI.KLInvariance.TitsSpace.bottFlabby
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2084
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSetProjection_nil_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2091
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSetImage_nil_subsingleton
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2101
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSetImage_nil_projective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2109
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottProjectiveUpper
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2114
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottFlabby
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the bilinear form, coefficient ring, finite coordinate presentation
    and lifting hypotheses explicit?
  verdict: Read the two empty-image cases and the precise bottProjectiveUpper induction.
    Retained the intermediate application of bottFlabby_of_projective to the tail
    and the final fixed-word lifting application.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Projective upper images and compatible lifts for every word

Fix a finite-generator Coxeter system and its symmetric coefficient algebra \(A\). For every word \(\mathbf t\):

1. every image \(L_{\mathbf t}(U)\) on a Bruhat upper set is projective;
2. every compatible tuple on such a set has a common word preimage.

These are the source's bottProjectiveUpper and bottFlabby theorems.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit word-image construction of the extension property.**

**OpenAI notes:** The moment-graph sheaf theorem gives extension of compatible sections on upper sets for the normalized boundary sheaf through the cited Braden–MacPherson and Soergel bridges. [bg:bmp](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

**Lean (primary):** The word module gives coordinate images and stable coefficient characters. Reflection geometry makes each prime congruence class a single weight or a reflection pair. Explicit diagonal operators combine class lifts, and prime-denominator removal proves compatible-tuple lifting from image projectivity. The word induction supplies upper-image projectivity using its two kernel sequences. [IntegralPairings:470](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L470), [IntegralPairings:467](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L467), [IntegralPairings:1299](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1299), [IntegralPairings:1408](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1408), [IntegralPairings:2057](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2057), [IntegralPairings:1620](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1620), [IntegralPairings:1833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1833), [BalancedPairings:292](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L292), [Support:293](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L293).

**Role in the proof:** Upper-image lifting gives interval flabbiness after extension to the ambient upper closure. Full-interval section realization also has a direct free-image proof. Free stalks, root quotients, flabbiness, generation and the normalized word top then supply the graded boundary summand.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Describe every empty-word image

The empty-word module is \(A\), with its only subexpression at weight \(1\), evaluated by the identity.

If \(1\in U\), the image projection \(A\to L_\varnothing(U)\) is injective because its weight-\(1\) coordinate recovers the coefficient. It is surjective by the image definition, so \(L_\varnothing(U)\simeq A\).

If \(1\notin U\), every selected stalk has an empty coordinate set and is zero. Thus \(L_\varnothing(U)=0\).

Both \(A\) and \(0\) are projective. This establishes upper-image projectivity for the empty word, and in fact describes its image on every subset.

### Step 2. State the induction hypothesis

Assume that the shorter word \(\mathbf t\) has projective images on every upper set. The [[node:kl.word.upper_image_lifting|fixed-word lifting theorem]] then gives compatible-tuple lifting for \(\mathbf t\).

Thus both hypotheses needed for the conditional projectivity step are now available for the same shorter word.

### Step 3. Prepend a simple reflection

For any simple reflection \(s\), apply the [[node:kl.word.upper_projectivity_step|conditional upper-image projectivity theorem]]. It uses the two descended tail maps, the patched common kernel and the two split sequences to prove projectivity of \(L_{s\mathbf t}(U)\) for every upper set \(U\).

This completes the induction step. The tail word has one fewer letter, so Steps 1–3 prove upper-image projectivity for all finite words.

### Step 4. Obtain lifting for the resulting word

Apply the [[node:kl.word.upper_image_lifting|fixed-word lifting theorem]] once more, now to the upper-image projectivity proved for an arbitrary \(\mathbf t\). It gives compatible-tuple lifting for that word.

The logical order is therefore: the fixed-word implication from projectivity to lifting, followed by word induction for projectivity using that implication on each tail, and finally lifting for every word.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottSetProjection_nil_injective`: [IntegralPairings.lean:2084](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2084).

`OAI.KLInvariance.TitsSpace.bottSetImage_nil_subsingleton`: [IntegralPairings.lean:2091](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2091).

`OAI.KLInvariance.TitsSpace.bottSetImage_nil_projective`: [IntegralPairings.lean:2101](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2101).

`OAI.KLInvariance.TitsSpace.bottProjectiveUpper`: [IntegralPairings.lean:2109](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2109).

`OAI.KLInvariance.TitsSpace.bottFlabby`: [IntegralPairings.lean:2114](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2114).
