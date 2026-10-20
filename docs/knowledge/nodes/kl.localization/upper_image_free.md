---
id: kl.notes.upper_image_free
title: The upper edge image is free over its quotient coefficient ring
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.sheaves.boundary_sheaf
- kl.sheaves.upward_kernel
- kl.detail.quotient_image_free
- kl.algebra.scalar_quotient_basis
- kl.algebra.root_label_primes
- kl.algebra.scalar_quotient_regular
- kl.algebra.scalar_quotient
- kl.detail.edge_images
lean:
  repository: openai-kl
  modules:
  - Support
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.BruhatGraph.edgeTorsion
  - OAI.KLInvariance.BruhatGraph.edgeModule
  - OAI.KLInvariance.BruhatGraph.edgeModule_tower
  - OAI.KLInvariance.BruhatGraph.edgeModule_free
  - OAI.KLInvariance.BruhatGraph.upperImage_free
  - OAI.KLInvariance.BruhatGraph.incoming_label_regular_outgoing
  - OAI.KLInvariance.MomentGraph.GradedSheaf.upwardSubmodule_saturated
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:665
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edgeTorsion
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:669
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edgeModule
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:674
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edgeModule_tower
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:681
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edgeModule_free
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:691
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.upperImage_free
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1361
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.incoming_label_regular_outgoing
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1302
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.upwardSubmodule_saturated
  - artifact: openai-kl-paper
    locator: 5. Comparison of edge images; edge:bound
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, finiteness and freeness hypotheses, original embedded
    submodules, localization multipliers and schedule assumptions explicit?
  verdict: Expanded the full finite-basis/BoundarySheaf setup, actual quotient action
    and free edge presentation, incoming/outgoing prime nondivisibility, coordinatewise
    regularity, selected-kernel saturation, Noetherian finiteness and quotient-basis
    transfer. Preserved arbitrary outgoing selections.
tags:
- Kazhdan-Lusztig
- global-inclusion
---

# The upper edge image is free over its quotient coefficient ring

Let \(W\) be a finite-generator real Coxeter system, \(u\le_Wb\), and \(\mathcal B\) a boundary sheaf on the Bruhat graph of \([u,b]_W\). Choose a finite real basis of the extended realization, with polynomial coefficient algebra \(A\) and root-polynomial labels \(\alpha_f\).

Fix an edge \(e:x\to y\), and set \(C_e=A/(\alpha_e)\). The upper-quotient rule gives a surjective map
\[
q_e=\rho_e^+:\mathcal B^y\to\mathcal B^e,\qquad
\ker q_e=\alpha_e\mathcal B^y.
\]
The edge module has the compatible quotient action
\(\overline r\,v=rv\), and is free over \(C_e\).

Let \(G\) be any selection of outgoing edges at \(y\), and put
\[
L=K_y^{\mathcal B}(G),\qquad J=q_e(L)\subseteq\mathcal B^e.
\]
If \(L\) is free over \(A\), then the actual image \(J\), with its same-carrier \(C_e\)-submodule structure, is free over \(C_e\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Compatible quotient actions and the actual free upper image.**

**OpenAI notes:** The notes identify the upper image with the selected upper kernel modulo the current root label. Saturation gives this quotient, and freeness of the upper kernel gives freeness over the edge coefficient ring. Multiplication by the nonzero correction then gives the free target. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The quotient action and its scalar tower are explicit. A finite free scalar presentation gives the edge-module basis. Regularity of the incoming label on every outgoing edge module gives saturation; Noetherian finiteness permits the finite quotient presentation. A separate same-carrier quotient-submodule construction and injective scalar-image map give freeness of the corrected target. [TerminalKernels:613](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L613), [TerminalKernels:624](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L624), [TerminalKernels:681](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L681), [TerminalKernels:691](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L691), [TerminalKernels:880](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L880).

**Role in the proof:** The Blueprint retains the precise coefficient ring of each freeness statement, all action compatibilities, the arbitrary outgoing selection and the finite-basis hypothesis used for finiteness.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Give the edge module its quotient action and free presentation

The upper-quotient rule implies that \(\alpha_e\) kills every vector in \(\mathcal B^e\). To see this, lift \(v=q_e(w)\) and compute
\[
\alpha_ev=q_e(\alpha_ew)=0.
\]
Thus the \(A\)-action factors through \(C_e\).

The upper stalk \(\mathcal B^y\) is finite free by the boundary-sheaf data. The [[node:kl.algebra.scalar_quotient_basis|coordinate-reduction presentation theorem]] applies to its free basis, the surjection \(q_e\), and its exact scalar kernel. It identifies the edge module with a finite free \(C_e\)-module. This also verifies compatibility between its original \(A\)-action and its quotient action.

### Step 2. Prove the incoming label regular on each outgoing edge module

Let \(h:y\to z\) be outgoing at \(y\). The current incoming reflection and this outgoing reflection are distinct: equality would send \(y\) both back to \(x\) and forward to \(z\), giving \(z=x\), contrary to strict increase of length.

Their positive roots are therefore distinct. The [[node:kl.algebra.root_label_primes|root-label prime theorem]] gives that \(\alpha_h\) is prime and \(\alpha_h\nmid\alpha_e\).

Suppose \(\alpha_ev=0\) in \(\mathcal B^h\). Lift \(v=q_h(w)\) from the free upper stalk \(\mathcal B^z\). Then
\[
q_h(\alpha_ew)=0,\qquad \alpha_ew\in\alpha_h\mathcal B^z.
\]
In a free basis of \(\mathcal B^z\), each coordinate satisfies \(\alpha_h\mid\alpha_e w_i\). Primality and \(\alpha_h\nmid\alpha_e\) imply \(\alpha_h\mid w_i\) for every \(i\). Divide the finitely many coordinates to obtain \(w=\alpha_hw'\). Consequently \(v=q_h(w)=0\).

Applying this zero-kernel calculation to a difference proves injectivity of multiplication by \(\alpha_e\) on every outgoing edge module. This is the [[node:kl.algebra.scalar_quotient_regular|scalar-quotient regularity argument]] used by `incoming_label_regular_outgoing`.

### Step 3. Prove saturation of the selected upper kernel

Suppose \(\alpha_ew\in L\). For every \(h\in G\), selected-kernel membership says
\[
0=\rho_h^-(\alpha_ew)=\alpha_e\rho_h^-(w).
\]
Step 2 permits cancellation on the edge module \(\mathcal B^h\), giving \(\rho_h^-(w)=0\). Thus \(w\in L\). We have proved
\[
\alpha_ew\in L\quad\Longrightarrow\quad w\in L.
\]

### Step 4. Verify finiteness and restrict the presentation

The coefficient ring is a polynomial ring in finitely many variables over a field, hence Noetherian: submodules of finitely generated modules are finitely generated. Since the upper stalk is finite over \(A\), its submodule \(L\) is finite as well. Together with the hypothesis that \(L\) is free, this makes \(L\) finite free.

Restriction gives a surjection \(q_e|_L:L\to J\). If \(w\in L\) is killed by it, the ambient kernel equality gives \(w=\alpha_ev\) with \(v\in\mathcal B^y\). Step 3 gives \(v\in L\). Conversely every \(\alpha_ev\), \(v\in L\), maps to zero. Thus
\[
\ker(q_e|_L)=\alpha_eL.
\]

### Step 5. Transfer the quotient basis to the actual image

The [[node:kl.detail.quotient_image_free|saturated-image freeness theorem]] now applies with \(R=A\), scalar \(\alpha_e\), map \(q_e\), and finite free saturated submodule \(L\). It constructs the \(C_e\)-linear isomorphism
\[
L/\alpha_eL\xrightarrow{\sim}J,\qquad [w]\longmapsto q_e(w).
\]
Reducing a free \(A\)-basis of \(L\) gives a free \(C_e\)-basis of the quotient, and this isomorphism transfers that basis to the embedded image \(J\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.edgeTorsion`: [TerminalKernels.lean:665](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L665).

`OAI.KLInvariance.BruhatGraph.edgeModule`: [TerminalKernels.lean:669](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L669).

`OAI.KLInvariance.BruhatGraph.edgeModule_tower`: [TerminalKernels.lean:674](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L674).

`OAI.KLInvariance.BruhatGraph.edgeModule_free`: [TerminalKernels.lean:681](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L681).

`OAI.KLInvariance.BruhatGraph.upperImage_free`: [TerminalKernels.lean:691](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L691).

`OAI.KLInvariance.BruhatGraph.incoming_label_regular_outgoing`: [Support.lean:1361](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1361).

`OAI.KLInvariance.MomentGraph.GradedSheaf.upwardSubmodule_saturated`: [Support.lean:1302](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1302).
