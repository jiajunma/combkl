---
id: kl.paths.plane_degree
title: The degree of the reduced-root edge factor
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.geometry.plane_weight_sum
- kl.detail.edge_factor
- kl.local.edge_factor_properties
- kl.detail.root_inversions
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.TitsSpace.edgeFactorDegree_cast
  - OAI.KLInvariance.TitsSpace.edgeFactor_degree_formula
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:985
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.edgeFactorDegree_cast
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:993
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.edgeFactor_degree_formula
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the exact natural-to-integer conversion in edgeFactorDegree_cast and
    the noninversion hypothesis of edgeFactor_degree_formula. Reused the separate
    nonzero/homogeneity theorem and expanded the cover and A2 long-edge examples while
    retaining the noncanonical representative choice.
tags:
- Kazhdan-Lusztig
- correction-factors
---

# The degree of the reduced-root edge factor

Let \(W\) be a finite-generator real Coxeter system. Fix \(x\in W\) and a positive root \(a\) such that \(x^{-1}a\) is positive, and set \(y=r_ax\).

Let \(V\) be the extended realization, \(i_0\) the original-root embedding and \(\iota\) the symmetric-algebra inclusion. Choose polynomial coordinates \(\Psi_a\) on
\[
E_a=\operatorname{Sym}_{\mathbb R}(V)/(\iota(i_0a)),
\]
the edge factor satisfies
\[
2\operatorname{totaldeg}\Psi_a(f_{x,a})
=\ell(y)-\ell(x)-1.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The same root product with explicit weight and coordinate constructions.**

**OpenAI notes:** The notes assign each plane its half-excess relative dihedral length, choose an independent root whenever that weight is positive, and multiply its reduced linear form to that power in the edge quotient. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The weights are first constructed by grouping half-root indicators. planeWeight_coset_edge identifies them with the relative dihedral length formula. planeRoot chooses a positive root with the required plane, edgeFactor is a product in the symmetric quotient, and edgeFactorLift is its explicit product before the polynomial quotient. The definitions and nonvanishing hold for every x; noninversion is used for the length-degree formula. [ReflectionSchedules:908](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L908), [ReflectionSchedules:944](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L944), [ReflectionSchedules:985](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L985), [ReflectionSchedules:993](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L993), [PlaneLocalization:1389](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1389), [PlaneLocalization:1413](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1413), [PlaneLocalization:1096](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1096).

**Role in the proof:** The Blueprint keeps the chosen representatives, all scalar maps and the natural/integer exponent conversion explicit. The quotient of the polynomial lift is exactly the constructed edge factor.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Replace total degree by the exponent sum

The [[node:kl.local.edge_factor_properties|edge-factor properties theorem]] gives
\[
\operatorname{totaldeg}\Psi_a(f_{x,a})=d_{x,a}
=\sum_{P\in\mathcal P(x,a)}(k_P)_{\mathbb N}.
\]
Here \((k_P)_{\mathbb N}\) is the natural-number conversion used by the source.

### Step 2. Compare the natural and integer sums

Every weight is nonnegative, so
\[
((k_P)_{\mathbb N}:\mathbb Z)=k_P.
\]
Casting a finite sum to the integers commutes with addition. Outside the supported set the weights are zero. Therefore
\[
(d_{x,a}:\mathbb Z)=\sum_Pk_P.
\]
This is edgeFactorDegree_cast.

### Step 3. Apply the plane-weight count with its exact hypothesis

The hypothesis that \(x^{-1}a\) is a positive root is precisely the noninversion hypothesis of the [[node:kl.geometry.plane_weight_sum|geometric plane-weight sum theorem]]. It gives
\[
2\sum_Pk_P=\ell(r_ax)-\ell(x)-1.
\]
Substitute Step 2 and then Step 1 to obtain the required degree formula.

### Step 4. Evaluate the covering-edge case

If \(\ell(y)=\ell(x)+1\), the degree formula gives \(d_{x,a}=0\). Every plane weight is nonnegative, so every weight is zero. The support is empty and the defining product is
\[
f_{x,a}=1.
\]

### Step 5. Evaluate the long edge in type A2

For an illustration, take simple roots \(a,b\) in type \(A_2\), with simple reflections \(s,t\), and put \(c=a+b\). The reflection \(r_c=sts\) has length three. For \(x=1\), the formula gives
\[
d_{1,c}=\frac{3-0-1}{2}=1.
\]

All roots lie in the single plane \(P=\operatorname{span}\{a,b\}\), so \(k_P=1\). The chosen representative different from \(c\) is one of \(a,b\).

Write \(\alpha=\iota(i_0a)\), \(\beta=\iota(i_0b)\). In the edge quotient by \(\iota(i_0c)=\alpha+\beta\),
\[
\overline\beta=-\overline\alpha.
\]
Thus the actual chosen factor is \(\overline\alpha\) or \(\overline\beta=-\overline\alpha\), according to that representative. In either case it is a nonzero homogeneous factor of degree one, as the formula predicts.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.edgeFactorDegree_cast`: [ReflectionSchedules.lean:985](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L985).

`OAI.KLInvariance.TitsSpace.edgeFactor_degree_formula`: [ReflectionSchedules.lean:993](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L993).
