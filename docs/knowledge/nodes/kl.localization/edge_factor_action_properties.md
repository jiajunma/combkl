---
id: kl.local.edge_factor_action_properties
title: Degree shift and injectivity of the edge-factor action
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.edge_factor_action
- kl.local.edge_factor_lift_properties
- kl.paths.plane_degree
- kl.algebra.scalar_quotient_regular
- kl.detail.root_reflection_correspondence
- kl.detail.root_inversion_count
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.BruhatGraph.rootRef_root
  - OAI.KLInvariance.BruhatGraph.root_not_inverted
  - OAI.KLInvariance.BruhatGraph.edgeFactorDegree_edge
  - OAI.KLInvariance.BruhatGraph.edgeFactorMap_graded
  - OAI.KLInvariance.BruhatGraph.edgeFactorLift_regular
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1424
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.rootRef_root
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1429
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.root_not_inverted
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1440
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edgeFactorDegree_edge
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1453
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edgeFactorMap_graded
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1462
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edgeFactorLift_regular
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the root-reflection identification, source noninversion contradiction,
    exact edge degree, graded scalar action and edgeFactorLift_regular. Verified the
    actual finite free upper stalk, upper quotient, prime root and nondivisibility
    hypotheses, and expanded the coordinate cancellation.
tags:
- Kazhdan-Lusztig
- correction-factors
---

# Degree shift and injectivity of the edge-factor action

Let \(B\) be a boundary sheaf on a Bruhat interval of a finite-generator real Coxeter system, over the polynomial coefficient algebra \(A\) of a finite basis of its extended realization. Fix an edge \(e:x\to y\), its positive root \(a_e\), and
\[
\delta_e=d_{x,a_e},\qquad
\mu_e(v)=F_{x,a_e}v.
\]
Then
\[
2\delta_e=\ell(y)-\ell(x)-1,\qquad
\mu_e(B^e_n)\subseteq B^e_{n+\delta_e},
\]
and \(\mu_e\) is injective.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The quotient factor through an explicit polynomial scalar.**

**OpenAI notes:** The edge factor is an element of the edge coefficient ring and scales the upper image inside the edge module. Its degree supplies the comparison shift, and its nonzero scalar action retains freeness of the scaled free target. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** Multiplication is defined on the actual edge module using edgeFactorLift in the original coefficient algebra. The source identifies the edge root, proves the grading shift and proves injectivity on the whole edge module from the free upper stalk, scalar quotient kernel and prime-root nondivisibility. [PlaneLocalization:1449](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1449), [PlaneLocalization:1440](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1440), [PlaneLocalization:1453](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1453), [PlaneLocalization:1462](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1462).

**Role in the proof:** The polynomial lift, its quotient class and the module endomorphism have separate definitions. The actual scalar action carries the degree shift used later in Hilbert comparison.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Identify the reflection and check noninversion

The positive root \(a_e\) represents the edge's left reflection label, so
\[
r_{a_e}=yx^{-1},\qquad r_{a_e}x=y.
\]
If \(x^{-1}a_e\) were negative, the [[node:kl.detail.root_inversion_count|root-sign length criterion]] would give
\(\ell(r_{a_e}x)<\ell(x)\). This contradicts the upward edge inequality
\(\ell(x)<\ell(y)\).

Thus the root is not inverted at \(x\), which is the hypothesis of the [[node:kl.paths.plane_degree|edge-factor degree theorem]].

### Step 2. Obtain the exact degree

Apply that theorem to \(x,a_e\), and substitute \(r_{a_e}x=y\). It gives
\[
2\delta_e=\ell(y)-\ell(x)-1.
\]
This is edgeFactorDegree_edge.

### Step 3. Apply the graded scalar action

The [[node:kl.local.edge_factor_lift_properties|polynomial-lift properties theorem]] puts \(F_{x,a_e}\) in the degree-\(\delta_e\) piece of \(A\).

The graded module action sends a scalar of degree \(\delta_e\) and a vector of degree \(n\) to a vector of degree \(n+\delta_e\). Since \(\mu_e\) is that scalar multiplication, the claimed grading formula follows.

### Step 4. Verify the scalar-quotient hypotheses

Let \(M=B^y\), \(N=B^e\), and \(q=\rho^+_e\). The boundary sheaf supplies a finite free stalk \(M\), a surjective map \(q\), and
\[
\ker q=\lambda(a_e)M.
\]
The scalar \(\lambda(a_e)\) is prime. The [[node:kl.local.edge_factor_lift_properties|polynomial-lift properties theorem]] gives
\[
\lambda(a_e)\nmid F_{x,a_e}.
\]
These are all hypotheses of the [[node:kl.algebra.scalar_quotient_regular|regular-scalar quotient theorem]].

### Step 5. Carry out the cancellation in stalk coordinates

Suppose \(F_{x,a_e}v=0\) in \(N\). Lift \(v\) to \(m\in M\). The kernel formula gives
\[
F_{x,a_e}m=\lambda(a_e)w
\]
for some \(w\in M\).

In a free basis of \(M\), every coordinate satisfies
\(F_{x,a_e}m_i=\lambda(a_e)w_i\). Primality and the nondivisibility from Step 4 force \(\lambda(a_e)\mid m_i\) for every \(i\). Hence \(m\in\lambda(a_e)M=\ker q\), so \(v=0\).

Applying this to the difference of two vectors with the same image proves injectivity of \(\mu_e\).

For a covering edge, the degree is zero and every plane weight is zero. Both defining products are empty, so \(F_{x,a_e}=1\) and \(\mu_e\) is the identity map.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.rootRef_root`: [PlaneLocalization.lean:1424](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1424).

`OAI.KLInvariance.BruhatGraph.root_not_inverted`: [PlaneLocalization.lean:1429](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1429).

`OAI.KLInvariance.BruhatGraph.edgeFactorDegree_edge`: [PlaneLocalization.lean:1440](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1440).

`OAI.KLInvariance.BruhatGraph.edgeFactorMap_graded`: [PlaneLocalization.lean:1453](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1453).

`OAI.KLInvariance.BruhatGraph.edgeFactorLift_regular`: [PlaneLocalization.lean:1462](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1462).
