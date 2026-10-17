---
id: kl.notes.extended_realization
title: Extending the Tits form without losing the root data
kind: theorem
status: proved
primary_topic: kl.02_background
topics:
- kl.02_background
uses: []
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.extendedForm_spec
  - OAI.KLInvariance.TitsSpace.extendedRoot_linearIndependent
  - OAI.KLInvariance.TitsSpace.extendedNormal_linearIndependent
  - OAI.KLInvariance.TitsSpace.extended_finrank
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:558
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.extendedForm_spec
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:569
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.extendedRoot_linearIndependent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:575
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.extendedNormal_linearIndependent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:613
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.extended_finrank
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; bg:realization
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

# Extending the Tits form without losing the root data

Assume that the simple-generator set \(I\) is finite. Let \(V_0=\mathbb R^I\) with the Tits form \(B\), normalized by
\[
B(\alpha_i,\alpha_i)=2,\qquad
B(\alpha_i,\alpha_j)=-2\cos(\pi/m_{ij}).
\]
The convention for an infinite Coxeter exponent is \(\cos(\pi/\infty)=1\).

The form can be degenerate. Writing \(K=\ker B\), enlarge the space to
\[
V=V_0\oplus K^*.
\]
There exists a symmetric nondegenerate form \(\widetilde B\) extending \(B\) on \(V_0\). The extended simple roots \((\alpha_i,0)\) and the corresponding linear forms \(\widetilde B((\alpha_i,0),-)\) are both independent. Moreover
\[
\dim V=|I|+\dim K.
\]

*Proof.*

Choose a complement \(U\) to \(K\). The restriction of \(B\) to \(U\) is nondegenerate. On
\(U\oplus K\oplus K^*\), keep that restriction and pair \(K\) with \(K^*\) by evaluation:
\[
\widetilde B((u,k,\lambda),(u',k',\lambda'))
=B(u,u')+\lambda(k')+\lambda'(k).
\]
This extends the original form because \(K\) is its radical. Orthogonality to \(K^*\), then to \(K\), then to \(U\), forces all three components to vanish, proving nondegeneracy.

The original roots remain independent under the inclusion \(V_0\hookrightarrow V\). The nondegenerate form identifies \(V\) with its dual, so their normal linear forms are independent as well.

Nondegeneracy is asserted for the ambient space. A two-dimensional root subspace may still have a degenerate restricted form, which is allowed in the infinite-dihedral arguments.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L34).

## Lean formalization

`OAI.KLInvariance.TitsSpace.extendedForm_spec`: [Tits.lean:558](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L558).

`OAI.KLInvariance.TitsSpace.extendedRoot_linearIndependent`: [Tits.lean:569](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L569).

`OAI.KLInvariance.TitsSpace.extendedNormal_linearIndependent`: [Tits.lean:575](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L575).

`OAI.KLInvariance.TitsSpace.extended_finrank`: [Tits.lean:613](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L613).
