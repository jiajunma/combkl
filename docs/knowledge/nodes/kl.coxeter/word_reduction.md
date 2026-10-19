---
id: kl.coxeter.word_reduction
title: Reduction of a word by deleting letters
kind: theorem
status: proved
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.coxeter.word_data
- kl.detail.strong_exchange
lean:
  repository: openai-kl
  modules:
  - Bruhat
  declarations:
  - OAI.KLInvariance.exists_reduced_subword
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:214
    format: lean-location
    note: OAI.KLInvariance.exists_reduced_subword
verification:
  statement: accepted
  proof: accepted
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

# Reduction of a word by deleting letters

Every word in the simple generators contains a reduced subword with the same product. A subword is obtained by deleting positions and retaining the order of the remaining letters.

*Proof.*

### Step 1. Induction on the word

The empty word is reduced. Write a nonempty word as \(s_i\omega\), and suppose the assertion is known for the shorter word \(\omega\). Choose a reduced subword \(\nu\) of \(\omega\) with the same product \(v\).

The length of \(s_iv\) is either \(\ell(v)+1\) or \(\ell(v)-1\).

### Step 2. The ascent case

If \(\ell(s_iv)=\ell(v)+1\), the word \(s_i\nu\) has \(\ell(v)+1\) letters and product \(s_iv\). It is therefore reduced. It is a subword of \(s_i\omega\), obtained by keeping the initial letter and the chosen positions of \(\nu\).

### Step 3. The descent case

If \(\ell(s_iv)=\ell(v)-1\), strong exchange applied to the simple reflection \(s_i\) deletes a position from \(\nu\) and gives the product \(s_iv\).

The resulting word has \(|\nu|-1=\ell(v)-1=\ell(s_iv)\) letters, so it is reduced. Its positions lie in \(\omega\); omitting the initial \(s_i\) makes it a subword of the original \(s_i\omega\).

Both cases construct the required reduced subword and complete the induction.

## References

The local word and parabolic calculations are listed below.

## Lean formalization

`OAI.KLInvariance.exists_reduced_subword`: [Bruhat.lean:214](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L214).
