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
- kl.detail.word_standard_stalks
- kl.detail.hilbert_exactness
- kl.sheaves.hilbert_free
- kl.notes.graded_projective_free
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.bottHeadKernelEquiv
  - OAI.KLInvariance.TitsSpace.bottHeadRightKernelEquiv
  - OAI.KLInvariance.TitsSpace.bottStalkCharacter_ascent
  - OAI.KLInvariance.TitsSpace.bottStalkCharacter_descent
  - OAI.KLInvariance.TitsSpace.bottStalkCharacter_eq_heckeWord
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1578
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadKernelEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:2045
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadRightKernelEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:104
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkCharacter_ascent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:120
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkCharacter_descent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:289
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkCharacter_eq_heckeWord
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# Word-stalk characters equal positive Hecke-word coefficients

For every word \(\mathbf s\) and every \(x\in W\), the actual word-stalk character is the coefficient of \(T_x\) in the positive Hecke word:
\[
C^{\mathbf s}_x(q)=[T_x]\prod_{s\text{ in }\mathbf s}(1+T_s).
\]
The product follows the written word order. Reducedness is not assumed.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate objects.**

**OpenAI notes:** The normalization discussion identifies indecomposable boundary-sheaf characters with KL polynomials by the cited character theorem. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The word-stalk character is proved to equal a positive Hecke-word coefficient. Its R-convolution is then proved before model decomposition and cancellation. The separate boundary-character identification is exposed as StalkCharacterObligation. [IntegralPairings:289](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L289), [CharacterReciprocity:1134](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1134), [SheafMorphisms:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219).

**Role in the proof:** The word formula and R-convolution describe the tensor word. A common decomposition into boundary models then supplies the character identities used in the cancellation argument.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Specify the two projections after adding a letter

Write the new word as \(s\mathbf t\). As in the free-stalk proof, its stalk at \(x\) is the two-stalk lattice in \(B^{\mathbf t}_x\oplus(B^{\mathbf t}_{sx})^\tau\). The first coordinate gives a surjective homogeneous map to \(B^{\mathbf t}_x\). The second gives a surjective homogeneous real-linear map to \(B^{\mathbf t}_{sx}\), after undoing the scalar twist. Surjectivity follows by projecting the old word elements in the defining pair lattice. The coefficient action \(\tau\) preserves polynomial degree, so undoing the twist preserves the real homogeneous pieces.

### Step 2. Identify the kernels with their exact degree shift

If \(x<s x\), the first projection has kernel \((0,\alpha y)\) with \(y\in(B^{\mathbf t}_{sx})^\tau\), by the proved edge-kernel equality. In new stalk coordinates the injection has zero zero-bit coordinates and one-bit coordinates \(\tau(\alpha y)\). It is injective because \(\alpha\ne0\) acts injectively on a stalk image, and surjective onto the kernel by that equality. Multiplication by the degree-one label raises degree by one; \(\tau\) preserves degree. Conversely, if the product has degree \(n\), decompose \(y\) into homogeneous pieces. Injectivity of multiplication by \(\alpha\) forces every piece except degree \(n-1\) to vanish.

If \(sx<x\), use the second projection. Its kernel is \((\alpha y,0)\) with \(y\in B^{\mathbf t}_x\); the same injectivity and degree argument applies. Thus degreewise exactness gives
\[
\dim(B^{s\mathbf t}_x)_n=
\begin{cases}
\dim(B^{\mathbf t}_x)_n+\dim(B^{\mathbf t}_{sx})_{n-1},&x<s x,\\
\dim(B^{\mathbf t}_{sx})_n+\dim(B^{\mathbf t}_x)_{n-1},&sx<x.
\end{cases}
\]
These are exact identities of finite-dimensional real vector spaces; no assertion about KL polynomials enters.

### Step 3. Pass from dimensions to character polynomials

Word stalks are finite graded free, so their convergent Hilbert series have the common denominator \((1-q)^N\). Multiply the dimension identities by \(q^n\) and sum. Reindexing the shifted term by \(n-1\) contributes a factor \(q\). For every \(0<q<1\), cancellation of the nonzero common denominator gives
\[
C^{s\mathbf t}_x=
\begin{cases}
C^{\mathbf t}_x+qC^{\mathbf t}_{sx},&x<s x,\\
C^{\mathbf t}_{sx}+qC^{\mathbf t}_x,&sx<x.
\end{cases}
\]
An equality at all real parameters in \((0,1)\) is a polynomial equality, since a nonzero real polynomial has only finitely many roots. Injectivity of the coefficient map from integers to reals returns the equality in \(\mathbb Z[q]\).

### Step 4. Match the Hecke recursion and its initial value

For a coefficient vector \(v\), the unnormalized left Hecke operator satisfies
\[
[(1+T_s)v]_x=
\begin{cases}
v_x+qv_{sx},&x<s x,\\
v_{sx}+qv_x,&sx<x.
\end{cases}
\]
This follows by applying the operator to standard basis vectors and collecting the contributions to \(x\); the descent coefficient \(q-1\) becomes \(q\) after adding \(v\).

The empty word has stalk \(A\) at \(1\) and zero stalks elsewhere. Its character vector is therefore the coefficient vector of \(T_1\). Induct on the word length: Step 3 and the displayed Hecke recursion apply the same rule to equal tail vectors, giving equality for the longer word. This proves the formula for all words.

The theorem concerns tensor-word characters. The passage to boundary-sheaf characters uses the separate model decomposition and cancellation results; it does not assert the conditional boundary-character identification with KL polynomials.

## References

The precise Lean sources are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottHeadKernelEquiv`: [BottSamelson.lean:1578](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1578).

`OAI.KLInvariance.TitsSpace.bottHeadRightKernelEquiv`: [BottSamelson.lean:2045](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L2045).

`OAI.KLInvariance.TitsSpace.bottStalkCharacter_ascent`: [IntegralPairings.lean:104](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L104).

`OAI.KLInvariance.TitsSpace.bottStalkCharacter_descent`: [IntegralPairings.lean:120](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L120).

`OAI.KLInvariance.TitsSpace.bottStalkCharacter_eq_heckeWord`: [IntegralPairings.lean:289](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L289).
