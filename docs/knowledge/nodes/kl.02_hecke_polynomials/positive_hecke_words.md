---
id: kl.hecke.positive_words
title: Positive Hecke words and their coefficient recurrence
kind: definition
status: formalized
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.definitions.hecke_operators
- kl.hecke.word_actions
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.HeckeQ.left_coeff
  - OAI.KLInvariance.HeckeQ.left_plus_coeff
  - OAI.KLInvariance.HeckeQ.positiveWord
  - OAI.KLInvariance.HeckeQ.positiveWord_nil
  - OAI.KLInvariance.HeckeQ.positiveWord_cons_coeff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:152
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.left_coeff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:197
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.left_plus_coeff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:204
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.positiveWord
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:208
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.positiveWord_nil
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:211
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.positiveWord_cons_coeff
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual coefficient hypotheses, conventions and source proof retained?
  verdict: Read positiveWord and the coefficient lemmas in IntegralPairings. Explained
    input versus output descent conditions, factor order, arbitrary words and elementary
    examples.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Positive Hecke words and their coefficient recurrence

Fix a Coxeter system and a commutative coefficient ring with parameter \(q\). For a word \(\omega=(s_1,\ldots,s_m)\), its positive Hecke word is the vector
\[
H_\omega(q)=(I+L_{s_1}(q))\cdots(I+L_{s_m}(q))T_1.
\]
Equivalently,
\[
H_{\varnothing}(q)=T_1,\qquad
H_{s\omega}(q)=H_\omega(q)+L_s(q)H_\omega(q).
\]
Write \(h_\omega(x;q)\) for its coefficient at \(T_x\). These definitions apply to every word, whether reduced or not.

## Coefficients of a simple left operation

For a general vector \(f=\sum_w f(w)T_w\), only \(w=sx\) and \(w=x\) can contribute to \((L_sf)(x)\). If \(sx<x\), the term from \(w=sx\) is an ascent contribution \(f(sx)\), while the term from \(w=x\) is \((q-1)f(x)\). If \(sx>x\), the former is a descent contribution \(qf(sx)\), and the latter is zero. Thus
\[
(L_s(q)f)(x)=
\begin{cases}
f(sx)+(q-1)f(x),&sx<x,\\
qf(sx),&sx>x.
\end{cases}
\]
Adding \(f(x)\) gives the positive-word recurrence
\[
h_{s\omega}(x;q)=
\begin{cases}
h_\omega(sx;q)+q\,h_\omega(x;q),&sx<x,\\
h_\omega(x;q)+q\,h_\omega(sx;q),&sx>x.
\end{cases}
\]

## One and two letters

For one letter,
\[
H_s(q)=T_1+T_s.
\]
If \(s\ne t\), then \(st\) is reduced and
\[
H_{st}(q)=T_1+T_s+T_t+T_{st}.
\]
For the repeated word \(ss\), the quadratic relation instead gives
\[
H_{ss}(q)
=(I+L_s)(T_1+T_s)
=(1+q)(T_1+T_s).
\]
The vector is attached to the word: its construction retains the number and order of the factors.

Over \(\mathbb Z[q]\), the recurrence has additions and multiplication by \(q\), starting from coefficients zero and one. Induction therefore gives nonnegative integer coefficients. In the word-module branch, the character theorem identifies these polynomials with the actual word-stalk characters.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.HeckeQ.left_coeff`: [IntegralPairings.lean:152](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L152).

`OAI.KLInvariance.HeckeQ.left_plus_coeff`: [IntegralPairings.lean:197](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L197).

`OAI.KLInvariance.HeckeQ.positiveWord`: [IntegralPairings.lean:204](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L204).

`OAI.KLInvariance.HeckeQ.positiveWord_nil`: [IntegralPairings.lean:208](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L208).

`OAI.KLInvariance.HeckeQ.positiveWord_cons_coeff`: [IntegralPairings.lean:211](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L211).
