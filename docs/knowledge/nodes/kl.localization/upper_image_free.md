---
id: kl.notes.upper_image_free
title: The upper edge image as a free quotient
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.sheaves.upward_kernel
- kl.sheaves.boundary_sheaf
- kl.detail.quotient_image_free
- kl.detail.edge_images
- kl.algebra.scalar_quotient
lean:
  repository: openai-kl
  modules:
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.BruhatGraph.upperImage_free
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:691
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.upperImage_free
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
  prompt: Are the mathematical hypotheses and scope retained from the referenced declarations?
  verdict: The exposition follows the fixed Lean source; worked calculations explain
    the constructions.
tags:
- Kazhdan-Lusztig
- edge_images
---

# The upper edge image as a free quotient

Let \(e:x\to y\) have label \(\alpha\), and let \(L=L_y(G)\) be the upper endpoint's remaining kernel. If \(L\) is free over \(A\), its image \(J\) in the edge module is free over \(C=A/(\alpha)\).

*Proof.*

### Step 1. Check the saturation required by the quotient-image theorem

Let \(L=K_y(G)\), and suppose \(\alpha_ev\in L\). For each remaining outgoing edge \(h:y\to z\),
\[
0=\rho_{y,h}(\alpha_ev)=\alpha_e\rho_{y,h}(v).
\]
The label \(\alpha_e\) belongs to an incoming edge at \(y\), while \(\alpha_h\) belongs to an outgoing edge there. They cannot be proportional: the same reflection sends \(y\) to only one other vertex and cannot send it both down to \(x\) and up to \(z\).

The quotient \(A/(\alpha_h)\) is a polynomial domain. The upper quotient rule and freeness of \(B^z\) make \(B^h\) free over that domain. The image of \(\alpha_e\) is nonzero in it, so its multiplication is injective. Therefore \(\rho_{y,h}(v)=0\) for every \(h\in G\), proving \(v\in L\).

### Step 2. Identify the image as a free quotient

The upper restriction along \(e\) has kernel \(\alpha_eB^y\). Step 1 and [[node:kl.detail.quotient_image_free]] give
\[
J_e\simeq L/\alpha_eL.
\]
The assumed free \(A\)-basis of \(L\) reduces to a free basis over \(C=A/(\alpha_e)\), so \(J_e\) is free over \(C\).

### Step 3. Prove the generic-span statement needed later

Let \(g=\prod_{h\in G}\alpha_h\), with empty product one. For every \(v\in B^y\) and \(h\in G\), the restriction of \(gv\) to \(B^h\) is zero because \(\alpha_h\) is a factor and annihilates that edge module. Thus \(gB^y\subseteq L\).

The upper map \(B^y\twoheadrightarrow B^e\) is surjective, so \(\overline gB^e\subseteq J_e\), where \(\overline g\) is the image in \(C\). No factor of \(g\) is proportional to \(\alpha_e\), so \(\overline g\ne0\).

After passing to the fraction field of \(C\), \(\overline g\) is invertible; therefore \(J_e\) spans all of \(B^e\). Multiplication by the nonzero edge factor gives the same generic-span property for \(f_eJ_e\).

## References

[5. Comparison of edge images](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.upperImage_free`: [TerminalKernels.lean:691](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L691).
