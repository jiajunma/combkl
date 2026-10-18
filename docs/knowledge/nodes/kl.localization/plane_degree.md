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
- kl.detail.linear_quotient
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.TitsSpace.edgeFactor_homogeneous
  - OAI.KLInvariance.TitsSpace.edgeFactor_totalDegree
  - OAI.KLInvariance.TitsSpace.edgeFactorDegree_cast
  - OAI.KLInvariance.TitsSpace.edgeFactor_degree_formula
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:966
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.edgeFactor_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:975
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.edgeFactor_totalDegree
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
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- dihedral
---

# The degree of the reduced-root edge factor

Let \(x^{-1}\alpha\) be positive and let \(y=r_\alpha x\). Form the edge factor \(f_{x,\alpha}\) in
\[
A_\alpha=\operatorname{Sym}_{\mathbb R}(V)/(\alpha)
\simeq\operatorname{Sym}_{\mathbb R}(V/\mathbb R\alpha),
\]
where \(V\) is the extended root space and roots are embedded in it. In any polynomial coordinates on this quotient,
\[
2\deg f_{x,\alpha}=\ell(y)-\ell(x)-1.
\]

*Proof.*

### Step 1. Identify the factors and their exponents

For each plane of positive weight \(k_P(x,\alpha)\), choose its root representative \(\beta_P\ne\alpha\). The definition is the finite product
\[
f_{x,\alpha}=\prod_P\overline\beta_P^{\,k_P(x,\alpha)}.
\]
The plane weights are nonnegative integers, so these are ordinary nonnegative powers.

### Step 2. Check the reduced factors

Distinct positive roots are linearly independent in pairs. Indeed, proportional positive roots have a positive proportionality scalar, and their squared norm two makes that scalar one. Their images in the extended space retain this independence.

Hence \(\beta_P\) has nonzero image in \(V/\mathbb R\alpha\). Its image in the symmetric algebra is a nonzero linear polynomial, homogeneous of degree one.

### Step 3. Compute the product degree

Choosing a basis of \(V/\mathbb R\alpha\) identifies its symmetric algebra with a polynomial ring over \(\mathbb R\). It is a domain. Therefore the product is nonzero. Each factor raised to exponent \(k_P\) is homogeneous of degree \(k_P\), so the product is homogeneous of degree \(\sum_P k_P\).

For a nonzero homogeneous polynomial, every monomial with nonzero coefficient has that degree. Its total degree is therefore
\[
\deg f_{x,\alpha}=\sum_Pk_P(x,\alpha).
\]

### Step 4. Apply the geometric count

The geometric plane-weight theorem gives
\[
2\sum_Pk_P(x,\alpha)=\ell(y)-\ell(x)-1.
\]
Substitution of the degree from Step 3 proves the assertion.

## References

The local root-sign and plane-weight calculations are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.edgeFactor_homogeneous`: [ReflectionSchedules.lean:966](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L966).

`OAI.KLInvariance.TitsSpace.edgeFactor_totalDegree`: [ReflectionSchedules.lean:975](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L975).

`OAI.KLInvariance.TitsSpace.edgeFactorDegree_cast`: [ReflectionSchedules.lean:985](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L985).

`OAI.KLInvariance.TitsSpace.edgeFactor_degree_formula`: [ReflectionSchedules.lean:993](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L993).
