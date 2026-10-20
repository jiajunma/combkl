---
id: kl.dihedral.parity_rank_counts
title: Parity sums on doubled internal ranks
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses: []
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.SignedDihedral.eligible_ranks_card
  - OAI.KLInvariance.SignedDihedral.total_outgoing_count
  - OAI.KLInvariance.SignedDihedral.positiveCount
  - OAI.KLInvariance.SignedDihedral.positiveCount_formula
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1027
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.eligible_ranks_card
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1563
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.total_outgoing_count
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1646
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.positiveCount
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1650
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.positiveCount_formula
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the signed-coordinate, parity, length and finite-period hypotheses explicit?
  verdict: Read eligible_ranks_card and both Nat.le_induction proofs total_outgoing_count/positiveCount_formula.
    Expanded the explicit rank bijection, both base cases, the first step at the lower
    boundary, and both parity changes at every later step. Kept all natural-number
    inequalities and the odd-gap hypothesis.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Parity sums on doubled internal ranks

For a condition \(E\), write \([E]=1\) when it holds and \(0\) otherwise. Let \(L,M,C\) be natural numbers.

Define the double-rank count
\[
T(L,C)=
\sum_{0\le r<C}2[L<r\text{ and }L+r\text{ odd}]
+[L<C\text{ and }L+C\text{ odd}],
\]
and the positive-endpoint count
\[
P(L,M,C)=
\sum_{0\le r<C}[L<r\text{ and }L+r\text{ odd}]\,(1+[M<r])
+[M<C\text{ and }L+C\text{ odd}].
\]
The factor \(1+[M<r]\) is one through rank \(M\) and two above it. The source names the second expression positiveCount.

Then \(T(L,C)=C-L\) whenever \(L\le C\). If \(L<M\), \(L+M\) is odd and \(M\le C\), put \(k=(M-L-1)/2\). Then
\[
\#\{r:L<r<M,\ L+r\text{ odd}\}=k,
\qquad
P(L,M,C)=k+(C-M).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The same difference from separate nonnegative counts.**

**OpenAI notes:** The notes count the k intermediate contributions and, for the positive upper index, cancel the extra opposite endpoint against an alternating-sign tail sum. They then subtract the endpoint counts. [dih:count](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L464).

**Lean (primary):** The numerical proof evaluates both nonnegative counts separately. An explicit parity-rank bijection gives k; induction on the top rank evaluates total_outgoing_count and positiveCount. The sign cases give the two closed formulas, whose difference is k. [DihedralIntervals:1027](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1027), [DihedralIntervals:1563](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1563), [DihedralIntervals:1650](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1650), [DihedralIntervals:1688](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1688), [DihedralIntervals:1718](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1718), [DihedralIntervals:1741](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1741), [DihedralIntervals:1765](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1765).

**Role in the proof:** The Blueprint follows the finite bijection and both induction calculations, including the first extension past the reference rank and the top-equals-current-upper case.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Count the eligible ranks between L and M

Since \(M-L\) is positive and odd, write
\[
M=L+2k+1.
\]
The map
\[
a\longmapsto L+1+2a,\qquad 0\le a<k,
\]
takes values strictly between \(L\) and \(M\), with \(L+r\) odd, and is injective.

Conversely, an eligible \(r\) has \(r-L\) positive and odd, so
\(a=(r-L-1)/2\) is a natural number and \(r=L+1+2a\). The bound \(r<M\) gives \(a<k\). Thus this is a bijection, proving the first count. The case \(k=0\) has no eligible rank.

### Step 2. Begin the induction for the double-rank count

At \(C=L\), no internal rank is strictly above \(L\), and the top is not strictly above \(L\). Thus \(T(L,L)=0\).

We show that increasing \(C\) by one increases \(T\) by exactly one.

### Step 3. Check every step of that induction

For the first step \(C=L\), the newly internal rank \(L\) contributes zero. The new top \(L+1\) has opposite parity to \(L\), so it contributes one.

Now assume \(C>L\). All older internal ranks stay unchanged. If \(L+C\) is odd, the old top contributes one, its new internal pair contributes two, and the new top \(C+1\) contributes zero. The net increase is \(2-1=1\).

If \(L+C\) is even, the old top and its new internal pair both contribute zero, while the new top contributes one. The increase is again one.

Induction gives \(T(L,C)=C-L\).

### Step 4. Begin the induction for the positive-endpoint count

At \(C=M\), every internal rank has \(r<M\), so its weight is one, and the top term is zero. Therefore
\[
P(L,M,M)=\#\{r:L<r<M,\ L+r\text{ odd}\}=k
\]
by Step 1.

### Step 5. Check the first extension past M

On passing from \(C=M\) to \(C=M+1\), rank \(M\) becomes internal. It is eligible because \(L<M\) and \(L+M\) is odd, and its weight is one.

The old top contributed zero. The new top has \(L+M+1\) even, so it contributes zero. The total increase is one.

### Step 6. Check every later extension

For \(C>M\), the newly internal rank \(C\) has weight two. If \(L+C\) is odd, its old top contribution is one, its internal contribution is two, and the next top contributes zero. If \(L+C\) is even, those first two contributions are zero and the next top contributes one.

Thus every subsequent extension again increases the count by one. Starting from Step 4 gives
\[
P(L,M,C)=k+(C-M).
\]

For example, \(L=0,M=3,C=5\) gives \(k=1\), \(P=3\), and \(T(3,5)=2\). The lower positive count receives one contribution below rank \(3\), one from the opposite endpoint at rank \(3\), and one from the singleton top at rank \(5\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.SignedDihedral.eligible_ranks_card`: [DihedralIntervals.lean:1027](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1027).

`OAI.KLInvariance.SignedDihedral.total_outgoing_count`: [DihedralIntervals.lean:1563](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1563).

`OAI.KLInvariance.SignedDihedral.positiveCount`: [DihedralIntervals.lean:1646](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1646).

`OAI.KLInvariance.SignedDihedral.positiveCount_formula`: [DihedralIntervals.lean:1650](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1650).
