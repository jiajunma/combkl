---
id: kl.comparison.schedule_upper_freeness
title: The complete schedule comparison under upper-kernel freeness
kind: theorem
status: proved
primary_topic: kl.invariance
topics:
- kl.invariance
uses:
- kl.detail.schedule_state
- kl.detail.schedule_comparison
- kl.paths.schedule_suffixes
- kl.local.edge_inclusion
- kl.sheaves.upper_interval_kernels
- kl.local.edge_factor_action
- kl.sheaves.interval_boundary
lean:
  repository: openai-kl
  modules:
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.BruhatGraph.intervalBoundary
  - OAI.KLInvariance.BruhatGraph.schedule_edge_image_le
  - OAI.KLInvariance.BruhatGraph.schedule_comparison_of_upper_freeness
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
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:1171
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.schedule_comparison_of_upper_freeness
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the state, list order, suffix hypotheses, parameter range and exact
    source conclusion stated explicitly?
  verdict: Read intervalBoundary and schedule_edge_image_le through both actual kernel
    equalities, transfer of upper freeness, ambient inclusion and correction-map identification;
    then followed schedule_comparison_of_upper_freeness and double reversal.
tags:
- Kazhdan-Lusztig
- comparison_and_freeness
---

# The complete schedule comparison under upper-kernel freeness

Let \(W,W'\) be Coxeter systems with finite simple-generator sets, let \(u\le_Wb\), and let
\[
\phi:[u,b]_W\xrightarrow{\sim}[u',b']_{W'}
\]
be an order isomorphism. Choose a finite real basis \(\Sigma\) of the source extended realization, with coefficient algebra \(A=\mathbb R[X_i:i\in\Sigma]\).

Let \(\mathcal C\) be the actual boundary sheaf on \([1,b]_W\), and let
\(\mathcal B=\mathcal C|_{[u,b]_W}\) be its upper-interval restriction, called `intervalBoundary`. Write
\[
P=\operatorname{chronologicalSchedule}(\phi),\qquad
Q=\operatorname{transportedSchedule}(\phi).
\]
The source defines \(P=Q^{\mathrm{rev}}\), so \(P^{\mathrm{rev}}=Q\).

For every suffix \(e::q\preceq_{\mathrm{suf}}P\), assume that the \(A\)-module
\[
K^{\mathcal B}_{r(e)}\bigl(F_q(r(e))\bigr)
\tag{1}
\]
is free. Here \(r(e)\) is the upper endpoint, \(F_q\) is the outgoing selection determined by the tail \(q\), and \(K^{\mathcal B}\) is the selected kernel in \(\mathcal B\).
For \(0<t<1\) and \(T=t^{-1}-t\),
\[
D_{[]}(t)\le\mathcal D_Q(T)D_P(t).
\tag{2}
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Actual suffix conditions and the conditional whole-list bound.**

**OpenAI notes:** The comparison processes the increasing edge schedule, retains the equations on unprocessed outgoing edges, and propagates the single-edge estimate through the complete matrix product. [eq:state](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L243), [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275), [eq:comparison](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L298), [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The numerical theorem first accepts any finite list with image inclusion at every nonempty suffix. A separate theorem takes the actual chronological schedule and freeness of each upper suffix kernel. Exact suffix-to-ambient kernel identities let it apply the global edge inclusion before invoking the numerical theorem. [PositiveTransfer:1089](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1089), [PositiveTransfer:1117](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1117), [PositiveTransfer:1148](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1148), [TerminalKernels:1126](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1126), [TerminalKernels:1171](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1171).

**Role in the proof:** The Blueprint spells out the set-valued remaining conditions, source and non-source coordinate changes, suffix quantifiers and reversed product. The source-specific upper-freeness step has its own entry.
<!-- source-comparison:end -->

*Proof.*

### Step 1. The current edge in the ambient interval

Fix \(e::q\preceq_{\mathrm{suf}}P\), and put \(x=s(e)\), \(y=r(e)\). The upper-interval inclusion sends \(e\) to an edge \(\bar e\) of \([1,b]_W\), with the same two underlying group elements. The restricted sheaf has the same stalks, edge module and restriction maps at these vertices and this edge.

Let \(\alpha'\) be the positive root labelling the transported target edge \(\phi(e)\). Write \(L_{\alpha'}\) for `ambientLater φ α'`, the ambient outgoing-edge selection defined by target-root score strictly after \(\alpha'\).

### Step 2. The two selected kernels

The [[node:kl.paths.schedule_suffixes|chronological suffix identification]] applies because \(e::q\) is a suffix of the actual chronological schedule. At each of \(x,y\), it identifies the outgoing edges in \(q\) with the ambient strictly-later selection under upper-interval inclusion.

The [[node:kl.sheaves.upper_interval_kernels|upper-interval kernel transport]] preserves these selected kernels. The resulting equalities are
\[
\begin{aligned}
K_x^{\mathcal B}(F_q(x))
 &=K_x^{\mathcal C}(L_{\alpha'}(x)),\\
K_y^{\mathcal B}(F_q(y))
 &=K_y^{\mathcal C}(L_{\alpha'}(y)).
\end{aligned}
\tag{3}
\]
The notation \(L_{\alpha'}(z)\) means the outgoing edges of the ambient selection at \(z\). Both sides of each equality are submodules of the same stalk. In the source, these equalities combine `remainingConditions_source_ambient` or `remainingConditions_target_ambient` with `restrictBoundary_kernel`.

By hypothesis (1), the left side of the second equality is free. Transporting a basis across that equality makes the ambient upper kernel on its right free.

### Step 3. The ambient global edge inclusion

The [[node:kl.local.edge_inclusion|global edge inclusion]] for \(\bar e\) uses the actual ambient boundary sheaf, the order isomorphism \(\phi\), the root \(\alpha'\), the two strict-later selections, and freeness of the ambient upper selected kernel. All of these have been supplied in Steps 1–2. It yields
\[
\rho_{\bar e}^-
 \bigl(K_x^{\mathcal C}(L_{\alpha'}(x))\bigr)
\subseteq
\mu_{\bar e}\rho_{\bar e}^+
 \bigl(K_y^{\mathcal C}(L_{\alpha'}(y))\bigr).
\tag{4}
\]
Here \(\mu_{\bar e}\) is multiplication by the corresponding edge factor on the ambient edge module.

Substitute (3) into (4). The restrictions agree under upper-interval inclusion, and the polynomial lift defining the edge-factor map uses the same source vertex and root. Thus the correction maps also agree. We obtain the actual inclusion
\[
\rho_e^-\bigl(K_x^{\mathcal B}(F_q(x))\bigr)
\subseteq
\mu_e\rho_e^+\bigl(K_y^{\mathcal B}(F_q(y))\bigr)
\tag{5}
\]
inside \(\mathcal B^e\). This is `schedule_edge_image_le`.

### Step 4. The numerical theorem for every suffix

The choice of \(e::q\) was arbitrary. Consequently (5) supplies the inclusion required by the [[node:kl.detail.schedule_comparison|full transfer inequality]] at every suffix of \(P\). Apply that theorem with \(\mathcal B\), list \(P\), and \(0<t<1\):
\[
D_{[]}(t)\le\mathcal D_{P^{\mathrm{rev}}}(T)D_P(t).
\]
Finally \(P^{\mathrm{rev}}=(Q^{\mathrm{rev}})^{\mathrm{rev}}=Q\), proving (2).

The freeness hypothesis enters in Step 3 through the global edge theorem. The numerical iteration then uses the image inclusions already obtained. In the simultaneous induction, the modules in (1) will be supplied by smaller upper intervals.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.intervalBoundary`: [TerminalKernels.lean:1123](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1123).

`OAI.KLInvariance.BruhatGraph.schedule_edge_image_le`: [TerminalKernels.lean:1126](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1126).

`OAI.KLInvariance.BruhatGraph.schedule_comparison_of_upper_freeness`: [TerminalKernels.lean:1171](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1171).
