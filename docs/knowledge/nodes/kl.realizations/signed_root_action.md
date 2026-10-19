---
id: kl.realization.signed_root_action
title: Compatibility of the signed action with root transformation
kind: theorem
status: proved
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.realization.signed_root_representation
- kl.detail.root_reflection_correspondence
- kl.realization.simple_root_sign
- kl.coxeter.signed_reflection_action
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.IsRoot.eq_simple_of_nonpos
  - OAI.KLInvariance.TitsSpace.Represents.simple_sign
  - OAI.KLInvariance.TitsSpace.SignedRepresents.simple
  - OAI.KLInvariance.TitsSpace.SignedRepresents.act
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1847
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.IsRoot.eq_simple_of_nonpos
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1867
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.Represents.simple_sign
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1895
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.SignedRepresents.simple
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1916
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.SignedRepresents.act
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

# Compatibility of the signed action with root transformation

Suppose \((t,\varepsilon)\) represents a root \(a\) with its sign. For every \(w\in W\), the signed pair
\[
A_w(t,\varepsilon)
\]
represents \(\rho_0(w)a\) with its actual coordinate sign.

*Proof.*

### Step 1. A positive root made negative by a simple generator

Let \(a\) be positive, and suppose \(\rho_0(s_i)a\) is nonpositive. The simple-action formula changes only the \(i\)-th coordinate. Every other coordinate is simultaneously nonnegative, from \(a\), and nonpositive, from its image; hence those coordinates are zero.

Thus \(a=c\alpha_i\) with \(c\ge0\). Both \(a\) and \(\alpha_i\) have squared norm two. Therefore \(c^2=1\), and \(c=1\). We have proved \(a=\alpha_i\).

Conversely, \(s_i\alpha_i=-\alpha_i\). By uniqueness in the root–reflection correspondence, a positive root representing \(t\) becomes negative under \(s_i\) exactly when \(t=s_i\). If \(t\ne s_i\), the root-sign theorem places its image in the positive alternative.

### Step 2. Positive and negative signed inputs

For a positive input, \(\varepsilon=0\). Step 1 says that its sign changes to one exactly when \(t=s_i\), which is precisely the bit update in the signed simple action.

For a negative input, apply Step 1 to \(-a\). Linearity gives \(s_i(-a)=-s_i(a)\). Therefore a negative root becomes positive exactly when \(t=s_i\). Its bit changes from one to zero in that case, and otherwise remains one.

Conjugation also gives the correct reflection label: if \(a=\rho_0(z)\alpha_j\) represents \(t=zs_jz^{-1}\), then \(\rho_0(s_i)a=\rho_0(s_iz)\alpha_j\) represents \(s_its_i\). Thus both the reflection and sign conditions are preserved by a simple generator.

### Step 3. Induct along a word

The identity action preserves both conditions. Write \(w=s_i u\) and suppose the conclusion holds for \(u\). Apply Step 2 to its transformed signed pair and root.

The group-action laws give
\[
A_w=A_iA_u,\qquad \rho_0(w)=\rho_0(s_i)\rho_0(u).
\]
The result is exactly the pair and root in the statement. Induction on a word for \(w\) completes the proof.

## References

The local action and sign calculations are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.IsRoot.eq_simple_of_nonpos`: [Tits.lean:1847](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1847).

`OAI.KLInvariance.TitsSpace.Represents.simple_sign`: [Tits.lean:1867](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1867).

`OAI.KLInvariance.TitsSpace.SignedRepresents.simple`: [Tits.lean:1895](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1895).

`OAI.KLInvariance.TitsSpace.SignedRepresents.act`: [Tits.lean:1916](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1916).
