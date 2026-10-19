---
id: kl.word.head_patch
title: Patching the two tail assignments on a reflected union
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.tail_maps
- kl.word.reflected_sets
- kl.word.upper_image_properties
- kl.word.set_tail_detection
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.ReflectionPairTranslation.tensor_difference
  - OAI.KLInvariance.TitsSpace.bottHead_difference
  - OAI.KLInvariance.TitsSpace.bottHeadPatch
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:761
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.tensor_difference
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:821
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHead_difference
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:827
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadPatch
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, coordinate sets, kernel maps and induction hypotheses
    explicit?
  verdict: Read tensor_difference, the actual branch definition of bottHeadPatch and
    its zero-overlap specialization. Defined the patch as a coordinate assignment
    and proved the underlying root-divisible tail difference.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Patching the two tail assignments on a reflected union

Fix a finite-generator Coxeter system, a simple reflection \(s\), and a tail word \(\mathbf t\). Let \(\tau=\chi_s\), and let \(\alpha=\alpha_s\) be the simple-root polynomial.

For \(m\in M_{s\mathbf t}\), write
\[
p=\mu(m),\qquad q=\nu(m)
\]
for its two underlying tail vectors in \(M_{\mathbf t}\).
They satisfy
\[
p-q=\alpha n
\]
for some tail vector \(n\). Indeed, for a pure tensor \(a\otimes v\), the difference is
\[
av-\tau(a)v=(a-\tau(a))v=\alpha(bv)
\]
with \(a-\tau(a)=\alpha b\). Summing this calculation over a finite pure-tensor expression proves the assertion for every \(m\).

## The patched assignment

For \(U\subseteq W\), put \(J=U\cup sU\) and \(K=U\cap sU\). Define the head patch on \(J\) by
\[
z_x=
\begin{cases}
\pi_x(p),&x\in U,\\
\pi_x(q),&x\in J\setminus U.
\end{cases}
\]
This is the source's bottHeadPatch.

When the two tail projections agree on \(K\), the patch agrees with \(p\) throughout \(U\) and with \(q\) throughout \(sU\): on the overlap, the two prescriptions give the same value.

The [[node:kl.word.head_patch_lifting|patched-tail lifting theorem]] proves compatibility on \(J\) when \(U\) is upper. The root multiple \(p-q=\alpha n\) handles a crossing edge between the two pieces. If the tail word has compatible-tuple lifting, the whole patch then has a single tail-word preimage.

## Vanishing on the overlap

If the new word vector \(m\) vanishes on \(K\), [[node:kl.word.set_tail_detection|set-tail detection]] and \(sK=K\) show that both \(p\) and \(q\) vanish there. Their values on \(K\) therefore agree. This is the overlap condition used in the two-stage kernel argument.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ReflectionPairTranslation.tensor_difference`: [IntegralPairings.lean:761](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L761).

`OAI.KLInvariance.TitsSpace.bottHead_difference`: [IntegralPairings.lean:821](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L821).

`OAI.KLInvariance.TitsSpace.bottHeadPatch`: [IntegralPairings.lean:827](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L827).
