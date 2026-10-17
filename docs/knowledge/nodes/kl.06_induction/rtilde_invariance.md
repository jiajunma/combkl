---
id: kl.comparison.rtilde_invariance
title: Simultaneous R-tilde invariance and terminal-kernel freeness
kind: theorem
status: proved
primary_topic: kl.06_induction
topics:
- kl.06_induction
uses:
- kl.comparison.rtilde_step
- kl.comparison.reverse_freeness
- kl.comparison.global_comparison
- kl.duality.actual_character_reciprocity
lean:
  repository: openai-kl
  modules:
  - Invariance
  declarations:
  - OAI.KLInvariance.BruhatGraph.rTilde_invariance_and_freeness
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Invariance:190
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.rTilde_invariance_and_freeness
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

# Simultaneous R-tilde invariance and terminal-kernel freeness

For an interval isomorphism \(\phi:[u,b]\simeq[u',b']\) in finite-generator real realizations, the following hold simultaneously:

1. \(\widetilde R_{u,b}=\widetilde R'_{u',b'}\).
2. All terminal kernels for the schedule transported by \(\phi\) are free.
3. All terminal kernels for the schedule transported by \(\phi^{-1}\) are free.

*Proof.*

Use strong induction on interval rank difference, quantifying over both endpoints in both systems. Smaller intervals supply the bottom-row equalities and the higher upper-interval freeness. [[node:kl.comparison.rtilde_step]] first establishes the current R-tilde equality.

Apply the smaller-interval equalities to all matrix entries. Actual-character reciprocity now makes the complete transfer comparison exact at its endpoints. Every edge image is consequently exact, and [[node:kl.comparison.reverse_freeness]] establishes terminal-kernel freeness in both directions, closing the induction.

## The two families of smaller intervals

For a current interval \([u,b]\), the induction uses two different restrictions.

- A proper initial interval \([u,z]\), with \(z<b\), supplies the corresponding bottom-row R-tilde entry.
- A proper upper interval \([y,b]\), with \(y>u\), supplies terminal-kernel freeness at the upper endpoint of an edge.

Both have strictly smaller rank difference. The induction is quantified over both endpoints, so both restrictions are legitimate instances of the same statement. The inverse interval isomorphism supplies the symmetric data.

After proving the new R-tilde entry, restriction to all subintervals identifies the entire R-tilde matrix. That exact matrix identity closes the Hilbert comparison and supplies the new freeness. This explains why polynomial invariance and kernel freeness are proved together rather than in separate independent inductions.

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.rTilde_invariance_and_freeness`: [Invariance.lean:190](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L190).
