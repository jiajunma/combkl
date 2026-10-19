---
id: kl.local.edge_factor_properties
title: Nonvanishing and homogeneity of the edge factor
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.detail.edge_factor
- kl.local.factor_roots
- kl.realization.root_planes
- kl.algebra.root_quotient_coordinates
- kl.algebra.linear_primes
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.TitsSpace.planeWeight_nonneg
  - OAI.KLInvariance.TitsSpace.embed_not_rootLine
  - OAI.KLInvariance.TitsSpace.reducedPlaneRoot_ne_zero
  - OAI.KLInvariance.TitsSpace.edgeFactor_nonzero
  - OAI.KLInvariance.TitsSpace.edgeFactor_homogeneous
  - OAI.KLInvariance.TitsSpace.edgeFactor_totalDegree
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:610
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.planeWeight_nonneg
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:920
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.embed_not_rootLine
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:938
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.reducedPlaneRoot_ne_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:954
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.edgeFactor_nonzero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:966
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.edgeFactor_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:975
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.edgeFactor_totalDegree
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the sum-of-indicators proof of planeWeight_nonneg, the embedded-root
    line exclusion, and all three factor property proofs. Checked nonzero quotient
    vectors, the polynomial domain argument, nonnegative powers, the empty support
    and the use of nonzero homogeneity for total degree.
tags:
- Kazhdan-Lusztig
- correction-factors
---

# Nonvanishing and homogeneity of the edge factor

Let \(W\) be a finite-generator real Coxeter system, \(x\in W\), and \(a\) a positive root. Let \(V\) be the extended realization, \(i_0\) the original-root embedding, and \(\iota\) the degree-one symmetric-algebra inclusion. In the edge coefficient ring \(E_a=\operatorname{Sym}_{\mathbb R}(V)/(\iota(i_0a))\), use the edge factor
\[
f_{x,a}=\prod_{P\in\mathcal P(x,a)}r_P^{k_P}\in E_a
\]
and its quotient polynomial coordinate map \(\Psi_a\). Put
\(d_{x,a}=\sum_Pk_P\). Then
\[
f_{x,a}\ne0,\qquad
\Psi_a(f_{x,a})\text{ is homogeneous of degree }d_{x,a},
\]
and
\[
\operatorname{totaldeg}\Psi_a(f_{x,a})=d_{x,a}.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The same root product with explicit weight and coordinate constructions.**

**OpenAI notes:** The notes assign each plane its half-excess relative dihedral length, choose an independent root whenever that weight is positive, and multiply its reduced linear form to that power in the edge quotient. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The weights are first constructed by grouping half-root indicators. planeWeight_coset_edge identifies them with the relative dihedral length formula. planeRoot chooses a positive root with the required plane, edgeFactor is a product in the symmetric quotient, and edgeFactorLift is its explicit product before the polynomial quotient. The definitions and nonvanishing hold for every x; noninversion is used for the length-degree formula. [ReflectionSchedules:908](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L908), [ReflectionSchedules:944](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L944), [ReflectionSchedules:985](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L985), [ReflectionSchedules:993](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L993), [PlaneLocalization:1389](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1389), [PlaneLocalization:1413](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1413), [PlaneLocalization:1096](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1096).

**Role in the proof:** The Blueprint keeps the chosen representatives, all scalar maps and the natural/integer exponent conversion explicit. The quotient of the polynomial lift is exactly the constructed edge factor.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Read the weights as nonnegative integers

Each half-root indicator has value \(0\) or \(1\). The plane-weight grouping map adds such values within each fiber of the root-plane map.

Thus every \(k_P\) is a finite sum of nonnegative integers, so \(k_P\ge0\). Its natural-number conversion has the same integer value. All powers in the product are therefore ordinary nonnegative powers.

### Step 2. Prove every reduced plane root nonzero

The chosen representative satisfies \(b_P\ne a\). Independence of distinct positive roots gives \(b_P\notin\mathbb R a\). Injectivity of the embedding \(i_0\) then gives
\[
i_0b_P\notin\mathbb R i_0a.
\]
Hence its class in \(V/\mathbb R i_0a\) is nonzero.

The degree-one inclusion of a vector space into its symmetric algebra is injective. Under the linear-quotient isomorphism, \(r_P\) is the image of that nonzero class, so \(r_P\ne0\).

### Step 3. Prove the product nonzero

The coordinate isomorphism \(\Psi_a\) identifies \(E_a\) with a polynomial ring over \(\mathbb R\), which is a domain.

Every factor \(\Psi_a(r_P)\) is nonzero by Step 2 and injectivity of \(\Psi_a\). Its nonnegative power is nonzero, and a finite product of these powers is nonzero. Since
\[
\Psi_a(f_{x,a})=\prod_P\Psi_a(r_P)^{k_P},
\]
injectivity of \(\Psi_a\) gives \(f_{x,a}\ne0\). For an empty support the product is \(1\), so the same conclusion holds.

### Step 4. Add the homogeneous degrees

A vector in the quotient space becomes a linear combination of the variables \(Y_i\); thus \(\Psi_a(r_P)\) is homogeneous of degree one.

Its \(k_P\)-th power is homogeneous of degree \(k_P\), including the zeroth power \(1\). Multiplication adds degrees, so the finite product is homogeneous of degree
\[
\sum_Pk_P=d_{x,a}.
\]

### Step 5. Identify total degree

A nonzero homogeneous polynomial of degree \(d\) has at least one nonzero monomial coefficient, and every such monomial has degree \(d\). The maximum of their degrees is therefore \(d\).

Apply this to the nonzero polynomial from Step 3 and the homogeneous degree from Step 4. This proves the total-degree assertion.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.planeWeight_nonneg`: [ReflectionSchedules.lean:610](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L610).

`OAI.KLInvariance.TitsSpace.embed_not_rootLine`: [ReflectionSchedules.lean:920](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L920).

`OAI.KLInvariance.TitsSpace.reducedPlaneRoot_ne_zero`: [ReflectionSchedules.lean:938](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L938).

`OAI.KLInvariance.TitsSpace.edgeFactor_nonzero`: [ReflectionSchedules.lean:954](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L954).

`OAI.KLInvariance.TitsSpace.edgeFactor_homogeneous`: [ReflectionSchedules.lean:966](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L966).

`OAI.KLInvariance.TitsSpace.edgeFactor_totalDegree`: [ReflectionSchedules.lean:975](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L975).
