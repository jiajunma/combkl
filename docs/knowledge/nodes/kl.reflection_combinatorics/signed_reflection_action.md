---
id: kl.dihedral.signed_reflection_action
title: Reflection action and labels in signed coordinates
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.signed_words
- kl.dihedral.signed_lengths
- kl.dihedral.odd_reflection_edges
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.Dihedral.simple_rotation
  - OAI.KLInvariance.Dihedral.simple_rotation_zpow
  - OAI.KLInvariance.Dihedral.indexWord_reflection_mul
  - OAI.KLInvariance.Dihedral.indexWord_label
  - OAI.KLInvariance.Dihedral.index_step_iff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:26
    format: lean-location
    note: OAI.KLInvariance.Dihedral.simple_rotation
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:31
    format: lean-location
    note: OAI.KLInvariance.Dihedral.simple_rotation_zpow
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:90
    format: lean-location
    note: OAI.KLInvariance.Dihedral.indexWord_reflection_mul
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:112
    format: lean-location
    note: OAI.KLInvariance.Dihedral.indexWord_label
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1792
    format: lean-location
    note: OAI.KLInvariance.Dihedral.index_step_iff
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the signed-coordinate, parity, length and finite-period hypotheses explicit?
  verdict: Read both parity cases of indexWord_reflection_mul, the right-cancellation
    proof of indexWord_label and index_step_iff. Preserved group equality for arbitrary
    integer indices, and retained the reduced-length hypotheses for the edge criterion
    rather than assigning length |i| to every index.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Reflection action and labels in signed coordinates

Let \(D\) be a Coxeter system with simple generators \(s,t\), length \(\ell\), rotation \(r=st\) and signed word values \(w_i\). For every odd integer \(q\) and every \(i\in\mathbb Z\),
\[
w_qw_i=w_{q-i}.
\]
Consequently, if \(i+j\) is odd,
\[
w_jw_i^{-1}=w_{i+j}.
\]

If the two signed words have their indicated lengths,
\(\ell(w_i)=|i|\) and \(\ell(w_j)=|j|\), then
\[
w_i\to w_j
\quad\Longleftrightarrow\quad
|i|<|j|\text{ and }i+j\text{ is odd}.
\]
The left reflection label of this edge is \(w_{i+j}\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The signed model constructed from word and length identities.**

**OpenAI notes:** The notes index the two alternating rays by positive and negative integers, use -m<i<=m in finite type, and obtain reflection labels as doubled midpoints i+j. The interval-shape lemma gives two vertices in each internal rank and a singleton top. [dih:shape](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L112), [dih:midpoint-order](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L358).

**Lean (primary):** indexWord evaluates rotation powers using Euclidean integer division. A diagram automorphism and reduced prefixes prove the length statements. A maximum length gives rotation period 2m, and GoodIndex selects the negative-open, positive-closed range. The internal-rank and signed-sum lemmas retain the zero-rank and singleton-top cases explicitly. [DihedralIntervals:41](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L41), [DihedralIntervals:709](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L709), [DihedralIntervals:90](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L90), [DihedralIntervals:763](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L763), [DihedralIntervals:1378](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1378), [ReflectionSchedules:1639](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1639), [DihedralIntervals:1341](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1341).

**Role in the proof:** The Blueprint separates integer parameters from their group values, and separates the vertex representative range from the odd reflection-label residues used in finite type.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Conjugate the rotation by a simple generator

Since \(s^2=t^2=1\),
\[
srs=s(st)s=ts=r^{-1}.
\]
Conjugation preserves integer powers, so
\[
sr^ns=r^{-n},\qquad sr^n=r^{-n}s
\]
for every \(n\in\mathbb Z\). This is simple_rotation_zpow.

### Step 2. Multiply at an even signed coordinate

Write \(q=2k+1\). If \(i=2l\), the signed formulas give
\[
w_qw_i=r^ksr^l=r^{k-l}s
=w_{2(k-l)+1}=w_{q-i}.
\]

### Step 3. Multiply at an odd signed coordinate

If \(i=2l+1\), the same calculation gives
\[
w_qw_i=r^ksr^ls=r^{k-l}
=w_{2(k-l)}=w_{q-i}.
\]
The even and odd cases cover every integer coordinate.

An odd signed word value is the product of an odd alternating word, so the [[node:kl.dihedral.odd_reflection_edges|odd-reflection theorem]] makes it a reflection. The displayed equality expresses its action through evaluated signed coordinates.

### Step 4. Recover the edge label

Take \(q=i+j\), which is odd. The first formula gives
\[
w_{i+j}w_i=w_j.
\]
Multiply on the right by \(w_i^{-1}\) to obtain
\(w_jw_i^{-1}=w_{i+j}\). Thus the signed reflection parameter is the sum of the two endpoint indices. The average of \(i\) and its reflected index \(q-i\) is \(q/2\), so \(q\) is their doubled midpoint on the signed index line.

### Step 5. Verify the edge criterion

The [[node:kl.dihedral.odd_reflection_edges|dihedral edge criterion]] says that an edge exists exactly when length increases by an odd amount. Under the stated reduced-length equalities, this means
\[
|i|<|j|,\qquad |j|-|i|\text{ is odd}.
\]
An integer and its absolute value have the same parity. Also a difference and the corresponding sum have the same parity. Hence the second condition is equivalent to \(i+j\) being odd.

This proves the criterion with its exact length hypotheses. In a periodic signed representation, the group equalities of Steps 2–4 hold before choosing the vertex representatives used for the length comparisons.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.simple_rotation`: [DihedralIntervals.lean:26](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L26).

`OAI.KLInvariance.Dihedral.simple_rotation_zpow`: [DihedralIntervals.lean:31](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L31).

`OAI.KLInvariance.Dihedral.indexWord_reflection_mul`: [DihedralIntervals.lean:90](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L90).

`OAI.KLInvariance.Dihedral.indexWord_label`: [DihedralIntervals.lean:112](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L112).

`OAI.KLInvariance.Dihedral.index_step_iff`: [DihedralIntervals.lean:1792](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1792).
