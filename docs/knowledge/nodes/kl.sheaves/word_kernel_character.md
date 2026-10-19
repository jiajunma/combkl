---
id: kl.duality.word_kernel_character
title: The outgoing-kernel character of a reduced word
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.word_section_pairing
- kl.detail.costalk_reciprocity
- kl.algebra.reflected_dual_character
- kl.detail.word_characters
- kl.duality.stalk_character
- kl.sheaves.word_polynomial_stalks
- kl.sheaves.cut_balance
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  declarations:
  - OAI.KLInvariance.TitsSpace.bottFreeSheaf
  - OAI.KLInvariance.TitsSpace.bottFreeDuality
  - OAI.KLInvariance.TitsSpace.bottKernelFree
  - OAI.KLInvariance.TitsSpace.bottKernelCharacter
  - OAI.KLInvariance.TitsSpace.bottStalkCharacter_natDegree_le
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:897
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottFreeSheaf
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:906
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottFreeDuality
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:910
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottKernelFree
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:915
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottKernelCharacter
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1088
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkCharacter_natDegree_le
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read bottFreeSheaf, bottFreeDuality, kernel freeness, reflected kernel
    character and the separate word natDegree bound. Checked the reduced-word length
    substitution, incoming-edge count and bundled full-kernel identification.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# The outgoing-kernel character of a reduced word

Fix a finite-generator Coxeter system, a finite real basis indexed by \(\sigma\) of its extended realization, and a reduced word \(\mathbf t\) with product \(b\). Let \(P=\mathbb R[X_i:i\in\sigma]\) be the polynomial coefficient algebra for this basis, and let \(S_{\mathbf t}\) be its word sheaf on \([1,b]\). For \(x\le b\), put
\[
K_x(S_{\mathbf t})
=\bigcap_{e:x\to y}\ker\rho^-_e,\qquad
d(x,b)=\ell(b)-\ell(x).
\]
This is the full outgoing kernel.

It is finite free over \(P\). Its character \(K_x^{\mathbf t}(q)\) and the stalk character satisfy
\[
K_x^{\mathbf t}(q)
=\operatorname{reflect}_{d(x,b)}C_x^{\mathbf t}(q),
\qquad
\operatorname{natDegree}C_x^{\mathbf t}\le d(x,b).
\]
Thus the kernel character also has the reciprocal expression
\(q^{d(x,b)}C_x^{\mathbf t}(q^{-1})\) in the Laurent polynomial ring.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate objects.**

**OpenAI notes:** The normalization discussion identifies indecomposable boundary-sheaf characters with KL polynomials by the cited character theorem. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The word-stalk character is proved to equal a positive Hecke-word coefficient. Its R-convolution is then proved before model decomposition and cancellation. The separate boundary-character identification is exposed as StalkCharacterObligation. [IntegralPairings:289](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L289), [CharacterReciprocity:1134](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1134), [SheafMorphisms:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219), [BottSamelson:1924](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1924), [BottSamelson:1945](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1945), [IntegralPairings:104](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L104), [IntegralPairings:120](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L120), [CharacterReciprocity:915](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L915).

**Role in the proof:** The word formula and R-convolution describe the tensor word. A common decomposition into boundary models then supplies the character identities used in the cancellation argument.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Specify the free-sheaf and duality data

The source packages the polynomial word sheaf as bottFreeSheaf. Its fields are the sheaf itself, free stalks, the root-labelled upper-quotient property, and global generation.

The [[node:kl.sheaves.word_section_pairing|reduced-word section pairing]] supplies a perfect pairing with shift
\(m=|\mathbf t|\) and both support-orthogonality equations. The [[node:kl.sheaves.cut_balance|cut-balance construction]] turns it into bottFreeDuality, the section-duality data for this free sheaf.

### Step 2. Identify the full kernel with the stalk dual

The stalk–costalk theorem gives a \(P\)-linear equivalence
\[
\Phi_x:(S_{\mathbf t}^x)^*\xrightarrow{\sim}K_x(S_{\mathbf t}),
\]
where the star denotes \(\operatorname{Hom}_P(-,P)\). The full kernel can be written either as bundled kernelData or as the kernel of the map taking all outgoing restrictions; their equivalence keeps the underlying vector.

Since the stalk is finite free, its dual is finite free. Transport through \(\Phi_x\) proves kernel freeness; finite generation also follows from this finite basis.

### Step 3. Calculate the duality degree

There are \(\ell(x)\) incoming reflection edges at \(x\) in \([1,b]\). The inverse stalk–costalk degree theorem sends a homogeneous functional of degree \(r\) to kernel degree
\[
r+m-\ell(x).
\]
Reducedness gives \(m=\ell(b)\), so this degree is \(r+d(x,b)\).

### Step 4. Reflect the character and bound its degree

Apply the [[node:kl.algebra.reflected_dual_character|homogeneous dual-character theorem]] with
\(M=S_{\mathbf t}^x\), \(N'=K_x(S_{\mathbf t})\), and \(D=d(x,b)\).
The source kernel grading is nonnegative, and Step 3 verifies the homogeneity hypothesis.

For stalk basis degrees \(d_i\), the transported dual basis has degrees \(D-d_i\ge0\). Hence \(d_i\le D\), the stalk character has degree at most \(D\), and
\[
K_x^{\mathbf t}(q)=\sum_iq^{D-d_i}
=\operatorname{reflect}_D C_x^{\mathbf t}(q).
\]
The polynomial word-sheaf stalk character is the defining bottStalkCharacter, so this is the source's bottKernelCharacter identity.

### Step 5. Read the reciprocal form

The proved degree bound allows the bounded reciprocal formula for polynomial reflection:
\[
\operatorname{reflect}_D C_x^{\mathbf t}(q)
=q^D C_x^{\mathbf t}(q^{-1}).
\]
Each exponent \(D-d_i\) is nonnegative, so this Laurent expression represents the ordinary kernel character polynomial.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottFreeSheaf`: [CharacterReciprocity.lean:897](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L897).

`OAI.KLInvariance.TitsSpace.bottFreeDuality`: [CharacterReciprocity.lean:906](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L906).

`OAI.KLInvariance.TitsSpace.bottKernelFree`: [CharacterReciprocity.lean:910](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L910).

`OAI.KLInvariance.TitsSpace.bottKernelCharacter`: [CharacterReciprocity.lean:915](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L915).

`OAI.KLInvariance.TitsSpace.bottStalkCharacter_natDegree_le`: [CharacterReciprocity.lean:1088](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1088).
