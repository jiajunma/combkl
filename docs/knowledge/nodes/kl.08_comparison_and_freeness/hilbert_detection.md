---
id: kl.sheaves.hilbert_detection
title: Equality detected by Hilbert values
kind: theorem
status: proved
primary_topic: kl.08_comparison_and_freeness
topics:
- kl.08_comparison_and_freeness
uses:
- kl.sheaves.hilbert_free
lean:
  repository: openai-kl
  modules:
  - HilbertSeries
  declarations:
  - OAI.KLInvariance.Hilbert.polynomial_eq_of_value_eq
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:273
    format: lean-location
    note: OAI.KLInvariance.Hilbert.polynomial_eq_of_value_eq
  - artifact: openai-kl-paper
    locator: 6. Reciprocity and simultaneous induction; sec:induction
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
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

# Equality detected by Hilbert values

Let \(M\) be a finitely generated graded polynomial module, and let \(S\subseteq T\) be subspaces of \(M\), with \(T\) closed under homogeneous components. If their Hilbert values, computed from the dimensions of their intersections with the graded pieces, agree at some \(0<q<1\), then \(S=T\).

*Proof.*

Finite homogeneous generators give a graded surjection from a finite sum of shifted free modules onto \(M\). [[node:kl.sheaves.hilbert_free]] bounds the relevant series and proves convergence and finiteness of each graded dimension.

Containment makes every graded dimension difference nonnegative. Equality of the sums forces all these differences to vanish. Decomposing an arbitrary element of \(T\) into homogeneous components then proves \(T\subseteq S\).

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.Hilbert.polynomial_eq_of_value_eq`: [HilbertSeries.lean:273](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L273).
