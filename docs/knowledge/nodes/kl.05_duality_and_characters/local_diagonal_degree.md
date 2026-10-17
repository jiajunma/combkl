---
id: kl.detail.local_diagonal_degree
title: A nonzero local diagonal forces a strict half-degree bound
kind: theorem
status: proved
primary_topic: kl.05_duality_and_characters
topics:
- kl.05_duality_and_characters
uses:
- kl.detail.local_intersection
- kl.detail.graded_character
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.BruhatGraph.localIntersection_diagonal_strict_degree
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:186
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.localIntersection_diagonal_strict_degree
  - artifact: openai-kl-paper
    locator: Related paper context; bg:normalization
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
- duality_and_characters
---

# A nonzero local diagonal forces a strict half-degree bound

Let \(x<b\), and let \(m_i\) be a homogeneous stalk basis with dual basis \(\lambda_i\) and degrees \(d_i\). If
\[
\lambda_i(I_x\lambda_i)\ne0,
\]
then
\[
2d_i<d(x,b).
\]

*Proof.*

The graded duality makes the displayed diagonal entry homogeneous of degree \(d(x,b)-2d_i\). Minimality puts every coordinate of the image of \(I_x\) in the positive-degree ideal. A nonzero homogeneous element of that ideal has strictly positive degree. Therefore \(d(x,b)-2d_i>0\).

The nonvanishing assumption is part of this proved implication. It is not a claim that every diagonal of every chosen basis is nonzero. Accordingly, this conditional local statement should not be used as an unconditional stalk-character identification. The R-first proof route uses actual-character reciprocity and simultaneous comparison to reach KL invariance.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization



`OAI.KLInvariance.BruhatGraph.localIntersection_diagonal_strict_degree`: [PositiveTransfer.lean:186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L186).
