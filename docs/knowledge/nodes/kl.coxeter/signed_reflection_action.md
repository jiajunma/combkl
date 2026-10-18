---
id: kl.coxeter.signed_reflection_action
title: The signed reflection action of the Coxeter group
kind: definition
status: formalized
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.coxeter.signed_coxeter_relations
- kl.coxeter.word_sign_record
lean:
  repository: openai-kl
  modules:
  - Coxeter
  declarations:
  - OAI.KLInvariance.CoxeterSupport.reflectionAction
  - OAI.KLInvariance.CoxeterSupport.reflectionAction_simple
  - OAI.KLInvariance.CoxeterSupport.reflectionAction_wordProd
  - OAI.KLInvariance.CoxeterSupport.reflectionAction_translation
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Coxeter:144
    format: lean-location
    note: OAI.KLInvariance.CoxeterSupport.reflectionAction
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Coxeter:147
    format: lean-location
    note: OAI.KLInvariance.CoxeterSupport.reflectionAction_simple
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Coxeter:151
    format: lean-location
    note: OAI.KLInvariance.CoxeterSupport.reflectionAction_wordProd
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Coxeter:160
    format: lean-location
    note: OAI.KLInvariance.CoxeterSupport.reflectionAction_translation
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry retain the local construction and its quantifiers?
  verdict: Checked arbitrary words, arbitrary labels, sign translation, and the precise
    Coxeter presentation relations directly in the local source.
tags:
- Kazhdan-Lusztig
- Coxeter
---

# The signed reflection action of the Coxeter group

The signed reflection action is the homomorphism
\[
A:W\longrightarrow\operatorname{Sym}(W\times\mathbb Z/2\mathbb Z)
\]
whose value at a simple generator is the signed simple permutation. The signed Coxeter-relation theorem supplies the presentation relations, so for every word \(\omega\),
\[
A_{w(\omega)}=A_\omega.
\]
In particular, two words for the same group element act by the same permutation.

## Conjugation and sign translation

For fixed \(w,t\in W\), there is a bit \(\delta(w,t)\) such that
\[
A_w(t,\varepsilon)
=\left(wtw^{-1},\varepsilon+\delta(w,t)\right)
\]
for every \(\varepsilon\). Choose a word \(\omega\) for \(w\). Applying the inversion-record formula with label \(wtw^{-1}\) gives
\[
\delta(w,t)=c_\omega(wtw^{-1})\bmod2.
\]
This formula also shows that the translation is independent of the initial bit.

The group-action law and inverse law are
\[
A_{wz}=A_w\circ A_z,\qquad A_{w^{-1}}=A_w^{-1}.
\]
Conjugation preserves reflections, so the subset of pairs whose first coordinate is a reflection is invariant.

A simple reflection toggles the bit of its own label. Conjugating this fact and cancelling the inverse sign translations proves the corresponding assertion for every reflection. That assertion is the sign input in strong exchange.

## References

The local declarations below give the construction and its word calculations.

## Lean formalization

`OAI.KLInvariance.CoxeterSupport.reflectionAction`: [Coxeter.lean:144](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Coxeter.lean#L144).

`OAI.KLInvariance.CoxeterSupport.reflectionAction_simple`: [Coxeter.lean:147](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Coxeter.lean#L147).

`OAI.KLInvariance.CoxeterSupport.reflectionAction_wordProd`: [Coxeter.lean:151](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Coxeter.lean#L151).

`OAI.KLInvariance.CoxeterSupport.reflectionAction_translation`: [Coxeter.lean:160](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Coxeter.lean#L160).
