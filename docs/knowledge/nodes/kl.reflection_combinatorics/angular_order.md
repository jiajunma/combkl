---
id: kl.dihedral.angular_order
title: Finite and infinite angular order of actual dihedral roots
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.prefix_roots
- kl.dihedral.prefix_order
- kl.dihedral.positive_negative_order
- kl.dihedral.signed_period
- kl.dihedral.signed_counts
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_infinite_order
  - OAI.KLInvariance.TitsSpace.PlaneBasis.max_length_pos
  - OAI.KLInvariance.TitsSpace.PlaneBasis.odd_residue_repr
  - OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_finite_order
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1143
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_infinite_order
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1234
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.max_length_pos
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1240
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.odd_residue_repr
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1251
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_finite_order
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient and intrinsic systems, root signs, signed lengths, finite
    representative bounds and counting domains explicit?
  verdict: Reviewed all four infinite sign cases, common witness bounds, finite positivity
    of m, odd Euclidean residues, period substitution and prefix-root identification.
    The statements use the original ambient geometric slope.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Finite and infinite angular order of actual dihedral roots

Let \(B\) be a plane basis in a finite-generator real Coxeter system, \(D\) its induced dihedral group, and \(\sigma\) its actual ambient geometric slope. Let \(e:x\to_Dy\) and \(f:z\to_Dt\) have odd signed reflection parameters \(a,b\):
\[
yx^{-1}=w_a,\qquad tz^{-1}=w_b,\qquad a,b\text{ odd}.
\]

Write \(\alpha_e,\alpha_f\) for their actual plane edge roots. If intrinsic lengths are unbounded, then
\[
\sigma(\alpha_e)<\sigma(\alpha_f)
\quad\Longleftrightarrow\quad
\operatorname{Before}(a,b).
\]
For these odd integers, the Before relation puts every positive parameter before every negative parameter and uses ordinary increasing integer order within each sign. The resulting order is
\[
1\prec3\prec5\prec\cdots\prec\cdots\prec-5\prec-3\prec-1.
\]

If \(v\in D\) has maximum intrinsic length \(m=\ell_D(v)\), then \(m>0\) and
\[
\sigma(\alpha_e)<\sigma(\alpha_f)
\quad\Longleftrightarrow\quad
(a\bmod 2m)<(b\bmod 2m),
\]
where the remainders belong to \(\{0,\ldots,2m-1\}\). The odd reflection labels occur in the order \(1,3,\ldots,2m-1\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Ambient inversion cuts in place of a root-coordinate recurrence.**

**OpenAI notes:** The notes set \(\kappa=-(a_L,a_R)/2\), where the parentheses denote the ambient Tits form. The midpoint-order lemma writes prefix roots using \(p_0=0\), \(p_1=1\) and \(p_{n+1}=2\kappa p_n-p_{n-1}\). It obtains \(\kappa=\cos(\pi/m)\) in finite type and \(\kappa\ge1\) in infinite type, then compares the resulting coordinate ratios. The functional ratio gives that angular order or its reverse. [dih:midpoint-order](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L358).

**Lean (primary):** PlaneBasis chooses its endpoint roots in increasing geometric slope. Convexity of inversion signs gives a middle-descent test, which orders the two actual ambient prefix-root sequences. A separating element \(w_{k+1}\) compares the two rays. Unbounded lengths give the signed Before order; a maximum length gives the odd residue order modulo 2m. [DyerPaths:923](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L923), [DyerPaths:1106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1106), [DihedralIntervals:832](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L832), [DihedralIntervals:844](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L844), [DihedralIntervals:1101](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1101), [DihedralIntervals:1143](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1143), [DihedralIntervals:1251](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1251).

**Role in the proof:** The ordering conclusion is developed along Lean’s inversion and length proof. The additional classification of \(\kappa\) in the notes is not a conclusion of these Lean angular-order declarations.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Represent every odd parameter on one of the two rays

An odd integer \(a\) is nonzero. Its absolute value is an odd natural number, so it is \(2k+1\) with
\(k=(|a|-1)/2\in\mathbb N\). According to its sign,
\(a=2k+1\) or \(a=-(2k+1)\).
Similarly write \(b=\pm(2l+1)\).

### Step 2. Compare positive parameters in the unbounded case

For \(a=2k+1\) and \(b=2l+1\), choose \(v\) with
\(\ell_D(v)\ge\max(k,l)+1\).
Both prefix-root values are in their meaningful range. The [[node:kl.dihedral.prefix_order|prefix-label theorem]] identifies
\(\alpha_e=\beta_k^+(v)\) and \(\alpha_f=\beta_l^+(v)\).

Strict monotonicity gives the comparison if \(k<l\). If \(k=l\), the roots are equal; if \(l<k\), strict monotonicity gives the reverse comparison. Hence
\[
\sigma(\alpha_e)<\sigma(\alpha_f)
\Longleftrightarrow k<l
\Longleftrightarrow a<b.
\]
This is exactly Before for two positive parameters.

### Step 3. Compare the two mixed-sign cases

If \(a=2k+1\) and \(b=-(2l+1)\), the [[node:kl.dihedral.positive_negative_order|positive-negative separator theorem]] proves the strict slope inequality. Before is also true because the first parameter is positive and the second negative.

If \(a=-(2k+1)\) and \(b=2l+1\), apply that theorem to \(f,e\). It proves the reverse strict slope inequality, so the proposed comparison is false. Before is false in this sign configuration as well.

### Step 4. Compare two negative parameters

Suppose \(a=-(2k+1)\) and \(b=-(2l+1)\). Choose the same kind of common long witness as in Step 2. Prefix-label identification gives
\(\alpha_e=\beta_k^-(v)\), \(\alpha_f=\beta_l^-(v)\).
The [[node:kl.dihedral.prefix_order|strict antitonicity theorem]], with its equality and reversed-index cases, gives
\[
\sigma(\alpha_e)<\sigma(\alpha_f)
\Longleftrightarrow l<k
\Longleftrightarrow -(2k+1)<-(2l+1).
\]
This is Before for two negative parameters. The four sign cases prove the unbounded assertion.

### Step 5. Reduce odd parameters in the maximum-length case

Now let \(v\) have maximum length \(m\). A simple generator has length one, so \(m\ge1\). The [[node:kl.dihedral.signed_period|period theorem]] gives
\[
w_a=w_{a\bmod 2m}.
\]
Let \(r=a\bmod 2m\). Euclidean remainder gives \(0\le r<2m\). Since \(2m\) is even and \(a\) is odd, \(r\) is odd. Thus
\[
r=2k+1,\qquad 0\le k<m.
\]
This also proves uniqueness of \(k\); explicitly \(k=(r-1)/2\). Similarly \(b\bmod 2m=2l+1\) with \(0\le l<m\).

### Step 6. Identify the finite list with one prefix sequence

Periodicity replaces the two edge reflections by \(w_{2k+1}\) and \(w_{2l+1}\). The maximum-length witness \(v\) has \(k,l<\ell_D(v)\), so prefix-label identification gives the roots \(\beta_k^+(v)\) and \(\beta_l^+(v)\).

Strict monotonicity then yields
\[
\sigma(\alpha_e)<\sigma(\alpha_f)
\Longleftrightarrow k<l
\Longleftrightarrow 2k+1<2l+1
\Longleftrightarrow (a\bmod2m)<(b\bmod2m).
\]
This proves the finite assertion.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_infinite_order`: [DihedralIntervals.lean:1143](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1143).

`OAI.KLInvariance.TitsSpace.PlaneBasis.max_length_pos`: [DihedralIntervals.lean:1234](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1234).

`OAI.KLInvariance.TitsSpace.PlaneBasis.odd_residue_repr`: [DihedralIntervals.lean:1240](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1240).

`OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_finite_order`: [DihedralIntervals.lean:1251](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1251).
