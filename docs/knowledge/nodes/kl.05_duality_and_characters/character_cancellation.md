---
id: kl.notes.character_cancellation
title: Cancelling lower summands in character identities
kind: theorem
status: proved
primary_topic: kl.05_duality_and_characters
topics:
- kl.05_duality_and_characters
uses: []
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.finite_character_cancellation
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:15
    format: lean-location
    note: OAI.KLInvariance.finite_character_cancellation
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; bg:normalization
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
- background
---

# Cancelling lower summands in character identities

Let the indexing set be finite and let the coefficients lie in a commutative ring. Suppose \(m_t=1\),
\[
\sum_y m_yq_y=\sum_z r_z\sum_y m_yp_{y,z},
\]
and, for every \(y\ne t\),
\[
q_y=\sum_z r_zp_{y,z}.
\]
Then the same identity holds for \(t\):
\[
q_t=\sum_z r_zp_{t,z}.
\]

*Proof.*

Interchange the two finite sums on the right and bring them to the left:
\[
0=\sum_y m_y\left(q_y-\sum_z r_zp_{y,z}\right).
\]
All summands except \(y=t\) vanish by hypothesis. The remaining coefficient is \(m_t=1\), so the bracket at \(t\) vanishes.

In the application, the word object decomposes into boundary objects. The same multiplicities occur in its stalk and kernel character decompositions. Reciprocity is already known for the lower summands by induction, and the top multiplicity is one. This elementary cancellation extracts reciprocity for the actual top boundary object. It does not require identifying that object's stalk character with the canonical KL polynomial.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization

`OAI.KLInvariance.finite_character_cancellation`: [DyerPaths.lean:15](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L15).
