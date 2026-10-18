---
id: kl.coxeter.signed_word_action
title: Signed permutations attached to simple generators and words
kind: definition
status: formalized
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.coxeter.word_data
lean:
  repository: openai-kl
  modules:
  - Coxeter
  declarations:
  - OAI.KLInvariance.CoxeterSupport.simpleAction
  - OAI.KLInvariance.CoxeterSupport.wordAction
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Coxeter:22
    format: lean-location
    note: OAI.KLInvariance.CoxeterSupport.simpleAction
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Coxeter:50
    format: lean-location
    note: OAI.KLInvariance.CoxeterSupport.wordAction
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

# Signed permutations attached to simple generators and words

Fix a Coxeter system \(W\). A signed label is a pair
\[
(t,\varepsilon)\in W\times\mathbb Z/2\mathbb Z.
\]
The second coordinate is a bit: adding one toggles it, and adding two leaves it unchanged. The applications to strong exchange use reflection labels in the first coordinate.

For a simple generator \(s_i\), define
\[
A_i(t,\varepsilon)
=\left(s_its_i,\ \varepsilon+\mathbf1_{t=s_i}\right).
\]
The first coordinate is conjugated. The bit changes precisely when the input label equals that simple generator.

## The involution calculation

The equation \(s_its_i=s_i\) is equivalent to \(t=s_i\), by conjugating once more by \(s_i\). Thus the same equality test occurs at both applications of \(A_i\). The first coordinate returns to \(t\), and the total bit change is either zero or two. Consequently \(A_i^2=1\).

For example,
\[
A_i(s_i,0)=(s_i,1),\qquad A_i(s_i,1)=(s_i,0).
\]
For another simple label \(s_j\ne s_i\), the result is \((s_is_js_i,\varepsilon)\).

## The word action

For \(\omega=(i_1,\ldots,i_n)\), put
\[
A_\omega=A_{i_1}\circ\cdots\circ A_{i_n}.
\]
The empty word acts as the identity, and the rightmost simple permutation acts first. Appending \(i\) on the right gives
\[
A_{\omega i}=A_\omega\circ A_i.
\]

Conjugation of the first coordinate composes in the same order:
\[
A_\omega(t,\varepsilon)
=\bigl(w(\omega)t\,w(\omega)^{-1},\ \text{a bit}\bigr).
\]
The inversion-record theorem determines the second coordinate. The signed Coxeter-relation theorem then allows this word construction to descend to an action of the group.

## References

The local declarations below give the construction and its word calculations.

## Lean formalization

`OAI.KLInvariance.CoxeterSupport.simpleAction`: [Coxeter.lean:22](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Coxeter.lean#L22).

`OAI.KLInvariance.CoxeterSupport.wordAction`: [Coxeter.lean:50](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Coxeter.lean#L50).
