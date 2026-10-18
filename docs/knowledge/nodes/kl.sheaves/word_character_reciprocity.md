---
id: kl.detail.word_character_reciprocity
title: Bar reciprocity and R-convolution for word characters
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.word_character_formula
- kl.definitions.bar_involution
- kl.detail.ordinary_r
- kl.detail.costalk_reciprocity
- kl.notes.tensor_pairing
- kl.detail.root_inversion_count
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  declarations:
  - OAI.KLInvariance.HeckeQ.barLinear_positiveWord
  - OAI.KLInvariance.HeckeQ.positiveWord_rValue
  - OAI.KLInvariance.TitsSpace.bottStalkCharacter_reciprocity
  - OAI.KLInvariance.TitsSpace.bottKernelCharacter_rConvolution
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:951
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.barLinear_positiveWord
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:997
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.positiveWord_rValue
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1105
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkCharacter_reciprocity
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1134
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottKernelCharacter_rConvolution
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

# Bar reciprocity and R-convolution for word characters

Let \(\mathbf s\) be a reduced word with product \(b\) and length \(m=\ell(b)\), and let \(x\le b\). Its stalk character and full outgoing-kernel character satisfy
\[
q^{m-\ell(x)}C^{\mathbf s}_x(q^{-1})
=\sum_{z\le b}R_{x,z}(q)C^{\mathbf s}_z(q)
=K^{\mathbf s}_x(q).
\]
The left side is a polynomial: the word-stalk duality gives the degree bound \(\deg C^{\mathbf s}_x\le m-\ell(x)\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate objects.**

**OpenAI notes:** The normalization discussion identifies indecomposable boundary-sheaf characters with KL polynomials by the cited character theorem. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The word-stalk character is proved to equal a positive Hecke-word coefficient. Its R-convolution is then proved before model decomposition and cancellation. The separate boundary-character identification is exposed as StalkCharacterObligation. [IntegralPairings:289](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L289), [CharacterReciprocity:1134](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1134), [SheafMorphisms:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219).

**Role in the proof:** The word formula and R-convolution describe the tensor word. A common decomposition into boundary models then supplies the character identities used in the cancellation argument.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Compute the bar of a positive generator

For an invertible parameter \(q\), the unnormalized quadratic relation gives
\[
T_s^{-1}=q^{-1}(T_s-(q-1)),\qquad
1+T_s^{-1}=q^{-1}(1+T_s).
\]
In the source's linear-bar notation, let \(B_q\) be the map relating parameter \(q^{-1}\) to parameter \(q\). Its intertwining identity and the displayed calculation give, by induction on the word,
\[
B_q(H_{\mathbf s}(q^{-1}))=q^{-m}H_{\mathbf s}(q).
\]
The empty word is fixed. Each new letter contributes one additional factor \(q^{-1}\) by the formula for \(1+T_s^{-1}\). Replacing \(q\) by \(q^{-1}\) gives
\(B_{q^{-1}}(H_{\mathbf s}(q))=q^mH_{\mathbf s}(q^{-1})\).

### Step 2. Extract the coefficient at x

The ordinary R-family is normalized so that the coefficient of \(T_x\) in \(B_{q^{-1}}(T_z)\) is \(q^{\ell(x)}R_{x,z}(q)\). Expand \(H_{\mathbf s}(q)\) in the standard basis and take its \(x\)-coefficient in the last bar identity. This gives
\[
q^{\ell(x)}\sum_{z\le b}R_{x,z}(q)[T_z]H_{\mathbf s}(q)
=q^m[T_x]H_{\mathbf s}(q^{-1}).
\]
The sum is over the finite lower ideal of \(b\). Its sufficiency follows inductively from the Hecke coefficient recursion and monotonicity of the upper simple envelope: prepending a reduced letter sends the support below the new word product.

Cancel the invertible \(q^{\ell(x)}\) and substitute the word-character formula. This proves the stalk identity in the Laurent polynomial ring.

### Step 3. Check the degree bound and identify the kernel character

The constructed word pairing has degree shift \(m\), and its balanced support duality identifies the full outgoing kernel with the dual of the stalk, with the incoming-label shift. At \(x\), there are exactly \(\ell(x)\) incoming labels by the inversion count. If a homogeneous stalk basis has degrees \(d_i\), the resulting outgoing-kernel basis has degrees
\[
m-\ell(x)-d_i.
\]
These must be nonnegative, since the kernel is a homogeneous submodule of a nonnegatively graded module. Therefore \(d_i\le m-\ell(x)\), establishing the asserted degree bound.

Its character is consequently
\[
\sum_iq^{m-\ell(x)-d_i}
=q^{m-\ell(x)}\sum_i(q^{-1})^{d_i}
=q^{m-\ell(x)}C^{\mathbf s}_x(q^{-1}).
\]
The stalk–costalk reciprocity proof supplies the dual-basis construction and the incoming-label product; the tensor pairing supplies the word's perfect form.

### Step 4. Return to ordinary polynomials

Step 3 shows that the Laurent expression on the left of Step 2 has no negative powers. Both sides are images of ordinary integer polynomials, and the embedding into Laurent polynomials is injective. Hence their equality holds in \(\mathbb Z[q]\). Substituting the kernel character computed in Step 3 gives the full convolution identity.

This is the word-object convolution used before cancelling lower boundary-model summands. It supplies an unconditional intermediate theorem without inserting the boundary-character identification condition.

## References

The precise Lean sources are listed below.

## Lean formalization

`OAI.KLInvariance.HeckeQ.barLinear_positiveWord`: [CharacterReciprocity.lean:951](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L951).

`OAI.KLInvariance.HeckeQ.positiveWord_rValue`: [CharacterReciprocity.lean:997](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L997).

`OAI.KLInvariance.TitsSpace.bottStalkCharacter_reciprocity`: [CharacterReciprocity.lean:1105](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1105).

`OAI.KLInvariance.TitsSpace.bottKernelCharacter_rConvolution`: [CharacterReciprocity.lean:1134](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1134).
