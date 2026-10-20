---
id: kl.dihedral.prefix_order
title: Monotonicity and labels of the two prefix-root sequences
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.prefix_roots
- kl.dihedral.middle_vertex_order
- kl.dihedral.internal_ranks
- kl.dihedral.signed_lengths
- kl.dihedral.signed_reflection_action
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.prefixRoot_strictMono
  - OAI.KLInvariance.TitsSpace.PlaneBasis.negPrefixRoot_strictAnti
  - OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_eq_of_label
  - OAI.KLInvariance.TitsSpace.PlaneBasis.prefixRoot_eq_edgeRoot
  - OAI.KLInvariance.TitsSpace.PlaneBasis.negPrefixRoot_eq_edgeRoot
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:832
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.prefixRoot_strictMono
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:844
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.negPrefixRoot_strictAnti
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:874
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_eq_of_label
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:882
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.prefixRoot_eq_edgeRoot
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:893
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.negPrefixRoot_eq_edgeRoot
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient and intrinsic systems, root signs, signed lengths, finite
    representative bounds and counting domains explicit?
  verdict: Checked the adjacent comparisons, strict n+1<N bound for uniqueness of
    the negative-path descent, strictness from distinct path labels, transitive extension
    and both odd reflection labels.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Monotonicity and labels of the two prefix-root sequences

In a finite-generator real Coxeter system, fix a plane basis \(B\), its induced dihedral group \(D\), and the geometric slope \(\sigma\). For \(v\in D\), set \(N=\ell_D(v)\) and use the two prefix-root sequences \(\beta_n^+(v),\beta_n^-(v)\).

For \(0\le k<l<N\),
\[
\sigma(\beta_k^+(v))<\sigma(\beta_l^+(v)),
\qquad
\sigma(\beta_l^-(v))<\sigma(\beta_k^-(v)).
\]
Moreover, any intrinsic edge \(e:x\to_Dy\) with left reflection
\[
yx^{-1}=w_{2n+1}\quad\text{or}\quad yx^{-1}=w_{-(2n+1)}
\qquad(n<N)
\]
has root \(\beta_n^+(v)\) or \(\beta_n^-(v)\), respectively.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Ambient inversion cuts in place of a root-coordinate recurrence.**

**OpenAI notes:** The notes set \(\kappa=-(a_L,a_R)/2\), where the parentheses denote the ambient Tits form. The midpoint-order lemma writes prefix roots using \(p_0=0\), \(p_1=1\) and \(p_{n+1}=2\kappa p_n-p_{n-1}\). It obtains \(\kappa=\cos(\pi/m)\) in finite type and \(\kappa\ge1\) in infinite type, then compares the resulting coordinate ratios. The functional ratio gives that angular order or its reverse. [dih:midpoint-order](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L358).

**Lean (primary):** PlaneBasis chooses its endpoint roots in increasing geometric slope. Convexity of inversion signs gives a middle-descent test, which orders the two actual ambient prefix-root sequences. A separating element \(w_{k+1}\) compares the two rays. Unbounded lengths give the signed Before order; a maximum length gives the odd residue order modulo 2m. [DyerPaths:923](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L923), [DyerPaths:1106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1106), [DihedralIntervals:832](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L832), [DihedralIntervals:844](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L844), [DihedralIntervals:1101](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1101), [DihedralIntervals:1143](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1143), [DihedralIntervals:1251](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1251).

**Role in the proof:** The ordering conclusion is developed along Lean’s inversion and length proof. The additional classification of \(\kappa\) in the notes is not a conclusion of these Lean angular-order declarations.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Compare adjacent roots on the positive signed path

Take \(n+1<N\). The two edges defining \(\beta_n^+(v)\) and \(\beta_{n+1}^+(v)\) have middle vertex \(w_{n+1}\). It is the reduced alternating word of positive length \(n+1\) beginning with \(s\). Left multiplication by \(s\) cancels its first letter, giving a word of length \(n\). Thus \(s\) is a left descent.

The [[node:kl.dihedral.middle_vertex_order|middle-vertex order theorem]] now gives
\[
\sigma(\beta_n^+(v))<\sigma(\beta_{n+1}^+(v)).
\]
Applying this for \(n=k,k+1,\ldots,l-1\) and using transitivity proves the first strict inequality.

### Step 2. Determine the descent on the negative signed path

The middle vertex for two adjacent negative-path roots is \(w_{-(n+1)}\), the reduced alternating word of length \(n+1\) beginning with \(t\). Cancellation of the first letter makes \(t\) a left descent.

Its length is positive and strictly less than \(\ell_D(v)=N\). The [[node:kl.dihedral.internal_ranks|internal-rank theorem]] therefore gives exactly one simple left descent. Since that descent is \(t\), \(s\) is not a descent.

### Step 3. Obtain the reversed strict inequality

The [[node:kl.dihedral.middle_vertex_order|middle-vertex order theorem]] says that
\(\sigma(\beta_n^-(v))<\sigma(\beta_{n+1}^-(v))\)
would be equivalent to the excluded \(s\)-descent. Hence
\[
\sigma(\beta_{n+1}^-(v))\le\sigma(\beta_n^-(v)).
\]
The two roots occur on consecutive upward edges, so they are distinct by the final argument of the [[node:kl.dihedral.middle_vertex_order|middle-vertex order theorem]]. Their slopes are distinct as well. The weak inequality is consequently strict.

Chaining these adjacent strict inequalities from \(k\) to \(l\) gives the second assertion.

### Step 4. Identify roots through their left reflections

For the positive prefix edge the signed label formula gives
\[
w_{n+1}w_n^{-1}=w_{n+(n+1)}=w_{2n+1}.
\]
For the negative prefix edge it gives
\[
w_{-(n+1)}w_{-n}^{-1}=w_{-n-(n+1)}=w_{-(2n+1)}.
\]
If the edge \(e\) has the corresponding left reflection, it has the same positive representing root as that prefix edge. This proves both root identifications, and also shows that their values agree for any two witnesses whose lengths exceed \(n\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.prefixRoot_strictMono`: [DihedralIntervals.lean:832](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L832).

`OAI.KLInvariance.TitsSpace.PlaneBasis.negPrefixRoot_strictAnti`: [DihedralIntervals.lean:844](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L844).

`OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_eq_of_label`: [DihedralIntervals.lean:874](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L874).

`OAI.KLInvariance.TitsSpace.PlaneBasis.prefixRoot_eq_edgeRoot`: [DihedralIntervals.lean:882](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L882).

`OAI.KLInvariance.TitsSpace.PlaneBasis.negPrefixRoot_eq_edgeRoot`: [DihedralIntervals.lean:893](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L893).
