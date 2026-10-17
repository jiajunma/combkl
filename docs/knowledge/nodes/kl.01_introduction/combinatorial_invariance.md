---
id: "kl.main.combinatorial_invariance"
title: "Combinatorial invariance of Kazhdan–Lusztig polynomials"
kind: "theorem"
status: "proved"
primary_topic: "kl.01_introduction"
topics: ["kl.01_introduction"]
uses: ["kl.main.kl_finite","kl.main.finite_model_transport"]
lean: {"repository":"openai-kl","modules":["Invariance"],"declarations":["OAI.KLInvariance.combinatorial_invariance"]}
source: {"spans":[{"artifact":"openai-kl-source","locator":"OAI.RepresentationTheory.KazhdanLusztig.Invariance:547","format":"lean-location","note":"OAI.KLInvariance.combinatorial_invariance"},{"artifact":"openai-kl-paper","locator":"1. Introduction and conventions; sec:introduction","format":"section","note":"Chapter organization follows the paper; Lean references identify the precise formal statements."}]}
verification: {"statement":"accepted","proof":"accepted","alignment":"aligned"}
generality: {"reviewed":true,"prompt":"Does the exposition preserve the mathematical scope of its Lean declarations?","verdict":"The stated hypotheses and conclusion follow the fixed source; explanatory derivations retain the original proof route."}
tags: ["Kazhdan-Lusztig","introduction"]
---

# Combinatorial invariance of Kazhdan–Lusztig polynomials

Let \((W,S)\) and \((W',S')\) be arbitrary Coxeter systems, with \(u\le b\) and \(u'\le b'\). If
\[
\phi:[u,b]\simeq[u',b']
\]
is an isomorphism of abstract partially ordered sets, then the ordinary equal-parameter Kazhdan–Lusztig polynomials satisfy
\[
P^W_{u,b}(q)=P^{W'}_{u',b'}(q).
\]

*Proof.*

Choose a finite-support model for each interval. Compose their interval isomorphisms with \(\phi\), obtaining an interval isomorphism between finite-generator Coxeter systems.

Choose bases for their extended real realizations and apply [[node:kl.main.kl_finite]] to identify the model polynomials. [[node:kl.main.finite_model_transport]] transports the equality back to the original systems.

The finite sets of generators, realizations, and bases are chosen inside the proof. The theorem's inputs are only the two Coxeter systems, comparable endpoints, and the unlabelled order isomorphism.

## References

[1. Introduction and conventions](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization

`OAI.KLInvariance.combinatorial_invariance`: [Invariance.lean:547](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L547).
