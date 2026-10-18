---
id: kl.detail.transfer_properties
title: Monotonicity and injectivity of elementary transfers
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.comparison.positive_transfer
lean:
  repository: openai-kl
  modules:
  - Comparison
  declarations:
  - OAI.KLInvariance.Comparison.transfer_monotone
  - OAI.KLInvariance.Comparison.transfer_injective
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Comparison:77
    format: lean-location
    note: OAI.KLInvariance.Comparison.transfer_monotone
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Comparison:85
    format: lean-location
    note: OAI.KLInvariance.Comparison.transfer_injective
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

# Monotonicity and injectivity of elementary transfers

For \(x\ne y\), define \(\tau_{x,y,T}=1+TE_{xy}\) on real vectors indexed by vertices. Then:

- If \(T\geq0\), \(\tau_{x,y,T}\) preserves the coordinatewise order.
- For every real \(T\), \(\tau_{x,y,T}\) is injective; its inverse is \(1-TE_{xy}\).

*Proof.*

### Step 1. Write the map coordinate by coordinate

Let \(V\) be the vertex set and \(x\ne y\). For \(v:V\to\mathbb R\),
\[
(\tau v)_x=v_x+Tv_y,\qquad(\tau v)_z=v_z\quad(z\ne x).
\]
In particular \((\tau v)_y=v_y\), because \(y\ne x\).

### Step 2. Check monotonicity at every coordinate

Assume \(T\ge0\) and \(v_z\le w_z\) for all \(z\). At \(z\ne x\),
\((\tau v)_z=v_z\le w_z=(\tau w)_z\).
At \(x\), multiplication of \(v_y\le w_y\) by \(T\) preserves the inequality, so
\[
v_x+Tv_y\le w_x+Tw_y.
\]
These are all coordinates, hence \(\tau v\le\tau w\). Neither \(v\) nor \(w\) is required to have nonnegative coordinates.

### Step 3. Recover a vector from its image

For arbitrary real \(T\), suppose \(\tau v=\tau w\). Equality at \(y\) gives \(v_y=w_y\). Equality at \(x\) now reads
\(v_x+Tv_y=w_x+Tv_y\), so \(v_x=w_x\). Equality at any other coordinate gives \(v_z=w_z\). Thus \(v=w\).

Equivalently, for a given image \(u\), define
\(v_y=u_y\), \(v_x=u_x-Tu_y\), and \(v_z=u_z\) at the remaining coordinates. Substitution into the formula in Step 1 verifies both inverse identities. This proves injectivity without assuming \(T\ge0\).

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization



`OAI.KLInvariance.Comparison.transfer_monotone`: [Comparison.lean:77](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L77).

`OAI.KLInvariance.Comparison.transfer_injective`: [Comparison.lean:85](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L85).
