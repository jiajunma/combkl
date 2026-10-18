---
id: kl.duality.stalk_character
title: The stalk character of the actual boundary sheaf
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.boundary_existence
- kl.sheaves.hilbert_free
- kl.detail.graded_character
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.BruhatGraph.stalkCharacter
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:206
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.stalkCharacter
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  definition: accepted
  proof: not_applicable
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

# The stalk character of the actual boundary sheaf

Let \(B(b)\) be the constructed minimal-boundary sheaf. Each stalk \(B^x\) is a finite nonnegatively graded free module. If a homogeneous basis has degrees \(d_i\), define its character by
\[
C_{x,b}(q)=\sum_i q^{d_i}.
\]
Its coefficients are nonnegative. The Hilbert formula determines this polynomial independently of the chosen homogeneous basis.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.stalkCharacter`: [SheafMorphisms.lean:206](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L206).
