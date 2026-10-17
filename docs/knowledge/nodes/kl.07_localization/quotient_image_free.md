---
id: kl.detail.quotient_image_free
title: Freeness of a saturated image over the edge quotient ring
kind: theorem
status: proved
primary_topic: kl.07_localization
topics:
- kl.07_localization
uses:
- kl.detail.upper_quotient
- kl.sheaves.upward_kernel
lean:
  repository: openai-kl
  modules:
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.ScalarQuotient.saturated_image_free
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:624
    format: lean-location
    note: OAI.KLInvariance.ScalarQuotient.saturated_image_free
  - artifact: openai-kl-paper
    locator: Related paper context; edge:lattice
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
- localization
---

# Freeness of a saturated image over the edge quotient ring

Let \(q:M\to N\) be \(R\)-linear, with \(N\) an \(R/(a)\)-module and
\[
\ker q=aM.
\]
Let \(L\subseteq M\) be finite free and saturated with respect to \(a\):
\[
av\in L\quad\Longrightarrow\quad v\in L.
\]
Then \(q(L)\), regarded as a module over \(R/(a)\), is free.

*Proof.*

Restrict \(q\) to \(L\). If \(v\in L\) maps to zero, write \(v=aw\) using the kernel description in \(M\). Saturation puts \(w\) in \(L\), so the restricted kernel is exactly \(aL\). Hence
\[
q(L)\simeq L/aL.
\]
Choose a finite \(R\)-basis of \(L\). Its images give an \(R/(a)\)-basis of the quotient, proving the claim.

In the edge comparison, \(a\) is the edge label and \(L\) is an upper terminal kernel. Freeness of \(L\) comes from the smaller-interval induction. Saturation follows from regularity of this label on the other relevant edge modules. This yields the genuinely free target needed by the height-one localization argument.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L26).

## Lean formalization



`OAI.KLInvariance.ScalarQuotient.saturated_image_free`: [TerminalKernels.lean:624](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L624).
