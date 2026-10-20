---
id: kl.dihedral.signed_counts
title: Signed label comparisons and finite later counts
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses: []
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.SignedDihedral.Before
  - OAI.KLInvariance.SignedDihedral.arrowAfter
  - OAI.KLInvariance.SignedDihedral.countAfter
  - OAI.KLInvariance.SignedDihedral.arrowAfter_of_not_lt
  - OAI.KLInvariance.SignedDihedral.arrowAfter_self
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:917
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.Before
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1046
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.arrowAfter
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1051
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.countAfter
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1055
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.arrowAfter_of_not_lt
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1058
    format: lean-location
    note: OAI.KLInvariance.SignedDihedral.arrowAfter_self
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the signed-coordinate, parity, length and finite-period hypotheses explicit?
  verdict: Read Before, arrowAfter and countAfter with their unrestricted integer
    arguments. Defined the zero-parameter behavior, length/parity/order tests, double
    internal ranks and singleton top, and evaluated a complete small indicator example.
    Kept the integer comparison separate from its later geometric identification.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Signed label comparisons and finite later counts

For signed label parameters \(a,b\in\mathbb Z\), define \(a\prec b\) by
\[
(a>0\land b>0\land a<b)
\quad\text{or}\quad
(a<0\land b<0\land a<b)
\quad\text{or}\quad
(a>0\land b<0).
\]
This is the source's Before relation. On nonzero integers it places positive parameters first, then negative parameters, with the usual increasing order within each sign. For example,
\[
1\prec3\prec-5\prec-1.
\]
When either parameter is zero, none of the defining clauses holds.

## The numerical arrow indicator

For \(i,q,z\in\mathbb Z\), define
\[
\operatorname{aft}(i,q,z)=
\begin{cases}
1,&|i|<|z|,\ i+z\text{ odd},\ q\prec i+z,\\
0,&\text{otherwise}.
\end{cases}
\]
This is arrowAfter. The first two conditions are the signed dihedral edge conditions; the third compares the edge's signed label with the threshold \(q\).

The construction is defined for every integer \(q\). In the edge comparison, \(q=i+j\) is the odd parameter of the current edge.

Strictness gives
\[
\operatorname{aft}(i,i+j,j)=0,
\]
because no parameter is Before itself. Also
\(\operatorname{aft}(i,q,0)=0\), since \(|i|\ge0\).

## The finite signed count

For a signed top \(c\), put \(C=|c|\), regarded as a natural number, and define
\[
\operatorname{cnt}(i,q,c)
=\sum_{0\le r<C}
 \bigl(\operatorname{aft}(i,q,r)+\operatorname{aft}(i,q,-r)\bigr)
+\operatorname{aft}(i,q,c).
\]
This is countAfter.

The formula has two signed positions at each internal rank and one prescribed top. The two zero-index terms are both zero. The [[node:kl.dihedral.lower_signed_sums|lower-interval signed-sum theorem]] supplies this pattern when actual group elements are translated to suitable signed representatives.

## A numerical example

Take \(i=0,q=3,c=3\). At internal rank one, the comparison \(3\prec1\) is false at the positive endpoint, while \(3\prec-1\) holds at the negative endpoint. Thus their contributions are \(0,1\). Rank two has even endpoint parity, so both contributions are zero. The top contributes zero by the strict self-comparison.

Hence
\[
\operatorname{cnt}(0,3,3)=1.
\]
Starting instead at \(i=3\) gives no endpoint of greater absolute length, so \(\operatorname{cnt}(3,3,3)=0\).

The [[node:kl.dihedral.signed_comparison_tables|signed-comparison theorem]] evaluates these indicators in general. The [[node:kl.dihedral.signed_residue_comparison|finite-residue comparison theorem]] relates the raw signed comparisons to the residue convention used for finite dihedral reflection labels.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit integer comparisons behind the midpoint table.**

**OpenAI notes:** The midpoint table compares the labels of edges at the two current endpoints. Infinite type uses the two signed blocks; finite type uses residues modulo 2m and the represented endpoint bounds to check the mixed-sign comparisons. [dih:midpoint-order](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L358), [dih:count](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L464).

**Lean (primary):** Before is an explicit relation on integers. The same-source and next-source formulas are proved under absolute-length inequalities. Separate finite_before lemmas identify residue comparison with Before only in those constrained configurations. arrowAfter then includes the length and parity tests. [DihedralIntervals:917](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L917), [DihedralIntervals:920](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L920), [DihedralIntervals:932](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L932), [DihedralIntervals:944](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L944), [DihedralIntervals:975](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L975), [DihedralIntervals:1001](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1001), [DihedralIntervals:1046](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1046).

**Role in the proof:** The Blueprint proves the sign and residue inequalities and keeps their hypotheses explicit. The actual root-slope identification uses the separate angular comparison lemmas.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.SignedDihedral.Before`: [DihedralIntervals.lean:917](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L917).

`OAI.KLInvariance.SignedDihedral.arrowAfter`: [DihedralIntervals.lean:1046](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1046).

`OAI.KLInvariance.SignedDihedral.countAfter`: [DihedralIntervals.lean:1051](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1051).

`OAI.KLInvariance.SignedDihedral.arrowAfter_of_not_lt`: [DihedralIntervals.lean:1055](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1055).

`OAI.KLInvariance.SignedDihedral.arrowAfter_self`: [DihedralIntervals.lean:1058](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1058).
