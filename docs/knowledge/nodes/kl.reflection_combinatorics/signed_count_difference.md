---
id: kl.dihedral.signed_count_difference
title: The signed later-count difference
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.signed_counts
- kl.dihedral.signed_comparison_tables
- kl.dihedral.parity_rank_counts
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.SignedDihedral.countAfter_base
  - OAI.KLInvariance.SignedDihedral.countAfter_pos_formula
  - OAI.KLInvariance.SignedDihedral.countAfter_neg_formula
  - OAI.KLInvariance.SignedDihedral.countAfter_next_formula
  - OAI.KLInvariance.SignedDihedral.countAfter_difference
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1537
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.countAfter_base
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1688
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.countAfter_pos_formula
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1718
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.countAfter_neg_formula
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1741
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.countAfter_next_formula
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1765
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.countAfter_difference
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the signed-coordinate, parity, length and finite-period hypotheses explicit?
  verdict: Read countAfter_base, all three closed formulas and countAfter_difference.
    Verified the exact top condition c=j or |j|<|c|, expanded the positive/negative
    lower counts and upper-source count through the two parity sums, and retained
    the singleton-top and empty intermediate-rank cases.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# The signed later-count difference

Let \(i,j,c\in\mathbb Z\), and define the natural numbers
\[
L=|i|,\qquad M=|j|,\qquad C=|c|.
\]
Assume
\[
L<M,\qquad L+M\text{ is odd},\qquad
c=j\text{ or }M<C.
\]
Set \(k=(M-L-1)/2\), a nonnegative integer, and write \([E]\) for the zero-or-one indicator of a condition \(E\). Then
\[
\begin{array}{c|cc}
 &\operatorname{cnt}(i,i+j,c)&\operatorname{cnt}(j,i+j,c)\\
j>0&k+(C-M)&C-M\\
j<0&k&0
\end{array}
\]
and therefore
\[
\operatorname{cnt}(i,i+j,c)
=\operatorname{cnt}(j,i+j,c)+k.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The same difference from separate nonnegative counts.**

**OpenAI notes:** The notes count the k intermediate contributions and, for the positive upper index, cancel the extra opposite endpoint against an alternating-sign tail sum. They then subtract the endpoint counts. [dih:count](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L464).

**Lean (primary):** The numerical proof evaluates both nonnegative counts separately. An explicit parity-rank bijection gives k; induction on the top rank evaluates total_outgoing_count and positiveCount. The sign cases give the two closed formulas, whose difference is k. [DihedralIntervals:1027](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1027), [DihedralIntervals:1563](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1563), [DihedralIntervals:1650](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1650), [DihedralIntervals:1688](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1688), [DihedralIntervals:1718](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1718), [DihedralIntervals:1741](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1741), [DihedralIntervals:1765](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1765).

**Role in the proof:** The Blueprint follows the finite bijection and both induction calculations, including the first extension past the reference rank and the top-equals-current-upper case.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Evaluate the case where the top is j

Suppose \(c=j\). The top contribution to the lower count is
\(\operatorname{aft}(i,i+j,j)=0\).

At an internal rank \(r<M\), the positive endpoint contributes zero by the [[node:kl.dihedral.signed_comparison_tables|signed-comparison formulas]], since it would require \(M<r\). The negative endpoint contributes one exactly when
\[
L<r,\qquad L+r\text{ is odd}.
\]
The condition \(r<M\) makes its remaining order clause true for either sign of \(j\).

The [[node:kl.dihedral.parity_rank_counts|parity-rank count theorem]] therefore gives
\[
\operatorname{cnt}(i,i+j,j)=k.
\]
The upper count is zero because none of its internal endpoints or its top has absolute length greater than \(M\).

### Step 2. Evaluate a positive upper index with a higher top

Assume \(j>0\) and \(C>M\). For an internal rank \(r<C\), the negative endpoint contributes one whenever \(L<r\) and \(L+r\) is odd. The positive endpoint contributes an additional one exactly when \(M<r\).

Thus the internal contribution is
\[
[L<r\text{ and }L+r\text{ odd}]\,(1+[M<r]).
\]
Because the top has absolute length \(C>M\), the [[node:kl.dihedral.signed_comparison_tables|far-endpoint formula]] gives its contribution as \([L+C\text{ odd}]\), regardless of the sign of \(c\).

These terms are exactly \(P(L,M,C)\). The [[node:kl.dihedral.parity_rank_counts|parity-rank count theorem]] gives
\[
\operatorname{cnt}(i,i+j,c)=k+(C-M).
\]
Together with Step 1, this proves the lower-count formula for every allowed top when \(j>0\).

### Step 3. Evaluate a negative upper index with a higher top

Assume \(j<0\) and \(C>M\). The positive internal endpoints all contribute zero. A negative internal endpoint contributes only when its rank satisfies \(r<M\), together with \(L<r\) and the odd parity condition.

Thus all ranks at or above \(M\) contribute zero. The [[node:kl.dihedral.signed_comparison_tables|far-endpoint formula]] also gives zero at the top. The remaining sum is precisely the internal sum from Step 1, equal to \(k\).

This proves the lower-count formula for \(j<0\).

### Step 4. Evaluate the count from the upper source

The [[node:kl.dihedral.signed_comparison_tables|next-source indicator formula]] gives
\[
\operatorname{aft}(j,i+j,z)=1
\quad\Longleftrightarrow\quad
M<|z|,\ M+|z|\text{ odd},\ j>0.
\]

If \(j<0\), every contribution is zero. If \(j>0\), the two internal endpoints and singleton top give exactly \(T(M,C)\). The top hypothesis implies \(M\le C\), so the [[node:kl.dihedral.parity_rank_counts|parity-rank count theorem]] gives \(T(M,C)=C-M\).

These are the upper-count formulas in the table.

### Step 5. Compare the two rows

Since \(M>L\ge0\), \(j\ne0\). The positive and negative cases exhaust the possibilities.

For \(j>0\), the counts are \(k+(C-M)\) and \(C-M\); for \(j<0\), they are \(k\) and zero. In either case the lower count equals the upper count plus \(k\), proving the identity.

For \(i=0,j=3,c=3\), the two counts are \(1,0\). For \(i=1,j=2,c=3\), they are \(1,1\). The second example has a covering length gap and hence correction exponent zero.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.SignedDihedral.countAfter_base`: [DihedralIntervals.lean:1537](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1537).

`OAI.KLInvariance.SignedDihedral.countAfter_pos_formula`: [DihedralIntervals.lean:1688](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1688).

`OAI.KLInvariance.SignedDihedral.countAfter_neg_formula`: [DihedralIntervals.lean:1718](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1718).

`OAI.KLInvariance.SignedDihedral.countAfter_next_formula`: [DihedralIntervals.lean:1741](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1741).

`OAI.KLInvariance.SignedDihedral.countAfter_difference`: [DihedralIntervals.lean:1765](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1765).
