---
id: kl.detail.root_inversions
title: Positive-root inversion sets
kind: definition
status: formalized
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.detail.positive_roots
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.RootInversions
  - OAI.KLInvariance.TitsSpace.rootInversionEquiv
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:2039
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.RootInversions
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:2042
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.rootInversionEquiv
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# Positive-root inversion sets

For \(w\in W\), define its left root-inversion set by
\[
\operatorname{Inv}_{\Phi}(w)=\{a\in\Phi^+:w^{-1}a\in-\Phi^+\}.
\]
The inverse on \(w\) is essential: this is the convention corresponding to left reflection multiplication. A reflection \(t\) is a left inversion of \(w\) when \(\ell(tw)<\ell(w)\). Under the root–reflection correspondence,
\[
a\in\operatorname{Inv}_{\Phi}(w)\quad\Longleftrightarrow\quad
\ell(r_a w)<\ell(w).
\]
The sign criterion and the equality \(|\operatorname{Inv}_{\Phi}(w)|=\ell(w)\) are proved in the inversion-count theorem. An infinite ambient root system therefore still gives a finite inversion set for each element.

For a reduced word \(w=s_{i_1}\cdots s_{i_m}\), its left inversion sequence consists of the reflections
\[
t_j=(s_{i_1}\cdots s_{i_{j-1}})s_{i_j}(s_{i_1}\cdots s_{i_{j-1}})^{-1}.
\]
The corresponding positive roots are the distinct roots inverted by \(w^{-1}\).

## References

The precise Lean sources are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.RootInversions`: [Tits.lean:2039](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L2039).

`OAI.KLInvariance.TitsSpace.rootInversionEquiv`: [Tits.lean:2042](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L2042).
