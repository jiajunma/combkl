---
id: kl.detail.reverse_projectivity
title: Recovering a projective kernel from scaled image equality
kind: theorem
status: proved
primary_topic: kl.08_comparison_and_freeness
topics:
- kl.08_comparison_and_freeness
uses:
- kl.detail.scaled_images
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.ReverseFiltration.inf_kernel_projective_of_image_eq
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:970
    format: lean-location
    note: OAI.KLInvariance.ReverseFiltration.inf_kernel_projective_of_image_eq
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

# Recovering a projective kernel from scaled image equality

Let \(S\subseteq M\) and \(T\subseteq P\) be projective \(A\)-modules, with maps
\(f:M\to N\), \(g:P\to N\), and an injective endomorphism \(\psi:N\to N\). Assume
\[
f(S)=\psi(g(T)),\qquad \ker g=aP,
\]
that multiplication by \(a\) on \(P\) is injective, and that \(T\) is saturated under division by \(a\). Then
\[
S\cap\ker f
\]
is projective.

*Proof.*

The map \(T\to f(S)\), \(t\mapsto\psi(g(t))\), is surjective by the equality of embedded images. Injectivity of \(\psi\) and saturation show that its kernel is \(aT\). Multiplication by \(a\) identifies this kernel with the projective module \(T\).

Compare this projective presentation of the common image with the surjection \(S\to f(S)\). The kernel-comparison result for projective presentations shows that the latter kernel is projective. Identifying that kernel with \(S\cap\ker f\) gives the conclusion.

For the graded polynomial modules of the blueprint, a separate homogeneous-basis theorem then turns this projectivity into graded freeness. This step explains why image equality, rather than merely an inequality of Hilbert series, is the input to reverse freeness.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization



`OAI.KLInvariance.ReverseFiltration.inf_kernel_projective_of_image_eq`: [PositiveTransfer.lean:970](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L970).
