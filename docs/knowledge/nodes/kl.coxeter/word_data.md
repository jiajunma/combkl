---
id: kl.coxeter.word_data
title: Words, length, reflections, and inversion sequences
kind: definition
status: formalized
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses: []
lean:
  repository: openai-kl
  modules:
  - Coxeter
  declarations:
  - OAI.KLInvariance.CoxeterSupport.leftInvSeq_alternating_formula
  - OAI.KLInvariance.CoxeterSupport.wordAction_record
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Coxeter:92
    format: lean-location
    note: OAI.KLInvariance.CoxeterSupport.leftInvSeq_alternating_formula
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Coxeter:60
    format: lean-location
    note: OAI.KLInvariance.CoxeterSupport.wordAction_record
verification:
  definition: accepted
  proof: not_applicable
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

# Words, length, reflections, and inversion sequences

Fix a Coxeter system with group \(W\), simple generators \(s_i\), and Coxeter exponents \(m_{ij}\). A word \(\omega=(i_1,\ldots,i_n)\) has product
\[
w(\omega)=s_{i_1}\cdots s_{i_n}.
\]
The empty word has product \(1\). Every group element has a word expression. The length \(\ell(w)\) is the smallest number of letters in such an expression, and \(\omega\) is reduced when \(n=\ell(w(\omega))\).

The defining relations are \(s_i^2=1\) and \((s_is_j)^{m_{ij}}=1\) for finite \(m_{ij}\). An infinite exponent imposes no relation on that pair. No finiteness of the set of generators is needed for these word constructions.

## Reflections and descents

A reflection is an element \(t=us_iu^{-1}\), with \(u\in W\). Its square is
\[
t^2=us_i(u^{-1}u)s_iu^{-1}=1.
\]
A left descent of \(w\) is a simple generator \(s_i\) for which \(\ell(s_iw)<\ell(w)\); a right descent satisfies \(\ell(ws_i)<\ell(w)\).

A left inversion of \(w\) is a reflection \(t\) satisfying \(\ell(tw)<\ell(w)\). The set of left inversions contains the left descents and can contain reflections that are not simple.

## Length changes under multiplication

Appending \(s_i\) to a reduced word for \(w\) gives \(\ell(ws_i)\le\ell(w)+1\). Applying the same argument to \(ws_i\), whose product with \(s_i\) is \(w\), gives \(\ell(w)\le\ell(ws_i)+1\).

Every Coxeter relation has even word length. Sending each simple generator to \(-1\) therefore defines a homomorphism \(W\to\{1,-1\}\). A word of length \(n\) has image \((-1)^n\), so multiplication by a simple generator changes the parity of length. Combining this parity change with the two inequalities gives
\[
\ell(ws_i)=\ell(w)+1\quad\text{or}\quad\ell(ws_i)=\ell(w)-1.
\]
The same argument applies on the left. Reversing a word gives a word for its inverse, and applying this twice proves \(\ell(w^{-1})=\ell(w)\).

A reflection, being a conjugate of a simple generator, also has sign \(-1\). Thus \(\ell(tw)-\ell(w)\) is odd for every reflection \(t\). This difference can have magnitude greater than one, as occurs for non-cover reflection edges.

## The left inversion sequence of a word

Write \(u_j=s_{i_1}\cdots s_{i_j}\), with \(u_0=1\). The left inversion sequence is the ordered list
\[
t_j=u_{j-1}s_{i_j}u_{j-1}^{-1},\qquad 1\le j\le n.
\]
Each entry is a reflection. It is attached to a position in the word, so repeated labels are counted with their multiplicities.

For a fixed position, write the word product as \(w=u_{j-1}s_{i_j}v\). Then
\[
t_jw
=u_{j-1}s_{i_j}u_{j-1}^{-1}u_{j-1}s_{i_j}v
=u_{j-1}v.
\]
Thus left multiplication by the position's reflection deletes that letter from the word.

If the original word is reduced, the deleted expression has \(n-1\) letters. Hence \(\ell(t_jw)\le n-1<\ell(w)\), so every entry is a left inversion. Strong exchange proves that every left inversion occurs in the sequence of the supplied reduced word.

## Two examples

For \(\omega=(i,i)\), the product is \(1\), and the sequence is \((s_i,s_i)\). The two occurrences will cancel when their multiplicity is read modulo two.

For a pair \(s,t\) with \(m_{st}=3\), the reduced word \((s,t,s)\) has inversion sequence
\[
(s,\ sts,\ t).
\]
For the third entry, the formula gives \(ststs=t\), using \(sts=tst\) and \(s^2=t^2=1\). The three entries describe the three left inversions of its product.

## References

The local declarations below give the construction and its word calculations.

## Lean formalization

`OAI.KLInvariance.CoxeterSupport.leftInvSeq_alternating_formula`: [Coxeter.lean:92](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Coxeter.lean#L92).

`OAI.KLInvariance.CoxeterSupport.wordAction_record`: [Coxeter.lean:60](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Coxeter.lean#L60).

The local proofs use the imported Coxeter-system operations `wordProd`, `length`, `IsReduced`, and `leftInvSeq`. The displayed sequence uses positions 1 through n; the source list operations use positions 0 through n-1.
