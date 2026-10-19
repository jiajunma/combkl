---
id: kl.duality.actual_character_reciprocity
title: R-reciprocity for the actual boundary-sheaf character
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.duality.bott_character_decomposition
- kl.duality.stalk_character
- kl.duality.boundary_kernel_character
- kl.duality.lower_character_convolution
- kl.notes.character_cancellation
- kl.detail.word_character_reciprocity
- kl.detail.ordinary_r
- kl.hecke.polynomial_reflection
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  - EdgeLocalization
  declarations:
  - OAI.KLInvariance.BruhatGraph.stalkCharacter_reciprocity
  - OAI.KLInvariance.BruhatGraph.stalkCharacter_natDegree_le
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:62
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.stalkCharacter_reciprocity
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:364
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.stalkCharacter_natDegree_le
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: 'Read the entire strong-induction proof in DyerPaths: top multiplicity,
    simultaneous substitutions, smaller-length hypotheses and ambient lower-character
    lifting. Kept the proof in integer polynomials until the separately justified
    reciprocal interpretation.'
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# R-reciprocity for the actual boundary-sheaf character

Fix a finite-generator Coxeter system and the polynomial coefficient algebra from a finite real basis of its extended realization. Let \(C_{x,b}(q)\) be the actual normalized boundary-stalk character on \(I_b=[1,b]\), and put \(d(x,b)=\ell(b)-\ell(x)\).

For every \(x\in I_b\),
\[
\operatorname{reflect}_{d(x,b)}C_{x,b}(q)
=\sum_{z\in I_b}R_{x,z}(q)C_{z,b}(q).
\]
The degree bound \(\operatorname{natDegree}C_{x,b}\le d(x,b)\) gives the equivalent Laurent expression
\[
q^{d(x,b)}C_{x,b}(q^{-1})
=\sum_{x\le z\le b}R_{x,z}(q)C_{z,b}(q).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate statement.**

**OpenAI notes:** The grading-normalization proposition identifies the stalk graded rank with the canonical KL polynomial and uses the Elias–Williamson character theorem through the cited moment-graph bridges. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The development defines the equality of actual stalk characters and canonical KL polynomials as StalkCharacterObligation. The unconditional theorem used in the main route is R-reciprocity for the actual character. The local strict half-degree implication retains an explicit nonzero-diagonal hypothesis. [SheafMorphisms:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219), [DyerPaths:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L62), [PositiveTransfer:186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L186), [CharacterReciprocity:1807](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1807), [TerminalKernels:1273](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1273), [TerminalKernels:1284](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1284).

**Role in the proof:** The comparison uses the actual character C and its proved R-reciprocity. Canonical P is handled by the later polynomial-rigidity induction. The local degree result applies to a diagonal coefficient satisfying its stated nonvanishing hypothesis.
<!-- source-comparison:end -->

*Proof.*

### Step 1. State the strong induction and its base

Induct strongly on \(\ell(b)\), proving the polynomial-reflection identity for every top of that length and every vertex below it.

If \(\ell(b)=0\), then \(b=1\) and the interval has one vertex. Its normalized character and diagonal R-polynomial are both \(1\), while \(\operatorname{reflect}_0(1)=1\). Thus the identity holds.

For the current \(b\), assume the result for every top \(c\) of strictly smaller length, at all vertices of \([1,c]\).

### Step 2. Write both decompositions with one multiplicity family

Choose a reduced word \(\mathbf t\) for \(b\). For \(c,z\in I_b\), let \(L_z^c\) be the lower-character function, zero when \(z\not\le c\). Put
\[
D_x^c=\operatorname{reflect}_{\delta(x,c)}L_x^c,
\qquad
\delta(x,c)=\max\{\ell(c)-\ell(x),0\}.
\]

The [[node:kl.duality.bott_character_decomposition|simultaneous word decomposition]] supplies polynomials \(\mu_c\) with
\[
C_z^{\mathbf t}=\sum_{c\in I_b}\mu_cL_z^c,\qquad
K_x^{\mathbf t}=\sum_{c\in I_b}\mu_cD_x^c.
\]
The second identity comes from transporting the full outgoing kernels through the same graded sheaf decomposition. Each \(\mu_c\) records the same shifts in both identities.

### Step 3. Compute the top multiplicity

Evaluate the first decomposition at \(z=b\). The reduced-word top character is \(1\). Lower-character normalization gives \(L_b^b=1\), and \(L_b^c=0\) for \(c\ne b\). Therefore
\[
1=C_b^{\mathbf t}=\mu_b.
\]

### Step 4. Substitute the word R-convolution

For the current reduced word, the [[node:kl.detail.word_character_reciprocity|word-character convolution]] gives
\[
K_x^{\mathbf t}=\sum_{z\in I_b}R_{x,z}C_z^{\mathbf t}.
\]
Substituting both decompositions yields
\[
\sum_c\mu_cD_x^c
=\sum_zR_{x,z}\left(\sum_c\mu_cL_z^c\right).
\]

### Step 5. Verify each proper-center identity

Let \(c\ne b\). Since \(c\le b\), strict Bruhat comparison gives
\(\ell(c)<\ell(b)\). The induction hypothesis supplies reciprocity on \([1,c]\).

The [[node:kl.duality.lower_character_convolution|lower-character convolution theorem]] then gives, for the current \(x\in I_b\),
\[
D_x^c=\sum_{z\in I_b}R_{x,z}L_z^c.
\]
Its proof includes both \(x\le c\) and \(x\not\le c\); in the latter case both sides are zero. Thus this identity is available for every proper center in the same ambient sum.

### Step 6. Cancel the proper-center defects

All sums are finite. Interchange the two sums in Step 4 and bring them to one side:
\[
0=\sum_{c\in I_b}\mu_c
\left(D_x^c-\sum_{z\in I_b}R_{x,z}L_z^c\right).
\]
Every summand with \(c\ne b\) vanishes by Step 5. The remaining coefficient is \(\mu_b=1\), so
\[
D_x^b=\sum_zR_{x,z}L_z^b.
\]
For the top center, \(L_z^b=C_{z,b}\) and
\(D_x^b=\operatorname{reflect}_{d(x,b)}C_{x,b}\).
This is the required induction conclusion. It is the source's [[node:kl.notes.character_cancellation|finite-character cancellation]] with distinguished index \(b\).

### Step 7. Interpret the reciprocal formula

Boundary kernel duality gives
\(\operatorname{natDegree}C_{x,b}\le d(x,b)\).
The [[node:kl.hecke.polynomial_reflection|bounded-reflection formula]] therefore identifies the left side with
\(q^{d(x,b)}C_{x,b}(q^{-1})\).

The R-polynomial vanishes unless \(x\le z\), so only \(x\le z\le b\) contribute. On the one-edge interval \([1,s]\), the lower-vertex identity is
\[
q=R_{1,1}+R_{1,s}=1+(q-1),
\]
matching the kernel character of the degree-one root ideal.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.stalkCharacter_reciprocity`: [DyerPaths.lean:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L62).

`OAI.KLInvariance.BruhatGraph.stalkCharacter_natDegree_le`: [EdgeLocalization.lean:364](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L364).
