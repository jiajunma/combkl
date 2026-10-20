---
id: kl.dihedral.middle_vertex_order
title: Consecutive root order is determined by the middle descent
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.inversion_cuts
- kl.dihedral.inversion_descent_bridge
- kl.dihedral.prefix_roots
- kl.detail.root_inversion_count
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.TitsSpace.graphRoot_inverted_target
  - OAI.KLInvariance.TitsSpace.graphRoot_not_inverted_source
  - OAI.KLInvariance.TitsSpace.PlaneBasis.consecutive_slopes_iff
  - OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_slopes_iff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:855
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.graphRoot_inverted_target
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:866
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.graphRoot_not_inverted_source
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:940
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.consecutive_slopes_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1106
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_slopes_iff
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient and intrinsic systems, root signs, signed lengths, finite
    representative bounds and counting domains explicit?
  verdict: Read both endpoint-sign proofs and both consecutive-root statements; expanded
    reflection multiplication, the mixed-sign application, the identity-coset substitution
    and distinctness of consecutive labels.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Consecutive root order is determined by the middle descent

Fix a finite-generator real Coxeter system \(W\), a plane basis \(B=(a_L,a_R)\), its root plane \(P\), and geometric slope \(\sigma\). Write \(\operatorname{Inv}_W(g,a)\) when \(g^{-1}a\) is a negative root.

Let \(x\to_Wy\to_Wz\) be two upward reflection edges whose positive roots \(\alpha,\beta\) lie in \(P\). Then
\[
\sigma(\alpha)<\sigma(\beta)
\quad\Longleftrightarrow\quad
\operatorname{Inv}_W(y,a_L).
\]
In the induced dihedral group \(D\), with left simple generator \(s\) represented by \(a_L\), every intrinsic two-edge path \(x\to_Dy\to_Dz\) satisfies
\[
\sigma(\alpha_{x\to y})<\sigma(\alpha_{y\to z})
\quad\Longleftrightarrow\quad
\ell_D(sy)<\ell_D(y).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Ambient inversion cuts in place of a root-coordinate recurrence.**

**OpenAI notes:** The notes set \(\kappa=-(a_L,a_R)/2\), where the parentheses denote the ambient Tits form. The midpoint-order lemma writes prefix roots using \(p_0=0\), \(p_1=1\) and \(p_{n+1}=2\kappa p_n-p_{n-1}\). It obtains \(\kappa=\cos(\pi/m)\) in finite type and \(\kappa\ge1\) in infinite type, then compares the resulting coordinate ratios. The functional ratio gives that angular order or its reverse. [dih:midpoint-order](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L358).

**Lean (primary):** PlaneBasis chooses its endpoint roots in increasing geometric slope. Convexity of inversion signs gives a middle-descent test, which orders the two actual ambient prefix-root sequences. A separating element \(w_{k+1}\) compares the two rays. Unbounded lengths give the signed Before order; a maximum length gives the odd residue order modulo 2m. [DyerPaths:923](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L923), [DyerPaths:1106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1106), [DihedralIntervals:832](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L832), [DihedralIntervals:844](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L844), [DihedralIntervals:1101](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1101), [DihedralIntervals:1143](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1143), [DihedralIntervals:1251](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1251).

**Role in the proof:** The ordering conclusion is developed along Lean’s inversion and length proof. The additional classification of \(\kappa\) in the notes is not a conclusion of these Lean angular-order declarations.
<!-- source-comparison:end -->

*Proof.*

### Step 1. The incoming root is inverted at the middle vertex

The first edge has left reflection \(q=yx^{-1}\). Since \(q^2=1\) and \(qx=y\), one has \(qy=x\). Its orientation says \(\ell_W(x)<\ell_W(y)\), and hence
\[
\ell_W(qy)=\ell_W(x)<\ell_W(y).
\]
The [[node:kl.detail.root_inversion_count|ambient root-sign criterion]] makes the positive root \(\alpha\) of \(q\) inverted at \(y\).

### Step 2. The outgoing root is noninverted there

The second edge has left reflection \(r=zy^{-1}\), so \(ry=z\). If its positive root \(\beta\) were inverted at \(y\), the same criterion would give
\(\ell_W(z)=\ell_W(ry)<\ell_W(y)\).
The upward edge gives the opposite strict inequality. Thus \(\beta\) is noninverted at \(y\).

### Step 3. Apply the mixed-sign inversion cut

The two roots belong to \(P\), with the mixed signs established in Steps 1 and 2. The [[node:kl.dihedral.inversion_cuts|inversion-cut theorem]], applied at \(w=y\), gives
\[
\sigma(\alpha)<\sigma(\beta)
\Longleftrightarrow
\operatorname{Inv}_W(y,a_L).
\]
This proves the ambient assertion.

### Step 4. Express the middle sign as an intrinsic descent

Each intrinsic edge is an ambient edge with the same positive root, and both actual plane edge roots belong to \(P\). Apply Step 3 to those ambient edges.

The [[node:kl.dihedral.inversion_descent_bridge|inversion-descent bridge]] with the least representative \(a_0=1\) gives
\[
\operatorname{Inv}_W(y,a_L)
\Longleftrightarrow
\ell_D(sy)<\ell_D(y).
\]
Substitution proves the intrinsic assertion.

In particular, the two roots of a two-edge upward path are distinct: equal roots would give the same reflection \(q\), and then \(z=qy=q^2x=x\), contrary to the strict increase of length along the path. Injectivity of slope therefore also makes their slopes distinct.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.graphRoot_inverted_target`: [DyerPaths.lean:855](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L855).

`OAI.KLInvariance.TitsSpace.graphRoot_not_inverted_source`: [DyerPaths.lean:866](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L866).

`OAI.KLInvariance.TitsSpace.PlaneBasis.consecutive_slopes_iff`: [DyerPaths.lean:940](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L940).

`OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_slopes_iff`: [DyerPaths.lean:1106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1106).
