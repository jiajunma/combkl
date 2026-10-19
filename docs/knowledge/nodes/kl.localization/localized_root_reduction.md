---
id: kl.local.localized_root_reduction
title: Root labels in a localized edge quotient
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.localized_edge_ring
- kl.algebra.plane_reduction
- kl.realization.root_planes
- kl.algebra.edge_coefficient_ring
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.TitsSpace.localizedReduction_self
  - OAI.KLInvariance.TitsSpace.positiveRoot_not_line
  - OAI.KLInvariance.TitsSpace.localizedReduction_associated
  - OAI.KLInvariance.TitsSpace.polynomialRoot_localized
  - OAI.KLInvariance.TitsSpace.polynomialRoot_reduced
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1320
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.localizedReduction_self
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1324
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.positiveRoot_not_line
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1330
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.localizedReduction_associated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1551
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.polynomialRoot_localized
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1555
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.polynomialRoot_reduced
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read localizedReduction_associated with its arbitrary localization subspace
    P, the distinct-positive-root line exclusion, and both definitional polynomial-root
    compatibility formulas. Kept the span P(a,b) separate from P and derived the explicit
    nonzero real coefficient through the generic lemma.
tags:
- Kazhdan-Lusztig
- coefficient-rings
---

# Root labels in a localized edge quotient

Fix a finite-generator Coxeter system, its original root space \(V_0\), and the embedding \(i_0:V_0\hookrightarrow V\) into the extended realization. A finite real basis gives polynomial coordinates \(\Phi:\operatorname{Sym}_{\mathbb R}(V)\to A\) and labels
\(\lambda(v)=\Phi(\iota(i_0v))\).

For any subspace \(P\subseteq V_0\) and vector \(a\), use the maps
\[
\eta_P:A\to R_P=A_{\mathfrak p_P},\qquad
q_{P,a}:R_P\to E_{P,a}=R_P/(\eta_P(\lambda(a))),
\]
\[
\lambda_P=\eta_P\lambda,\qquad
r_{P,a}=q_{P,a}\eta_P\lambda.
\]
The map \(r_{P,a}\) is the localized reduction that kills \(a\).

Let \(a,b,c\) be positive roots with
\[
c\in P(a,b)=\operatorname{span}_{\mathbb R}\{a,b\},
\qquad c\ne a.
\]
Then \(r_{P,a}(c)\) and \(r_{P,a}(b)\) are associated scalars in \(E_{P,a}\). More explicitly, some nonzero real scalar \(r\) satisfies
\[
r_{P,a}(c)=r\,r_{P,a}(b).
\]

The actual polynomial root labels commute with the coefficient maps:
\[
\eta_P(\operatorname{polynomialRoot}(c))=\lambda_P(c),
\]
\[
q_{P,a}\bigl(\eta_P(\operatorname{polynomialRoot}(c))\bigr)
=r_{P,a}(c).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit coefficient maps and scalar reduction.**

**OpenAI notes:** The edge-image proof localizes at the plane prime, passes to the quotient by the current root label, and expresses the remaining plane labels as uniformizers times units in the resulting localized edge ring. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The coefficient operations are explicit tensor and quotient maps. A real-linear reduction kills the current root; writing another root as s*a+r*b gives a nonzero field coefficient r and therefore a unit multiple after reduction. The root-label compatibility formulas identify these elements with the actual polynomial labels. [MinimalExtensions:1239](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1239), [PlaneLocalization:1315](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1315), [PlaneLocalization:1268](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1268), [PlaneLocalization:1330](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1330), [PlaneLocalization:1555](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1555).

**Role in the proof:** The reduced-label comparison is an equality up to an explicitly obtained unit. Later product arguments use associated elements in the localized quotient ring to compare actual scalar-image submodules.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Exclude the killed root line

Distinct positive roots are linearly independent. If \(c\) belonged to the line \(\mathbb R a\), there would be a scalar \(s\) with \(c=sa\), contradicting that independence for \(c\ne a\).

Thus \(c\notin\mathbb R a\). This is positiveRoot_not_line.

### Step 2. Apply the [[node:kl.algebra.plane_reduction|plane-reduction theorem]]

The localized reduction map is real-linear and satisfies
\(r_{P,a}(a)=0\). The stated plane membership and Step 1 verify the other two hypotheses of the [[node:kl.algebra.plane_reduction|plane-reduction theorem]].

Write \(c=sa+rb\). Its proof gives \(r\ne0\) and
\[
r_{P,a}(c)=r\,r_{P,a}(b).
\]
The image of \(r\) is a unit, with inverse the image of \(r^{-1}\). This proves localizedReduction_associated.

The localization subspace \(P\) is arbitrary in this assertion. The span \(P(a,b)\) supplies the linear relation being reduced.

### Step 3. Follow the polynomial root through localization

By definition,
\[
\operatorname{polynomialRoot}(c)
=\Phi(\iota(i_0c))=\lambda(c).
\]
Applying \(\eta_P\) gives \(\lambda_P(c)\). This is polynomialRoot_localized.

### Step 4. Follow the label through the edge quotient

The localized reduction was defined by
\(r_{P,a}=q_{P,a}\eta_P\lambda\). Substitute Step 3:
\[
q_{P,a}\bigl(\eta_P(\operatorname{polynomialRoot}(c))\bigr)
=q_{P,a}(\lambda_P(c))
=r_{P,a}(c).
\]
This is polynomialRoot_reduced.

The associated labels in Step 2 are therefore the actual reduced polynomial labels used in the edge-module calculation. Their unit relation yields equal principal ideals, and equal scalar-image submodules on any module over \(E_{P,a}\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.localizedReduction_self`: [PlaneLocalization.lean:1320](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1320).

`OAI.KLInvariance.TitsSpace.positiveRoot_not_line`: [PlaneLocalization.lean:1324](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1324).

`OAI.KLInvariance.TitsSpace.localizedReduction_associated`: [PlaneLocalization.lean:1330](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1330).

`OAI.KLInvariance.TitsSpace.polynomialRoot_localized`: [PlaneLocalization.lean:1551](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1551).

`OAI.KLInvariance.TitsSpace.polynomialRoot_reduced`: [PlaneLocalization.lean:1555](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1555).
