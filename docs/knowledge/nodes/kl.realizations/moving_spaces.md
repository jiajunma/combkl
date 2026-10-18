---
id: kl.realization.moving_spaces
title: Moving spaces, fixed spaces, and reflection faithfulness
kind: definition
status: formalized
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.realization.linear_reflection
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.Realization.finrank_moving_conj
  - OAI.KLInvariance.Realization.range_reflection_sub_id
  - OAI.KLInvariance.Realization.finrank_reflection_sub_id
  - OAI.KLInvariance.TitsSpace.reflectionFaithful
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1015
    format: lean-location
    note: OAI.KLInvariance.Realization.finrank_moving_conj
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1080
    format: lean-location
    note: OAI.KLInvariance.Realization.range_reflection_sub_id
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1099
    format: lean-location
    note: OAI.KLInvariance.Realization.finrank_reflection_sub_id
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1255
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.reflectionFaithful
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the calculation preserve the local statement and proof route?
  verdict: Checked the general linear-functional hypotheses, even/odd Chebyshev vanishings,
    rank-one normal form, and arbitrary-rank coordinate action.
tags:
- Kazhdan-Lusztig
- realization
---

# Moving spaces, fixed spaces, and reflection faithfulness

For an invertible linear map \(g:V\to V\), define its fixed space and moving space by
\[
\operatorname{Fix}(g)=\ker(g-1),\qquad
\operatorname{Mov}(g)=\operatorname{im}(g-1).
\]
The moving rank is \(\dim\operatorname{Mov}(g)\). If \(V\) is finite-dimensional, rank–nullity gives
\[
\dim\operatorname{Mov}(g)=\dim V-\dim\operatorname{Fix}(g).
\]
Thus moving rank one means that the fixed space has codimension one.

## The moving line of a reflection

For \(r(v)=v-f(v)\alpha\), with \(f(\alpha)=2\),
\[
(r-1)v=-f(v)\alpha.
\]
Every value lies in \(\mathbb R\alpha\), and the value at \(-\alpha/2\) is \(\alpha\). Therefore
\[
\operatorname{Mov}(r)=\mathbb R\alpha.
\]
The normalization makes \(\alpha\ne0\), so the moving rank is one.

## Conjugation

For an invertible \(h\),
\[
hgh^{-1}-1=h(g-1)h^{-1}.
\]
Surjectivity of \(h^{-1}\) and injectivity of \(h\) identify
\[
\operatorname{Mov}(hgh^{-1})=h(\operatorname{Mov}(g)).
\]
Thus conjugation preserves moving rank. For a group representation, this transfers the rank-one property of simple reflections to all their conjugates.

## Faithful and reflection-faithful representations

A representation \(\rho:W\to\operatorname{GL}(V)\) is faithful when \(\rho\) is injective. Equivalently, \(\rho(w)=1\) implies \(w=1\).

For a Coxeter group, it is reflection faithful when it is faithful and
\[
\dim\operatorname{Mov}(\rho(w))=1
\quad\Longleftrightarrow\quad
w\text{ is a Coxeter reflection}.
\]
The extended Tits action satisfies this property. Its proof combines the root-sign criterion, a rank-one orthogonal calculation, and descent in Coxeter length.

## References

The local source statements and calculations are listed below.

## Lean formalization

`OAI.KLInvariance.Realization.finrank_moving_conj`: [Tits.lean:1015](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1015).

`OAI.KLInvariance.Realization.range_reflection_sub_id`: [Tits.lean:1080](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1080).

`OAI.KLInvariance.Realization.finrank_reflection_sub_id`: [Tits.lean:1099](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1099).

`OAI.KLInvariance.TitsSpace.reflectionFaithful`: [Tits.lean:1255](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1255).
