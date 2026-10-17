---
id: kl.realization.reflection_plane
title: The image of a product of pre-reflections
kind: theorem
status: proved
primary_topic: kl.03_realizations_and_grading
topics:
- kl.03_realizations_and_grading
uses: []
lean:
  repository: openai-kl
  modules:
  - ReflectionPlane
  declarations:
  - OAI.KLInvariance.ReflectionPlane.range_preReflection_product_sub_id
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionPlane:44
    format: lean-location
    note: OAI.KLInvariance.ReflectionPlane.range_preReflection_product_sub_id
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
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

# The image of a product of pre-reflections

Let \(V\) be a vector space over a field \(k\), let \(\alpha,\beta\in V\), and let \(f,g\in V^*\) be linearly independent. Put
\[
r_{\alpha,f}(v)=v-f(v)\alpha.
\]
Then
\[
\operatorname{im}(r_{\alpha,f}r_{\beta,g}-1)
=\operatorname{span}_k\{\alpha,\beta\}.
\]

*Proof.*

Expanding the difference from the identity gives
\[
v\longmapsto(-f(v)+f(\beta)g(v))\alpha-g(v)\beta.
\]
This proves containment in the stated span. Independence of the two forms makes \(v\mapsto(f(v),g(v))\) surjective onto \(k^2\). The displayed change of coefficients is invertible, so every linear combination of \(\alpha,\beta\) occurs, proving the reverse containment.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.ReflectionPlane.range_preReflection_product_sub_id`: [ReflectionPlane.lean:44](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionPlane.lean#L44).
