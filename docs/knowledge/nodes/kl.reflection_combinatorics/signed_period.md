---
id: kl.dihedral.signed_period
title: Periods and admissible representatives of signed words
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.signed_words
- kl.dihedral.signed_lengths
- kl.dihedral.good_indices
- kl.coxeter.dihedral_reduced_words
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.Dihedral.indexWord_add_even
  - OAI.KLInvariance.Dihedral.rotation_pow_max
  - OAI.KLInvariance.Dihedral.indexWord_period
  - OAI.KLInvariance.Dihedral.indexWord_mod_period
  - OAI.KLInvariance.Dihedral.maximal_or_unbounded
  - OAI.KLInvariance.Dihedral.max_length_positive
  - OAI.KLInvariance.Dihedral.goodIndex_nat
  - OAI.KLInvariance.Dihedral.goodIndex_neg_nat
  - OAI.KLInvariance.Dihedral.exists_good_index
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:752
    format: lean-location
    note: OAI.KLInvariance.Dihedral.indexWord_add_even
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:763
    format: lean-location
    note: OAI.KLInvariance.Dihedral.rotation_pow_max
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:779
    format: lean-location
    note: OAI.KLInvariance.Dihedral.indexWord_period
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:785
    format: lean-location
    note: OAI.KLInvariance.Dihedral.indexWord_mod_period
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1381
    format: lean-location
    note: OAI.KLInvariance.Dihedral.maximal_or_unbounded
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1396
    format: lean-location
    note: OAI.KLInvariance.Dihedral.max_length_positive
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1412
    format: lean-location
    note: OAI.KLInvariance.Dihedral.goodIndex_nat
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1419
    format: lean-location
    note: OAI.KLInvariance.Dihedral.goodIndex_neg_nat
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1425
    format: lean-location
    note: OAI.KLInvariance.Dihedral.exists_good_index
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the signed-coordinate, parity, length and finite-period hypotheses explicit?
  verdict: Read the even-shift identity, maximum-length rotation argument, period
    and remainder formulas, length dichotomy and exists_good_index repair. Preserved
    the generic period statement, explained the zero-modulus convention, and retained
    the explicit exclusion of the negative maximum.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Periods and admissible representatives of signed words

Let \(D\) be a Coxeter system with simple generators \(s,t\), length \(\ell\), rotation \(r=st\), and signed word values \(w_i\).

For all integers \(i,n\),
\[
w_{i+2n}=r^nw_i.
\]
If \(r^N=1\), \(N\in\mathbb N\), then
\[
w_{i+2Nk}=w_i\qquad(i,k\in\mathbb Z).
\]
Reduction modulo \(2N\) gives the same group value; for the zero modulus the source uses \(i\bmod0=i\).

If the system has a maximum-length element of length \(m\), then \(m>0\), \(r^m=1\), and \(w_{-m}=w_m\). Every element \(z\in D\), in both the bounded and unbounded cases, has an admissible signed representative \(i\) with \(w_i=z\) and \(|i|=\ell(z)\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The signed model constructed from word and length identities.**

**OpenAI notes:** The notes index the two alternating rays by positive and negative integers, use -m<i<=m in finite type, and obtain reflection labels as doubled midpoints i+j. The interval-shape lemma gives two vertices in each internal rank and a singleton top. [dih:shape](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L112), [dih:midpoint-order](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L358).

**Lean (primary):** indexWord evaluates rotation powers using Euclidean integer division. A diagram automorphism and reduced prefixes prove the length statements. A maximum length gives rotation period 2m, and GoodIndex selects the negative-open, positive-closed range. The internal-rank and signed-sum lemmas retain the zero-rank and singleton-top cases explicitly. [DihedralIntervals:41](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L41), [DihedralIntervals:709](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L709), [DihedralIntervals:90](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L90), [DihedralIntervals:763](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L763), [DihedralIntervals:1378](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1378), [ReflectionSchedules:1639](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1639), [DihedralIntervals:1341](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1341).

**Role in the proof:** The Blueprint separates integer parameters from their group values, and separates the vertex representative range from the odd reflection-label residues used in finite type.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Shift a coordinate by an even integer

The integers \(i\) and \(i+2n\) have the same parity, and
\[
\left\lfloor\frac{i+2n}{2}\right\rfloor
=\left\lfloor\frac i2\right\rfloor+n.
\]
Substitute in the two branches of the [[node:kl.dihedral.signed_words|signed-word definition]]. In either branch the new rotation power is \(r^n\) times the old one; the odd branch retains its final \(s\). Hence \(w_{i+2n}=r^nw_i\).

### Step 2. Use a rotation period

If \(r^N=1\), Step 1 with shift \(2Nk\) gives
\[
w_{i+2Nk}=r^{Nk}w_i=(r^N)^kw_i=w_i.
\]
For \(N>0\), write the Euclidean division
\(i=(i\bmod2N)+2Nq\). Applying the periodic identity gives
\(w_i=w_{i\bmod2N}\). For \(N=0\), the remainder convention makes this equality immediate.

### Step 3. Obtain the period from a maximum-length element

Let \(v\) have maximum length \(m\). Since a simple generator has length one, \(m\ge1\).

For either simple generator \(s_i\), maximality gives
\(\ell(s_iv)\le m\). Simple multiplication changes length by one, so it decreases length here. Thus both generators are left descents of \(v\).

The [[node:kl.coxeter.dihedral_reduced_words|reduced-alternating-word theorem]] with prescribed first letter gives
\[
v=w_m=w_{-m}.
\]
Step 1 at \(i=-m,n=m\) gives \(w_m=r^mw_{-m}\). Substitute equality of the two word values and cancel on the right. This proves \(r^m=1\).

### Step 4. Separate bounded and unbounded lengths

If lengths are bounded in \(\mathbb N\), their nonempty range is finite and has a maximum attained by some element. If they are unbounded, elements of arbitrarily large length exist, so there is no maximum-length element.

In the unbounded case every integer satisfies GoodIndex. Any signed representative of the correct length from the [[node:kl.dihedral.signed_lengths|signed-length theorem]] is therefore admissible.

### Step 5. Repair the endpoint in the bounded case

Choose a maximum length \(m\) and a signed representative \(i\) of \(z\) with \(|i|=\ell(z)\). Since \(\ell(z)\le m\),
\[
-m\le i\le m.
\]
If \(i\) is not already in the admissible range \((-m,m]\), it must be \(-m\).

Step 3 and the period \(2m\) give \(w_{-m}=w_m\). Replace \(i=-m\) by \(i=m\). This preserves the group value and absolute length. Because \(m>0\), the new index lies in \((-m,m]\).

All maximum-length elements have length \(m\), so this range verifies every clause of GoodIndex. The repaired index is the required admissible representative.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.indexWord_add_even`: [DihedralIntervals.lean:752](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L752).

`OAI.KLInvariance.Dihedral.rotation_pow_max`: [DihedralIntervals.lean:763](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L763).

`OAI.KLInvariance.Dihedral.indexWord_period`: [DihedralIntervals.lean:779](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L779).

`OAI.KLInvariance.Dihedral.indexWord_mod_period`: [DihedralIntervals.lean:785](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L785).

`OAI.KLInvariance.Dihedral.maximal_or_unbounded`: [DihedralIntervals.lean:1381](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1381).

`OAI.KLInvariance.Dihedral.max_length_positive`: [DihedralIntervals.lean:1396](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1396).

`OAI.KLInvariance.Dihedral.goodIndex_nat`: [DihedralIntervals.lean:1412](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1412).

`OAI.KLInvariance.Dihedral.goodIndex_neg_nat`: [DihedralIntervals.lean:1419](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1419).

`OAI.KLInvariance.Dihedral.exists_good_index`: [DihedralIntervals.lean:1425](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1425).
