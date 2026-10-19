---
id: kl.main.finite_model_transport
title: Existence and transport of finite-support interval models
kind: theorem
status: proved
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.main.finite_interval_model
- kl.foundations.finite_support
- kl.foundations.canonical_kl
- kl.foundations.subword
- kl.realization.cotangent_action
- kl.realization.faithful_actions
- kl.coxeter.parabolic_subgroups
lean:
  repository: openai-kl
  modules:
  - Invariance
  - Tits
  declarations:
  - OAI.KLInvariance.exists_finiteIntervalModel
  - OAI.KLInvariance.FiniteIntervalModel.orderIso
  - OAI.KLInvariance.FiniteIntervalModel.kl_eq
  - OAI.KLInvariance.StandardParabolic.inclusion_injective
  - OAI.KLInvariance.StandardParabolic.length_inclusion
  - OAI.KLInvariance.StandardParabolic.bruhat_inclusion_iff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Invariance:484
    format: lean-location
    note: OAI.KLInvariance.exists_finiteIntervalModel
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Invariance:505
    format: lean-location
    note: OAI.KLInvariance.FiniteIntervalModel.orderIso
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Invariance:517
    format: lean-location
    note: OAI.KLInvariance.FiniteIntervalModel.kl_eq
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1446
    format: lean-location
    note: OAI.KLInvariance.StandardParabolic.inclusion_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1488
    format: lean-location
    note: OAI.KLInvariance.StandardParabolic.length_inclusion
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1519
    format: lean-location
    note: OAI.KLInvariance.StandardParabolic.bruhat_inclusion_iff
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

# Existence and transport of finite-support interval models

For \(u\le b\), a [[node:kl.main.finite_interval_model]] exists. Its standard inclusion induces
\[
[\bar u,\bar b]\simeq[u,b],
\qquad
P_{\bar u,\bar b}=P_{u,b},
\]
and preserves the rank difference.

*Proof.*

### Step 1. Choose one finite generator set for the entire lower ideal

By [[node:kl.foundations.finite_support]], there is a finite subset \(J\) of the simple generators such that every \(x\le b\) has an expression using only generators in \(J\). In particular this holds for \(u\) and \(b\).

Let \(W_J\) be the standard parabolic Coxeter system on \(J\), and let \(j:W_J\to W\) be its inclusion. Relabel the two chosen expressions as words in \(J\), and let their products in \(W_J\) be \(\bar u,\bar b\). Preservation of word products gives
\(j(\bar u)=u\) and \(j(\bar b)=b\). These are exactly the endpoint equations required by the finite interval model.

### Step 2. Obtain the interval isomorphism

Here are the facts about standard parabolic inclusion used in this step.

First, it is injective. Lean proves this using the cotangent action: restriction of coordinate functions from the full generator set to \(J\) intertwines the two actions. This restriction is surjective, since a function on \(J\) extends by zero. If \(j(w)=1\), the intertwining equality makes \(w\) act trivially on every restricted function. Faithfulness of the finite-\(J\) cotangent representation gives \(w=1\).

Second, it preserves length. A reduced word in \(W_J\) becomes an ambient expression of the same length, so \(\ell_W(j(w))\le\ell_{W_J}(w)\). Conversely, reduce an expression for \(j(w)\) whose letters lie in \(J\) by taking a reduced subword; this introduces no new letters. Lift the resulting word back to \(J\). Injectivity identifies its product with \(w\), so \(\ell_{W_J}(w)\) is at most its length, which is \(\ell_W(j(w))\). The lengths are equal, and a \(J\)-word is reduced precisely when its ambient word is reduced.

Third, it preserves and reflects Bruhat order. Choose a fixed reduced \(J\)-word for the upper element. Its ambient image is reduced by length preservation. The fixed-word subword criterion identifies a lower comparison on either side with retaining positions in this same word; injectivity identifies the resulting lower products. Thus the two order predicates agree.

In particular, \(\bar u\le\bar b\), since \(u\le b\). It defines an order-preserving map
\[
j:[\bar u,\bar b]_{W_J}\longrightarrow[u,b]_W.
\]
Injectivity follows from injectivity of the parabolic inclusion.

For surjectivity, an element \(x\le b=j(\bar b)\) has a reduced subword expression inside a reduced expression of \(\bar b\). Hence \(x=j(\bar x)\) for some \(\bar x\le\bar b\). Since \(u\le x\), order reflection gives \(\bar u\le\bar x\). Therefore every element of \([u,b]\) occurs. Restricting the inverse gives the order isomorphism.

### Step 3. Polynomial transport through parabolic inclusion

The parabolic polynomial identity is proved from the defining recursions, not from combinatorial invariance. Parabolic inclusion preserves length and simple multiplication by generators in \(J\). Therefore the R-recursion in the parabolic and the ambient system has identical descent cases and identical lower terms. Induction on the upper endpoint's length identifies the R-families.

The interval isomorphism in Step 2 identifies the finite convolution sums and rank differences. The canonical lower-half recursion then identifies the P-families, or equivalently their normalization and uniqueness do. Consequently
\[
P^{W_J}_{\bar u,\bar b}=P^W_{u,b}.
\]
Length preservation also gives \(d(\bar u,\bar b)=d(u,b)\).

### Step 4. Assemble the model data

The finite set \(J\), the two lifted endpoints, and their endpoint equations define the model. Steps 2–3 establish its order-isomorphism and polynomial-transport properties. Thus the later reduction to finite generators does not presuppose the unrestricted invariance theorem.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.exists_finiteIntervalModel`: [Invariance.lean:484](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L484).

`OAI.KLInvariance.FiniteIntervalModel.orderIso`: [Invariance.lean:505](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L505).

`OAI.KLInvariance.FiniteIntervalModel.kl_eq`: [Invariance.lean:517](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L517).

`OAI.KLInvariance.StandardParabolic.inclusion_injective`: [Tits.lean:1446](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1446).

`OAI.KLInvariance.StandardParabolic.length_inclusion`: [Tits.lean:1488](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1488).

`OAI.KLInvariance.StandardParabolic.bruhat_inclusion_iff`: [Tits.lean:1519](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1519).
