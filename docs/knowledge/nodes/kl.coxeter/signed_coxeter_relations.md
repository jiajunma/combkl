---
id: kl.coxeter.signed_coxeter_relations
title: Coxeter relations for the signed simple permutations
kind: theorem
status: proved
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.coxeter.signed_word_action
- kl.coxeter.word_sign_record
lean:
  repository: openai-kl
  modules:
  - Coxeter
  declarations:
  - OAI.KLInvariance.CoxeterSupport.leftInvSeq_alternating_formula
  - OAI.KLInvariance.CoxeterSupport.leftInvSeq_relation_doubled
  - OAI.KLInvariance.CoxeterSupport.wordAction_alternating
  - OAI.KLInvariance.CoxeterSupport.simpleAction_liftable
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Coxeter:92
    format: lean-location
    note: OAI.KLInvariance.CoxeterSupport.leftInvSeq_alternating_formula
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Coxeter:106
    format: lean-location
    note: OAI.KLInvariance.CoxeterSupport.leftInvSeq_relation_doubled
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Coxeter:118
    format: lean-location
    note: OAI.KLInvariance.CoxeterSupport.wordAction_alternating
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Coxeter:132
    format: lean-location
    note: OAI.KLInvariance.CoxeterSupport.simpleAction_liftable
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

# Coxeter relations for the signed simple permutations

For a finite Coxeter exponent \(m=m_{ij}\), the signed simple permutations satisfy
\[
(A_iA_j)^m=1.
\]
Together with \(A_i^2=1\), these relations define a group action of \(W\) on \(W\times\mathbb Z/2\mathbb Z\).

*Proof.*

### Step 1. The relation word and its inversion list

Write \(s=s_i\), \(t=s_j\), and let \(\omega\) be the alternating word \(stst\cdots st\) with \(2m\) letters. Its product is \((st)^m=1\), and its signed word action is \((A_iA_j)^m\).

Its inversion entry at position \(k+1\), for \(0\le k<2m\), is
\[
s(ts)^k.
\]
For \(k=2r\), the prefix is \((st)^r\) and the next letter is \(s\). Conjugation gives
\[
(st)^rs(ts)^r=s(ts)^{2r}.
\]
For \(k=2r+1\), the prefix is \((st)^rs\) and the next letter is \(t\). The resulting conjugate is
\[
(st)^rst\,s(ts)^r=s(ts)^{2r+1}.
\]
Both computations use \((st)^rs=s(ts)^r\), obtained by repeated cancellation of adjacent copies of \(s\).

### Step 2. The two equal halves

The Coxeter relation also gives \((ts)^m=1\). Hence
\[
s(ts)^{k+m}=s(ts)^k
\]
for every \(k\). The second half of the inversion list equals the first half. Each label therefore occurs twice its multiplicity in the first half, and its total multiplicity is even.

### Step 3. The relation acts trivially

Apply the inversion-record theorem to \(\omega\). Since its product is \(1\), the input \(w(\omega)^{-1}rw(\omega)\) is just \(r\). The output label is \(r\), and the bit changes by an even number. Thus \(A_\omega(r,\varepsilon)=(r,\varepsilon)\) for every pair.

This proves \((A_iA_j)^m=1\). The diagonal case uses \(m_{ii}=1\) and the two-letter word \(s_is_i\). Infinite exponents contribute no defining relation. The universal property of the Coxeter presentation now supplies the action of \(W\).

## References

The local declarations below give the construction and its word calculations.

## Lean formalization

`OAI.KLInvariance.CoxeterSupport.leftInvSeq_alternating_formula`: [Coxeter.lean:92](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Coxeter.lean#L92).

`OAI.KLInvariance.CoxeterSupport.leftInvSeq_relation_doubled`: [Coxeter.lean:106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Coxeter.lean#L106).

`OAI.KLInvariance.CoxeterSupport.wordAction_alternating`: [Coxeter.lean:118](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Coxeter.lean#L118).

`OAI.KLInvariance.CoxeterSupport.simpleAction_liftable`: [Coxeter.lean:132](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Coxeter.lean#L132).

An infinite Coxeter exponent is encoded by zero. In the liftability condition its zeroth power equals the identity, imposing no relation on that pair.
