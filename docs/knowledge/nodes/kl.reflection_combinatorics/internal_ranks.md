---
id: kl.dihedral.internal_ranks
title: Two elements and a unique descent at each internal rank
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.signed_words
- kl.dihedral.signed_lengths
- kl.coxeter.dihedral_reduced_words
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  - DyerPaths
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.Dihedral.two_elements_length
  - OAI.KLInvariance.Dihedral.unique_leftDescent
  - OAI.KLInvariance.Dihedral.leftDescent_alt
  - OAI.KLInvariance.Dihedral.indexWord_pos_ne_neg
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1639
    format: lean-location
    note: OAI.KLInvariance.Dihedral.two_elements_length
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1019
    format: lean-location
    note: OAI.KLInvariance.Dihedral.unique_leftDescent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:742
    format: lean-location
    note: OAI.KLInvariance.Dihedral.leftDescent_alt
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1281
    format: lean-location
    note: OAI.KLInvariance.Dihedral.indexWord_pos_ne_neg
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the signed-coordinate, parity, length and finite-period hypotheses explicit?
  verdict: Read two_elements_length, the exact unique_leftDescent proof through the
    two candidates, leftDescent_alt and indexWord_pos_ne_neg. Expanded the n+1 versus
    n-1 cancellation contradiction, exhaustive alternating forms, descent existence
    and the strict internal-rank hypothesis.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Two elements and a unique descent at each internal rank

Let \(D\) be a Coxeter system with simple generators \(s,t\), length \(\ell\) and signed word values \(w_i\). Suppose a natural number \(n\) and an element \(v\in D\) satisfy
\[
0<n<\ell(v).
\]
Then exactly two elements have length \(n\), namely \(w_n\) and \(w_{-n}\), and they are distinct.

Every element \(z\) of this length has exactly one simple left descent. The descent of \(w_n\) is \(s\), and that of \(w_{-n}\) is \(t\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The signed model constructed from word and length identities.**

**OpenAI notes:** The notes index the two alternating rays by positive and negative integers, use -m<i<=m in finite type, and obtain reflection labels as doubled midpoints i+j. The interval-shape lemma gives two vertices in each internal rank and a singleton top. [dih:shape](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L112), [dih:midpoint-order](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L358).

**Lean (primary):** indexWord evaluates rotation powers using Euclidean integer division. A diagram automorphism and reduced prefixes prove the length statements. A maximum length gives rotation period 2m, and GoodIndex selects the negative-open, positive-closed range. The internal-rank and signed-sum lemmas retain the zero-rank and singleton-top cases explicitly. [DihedralIntervals:41](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L41), [DihedralIntervals:709](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L709), [DihedralIntervals:90](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L90), [DihedralIntervals:763](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L763), [DihedralIntervals:1378](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1378), [ReflectionSchedules:1639](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1639), [DihedralIntervals:1341](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1341).

**Role in the proof:** The Blueprint separates integer parameters from their group values, and separates the vertex representative range from the odd reflection-label residues used in finite type.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Produce two reduced alternating candidates

Choose a reduced alternating word for \(v\), beginning with \(s_i\). Its prefixes of lengths \(n\) and \(n+1\) are reduced. Removing the first letter of the latter leaves a reduced alternating word of length \(n\) beginning with the other generator \(s_{\bar i}\).

Thus both alternating products of length \(n\), one with each first letter, have length \(n\).

### Step 2. Prove these candidates distinct

Suppose the two products of length \(n\) were equal. Let \(u_i(k)\) denote the alternating product of \(k\) letters beginning with \(s_i\). Then
\[
u_i(n+1)
=s_i u_{\bar i}(n)
=s_i u_i(n)
=u_{\bar i}(n-1).
\]
The last equality cancels the first two copies of \(s_i\); it uses \(n>0\).

The left side is a reduced prefix of \(v\), with length \(n+1\). The right side has a word of length \(n-1\), so its group length is at most \(n-1\). This is impossible. The candidates are therefore distinct.

### Step 3. Exhaust the rank

Every element of length \(n\) has a reduced alternating expression of that length. Its first letter is one of the two simple generators, so its product is one of the two candidates from Step 1.

The [[node:kl.dihedral.signed_words|signed-word identities]] identify these candidates as \(w_n,w_{-n}\). This proves the exact rank count.

### Step 4. Prove uniqueness of the left descent

An element \(z\) of positive length has a simple left descent: the first letter of any reduced expression cancels to a shorter word.

If both generators were descents, the [[node:kl.coxeter.dihedral_reduced_words|reduced-word theorem]] with prescribed first letter would identify \(z\) with both alternating products of length \(n\). Then every element of length \(n\) would equal \(z\), contradicting the two distinct elements from Steps 2–3. Hence the descent is unique.

### Step 5. Identify the descent on each ray

For \(w_n\), cancellation of the leading \(s\) leaves an alternating word of length \(n-1\), so \(s\) is a left descent. The corresponding calculation gives \(t\) as a descent of \(w_{-n}\).

Uniqueness proves the stated assignments. It also supplies the source's second way to see \(w_n\ne w_{-n}\): equality would give one internal-rank element both descents.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.two_elements_length`: [ReflectionSchedules.lean:1639](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1639).

`OAI.KLInvariance.Dihedral.unique_leftDescent`: [DyerPaths.lean:1019](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1019).

`OAI.KLInvariance.Dihedral.leftDescent_alt`: [DihedralIntervals.lean:742](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L742).

`OAI.KLInvariance.Dihedral.indexWord_pos_ne_neg`: [DihedralIntervals.lean:1281](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1281).
