---
id: kl.local.ambient_plane_scaled_images
title: Scaled image equality at every actual root-plane localization
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.ambient_later_edges
- kl.local.actual_edge_coset
- kl.local.localized_boundary_scaled_images
- kl.local.localized_coset_kernels
- kl.dihedral.plane_basis_existence
- kl.local.coset_edge_reduction
- kl.local.edge_factor_lift
- kl.detail.edge_images
- kl.detail.scaled_images
lean:
  repository: openai-kl
  modules:
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.ambient_boundary_scaledImages
  - OAI.KLInvariance.BruhatGraph.boundary_plane_scaledImages
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:418
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.ambient_boundary_scaledImages
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:462
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.boundary_plane_scaledImages
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the coefficient actions, actual modules, interval bounds, selected sets,
    finite-basis assumptions and support cases explicit?
  verdict: 'Expanded both actual ambient comparison theorems: finite basis/system
    hypotheses, arbitrary beta distinct from current root, existence of coset edge,
    source-bound transfer, exact source/mapped roots and fixed scalar, both selected-kernel
    identities and the two restrictions into one identical edge module.'
tags:
- Kazhdan-Lusztig
- embedded-images
- local-comparison
---

# Scaled image equality at every actual root-plane localization

Fix finite-generator real Coxeter systems \(W,W'\) and an interval order isomorphism
\(\varphi:[u,b]_W\simeq[u',b']_{W'}\).
Choose a finite real basis of the source extended realization, let \(A\) be its polynomial coefficient algebra, and let \(\mathcal B_b\) be the underlying \(A\)-module boundary sheaf on \([1,b]_W\).

Let \(e:x\to_Wy\) be an actual edge of this ambient graph with \(u\le_Wx\), and let \(a\) be its positive root. Choose any positive source root \(\beta\ne a\), and put
\[
P=\operatorname{span}_{\mathbb R}\{a,\beta\},\qquad
R_P=A_{\mathfrak p_P},\qquad
\mathcal B_R=R_P\otimes_A\mathcal B_b.
\]
Write \(\eta_P:A\to R_P\) for localization. Let
\[
T=T_{\varphi,\alpha'_{\varphi,e}}
\]
be the ambient later-edge set for the mapped edge root of the current edge, and let \(T_x,T_y\) be its outgoing selections at \(x,y\).

Then, inside the actual localized edge module
\[
\mathcal B_R^e=R_P\otimes_A\mathcal B_b^e,
\]
one has
\[
\rho_e^-\bigl(K_x^{\mathcal B_R}(T_x)\bigr)
=
\eta_P(F_{x,a})\,
\rho_e^+\bigl(K_y^{\mathcal B_R}(T_y)\bigr).
\]
Here \(K\) denotes the selected kernel, \(\rho_e^\pm\) the lower and upper restriction maps, and \(F_{x,a}\) the fixed polynomial lift of the correction factor. This equality is the actual plane-local input to the global edge-image inclusion.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**One edge component carries both images and the common scalar.**

**OpenAI notes:** The notes decompose the localized sheaf, compare both image ideals in every supported model copy, and use the same linear edge component of the decomposition to recover equality in the original localized edge module. This calculation appears within the edge-image proposition, whose global conclusion assumes upper-kernel freeness. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** A ModelSum argument gives the common-scalar equality in the model sum; Iso.scaledImages transports it to the actual localized boundary sheaf. Selected-kernel pullback then gives the ambient equality. Finally exists_coset_edge supplies coordinates for any actual edge in a plane. These local equalities are proved before upper-kernel freeness is used in the global inclusion. [TerminalKernels:245](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L245), [TerminalKernels:418](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L418), [TerminalKernels:462](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L462).

**Role in the proof:** The Blueprint follows the identical stalk and edge modules through each map, verifies the exact selections and root/factor identities, and states the local equality with its own hypotheses.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Choose the plane basis and relative coordinates of the actual edge

The distinct positive roots \(a,\beta\) are independent, so they span a root plane. The [[node:kl.dihedral.plane_basis_existence|plane-basis existence theorem]] supplies a basis datum \(B\) for \(P\), with induced subgroup \(D\).

The [[node:kl.local.actual_edge_coset|actual-edge coset theorem]] applies because \(a\in P\). It supplies a least representative \(a_0\), a coset graph \(K\), and an edge
\[
d:g\to_Dh,\qquad ga_0=x,\quad ha_0=y,\quad j_E(d)=e.
\]
The required source bound for the local comparison is
\(u\le_Wga_0\), which is exactly the given bound \(u\le_Wx\).

### Step 2. Identify the current roots, threshold and scalar

Write \(a_d\) for the source root of \(d\). It equals the ambient root \(a\): their left reflections are
\[
hg^{-1}=(ha_0)(ga_0)^{-1}=yx^{-1}.
\]
The [[node:kl.local.coset_edge_reduction|coset edge-reduction theorem]] makes this the exact root equality used by the polynomial labels.

The mapped-root compatibility in the [[node:kl.local.ambient_later_edges|ambient later-edge definition]] gives
\[
\alpha'_{\mathrm{coset},d}=\alpha'_{\varphi,e}.
\]
Consequently the correction scalar used for \(d\) is
\[
\eta_P(F_{ga_0,a_d})=\eta_P(F_{x,a}),
\]
and its two selected edge sets use exactly the threshold defining \(T\).

### Step 3. Apply the localized boundary comparison on the coset

Let \(j\) be the coset graph map with \(j_V(g)=ga_0\), and let
\(\mathcal C=j^*\mathcal B_R\)
be the actual localized coset sheaf. The [[node:kl.local.localized_boundary_scaled_images|localized-boundary scaled-image theorem]] gives
\[
\rho_d^{\mathcal C,-}(K_g^{\mathcal C}(F_d))
=
\eta_P(F_{x,a})\,
\rho_d^{\mathcal C,+}(K_h^{\mathcal C}(H_d)).
\]
Its hypotheses hold: both systems have finite generating sets, the chosen coefficient basis is finite, \(a_0\) is least, and the source of \(d\) satisfies the ambient lower bound checked in Step 1.

### Step 4. Identify the selected kernels in the same stalk modules

The coset-pullback identity for the ambient later-edge set gives
\[
F_d=\{f\in\operatorname{Out}_K(g):j_E(f)\in T\},\qquad
H_d=\{f\in\operatorname{Out}_K(h):j_E(f)\in T\}.
\]
The [[node:kl.local.localized_coset_kernels|selected-kernel theorem on the localized coset]] therefore applies at \(g\) and \(h\), with the same ambient set \(T\):
\[
K_g^{\mathcal C}(F_d)=K_x^{\mathcal B_R}(T_x),\qquad
K_h^{\mathcal C}(H_d)=K_y^{\mathcal B_R}(T_y).
\]
These are equalities inside the identical stalk modules given by pullback.

The theorem uses the upper-quotient property of the actual boundary sheaf. After localization, a selected ambient edge whose root lies outside \(P\) has a unit label and zero edge module, so its equation is automatic. Every surviving outgoing edge has a coset lift. Thus the relative and ambient selected equations impose exactly the same kernel.

### Step 5. Identify both restriction maps and substitute

By definition of pullback,
\[
\mathcal C^d=\mathcal B_R^{j_E(d)}=\mathcal B_R^e.
\]
Its lower restriction is the lower restriction of \(\mathcal B_R\) at \(e\), with \(ga_0=x\); its upper restriction is the upper restriction at the same edge, with \(ha_0=y\).

Substitute the two kernel equalities from Step 4 into Step 3, and use these restriction-map identities. The lower side becomes
\(\rho_e^-(K_x^{\mathcal B_R}(T_x))\);
the upper side becomes
\(\eta_P(F_{x,a})\rho_e^+(K_y^{\mathcal B_R}(T_y))\).
This proves the required equality of embedded submodules.

The source first packages this substitution for a specified coset edge as `ambient_boundary_scaledImages`. Choosing the coset coordinates of an arbitrary actual edge gives `boundary_plane_scaledImages`.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.ambient_boundary_scaledImages`: [TerminalKernels.lean:418](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L418).

`OAI.KLInvariance.BruhatGraph.boundary_plane_scaledImages`: [TerminalKernels.lean:462](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L462).
