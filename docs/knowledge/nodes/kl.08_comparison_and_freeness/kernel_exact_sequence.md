---
id: kl.detail.kernel_exact_sequence
title: The exact sequence for adding one outgoing condition
kind: theorem
status: proved
primary_topic: kl.08_comparison_and_freeness
topics:
- kl.08_comparison_and_freeness
uses:
- kl.detail.edge_images
- kl.sheaves.upward_kernel
- kl.sheaves.hilbert_free
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.kernelHilbert_edge
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:377
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.kernelHilbert_edge
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
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- comparison_and_freeness
---

# The exact sequence for adding one outgoing condition

For \(e:x\to y\) and a set \(F\) of outgoing conditions at \(x\), restriction along \(e\) gives a graded exact sequence
\[
0\longrightarrow K_x(F\cup\{e\})
\longrightarrow K_x(F)
\xrightarrow{\rho_{x,e}}L_e(F)\longrightarrow0.
\]
For a finite nonnegatively graded polynomial-ring sheaf and \(0<q<1\), it follows that
\[
H_{K_x(F)}(q)-H_{K_x(F\cup\{e\})}(q)=H_{L_e(F)}(q).
\]

*Proof.*

The map is surjective onto its defined image. Its kernel consists of vectors satisfying all conditions in \(F\) and the additional \(e\)-condition, exactly \(K_x(F\cup\{e\})\). Since restrictions preserve degree, this is an exact sequence on each homogeneous component. Add dimensions there, multiply by \(q^n\), and sum; the polynomial-module summability result justifies these sums for \(0<q<1\).

No freeness of the partial kernels is required for this identity. They need finite-dimensional graded pieces and the stated summability. This allows the comparison inequality to be established before the new terminal-kernel freeness is known.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization



`OAI.KLInvariance.MomentGraph.GradedSheaf.kernelHilbert_edge`: [PositiveTransfer.lean:377](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L377).
