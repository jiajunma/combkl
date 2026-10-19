---
id: kl.coxeter.dihedral_bruhat_order
title: Bruhat comparison by length in a dihedral system
kind: theorem
status: proved
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.coxeter.dihedral_reduced_words
- kl.foundations.subword
- kl.foundations.bruhat_order
lean:
  repository: openai-kl
  modules:
  - Dihedral
  declarations:
  - OAI.KLInvariance.Dihedral.shorter_bruhat
  - OAI.KLInvariance.Dihedral.bruhat_iff_length_lt_or_eq
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:144
    format: lean-location
    note: OAI.KLInvariance.Dihedral.shorter_bruhat
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:162
    format: lean-location
    note: OAI.KLInvariance.Dihedral.bruhat_iff_length_lt_or_eq
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the reduced-word, coefficient and interval
    hypotheses?
  verdict: Read shorter_bruhat and bruhat_iff_length_lt_or_eq. Both first-letter cases
    are realized as explicit prefixes or tail-prefixes before invoking the fixed reduced-subword
    criterion.
tags:
- Kazhdan-Lusztig
- dihedral
---

# Bruhat comparison by length in a dihedral system

In a Coxeter system with two simple generators,
\[
x\le w\quad\Longleftrightarrow\quad \ell(x)<\ell(w)\ \text{or}\ x=w.
\]
In particular every strictly shorter element lies below every longer element.

*Proof.*

### Step 1. Choose reduced alternating expressions

Assume \(\ell(x)=k<n=\ell(w)\). The [[node:kl.coxeter.dihedral_reduced_words|reduced-word theorem]] gives
\[
x=\operatorname{prod}\omega_j(k),\qquad
w=\operatorname{prod}\omega_i(n).
\]
The word for \(w\) is reduced, and \(n\ge1\).

### Step 2. Locate the shorter expression as a subword

If \(j=i\), the list \(\omega_j(k)\) is the first \(k\) letters of \(\omega_i(n)\), since \(k<n\).

If \(j\ne i\), there are exactly two generators, so \(j=\bar i\). Deleting the first letter of \(\omega_i(n)\) leaves \(\omega_{\bar i}(n-1)\). Since \(k\le n-1\), the first \(k\) letters of this tail are \(\omega_j(k)\).

In both cases the reduced expression for \(x\) occurs as a subword of the fixed reduced expression for \(w\).

### Step 3. Apply the subword criterion

The [[node:kl.foundations.subword|reduced-subword criterion]] now gives \(x\le w\). This proves the implication from strict length inequality.

Equality \(x=w\) gives comparison by reflexivity. Conversely, if \(x\le w\) and \(x\ne w\), strict Bruhat length monotonicity gives \(\ell(x)<\ell(w)\). Together these prove the equivalence.

### Step 4. Describe a lower interval

The lower ideal of \(w\) therefore consists of every element of length strictly less than \(\ell(w)\), together with \(w\) itself. Distinct elements of the same length are incomparable.

For a reduced word \(st\), this gives \([1,st]=\{1,s,t,st\}\). For a reduced word \(sts\), it gives the identity, both simple elements, both length-two elements, and the chosen length-three top. In type \(A_2\), that top also has the reduced expression \(tst\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.shorter_bruhat`: [Dihedral.lean:144](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L144).

`OAI.KLInvariance.Dihedral.bruhat_iff_length_lt_or_eq`: [Dihedral.lean:162](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L162).
