---
id: kl.dihedral.good_indices
title: Admissible signed vertex indices
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.signed_words
- kl.dihedral.signed_lengths
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.Dihedral.GoodIndex
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1378
    format: lean-location
    note: OAI.KLInvariance.Dihedral.GoodIndex
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the signed-coordinate, parity, length and finite-period hypotheses explicit?
  verdict: Read the exact universally quantified GoodIndex predicate. Explained its
    unbounded and bounded cases, distinguished the chosen vertex range from reflection-label
    parameters, and recorded the A2 duplicate top as an illustration of the period
    theorem.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Admissible signed vertex indices

Let \(D\) be a Coxeter system with simple generators \(s,t\), length \(\ell\), and signed word values \(w_i\). An integer \(i\) is an **admissible signed index** when, for every maximum-length element \(w\),
\[
-\ell(w)<i\le\ell(w).
\]
Here maximum-length means that \(\ell(z)\le\ell(w)\) for every \(z\in D\). This is the source's predicate GoodIndex.

If lengths are unbounded, there is no maximum-length element and the predicate holds for every integer.

If there is a maximum length \(m\), all maximum-length elements have that same length, and the condition is
\[
-m<i\le m.
\]
Thus the chosen range includes the positive endpoint \(m\).

## The longest vertex

The [[node:kl.dihedral.signed_period|period-and-representative theorem]] proves \(w_{-m}=w_m\). Both evaluate to the longest vertex, so the interval \((-m,m]\) records that vertex once.

The same theorem proves that every group element has a representative satisfying both GoodIndex and
\[
|i|=\ell(w_i).
\]
These two pieces of data are used in the finite angular comparison lemmas.

## The A2 example

For type \(A_2\), the maximum length is \(3\), and the braid relation gives
\[
w_{-3}=tst=sts=w_3.
\]
The admissible vertex representatives are
\[
-2,-1,0,1,2,3,
\]
with values \(ts,t,1,s,st,sts\).

An edge reflection uses the parameter \(i+j\). This parameter is subsequently reduced modulo \(2m\) in the finite root-order comparison. For example, the parameters \(3\) and \(-3\) represent the same reflection modulo \(6\) in type \(A_2\).

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

`OAI.KLInvariance.Dihedral.GoodIndex`: [DihedralIntervals.lean:1378](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1378).
