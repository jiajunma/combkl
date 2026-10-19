---
id: kl.sheaves.word_boundary_summand
title: A normalized boundary sheaf is a graded summand of a word sheaf
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.top_splitting
- kl.detail.word_flabbiness
- kl.detail.word_standard_stalks
- kl.word.top_stalk
- kl.detail.word_sheaf
- kl.sheaves.boundary_sheaf
- kl.sheaves.boundary_top_detection
lean:
  repository: openai-kl
  modules:
  - Frobenius
  - Support
  declarations:
  - OAI.KLInvariance.TitsSpace.bottBoundarySheafTopInclusion
  - OAI.KLInvariance.TitsSpace.bottBoundarySheafTopProjection
  - OAI.KLInvariance.TitsSpace.bottBoundarySheafTop_split
  - OAI.KLInvariance.TitsSpace.bottBoundarySheaf_splitIn
  - OAI.KLInvariance.TitsSpace.bottProjectionSheaf_generated
  - OAI.KLInvariance.TitsSpace.bottGradedProjectionSheaf_upperQuotient
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:263
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottBoundarySheafTopInclusion
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:272
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottBoundarySheafTopProjection
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:281
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottBoundarySheafTop_split
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:293
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottBoundarySheaf_splitIn
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1792
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottProjectionSheaf_generated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:257
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottGradedProjectionSheaf_upperQuotient
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the bilinear form, coefficient ring, finite coordinate presentation
    and lifting hypotheses explicit?
  verdict: Read the two top maps, their pointwise inverse identity and all arguments
    to splitIn_of_top_split. Checked the actual symmetric coefficient model, finite
    interval, free/quotient/flabby/generated properties and graded top normalization.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# A normalized boundary sheaf is a graded summand of a word sheaf

Fix a finite-generator Coxeter system and a reduced word \(\mathbf t\) with product \(b\). Choose a finite basis of the extended realization and use its degree-one symmetric coefficient grading.

Let \(B\) be a normalized boundary sheaf on \([1,b]\), with the symmetric root labels and top \(b\). Let \(C\) be the graded pair-projection sheaf of the word. Then there are degree-zero sheaf maps
\[
i:B\to C,\qquad p:C\to B,\qquad pi=1_B.
\]
Thus \(B\) is a graded direct summand of \(C\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit word-image construction of the extension property.**

**OpenAI notes:** The moment-graph sheaf theorem gives extension of compatible sections on upper sets for the normalized boundary sheaf through the cited Braden–MacPherson and Soergel bridges. [bg:bmp](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

**Lean (primary):** The word module gives coordinate images and stable coefficient characters. Reflection geometry makes each prime congruence class a single weight or a reflection pair. Explicit diagonal operators combine class lifts, and prime-denominator removal proves compatible-tuple lifting from image projectivity. The word induction supplies upper-image projectivity using its two kernel sequences. [IntegralPairings:470](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L470), [IntegralPairings:467](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L467), [IntegralPairings:1299](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1299), [IntegralPairings:1408](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1408), [IntegralPairings:2057](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2057), [IntegralPairings:1620](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1620), [IntegralPairings:1833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1833), [BalancedPairings:292](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L292), [Support:293](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L293).

**Role in the proof:** Upper-image lifting gives interval flabbiness after extension to the ambient upper closure. Full-interval section realization also has a direct free-image proof. Free stalks, root quotients, flabbiness, generation and the normalized word top then supply the graded boundary summand.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Check the ring and graph conditions

The coefficient ring is a symmetric algebra on a finite-dimensional real vector space, hence a polynomial ring after choosing the basis. It is a connected nonnegatively graded Noetherian domain.

The Bruhat interval is finite and has greatest vertex \(b\). Its edge set is finite as well, and both sheaves use the same symmetric root label at each edge. These are the ambient conditions of the [[node:kl.detail.top_splitting|top-splitting theorem]].

### Step 2. Check the word-sheaf properties

The [[node:kl.detail.word_standard_stalks|word-stalk induction]] gives free stalks and the exact upper edge kernel
\(\alpha_E C^y\). The upper restriction is surjective, so \(C\) has the required upper-quotient rule.

The [[node:kl.detail.word_flabbiness|interval word-sheaf theorem]] gives flabbiness. Global generation follows directly from stalk surjectivity: for a prescribed vector at one vertex, choose a word lift, and take all its vertex projections as a compatible global section.

Thus \(C\) has every sheaf property required by the [[node:kl.detail.top_splitting|top-splitting theorem]].

### Step 3. Construct inverse maps at the top vertex

Normalization gives a degree-zero identification
\(\eta_B:B^b\xrightarrow{\sim}A\).
The [[node:kl.word.top_stalk|reduced-word top-stalk theorem]] gives
\(\eta_C:C^b\xrightarrow{\sim}A\), also preserving degree in both directions.

Define
\[
i_b=\eta_C^{-1}\eta_B,\qquad
p_b=\eta_B^{-1}\eta_C.
\]
Their composite is
\[
p_bi_b
=\eta_B^{-1}\eta_C\eta_C^{-1}\eta_B
=1_{B^b}.
\]
These are the source's bottBoundarySheafTopInclusion and bottBoundarySheafTopProjection. Its top-splitting identity is exactly this cancellation.

### Step 4. Extend and correct the sheaf maps

Apply the [[node:kl.detail.top_splitting|top-splitting theorem]] with the properties checked in Steps 1–3. Its morphism-extension argument first produces degree-zero sheaf maps
\(i_0:B\to C\), \(p_0:C\to B\) having the prescribed top components.

Their composite \(h=p_0i_0\) is the identity at the top. The [[node:kl.sheaves.boundary_top_detection|boundary top-detection theorem]] makes \(h\) a sheaf automorphism. Set
\[
i=i_0h^{-1},\qquad p=p_0.
\]
Then \(pi=p_0i_0h^{-1}=hh^{-1}=1_B\). These maps give the asserted graded summand.

The source packages their existence as bottBoundarySheaf_splitIn. This split inclusion is the input to the later adjoint and boundary-duality constructions.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottBoundarySheafTopInclusion`: [Support.lean:263](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L263).

`OAI.KLInvariance.TitsSpace.bottBoundarySheafTopProjection`: [Support.lean:272](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L272).

`OAI.KLInvariance.TitsSpace.bottBoundarySheafTop_split`: [Support.lean:281](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L281).

`OAI.KLInvariance.TitsSpace.bottBoundarySheaf_splitIn`: [Support.lean:293](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L293).

`OAI.KLInvariance.TitsSpace.bottProjectionSheaf_generated`: [Frobenius.lean:1792](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1792).

`OAI.KLInvariance.TitsSpace.bottGradedProjectionSheaf_upperQuotient`: [Support.lean:257](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L257).
