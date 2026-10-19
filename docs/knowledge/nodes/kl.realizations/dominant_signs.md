---
id: kl.realization.dominant_signs
title: Dominant evaluation detects right and left ascents
kind: theorem
status: proved
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.realization.dominant_functional
- kl.realization.simple_root_sign
- kl.coxeter.word_data
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.dominant_pos_iff_ascent
  - OAI.KLInvariance.TitsSpace.dominant_dual_pos_iff_left_ascent
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1266
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.dominant_pos_iff_ascent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1294
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.dominant_dual_pos_iff_left_ascent
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are all action, sign, and length conventions retained?
  verdict: Read the finite-rank Tits proofs, the exact two-generator tail convention,
    and both group-action directions; the chosen smaller induction instance is explicit.
tags:
- Kazhdan-Lusztig
- root-geometry
---

# Dominant evaluation detects right and left ascents

For the coordinate-sum functional \(\lambda\) on the extended realization,
\[
\lambda(\rho(w)\widetilde\alpha_i)>0
\quad\Longleftrightarrow\quad
\ell(ws_i)>\ell(w).
\]
For the induced action on functionals,
\[
(w\cdot\lambda)(\widetilde\alpha_i)>0
\quad\Longleftrightarrow\quad
\ell(s_iw)>\ell(w).
\]

*Proof.*

### Step 1. Sum the coordinates in the ascent case

If \(\ell(ws_i)>\ell(w)\), the simple-root sign theorem makes every coordinate of \(\rho_0(w)\alpha_i\) nonnegative. This vector is nonzero, so some coordinate is positive.

The finite sum of its coordinates is therefore positive. By the definition of \(\lambda\) and the restriction identity, that sum equals \(\lambda(\rho(w)\widetilde\alpha_i)\).

### Step 2. The descent case excludes positivity

If \(\ell(ws_i)<\ell(w)\), all the same coordinates are nonpositive. Their sum is at most zero, so the displayed value is not positive.

These are the only two simple-length cases. Steps 1–2 prove the first equivalence.

### Step 3. Convert the inverse action to a left ascent

Apply the first equivalence to \(w^{-1}\). By definition,
\[
(w\cdot\lambda)(\widetilde\alpha_i)
=\lambda(\rho(w^{-1})\widetilde\alpha_i).
\]
Also,
\[
\ell(w^{-1})=\ell(w),\qquad
\ell(w^{-1}s_i)=\ell((w^{-1}s_i)^{-1})=\ell(s_iw).
\]
Substitution into the first equivalence proves the left-ascent statement.

## References

The local action and sign calculations are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.dominant_pos_iff_ascent`: [Tits.lean:1266](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1266).

`OAI.KLInvariance.TitsSpace.dominant_dual_pos_iff_left_ascent`: [Tits.lean:1294](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1294).
