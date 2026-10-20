---
id: kl.local.edge_inclusion
title: The edge-image inclusion for a chronological schedule suffix
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.boundary_edge_inclusion
- kl.paths.schedule_suffixes
- kl.sheaves.upper_interval_kernels
- kl.detail.transported_schedule
- kl.local.edge_factor_action_properties
- kl.paths.plane_degree
lean:
  repository: openai-kl
  modules:
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.BruhatGraph.intervalBoundary
  - OAI.KLInvariance.BruhatGraph.schedule_edge_image_le
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:1123
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.intervalBoundary
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:1126
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.schedule_edge_image_le
  - artifact: openai-kl-paper
    locator: 5. Comparison of edge images; sec:edge
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, finiteness and freeness hypotheses, original embedded
    submodules, localization multipliers and schedule assumptions explicit?
  verdict: Replaced the broad parent outline with the exact restricted canonical boundary
    sheaf, suffix and upper-kernel freeness hypotheses; checked both condition-set
    equalities, literal kernel transfer, ambient inclusion and unchanged root/scalar/restriction
    maps.
tags:
- Kazhdan-Lusztig
- global-inclusion
---

# The edge-image inclusion for a chronological schedule suffix

Fix finite-generator real Coxeter systems \(W,W'\), \(u\le_Wb\), an interval order isomorphism
\(\varphi:[u,b]_W\simeq[u',b']_{W'}\),
and a finite real basis of the source extended realization. Let \(A\) be the polynomial coefficient algebra.

Let \(\mathcal B_b\) be the boundary sheaf on \([1,b]_W\), and let \(\mathcal B^I\) be its restriction to the upper interval \(I=[u,b]_W\). This is the source's `intervalBoundary`.

Suppose \(e:x\to y\) followed by a list \(q\) is a suffix of the chronological schedule. Let
\[
L_x=K_x^{\mathcal B^I}(\mathcal R_q(x)),\qquad
L_y=K_y^{\mathcal B^I}(\mathcal R_q(y)),
\]
where \(\mathcal R_q(v)\) is the remaining outgoing selection. Assume \(L_y\) is free over \(A\).

If \(a_e\) is the positive source root of \(e\), and \(F_{x,a_e}\in A\) is the fixed correction lift, then
\[
\rho_e^-(L_x)\subseteq
F_{x,a_e}\,\rho_e^+(L_y)
\]
inside the actual edge module \((\mathcal B^I)^e\). Multiplication by this lift is the source's `edgeFactorMap`.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Exact suffix conditions specialize the ambient inclusion.**

**OpenAI notes:** The notes formulate the current endpoint conditions as the edges strictly later than the current edge in a transported reflection order. [dih:count](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L464), [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The actual schedule is a complete duplicate-free sorted list with a diagonal lexicographic score; its reverse is chronological. Two sorted-list lemmas, same-source score injectivity and consecutive-edge score inequality identify both suffix selections with the ambient later-edge set. Upper-interval restriction then transfers both kernels and the upper freeness hypothesis. [EdgeLocalization:40](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L40), [PositiveTransfer:1228](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1228), [PositiveTransfer:1225](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1225), [PositiveTransfer:1306](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1306), [PositiveTransfer:1315](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1315), [TerminalKernels:1126](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1126).

**Role in the proof:** The Blueprint states the exact suffix assumption and distinguishes weak list ordering from the strict score test at the two current endpoints.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Identify the ambient edge and the common target threshold

Let \(\iota:I\hookrightarrow[1,b]_W\) be the upper-interval inclusion, and let \(\widehat e=\iota_E(e)\). Its endpoints are the same group elements \(x,y\), and its source satisfies \(u\le_Wx\).

Let \(\alpha'_e\) be the positive root of \(\varphi(x)\to\varphi(y)\), and set
\[
T=T_{\varphi,\alpha'_e}.
\]
The mapped edge root of \(\widehat e\) is exactly \(\alpha'_e\), because both are defined from this target edge.

### Step 2. Identify the two remaining condition sets

The [[node:kl.paths.schedule_suffixes|schedule-suffix theorem]] applies to the given suffix. It identifies \(\mathcal R_q(x)\) with the outgoing edges at \(x\) whose ambient inclusions belong to \(T\), and gives the corresponding identification at \(y\).

The [[node:kl.sheaves.upper_interval_kernels|upper-interval kernel theorem]] then gives literal equalities in the corresponding stalk modules:
\[
L_x=K_x^{\mathcal B_b}(T(x)),\qquad
L_y=K_y^{\mathcal B_b}(T(y)).
\]
Its hypotheses hold because \(I\) is an upper interval and \(\mathcal B^I\) is the restriction of this actual boundary sheaf. An outgoing edge from a vertex above \(u\) also ends above \(u\), so every relevant ambient condition is represented in the restriction.

### Step 3. Transfer freeness and apply the ambient inclusion

The second equality in Step 2 identifies the assumed free \(A\)-module \(L_y\) with the ambient upper selected kernel. Hence the [[node:kl.local.boundary_edge_inclusion|global ambient edge-inclusion theorem]] applies to \(\widehat e\), its source bound and the common threshold \(T\). It gives
\[
\rho_{\widehat e}^{\mathcal B_b,-}
\bigl(K_x^{\mathcal B_b}(T(x))\bigr)
\subseteq
F_{x,a_e}\,
\rho_{\widehat e}^{\mathcal B_b,+}
\bigl(K_y^{\mathcal B_b}(T(y))\bigr).
\]

### Step 4. Return both images to the restricted edge module

Restriction retains the stalks at \(x,y\), the edge module at \(e\), and its lower and upper maps. The root of \(\widehat e\) is \(a_e\), since its endpoint pair is unchanged. Therefore the scalar \(F_{x,a_e}\) is also the same polynomial lift in both descriptions.

Substitute the two kernel equalities of Step 2 and the retained restriction maps into Step 3. The resulting inclusion is exactly
\[
\rho_e^-(L_x)\subseteq F_{x,a_e}\rho_e^+(L_y).
\]
This proves the schedule-suffix edge-image inclusion.

The previously established [[node:kl.local.edge_factor_action_properties|correction-action theorem]] gives homogeneity and the degree shift \((\ell_W(y)-\ell_W(x)-1)/2\) for multiplication by this lift along the actual edge.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.intervalBoundary`: [TerminalKernels.lean:1123](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1123).

`OAI.KLInvariance.BruhatGraph.schedule_edge_image_le`: [TerminalKernels.lean:1126](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1126).
