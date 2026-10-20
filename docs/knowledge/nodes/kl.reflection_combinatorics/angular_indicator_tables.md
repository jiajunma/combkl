---
id: kl.dihedral.angular_indicator_tables
title: Actual root comparisons give the signed indicator tables
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.native_later_counts
- kl.dihedral.angular_order
- kl.dihedral.signed_reflection_action
- kl.dihedral.good_indices
- kl.dihedral.signed_residue_comparison
- kl.dihedral.signed_counts
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_same_table
  - OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_next_table
  - OAI.KLInvariance.TitsSpace.PlaneBasis.afterIndicator_one
  - OAI.KLInvariance.TitsSpace.PlaneBasis.afterIndicator_same
  - OAI.KLInvariance.TitsSpace.PlaneBasis.afterIndicator_next
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1814
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_same_table
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1833
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_next_table
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1858
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.afterIndicator_one
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1867
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.afterIndicator_same
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1885
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.afterIndicator_next
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient and intrinsic systems, root signs, signed lengths, finite
    representative bounds and counting domains explicit?
  verdict: Verified different GoodIndex requirements for same-source and next-source
    comparisons, all three reduced-length assumptions, odd labels, bounded/unbounded
    alternatives and both edge/nonedge indicator branches.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Actual root comparisons give the signed indicator tables

Fix a plane basis \(B\) in a finite-generator real Coxeter system, its induced dihedral group \(D\), and its actual geometric slope \(\sigma\). Let \(i,j,z\in\mathbb Z\) have their correct signed lengths:
\[
\ell_D(w_i)=|i|,\qquad \ell_D(w_j)=|j|,\qquad \ell_D(w_z)=|z|.
\]
Suppose \(e:w_i\to_Dw_j\) is an upward reflection edge, with actual plane edge root \(\alpha_e\).

The two slope comparisons have the following conditions.

| Configuration | Admissibility assumptions | Equivalent integer comparison |
|---|---|---|
| Another edge \(w_i\to_Dw_z\) | \(j,z\) are admissible signed indices | \(\sigma(\alpha_e)<\sigma(\alpha_{w_i\to w_z})\ \Longleftrightarrow\ \operatorname{Before}(i+j,i+z)\) |
| A next edge \(w_j\to_Dw_z\) | \(z\) is an admissible signed index | \(\sigma(\alpha_e)<\sigma(\alpha_{w_j\to w_z})\ \Longleftrightarrow\ \operatorname{Before}(i+j,j+z)\) |

For arbitrary \(z\) with the displayed length and admissibility assumptions, these comparisons extend to indicators:
\[
\begin{aligned}
\varepsilon_D(w_i,\alpha_e,w_z)&=\operatorname{aft}(i,i+j,z)
&&\text{if }j,z\text{ are admissible},\\
\varepsilon_D(w_j,\alpha_e,w_z)&=\operatorname{aft}(j,i+j,z)
&&\text{if }z\text{ is admissible}.
\end{aligned}
\]
Here \(\operatorname{aft}(p,a,z)\) is the numerical arrow indicator: it is one when \(|p|<|z|\), \(p+z\) is odd, and \(\operatorname{Before}(a,p+z)\); otherwise it is zero.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**From actual root slopes to nonnegative endpoint counts.**

**OpenAI notes:** The later-edge lemma first transports a relative interval, then uses the midpoint-order table to calculate the difference of two outgoing counts. Its proof also treats reversal of the angular order by subtracting earlier and later edges from total outgoing counts. [dih:midpoint-order](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L358), [dih:count](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L464).

**Lean (primary):** The native count is first defined over the full lower ideal in the induced dihedral group. Actual root comparisons are translated into signed indicators with explicit reduced-length and GoodIndex hypotheses. The two nonnegative counts are evaluated separately. interval_laterCount then removes zero terms to restrict either count to a relative interval. [DihedralIntervals:1852](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1852), [DihedralIntervals:1814](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1814), [DihedralIntervals:1833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1833), [DihedralIntervals:1919](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1919), [DihedralIntervals:1923](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1923), [DihedralIntervals:1948](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1948), [DihedralIntervals:1974](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1974), [DihedralIntervals:2030](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2030).

**Role in the proof:** The Blueprint gives the native count independently of interval transport, with the exact hypotheses of both indicator tables. Its slope orientation is the increasing orientation of the chosen PlaneBasis.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Extract the edge parameters and their bounds

The [[node:kl.dihedral.signed_reflection_action|signed edge criterion]] turns the current edge into
\[
|i|<|j|,\qquad i+j\text{ odd}.
\]
Its left reflection is \(w_{i+j}\). A second edge from \(i\) gives \(|i|<|z|\), odd \(i+z\), and reflection \(w_{i+z}\). A next edge from \(j\) gives \(|j|<|z|\), odd \(j+z\), and reflection \(w_{j+z}\).

### Step 2. Apply the angular theorem when lengths are unbounded

If lengths are unbounded, the [[node:kl.dihedral.angular_order|angular-order theorem]] identifies slope comparison of any two actual edge roots with Before on their odd parameters. Substituting the labels from Step 1 proves both rows directly.

### Step 3. Apply the constrained residue formulas at maximum length

If lengths are bounded, their nonempty set of natural values has a maximum, attained by an element of \(D\); denote it by \(m\). The [[node:kl.dihedral.angular_order|angular-order theorem]] expresses each comparison using odd residues modulo \(2m\).

For the first row, admissibility supplies
\[
-m<j\le m,\qquad -m<z\le m.
\]
Together with \(|i|<|j|\) and \(|i|<|z|\), these are exactly the hypotheses of the [[node:kl.dihedral.signed_residue_comparison|same-source finite-residue comparison theorem]]. It replaces
\[
(i+j)\bmod2m<(i+z)\bmod2m
\]
by \(\operatorname{Before}(i+j,i+z)\).

For the second row, admissibility of \(z\) gives \(-m<z\le m\), while the two edges give \(|i|<|j|<|z|\). The [[node:kl.dihedral.signed_residue_comparison|next-source finite-residue comparison theorem]] replaces
\[
(i+j)\bmod2m<(j+z)\bmod2m
\]
by \(\operatorname{Before}(i+j,j+z)\). These are precisely its required bounds. This proves both slope rows in the bounded case.

### Step 4. Include vertices which are not edge targets

For the first indicator, split according to whether \(w_i\to_Dw_z\).

If it is an edge, the length and parity tests in \(\operatorname{aft}\) hold. Both sides are consequently one or zero according to the first slope row, so they agree.

If it is not an edge, the actual indicator is zero. The [[node:kl.dihedral.signed_reflection_action|signed edge criterion]] says that the conjunction \(|i|<|z|\) and odd \(i+z\) is false. Thus the numerical indicator is also zero, independently of the Before test.

The identical split with source \(w_j\), using the second row, proves the next-source identity. Finally an edge to the identity would give \(\ell_D(x)<\ell_D(1)=0\), so every actual after-indicator at target \(1\) is zero, as used in the lower-interval sum.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_same_table`: [DihedralIntervals.lean:1814](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1814).

`OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_next_table`: [DihedralIntervals.lean:1833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1833).

`OAI.KLInvariance.TitsSpace.PlaneBasis.afterIndicator_one`: [DihedralIntervals.lean:1858](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1858).

`OAI.KLInvariance.TitsSpace.PlaneBasis.afterIndicator_same`: [DihedralIntervals.lean:1867](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1867).

`OAI.KLInvariance.TitsSpace.PlaneBasis.afterIndicator_next`: [DihedralIntervals.lean:1885](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1885).
