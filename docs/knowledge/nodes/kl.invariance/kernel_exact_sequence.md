---
id: kl.detail.kernel_exact_sequence
title: The exact sequence for adding one outgoing condition
kind: theorem
status: proved
primary_topic: kl.invariance
topics:
- kl.invariance
uses:
- kl.detail.edge_images
- kl.sheaves.upward_kernel
- kl.algebra.hilbert_image_exactness
- kl.detail.hilbert_exactness
- kl.algebra.hilbert_convergence
- kl.sheaves.graded_module
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.lowerAt
  - OAI.KLInvariance.MomentGraph.GradedSheaf.lowerAt_map
  - OAI.KLInvariance.MomentGraph.GradedSheaf.upwardKernel_insert
  - OAI.KLInvariance.MomentGraph.GradedSheaf.hilbert_edge_increment
  - OAI.KLInvariance.MomentGraph.GradedSheaf.kernelHilbert_edge
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:20
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.lowerAt
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:25
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.lowerAt_map
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:47
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.upwardKernel_insert
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:59
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.hilbert_edge_increment
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:377
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.kernelHilbert_edge
  - artifact: openai-kl-paper
    locator: Related paper context; sec:induction
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the integer degree, scalar regularity, image inclusion, convergence
    and parameter assumptions explicit, and are source hypotheses separated from derived
    applications?
  verdict: Read GradedSheaf.vertex/edge and ModuleData.nonneg as inherited hypotheses.
    Preserved integer indexing and zero negative pieces, generic positive-q/summability
    assumptions, polynomial convergence, both kernel directions, degreewise surjectivity
    and the already-selected edge case.
tags:
- Kazhdan-Lusztig
- Hilbert-comparison
---

# The exact sequence for adding one outgoing condition

Let \(k\) be a field, \(A\) a commutative \(k\)-algebra with its grading, and \(\mathcal B\) a graded module sheaf on an ordered graph. Its stalks and edge modules are graded module data: finite over \(A\), indexed by \(\mathbb Z\), and with zero pieces in every negative degree. Its restrictions have degree zero.

Fix an edge \(e:x\to y\) and any outgoing selection \(F\) at \(x\). Write \(K_x(F)\) for the selected kernel and
\[
I_e(F)=\rho_e^-(K_x(F))
\]
for its actual lower edge image. Restriction gives a degree-zero exact sequence
\[
0\longrightarrow K_x(F\cup\{e\})
\longrightarrow K_x(F)
\xrightarrow{\rho_e^-}I_e(F)\longrightarrow0.
\]

Assume the homogeneous pieces of \(\mathcal B^x\) are finite-dimensional. If \(q>0\) and the series defining \(H_{K_x(F)}(q)\) is summable, then
\[
H_{K_x(F)}(q)-H_{K_x(F\cup\{e\})}(q)=H_{I_e(F)}(q),
\]
where every Hilbert value sums over \(n\in\mathbb Z\).

In the polynomial-sheaf case \(A=\mathbb R[X_i:i\in\Sigma]\), with \(\Sigma\) finite and the source's finitely generated graded stalks, piece finiteness and summability hold for every \(0<q<1\). The field `ModuleData.nonneg` makes every negative stalk and edge piece zero, so the integer-indexed Hilbert sum equals its sum over nonnegative degrees.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Integer-graded exactness before the polynomial specialization.**

**OpenAI notes:** The notes use the exact sequence for removing one kernel condition and evaluate the Hilbert series of finitely generated kernels bounded below in degree. [eq:state](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L243), [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275).

**Lean (primary):** The sheaf lemma uses integer-indexed pieces, positive q and summability of the original selected kernel. Its GradedSheaf data consist of ModuleData objects whose nonneg field makes all negative pieces zero. The polynomial specialization supplies finite piece dimensions and convergence for 0<q<1. Adding an already-present condition gives the same kernel and zero image. [MinimalExtensions:47](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L47), [MinimalExtensions:59](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L59), [PositiveTransfer:377](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L377).

**Role in the proof:** The Blueprint retains both the integer indexing and the nonnegative support of the sheaf modules. The broader generic Hilbert-module lemmas and their negative-degree example are developed separately.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Specify the restricted map and its actual codomain

Put
\[
K=K_x(F),\qquad K'=K_x(F\cup\{e\}),\qquad I=I_e(F).
\]
Restrict the lower map to \(K\), and give it codomain \(I\):
\[
r:K\to I,\qquad v\longmapsto\rho_e^-(v).
\]
This is surjective by the definition of \(I\). The source's `lowerAt` expresses the same lower restriction with its source vertex identified as \(x\).

### Step 2. Identify the kernel in both directions

If \(v\in\ker r\), all restrictions indexed by \(F\) vanish because \(v\in K\), and the \(e\)-restriction vanishes because \(r(v)=0\). Thus \(v\in K'\).

Conversely, \(v\in K'\) satisfies every condition in \(F\) and the \(e\)-condition, so it lies in \(K\) and maps to zero. Hence
\[
K'=K\cap\ker\rho_e^-,\qquad \ker r=K'.
\]
The first inclusion in the exact sequence is the actual submodule inclusion and is injective. This proves exactness.

### Step 3. Restrict the exact sequence to each integer degree

The selected kernels are homogeneous because every selected restriction preserves degree. The image \(I\) is homogeneous as well.

If \(w\in I_n\), choose \(v\in K\) with \(r(v)=w\). The component \(v_n\) lies in \(K_n\). With \(\pi_n\) the degree-\(n\) projection on the edge module,
\[
r(v_n)=\pi_n(r(v))=\pi_n(w)=w.
\]
Thus the restriction \(r_n:K_n\to I_n\) is surjective, with kernel \(K'_n\), giving
\[
0\longrightarrow K'_n\longrightarrow K_n\longrightarrow I_n\longrightarrow0
\qquad(n\in\mathbb Z).
\]
All spaces are finite-dimensional: \(K_n,K'_n\) are subspaces of \((\mathcal B^x)_n\), and \(I_n\) is a quotient of \(K_n\). Consequently
\[
\dim_kK_n=\dim_kK'_n+\dim_kI_n.
\]

### Step 4. Sum the degreewise identities

For \(q>0\), the weight \(q^n\) is positive for every integer \(n\). The terms for \(K'\) and \(I\) are nonnegative and bounded by those for \(K\), so the assumed summability of the latter implies summability of both former series.

Multiply the dimension identity by \(q^n\) and sum over \(\mathbb Z\). The [[node:kl.algebra.hilbert_image_exactness|Hilbert image-exactness theorem]] gives
\[
H_K(q)=H_{K'}(q)+H_I(q).
\]
Subtracting the finite real value \(H_{K'}(q)\) proves the asserted difference formula.

### Step 5. Verify the polynomial-sheaf hypotheses

For a finitely generated graded polynomial module over finitely many variables, the [[node:kl.algebra.hilbert_convergence|Hilbert-convergence theorem]] gives finite-dimensional pieces, a lower degree bound and convergence at \(0<q<1\). It also gives convergence for the intersection pieces of any subspace, including \(K_x(F)\).

The general polynomial-module convergence theorem allows an integer lower degree bound. For this sheaf, graded module data give
\[
(\mathcal B^x)_n=0\quad(n<0).
\]
The selected kernel and its image consequently also have zero negative pieces. Thus the sum over \(\mathbb Z\) in Step 4 can equivalently be written over \(n\ge0\).

The exact-sequence statement also covers \(e\in F\): then \(K'=K\), its \(e\)-restriction is already zero, and the lower image and Hilbert increment are both zero.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.lowerAt`: [MinimalExtensions.lean:20](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L20).

`OAI.KLInvariance.MomentGraph.GradedSheaf.lowerAt_map`: [MinimalExtensions.lean:25](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L25).

`OAI.KLInvariance.MomentGraph.GradedSheaf.upwardKernel_insert`: [MinimalExtensions.lean:47](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L47).

`OAI.KLInvariance.MomentGraph.GradedSheaf.hilbert_edge_increment`: [MinimalExtensions.lean:59](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L59).

`OAI.KLInvariance.MomentGraph.GradedSheaf.kernelHilbert_edge`: [PositiveTransfer.lean:377](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L377).
