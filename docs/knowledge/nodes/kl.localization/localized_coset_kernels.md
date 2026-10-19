---
id: kl.local.localized_coset_kernels
title: Selected kernels and edge images on the localized coset
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.localized_coset
- kl.local.localized_coset_properties
- kl.sheaves.pullback_selected_kernels
- kl.notes.sheaf_localization
- kl.algebra.flat_embedded_modules
- kl.local.coset_outgoing_lifts
lean:
  repository: openai-kl
  modules:
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.localizedCoset_kernel
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChange_upwardKernel
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChange_lowerImage
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChange_upperImage
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:393
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.localizedCoset_kernel
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:347
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChange_upwardKernel
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:360
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChange_lowerImage
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:367
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChange_upperImage
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read localizedCoset_kernel and verified its live-edge inputs. Combined
    it with the already reviewed flat kernel and lower/upper image theorems, preserving
    arbitrary independently selected edge sets and equality inside the fixed ambient
    stalk and edge tensor modules.
tags:
- Kazhdan-Lusztig
- localization
---

# Selected kernels and edge images on the localized coset

Fix a finite-generator Coxeter system, a root plane \(P\) with a chosen plane basis and induced subgroup \(D_P\), a least-length representative \(a_0\) in \(D_Pa_0\), and \(b\in W\). Choose a finite real basis of the extended realization, giving the polynomial coefficient algebra \(A\). Let
\[
j:K\to[1,b],\qquad j_V(d)=da_0,\qquad
K=\{d\in D_P:1\le_Dd,\ da_0\le_Wb\}
\]
be the finite relative coset graph map. Let \(C\) be an \(A\)-linear sheaf on \([1,b]\) satisfying the polynomial upper-quotient rule, and put
\[
R=R_P=A_{\mathfrak p_P},\qquad C_R=R\otimes_A C,\qquad \mathcal C=j^*(C_R).
\]

For an arbitrary set \(T\) of ambient edges, \(K_y^C(T)\) denotes vanishing on the members of \(T\) starting at \(y\). At a relative vertex \(d\), let \(T^K=j_E^{-1}(T)\). Then
\[
K_d^{\mathcal C}(T^K)
=K_{j_V(d)}^{C_R}(T)
=\bigl(K_{j_V(d)}^C(T)\bigr)_R
\]
inside \(\mathcal C^d=R\otimes_A C^{j_V(d)}\). The subscript \(R\) denotes the embedded image of the tensor of a submodule inclusion.

For a relative edge \(a:d\to c\), and arbitrary ambient edge sets \(T,H\), both selected edge images satisfy
\[
\rho_a^{\mathcal C,-}\bigl(K_d^{\mathcal C}(j_E^{-1}(T))\bigr)
=\bigl(\rho_{j_E(a)}^{C,-}(K_{j_V(d)}^C(T))\bigr)_R,
\]
\[
\rho_a^{\mathcal C,+}\bigl(K_c^{\mathcal C}(j_E^{-1}(H))\bigr)
=\bigl(\rho_{j_E(a)}^{C,+}(K_{j_V(c)}^C(H))\bigr)_R.
\]
These are equalities of submodules of the same edge module
\(\mathcal C^a=R\otimes_A C^{j_E(a)}\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Relative extension through an explicit graph map.**

**OpenAI notes:** The coset intersection is a finite relative lower ideal. A relative upper subset is closed under the surviving plane-labelled edges. Descending ambient extension gives relative flabbiness after localization. [loc:relative-flabbiness](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L226).

**Lean (primary):** The same descending extension is factored into extend_closedUnder and a graph-pullback theorem. The coset map supplies vertex injectivity and explicit outgoing lifts; the root/unit criterion makes all outside edge modules zero. A separate theorem records selected-kernel equality under that pullback. [Sheaves:106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L106), [MinimalExtensions:1520](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1520), [PlaneLocalization:497](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L497), [PlaneLocalization:591](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L591), [TerminalKernels:393](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L393).

**Role in the proof:** Relative order determines the upper subsets on the coset, while the ambient graph supplies the extension. The localized stalks and edge maps remain the actual tensor-extended ambient modules, so selected kernels and their edge images retain their embeddings.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Specify the surviving edges and their lifts

Set \(L=\{e:\tau_e\in D_P\}\), where \(\tau_e\) is the ambient edge’s left reflection label. The [[node:kl.local.localized_coset_properties|localized coset properties theorem]] shows that every edge module of \(C_R\) outside \(L\) is zero.

At the fixed vertex \(d\), the [[node:kl.local.coset_outgoing_lifts|coset outgoing-lift theorem]] supplies a relative outgoing lift for each edge in \(L\) starting at \(j_V(d)\).

### Step 2. Apply the [[node:kl.sheaves.pullback_selected_kernels|selected-kernel pullback theorem]]

Apply the [[node:kl.sheaves.pullback_selected_kernels|selected-kernel pullback theorem]] to \(C_R,j,d,T,L\). Step 1 verifies its two hypotheses, and it gives
\[
K_d^{\mathcal C}(j_E^{-1}(T))
=K_{j_V(d)}^{C_R}(T)
\]
in the identical stalk module.

In detail, every selected relative equation is an ambient selected equation. Conversely, a selected ambient equation either has a relative lift or takes values in a zero edge module. These are precisely the two containment arguments in that theorem.

### Step 3. Identify the ambient localized kernel

The ambient Bruhat graph has finitely many edges, and \(R=A_{\mathfrak p_P}\) is flat over \(A\). The [[node:kl.notes.sheaf_localization|flat kernel-and-image theorem]] gives
\[
K_{j_V(d)}^{C_R}(T)
=\bigl(K_{j_V(d)}^C(T)\bigr)_R.
\]
Combining with Step 2 proves both equalities of selected kernels.

### Step 4. Transport the lower edge image

The pullback lower restriction at \(a\) is the lower restriction of \(C_R\) at \(j_E(a)\), under the endpoint identification. Step 2 therefore gives
\[
\rho_a^{\mathcal C,-}(K_d^{\mathcal C}(j_E^{-1}(T)))
=\rho_{j_E(a)}^{C_R,-}(K_{j_V(d)}^{C_R}(T)).
\]
The lower-image part of the [[node:kl.notes.sheaf_localization|flat kernel-and-image theorem]] identifies the right side with
\(\bigl(\rho_{j_E(a)}^{C,-}(K_{j_V(d)}^C(T))\bigr)_R\).

### Step 5. Transport the upper edge image

Apply Steps 2–3 at \(c\) with the independently chosen set \(H\). The pullback upper restriction is the upper restriction of \(C_R\) at the same ambient edge \(j_E(a)\). The upper-image part of the [[node:kl.notes.sheaf_localization|flat kernel-and-image theorem]] gives the second displayed image equality.

Both calculations use that single ambient edge module. They supply the submodules to which the later local model isomorphism is applied.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.localizedCoset_kernel`: [TerminalKernels.lean:393](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L393).

`OAI.KLInvariance.MomentGraph.Sheaf.baseChange_upwardKernel`: [TerminalKernels.lean:347](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L347).

`OAI.KLInvariance.MomentGraph.Sheaf.baseChange_lowerImage`: [TerminalKernels.lean:360](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L360).

`OAI.KLInvariance.MomentGraph.Sheaf.baseChange_upperImage`: [TerminalKernels.lean:367](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L367).
