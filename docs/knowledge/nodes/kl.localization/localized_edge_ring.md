---
id: kl.local.localized_edge_ring
title: The localized edge ring and its reduction map
kind: definition
status: formalized
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.detail.localization_rings
- kl.algebra.edge_coefficient_ring
- kl.algebra.tensor_scalar_quotient
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.TitsSpace.localizedEdgeIdeal
  - OAI.KLInvariance.TitsSpace.LocalizedEdgeRing
  - OAI.KLInvariance.TitsSpace.localizedReduction
  - OAI.KLInvariance.TitsSpace.localizedReduction_self
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1309
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.localizedEdgeIdeal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1312
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.LocalizedEdgeRing
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1315
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.localizedReduction
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1320
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.localizedReduction_self
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read localizedEdgeIdeal, LocalizedEdgeRing, localizedReduction and its
    self-vanishing. Defined all maps and their domains, retained independent P and
    a, and explained the induced original-quotient map and the exact tensor formula.
tags:
- Kazhdan-Lusztig
- coefficient-rings
---

# The localized edge ring and its reduction map

Fix a finite-generator Coxeter system, its original root space \(V_0\), and a polynomial coefficient algebra \(A\) from a finite real basis of the extended realization. Let
\[
\lambda:V_0\to A,\qquad
\eta_P:A\to R_P=A_{\mathfrak p_P},\qquad
\lambda_P=\eta_P\lambda
\]
be the linear label, localization, and localized label maps for a subspace \(P\subseteq V_0\).

For any \(a\in V_0\), define the **localized edge ideal**
\[
J_{P,a}=(\lambda_P(a))\subseteq R_P
\]
and the **localized edge ring**
\[
E_{P,a}=R_P/J_{P,a}.
\]
These are localizedEdgeIdeal and LocalizedEdgeRing. Write
\[
q_{P,a}:R_P\to E_{P,a}
\]
for the quotient map.

## Reduction of root-space vectors

The **localized reduction map** is the real-linear map
\[
r_{P,a}:V_0\to E_{P,a},\qquad
r_{P,a}(v)=q_{P,a}(\eta_P(\lambda(v))).
\]
This is localizedReduction. Its value at \(a\) is zero, because \(\lambda_P(a)\) generates the quotient ideal:
\[
r_{P,a}(a)=0.
\]

The construction specifies \(P\) and \(a\) independently. The later edge calculation takes \(a\) to be the current edge root and \(P\) to be a root plane containing it.

## The map from the original edge quotient

Let \(E_a=A/(\lambda(a))\), with quotient map \(q_a\). Since \(q_{P,a}\eta_P\) kills \(\lambda(a)\), it factors through
\[
\overline\eta_{P,a}:E_a\to E_{P,a},
\qquad
[f]\longmapsto q_{P,a}(\eta_P(f)).
\]
Changing \(f\) by \(\lambda(a)g\) changes its image by
\(q_{P,a}(\lambda_P(a)\eta_P(g))=0\), so this map is well defined. It satisfies
\[
\overline\eta_{P,a}\,q_a=q_{P,a}\eta_P.
\]

The [[node:kl.algebra.tensor_scalar_quotient|tensor-quotient theorem]] identifies its scalar extension:
\[
R_P\otimes_A E_a\xrightarrow{\sim}E_{P,a},
\qquad
s\otimes[f]\longmapsto q_{P,a}(s\eta_P(f)).
\]
Thus a root label has the same image under either route through these coefficient maps.

## A concrete reduction

In the illustrative ring \(A=\mathbb R[\alpha,\beta,\gamma]\), take
\(\mathfrak p_P=(\alpha,\beta)\) and kill the root label \(\alpha\). Then
\[
E_{P,\alpha}
=A_{(\alpha,\beta)}/(\alpha/1).
\]
The class of \(\gamma/1\) is a unit, and the class of
\((\alpha+2\beta)/1\) is twice the class of \(\beta/1\). The [[node:kl.local.localized_root_reduction|localized root-reduction theorem]] derives the corresponding scalar identity for actual positive roots.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit coefficient maps and scalar reduction.**

**OpenAI notes:** The edge-image proof localizes at the plane prime, passes to the quotient by the current root label, and expresses the remaining plane labels as uniformizers times units in the resulting localized edge ring. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The coefficient operations are explicit tensor and quotient maps. A real-linear reduction kills the current root; writing another root as s*a+r*b gives a nonzero field coefficient r and therefore a unit multiple after reduction. The root-label compatibility formulas identify these elements with the actual polynomial labels. [MinimalExtensions:1239](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1239), [PlaneLocalization:1315](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1315), [PlaneLocalization:1268](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1268), [PlaneLocalization:1330](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1330), [PlaneLocalization:1555](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1555).

**Role in the proof:** The reduced-label comparison is an equality up to an explicitly obtained unit. Later product arguments use associated elements in the localized quotient ring to compare actual scalar-image submodules.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.localizedEdgeIdeal`: [PlaneLocalization.lean:1309](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1309).

`OAI.KLInvariance.TitsSpace.LocalizedEdgeRing`: [PlaneLocalization.lean:1312](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1312).

`OAI.KLInvariance.TitsSpace.localizedReduction`: [PlaneLocalization.lean:1315](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1315).

`OAI.KLInvariance.TitsSpace.localizedReduction_self`: [PlaneLocalization.lean:1320](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1320).
