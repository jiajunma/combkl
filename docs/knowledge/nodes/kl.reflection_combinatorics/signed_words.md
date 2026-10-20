---
id: kl.dihedral.signed_words
title: Signed coordinates for the two alternating rays
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.coxeter.alternating_words
- kl.coxeter.word_data
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.Dihedral.rotation
  - OAI.KLInvariance.Dihedral.indexWord
  - OAI.KLInvariance.Dihedral.indexWord_even
  - OAI.KLInvariance.Dihedral.indexWord_odd
  - OAI.KLInvariance.Dihedral.indexWord_nat
  - OAI.KLInvariance.Dihedral.indexWord_neg_nat
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:24
    format: lean-location
    note: OAI.KLInvariance.Dihedral.rotation
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:41
    format: lean-location
    note: OAI.KLInvariance.Dihedral.indexWord
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:45
    format: lean-location
    note: OAI.KLInvariance.Dihedral.indexWord_even
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:48
    format: lean-location
    note: OAI.KLInvariance.Dihedral.indexWord_odd
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:53
    format: lean-location
    note: OAI.KLInvariance.Dihedral.indexWord_nat
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:63
    format: lean-location
    note: OAI.KLInvariance.Dihedral.indexWord_neg_nat
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the signed-coordinate, parity, length and finite-period hypotheses explicit?
  verdict: Read rotation and indexWord with Euclidean integer division, then both
    parity formulas and the positive/negative alternating-word identities. Distinguished
    the integer coordinate from the evaluated group element and worked out the negative
    odd exponent explicitly.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Signed coordinates for the two alternating rays

Let \(D\) be a Coxeter system with simple generators \(s,t\), corresponding to the source's indices false and true. Put
\[
r=st.
\]
For an integer \(i\), define its **signed word value**
\[
w_i=
\begin{cases}
r^{\,i/2},&i\text{ is even},\\
r^{\,\lfloor i/2\rfloor}s,&i\text{ is odd}.
\end{cases}
\]
The source calls \(r\) rotation and this function indexWord. Integer division is Euclidean division, so
\[
w_{2n}=r^n,\qquad w_{2n+1}=r^ns\qquad(n\in\mathbb Z).
\]

The parameter \(i\) is an integer, while \(w_i\) is a group element. The following initial values display the two alternating rays.

| \(i\) | \(-3\) | \(-2\) | \(-1\) | \(0\) | \(1\) | \(2\) | \(3\) |
|---|---|---|---|---|---|---|---|
| \(w_i\) | \(tst\) | \(ts\) | \(t\) | \(1\) | \(s\) | \(st\) | \(sts\) |

## Positive and negative indices

For \(n\ge0\), \(w_n\) is the product of the alternating word of \(n\) letters beginning with \(s\). For \(w_{-n}\), it begins with \(t\).

For even \(n=2k\), this follows from \(r^k=(st)^k\) and \(r^{-k}=(ts)^k\). For odd \(n=2k+1\),
\[
w_n=(st)^ks.
\]
The negative odd index is \(-n=2(-k-1)+1\), so
\[
w_{-n}=r^{-k-1}s=(ts)^kt.
\]
The last equality uses \(r^{-1}s=tss=t\).

Thus the same integer formula evaluates both alternating rays. The [[node:kl.dihedral.signed_lengths|signed-length theorem]] determines when these words are reduced. The [[node:kl.dihedral.signed_period|period theorem]] describes the repeated values when the group has a longest element.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The signed model constructed from word and length identities.**

**OpenAI notes:** The notes index the two alternating rays by positive and negative integers, use -m<i<=m in finite type, and obtain reflection labels as doubled midpoints i+j. The interval-shape lemma gives two vertices in each internal rank and a singleton top. [dih:shape](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L112), [dih:midpoint-order](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L358).

**Lean (primary):** indexWord evaluates rotation powers using Euclidean integer division. A diagram automorphism and reduced prefixes prove the length statements. A maximum length gives rotation period 2m, and GoodIndex selects the negative-open, positive-closed range. The internal-rank and signed-sum lemmas retain the zero-rank and singleton-top cases explicitly. [DihedralIntervals:41](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L41), [DihedralIntervals:709](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L709), [DihedralIntervals:90](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L90), [DihedralIntervals:763](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L763), [DihedralIntervals:1378](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1378), [ReflectionSchedules:1639](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1639), [DihedralIntervals:1341](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1341).

**Role in the proof:** The Blueprint separates integer parameters from their group values, and separates the vertex representative range from the odd reflection-label residues used in finite type.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.rotation`: [DihedralIntervals.lean:24](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L24).

`OAI.KLInvariance.Dihedral.indexWord`: [DihedralIntervals.lean:41](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L41).

`OAI.KLInvariance.Dihedral.indexWord_even`: [DihedralIntervals.lean:45](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L45).

`OAI.KLInvariance.Dihedral.indexWord_odd`: [DihedralIntervals.lean:48](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L48).

`OAI.KLInvariance.Dihedral.indexWord_nat`: [DihedralIntervals.lean:53](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L53).

`OAI.KLInvariance.Dihedral.indexWord_neg_nat`: [DihedralIntervals.lean:63](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L63).
