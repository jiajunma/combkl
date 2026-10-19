---
id: kl.hecke.selected_families
title: The selected R and KL polynomial interfaces
kind: definition
status: formalized
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.foundations.normalized_kl
lean:
  repository: openai-kl
  modules:
  - Bruhat
  - Model
  declarations:
  - OAI.KLInvariance.klFamilies
  - OAI.KLInvariance.klPolynomial
  - OAI.KLInvariance.rPolynomial
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Model:74
    format: lean-location
    note: OAI.KLInvariance.klFamilies
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Model:77
    format: lean-location
    note: OAI.KLInvariance.klPolynomial
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:54
    format: lean-location
    note: OAI.KLInvariance.rPolynomial
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the exact domain, degree conventions and source
    argument?
  verdict: Read klFamilies/klPolynomial in Model and rPolynomial in Bruhat, plus their
    later equality interfaces. Kept the classical selection distinct from the explicit
    recursive constructors.
tags:
- Kazhdan-Lusztig
- Hecke
---

# The selected R and KL polynomial interfaces

The source exposes the normalized polynomial pair through three names:

| Source name | Mathematical value |
|---|---|
| klFamilies | A pair selected using the predicate NormalizedKL. |
| rPolynomial | The first component of that selected pair. |
| klPolynomial | The second component of that selected pair. |

The selection uses classical choice. The [[node:kl.foundations.canonical_kl|existence-and-uniqueness theorem]] establishes that the predicate has exactly one satisfying pair and identifies the selected pair with
\[
(\mathrm{OrdinaryR.polynomial},\mathrm{CanonicalP.polynomial}).
\]
Consequently
\[
\mathrm{rPolynomial}(x,y)=R_{x,y},\qquad
\mathrm{klPolynomial}(x,y)=P_{x,y},
\]
where the right sides are the explicit bar-derived R construction and lower-half P construction.

The public names let later statements use the characterization by normalization. The identification theorem connects those names to the formulas and inductions developed in this topic.

For example, the square-parameter R normalization is stated for rPolynomial. Its proof first uses equality with OrdinaryR.polynomial and then compares the ordinary and normalized descent recurrences.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.klFamilies`: [Model.lean:74](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Model.lean#L74).

`OAI.KLInvariance.klPolynomial`: [Model.lean:77](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Model.lean#L77).

`OAI.KLInvariance.rPolynomial`: [Bruhat.lean:54](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L54).
