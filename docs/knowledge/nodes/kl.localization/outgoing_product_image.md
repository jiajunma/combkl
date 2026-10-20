---
id: kl.local.outgoing_product_image
title: Outgoing label products send stalks and edge modules into selected images
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.outgoing_label_product
- kl.sheaves.upward_kernel
- kl.detail.edge_images
lean:
  repository: openai-kl
  modules:
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.outgoingLabelProduct_smul_mem
  - OAI.KLInvariance.MomentGraph.Sheaf.outgoingLabelProduct_smul_upperImage
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:788
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.outgoingLabelProduct_smul_mem
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:798
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.outgoingLabelProduct_smul_upperImage
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, finiteness and freeness hypotheses, original embedded
    submodules, localization multipliers and schedule assumptions explicit?
  verdict: Verified the generic commutative-ring, finite-edge, label-annihilation
    and upper-surjectivity hypotheses, with the explicit factor and lift witnesses
    and the empty-selection case.
tags:
- Kazhdan-Lusztig
- global-inclusion
---

# Outgoing label products send stalks and edge modules into selected images

Let \(R\) be a commutative ring, \(G\) an ordered graph with finitely many edges, and \(\mathcal B\) an \(R\)-linear sheaf on it. Choose scalar labels \(\alpha_f\in R\). Suppose each label annihilates its edge module:
\[
\alpha_fv=0\qquad(f\text{ an edge},\ v\in\mathcal B^f).
\]
For any outgoing selection \(F\) at \(x\), its outgoing label product satisfies
\[
g_{x,F}\mathcal B^x\subseteq K_x^{\mathcal B}(F).
\]

For an edge \(e\) ending at \(x\), assume its upper restriction
\(\rho_e^+:\mathcal B^x\to\mathcal B^e\) is surjective. Then
\[
g_{x,F}\mathcal B^e
\subseteq U_e^{\mathcal B}(F)
=\rho_e^+(K_x^{\mathcal B}(F)).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The correction and outgoing products supply one global multiplier.**

**OpenAI notes:** The notes multiply the upper outgoing labels to obtain a nonzero reduced scalar whose multiples lie in the upper image. The correction factor gives a free target of full generic rank, and primes containing reduced roots are related to plane primes. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The outgoing product is defined for any finite graph and selection. Label annihilation and an upper lift prove its image containment. The actual reduced outgoing and correction products are nonzero, and every prime divisor of their product is associated to one reduced independent root. Quotient divisibility by that root is equivalent to membership in its plane ideal. [TerminalKernels:781](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L781), [TerminalKernels:798](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L798), [TerminalKernels:732](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L732), [TerminalKernels:752](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L752), [TerminalKernels:838](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L838).

**Role in the proof:** The Blueprint gives the explicit global multiplier and the complete factor classification used by the membership theorem.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Check each selected restriction after multiplication

Take \(w\in\mathcal B^x\) and \(f\in F\). Factor the outgoing label product as \(g_{x,F}=\alpha_fr_f\), using its factor-divisibility identity. Linearity and commutativity give
\[
\rho_f^-(g_{x,F}w)
=g_{x,F}\rho_f^-(w)
=r_f\bigl(\alpha_f\rho_f^-(w)\bigr)
=0.
\]
The final equality uses label annihilation on \(\mathcal B^f\). Since this holds for every \(f\in F\), the vector \(g_{x,F}w\) lies in the selected kernel. This proves the first containment.

### Step 2. Lift an arbitrary edge vector to the upper stalk

Take \(v\in\mathcal B^e\). Surjectivity supplies \(w\in\mathcal B^x\) with \(\rho_e^+(w)=v\). Step 1 gives \(g_{x,F}w\in K_x^{\mathcal B}(F)\). Its upper image is
\[
\rho_e^+(g_{x,F}w)=g_{x,F}\rho_e^+(w)=g_{x,F}v.
\]
Thus \(g_{x,F}v\) belongs to \(U_e^{\mathcal B}(F)\), proving the second containment.

When \(F\) is empty, the product is \(1\), the selected kernel is the whole stalk, and the second statement is exactly surjectivity of the upper restriction.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.outgoingLabelProduct_smul_mem`: [TerminalKernels.lean:788](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L788).

`OAI.KLInvariance.MomentGraph.Sheaf.outgoingLabelProduct_smul_upperImage`: [TerminalKernels.lean:798](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L798).
