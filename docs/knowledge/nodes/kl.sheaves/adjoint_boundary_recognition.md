---
id: kl.sheaves.adjoint_boundary_recognition
title: Recognition of the adjoint boundary image
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.boundary_recognition
- kl.sheaves.split_sheaf_properties
- kl.sheaves.primitive_image
- kl.detail.indecomposable_boundary
- kl.detail.adjoint_primitivity
- kl.sheaves.adjoint_fixed_stalk
- kl.word.top_stalk
- kl.detail.word_standard_stalks
- kl.detail.word_flabbiness
- kl.detail.top_splitting
- kl.notes.graded_projective_free
- kl.sheaves.word_boundary_summand
lean:
  repository: openai-kl
  modules:
  - BalancedPairings
  - CharacterReciprocity
  - Support
  declarations:
  - OAI.KLInvariance.TitsSpace.bottBoundarySheaf_splitIn
  - OAI.KLInvariance.TitsSpace.bottSplitAdjointSplit
  - OAI.KLInvariance.TitsSpace.bottSplitAdjoint_free
  - OAI.KLInvariance.TitsSpace.bottSplitAdjointTop_split
  - OAI.KLInvariance.TitsSpace.bottBoundarySplitAdjoint_primitive
  - OAI.KLInvariance.TitsSpace.bottBoundarySheaf_iso_adjoint
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:293
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottBoundarySheaf_splitIn
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1213
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSplitAdjointSplit
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1221
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSplitAdjoint_free
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1245
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSplitAdjointTop_split
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:2025
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottBoundarySplitAdjoint_primitive
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1258
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottBoundarySheaf_iso_adjoint
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the bilinear form, coefficient ring, finite coordinate presentation
    and lifting hypotheses explicit?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- duality_and_characters
---

# Recognition of the adjoint boundary image

Fix a reduced word \(\mathbf s\) with product \(b\), and work on the interval \([1,b]\) over the symmetric coefficient algebra of a finite-generator real extended realization. Let \(W\) be the graded word sheaf and \(B\) a normalized boundary sheaf with the same labels.

There exists a graded splitting \(i:B\to W,\ p:W\to B,\ pi=1_B\).
For any such splitting, put \(e=ip\), let \(e^*\) be the word-sheaf adjoint, and set
\[
C=\operatorname{im}e^*.
\]
Then \(C\) is graded isomorphic to \(B\).

*Proof.*

### Step 1. Supply the splitting from the normalized top

The [[node:kl.detail.word_standard_stalks|word-stalk theorem]] gives free stalks for \(W\), and its edge theorem gives the upper-quotient rule. [[node:kl.detail.word_flabbiness|Word flabbiness]] and the section construction give flabbiness and global generation.

The [[node:kl.word.top_stalk|reduced-word top-stalk theorem]] identifies \(W^b\) with the degree-zero unit module \(A\). The boundary normalization identifies \(B^b\) with the same module. Composing these identifications gives inverse degree-zero maps
\[
a_0:B^b\to W^b,\qquad b_0:W^b\to B^b.
\]
The interval is finite with greatest vertex \(b\), and the symmetric coefficient algebra is a connected graded Noetherian domain. The [[node:kl.detail.top_splitting|top-splitting theorem]] therefore supplies a splitting of \(B\) into \(W\).

The [[node:kl.sheaves.word_boundary_summand|word-boundary summand theorem]] records this application with all its ring, graph and sheaf hypotheses.

Fix any splitting \(i,p\) for the remaining steps.

### Step 2. Form the adjoint image and its actual split maps

The word adjoint is a graded sheaf endomorphism, and the adjoint of an idempotent is idempotent. Thus \(e^*\) is a graded sheaf projector.

Its image sheaf has the component images as stalks and edge modules. Let
\[
j:C\to W,\qquad q:W\to C
\]
be its inclusion and projection. They satisfy \(qj=1_C\) and \(jq=e^*\).

### Step 3. Transfer the sheaf properties to C

The [[node:kl.sheaves.split_sheaf_properties|split-summand theorem]] transfers the upper-quotient rule, flabbiness, and global generation from \(W\) to \(C\). Each stalk of \(C\) is a graded direct summand of a finite free stalk of \(W\), hence projective.

The coefficient algebra is connected, nonnegative, Noetherian, and a domain. The [[node:kl.notes.graded_projective_free|graded projective-to-free theorem]] therefore makes every stalk of \(C\) free. These are the sheaf properties needed by boundary recognition.

### Step 4. Prove the identity of C is primitive

The normalized boundary sheaf \(B\) has primitive identity by the [[node:kl.detail.indecomposable_boundary|indecomposability theorem]]. Transferring primitivity through the splitting \(i,p\) makes \(e=ip\) primitive.

The adjoint reverses composition, is involutive, and preserves zero. The [[node:kl.detail.adjoint_primitivity|adjoint-primitivity theorem]] therefore makes \(e^*\) primitive. Transferring primitivity to its image makes \(1_C\) primitive.

### Step 5. Split the normalized top into C

The [[node:kl.sheaves.adjoint_fixed_stalk|fixed-stalk theorem]] gives \(e_b^*=1_{W^b}\). Use the normalized top identifications \(a_0,b_0\) from Step 1, and define
\[
a=q_ba_0:B^b\to C^b,\qquad
c=b_0j_b:C^b\to B^b.
\]
Then
\[
ca=b_0j_bq_ba_0=b_0e_b^*a_0=b_0a_0=1_{B^b}.
\]
All these maps preserve degree.

### Step 6. Apply boundary recognition

The finite interval, coefficient algebra, quotient rule, free stalks, flabbiness, generation, primitive identity, and top splitting have all been supplied in Steps 1–5.

The [[node:kl.sheaves.boundary_recognition|boundary-recognition theorem]] now gives a graded isomorphism \(B\simeq C\). This recognition is the input for proving that the particular canonical comparison map is an isomorphism.

## References

The source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottBoundarySheaf_splitIn`: [Support.lean:293](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L293).

`OAI.KLInvariance.TitsSpace.bottSplitAdjointSplit`: [CharacterReciprocity.lean:1213](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1213).

`OAI.KLInvariance.TitsSpace.bottSplitAdjoint_free`: [CharacterReciprocity.lean:1221](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1221).

`OAI.KLInvariance.TitsSpace.bottSplitAdjointTop_split`: [CharacterReciprocity.lean:1245](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1245).

`OAI.KLInvariance.TitsSpace.bottBoundarySplitAdjoint_primitive`: [BalancedPairings.lean:2025](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L2025).

`OAI.KLInvariance.TitsSpace.bottBoundarySheaf_iso_adjoint`: [CharacterReciprocity.lean:1258](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1258).
