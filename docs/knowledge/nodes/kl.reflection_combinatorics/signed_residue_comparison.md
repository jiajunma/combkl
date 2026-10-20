---
id: kl.dihedral.signed_residue_comparison
title: Finite residue comparisons at incident signed edges
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
  - OAI.KLInvariance.SignedDihedral.midpoint_mod
  - OAI.KLInvariance.SignedDihedral.finite_before_same
  - OAI.KLInvariance.SignedDihedral.finite_before_next
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:965
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.midpoint_mod
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:975
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.finite_before_same
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1001
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.finite_before_next
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the signed-coordinate, parity, length and finite-period hypotheses explicit?
  verdict: Read midpoint_mod and both finite_before proofs. Expanded the strict range
    bounds, same-sign shifts and both mixed-sign inequalities. Retained GoodIndex-style
    bounds on both upper endpoints for the same-source result, but only on z for the
    next-source result, and kept the statement as a constrained residue comparison.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Finite residue comparisons at incident signed edges

Let \(m\) be a positive integer and \(i,j,z\in\mathbb Z\).

If
\[
|i|<|j|,\qquad |i|<|z|,\qquad
-m<j\le m,\quad -m<z\le m,
\]
then
\[
(i+j)\bmod2m<(i+z)\bmod2m
\quad\Longleftrightarrow\quad
(i+j)\prec(i+z).
\]

If instead
\[
|i|<|j|<|z|,\qquad -m<z\le m,
\]
then
\[
(i+j)\bmod2m<(j+z)\bmod2m
\quad\Longleftrightarrow\quad
(i+j)\prec(j+z).
\]

These are the two residue comparisons used for outgoing edges at the same vertex and at successive vertices.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit integer comparisons behind the midpoint table.**

**OpenAI notes:** The midpoint table compares the labels of edges at the two current endpoints. Infinite type uses the two signed blocks; finite type uses residues modulo 2m and the represented endpoint bounds to check the mixed-sign comparisons. [dih:midpoint-order](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L358), [dih:count](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L464).

**Lean (primary):** Before is an explicit relation on integers. The same-source and next-source formulas are proved under absolute-length inequalities. Separate finite_before lemmas identify residue comparison with Before only in those constrained configurations. arrowAfter then includes the length and parity tests. [DihedralIntervals:917](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L917), [DihedralIntervals:920](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L920), [DihedralIntervals:932](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L932), [DihedralIntervals:944](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L944), [DihedralIntervals:975](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L975), [DihedralIntervals:1001](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1001), [DihedralIntervals:1046](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1046).

**Role in the proof:** The Blueprint proves the sign and residue inequalities and keeps their hypotheses explicit. The actual root-slope identification uses the separate angular comparison lemmas.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Write the remainder in the needed range

For \(-2m<a<2m\),
\[
a\bmod2m=
\begin{cases}
a,&a\ge0,\\
a+2m,&a<0.
\end{cases}
\]
In the first case \(a\) already lies in \([0,2m)\). In the second, \(a+2m\) lies there and differs from \(a\) by the modulus. This is midpoint_mod.

### Step 2. Bound and identify the signs of the same-source sums

In the first statement, \(|j|,|z|\le m\) and \(|i|<m\). Hence both sums \(i+j,i+z\) lie strictly between \(-2m\) and \(2m\).

The first has the sign of \(j\), and the second has the sign of \(z\), by dominance of the larger absolute value.

### Step 3. Compare sums of the same sign

If both sums are positive, Step 1 leaves both unchanged. If both are negative, it adds \(2m\) to both. In either case the remainder comparison is exactly their ordinary comparison, which is the Before relation within that sign block.

### Step 4. Compare opposite signs at the same source

If \(j>0,z<0\), the Before relation holds. The remainder inequality is
\[
i+j<i+z+2m,
\]
equivalent to \(j-z<2m\). This follows from \(j\le m\) and \(z>-m\).

If \(j<0,z>0\), Before is false. The opposite inequality follows from
\(z-j<2m\), using \(z\le m\) and \(j>-m\); thus
\(i+j+2m>i+z\), and the proposed strict comparison is also false.

This proves the first statement.

### Step 5. Compare the next-source sums

For the second statement, the bounds on \(z\) and
\(|i|<|j|<|z|\) imply \(|i|,|j|<m\). Both sums again lie in \((-2m,2m)\), with signs given by \(j,z\).

For equal signs, Step 3 applies. If \(j>0,z<0\), the required residue inequality is
\[
i+j<j+z+2m,
\]
equivalent to \(i-z<2m\). This follows from \(i<m\) and \(z>-m\).

If \(j<0,z>0\), the proposed residue comparison is false because
\(z-i<2m\), from \(z\le m\) and \(i>-m\). This agrees with the false Before comparison.

These cases prove the second statement.

In a finite dihedral system, admissible vertex indices supply the displayed bounds, while reflection labels use the residue of their odd endpoint sum. The theorem is the exact connection between that finite residue convention and the raw signed comparison in the two incident-edge configurations.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.SignedDihedral.midpoint_mod`: [DihedralIntervals.lean:965](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L965).

`OAI.KLInvariance.SignedDihedral.finite_before_same`: [DihedralIntervals.lean:975](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L975).

`OAI.KLInvariance.SignedDihedral.finite_before_next`: [DihedralIntervals.lean:1001](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1001).
