---
id: kl.duality.boundary_kernel_character
title: Boundary kernel characters and their degree bound
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.boundary_pairing
- kl.detail.costalk_reciprocity
- kl.algebra.reflected_dual_character
- kl.duality.stalk_character
- kl.sheaves.cut_balance
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  - EdgeLocalization
  declarations:
  - OAI.KLInvariance.BruhatGraph.boundaryFreeSheaf
  - OAI.KLInvariance.BruhatGraph.boundaryPerfectPairing
  - OAI.KLInvariance.BruhatGraph.boundaryFreeDuality
  - OAI.KLInvariance.BruhatGraph.boundaryKernelFree
  - OAI.KLInvariance.BruhatGraph.costalkCharacter
  - OAI.KLInvariance.BruhatGraph.costalkCharacter_reflect
  - OAI.KLInvariance.BruhatGraph.stalkBasis_degree_le
  - OAI.KLInvariance.BruhatGraph.stalkCharacter_natDegree_le
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1786
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.boundaryFreeSheaf
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1792
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.boundaryPerfectPairing
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1796
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.boundaryFreeDuality
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1799
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.boundaryKernelFree
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1804
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.costalkCharacter
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1807
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.costalkCharacter_reflect
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1815
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.stalkBasis_degree_le
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:364
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.stalkCharacter_natDegree_le
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read the actual boundary FreeSheaf/perfect-pairing/duality packages, kernel
    character and basis-degree/natDegree bounds. Kept the exact nonnegative degree
    bound and full outgoing-kernel meaning.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Boundary kernel characters and their degree bound

Fix a finite-generator Coxeter system and the polynomial coefficient algebra from a finite basis of its extended realization. Let \(B(b)\) be the actual normalized boundary sheaf on \([1,b]\), and, for \(x\in[1,b]\), let
\[
C_{x,b}(q)=\operatorname{ch}(B(b)^x;q),\qquad d(x,b)=\ell(b)-\ell(x).
\]

Every full outgoing kernel \(K_x(B(b))\) is finite free. Its character, named costalkCharacter in the source, satisfies
\[
K_{x,b}(q)=\operatorname{reflect}_{d(x,b)}C_{x,b}(q).
\]
Every nonnegative homogeneous stalk-basis degree is at most \(d(x,b)\); consequently
\[
\operatorname{natDegree}C_{x,b}\le d(x,b).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate statement.**

**OpenAI notes:** The grading-normalization proposition identifies the stalk graded rank with the canonical KL polynomial and uses the Elias–Williamson character theorem through the cited moment-graph bridges. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The development defines the equality of actual stalk characters and canonical KL polynomials as StalkCharacterObligation. The unconditional theorem used in the main route is R-reciprocity for the actual character. The local strict half-degree implication retains an explicit nonzero-diagonal hypothesis. [SheafMorphisms:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219), [DyerPaths:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L62), [PositiveTransfer:186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L186), [CharacterReciprocity:1807](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1807), [TerminalKernels:1273](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1273), [TerminalKernels:1284](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1284).

**Role in the proof:** The comparison uses the actual character C and its proved R-reciprocity. Canonical P is handled by the later polynomial-rigidity induction. The local degree result applies to a diagonal coefficient satisfying its stated nonvanishing hypothesis.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Use the constructed boundary pairing

The [[node:kl.detail.boundary_pairing|boundary-pairing theorem]] supplies a perfect graded section pairing of shift \(\ell(b)\), with both support-orthogonality conditions.

The source's boundaryFreeSheaf packages the chosen boundary sheaf, its free stalks, upper root quotients and global generation. Applying the [[node:kl.sheaves.cut_balance|cut-balance construction]] to the pairing gives boundaryFreeDuality.

### Step 2. Obtain the full-kernel dual equivalence

Stalk–costalk duality yields
\[
\Phi_x:(B(b)^x)^*\xrightarrow{\sim}K_x(B(b)).
\]
The dual of a finite free stalk has its finite dual basis, so the kernel is finite free. This supplies boundaryKernelFree and makes its character well defined.

For a homogeneous functional of degree \(r\), the inverse-duality degree theorem gives
\[
\Phi_x(\lambda)\in K_x(B(b))_{r+\ell(b)-\ell(x)}.
\]
The incoming-edge count is \(\ell(x)\), and \(x\le b\) makes this difference nonnegative.

### Step 3. Construct the kernel basis from any stalk basis

Let \(b_i\) be a finite nonnegative homogeneous stalk basis of degrees \(d_i\). Its dual basis has degrees \(-d_i\). Step 2 therefore puts the kernel basis
\(\Phi_x(b_i^*)\) in degrees
\[
d(x,b)-d_i.
\]
These vectors are nonzero, since \(\Phi_x\) is an isomorphism and each dual basis functional takes value \(1\) on its corresponding basis vector.

The kernel has a nonnegative grading. Thus every \(d(x,b)-d_i\) is nonnegative, giving \(d_i\le d(x,b)\).

### Step 4. Compute both character assertions

The [[node:kl.algebra.reflected_dual_character|homogeneous dual-character theorem]] now gives
\[
K_{x,b}(q)=\sum_iq^{d(x,b)-d_i}
=\operatorname{reflect}_{d(x,b)}C_{x,b}(q).
\]
Since \(C_{x,b}(q)=\sum_iq^{d_i}\) and every \(d_i\le d(x,b)\), its natural degree is at most \(d(x,b)\). The zero-basis case gives the zero polynomial, whose natural degree is zero.

This is the source's costalkCharacter_reflect formula, together with stalkBasis_degree_le and stalkCharacter_natDegree_le. It also makes
\(q^{d(x,b)}C_{x,b}(q^{-1})\) an ordinary polynomial.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.boundaryFreeSheaf`: [CharacterReciprocity.lean:1786](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1786).

`OAI.KLInvariance.BruhatGraph.boundaryPerfectPairing`: [CharacterReciprocity.lean:1792](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1792).

`OAI.KLInvariance.BruhatGraph.boundaryFreeDuality`: [CharacterReciprocity.lean:1796](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1796).

`OAI.KLInvariance.BruhatGraph.boundaryKernelFree`: [CharacterReciprocity.lean:1799](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1799).

`OAI.KLInvariance.BruhatGraph.costalkCharacter`: [CharacterReciprocity.lean:1804](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1804).

`OAI.KLInvariance.BruhatGraph.costalkCharacter_reflect`: [CharacterReciprocity.lean:1807](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1807).

`OAI.KLInvariance.BruhatGraph.stalkBasis_degree_le`: [CharacterReciprocity.lean:1815](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1815).

`OAI.KLInvariance.BruhatGraph.stalkCharacter_natDegree_le`: [EdgeLocalization.lean:364](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L364).
