---
id: kl.dihedral.native_later_counts
title: Actual dihedral after-indicators and later-edge counts
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.prefix_roots
- kl.dihedral.lower_signed_sums
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.afterIndicator
  - OAI.KLInvariance.TitsSpace.PlaneBasis.laterCount
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1852
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.afterIndicator
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1919
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.laterCount
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient and intrinsic systems, root signs, signed lengths, finite
    representative bounds and counting domains explicit?
  verdict: Defined both natural-valued quantities with arbitrary positive ambient
    threshold, strict slope condition, intrinsic lower interval and finite sum; distinguished
    actual roots from the signed integer indicator and supplied the A2 calculation.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Actual dihedral after-indicators and later-edge counts

Let \(B\) be a plane basis in a finite-generator real Coxeter system. Let \(D\) be its induced dihedral group with intrinsic Bruhat order \(\le_D\), and let \(\sigma\) be the geometric slope on ambient positive roots.

Choose \(x,z\in D\) and a positive ambient root \(\alpha\), used as the threshold. Define the actual dihedral after-indicator
\[
\varepsilon_D(x,\alpha,z)=
\begin{cases}
1,&x\to_D z\text{ and }\sigma(\alpha)<\sigma(\alpha_{x\to z}),\\
0,&\text{otherwise}.
\end{cases}
\]
The root \(\alpha\) may be any positive ambient root; the definition imposes no plane-membership condition on it. The edge root \(\alpha_{x\to z}\) is the actual plane edge root. In Lean the test for an edge is performed first, so this root is used only when the edge exists.

For \(c\in D\), define the native later-edge count
\[
h_D(x,\alpha;c)
=\sum_{z\le_Dc}\varepsilon_D(x,\alpha,z)\in\mathbb N.
\]
The sum is finite because the lower Bruhat interval of \(c\) is finite. These are `PlaneBasis.afterIndicator` and `PlaneBasis.laterCount`.

## The threshold and the counted edges

The adjective “later” means strictly greater slope. An edge whose root equals \(\alpha\) contributes zero. A vertex \(z\) which is not the target of an upward reflection edge from \(x\) also contributes zero.

In particular \(\varepsilon_D(x,\alpha,1)=0\): an upward edge ending at the identity would require \(\ell_D(x)<0\). More generally, if \(x\not\le_Dz\), the indicator is zero, because an upward reflection edge itself gives a Bruhat comparison.

## A long edge in type A2

As an illustrative calculation, use a plane of type \(A_2\), with maximum length \(3\) and slope order of odd reflection parameters \(1,3,5\) modulo \(6\). Let \(c=sts\), and take the current edge \(1\to c\), whose parameter is \(3\).

The outgoing edges from \(1\) below \(c\) have targets \(s,t,c\) and parameters \(1,-1,3\). Their residues are \(1,5,3\). Only the edge to \(t\) is later than the threshold. At \(c\) there is no outgoing edge staying below \(c\). Therefore
\[
h_D(1,\alpha_{1\to c};c)=1,\qquad
h_D(c,\alpha_{1\to c};c)=0.
\]
The [[node:kl.dihedral.native_count_difference|native count-difference theorem]] explains this difference as
\((3-0-1)/2=1\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**From actual root slopes to nonnegative endpoint counts.**

**OpenAI notes:** The later-edge lemma first transports a relative interval, then uses the midpoint-order table to calculate the difference of two outgoing counts. Its proof also treats reversal of the angular order by subtracting earlier and later edges from total outgoing counts. [dih:midpoint-order](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L358), [dih:count](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L464).

**Lean (primary):** The native count is first defined over the full lower ideal in the induced dihedral group. Actual root comparisons are translated into signed indicators with explicit reduced-length and GoodIndex hypotheses. The two nonnegative counts are evaluated separately. interval_laterCount then removes zero terms to restrict either count to a relative interval. [DihedralIntervals:1852](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1852), [DihedralIntervals:1814](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1814), [DihedralIntervals:1833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1833), [DihedralIntervals:1919](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1919), [DihedralIntervals:1923](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1923), [DihedralIntervals:1948](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1948), [DihedralIntervals:1974](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1974), [DihedralIntervals:2030](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2030).

**Role in the proof:** The Blueprint gives the native count independently of interval transport, with the exact hypotheses of both indicator tables. Its slope orientation is the increasing orientation of the chosen PlaneBasis.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.afterIndicator`: [DihedralIntervals.lean:1852](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1852).

`OAI.KLInvariance.TitsSpace.PlaneBasis.laterCount`: [DihedralIntervals.lean:1919](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1919).
