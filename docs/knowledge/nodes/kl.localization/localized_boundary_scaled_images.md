---
id: kl.local.localized_boundary_scaled_images
title: Scaled image equality in the localized boundary sheaf
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.localized_coset
- kl.local.localized_decomposition
- kl.local.coset_model_scaled_images
- kl.local.model_sum_scaled_images
- kl.local.image_isomorphism_transport
- kl.detail.scaled_images
lean:
  repository: openai-kl
  modules:
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.localized_boundary_scaledImages
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:245
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.localized_boundary_scaledImages
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the coefficient actions, actual modules, interval bounds, selected sets,
    finite-basis assumptions and support cases explicit?
  verdict: Read the actual localized-boundary proof, verified finite edge instances
    and the exact decomposition input, then expanded the common-scalar model-sum argument
    and both-image transport through one injective edge component.
tags:
- Kazhdan-Lusztig
- embedded-images
- local-comparison
---

# Scaled image equality in the localized boundary sheaf

Fix finite-generator real Coxeter systems \(W,W'\), an interval order isomorphism
\(\varphi:[u,b]_W\simeq[u',b']_{W'}\),
and a finite real basis of the source extended realization. Let \(A\) be its polynomial coefficient algebra and \(\mathcal B_b\) the underlying \(A\)-module sheaf of the boundary sheaf on \([1,b]_W\).

Choose a plane basis \(B\) for \(P\), its induced subgroup \(D\), and a representative \(a_0\) satisfying \(\ell_W(a_0)\le\ell_W(da_0)\) for every \(d\in D\). Let
\[
K=\{d\in D:da_0\le_Wb\},\qquad
j:K\longrightarrow[1,b]_W,\quad j(d)=da_0.
\]
With \(R_P=A_{\mathfrak p_P}\) and localization map \(\eta_P:A\to R_P\), define the localized coset sheaf
\[
\mathcal C=j^*(R_P\otimes_A\mathcal B_b).
\]

For an edge \(e:x\to_Dy\) of \(K\) with \(u\le_Wxa_0\), let \(a\) be its actual positive source root, \(F_e,H_e\) its two coset later-edge selections, and
\[
r_e=\eta_P(F_{xa_0,a}).
\]
Here \(F_{xa_0,a}\) is the polynomial lift of the correction factor. Then
\[
L_e^{\mathcal C}(F_e)=r_e\,U_e^{\mathcal C}(H_e).
\]
Here \(L_e^{\mathcal C}(F_e)=\rho_e^-(K_x^{\mathcal C}(F_e))\) and \(U_e^{\mathcal C}(H_e)=\rho_e^+(K_y^{\mathcal C}(H_e))\) are the lower and upper images of the selected kernels, inside the one localized edge module
\[
\mathcal C^e=R_P\otimes_A\mathcal B_b^{\,j_E(e)}.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**One edge component carries both images and the common scalar.**

**OpenAI notes:** The notes decompose the localized sheaf, compare both image ideals in every supported model copy, and use the same linear edge component of the decomposition to recover equality in the original localized edge module. This calculation appears within the edge-image proposition, whose global conclusion assumes upper-kernel freeness. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** A ModelSum argument gives the common-scalar equality in the model sum; Iso.scaledImages transports it to the actual localized boundary sheaf. Selected-kernel pullback then gives the ambient equality. Finally exists_coset_edge supplies coordinates for any actual edge in a plane. These local equalities are proved before upper-kernel freeness is used in the global inclusion. [TerminalKernels:245](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L245), [TerminalKernels:418](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L418), [TerminalKernels:462](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L462).

**Role in the proof:** The Blueprint follows the identical stalk and edge modules through each map, verifies the exact selections and root/factor identities, and states the local equality with its own hypotheses.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Apply the actual localized decomposition

The coset vertex set is finite, since it injects into the finite ambient interval \([1,b]\). Its edge set is a subtype of the finite set of vertex pairs, and hence finite too.

The [[node:kl.local.localized_decomposition|localized boundary-decomposition theorem]] applies to the actual sheaf \(\mathcal C\). It supplies a finite ungraded model sum \(\mathcal M\), built from the coset structure sheaves, and an \(R_P\)-linear sheaf isomorphism
\[
\psi:\mathcal C\xrightarrow{\sim}\mathcal M.
\]
The theorem has already verified the required finite free stalks, upper quotients, flabbiness and generation for this localized boundary sheaf.

### Step 2. Establish the same scalar equality in every model

For each center \(c\in K\), the [[node:kl.local.coset_model_scaled_images|coset-model scaled-image theorem]] gives
\[
L_e^{\mathcal O_c}(F_e)=r_e\,U_e^{\mathcal O_c}(H_e).
\]
Every copy uses the same edge, selections and scalar \(r_e\). The formula includes centers where the edge module vanishes.

The [[node:kl.local.model_sum_scaled_images|model-sum scaled-image theorem]] therefore applies at every step of the finite model-sum construction and gives
\[
L_e^{\mathcal M}(F_e)=r_e\,U_e^{\mathcal M}(H_e).
\]
Its proof combines witnesses coordinate by coordinate; a single scalar multiplies every coordinate.

### Step 3. Carry both embedded images through one edge component

The [[node:kl.local.image_isomorphism_transport|sheaf-isomorphism image theorem]] identifies
\[
\psi_e(L_e^{\mathcal C}(F_e))=L_e^{\mathcal M}(F_e),\qquad
\psi_e(U_e^{\mathcal C}(H_e))=U_e^{\mathcal M}(H_e).
\]
Both equalities use the same edge map \(\psi_e\); their endpoint kernel identifications follow from the corresponding restriction squares.

Because \(\psi_e\) is \(R_P\)-linear, it commutes with multiplication by \(r_e\). Consequently
\[
\begin{aligned}
\psi_e(L_e^{\mathcal C}(F_e))
&=L_e^{\mathcal M}(F_e)\\
&=r_e\,U_e^{\mathcal M}(H_e)\\
&=r_e\,\psi_e(U_e^{\mathcal C}(H_e))\\
&=\psi_e(r_e\,U_e^{\mathcal C}(H_e)).
\end{aligned}
\]

### Step 4. Pull the equality back to the actual localized edge

The map \(\psi_e\) is injective. For a vector in either of the two submodules of \(\mathcal C^e\), equality of their images in Step 3 supplies a vector in the other submodule with the same \(\psi_e\)-image. Injectivity identifies these vectors. This proves both containments and hence
\[
L_e^{\mathcal C}(F_e)=r_e\,U_e^{\mathcal C}(H_e).
\]
Only the ungraded \(R_P\)-linearity of the decomposition is used in these image equalities.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.localized_boundary_scaledImages`: [TerminalKernels.lean:245](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L245).
