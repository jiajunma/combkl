---
id: kl.detail.word_flabbiness
title: Flabbiness of the actual word sheaf
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.interval_word_extension
- kl.word.upper_image_induction
- kl.algebra.pair_projection
- kl.word.weight_support
- kl.detail.word_sheaf
- kl.sheaves.flabbiness
lean:
  repository: openai-kl
  modules:
  - Frobenius
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.intervalUpperClosure_upper
  - OAI.KLInvariance.TitsSpace.intervalUpperClosure_member
  - OAI.KLInvariance.TitsSpace.bottIntervalExtension_compatible
  - OAI.KLInvariance.TitsSpace.bottProjectionSheaf_flabby
  - OAI.KLInvariance.TitsSpace.bottProjectionSheaf_generated
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2146
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.intervalUpperClosure_upper
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2152
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.intervalUpperClosure_member
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2172
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottIntervalExtension_compatible
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2192
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottProjectionSheaf_flabby
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1792
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottProjectionSheaf_generated
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
  prompt: Are the bilinear form, coefficient ring, finite coordinate presentation
    and lifting hypotheses explicit?
  verdict: Replaced the former combined outline by the exact ambient-closure proof
    in bottProjectionSheaf_flabby. Checked both endpoint cases, full-assignment conventions,
    reduced-word support and the final section map.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Flabbiness of the actual word sheaf

Fix a finite-generator Coxeter system and a reduced word \(\mathbf t\) with product \(b\). Its pair-projection sheaf \(S\) on \(I=[1,b]\) is flabby.

Explicitly, let \(U\subseteq I\) be upper and let \(f\) be an assignment on \(I\) compatible on every edge with both endpoints in \(U\). There is a compatible global assignment \(g\) on \(I\) satisfying
\[
g_x=f_x\qquad(x\in U).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit word-image construction of the extension property.**

**OpenAI notes:** The moment-graph sheaf theorem gives extension of compatible sections on upper sets for the normalized boundary sheaf through the cited Braden–MacPherson and Soergel bridges. [bg:bmp](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

**Lean (primary):** The word module gives coordinate images and stable coefficient characters. Reflection geometry makes each prime congruence class a single weight or a reflection pair. Explicit diagonal operators combine class lifts, and prime-denominator removal proves compatible-tuple lifting from image projectivity. The word induction supplies upper-image projectivity using its two kernel sequences. [IntegralPairings:470](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L470), [IntegralPairings:467](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L467), [IntegralPairings:1299](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1299), [IntegralPairings:1408](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1408), [IntegralPairings:2057](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2057), [IntegralPairings:1620](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1620), [IntegralPairings:1833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1833), [BalancedPairings:292](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L292), [Support:293](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L293).

**Role in the proof:** Upper-image lifting gives interval flabbiness after extension to the ambient upper closure. Full-interval section realization also has a direct free-image proof. Free stalks, root quotients, flabbiness, generation and the normalized word top then supply the graded boundary summand.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Form the ambient upper closure

Let
\[
\overline U=\{x\in W:\exists a\in U,\ a\le x\}.
\]
The [[node:kl.sheaves.interval_word_extension|interval-extension construction]] proves that this is upper in \(W\), and that its vertices below \(b\) are exactly those in \(U\).

Define \(\widetilde f\) on \(\overline U\) by \(f_x\) at \(x\le b\) and zero otherwise. A reduced word has zero stalk outside \([1,b]\), so each value is a vector in the required word stalk.

### Step 2. Verify compatibility when the upper endpoint is below b

Take an upward reflection edge \(x\to y\) in \(\overline U\). Suppose \(y\le b\). Then \(x\le y\le b\), so both endpoints are in the interval. By the upper-closure intersection property, both lie in \(U\).

The original compatibility assumption gives equality of their two edge restrictions. The pair-projection criterion therefore supplies a word vector \(m\) with
\[
\pi_x(m)=f_x=\widetilde f_x,\qquad
\pi_y(m)=f_y=\widetilde f_y.
\]
This is the required two-endpoint witness.

### Step 3. Verify compatibility when the upper endpoint is outside the support

Suppose \(y\not\le b\). The \(y\)-stalk is zero. Stalk surjectivity supplies a word vector \(m\) attaining the prescribed lower value \(\widetilde f_x\).

Its projection at \(y\) is automatically the unique zero vector, equal to \(\widetilde f_y\). Thus it realizes both endpoint values. This case also covers an edge whose two endpoints are outside the support.

Steps 2–3 prove compatibility of \(\widetilde f\) on \(\overline U\).

### Step 4. Lift the compatible ambient tuple

The [[node:kl.word.upper_image_induction|completed upper-image induction]] gives compatible-tuple lifting for the word \(\mathbf t\) on every ambient upper set. Apply it to \(\overline U\) and \(\widetilde f\).

It supplies \(m\in M_{\mathbf t}\) with
\[
\pi_x(m)=\widetilde f_x\qquad(x\in\overline U).
\]

### Step 5. Return to a global section of the interval sheaf

Define \(g_x=\pi_x(m)\) for every \(x\in I\). On any interval edge, the same word vector \(m\) is a common preimage of the two endpoint values. Hence \(g\) is compatible globally.

If \(x\in U\), then \(x\in\overline U\) and \(\widetilde f_x=f_x\). Step 4 gives \(g_x=f_x\). This proves flabbiness.

The source implements the final global assignment as bottSection applied to \(m\); its compatibility is built into the pair-projection sheaf construction.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.intervalUpperClosure_upper`: [IntegralPairings.lean:2146](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2146).

`OAI.KLInvariance.TitsSpace.intervalUpperClosure_member`: [IntegralPairings.lean:2152](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2152).

`OAI.KLInvariance.TitsSpace.bottIntervalExtension_compatible`: [IntegralPairings.lean:2172](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2172).

`OAI.KLInvariance.TitsSpace.bottProjectionSheaf_flabby`: [IntegralPairings.lean:2192](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2192).

`OAI.KLInvariance.TitsSpace.bottProjectionSheaf_generated`: [Frobenius.lean:1792](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1792).
