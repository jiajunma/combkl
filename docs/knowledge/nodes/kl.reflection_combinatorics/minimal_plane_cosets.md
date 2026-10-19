---
id: kl.dihedral.minimal_plane_cosets
title: Least coset representatives preserve the signs of plane roots
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.realization.plane_reflection_membership
- kl.detail.root_inversion_count
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.planeCoset_exists_minimal
  - OAI.KLInvariance.TitsSpace.root_nonneg_of_coset_minimal
  - OAI.KLInvariance.TitsSpace.root_nonpos_coset_minimal_iff
  - OAI.KLInvariance.TitsSpace.root_inversion_coset_iff
  - OAI.KLInvariance.TitsSpace.leftInversion_coset_iff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:2166
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.planeCoset_exists_minimal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:2191
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.root_nonneg_of_coset_minimal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:2204
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.root_nonpos_coset_minimal_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:2218
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.root_inversion_coset_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:2229
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.leftInversion_coset_iff
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

# Least coset representatives preserve the signs of plane roots

Let \(P\) be a subspace of the original root space of a finite-generator Coxeter system, and let \(D_P\) be its reflection-generated subgroup.

Every coset \(D_Pa\) contains an element \(a_0\) of least ambient length. For any such \(a_0\), the inverse action \(a_0^{-1}\) preserves the positive or negative sign of every root lying in \(P\).

Consequently, for \(g\in D_P\) and a root \(r\in P\),
\[
(ga_0)^{-1}r\text{ is negative}
\quad\Longleftrightarrow\quad
g^{-1}r\text{ is negative}.
\]

*Proof.*

### Step 1. Choose a least length in the coset

The set
\[
\{\ell_W(da):d\in D_P\}\subseteq\mathbb N
\]
is nonempty, since it contains \(\ell_W(a)\). Its least element is attained by some \(a_0=d_0a\). The original element can be written
\(a=d_0^{-1}a_0\), and every \(z a_0\), \(z\in D_P\), lies in the same coset. Thus
\[
\ell_W(a_0)\le\ell_W(za_0)\qquad(z\in D_P).
\]

### Step 2. Preserve each positive plane root

Let \(r\in\Phi^+\cap P\). Its reflection \(r_r\) belongs to \(D_P\).

If \(a_0^{-1}r\) were negative, the [[node:kl.detail.root_inversion_count|ambient root-sign criterion]] would give
\[
\ell_W(r_r a_0)<\ell_W(a_0),
\]
contradicting minimality. The transformed root is nonzero and has one of the two root signs, so it is positive.

### Step 3. Preserve the negative sign as well

If \(r\in P\) is negative, then \(-r\) is a positive root in \(P\). Step 2 makes \(a_0^{-1}(-r)\) positive. By linearity its negative, \(a_0^{-1}r\), is negative.

Thus the inverse action preserves each of the two signs. In particular its image is negative exactly when the original root is negative.

### Step 4. Apply the sign statement after a subgroup element

For \(g\in D_P\), the root \(g^{-1}r\) still lies in \(P\), because the subgroup preserves the subspace. Since
\[
(ga_0)^{-1}r=a_0^{-1}(g^{-1}r),
\]
Step 3 gives the stated equivalence.

If \(r\) is positive and represents a reflection \(t\in D_P\), applying the [[node:kl.detail.root_inversion_count|ambient root-sign criterion]] to both sides also gives
\[
t\text{ lowers }ga_0
\quad\Longleftrightarrow\quad
t\text{ lowers }g.
\]
This is the orientation comparison used for coset reflection edges.

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.TitsSpace.planeCoset_exists_minimal`: [Tits.lean:2166](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L2166).

`OAI.KLInvariance.TitsSpace.root_nonneg_of_coset_minimal`: [Tits.lean:2191](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L2191).

`OAI.KLInvariance.TitsSpace.root_nonpos_coset_minimal_iff`: [Tits.lean:2204](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L2204).

`OAI.KLInvariance.TitsSpace.root_inversion_coset_iff`: [Tits.lean:2218](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L2218).

`OAI.KLInvariance.TitsSpace.leftInversion_coset_iff`: [Tits.lean:2229](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L2229).
