---
id: kl.coxeter.reduced_alternating_tail
title: The form and length of a reduced two-generator tail
kind: theorem
status: proved
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.coxeter.alternating_words
- kl.coxeter.word_data
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.ParabolicSupport.reduced_pair_eq_alternating
  - OAI.KLInvariance.ParabolicSupport.alternating_length_bound
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:764
    format: lean-location
    note: OAI.KLInvariance.ParabolicSupport.reduced_pair_eq_alternating
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:790
    format: lean-location
    note: OAI.KLInvariance.ParabolicSupport.alternating_length_bound
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

# The form and length of a reduced two-generator tail

Let \(i\ne j\), and let \(\omega\) be a word using only \(i,j\). Suppose \(\omega[i]\) is reduced, and put \(n=|\omega|\). Then
\[
\omega=a_n(i,j).
\]
If \(m_{ij}\) is finite, then \(n+1\le m_{ij}\).

*Proof.*

### Step 1. The letters alternate

A reduced word cannot contain two adjacent equal simple generators: deleting that pair preserves the product and shortens the word by two.

If \(\omega\) is nonempty, its final letter cannot be \(i\), because the appended \(i\) would then form such a pair. The final letter is therefore \(j\). Working backwards, each preceding letter must be the other of \(i,j\). This uniquely determines \(a_n(i,j)\).

### Step 2. The finite braid relation bounds the length

Suppose \(m=m_{ij}<\infty\) and \(n+1>m\). The reduced word \(\omega[i]\) is alternating and has at least \(m+1\) letters.

Replace its first alternating block of length \(m\) by the equal braid block starting with the other generator. This switches every letter of that block, including its last letter. The next letter of the original alternating word was opposite to the old last letter, so it equals the new last letter. They now cancel.

The resulting expression has two fewer letters and the same product. This contradicts reducedness. Hence \(n+1\le m\).

## References

The local word and parabolic calculations are listed below.

## Lean formalization

`OAI.KLInvariance.ParabolicSupport.reduced_pair_eq_alternating`: [Tits.lean:764](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L764).

`OAI.KLInvariance.ParabolicSupport.alternating_length_bound`: [Tits.lean:790](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L790).
