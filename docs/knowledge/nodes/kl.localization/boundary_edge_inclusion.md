---
id: kl.local.boundary_edge_inclusion
title: The global inclusion for actual ambient boundary-sheaf edge images
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.ambient_later_edges
- kl.notes.upper_image_free
- kl.algebra.scalar_image_free
- kl.local.outgoing_product_image
- kl.local.root_factor_divisibility
- kl.local.scaled_image_denominator
- kl.local.plane_denominator_membership
- kl.local.ambient_plane_scaled_images
- kl.local.edge_factor_action_properties
lean:
  repository: openai-kl
  modules:
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.BruhatGraph.boundary_edge_image_le
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:1045
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.boundary_edge_image_le
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, finiteness and freeness hypotheses, original embedded
    submodules, localization multipliers and schedule assumptions explicit?
  verdict: Verified the exact [1,b] boundary sheaf, source-above-u condition and common
    target threshold; checked C-actions and target freeness, explicit multiplier f
    times the outgoing product, root classification and all plane-denominator hypotheses
    before the final inclusion.
tags:
- Kazhdan-Lusztig
- global-inclusion
---

# The global inclusion for actual ambient boundary-sheaf edge images

Fix finite-generator real Coxeter systems \(W,W'\), an interval order isomorphism
\(\varphi:[u,b]_W\simeq[u',b']_{W'}\),
and a finite real basis of the source extended realization. Let \(A\) be the polynomial coefficient algebra and \(\mathcal B_b\) the underlying \(A\)-module boundary sheaf on \([1,b]_W\).

Choose an actual edge \(e:x\to_Wy\) with \(u\le_Wx\). Let \(a\) be its positive source root and \(\alpha'_{\varphi,e}\) its mapped edge root. Write \(\lambda(a)\) for the root polynomial. Put
\[
T=T_{\varphi,\alpha'_{\varphi,e}},\qquad
F=T(x),\qquad G=T(y),
\]
where \(T\) is the ambient later-edge set and \(T(x),T(y)\) are its outgoing selections.

Inside \(N=\mathcal B_b^e\), define
\[
I=\rho_e^-(K_x^{\mathcal B_b}(F)),\qquad
J=\rho_e^+(K_y^{\mathcal B_b}(G)),\qquad
f=F_{x,a}\in A.
\]
The polynomial \(F_{x,a}\) is the fixed correction lift. Assume the upper selected kernel \(K_y^{\mathcal B_b}(G)\) is free over \(A\). Then
\[
I\subseteq fJ.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Prime divisors of one multiplier organize the local-to-global step.**

**OpenAI notes:** The notes use membership in a free target at height-one primes. Primes avoiding all reduced root labels give the full localized edge module; root primes use the dihedral local comparison. [edge:lattice](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L26), [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The proof fixes one global multiplier, the correction lift times the outgoing label product. A prime dividing its reduction is associated to a reduced root and receives the corresponding plane witness. A prime not dividing it uses the global multiplier itself. The free-target prime-removal theorem then gives membership. [TerminalKernels:992](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L992), [TerminalKernels:1045](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1045).

**Role in the proof:** The Blueprint follows these two prime cases and checks quotient-ring freeness, torsion-free cancellation, nonzero global multiplication and every local witness before concluding the inclusion.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Establish the coefficient action and the free target

Set \(C=A/(\lambda(a))\), and write \(S=fJ\subseteq N\). The [[node:kl.notes.upper_image_free|upper-image freeness theorem]] gives a compatible \(C\)-action on \(N\), makes \(N\) free over \(C\), and makes the actual upper image \(J_C\) free over \(C\) using the assumed freeness of the selected upper kernel.

The ring \(C\) is a domain, so its free module \(N\) is torsion-free. The [[node:kl.local.edge_factor_action_properties|correction-action theorem]] gives injectivity of multiplication by the fixed lift \(f\) on \(N\). The [[node:kl.algebra.scalar_image_free|scalar-image freeness theorem]] therefore makes \(S_C=(fJ)_C\) free over \(C\).

### Step 2. Construct a nonzero global multiplier

Let
\[
g=\prod_{h\in G}\lambda(a_h),\qquad c=fg,
\]
the outgoing label product followed by the correction factor.

The boundary sheaf satisfies label annihilation and has surjective upper restrictions. The [[node:kl.local.outgoing_product_image|outgoing-product image theorem]] gives \(gN\subseteq J\). Hence for every \(z\in N\),
\[
cz=f(gz)\in fJ=S.
\]
The [[node:kl.local.root_factor_divisibility|root-factor divisibility theorem]] gives \(\overline c\ne0\) in \(C\).

### Step 3. Classify the prime divisors of this multiplier

The same [[node:kl.local.root_factor_divisibility|root-factor theorem]] applies to the actual edge \(e\) and outgoing selection \(G\). Every prime \(\pi\mid\overline c\) is associated to \(\overline{\lambda(\beta)}\) for a positive root \(\beta\ne a\).

This verifies the root-factor hypothesis of plane-denominator membership for the particular multiplier \(c\) constructed in Step 2.

### Step 4. Obtain a multiplier outside each plane prime

Fix \(z\in I\), and let \(\beta\ne a\) be any positive source root. Put
\[
P=\operatorname{span}\{a,\beta\},\qquad R_P=A_{\mathfrak p_P}.
\]
Write \(\eta_P:A\to R_P\) for localization. The [[node:kl.local.ambient_plane_scaled_images|actual ambient plane-comparison theorem]] applies to the same edge, threshold and endpoint selections. It gives equality of the localized lower image with \(\eta_P(f)\) times the localized upper image.

Apply the [[node:kl.local.scaled_image_denominator|scaled-image denominator theorem]] with original ring \(A\), localization \(R_P\), multiplicative set \(A\setminus\mathfrak p_P\), scalar \(f\), and the chosen lower-image vector \(z\). It supplies
\[
s\notin\mathfrak p_P,\qquad sz\in fJ=S.
\]
This works for every positive \(\beta\ne a\).

### Step 5. Remove all denominators for the chosen lower-image vector

Apply plane-denominator membership to \(N,S,z,c\). Step 1 supplies the compatible actions, torsion-free ambient module and free target. Step 2 supplies a nonzero reduced multiplier and \(cz\in S\). Step 3 classifies its prime divisors, and Step 4 supplies all plane witnesses.

The theorem gives \(z\in S\). Since the choice \(z\in I\) was arbitrary, every vector in the lower image belongs to \(fJ\), proving \(I\subseteq fJ\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.boundary_edge_image_le`: [TerminalKernels.lean:1045](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1045).
