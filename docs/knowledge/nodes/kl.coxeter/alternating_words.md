---
id: kl.coxeter.alternating_words
title: Alternating words and their endpoint conventions
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
  - Dihedral
  - Tits
  declarations:
  - OAI.KLInvariance.ParabolicSupport.reduced_pair_eq_alternating
  - OAI.KLInvariance.CoxeterSupport.wordAction_alternating
  - OAI.KLInvariance.Dihedral.alt
  - OAI.KLInvariance.Dihedral.length_alt
  - OAI.KLInvariance.Dihedral.take_alt
  - OAI.KLInvariance.Dihedral.alt_sublist
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
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:74
    format: lean-location
    note: OAI.KLInvariance.Dihedral.alt
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:80
    format: lean-location
    note: OAI.KLInvariance.Dihedral.length_alt
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:85
    format: lean-location
    note: OAI.KLInvariance.Dihedral.take_alt
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:131
    format: lean-location
    note: OAI.KLInvariance.Dihedral.alt_sublist
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the reduced-word, coefficient and interval
    hypotheses?
  verdict: Retained the final-letter convention used in Tits and added the first-letter
    Dihedral.alt definition, parity conversion, length and prefix identities. Both
    conventions are explicit.
tags:
- Kazhdan-Lusztig
- dihedral
---

# Alternating words and their endpoint conventions

## A specified final generator

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

## A specified first generator in rank two

For a Coxeter system with two simple generators, index them by \(i\in\{0,1\}\), and write \(\bar i\) for the other index. Define
\[
\omega_i(0)=[],\qquad
\omega_i(n+1)=[i]\,\omega_{\bar i}(n).
\]
This is Dihedral.alt in the local source. Its first cases are
\[
\omega_i(1)=[i],\quad
\omega_i(2)=[i,\bar i],\quad
\omega_i(3)=[i,\bar i,i].
\]
It has length \(n\), begins with \(i\) when nonempty, and has prefix
\[
\operatorname{take}_k\omega_i(n)=\omega_i(\min\{k,n\}).
\]
The recursive definition proves the length and prefix identities by induction on \(n\), removing the first letter at each step.

The two conventions describe the same alternating lists with different endpoint data. In the final-generator notation above,
\[
\omega_i(n)=
\begin{cases}
a_n(i,\bar i),&n\text{ even},\\
a_n(\bar i,i),&n\text{ odd}.
\end{cases}
\]
The rank-two polynomial calculation uses the specified first generator, so removing the first letter changes \(\omega_i(n+1)\) to \(\omega_{\bar i}(n)\).

Reducedness is a separate property of an alternating word. Every prefix of a reduced word remains reduced. The next theorem identifies every reduced rank-two word with one of these lists and derives the prescribed first letter from a left descent.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ParabolicSupport.reduced_pair_eq_alternating`: [Tits.lean:764](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L764).

`OAI.KLInvariance.CoxeterSupport.wordAction_alternating`: [Coxeter.lean:118](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Coxeter.lean#L118).

`OAI.KLInvariance.Dihedral.alt`: [Dihedral.lean:74](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L74).

`OAI.KLInvariance.Dihedral.length_alt`: [Dihedral.lean:80](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L80).

`OAI.KLInvariance.Dihedral.take_alt`: [Dihedral.lean:85](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L85).

`OAI.KLInvariance.Dihedral.alt_sublist`: [Dihedral.lean:131](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L131).
