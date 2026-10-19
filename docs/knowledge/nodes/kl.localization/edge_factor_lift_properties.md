---
id: kl.local.edge_factor_lift_properties
title: Degree, reduction and root nondivisibility of the polynomial lift
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.edge_factor_lift
- kl.local.edge_factor_properties
- kl.algebra.linear_primes
- kl.realization.root_planes
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.BruhatGraph.polynomialRoot_homogeneous
  - OAI.KLInvariance.BruhatGraph.polynomialRoot_prime
  - OAI.KLInvariance.BruhatGraph.polynomialRoot_not_dvd
  - OAI.KLInvariance.BruhatGraph.edgeFactorLift_homogeneous
  - OAI.KLInvariance.BruhatGraph.edgeFactorLift_not_dvd
  - OAI.KLInvariance.BruhatGraph.edgeFactorLift_reduction
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1360
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.polynomialRoot_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1372
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.polynomialRoot_prime
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1379
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.polynomialRoot_not_dvd
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1393
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edgeFactorLift_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1404
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edgeFactorLift_not_dvd
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1413
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edgeFactorLift_reduction
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the exact graded-product proof, polynomialRoot primality and linear-generator
    divisibility argument, prime divisibility of a finite product and powers, and
    the reduction identity. Preserved actual equality in the symmetric quotient and
    all zero-exponent/empty-product cases.
tags:
- Kazhdan-Lusztig
- correction-factors
---

# Degree, reduction and root nondivisibility of the polynomial lift

Let \(W\) be a finite-generator real Coxeter system with a chosen finite basis of the extended realization \(V\), polynomial coefficient algebra \(A\), and coordinate isomorphism \(\Phi:\operatorname{Sym}_{\mathbb R}(V)\simeq A\). Fix \(x\in W\) and a positive root \(a\). Write \(\lambda(b)=\Phi(\iota(i_0b))\) for a root's polynomial, where \(i_0\) is the original-root embedding and \(\iota\) the symmetric-algebra inclusion. Let \(q_a\) be the symmetric-algebra quotient map killing \(\iota(i_0a)\).

For the polynomial lift \(F_{x,a}\), edge factor \(f_{x,a}\) and exponent sum \(d_{x,a}\),
\[
F_{x,a}\in A_{d_{x,a}},\qquad
\lambda(a)\nmid F_{x,a},\qquad
q_a(\Phi^{-1}(F_{x,a}))=f_{x,a}.
\]
The grading gives each linear root label degree one.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The same root product with explicit weight and coordinate constructions.**

**OpenAI notes:** The notes assign each plane its half-excess relative dihedral length, choose an independent root whenever that weight is positive, and multiply its reduced linear form to that power in the edge quotient. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The weights are first constructed by grouping half-root indicators. planeWeight_coset_edge identifies them with the relative dihedral length formula. planeRoot chooses a positive root with the required plane, edgeFactor is a product in the symmetric quotient, and edgeFactorLift is its explicit product before the polynomial quotient. The definitions and nonvanishing hold for every x; noninversion is used for the length-degree formula. [ReflectionSchedules:908](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L908), [ReflectionSchedules:944](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L944), [ReflectionSchedules:985](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L985), [ReflectionSchedules:993](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L993), [PlaneLocalization:1389](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1389), [PlaneLocalization:1413](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1413), [PlaneLocalization:1096](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1096).

**Role in the proof:** The Blueprint keeps the chosen representatives, all scalar maps and the natural/integer exponent conversion explicit. The quotient of the polynomial lift is exactly the constructed edge factor.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Identify the homogeneous linear labels

Expand an embedded root in the chosen basis:
\[
i_0b=\sum_i c_i v_i.
\]
The coordinate isomorphism sends its symmetric generator to
\[
\lambda(b)=\sum_i c_iX_i.
\]
Each scalar multiple of a variable belongs to the homogeneous degree-one piece, including a term with zero coefficient. Hence \(\lambda(b)\) is homogeneous of degree one.

The \(k_P\)-th power of \(\lambda(b_P)\) has degree \(k_P\), and multiplication adds these degrees. Therefore
\[
F_{x,a}=\prod_P\lambda(b_P)^{k_P}
\]
is homogeneous of degree \(\sum_Pk_P=d_{x,a}\). This is the source's graded product calculation.

### Step 2. Exclude divisibility between the current root and a factor root

The polynomial \(\lambda(a)\) is prime: the embedded root is nonzero, and a nonzero symmetric-algebra linear generator is prime; the coordinate isomorphism preserves this property.

Suppose \(\lambda(a)\mid\lambda(b_P)\). Transporting divisibility through \(\Phi^{-1}\), the [[node:kl.algebra.linear_primes|linear-generator divisibility theorem]] puts \(i_0b_P\) in the line \(\mathbb R i_0a\).

Injectivity of \(i_0\) would put \(b_P\) in \(\mathbb R a\), contradicting independence of the distinct positive roots \(a,b_P\). Thus
\(\lambda(a)\nmid\lambda(b_P)\).

### Step 3. Exclude divisibility of the full product

If the prime \(\lambda(a)\) divided \(F_{x,a}\), repeated use of its prime-product property would make it divide one factor
\(\lambda(b_P)^{k_P}\).

For a power \(z^{n+1}=z^nz\), the prime-product property gives divisibility of \(z^n\) or of \(z\). Induction therefore makes divisibility of a positive power imply divisibility of its base, contradicting Step 2. A zeroth power is \(1\), which a prime nonunit cannot divide. If the full product is empty, it is also \(1\). These cases prove
\[
\lambda(a)\nmid F_{x,a}.
\]

### Step 4. Reduce the product through the coordinate isomorphism

Both \(\Phi^{-1}\) and \(q_a\) preserve products and powers. For each representative,
\[
q_a(\Phi^{-1}(\lambda(b_P)))
=q_a(\iota(i_0b_P))
=r_P.
\]
Hence
\[
q_a(\Phi^{-1}(F_{x,a}))
=\prod_Pr_P^{k_P}
=f_{x,a}.
\]
The representatives and exponents are exactly the same on both sides, so this is equality of elements, as asserted by edgeFactorLift_reduction.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.polynomialRoot_homogeneous`: [PlaneLocalization.lean:1360](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1360).

`OAI.KLInvariance.BruhatGraph.polynomialRoot_prime`: [PlaneLocalization.lean:1372](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1372).

`OAI.KLInvariance.BruhatGraph.polynomialRoot_not_dvd`: [PlaneLocalization.lean:1379](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1379).

`OAI.KLInvariance.BruhatGraph.edgeFactorLift_homogeneous`: [PlaneLocalization.lean:1393](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1393).

`OAI.KLInvariance.BruhatGraph.edgeFactorLift_not_dvd`: [PlaneLocalization.lean:1404](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1404).

`OAI.KLInvariance.BruhatGraph.edgeFactorLift_reduction`: [PlaneLocalization.lean:1413](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1413).
