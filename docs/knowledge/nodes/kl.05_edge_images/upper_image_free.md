---
id: kl.notes.upper_image_free
title: The upper edge image as a free quotient
kind: theorem
status: proved
primary_topic: kl.05_edge_images
topics:
- kl.05_edge_images
uses:
- kl.sheaves.upward_kernel
- kl.sheaves.boundary_sheaf
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

The upper edge map has kernel \(\alpha B^y\), so
\[
J\simeq L/(L\cap\alpha B^y).
\]
We claim \(L\cap\alpha B^y=\alpha L\). One inclusion is immediate. If \(\alpha v\in L\), then for every remaining edge \(g\),
\[
\alpha\,\rho_g(v)=0.
\]
Its label is not proportional to \(\alpha\), and its module is free over the quotient by that other label. Multiplication by \(\alpha\) on this edge module is injective. Hence \(\rho_g(v)=0\) for every \(g\), proving \(v\in L\).

It follows that \(J\simeq L/\alpha L\). Reducing an \(A\)-basis of \(L\) modulo \(\alpha\) gives a \(C\)-basis of \(J\).

There is also full generic rank. The product of the remaining labels times \(B^y\) lies in \(L\); its image modulo \(\alpha\) is nonzero. Consequently \(J\) spans the whole edge module after passing to the fraction field of \(C\). These are the freeness and generic-span inputs required by height-one membership detection.

## References

[5. Comparison of edge images](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.upperImage_free`: [TerminalKernels.lean:691](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L691).
