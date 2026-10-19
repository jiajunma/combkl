---
id: kl.coxeter.parabolic_subgroups
title: Generated parabolic subgroups and minimal coset representatives
kind: definition
status: formalized
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.coxeter.word_data
- kl.coxeter.word_reduction
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.ParabolicSupport.subgroup
  - OAI.KLInvariance.ParabolicSupport.word_mem
  - OAI.KLInvariance.ParabolicSupport.exists_word
  - OAI.KLInvariance.ParabolicSupport.exists_reduced_word
  - OAI.KLInvariance.ParabolicSupport.exists_minimal
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:639
    format: lean-location
    note: OAI.KLInvariance.ParabolicSupport.subgroup
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:641
    format: lean-location
    note: OAI.KLInvariance.ParabolicSupport.word_mem
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:651
    format: lean-location
    note: OAI.KLInvariance.ParabolicSupport.exists_word
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:667
    format: lean-location
    note: OAI.KLInvariance.ParabolicSupport.exists_reduced_word
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:714
    format: lean-location
    note: OAI.KLInvariance.ParabolicSupport.exists_minimal
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

# Generated parabolic subgroups and minimal coset representatives

Let \(J\) be a subset of the simple-generator indices of a Coxeter system. Define
\[
W_J=\langle s_j:j\in J\rangle,
\]
the smallest subgroup of \(W\) containing those generators. All lengths in this entry are measured by the ambient Coxeter length \(\ell_W\).

An element belongs to \(W_J\) exactly when it is the product of a word whose letters have indices in \(J\). To verify this description, the products of such words contain the identity, are closed under multiplication by concatenation, and are closed under inverse by reversing a word. They therefore form a subgroup containing all \(s_j\). Conversely, any subgroup containing those generators contains all their word products.

## Reduced expressions using the same generators

Take \(v\in W_J\) and choose a word for it using \(J\). The word-reduction theorem deletes positions to produce a reduced word with the same product. Every remaining letter still lies in \(J\). Thus every element of \(W_J\) has a reduced expression using \(J\).

## Cosets formed by multiplication on the right

For \(w\in W\), the coset
\[
wW_J=\{wz:z\in W_J\}
\]
consists of the elements obtainable by multiplying \(w\) on the right by a member of \(W_J\).

An element \(u\) is a minimal representative of this coset when \(u\in wW_J\) and
\[
\ell(u)\le\ell(uz)\qquad\text{for every }z\in W_J.
\]
The lengths of elements in a nonempty coset form a nonempty set of natural numbers. Choose an element whose length is its least member. This gives a minimal representative \(u\).

Writing \(u=wz\) gives \(w=uz^{-1}\). Hence there is \(v\in W_J\) with \(w=uv\), with \(u\) minimal. The length-additive decomposition theorem proves the stronger relation \(\ell(w)=\ell(u)+\ell(v)\).

For \(J=\{i\}\), the subgroup consists of \(1,s_i\). The minimal representative of \(wW_J\) is the shorter of \(w\) and \(ws_i\). For larger \(J\), minimality compares \(u\) with all products \(uz\) in the same coset.

## References

The local word and parabolic calculations are listed below.

## Lean formalization

`OAI.KLInvariance.ParabolicSupport.subgroup`: [Tits.lean:639](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L639).

`OAI.KLInvariance.ParabolicSupport.word_mem`: [Tits.lean:641](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L641).

`OAI.KLInvariance.ParabolicSupport.exists_word`: [Tits.lean:651](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L651).

`OAI.KLInvariance.ParabolicSupport.exists_reduced_word`: [Tits.lean:667](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L667).

`OAI.KLInvariance.ParabolicSupport.exists_minimal`: [Tits.lean:714](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L714).
