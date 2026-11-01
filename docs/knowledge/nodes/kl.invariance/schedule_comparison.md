---
id: kl.detail.schedule_comparison
title: From one-edge bounds to the full transfer inequality
kind: theorem
status: proved
primary_topic: kl.invariance
topics:
- kl.invariance
uses:
- kl.detail.schedule_state
- kl.comparison.edge_increment
- kl.detail.transfer_properties
- kl.local.edge_factor_action
- kl.detail.edge_images
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.SchedulePaths.remaining_state_le
  - OAI.KLInvariance.BruhatGraph.scheduleState_step
  - OAI.KLInvariance.BruhatGraph.scheduleState_le
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:866
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.remaining_state_le
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1117
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.scheduleState_step
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1148
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.scheduleState_le
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
  prompt: Are the state, list order, suffix hypotheses, parameter range and exact
    source conclusion stated explicitly?
  verdict: Read scheduleState_step and scheduleState_le in their full boundary-sheaf
    context, and followed remaining_state_le head/tail induction. Checked every suffix
    inclusion, source/target conditions, arbitrary-list scope and reversed concatenation.
tags:
- Kazhdan-Lusztig
- comparison_and_freeness
---

# From one-edge bounds to the full transfer inequality

Fix a finite-generator Coxeter system \(W\), \(u\le_W b\), a finite real basis \(\Sigma\) of its extended realization, and a boundary sheaf \(\mathcal B\) with top \(b\) on the corresponding polynomially labelled graph of \([u,b]_W\). The coefficient ring is \(A=\mathbb R[X_i:i\in\Sigma]\).

Let \(p\) be a finite list of graph edges. A suffix of \(p\) is a list \(q\) such that \(p=r+\!\!+q\) for some list \(r\); write \(q\preceq_{\mathrm{suf}}p\). For every suffix \(e::q\), put \(x=s(e)\), \(y=r(e)\), where \(s,r\) denote source and target, and define the actual edge images
\[
I_e(q)=\rho_e^-\bigl(K_x(F_q(x))\bigr),\qquad
J_e(q)=\rho_e^+\bigl(K_y(F_q(y))\bigr).
\]
Here \(F_q\) is the remaining-condition set, and \(K\) its selected kernel. Let \(\mu_e:\mathcal B^e\to\mathcal B^e\) be the edge-factor multiplication map `edgeFactorMap`. Assume
\[
I_e(q)\subseteq\mu_e(J_e(q))
\qquad\text{for every }e::q\preceq_{\mathrm{suf}}p.
\tag{1}
\]

For \(0<t<1\), set \(T=t^{-1}-t>0\), and let \(D_q(t)\) be the Hilbert-state vector. Then
\[
D_{[]}(t)\le\mathcal D_{p^{\mathrm{rev}}}(T)D_p(t)
\tag{2}
\]
coordinatewise. The hypothesis (1) is specified for each actual tail \(q\); the conclusion applies to any finite edge list satisfying these hypotheses.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Actual suffix conditions and the conditional whole-list bound.**

**OpenAI notes:** The comparison processes the increasing edge schedule, retains the equations on unprocessed outgoing edges, and propagates the single-edge estimate through the complete matrix product. [eq:state](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L243), [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275), [eq:comparison](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L298), [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The numerical theorem first accepts any finite list with image inclusion at every nonempty suffix. A separate theorem takes the actual chronological schedule and freeness of each upper suffix kernel. Exact suffix-to-ambient kernel identities let it apply the global edge inclusion before invoking the numerical theorem. [PositiveTransfer:1089](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1089), [PositiveTransfer:1117](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1117), [PositiveTransfer:1148](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1148), [TerminalKernels:1126](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1126), [TerminalKernels:1171](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1171).

**Role in the proof:** The Blueprint spells out the set-valued remaining conditions, source and non-source coordinate changes, suffix quantifiers and reversed product. The source-specific upper-freeness step has its own entry.
<!-- source-comparison:end -->

*Proof.*

### Step 1. The states before and after one removal

Fix a suffix \(e::q\), and abbreviate \(x=s(e)\), \(y=r(e)\),
\(F=F_q(x)\), \(H=F_q(y)\).
The [[node:kl.detail.schedule_state|remaining-condition identities]] give
\[
F_{e::q}(x)=F\cup\{e\},\qquad
F_{e::q}(z)=F_q(z)\quad(z\ne x).
\]
The first state is \(D_{e::q}(t)\). After processing \(e\), it is \(D_q(t)\).
Since the edge is strictly increasing, \(x\ne y\), and the second identity applies in particular at \(y\).

### Step 2. The inequality at the source

Apply the [[node:kl.comparison.edge_increment|one-edge Hilbert comparison]] to \(e,F,H\) and inclusion (1). It gives
\[
D_x(t,F)\le D_x(t,F\cup\{e\})+T D_y(t,H).
\]
The first two values are \(D_q(t)_x\) and \(D_{e::q}(t)_x\). At \(y\), the selected set is unchanged, so
\(D_y(t,H)=D_{e::q}(t)_y\).
Substitution yields
\[
D_q(t)_x
\le D_{e::q}(t)_x+T D_{e::q}(t)_y
=\bigl(U_e(T)D_{e::q}(t)\bigr)_x.
\]

### Step 3. Equality at every other coordinate

For \(z\ne x\), the selected sets agree, so
\[
D_q(t)_z=D_{e::q}(t)_z.
\]
The elementary transfer also leaves coordinate \(z\) unchanged. Thus
\[
D_q(t)_z=\bigl(U_e(T)D_{e::q}(t)\bigr)_z.
\]
Together with Step 2 this proves the vector inequality
\[
D_q(t)\le U_e(T)D_{e::q}(t).
\tag{3}
\]
This is `scheduleState_step`.

### Step 4. The induction with all suffix hypotheses

The generic `remaining_state_le` applies to any function \(D\) from finite edge lists to real vectors and any \(T\ge0\). Its hypothesis is
\[
D_q\le U_e(T)D_{e::q}
\quad\text{for every }e::q\preceq_{\mathrm{suf}}p.
\]
We prove \(D_{[]}\le\mathcal D_{p^{\mathrm{rev}}}(T)D_p\) by induction on \(p\), keeping \(D\) fixed and carrying these suffix hypotheses.

For \(p=[]\), its reverse is empty and the product is the identity, so the conclusion is \(D_{[]}\le D_{[]}\).

### Step 5. Propagation through the tail

Let the list be \(p=e::h\), and suppose the result holds for \(h\).
Every suffix \(a::q\) of \(h\) is also a suffix of \(e::h\): concatenate the initial segment witnessing the first suffix relation with the initial edge \(e\). Thus the original hypotheses supply all the hypotheses for the shorter list, giving
\[
D_{[]}\le\mathcal D_{h^{\mathrm{rev}}}(T)D_h.
\tag{4}
\]
The full list \(e::h\) is its own suffix. Its one-step hypothesis says
\[
D_h\le U_e(T)D_{e::h}.
\tag{5}
\]
By the [[node:kl.detail.transfer_properties|transfer properties]], the tail product is monotone for \(T\ge0\). Apply it to (5) and combine with (4):
\[
D_{[]}\le
\mathcal D_{h^{\mathrm{rev}}}(T)D_h
\le\mathcal D_{h^{\mathrm{rev}}}(T)\bigl(U_e(T)D_{e::h}\bigr).
\tag{6}
\]

### Step 6. The reversed product

Reversing \(e::h\) gives \(h^{\mathrm{rev}}+\!\!+[e]\). The concatenation formula gives
\[
\mathcal D_{(e::h)^{\mathrm{rev}}}(T)v
=\mathcal D_{h^{\mathrm{rev}}}(T)
  \bigl(\mathcal D_{[e]}(T)v\bigr)
=\mathcal D_{h^{\mathrm{rev}}}(T)(U_e(T)v).
\]
Use \(v=D_{e::h}\) in (6). This is precisely the induction conclusion for \(e::h\), completing the generic proof.

For the sheaf states, Steps 1–3 supply its hypotheses at every suffix, and \(0<t<1\) gives \(T=t^{-1}-t>0\). Substitution proves (2), the source's `scheduleState_le`.

### Step 7. A two-edge instance

For chronological list \([e_1,e_2]\), (3) gives
\[
D_{[e_2]}\le U_{e_1}D_{[e_1,e_2]},\qquad
D_{[]}\le U_{e_2}D_{[e_2]}.
\]
Applying \(U_{e_2}\) to the first inequality and using the second gives
\[
D_{[]}\le U_{e_2}D_{[e_2]}
\le U_{e_2}U_{e_1}D_{[e_1,e_2]}.
\]
This is dispatch on the reversed list \([e_2,e_1]\). Each intermediate vector is still the Hilbert value of its actual remaining kernels.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.SchedulePaths.remaining_state_le`: [PositiveTransfer.lean:866](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L866).

`OAI.KLInvariance.BruhatGraph.scheduleState_step`: [PositiveTransfer.lean:1117](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1117).

`OAI.KLInvariance.BruhatGraph.scheduleState_le`: [PositiveTransfer.lean:1148](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1148).
