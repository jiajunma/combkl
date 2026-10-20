---
id: kl.dihedral.signed_comparison_tables
title: Signed midpoint comparison formulas
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.signed_counts
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.SignedDihedral.before_same_source_pos
  - OAI.KLInvariance.SignedDihedral.before_same_source_neg
  - OAI.KLInvariance.SignedDihedral.before_next_source
  - OAI.KLInvariance.SignedDihedral.odd_add_natAbs
  - OAI.KLInvariance.SignedDihedral.odd_sub_natAbs
  - OAI.KLInvariance.SignedDihedral.odd_add_abs
  - OAI.KLInvariance.SignedDihedral.arrowAfter_pos
  - OAI.KLInvariance.SignedDihedral.arrowAfter_neg
  - OAI.KLInvariance.SignedDihedral.arrowAfter_next
  - OAI.KLInvariance.SignedDihedral.arrowAfter_far
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:920
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.before_same_source_pos
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:932
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.before_same_source_neg
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:944
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.before_next_source
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1455
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.odd_add_natAbs
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1464
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.odd_sub_natAbs
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1610
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.odd_add_abs
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1468
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.arrowAfter_pos
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1488
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.arrowAfter_neg
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1510
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.arrowAfter_next
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1628
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.arrowAfter_far
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the signed-coordinate, parity, length and finite-period hypotheses explicit?
  verdict: Read the three Before comparison proofs and the parity/arrowAfter specializations.
    Expanded all four sign combinations using the dominant absolute value, proved
    the parity conversion and retained the exact conjunctions in the positive, negative
    and next-source indicator formulas.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Signed midpoint comparison formulas

Let \(i,j\in\mathbb Z\) with \(|i|<|j|\), and put \(L=|i|\), \(M=|j|\).

For \(|i|<|z|\), the same-source comparisons are
\[
(i+j)\prec(i+z)\ \Longleftrightarrow
\begin{cases}
z<0\text{ or }j<z,&j>0,\\
z<0\text{ and }j<z,&j<0.
\end{cases}
\]
For \(|j|<|z|\), the next-source comparison is
\[
(i+j)\prec(j+z)\quad\Longleftrightarrow\quad j>0.
\]

Consequently, for \(r\in\mathbb N\), the numerical arrow indicators are given by the following conditions for value \(1\); otherwise their value is \(0\).

| Indicator | Conditions for value \(1\) |
|---|---|
| \(\operatorname{aft}(i,i+j,r)\) | \(L<r\), \(L+r\) odd, \(j>0\), \(M<r\) |
| \(\operatorname{aft}(i,i+j,-r)\) | \(L<r\), \(L+r\) odd, and \((j>0\text{ or }r<M)\) |
| \(\operatorname{aft}(j,i+j,z)\) | \(M<|z|\), \(M+|z|\) odd, \(j>0\) |

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit integer comparisons behind the midpoint table.**

**OpenAI notes:** The midpoint table compares the labels of edges at the two current endpoints. Infinite type uses the two signed blocks; finite type uses residues modulo 2m and the represented endpoint bounds to check the mixed-sign comparisons. [dih:midpoint-order](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L358), [dih:count](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L464).

**Lean (primary):** Before is an explicit relation on integers. The same-source and next-source formulas are proved under absolute-length inequalities. Separate finite_before lemmas identify residue comparison with Before only in those constrained configurations. arrowAfter then includes the length and parity tests. [DihedralIntervals:917](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L917), [DihedralIntervals:920](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L920), [DihedralIntervals:932](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L932), [DihedralIntervals:944](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L944), [DihedralIntervals:975](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L975), [DihedralIntervals:1001](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1001), [DihedralIntervals:1046](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1046).

**Role in the proof:** The Blueprint proves the sign and residue inequalities and keeps their hypotheses explicit. The actual root-slope identification uses the separate angular comparison lemmas.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Determine the signs of the label sums

If \(|i|<|j|\), then \(-|j|<i<|j|\). Therefore \(i+j\) has the same sign as \(j\).

Likewise, under \(|i|<|z|\), the sum \(i+z\) has the sign of \(z\). Under \(|j|<|z|\), the sum \(j+z\) has the sign of \(z\).

The dominant endpoints \(j,z\) in these statements are nonzero, so the two sign cases exhaust the possibilities.

### Step 2. Compare two labels from the same source

Suppose \(j>0\). If \(z<0\), the first label is positive and the second negative, so the Before relation holds. If \(z>0\), both are positive, and their comparison is
\(i+j<i+z\), equivalent to \(j<z\).

Suppose \(j<0\). A positive \(z\) gives a negative first label and positive second label, so the comparison is false. For negative \(z\), both labels are negative and the comparison again reduces to \(j<z\).

These four cases prove the first displayed formula.

### Step 3. Compare a label at the next source

Assume \(|j|<|z|\). If \(j>0,z<0\), the positive label precedes the negative one. If both \(j,z\) are positive, the comparison becomes \(i<z\), which follows from \(|i|<|j|<z\).

If \(j<0,z>0\), the comparison is false by the sign blocks. If both are negative, it would require \(i<z\). But
\[
z<-|j|<i,
\]
so that inequality is false. Thus the comparison holds exactly when \(j>0\).

### Step 4. Insert the length and parity tests

An integer and its absolute value have the same parity, because changing a sign changes it by an even integer. Therefore
\[
i+r\text{ odd}\ \Longleftrightarrow\ L+r\text{ odd},
\]
and the same holds for \(i-r\). Also \(j+z\) is odd exactly when \(M+|z|\) is odd.

For endpoint \(r\ge0\), Step 2 reduces the order condition to \(j>0\) and \(M<r\), once \(L<r\). For endpoint \(-r\), it reduces to \(j>0\) or \(r<M\). Combining these with the length and parity clauses of arrowAfter gives the first two rows.

Step 3 gives the last row in exactly the same way.

### Step 5. Evaluate an endpoint beyond the current upper rank

If \(|z|>M\), the first two rows show that
\[
\operatorname{aft}(i,i+j,z)=1
\quad\Longleftrightarrow\quad
L+|z|\text{ is odd and }j>0.
\]
For a positive endpoint the inequality \(M<|z|\) supplies the extra condition. For a negative endpoint it rules out \(|z|<M\), leaving only \(j>0\). This is arrowAfter_far, used for the singleton top in the count.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.SignedDihedral.before_same_source_pos`: [DihedralIntervals.lean:920](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L920).

`OAI.KLInvariance.SignedDihedral.before_same_source_neg`: [DihedralIntervals.lean:932](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L932).

`OAI.KLInvariance.SignedDihedral.before_next_source`: [DihedralIntervals.lean:944](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L944).

`OAI.KLInvariance.SignedDihedral.odd_add_natAbs`: [DihedralIntervals.lean:1455](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1455).

`OAI.KLInvariance.SignedDihedral.odd_sub_natAbs`: [DihedralIntervals.lean:1464](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1464).

`OAI.KLInvariance.SignedDihedral.odd_add_abs`: [DihedralIntervals.lean:1610](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1610).

`OAI.KLInvariance.SignedDihedral.arrowAfter_pos`: [DihedralIntervals.lean:1468](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1468).

`OAI.KLInvariance.SignedDihedral.arrowAfter_neg`: [DihedralIntervals.lean:1488](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1488).

`OAI.KLInvariance.SignedDihedral.arrowAfter_next`: [DihedralIntervals.lean:1510](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1510).

`OAI.KLInvariance.SignedDihedral.arrowAfter_far`: [DihedralIntervals.lean:1628](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1628).
