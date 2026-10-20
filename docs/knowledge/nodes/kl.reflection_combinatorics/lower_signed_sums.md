---
id: kl.dihedral.lower_signed_sums
title: Rank fibers and signed sums in a dihedral lower interval
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.signed_words
- kl.dihedral.signed_lengths
- kl.dihedral.internal_ranks
- kl.coxeter.dihedral_bruhat_order
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.Dihedral.lower_length_fiber
  - OAI.KLInvariance.Dihedral.lower_zero_fiber
  - OAI.KLInvariance.Dihedral.lower_top_fiber
  - OAI.KLInvariance.Dihedral.sum_lower_signed
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1296
    format: lean-location
    note: OAI.KLInvariance.Dihedral.lower_length_fiber
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1316
    format: lean-location
    note: OAI.KLInvariance.Dihedral.lower_zero_fiber
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1326
    format: lean-location
    note: OAI.KLInvariance.Dihedral.lower_top_fiber
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1341
    format: lean-location
    note: OAI.KLInvariance.Dihedral.sum_lower_signed
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the signed-coordinate, parity, length and finite-period hypotheses explicit?
  verdict: Read all three fiber lemmas and the rank-partition proof of sum_lower_signed.
    Explained the two internal values, their distinctness, singleton top, zero-rank
    fiber and the exact f(1)=0 hypothesis that permits the doubled zero index.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Rank fibers and signed sums in a dihedral lower interval

Let \(D\) be a Coxeter system with simple generators \(s,t\), length \(\ell\) and signed word values \(w_i\). Fix \(c\in D\) and put \(C=\ell(c)\). The lower Bruhat interval has these rank fibers:

- the rank-zero fiber is \(\{1\}\);
- for \(0<n<C\), the rank-\(n\) fiber is \(\{w_n,w_{-n}\}\), with two distinct elements;
- the rank-\(C\) fiber is \(\{c\}\).

Consequently, for a function \(f:D\to M\) into an additive commutative monoid, with \(f(1)=0\),
\[
\sum_{z\le c}f(z)
=\sum_{0\le n<C}\bigl(f(w_n)+f(w_{-n})\bigr)+f(c).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The signed model constructed from word and length identities.**

**OpenAI notes:** The notes index the two alternating rays by positive and negative integers, use -m<i<=m in finite type, and obtain reflection labels as doubled midpoints i+j. The interval-shape lemma gives two vertices in each internal rank and a singleton top. [dih:shape](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L112), [dih:midpoint-order](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L358).

**Lean (primary):** indexWord evaluates rotation powers using Euclidean integer division. A diagram automorphism and reduced prefixes prove the length statements. A maximum length gives rotation period 2m, and GoodIndex selects the negative-open, positive-closed range. The internal-rank and signed-sum lemmas retain the zero-rank and singleton-top cases explicitly. [DihedralIntervals:41](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L41), [DihedralIntervals:709](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L709), [DihedralIntervals:90](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L90), [DihedralIntervals:763](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L763), [DihedralIntervals:1378](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1378), [ReflectionSchedules:1639](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1639), [DihedralIntervals:1341](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1341).

**Role in the proof:** The Blueprint separates integer parameters from their group values, and separates the vertex representative range from the odd reflection-label residues used in finite type.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Identify an internal rank fiber

Take \(n\in\mathbb N\) with \(n<C\). Any element below \(c\) of length \(n\) has an alternating expression beginning with \(s\) or \(t\), so it is \(w_n\) or \(w_{-n}\).

Conversely, the [[node:kl.dihedral.signed_lengths|signed-length theorem]] gives length \(n\) to both values, since the element \(c\) has greater length. The [[node:kl.coxeter.dihedral_bruhat_order|dihedral Bruhat comparison theorem]] then puts both below \(c\). This proves the fiber formula.

For \(n>0\), the [[node:kl.dihedral.internal_ranks|internal-rank theorem]] makes the two values distinct.

### Step 2. Identify the bottom and top fibers

Length zero characterizes the identity, and \(1\le c\), so the zero fiber is \(\{1\}\).

If \(z\le c\) and \(\ell(z)=\ell(c)\), strict length increase along a nontrivial Bruhat comparison forces \(z=c\). Thus the top fiber is \(\{c\}\).

### Step 3. Sum by rank

Suppose first that \(C>0\). The interval is finite, and every element in it has length between \(0\) and \(C\). Partition its sum into these rank fibers.

Every internal positive rank contributes \(f(w_n)+f(w_{-n})\). The top contributes \(f(c)\). The rank-zero fiber contributes \(f(1)=0\).

### Step 4. Include the zero index in the uniform formula

The displayed sum starts at \(n=0\), where \(w_0=w_{-0}=1\). Its contribution is \(f(1)+f(1)=0\), equal to the true rank-zero contribution.

This yields the stated uniform formula. If \(C=0\), the internal sum is empty and the top is \(c=1\), so the same identity holds.

For the relative later-edge indicator, the value at \(1\) is zero because no upward edge ends at length zero. Hence this signed-sum formula is the one used to pass from the actual lower interval to the numerical countAfter function.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.lower_length_fiber`: [DihedralIntervals.lean:1296](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1296).

`OAI.KLInvariance.Dihedral.lower_zero_fiber`: [DihedralIntervals.lean:1316](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1316).

`OAI.KLInvariance.Dihedral.lower_top_fiber`: [DihedralIntervals.lean:1326](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1326).

`OAI.KLInvariance.Dihedral.sum_lower_signed`: [DihedralIntervals.lean:1341](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1341).
