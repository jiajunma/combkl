---
id: kl.detail.hecke_quadratic_identity
title: Quadratic identities and inverses of simple Hecke operators
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.definitions.hecke_operators
- kl.definitions.hecke_quadratic_relation
lean:
  repository: openai-kl
  modules:
  - Hecke
  declarations:
  - OAI.KLInvariance.Hecke.left_quadratic
  - OAI.KLInvariance.Hecke.leftInv
  - OAI.KLInvariance.Hecke.left_mul_leftInv
  - OAI.KLInvariance.Hecke.leftInv_mul_left
  - OAI.KLInvariance.HeckeQ.left_quadratic
  - OAI.KLInvariance.HeckeQ.leftInv
  - OAI.KLInvariance.HeckeQ.left_mul_leftInv
  - OAI.KLInvariance.HeckeQ.leftInv_mul_left
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:83
    format: lean-location
    note: OAI.KLInvariance.Hecke.left_quadratic
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:99
    format: lean-location
    note: OAI.KLInvariance.Hecke.leftInv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:102
    format: lean-location
    note: OAI.KLInvariance.Hecke.left_mul_leftInv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:115
    format: lean-location
    note: OAI.KLInvariance.Hecke.leftInv_mul_left
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:569
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.left_quadratic
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:583
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.leftInv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:589
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.left_mul_leftInv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:602
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.leftInv_mul_left
  - artifact: openai-kl-paper
    locator: Related paper context; sec:introduction
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual coefficient hypotheses, conventions and source proof retained?
  verdict: Read both quadratic proofs and both-sided inverse declarations; the ascent-pair
    calculation covers every basis vector and retains the unit hypothesis only in
    the q convention.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Quadratic identities and inverses of simple Hecke operators

Over a commutative ring, normalized operators satisfy
\[
L_s(a)^2=I+aL_s(a),\qquad L_s(a)^{-1}=L_s(a)-aI.
\]
Unnormalized operators satisfy
\[
L_s(q)^2=qI+(q-1)L_s(q).
\]
When \(q\) is a unit, their inverse is
\[
L_s(q)^{-1}=q^{-1}\bigl(L_s(q)-(q-1)I\bigr).
\]

*Proof.*

### Step 1. Reduce to an ascent pair

Since \(s^2=1\) and simple multiplication changes length by one, the basis is partitioned into pairs \(e_w,e_{sw}\), where the shorter member is chosen as \(w\). Each such two-dimensional span is preserved by \(L_s\).

For normalized operators, \(L_sH_w=H_{sw}\) and \(L_sH_{sw}=H_w+aH_{sw}\). Therefore
\[
L_s^2H_w=H_w+aL_sH_w,
\]
\[
L_s^2H_{sw}
=L_s(H_w+aH_{sw})
=H_{sw}+aL_sH_{sw}.
\]
These equations prove the normalized identity on every basis vector.

### Step 2. Compute both unnormalized columns

The unnormalized pair satisfies
\[
L_sT_w=T_{sw},\qquad L_sT_{sw}=qT_w+(q-1)T_{sw}.
\]
Hence
\[
L_s^2T_w=qT_w+(q-1)L_sT_w,
\]
\[
L_s^2T_{sw}
=L_s\bigl(qT_w+(q-1)T_{sw}\bigr)
=qT_{sw}+(q-1)L_sT_{sw}.
\]
Linearity proves the unnormalized operator identity.

### Step 3. Verify each inverse on both sides

In the normalized case,
\[
L_s(L_s-aI)=L_s^2-aL_s=I.
\]
The scalar map \(aI\) commutes with every \(C\)-linear operator, so the reversed product has the same value.

For a unit \(q\),
\[
L_s\,q^{-1}(L_s-(q-1)I)
=q^{-1}\bigl(L_s^2-(q-1)L_s\bigr)
=q^{-1}qI=I.
\]
The same commutation with scalar maps proves the reversed product is \(I\).

Thus these formulas define actual invertible operators. The source packages each operator and its inverse as a unit of the endomorphism ring.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Hecke.left_quadratic`: [Hecke.lean:83](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L83).

`OAI.KLInvariance.Hecke.leftInv`: [Hecke.lean:99](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L99).

`OAI.KLInvariance.Hecke.left_mul_leftInv`: [Hecke.lean:102](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L102).

`OAI.KLInvariance.Hecke.leftInv_mul_left`: [Hecke.lean:115](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L115).

`OAI.KLInvariance.HeckeQ.left_quadratic`: [Hecke.lean:569](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L569).

`OAI.KLInvariance.HeckeQ.leftInv`: [Hecke.lean:583](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L583).

`OAI.KLInvariance.HeckeQ.left_mul_leftInv`: [Hecke.lean:589](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L589).

`OAI.KLInvariance.HeckeQ.leftInv_mul_left`: [Hecke.lean:602](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L602).
