---
id: kl.local.factor_plane_reduction
title: The edge factor retains one plane exponent after local reduction
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.edge_factor_lift
- kl.local.factor_roots
- kl.local.localized_root_reduction
- kl.local.plane_prime_membership
- kl.algebra.linear_ideals
- kl.realization.root_planes
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.TitsSpace.planeRoot_outside
  - OAI.KLInvariance.TitsSpace.reduced_planeRoot_other_isUnit
  - OAI.KLInvariance.TitsSpace.edgeFactor_local_associated
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1560
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.planeRoot_outside
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1569
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.reduced_planeRoot_other_isUnit
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1579
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.edgeFactor_local_associated
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read planeRoot_outside, reduced_planeRoot_other_isUnit and all branches
    of edgeFactor_local_associated. Expanded the equal-dimension plane argument, unit
    preservation through the quotient, nonzero transverse real coefficient, finite
    product of associations and absent-plane exponent zero case.
tags:
- Kazhdan-Lusztig
- correction-factors
---

# The edge factor retains one plane exponent after local reduction

Fix a finite-generator real Coxeter system \(W\) and polynomial coefficient algebra \(A\) from a basis of its extended realization. Let \(\lambda(c)\) denote the polynomial of an embedded root \(c\). Let \(x\in W\), and let \(a,b\) be distinct positive roots. Put
\[
P=\operatorname{span}\{a,b\},\qquad
R_P=A_{\mathfrak p_P},\qquad
E_{P,a}=R_P/(\eta_P(\lambda(a))).
\]
Here \(\eta_P:A\to R_P\) is localization and \(q_{P,a}:R_P\to E_{P,a}\) is the quotient map. Write
\[
r_{P,a}(c)=q_{P,a}(\eta_P(\lambda(c)))
\]
for localized root reduction, and put \(p=r_{P,a}(b)\).

The image of the polynomial lift satisfies
\[
q_{P,a}(\eta_P(F_{x,a}))\sim p^{\,k_P(x,a)}
\quad\text{in }E_{P,a},
\]
where \(\sim\) means equality up to multiplication by a unit. The weight is interpreted as its equal natural-number value in the exponent.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Associated products give the local scalar-image calculation.**

**OpenAI notes:** In a localized edge quotient viewed as a discrete valuation ring, the notes compare valuations of later-label products. The current plane contributes its exponent to the correction factor, and all other plane factors are units. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The factor proof directly establishes association with the power of a chosen reduced plane root, checking the same-plane and other-plane factors and the absent-plane case. LocalProducts then works over arbitrary compatible commutative scalar rings: a cardinality equation and associated factors give equality of scalar-image submodules. [PlaneLocalization:1560](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1560), [PlaneLocalization:1569](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1569), [PlaneLocalization:1579](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1579), [PlaneLocalization:1509](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1509), [PlaneLocalization:1523](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1523).

**Role in the proof:** The Blueprint explains the unit and power calculations explicitly. The later-edge count remains the stated hypothesis of the product-image lemma until the dihedral transport argument supplies it.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Show that a different plane has its representative outside P

Take \(Q\in\mathcal P(x,a)\) with \(Q\ne P\). Its representative root satisfies
\[
b_Q\ne a,\qquad Q=\operatorname{span}\{a,b_Q\}.
\]
If \(b_Q\) belonged to \(P\), this span would be contained in \(P\).

The roots \(a,b_Q\) are independent, so their span has dimension two. The plane \(P\) also has dimension two because \(a\ne b\). Inclusion and equal dimensions would give \(Q=P\), a contradiction. Thus \(b_Q\notin P\).

### Step 2. Prove the other-plane factors are units

The [[node:kl.local.plane_prime_membership|plane-prime unit criterion]] makes \(\eta_P(\lambda(b_Q))\) a unit in \(R_P\) whenever \(Q\ne P\).

A ring homomorphism sends a unit and its inverse to mutually inverse elements. Hence its image
\(r_{P,a}(b_Q)\) is a unit in \(E_{P,a}\), and so is any nonnegative power of that image. Therefore
\[
r_{P,a}(b_Q)^{k_Q}\sim1\qquad(Q\ne P).
\]

### Step 3. Identify the factor from P itself

If \(P\) belongs to the supported set, its representative \(b_P\) lies in \(P\) and differs from \(a\). Write
\[
b_P=sa+tb.
\]
The coefficient \(t\) is nonzero, since otherwise \(b_P\) would lie on the line of \(a\), contradicting independence of distinct positive roots.

Reduction kills \(a\), so
\[
r_{P,a}(b_P)=t\,r_{P,a}(b)=tp.
\]
The nonzero real scalar \(t\) has inverse \(t^{-1}\), whose image is its inverse in the quotient ring. Thus the [[node:kl.local.localized_root_reduction|localized root-reduction theorem]] gives
\[
r_{P,a}(b_P)\sim p,\qquad
r_{P,a}(b_P)^{k_P}\sim p^{k_P}.
\]

### Step 4. Multiply the factor associations

The localization and quotient maps preserve the defining product:
\[
q_{P,a}(\eta_P(F_{x,a}))
=\prod_{Q\in\mathcal P(x,a)}r_{P,a}(b_Q)^{k_Q}.
\]
Every factor from \(Q\ne P\) is associated to \(1\) by Step 2. If \(P\) is present, its unique factor is associated to \(p^{k_P}\) by Step 3. Multiplying the witnessing units gives the required association of the full product.

### Step 5. Treat an absent plane

If \(P\notin\mathcal P(x,a)\), then \(k_P=0\). Every factor is from another plane, so Step 2 makes the full product a unit. Its target power is \(p^0=1\).

This proves the association in both support cases. It records explicitly the contribution of every factor, including the unit factors that remain after localization.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.planeRoot_outside`: [PlaneLocalization.lean:1560](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1560).

`OAI.KLInvariance.TitsSpace.reduced_planeRoot_other_isUnit`: [PlaneLocalization.lean:1569](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1569).

`OAI.KLInvariance.TitsSpace.edgeFactor_local_associated`: [PlaneLocalization.lean:1579](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1579).
