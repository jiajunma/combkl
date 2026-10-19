---
id: kl.word.set_kernel_data
title: The two-stage kernel data for upper-coordinate images
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.coordinate_images
- kl.word.reflected_sets
- kl.word.set_tail_maps
- kl.word.set_tail_detection
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.bottInterRestriction
  - OAI.KLInvariance.TitsSpace.bottUnionRestriction
  - OAI.KLInvariance.TitsSpace.bottUnionPullRestriction
  - OAI.KLInvariance.TitsSpace.bottCommonKernel
  - OAI.KLInvariance.TitsSpace.bottCommonSecond
  - OAI.KLInvariance.TitsSpace.bottCommonSecond_injective
  - OAI.KLInvariance.TitsSpace.bottUnionKernelSecond
  - OAI.KLInvariance.TitsSpace.bottUnionKernelSecond_injective
  - OAI.KLInvariance.TitsSpace.bottInter_first_zero
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1086
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottInterRestriction
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1090
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottUnionRestriction
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1094
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottUnionPullRestriction
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1099
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCommonKernel
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1103
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCommonSecond
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1108
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCommonSecond_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1112
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottUnionKernelSecond
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1117
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottUnionKernelSecond_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1373
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottInter_first_zero
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, coordinate sets, kernel maps and induction hypotheses
    explicit?
  verdict: Read the three restrictions, common kernel, both second-coordinate maps
    and their injectivity proofs. Defined all domains and the two exact-sequence roles
    before the projectivity application.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# The two-stage kernel data for upper-coordinate images

Fix a finite-generator Coxeter system, a simple reflection \(s\), a tail word \(\mathbf t\), and \(U\subseteq W\). Put
\[
J=U\cup sU,\qquad K=U\cap sU,\qquad
M'=L_{s\mathbf t}(U).
\]
Write \(L=L_{\mathbf t}\) and \(L'=L_{s\mathbf t}\) for the two image families.

The two-stage argument uses
\[
r:M'\to L'(K),\qquad
F_U:M'\to L(U),\qquad
k:L(U)\to L(K),
\]
where \(r,k\) are coordinate restrictions and \(F_U\) is the first image tail map.

Restriction commutes with this first map:
\[
kF_U=F_Kr.
\]
Hence \(F_U\) sends \(\ker r\) into \(\ker k\).

## The common kernel

Define
\[
D=\ker r\cap\ker F_U\subseteq M'.
\]
Thus \(z\in D\) has zero new-word coordinates on \(K\), and its first tail image vanishes throughout \(U\). This is bottCommonKernel.

The second image tail map restricts to
\[
\gamma:D\to{}^\tau L(sU),\qquad \gamma(z)=G_U(z).
\]
It is injective: if two elements have the same second image, their first images are both zero, and joint injectivity of \(F_U,G_U\) makes the elements equal. This is bottCommonSecond.

## The old union-restriction kernel

Define
\[
T=\ker\bigl(r_{J,U}:L(J)\to L(U)\bigr).
\]
Its vectors are old image assignments on \(J\) vanishing on \(U\). Restriction to the other part gives
\[
j:T\to L(sU).
\]
This is bottUnionKernelSecond. It is injective because an assignment on
\(J=U\cup sU\) is determined by these two restrictions, and its restriction to \(U\) is already zero.

Twisting gives another injective map
\[
{}^\tau j:{}^\tau T\to{}^\tau L(sU).
\]
The [[node:kl.word.common_kernel_equivalence|common-kernel theorem]] proves that \(\gamma\) and \({}^\tau j\) have the same image when \(U\) is upper and the shorter word has compatible-tuple lifting. This identifies \(D\) with the twisted old kernel.

## The two successive sequences

Once \(F_U:\ker r\to\ker k\) is shown surjective, the two sequences are
\[
0\to D\to\ker r\to\ker k\to0,
\qquad
0\to\ker r\to M'\xrightarrow{r}L'(K)\to0.
\]
They organize the projectivity proof: the first controls \(\ker r\), and the second controls the new image \(M'\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottInterRestriction`: [IntegralPairings.lean:1086](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1086).

`OAI.KLInvariance.TitsSpace.bottUnionRestriction`: [IntegralPairings.lean:1090](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1090).

`OAI.KLInvariance.TitsSpace.bottUnionPullRestriction`: [IntegralPairings.lean:1094](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1094).

`OAI.KLInvariance.TitsSpace.bottCommonKernel`: [IntegralPairings.lean:1099](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1099).

`OAI.KLInvariance.TitsSpace.bottCommonSecond`: [IntegralPairings.lean:1103](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1103).

`OAI.KLInvariance.TitsSpace.bottCommonSecond_injective`: [IntegralPairings.lean:1108](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1108).

`OAI.KLInvariance.TitsSpace.bottUnionKernelSecond`: [IntegralPairings.lean:1112](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1112).

`OAI.KLInvariance.TitsSpace.bottUnionKernelSecond_injective`: [IntegralPairings.lean:1117](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1117).

`OAI.KLInvariance.TitsSpace.bottInter_first_zero`: [IntegralPairings.lean:1373](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1373).
