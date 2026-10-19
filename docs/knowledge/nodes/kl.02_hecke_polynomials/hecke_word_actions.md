---
id: kl.hecke.word_actions
title: Word operators and the standard invertible action
kind: definition
status: formalized
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.definitions.hecke_operators
- kl.detail.hecke_quadratic_identity
- kl.coxeter.word_data
lean:
  repository: openai-kl
  modules:
  - Hecke
  declarations:
  - OAI.KLInvariance.Hecke.leftWord
  - OAI.KLInvariance.Hecke.rightWord
  - OAI.KLInvariance.Hecke.unit
  - OAI.KLInvariance.Hecke.wordUnit
  - OAI.KLInvariance.Hecke.standardUnit
  - OAI.KLInvariance.HeckeQ.leftWord
  - OAI.KLInvariance.HeckeQ.rightWord
  - OAI.KLInvariance.HeckeQ.unit
  - OAI.KLInvariance.HeckeQ.wordUnit
  - OAI.KLInvariance.HeckeQ.standardUnit
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:128
    format: lean-location
    note: OAI.KLInvariance.Hecke.leftWord
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:152
    format: lean-location
    note: OAI.KLInvariance.Hecke.rightWord
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:225
    format: lean-location
    note: OAI.KLInvariance.Hecke.unit
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:232
    format: lean-location
    note: OAI.KLInvariance.Hecke.wordUnit
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:252
    format: lean-location
    note: OAI.KLInvariance.Hecke.standardUnit
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:615
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.leftWord
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:639
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.rightWord
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:712
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.unit
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:719
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.wordUnit
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:739
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.standardUnit
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual coefficient hypotheses, conventions and source proof retained?
  verdict: Read both word/standard unit definitions; explained composition order,
    the inverse word, reduced-word choice and the length-additive identities.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Word operators and the standard invertible action

Fix either Hecke convention over \(C\). In the unnormalized convention, assume \(q\) invertible when using the unit constructions below.

For a word \(\omega=(s_1,\ldots,s_m)\), define
\[
L_\omega=L_{s_1}\cdots L_{s_m},\qquad
D_\omega=D_{s_1}\cdots D_{s_m}.
\]
Multiplication of operators means composition: the rightmost operator acts first. The empty word gives the identity operator. Prepending \(s\) gives \(L_{s\omega}=L_sL_\omega\) and \(D_{s\omega}=D_sD_\omega\).

For example, \(L_{st}e_1=e_{st}\) when \(st\) is reduced, whereas \(D_{st}e_1=e_{ts}=e_{(st)^{-1}}\). The order reversal in the right action comes from composition and right multiplication.

## Units and inverse words

A unit of the endomorphism ring is an operator together with a two-sided inverse. The [[node:kl.detail.hecke_quadratic_identity|quadratic inverse formula]] makes each \(L_s\) such a unit. The word unit is their product; its underlying operator is \(L_\omega\), and its inverse is
\[
L_\omega^{-1}=L_{s_m}^{-1}\cdots L_{s_1}^{-1}.
\]
This identity follows by cancelling adjacent inverse pairs in each composite.

## The standard action at a group element

For \(w\in W\), choose a reduced word \(\omega\) with product \(w\), and define the standard unit
\[
U_w=L_\omega.
\]
The [[node:kl.hecke.word_independence|word-independence theorem]] proves that every reduced word for \(w\) gives this same operator, including its inverse. Thus \(U_w\) is the standard invertible action attached to \(w\).

For an ascent \(\ell(sw)=\ell(w)+1\), concatenating a reduced word gives
\[
U_{sw}=L_sU_w.
\]
For a right ascent, \(U_{ws}=U_wL_s\). These length-additive identities are the ones used to construct the inverse-basis vectors.

The notation \(H_w^{-1}\) or \(T_w^{-1}\) in a bar formula denotes the vector obtained by applying the corresponding inverse standard operator to \(e_1\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Hecke.leftWord`: [Hecke.lean:128](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L128).

`OAI.KLInvariance.Hecke.rightWord`: [Hecke.lean:152](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L152).

`OAI.KLInvariance.Hecke.unit`: [Hecke.lean:225](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L225).

`OAI.KLInvariance.Hecke.wordUnit`: [Hecke.lean:232](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L232).

`OAI.KLInvariance.Hecke.standardUnit`: [Hecke.lean:252](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L252).

`OAI.KLInvariance.HeckeQ.leftWord`: [Hecke.lean:615](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L615).

`OAI.KLInvariance.HeckeQ.rightWord`: [Hecke.lean:639](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L639).

`OAI.KLInvariance.HeckeQ.unit`: [Hecke.lean:712](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L712).

`OAI.KLInvariance.HeckeQ.wordUnit`: [Hecke.lean:719](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L719).

`OAI.KLInvariance.HeckeQ.standardUnit`: [Hecke.lean:739](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L739).
