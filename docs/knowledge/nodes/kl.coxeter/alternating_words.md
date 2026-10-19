---
id: kl.coxeter.alternating_words
title: Alternating words with a specified final generator
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
  - Tits
  declarations:
  - OAI.KLInvariance.ParabolicSupport.reduced_pair_eq_alternating
  - OAI.KLInvariance.CoxeterSupport.wordAction_alternating
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:764
    format: lean-location
    note: OAI.KLInvariance.ParabolicSupport.reduced_pair_eq_alternating
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Coxeter:118
    format: lean-location
    note: OAI.KLInvariance.CoxeterSupport.wordAction_alternating
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the word, coset, and length hypotheses explicit?
  verdict: Checked arbitrary generator subsets, the right-multiplication coset convention,
    the alternating-word endpoint convention, and the exact noncollapsed-edge condition.
tags:
- Kazhdan-Lusztig
- Coxeter
---

# Alternating words with a specified final generator

For generator indices \(i,j\), write \(a_n(i,j)\) for the alternating word of length \(n\) ending in \(j\). The first cases are
\[
a_0=[],\quad a_1=[j],\quad a_2=[i,j],\quad
a_3=[j,i,j],\quad a_4=[i,j,i,j].
\]
Equivalently, start with the empty word and prepend \(j\) when the current length is even, or prepend \(i\) when it is odd.

This convention specifies the final letter. For even length \(2r\),
\[
\operatorname{prod}(a_{2r}(i,j))=(s_is_j)^r.
\]
For odd length \(2r+1\),
\[
\operatorname{prod}(a_{2r+1}(i,j))=s_j(s_is_j)^r.
\]

## Appending the other generator

Appending \(i\) to \(a_n(i,j)\) gives
\[
a_n(i,j)\,[i]=a_{n+1}(j,i).
\]
For example, appending \(i\) to \([j,i,j]\) gives \([j,i,j,i]\).

A word using only \(i,j\) and ending just before an appended \(i\) must have this form if the full word is reduced. Adjacent equal letters would cancel, and the last letter of the initial word must be \(j\). The reduced-tail theorem proves this assertion together with its finite-exponent length bound.

## The finite braid equality

For distinct \(i,j\) with finite exponent \(m=m_{ij}\), the two alternating products of length \(m\), starting in the two different generators, are equal. Write them as \(b_m,c_m\). Their product \(b_mc_m^{-1}\) is the alternating product \((s_is_j)^m\): reversal changes the final generator exactly as needed in each parity. The Coxeter relation therefore gives \(b_m=c_m\).

This equality permits the change of an alternating block of length \(m\) in a word. Its use in the reduced-tail bound is a direct cancellation calculation.

## References

The local word and parabolic calculations are listed below.

## Lean formalization

`OAI.KLInvariance.ParabolicSupport.reduced_pair_eq_alternating`: [Tits.lean:764](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L764).

`OAI.KLInvariance.CoxeterSupport.wordAction_alternating`: [Coxeter.lean:118](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Coxeter.lean#L118).
