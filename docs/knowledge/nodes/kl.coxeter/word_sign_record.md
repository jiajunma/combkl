---
id: kl.coxeter.word_sign_record
title: The inversion sequence records the sign change of a word
kind: theorem
status: proved
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.coxeter.signed_word_action
- kl.coxeter.word_data
lean:
  repository: openai-kl
  modules:
  - Coxeter
  declarations:
  - OAI.KLInvariance.CoxeterSupport.wordAction_record
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Coxeter:60
    format: lean-location
    note: OAI.KLInvariance.CoxeterSupport.wordAction_record
verification:
  statement: accepted
  proof: accepted
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

# The inversion sequence records the sign change of a word

Let \(\omega=(i_1,\ldots,i_n)\) be any word, let \(w=w(\omega)\), and let \(c_\omega(t)\) count the occurrences of \(t\) in its left inversion sequence. For \(t\in W\) and \(\varepsilon\in\mathbb Z/2\mathbb Z\),
\[
A_\omega(w^{-1}tw,\varepsilon)
=\bigl(t,\varepsilon+c_\omega(t)\bmod2\bigr).
\]

*Proof.*

### Step 1. The empty word

For the empty word, \(w=1\), the action is the identity, and the inversion sequence is empty. Both sides are \((t,\varepsilon)\).

### Step 2. Append one letter

Suppose the formula holds for \(\omega\), and append a simple generator \(s=s_i\). The new word product is \(ws\). Its input label is
\[
(ws)^{-1}t(ws)=s\,w^{-1}tw\,s.
\]
Applying \(A_i\) conjugates this label to \(w^{-1}tw\) and adds one to the bit exactly when
\[
s\,w^{-1}tw\,s=s.
\]
Multiplying this equality on both sides by \(s\) shows that it is equivalent to \(w^{-1}tw=s\), or \(t=wsw^{-1}\).

### Step 3. Apply the induction hypothesis

The remaining action is \(A_\omega\). The induction hypothesis, with its initial bit increased by the indicator from Step 2, gives the output
\[
\left(t,\varepsilon+\mathbf1_{t=wsw^{-1}}+c_\omega(t)\bmod2\right).
\]

The inversion sequence of the appended word is the old sequence followed by \(wsw^{-1}\). Its multiplicity of \(t\) is therefore
\[
c_{\omega i}(t)=c_\omega(t)+\mathbf1_{t=wsw^{-1}}.
\]
This identifies the output with the required formula for \(\omega i\). Every finite word is obtained by successive right appends, so induction proves the theorem.

## References

The local declarations below give the construction and its word calculations.

## Lean formalization

`OAI.KLInvariance.CoxeterSupport.wordAction_record`: [Coxeter.lean:60](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Coxeter.lean#L60).
