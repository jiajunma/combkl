---
id: kl.realization.faithful_actions
title: Faithfulness of the geometric, extended, and coordinate-dual actions
kind: theorem
status: proved
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.realization.simple_root_sign
- kl.realization.extended_action
- kl.realization.cotangent_action
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.action_injective
  - OAI.KLInvariance.TitsSpace.extendedAction_injective
  - OAI.KLInvariance.Cotangent.action_injective
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:997
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.action_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1117
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.extendedAction_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1379
    format: lean-location
    note: OAI.KLInvariance.Cotangent.action_injective
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

# Faithfulness of the geometric, extended, and coordinate-dual actions

For a Coxeter system with finitely many simple generators, the ordinary geometric action, its extended action, and the coordinate-dual action are faithful.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit root-sign proof.**

**OpenAI notes:** The realization discussion invokes the geometric representation theorem and its root-sign property from the cited Coxeter theory. [bg:realization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L34).

**Lean (primary):** The root-sign implication is proved by strong length induction. A minimal two-generator parabolic decomposition supplies a shorter prefix, and the alternating-root formula supplies nonnegative coefficients. Faithfulness follows by applying the descent sign to an element in the kernel. [Tits:941](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L941), [Tits:997](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L997).

**Role in the proof:** The entries develop the coset decomposition, coefficient formula, and induction before applying faithfulness. This gives the stated geometric facts from the local word calculations.
<!-- source-comparison:end -->

*Proof.*

### Step 1. The kernel of the ordinary action

Suppose \(\rho_0(w)=1\). If \(w\ne1\), choose a right descent \(s_i\). The simple-root sign theorem makes \(\rho_0(w)\alpha_i\) coordinatewise nonpositive.

But \(\rho_0(w)=1\) makes this vector \(\alpha_i\), whose \(i\)-th coordinate is one. This is a contradiction. Therefore \(w=1\).

A group homomorphism with trivial kernel is injective: if \(\rho_0(w)=\rho_0(z)\), then \(\rho_0(w^{-1}z)=1\), so \(w^{-1}z=1\) and \(w=z\).

### Step 2. Restriction of the extended action

Let \(\iota:V_0\to E\) be the inclusion \(v\mapsto(v,0)\). The restriction identity is
\[
\rho(w)\iota(v)=\iota(\rho_0(w)v).
\]
If \(\rho(w)=1\), injectivity of \(\iota\) gives \(\rho_0(w)v=v\) for every \(v\). Step 1 implies \(w=1\). Thus the extended action has trivial kernel and is faithful.

### Step 3. The coordinate-dual pairing

For the coordinate-dual action, the pairing identity says
\[
\rho^\vee(w)\lambda\cdot\rho_0(w)v=\lambda\cdot v.
\]
Suppose \(\rho^\vee(w)=1\). Then
\[
\lambda\cdot\rho_0(w)v=\lambda\cdot v
\]
for every \(\lambda,v\).

Choose \(\lambda\) to be each coordinate functional in turn. The displayed equality identifies every coordinate of \(\rho_0(w)v\) with that of \(v\). Hence \(\rho_0(w)=1\), and Step 1 gives \(w=1\). The coordinate-dual action is therefore faithful.

## References

The local action and sign calculations are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.action_injective`: [Tits.lean:997](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L997).

`OAI.KLInvariance.TitsSpace.extendedAction_injective`: [Tits.lean:1117](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1117).

`OAI.KLInvariance.Cotangent.action_injective`: [Tits.lean:1379](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1379).
