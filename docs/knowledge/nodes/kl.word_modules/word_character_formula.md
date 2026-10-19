---
id: kl.detail.word_character_formula
title: Word-stalk characters equal positive Hecke-word coefficients
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.detail.word_characters
- kl.word.character_recursion
- kl.word.character_normalization
- kl.hecke.positive_words
- kl.definitions.hecke_operators
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.bottStalkCharacter_eq_heckeWord
  - OAI.KLInvariance.HeckeQ.positiveWord
  - OAI.KLInvariance.HeckeQ.positiveWord_nil
  - OAI.KLInvariance.HeckeQ.positiveWord_cons_coeff
  - OAI.KLInvariance.HeckeQ.left_coeff
  - OAI.KLInvariance.HeckeQ.left_plus_coeff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:289
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkCharacter_eq_heckeWord
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:204
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.positiveWord
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:208
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.positiveWord_nil
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:211
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.positiveWord_cons_coeff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:152
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.left_coeff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:197
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.left_plus_coeff
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the gradings, scalar actions, coefficient variables and formal polynomial
    conclusions explicit?
  verdict: Rewrote the equality proof as the source induction on the whole coefficient
    family, with exact output-weight Hecke contributions, the empty-word base and
    both tail substitutions. The graded-kernel and numerator arguments now have their
    own detailed prerequisites.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Word-stalk characters equal positive Hecke-word coefficients

Fix a finite-generator Coxeter system and a finite basis of its extended realization. For every word \(\mathbf t=(s_1,\ldots,s_m)\) and every \(x\in W\),
\[
C_x^{\mathbf t}(q)
=[T_x](I+L_{s_1}(q))\cdots(I+L_{s_m}(q))T_1.
\]
The Hecke module here has coefficient ring \(\mathbb Z[q]\). Here \(C_x^{\mathbf t}\in\mathbb Z[q]\) is the character of the actual word stalk, \(L_s(q)\) is the unnormalized left Hecke operator, and \([T_x]\) extracts the coefficient of the standard basis vector \(T_x\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate objects.**

**OpenAI notes:** The normalization discussion identifies indecomposable boundary-sheaf characters with KL polynomials by the cited character theorem. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The word-stalk character is proved to equal a positive Hecke-word coefficient. Its R-convolution is then proved before model decomposition and cancellation. The separate boundary-character identification is exposed as StalkCharacterObligation. [IntegralPairings:289](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L289), [CharacterReciprocity:1134](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1134), [SheafMorphisms:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219), [BottSamelson:1924](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1924), [BottSamelson:1945](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1945), [IntegralPairings:104](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L104), [IntegralPairings:120](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L120), [CharacterReciprocity:915](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L915).

**Role in the proof:** The word formula and R-convolution describe the tensor word. A common decomposition into boundary models then supplies the character identities used in the cancellation argument.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Name the positive-word coefficients

Let
\[
H_\varnothing=T_1,\qquad
H_{s\mathbf t}=H_{\mathbf t}+L_s(q)H_{\mathbf t},
\qquad h_{\mathbf t}(x;q)=[T_x]H_{\mathbf t}.
\]
This recursion gives the written factor order. We prove equality
\(C_x^{\mathbf t}(q)=h_{\mathbf t}(x;q)\) for all \(x\), by induction on the word.

### Step 2. Verify the empty-word values

The standard vector \(T_1\) has coefficient \(1\) at \(x=1\) and \(0\) elsewhere. The [[node:kl.word.character_normalization|empty-word character theorem]] gives exactly those same values. Thus the induction starts at the empty word.

### Step 3. Read the positive Hecke recurrence at the output weight

Only the standard input weights \(x\) and \(sx\) contribute to the coefficient at \(x\) after applying \(L_s(q)\).

If \(\ell(sx)<\ell(x)\), the input \(sx\) contributes \(h_{\mathbf t}(sx;q)\), and the input \(x\) contributes \((q-1)h_{\mathbf t}(x;q)\). Adding the original vector changes the latter factor to \(q\). Hence
\[
h_{s\mathbf t}(x;q)
=h_{\mathbf t}(sx;q)+q\,h_{\mathbf t}(x;q).
\]

If \(\ell(x)<\ell(sx)\), the operator contributes
\(q\,h_{\mathbf t}(sx;q)\), and addition of the original vector gives
\[
h_{s\mathbf t}(x;q)
=h_{\mathbf t}(x;q)+q\,h_{\mathbf t}(sx;q).
\]
These are the positive-word coefficient identities.

### Step 4. Substitute the induction hypothesis at both tail weights

Assume \(C_y^{\mathbf t}=h_{\mathbf t}(y)\) for every \(y\in W\). Apply the [[node:kl.word.character_recursion|word-character recurrence]] at \(x\).

In the descent case it gives
\[
C_x^{s\mathbf t}
=C_{sx}^{\mathbf t}+qC_x^{\mathbf t}
=h_{\mathbf t}(sx)+q h_{\mathbf t}(x)
=h_{s\mathbf t}(x).
\]
In the ascent case it gives
\[
C_x^{s\mathbf t}
=C_x^{\mathbf t}+qC_{sx}^{\mathbf t}
=h_{\mathbf t}(x)+q h_{\mathbf t}(sx)
=h_{s\mathbf t}(x).
\]
Both substituted tail weights are covered by the same induction hypothesis. This proves the equality for the longer word and completes the induction.

The resulting coefficient identity is the word-character input to the later decomposition into shifted boundary models and actual-character reciprocity.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottStalkCharacter_eq_heckeWord`: [IntegralPairings.lean:289](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L289).

`OAI.KLInvariance.HeckeQ.positiveWord`: [IntegralPairings.lean:204](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L204).

`OAI.KLInvariance.HeckeQ.positiveWord_nil`: [IntegralPairings.lean:208](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L208).

`OAI.KLInvariance.HeckeQ.positiveWord_cons_coeff`: [IntegralPairings.lean:211](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L211).

`OAI.KLInvariance.HeckeQ.left_coeff`: [IntegralPairings.lean:152](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L152).

`OAI.KLInvariance.HeckeQ.left_plus_coeff`: [IntegralPairings.lean:197](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L197).
