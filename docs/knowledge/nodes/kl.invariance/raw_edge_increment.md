---
id: kl.comparison.raw_edge_increment
title: The Hilbert increment from an embedded edge-image inclusion
kind: theorem
status: proved
primary_topic: kl.invariance
topics:
- kl.invariance
uses:
- kl.detail.kernel_exact_sequence
- kl.algebra.saturated_image_hilbert
- kl.algebra.shifted_image_hilbert
- kl.sheaves.hilbert_detection
- kl.algebra.hilbert_convergence
- kl.notes.upper_image_free
- kl.local.edge_factor_action_properties
- kl.detail.upper_quotient
- kl.detail.edge_images
- kl.sheaves.graded_module
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  - Support
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.upper_image_value
  - OAI.KLInvariance.MomentGraph.GradedSheaf.shifted_upperImage_value
  - OAI.KLInvariance.MomentGraph.GradedSheaf.edge_increment_le
  - OAI.KLInvariance.MomentGraph.GradedSheaf.edge_increment_eq_iff
  - OAI.KLInvariance.BruhatGraph.actual_edge_increment_le
  - OAI.KLInvariance.BruhatGraph.actual_edge_increment_eq_iff
  - OAI.KLInvariance.BruhatGraph.label_regular_stalk
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1315
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.upper_image_value
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:388
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.shifted_upperImage_value
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:410
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.edge_increment_le
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:433
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.edge_increment_eq_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:479
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.actual_edge_increment_le
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:500
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.actual_edge_increment_eq_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1353
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.label_regular_stalk
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the integer degree, scalar regularity, image inclusion, convergence
    and parameter assumptions explicit, and are source hypotheses separated from derived
    applications?
  verdict: Read generic edge-value proofs together with GradedSheaf/ModuleData fields.
    Retained nonnegative support of the sheaf modules, arbitrary selections, regularity
    and embedded inclusion; expanded equality detection and the explicit nonnegative
    one-edge example.
tags:
- Kazhdan-Lusztig
- Hilbert-comparison
---

# The Hilbert increment from an embedded edge-image inclusion

Let \(A=\mathbb R[X_i:i\in\Sigma]\), with \(\Sigma\) finite and every variable of degree one. Let \(\mathcal B\) be a graded sheaf on an ordered graph, with graded module data as stalks and edge modules: they are finitely generated over \(A\), indexed by \(\mathbb Z\), and zero in negative degrees.

For a homogeneous submodule \(S\), write \(H_S(q)=\sum_{n\in\mathbb Z}\dim_{\mathbb R}S_n\,q^n\) for its Hilbert value. Choose scalar labels \(\alpha_f\in A\) satisfying the upper-quotient rule. Fix an edge \(e:x\to y\), outgoing selections \(F,H\) at \(x,y\), and an injective \(A\)-linear map
\[
\Phi:\mathcal B^e\to\mathcal B^e
\]
homogeneous of degree \(d\in\mathbb Z\). Suppose:

- The current label satisfies \(\alpha_e\in A_1\).
- Multiplication by \(\alpha_e\) is injective on \(\mathcal B^y\) and on every edge module \(\mathcal B^h\) for \(h\in H\).
- With \(I=\rho_e^-(K_x(F))\) and \(J=\rho_e^+(K_y(H))\), the actual embedded images satisfy \(I\subseteq\Phi(J)\).

For \(0<q<1\), one has
\[
H_{K_x(F)}(q)-H_{K_x(F\cup\{e\})}(q)
\le q^d(1-q)H_{K_y(H)}(q).
\]
Equality at the chosen \(q\) holds exactly when
\[
I=\Phi(J)
\]
as submodules of the actual edge module.

For a boundary sheaf on a finite-generator real Coxeter interval, over the coefficient algebra of a finite real basis of the extended realization, take \(\Phi\) to be multiplication by its correction lift. The label and regularity hypotheses then follow from the boundary-sheaf and root data. The conclusions hold whenever the displayed image inclusion is given, with \(d\) the correction degree.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Numerical equality detects equality of the embedded images.**

**OpenAI notes:** The notes bound the lower-kernel increase by the corrected upper-image Hilbert value. After the global endpoint comparison forces equality, positive degreewise defects recover equality of the two actual images. [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275), [eq:image-equality](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L370).

**Lean (primary):** The single-edge theorem proves the inequality and its exact equality criterion together for a homogeneous injective edge map, conditional on the actual image inclusion. The Bruhat specialization verifies the label and correction regularity hypotheses directly. [PositiveTransfer:388](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L388), [PositiveTransfer:410](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L410), [PositiveTransfer:433](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L433), [PositiveTransfer:479](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L479), [PositiveTransfer:500](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L500).

**Role in the proof:** The Blueprint preserves the conditional image-inclusion interface, explains the positive defect in every integer degree and treats the actual correction map as a specialization of the generic image theorem.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Express the lower increment as the Hilbert value of its image

The [[node:kl.detail.kernel_exact_sequence|one-condition exact-sequence theorem]] gives
\[
H_{K_x(F)}(q)-H_{K_x(F\cup\{e\})}(q)=H_I(q).
\]
Its hypotheses hold by finite polynomial-module piece dimensions and Hilbert convergence.

### Step 2. Compute the actual upper-image value

Put \(S=K_y(H)\). The upper-quotient rule says
\[
\ker\rho_e^+=\alpha_e\mathcal B^y.
\]
If \(\alpha_ev\in S\), then for each \(h\in H\),
\[
0=\rho_h^-(\alpha_ev)=\alpha_e\rho_h^-(v).
\]
Regularity on \(\mathcal B^h\) gives \(\rho_h^-(v)=0\). Hence \(v\in S\), proving saturation of the selected upper kernel.

The restrictions have degree zero, the selected kernel is homogeneous, the current label has degree one, and multiplication by it is injective on the upper stalk. All pieces are finite-dimensional and the selected-kernel series converges. The [[node:kl.algebra.saturated_image_hilbert|saturated-image Hilbert theorem]] therefore gives
\[
H_J(q)=(1-q)H_{K_y(H)}(q).
\]

### Step 3. Account for the homogeneous correction map

The upper image \(J\) is homogeneous, as the image of a homogeneous submodule under a degree-zero restriction. The [[node:kl.algebra.shifted_image_hilbert|homogeneous-image shift theorem]] applies to the injective degree-\(d\) map \(\Phi\), with \(q\ne0\) and the convergent series of \(J\). It gives
\[
H_{\Phi(J)}(q)=q^dH_J(q)
=q^d(1-q)H_{K_y(H)}(q).
\]
It also proves homogeneity of \(\Phi(J)\).

### Step 4. Compare the two embedded submodules degree by degree

The inclusion \(I\subseteq\Phi(J)\) gives
\(I_n\subseteq\Phi(J)_n\).
Their finite dimensions satisfy
\[
\dim_{\mathbb R}I_n\le\dim_{\mathbb R}\Phi(J)_n.
\]
Multiplying by \(q^n>0\) and summing the convergent series gives
\(H_I(q)\le H_{\Phi(J)}(q)\).
Substitution of Steps 1 and 3 proves the claimed bound.

### Step 5. Detect equality of the embedded images

If the numerical bound is an equality, Steps 1 and 3 give \(H_I(q)=H_{\Phi(J)}(q)\). The Hilbert defect has terms
\[
\bigl(\dim_{\mathbb R}\Phi(J)_n-\dim_{\mathbb R}I_n\bigr)q^n\ge0.
\]
Their sum is zero, so each term vanishes. Positivity of \(q^n\) and finite-dimensional inclusion give \(I_n=\Phi(J)_n\) for every \(n\).

The larger submodule \(\Phi(J)\) is homogeneous. Every vector in it is a finite sum of components in these common pieces, each of which lies in \(I\). Therefore \(\Phi(J)\subseteq I\). Combining with the given inclusion gives equality of the two actual submodules. This is the [[node:kl.sheaves.hilbert_detection|Hilbert equality-detection theorem]] applied to these images.

Conversely, \(I=\Phi(J)\) makes their Hilbert values equal. Steps 1 and 3 then give equality in the numerical bound.

### Step 6. Verify the actual Bruhat-sheaf specialization

For the actual boundary sheaf, root labels are homogeneous of degree one. The incoming-label regularity proof in the [[node:kl.notes.upper_image_free|upper-image freeness theorem]] gives regularity of the current label on every selected outgoing upper edge module.

The upper stalk is free over the polynomial domain and the root label is nonzero, so multiplication by that label is injective there. The [[node:kl.local.edge_factor_action_properties|correction-action theorem]] gives the required homogeneity and injectivity of the actual correction map.

Thus all hypotheses besides the explicitly supplied image inclusion hold for the actual Bruhat sheaf. Applying Steps 1–5 proves the source's `actual_edge_increment_le` and `actual_edge_increment_eq_iff`.

## A strict bound with a one-dimensional defect

As an illustrative example of the generic theorem, take the one-edge graph \(x\to y\), with \(A=\mathbb R[X,Y,Z]\). Give the lower stalk two free basis vectors of degree one, the upper stalk \(A\) with its generator in degree zero, and the edge module \(C=A/(Z)\).

Let the lower map send the two basis vectors to \(\overline X,\overline Y\), and let the upper map be the quotient map. Use the label \(Z\), empty outgoing selections, and \(\Phi=\operatorname{id}_C\), of degree zero. Then
\[
I=(\overline X,\overline Y)\subseteq C=J,\qquad C/I=\mathbb R
\]
in degree zero. Hence
\[
H_J(q)=\frac1{(1-q)^2},\qquad H_I(q)=\frac1{(1-q)^2}-1.
\]
The raw Hilbert bound has a positive deficit of \(1\). At \(q=1/2\), the lower increment is \(3\) and its upper bound is \(4\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.upper_image_value`: [Support.lean:1315](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1315).

`OAI.KLInvariance.MomentGraph.GradedSheaf.shifted_upperImage_value`: [PositiveTransfer.lean:388](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L388).

`OAI.KLInvariance.MomentGraph.GradedSheaf.edge_increment_le`: [PositiveTransfer.lean:410](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L410).

`OAI.KLInvariance.MomentGraph.GradedSheaf.edge_increment_eq_iff`: [PositiveTransfer.lean:433](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L433).

`OAI.KLInvariance.BruhatGraph.actual_edge_increment_le`: [PositiveTransfer.lean:479](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L479).

`OAI.KLInvariance.BruhatGraph.actual_edge_increment_eq_iff`: [PositiveTransfer.lean:500](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L500).

`OAI.KLInvariance.BruhatGraph.label_regular_stalk`: [Support.lean:1353](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1353).
