---
id: kl.comparison.reverse_freeness
title: Recovering terminal-kernel freeness by reverse traversal
kind: theorem
status: proved
primary_topic: kl.06_induction
topics:
- kl.06_induction
uses:
- kl.comparison.free_suffixes
- kl.comparison.no_deficit
- kl.sheaves.hilbert_detection
- kl.notes.graded_projective_free
lean:
  repository: openai-kl
  modules:
  - SimultaneousInvariance
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.BruhatGraph.schedule_kernels_free_of_images_eq
  - OAI.KLInvariance.BruhatGraph.partial_kernel_free_of_image_eq
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SimultaneousInvariance:181
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.schedule_kernels_free_of_images_eq
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1052
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.partial_kernel_free_of_image_eq
  - artifact: openai-kl-paper
    locator: 6. Reciprocity and simultaneous induction; sec:induction
    format: section
    note: Chapter organization follows the paper; Lean references identify the precise
      formal statements.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- induction
---

# Recovering terminal-kernel freeness by reverse traversal

If every lower edge image in a schedule equals its corrected upper edge image, then all terminal kernels at every vertex are free.

*Proof.*

Start with no remaining conditions; every vertex module is already free. Add conditions back in reverse order. For a new edge, both endpoint kernels for the shorter suffix are already free. Image equality, regularity of the label, and saturation give projectivity of the new kernel. The homogeneous-basis theorem for graded polynomial modules then makes it free. Induct on suffix length.

In the main argument, endpoint equality and [[node:kl.comparison.no_deficit]] supply the image equalities. Hilbert detection converts equality of numerical increments into equality of actual submodules.

## The exact-sequence argument at one reverse step

Let \(F\) be the already free lower kernel before adding back the next condition, and let \(L\) be the already free upper kernel. The new kernel \(K\) fits into
\[
0\longrightarrow K\longrightarrow F\longrightarrow I_e\longrightarrow0.
\]
The image equality identifies \(I_e\) with the corrected upper image. The upper quotient description gives a free resolution of length one, obtained from multiplication by the edge label on \(L\); multiplication by the correction factor transports its quotient to \(I_e\).

Compare these two presentations with Schanuel's lemma. Since all modules in the comparison except \(K\) are free, \(K\) is projective. Its grading and lower degree bound then give a homogeneous free basis by [[node:kl.notes.graded_projective_free]].

The order of the reverse induction matters: both \(F\) and \(L\) belong to the shorter suffix and are available before the new condition is imposed.

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.schedule_kernels_free_of_images_eq`: [SimultaneousInvariance.lean:181](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SimultaneousInvariance.lean#L181).

`OAI.KLInvariance.BruhatGraph.partial_kernel_free_of_image_eq`: [PositiveTransfer.lean:1052](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1052).
