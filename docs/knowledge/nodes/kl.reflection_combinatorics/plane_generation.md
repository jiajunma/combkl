---
id: kl.dihedral.plane_generation
title: The angular endpoint reflections generate the plane subgroup
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.detail.plane_basis
- kl.dihedral.angular_extremes_simple
- kl.dihedral.plane_simple_steps
- kl.order.slope_cone
- kl.realization.positive_root_action
- kl.realization.plane_reflection_membership
lean:
  repository: openai-kl
  modules:
  - Decomposition
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.positive_cone
  - OAI.KLInvariance.TitsSpace.PlaneBasis.reflection_inverts_endpoint
  - OAI.KLInvariance.TitsSpace.PlaneSimple.inverted_after_mul
  - OAI.KLInvariance.TitsSpace.PlaneSimple.planeLength_conj_drop
  - OAI.KLInvariance.TitsSpace.PlaneBasis.rootRef_mem_pairClosure
  - OAI.KLInvariance.TitsSpace.PlaneBasis.pairClosure_eq_planeSubgroup
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:653
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.positive_cone
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:784
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.reflection_inverts_endpoint
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:796
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneSimple.inverted_after_mul
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:807
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneSimple.planeLength_conj_drop
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:833
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.rootRef_mem_pairClosure
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:869
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.pairClosure_eq_planeSubgroup
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
- background
---

# The angular endpoint reflections generate the plane subgroup

Let \((a,b)\) be a plane basis of a root plane \(P\) in a finite-generator Coxeter system. Then
\[
D_P=\langle r_a,r_b\rangle.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same plane subgroup, different construction.**

**OpenAI notes:** The plane lemma invokes the reflection-subgroup theorem to obtain a canonical Coxeter system, then uses positivity in the plane to show that its rank is two. [dih:plane](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L20).

**Lean (primary):** Finite ambient inversion sets produce angular endpoints. Their plane-simple sign criterion and the plane inversion count prove generation by two endpoint reflections through a count-decreasing conjugation. A two-involution presentation constructs the Coxeter system; the induced signed relation then identifies its inversions. [Decomposition:627](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L627), [Decomposition:869](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L869), [Decomposition:906](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L906), [Decomposition:1010](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1010).

**Role in the proof:** The Blueprint follows the endpoint-existence, generation, presentation, and signed-inversion proofs in that order.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Detect an inverted endpoint

Take a positive root \(r\in P\), and put \(t=r_r\). The plane-basis cone property writes
\[
r=ca+db,\qquad c,d\ge0.
\]
If \(t(a)\) and \(t(b)\) were both positive, their nonnegative combination \(t(r)\) would be nonnegative. But \(t(r)=-r\) is negative and nonzero.

Thus \(t\) inverts at least one endpoint. Both endpoints are plane-simple by the [[node:kl.dihedral.angular_extremes_simple|angular-extreme theorem]].

### Step 2. Establish a second descent for a nonsimple reflection

Let \(u\) be an endpoint inverted by \(t\), and suppose \(r\ne u\). Write \(s=r_u\), and let
\[
v=-t(u).
\]
The root \(v\) is positive and belongs to \(P\).

If \(v=u\), the reflection equation \(t(u)=-u\) gives
\[
2u=B(r,u)r.
\]
The scalar on the right is positive by heights. Comparing the root norms makes \(r=u\), a contradiction. Thus \(v\ne u\).

Plane simplicity of \(u\) makes \(s(v)\) positive. Therefore
\[
(ts)^{-1}u=st(u)=-s(v)
\]
is negative: \(ts\) also inverts \(u\).

### Step 3. Compute the drop under conjugation

Since \(t\) inverts \(u\), the [[node:kl.dihedral.plane_simple_steps|simple-step theorem]] gives
\[
L_P(st)=L_P(t)-1.
\]
Both \(s,t\) belong to \(D_P\), and \((st)^{-1}=ts\), so inverse symmetry gives
\(L_P(ts)=L_P(st)\).

Step 2 and another downward simple step give
\[
L_P(sts)=L_P(ts)-1=L_P(t)-2.
\]
The conjugate reflection is \(sts=r_{s\star r}\). The positive root \(s\star r\) still lies in \(P\).

### Step 4. Induct on the finite plane inversion count

Let \(H=\langle r_a,r_b\rangle\). We prove \(r_r\in H\) for every positive \(r\in P\), by strong induction on the nonnegative integer \(L_P(r_r)\).

The value cannot be zero: \(r_r\) inverts \(r\in P\). If \(r=a\) or \(r=b\), the reflection is a generator of \(H\).

Otherwise choose the inverted endpoint \(u\) from Step 1. Step 3 gives a reflection \(t'=r_{r'}\), with \(r'=r_u\star r\in P\), whose nonnegative count is \(L_P(r_r)-2<L_P(r_r)\). The induction hypothesis gives \(t'\in H\).

Since \(r_u\in H\) and \(r_r=r_ut'r_u\), the original reflection belongs to \(H\). This completes the induction.

### Step 5. Compare the generated subgroups

Every root in \(P\) is a positive root or the negative of one, and these two signs define the same reflection. Step 4 therefore places every generator of \(D_P\) in \(H\), proving \(D_P\subseteq H\).

Conversely, \(a,b\in P\), so their reflections belong to \(D_P\). Thus \(H\subseteq D_P\), and the groups are equal.

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.positive_cone`: [Decomposition.lean:653](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L653).

`OAI.KLInvariance.TitsSpace.PlaneBasis.reflection_inverts_endpoint`: [Decomposition.lean:784](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L784).

`OAI.KLInvariance.TitsSpace.PlaneSimple.inverted_after_mul`: [Decomposition.lean:796](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L796).

`OAI.KLInvariance.TitsSpace.PlaneSimple.planeLength_conj_drop`: [Decomposition.lean:807](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L807).

`OAI.KLInvariance.TitsSpace.PlaneBasis.rootRef_mem_pairClosure`: [Decomposition.lean:833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L833).

`OAI.KLInvariance.TitsSpace.PlaneBasis.pairClosure_eq_planeSubgroup`: [Decomposition.lean:869](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L869).
