---
id: kl.duality.stalk_character
title: Stalk and outgoing-kernel characters of graded sheaves
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.graded_character
- kl.sheaves.upward_kernel
- kl.sheaves.hilbert_free
- kl.sheaves.boundary_existence
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  - Decomposition
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.freeStalkChar
  - OAI.KLInvariance.MomentGraph.GradedSheaf.freeKernelChar
  - OAI.KLInvariance.MomentGraph.GradedSheaf.kernelData
  - OAI.KLInvariance.BruhatGraph.stalkCharacter
  - OAI.KLInvariance.BruhatGraph.lowerCharacter
  - OAI.KLInvariance.MomentGraph.GradedSheaf.kernelEquivFull
  - OAI.KLInvariance.BruhatGraph.costalkCharacter
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:18
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.freeStalkChar
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:705
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.freeKernelChar
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:576
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.kernelData
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:206
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.stalkCharacter
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:104
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.lowerCharacter
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:787
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.kernelEquivFull
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1804
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.costalkCharacter
verification:
  definition: accepted
  proof: not_applicable
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

# Stalk and outgoing-kernel characters of graded sheaves

Let \(A=k[X_1,\ldots,X_N]\), with every variable in degree one. For a finite nonnegative graded free module \(M\), its graded character is
\[
\operatorname{ch}(M;q)=\sum_iq^{d_i},
\]
where \(d_i\) are the degrees of a homogeneous free basis. This polynomial is independent of the chosen homogeneous basis.

For a graded sheaf \(B\) with free stalks, define its stalk character at \(x\) by
\[
C_B(x;q)=\operatorname{ch}(B^x;q).
\]
If its full outgoing kernel \(K_x(B)\) is free, define the kernel character by
\[
K_B(x;q)=\operatorname{ch}(K_x(B);q).
\]
The kernel carries the grading inherited from the stalk. Each coefficient counts basis generators of the corresponding degree and is a nonnegative integer.

## The full outgoing-kernel module

If \(\rho^-_e:B^x\to B^e\) is the lower restriction for an outgoing edge \(e:x\to y\), then
\[
K_x(B)=\{v\in B^x:\rho^-_e(v)=0\text{ for every outgoing }e\}.
\]
Its degree-\(n\) piece is \(K_x(B)\cap B^x_n\). Each restriction preserves degree, so the vanishing conditions hold on every homogeneous component of a kernel vector.

The source packages this finite graded module as kernelData. Equivalently, combine the outgoing restrictions into
\[
\partial_x:B^x\to\prod_{e:x\to y}B^e,\qquad
v\mapsto(\rho^-_e(v))_e.
\]
Then \(K_x(B)=\ker\partial_x\), with the same underlying vectors. This is kernelEquivFull.

The argument to freeKernelChar supplies freeness of this full kernel. The boundary-kernel theorem constructs that argument for the actual boundary sheaf; the resulting costalkCharacter is its full outgoing-kernel character.

## The actual boundary-stalk character

For the chosen normalized boundary sheaf on an interval \([u,b]\), the source defines the stalk character using its constructed free stalk at \(x\). On \([1,b]\), write this polynomial as
\[
C_{x,b}(q).
\]
The normalized top stalk is \(A\) in degree zero, so \(C_{b,b}(q)=1\). Its kernel character is supplied by the full-kernel freeness and duality theorems.

## The lower-character function

For \(c\in[1,b]\), define a character function on the whole interval by
\[
C^{\le c}_x(q)=
\begin{cases}
C_{x,c}(q),&x\le c,\\
0,&x\not\le c.
\end{cases}
\]
This is the source's lower character. Its zero extension gives a common vertex domain for all model centers. The lower-model theorem identifies it with the stalk character of \(O_c\).

## Characters and Hilbert values

The character records free-basis degrees. The Hilbert value counts the dimensions of all homogeneous components:
\[
H_M(q)=\sum_{n\ge0}\dim_k(M_n)q^n.
\]
For \(0<q<1\),
\[
H_M(q)=\operatorname{ch}(M;q)(1-q)^{-N}.
\]
Thus the stalk and kernel characters give their respective Hilbert numerators over the same polynomial coefficient algebra.

## The one-edge example

For the congruence model \(O_y\) on \(x\to y\),
\[
C_{O_y}(x;q)=C_{O_y}(y;q)=1,
\qquad
K_{O_y}(x;q)=q,\quad K_{O_y}(y;q)=1.
\]
The lower kernel is \(\alpha A\), whose generator has degree one; the top kernel is \(A\).

For \(B=O_y\oplus O_x(2)\),
\[
C_B(x;q)=1+q^2,\qquad K_B(x;q)=q+q^2.
\]
The additional model contributes a degree-two generator to both quantities.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.freeStalkChar`: [Decomposition.lean:18](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L18).

`OAI.KLInvariance.MomentGraph.GradedSheaf.freeKernelChar`: [CharacterReciprocity.lean:705](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L705).

`OAI.KLInvariance.MomentGraph.GradedSheaf.kernelData`: [CharacterReciprocity.lean:576](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L576).

`OAI.KLInvariance.BruhatGraph.stalkCharacter`: [SheafMorphisms.lean:206](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L206).

`OAI.KLInvariance.BruhatGraph.lowerCharacter`: [Decomposition.lean:104](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L104).

`OAI.KLInvariance.MomentGraph.GradedSheaf.kernelEquivFull`: [CharacterReciprocity.lean:787](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L787).

`OAI.KLInvariance.BruhatGraph.costalkCharacter`: [CharacterReciprocity.lean:1804](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1804).
