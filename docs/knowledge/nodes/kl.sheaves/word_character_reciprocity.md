---
id: kl.detail.word_character_reciprocity
title: Polynomial R-convolution for word-stalk and kernel characters
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.word_character_formula
- kl.duality.word_kernel_character
- kl.hecke.positive_word_reciprocity
- kl.hecke.ordinary_r_construction
- kl.hecke.polynomial_reflection
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  declarations:
  - OAI.KLInvariance.TitsSpace.bottStalkCharacter_natDegree_le
  - OAI.KLInvariance.TitsSpace.bottStalkCharacter_reciprocity
  - OAI.KLInvariance.TitsSpace.bottKernelCharacter_rConvolution
  - OAI.KLInvariance.HeckeQ.positiveWord_rValue
  - OAI.KLInvariance.HeckeQ.eval_positiveWord
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1088
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkCharacter_natDegree_le
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1105
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkCharacter_reciprocity
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1134
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottKernelCharacter_rConvolution
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:997
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.positiveWord_rValue
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1027
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.eval_positiveWord
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read the Laurent embedding/evaluation comparison, positiveWord_rValue specialization,
    exponent calculation, bounded reflection, injectivity and final lowerFinset-to-interval
    reindexing. Made the actual kernel character the separate geometric input.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Polynomial R-convolution for word-stalk and kernel characters

Fix a finite-generator Coxeter system, a finite basis of its extended realization, and a reduced word \(\mathbf t\) with product \(b\). Put \(I_b=[1,b]\). For \(x\in I_b\), let \(d=\ell(b)-\ell(x)\). Let \(C_x^{\mathbf t}\) be the character of the polynomial word-sheaf stalk at \(x\), and \(K_x^{\mathbf t}\) the character of its full outgoing kernel, the intersection of all outgoing restriction kernels. Then
\[
\operatorname{reflect}_d C_x^{\mathbf t}(q)
=\sum_{z\in I_b}R_{x,z}(q)C_z^{\mathbf t}(q)
=K_x^{\mathbf t}(q).
\]
These are identities in \(\mathbb Z[q]\). The degree bound
\(\operatorname{natDegree}C_x^{\mathbf t}\le d\) makes the left polynomial equal to
\(q^d C_x^{\mathbf t}(q^{-1})\) in the Laurent polynomial ring.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate objects.**

**OpenAI notes:** The normalization discussion identifies indecomposable boundary-sheaf characters with KL polynomials by the cited character theorem. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The word-stalk character is proved to equal a positive Hecke-word coefficient. Its R-convolution is then proved before model decomposition and cancellation. The separate boundary-character identification is exposed as StalkCharacterObligation. [IntegralPairings:289](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L289), [CharacterReciprocity:1134](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1134), [SheafMorphisms:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219), [BottSamelson:1924](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1924), [BottSamelson:1945](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1945), [IntegralPairings:104](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L104), [IntegralPairings:120](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L120), [CharacterReciprocity:915](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L915).

**Role in the proof:** The word formula and R-convolution describe the tensor word. A common decomposition into boundary models then supplies the character identities used in the cancellation argument.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Work at the formal Laurent unit

Let \(\Lambda=\mathbb Z[q,q^{-1}]\), and let \(u\in\Lambda^\times\) be its distinguished variable unit. The embedding
\[
j:\mathbb Z[q]\hookrightarrow\Lambda
\]
sends a polynomial \(F\) to \(F(u)\). Indeed, both descriptions send a monomial \(a q^n\) to \(a u^n\), and preserve finite sums.

The [[node:kl.hecke.positive_word_reciprocity|positive Hecke-word reciprocity theorem]] applies to this unit. Writing
\(m=|\mathbf t|\), it gives
\[
\sum_{z\le b}R_{x,z}(u)\,h_{\mathbf t}(z;u)
=u^{-\ell(x)}u^m h_{\mathbf t}(x;u^{-1}).
\]
Reducedness is the support hypothesis that makes this a sum over the finite lower interval of \(b\).

### Step 2. Substitute the word-character coefficients

The [[node:kl.detail.word_character_formula|word-character theorem]] identifies the positive-word coefficient polynomials with \(C_z^{\mathbf t}\). Evaluation commutes with the positive-word recursion because it preserves addition, multiplication and integer coefficients. Therefore
\[
h_{\mathbf t}(z;u)=C_z^{\mathbf t}(u),\qquad
h_{\mathbf t}(x;u^{-1})=C_x^{\mathbf t}(u^{-1}).
\]
The ordinary R-polynomial evaluation theorem identifies the R-values in the Hecke identity with the displayed \(R_{x,z}(u)\).

Reducedness gives \(m=\ell(b)\). Since \(x\le b\), \(\ell(x)\le m\), and the unit powers simplify to
\[
u^{-\ell(x)}u^m=u^{m-\ell(x)}=u^d.
\]

### Step 3. Recognize the reflected polynomial

The [[node:kl.duality.word_kernel_character|outgoing-kernel character theorem]] supplies
\(\operatorname{natDegree}C_x^{\mathbf t}\le d\).
Hence [[node:kl.hecke.polynomial_reflection|bounded polynomial reflection]] gives
\[
u^d C_x^{\mathbf t}(u^{-1})
=j(\operatorname{reflect}_d C_x^{\mathbf t}).
\]
The finite sum on the other side is
\[
j\left(\sum_{z\le b}R_{x,z}C_z^{\mathbf t}\right),
\]
because \(j\) is a ring homomorphism.

### Step 4. Return to integer polynomials and interval vertices

Injectivity of \(j\) proves
\[
\operatorname{reflect}_d C_x^{\mathbf t}
=\sum_{z\le b}R_{x,z}C_z^{\mathbf t}
\]
in \(\mathbb Z[q]\).

Every group element below \(b\) lies above \(1\). Thus \(z\mapsto\langle z,1\le z,z\le b\rangle\) identifies this finite index set with \(I_b\), giving the stated sum over interval vertices.

### Step 5. Insert the actual kernel character

The [[node:kl.duality.word_kernel_character|kernel-character theorem]] gives
\(K_x^{\mathbf t}=\operatorname{reflect}_d C_x^{\mathbf t}\).
Substituting into Step 4 proves the full R-convolution identity.

For one letter \(s\), the two stalk characters are \(1\). At the lower vertex, the sum is
\(R_{1,1}+R_{1,s}=1+(q-1)=q\), which is the character of the kernel \(\alpha_s A\). At the top vertex, the sum and the kernel character are both \(1\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottStalkCharacter_natDegree_le`: [CharacterReciprocity.lean:1088](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1088).

`OAI.KLInvariance.TitsSpace.bottStalkCharacter_reciprocity`: [CharacterReciprocity.lean:1105](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1105).

`OAI.KLInvariance.TitsSpace.bottKernelCharacter_rConvolution`: [CharacterReciprocity.lean:1134](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1134).

`OAI.KLInvariance.HeckeQ.positiveWord_rValue`: [CharacterReciprocity.lean:997](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L997).

`OAI.KLInvariance.HeckeQ.eval_positiveWord`: [CharacterReciprocity.lean:1027](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1027).
