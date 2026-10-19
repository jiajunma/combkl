---
id: kl.sheaves.kernel_transport
title: Outgoing kernels under sheaf isomorphisms, sums, and shifts
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.sheaf_isomorphisms
- kl.sheaves.finite_operations
- kl.sheaves.upward_kernel
- kl.detail.graded_character
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.Iso.kernelEquiv
  - OAI.KLInvariance.MomentGraph.GradedSheaf.Iso.kernelEquiv_graded
  - OAI.KLInvariance.MomentGraph.GradedSheaf.kernelShiftEquiv
  - OAI.KLInvariance.MomentGraph.GradedSheaf.kernelProdEquiv
  - OAI.KLInvariance.MomentGraph.GradedSheaf.kernelPiEquiv
  - OAI.KLInvariance.MomentGraph.GradedSheaf.kernelChar_shift
  - OAI.KLInvariance.MomentGraph.GradedSheaf.kernelChar_prod
  - OAI.KLInvariance.MomentGraph.GradedSheaf.kernelChar_pi
  - OAI.KLInvariance.MomentGraph.GradedSheaf.kernelChar_zero
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:615
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.Iso.kernelEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:624
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.Iso.kernelEquiv_graded
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:608
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.kernelShiftEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:579
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.kernelProdEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:594
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.kernelPiEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:666
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.kernelChar_shift
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:673
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.kernelChar_prod
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:681
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.kernelChar_pi
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:688
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.kernelChar_zero
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- moment_graph_sheaves
---

# Outgoing kernels under sheaf isomorphisms, sums, and shifts

Let \(B,C\) be graded sheaves over a Noetherian coefficient algebra, and let \(K_x\) denote the full outgoing kernel at \(x\). A graded sheaf isomorphism \(j:B\to C\) induces a graded isomorphism
\[
K_x(B)\xrightarrow{\sim}K_x(C).
\]
For a finite family \((B_i)\) and a nonnegative shift \(d\),
\[
K_x\!\left(\bigoplus_iB_i\right)\simeq\bigoplus_iK_x(B_i),
\qquad
K_x(B(d))\simeq K_x(B)(d).
\]

Over a polynomial coefficient algebra, whenever these kernels are free, their characters therefore satisfy
\[
K_{B(d)}(x;q)=q^dK_B(x;q),\qquad
K_{\oplus_i B_i}(x;q)=\sum_iK_{B_i}(x;q),
\qquad K_0(x;q)=0.
\]

*Proof.*

### Step 1. Restrict the stalk isomorphism to the kernel

If \(v\in K_x(B)\), then every outgoing restriction vanishes. For an edge \(e\) starting at \(x\), the lower commuting square gives
\[
\rho^{C,-}_e(j_xv)=j_e(\rho^{B,-}_e(v))=0.
\]
Thus \(j_xv\in K_x(C)\).

Conversely, if \(j_xv\in K_x(C)\), the same equality gives
\(j_e(\rho^{B,-}_e(v))=0\). Injectivity of \(j_e\) gives \(\rho^{B,-}_e(v)=0\) on every outgoing edge. Hence \(v\in K_x(B)\).

The maps \(j_x,j_x^{-1}\) therefore restrict to mutually inverse kernel maps. Both preserve degree, so this is a graded isomorphism.

### Step 2. Decompose the kernel of a finite sum

In a finite sum, the restriction of a stalk tuple is the tuple of its component restrictions. It is zero on every outgoing edge exactly when each component lies in the corresponding full outgoing kernel.

The map sending a kernel tuple to its component kernel vectors is linear, has the coordinate-assembly inverse, and preserves every homogeneous degree. This proves the sum isomorphism.

### Step 3. Track the shift

A shift leaves the underlying restriction maps unchanged. Its kernel is therefore the same underlying submodule, and its degree-\(n\) piece is the old kernel piece of degree \(n-d\). This is exactly \(K_x(B)(d)\).

### Step 4. Read off the character identities

A shifted homogeneous free basis has every degree increased by \(d\), multiplying its character by \(q^d\). The union of the component bases is a basis for a finite sum, so the characters add. The zero kernel has an empty basis and character zero.

Step 1 also preserves basis degrees, so isomorphic sheaf kernels have equal characters.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.Iso.kernelEquiv`: [CharacterReciprocity.lean:615](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L615).

`OAI.KLInvariance.MomentGraph.GradedSheaf.Iso.kernelEquiv_graded`: [CharacterReciprocity.lean:624](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L624).

`OAI.KLInvariance.MomentGraph.GradedSheaf.kernelShiftEquiv`: [CharacterReciprocity.lean:608](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L608).

`OAI.KLInvariance.MomentGraph.GradedSheaf.kernelProdEquiv`: [CharacterReciprocity.lean:579](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L579).

`OAI.KLInvariance.MomentGraph.GradedSheaf.kernelPiEquiv`: [CharacterReciprocity.lean:594](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L594).

`OAI.KLInvariance.MomentGraph.GradedSheaf.kernelChar_shift`: [CharacterReciprocity.lean:666](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L666).

`OAI.KLInvariance.MomentGraph.GradedSheaf.kernelChar_prod`: [CharacterReciprocity.lean:673](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L673).

`OAI.KLInvariance.MomentGraph.GradedSheaf.kernelChar_pi`: [CharacterReciprocity.lean:681](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L681).

`OAI.KLInvariance.MomentGraph.GradedSheaf.kernelChar_zero`: [CharacterReciprocity.lean:688](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L688).
