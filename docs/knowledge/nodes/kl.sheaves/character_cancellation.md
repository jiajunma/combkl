---
id: kl.notes.character_cancellation
title: Cancelling lower summands in character identities
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
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

### Step 1. Expand the right-hand side in a fixed order

The hypothesis is
\[
\sum_y m_yq_y=\sum_z r_z\left(\sum_y m_yp_{y,z}\right).
\]
All sums are finite. Distribute multiplication and interchange the summation order:
\[
\sum_z\sum_y r_zm_yp_{y,z}
=\sum_y m_y\left(\sum_zr_zp_{y,z}\right).
\]
Only commutativity and finite distributivity are used.

### Step 2. Move all terms into one sum

Subtract the expanded right-hand side from the left:
\[
0=\sum_y m_y\left(q_y-\sum_zr_zp_{y,z}\right).
\]
The displayed identity follows by distributivity in the coefficient ring.

### Step 3. Eliminate each lower-index term

For every \(y\ne t\), the lower identity says
\(q_y=\sum_zr_zp_{y,z}\). Its parenthesized factor is therefore zero, so that entire summand is zero, regardless of the value of \(m_y\).

The only remaining summand is
\(m_t(q_t-\sum_zr_zp_{t,z})\).

### Step 4. Use the normalized top multiplicity

The hypothesis \(m_t=1\) changes the last equality to
\(q_t-\sum_zr_zp_{t,z}=0\).
Add the finite sum to both sides to obtain the conclusion.

The normalization at the top makes this a finite-sum identity over the original commutative ring, so it applies directly to integral character polynomials.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization

`OAI.KLInvariance.finite_character_cancellation`: [DyerPaths.lean:15](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L15).
