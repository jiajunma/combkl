---
id: kl.coxeter.dihedral_reduced_words
title: Reduced alternating words in a rank-two Coxeter system
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
  - Dihedral
  declarations:
  - OAI.KLInvariance.Dihedral.reduced_cons_cons_ne
  - OAI.KLInvariance.Dihedral.reduced_cons_eq_alt
  - OAI.KLInvariance.Dihedral.reduced_eq_alt
  - OAI.KLInvariance.Dihedral.exists_alt
  - OAI.KLInvariance.Dihedral.reduced_alt_take
  - OAI.KLInvariance.Dihedral.eq_alt_of_descent
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:93
    format: lean-location
    note: OAI.KLInvariance.Dihedral.reduced_cons_cons_ne
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:101
    format: lean-location
    note: OAI.KLInvariance.Dihedral.reduced_cons_eq_alt
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:114
    format: lean-location
    note: OAI.KLInvariance.Dihedral.reduced_eq_alt
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:120
    format: lean-location
    note: OAI.KLInvariance.Dihedral.exists_alt
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:127
    format: lean-location
    note: OAI.KLInvariance.Dihedral.reduced_alt_take
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:173
    format: lean-location
    note: OAI.KLInvariance.Dihedral.eq_alt_of_descent
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the reduced-word, coefficient and interval
    hypotheses?
  verdict: Read the reduced-list and descent lemmas in Dihedral. Expanded adjacent
    cancellation, tail induction, element existence, reduced prefixes and the one-letter
    extension of a reduced descent word.
tags:
- Kazhdan-Lusztig
- dihedral
---

# Reduced alternating words in a rank-two Coxeter system

Let \(D\) be a Coxeter group with two simple generators \(s_0,s_1\). Every reduced word is alternating. Consequently every \(w\in D\) has a reduced expression
\[
w=\operatorname{prod}\omega_i(\ell(w))
\]
for some first index \(i\).

If \(s_iw<w\), this expression can be chosen with first index \(i\). Every prefix \(\omega_i(k)\) of a reduced \(\omega_i(n)\), \(k\le n\), is reduced.

*Proof.*

### Step 1. Exclude adjacent equal letters

Suppose a reduced word contains adjacent occurrences of the same simple generator \(s\). Since \(s^2=1\), removing those two letters preserves the product and shortens the expression by two. This contradicts reducedness.

In particular, if a reduced word begins with \(i,j\), then \(j\ne i\). With only two possible indices, \(j=\bar i\).

### Step 2. Determine the whole reduced list

Induct on the word length. The empty word is \(\omega_i(0)\), for either index.

For a nonempty reduced word beginning with \(i\), its tail is reduced. If the tail is nonempty, Step 1 says it begins with \(\bar i\). The induction hypothesis identifies that tail with the corresponding alternating list, so the full word is
\([i]\omega_{\bar i}(n)=\omega_i(n+1)\).

Thus a nonempty reduced word is determined as a list by its length and first letter.

### Step 3. Obtain an alternating expression for any element

Choose a reduced expression for \(w\). Its number of letters equals \(\ell(w)\), and Step 2 puts it in the required alternating form. This proves existence for every element.

The prefix assertion follows from the reduced-prefix property of words: a shorter expression for a prefix could be followed by the unchanged suffix to shorten the original word. The prefix formula identifies that list with \(\omega_i(k)\).

### Step 4. Prescribe the first letter from a descent

Assume \(\ell(s_iw)<\ell(w)\). Choose a reduced word \(\nu\) for \(s_iw\). Simple multiplication changes length by one, so
\[
|\nu|=\ell(s_iw)=\ell(w)-1.
\]
Prepending \(i\) gives product \(s_i(s_iw)=w\) and length \(\ell(w)\). It is therefore reduced.

By Step 2 this word is \(\omega_i(\ell(w))\). This proves the assertion with prescribed first letter.

All these arguments use reduced expressions and the two-generator condition. They apply to finite and infinite dihedral Coxeter systems.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.reduced_cons_cons_ne`: [Dihedral.lean:93](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L93).

`OAI.KLInvariance.Dihedral.reduced_cons_eq_alt`: [Dihedral.lean:101](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L101).

`OAI.KLInvariance.Dihedral.reduced_eq_alt`: [Dihedral.lean:114](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L114).

`OAI.KLInvariance.Dihedral.exists_alt`: [Dihedral.lean:120](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L120).

`OAI.KLInvariance.Dihedral.reduced_alt_take`: [Dihedral.lean:127](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L127).

`OAI.KLInvariance.Dihedral.eq_alt_of_descent`: [Dihedral.lean:173](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L173).
