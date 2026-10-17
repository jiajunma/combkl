---
id: "kl.foundations.canonical_kl"
title: "Existence and uniqueness of the canonical KL families"
kind: "theorem"
status: "proved"
primary_topic: "kl.01_introduction"
topics: ["kl.01_introduction"]
uses: ["kl.foundations.normalized_kl","kl.foundations.low_half"]
lean: {"repository":"openai-kl","modules":["CanonicalKL","Model"],"declarations":["OAI.KLInvariance.normalizedKL_existsUnique","OAI.KLInvariance.klFamilies_spec","OAI.KLInvariance.klPolynomial_eq_constructed"]}
source: {"spans":[{"artifact":"openai-kl-source","locator":"OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:273","format":"lean-location","note":"OAI.KLInvariance.normalizedKL_existsUnique"},{"artifact":"openai-kl-source","locator":"OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:279","format":"lean-location","note":"OAI.KLInvariance.klFamilies_spec"},{"artifact":"openai-kl-source","locator":"OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:286","format":"lean-location","note":"OAI.KLInvariance.klPolynomial_eq_constructed"},{"artifact":"openai-kl-paper","locator":"1. Introduction and conventions; sec:introduction","format":"section","note":"Chapter organization follows the paper; Lean references identify the precise formal statements."}]}
verification: {"statement":"accepted","proof":"accepted","alignment":"aligned"}
generality: {"reviewed":true,"prompt":"Does the exposition preserve the mathematical scope of its Lean declarations?","verdict":"The stated hypotheses and conclusion follow the fixed source; explanatory derivations retain the original proof route."}
tags: ["Kazhdan-Lusztig","introduction"]
---

# Existence and uniqueness of the canonical KL families

For every Coxeter system, exactly one pair of polynomial families satisfies [[node:kl.foundations.normalized_kl]]. The polynomials selected by those conditions agree with the explicit lower-half construction.

*Proof.*

Construct ordinary \(R\)-polynomials from the Hecke action and establish their recursion. Then recurse on interval rank difference, using the strict lower-half operation to construct \(P\). Prove the diagonal and vanishing conditions, the strict degree bound, and reciprocity. This produces a pair satisfying every normalization condition.

For uniqueness, the simple-reflection recursion first determines \(R\). With \(R\) fixed, induction on smaller intervals and reciprocal low-degree uniqueness determine \(P\). The selected family must therefore equal this explicitly constructed family.

## References

[1. Introduction and conventions](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization

`OAI.KLInvariance.normalizedKL_existsUnique`: [CanonicalKL.lean:273](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L273).

`OAI.KLInvariance.klFamilies_spec`: [CanonicalKL.lean:279](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L279).

`OAI.KLInvariance.klPolynomial_eq_constructed`: [CanonicalKL.lean:286](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L286).
