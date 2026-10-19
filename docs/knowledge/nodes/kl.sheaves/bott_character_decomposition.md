---
id: kl.duality.bott_character_decomposition
title: Simultaneous decomposition of Bott–Samelson stalk and kernel characters
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.model_sum_characters
- kl.sheaves.lower_model_kernels
- kl.detail.word_flabbiness
- kl.detail.word_standard_stalks
- kl.detail.word_characters
- kl.word.top_stalk
- kl.detail.costalk_duality
- kl.notes.tensor_pairing
- kl.word.support_duality
- kl.word.pairing_degree
- kl.duality.word_kernel_character
- kl.duality.boundary_kernel_character
- kl.duality.lower_character_convolution
- kl.sheaves.word_section_pairing
- kl.detail.model_decomposition
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  declarations:
  - OAI.KLInvariance.TitsSpace.bottCharacter_decomposition_both
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:2019
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCharacter_decomposition_both
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- background
---

# Simultaneous decomposition of Bott–Samelson stalk and kernel characters

Fix a reduced word \(\mathbf s\) with product \(b\) in a finite-generator Coxeter system. Choose a real basis of the extended realization and use the corresponding polynomial coefficient algebra, with root labels in degree one. There exist polynomials \(\mu_y(q)\in\mathbb Z[q]\), \(y\in[1,b]\), with nonnegative coefficients, such that for every \(x\in[1,b]\),
\[
C_x^{\mathbf s}(q)
=\sum_{x\le y\le b}\mu_y(q)C_{x,y}(q),
\]
\[
K_x^{\mathbf s}(q)
=\sum_{x\le y\le b}\mu_y(q)\,
 q^{\ell(y)-\ell(x)}C_{x,y}(q^{-1}).
\]
Here \(C_x^{\mathbf s}\) is the word-stalk character and \(K_x^{\mathbf s}\) the full outgoing-kernel character of its word sheaf. Moreover \(\mu_b(q)=1\).

*Proof.*

### Step 1. Check the word-sheaf and model inputs

The polynomial-coordinate word sheaf has free stalks and the upper-quotient rule by the word-stalk and edge-kernel theorems. Its word sections generate each stalk, and the reduced-word flabbiness theorem gives flabbiness.

The [[node:kl.sheaves.word_section_pairing|word section pairing]] is perfect and support-orthogonal, so it supplies section duality. Together with the free-stalk, quotient, and generation data, the costalk theorem identifies each full outgoing kernel with the dual of its finite free stalk. This proves the required kernel freeness. The actual lower-supported boundary models have free stalks by construction and free full outgoing kernels by the [[node:kl.sheaves.lower_model_kernels|lower-model kernel theorem]]. All coefficients, labels, and graph vertices are those of the common finite interval \([1,b]\).

### Step 2. Decompose the sheaf and record its shifts

Apply the [[node:kl.detail.model_decomposition|model-decomposition theorem]] to obtain a graded sheaf isomorphism
\[
B^{\mathbf s}\simeq\bigoplus_{y,j}O_y(d_{y,j}),
\qquad d_{y,j}\in\mathbb N.
\]
Define
\[
\mu_y(q)=\sum_jq^{d_{y,j}}.
\]
The sums are finite, and every coefficient counts occurrences of a nonnegative shift.

### Step 3. Substitute the model stalk characters

The [[node:kl.sheaves.model_sum_characters|simultaneous model-character theorem]] gives
\[
C_x^{\mathbf s}(q)=\sum_y\mu_y(q)C_{O_y}(x;q).
\]
For \(x\le y\), the model stalk is the actual boundary stalk on \([1,y]\), with character \(C_{x,y}\). For \(x\not\le y\), the model stalk is zero. Removing those zero terms yields the first displayed formula.

### Step 4. Substitute the model kernel characters

The same theorem and the same shifts give
\[
K_x^{\mathbf s}(q)=\sum_y\mu_y(q)K_{O_y}(x;q).
\]
For \(x\le y\), the [[node:kl.sheaves.lower_model_kernels|lower-model kernel theorem]] identifies the term as
\(q^{\ell(y)-\ell(x)}C_{x,y}(q^{-1})\).
For the other centers it is zero. This gives the second formula.

Each reflected expression is a polynomial because its exponents are the nonnegative degrees of the model's kernel basis.

### Step 5. Determine the top multiplicity

The reduced-word top-stalk theorem gives \(C_b^{\mathbf s}=1\). Among centers \(y\le b\), the support condition permits a nonzero stalk at \(b\) only when \(b\le y\), hence only when \(y=b\). That model has normalized top character \(C_{b,b}=1\).

The first formula at \(x=b\) therefore gives
\[
1=\mu_b(q)\cdot1.
\]
Thus \(\mu_b=1\), the coefficient used when lower-center terms are cancelled in actual-character reciprocity.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottCharacter_decomposition_both`: [CharacterReciprocity.lean:2019](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L2019).
