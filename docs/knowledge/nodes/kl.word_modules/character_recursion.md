---
id: kl.word.character_recursion
title: The ascent and descent recursions for word-stalk characters
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.stalk_degree_exactness
- kl.word.stalk_hilbert_formula
- kl.algebra.hilbert_numerators
- kl.word.character_normalization
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.bottStalkCharacter_ascent
  - OAI.KLInvariance.TitsSpace.bottStalkCharacter_descent
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:104
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkCharacter_ascent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:120
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkCharacter_descent
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the gradings, scalar actions, coefficient variables and formal polynomial
    conclusions explicit?
  verdict: Read both numerator_add_shift applications and their common nonzero coefficient
    factor. Preserved the exact ascent/descent roles and obtained formal polynomial
    equalities from convergent real evaluations.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# The ascent and descent recursions for word-stalk characters

Fix a finite-generator Coxeter system and a finite basis of its extended realization. For every word \(\mathbf t\), simple reflection \(s\), and weight \(x\), the formal character polynomials satisfy
\[
C_x^{s\mathbf t}(q)=
\begin{cases}
C_x^{\mathbf t}(q)+qC_{sx}^{\mathbf t}(q),&\ell(x)<\ell(sx),\\
C_{sx}^{\mathbf t}(q)+qC_x^{\mathbf t}(q),&\ell(sx)<\ell(x).
\end{cases}
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate objects.**

**OpenAI notes:** The normalization discussion identifies indecomposable boundary-sheaf characters with KL polynomials by the cited character theorem. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The word-stalk character is proved to equal a positive Hecke-word coefficient. Its R-convolution is then proved before model decomposition and cancellation. The separate boundary-character identification is exposed as StalkCharacterObligation. [IntegralPairings:289](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L289), [CharacterReciprocity:1134](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1134), [SheafMorphisms:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219), [BottSamelson:1924](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1924), [BottSamelson:1945](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1945), [IntegralPairings:104](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L104), [IntegralPairings:120](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L120), [CharacterReciprocity:915](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L915).

**Role in the proof:** The word formula and R-convolution describe the tensor word. A common decomposition into boundary models then supplies the character identities used in the cancellation argument.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Fix the common coefficient factor

All stalks in the formula use the same coefficient algebra and its fixed \(N\) degree-one variables. For real \(0<t<1\), put
\[
D(t)=(1-t)^{-N}.
\]
This factor is nonzero. The [[node:kl.word.stalk_hilbert_formula|word-stalk Hilbert theorem]] describes each stalk's convergent dimension sum by its character evaluated at \(t\), multiplied by \(D(t)\).

### Step 2. Apply the degreewise ascent identity

Suppose \(\ell(x)<\ell(sx)\). The [[node:kl.word.stalk_degree_exactness|exact-sequence theorem]] gives, for every \(n\),
\[
f_{s\mathbf t,x}(n)
=f_{\mathbf t,x}(n)+f_{\mathbf t,sx}(n-1).
\]
These three sequences have polynomial numerators
\(C_x^{s\mathbf t}\), \(C_x^{\mathbf t}\), and \(C_{sx}^{\mathbf t}\), with the common factor from Step 1.

The [[node:kl.algebra.hilbert_numerators|Hilbert-numerator shift theorem]] therefore gives
\(C_x^{s\mathbf t}=C_x^{\mathbf t}+qC_{sx}^{\mathbf t}\).

### Step 3. Apply the degreewise descent identity

Suppose \(\ell(sx)<\ell(x)\). The dimension identity is now
\[
f_{s\mathbf t,x}(n)
=f_{\mathbf t,sx}(n)+f_{\mathbf t,x}(n-1).
\]
Apply the same [[node:kl.algebra.hilbert_numerators|numerator theorem]], with the two tail roles exchanged. It gives
\(C_x^{s\mathbf t}=C_{sx}^{\mathbf t}+qC_x^{\mathbf t}\).

These are equalities in \(\mathbb Z[q]\): the [[node:kl.algebra.hilbert_numerators|numerator theorem]] first proves equality at every \(t\in(0,1)\), then recovers the polynomial coefficients. Simple multiplication changes length by one, so Steps 2–3 cover every \(x\).

### Step 4. Compute two equal letters

In the two-element Coxeter group \(1<s\), the empty-word values and the recurrence give
\[
C_1^s(q)=C_s^s(q)=1.
\]
Prepending \(s\) again gives
\[
C_1^{ss}(q)=1+q,\qquad C_s^{ss}(q)=1+q.
\]
Thus each stalk of the repeated word has two homogeneous generators, in degrees zero and one. This agrees with the explicit basis of its reflected pair lattice.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottStalkCharacter_ascent`: [IntegralPairings.lean:104](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L104).

`OAI.KLInvariance.TitsSpace.bottStalkCharacter_descent`: [IntegralPairings.lean:120](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L120).
