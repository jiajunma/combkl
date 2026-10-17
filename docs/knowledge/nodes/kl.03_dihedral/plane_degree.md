---
id: "kl.paths.plane_degree"
title: "The sum of root-plane weights and the edge-factor degree"
kind: "theorem"
status: "proved"
primary_topic: "kl.03_dihedral"
topics: ["kl.03_dihedral"]
uses: ["kl.realization.reflection_plane","kl.foundations.bruhat_step"]
lean: {"repository":"openai-kl","modules":["ReflectionSchedules"],"declarations":["OAI.KLInvariance.TitsSpace.sum_planeWeight","OAI.KLInvariance.TitsSpace.edgeFactor_degree_formula"]}
source: {"spans":[{"artifact":"openai-kl-source","locator":"OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:621","format":"lean-location","note":"OAI.KLInvariance.TitsSpace.sum_planeWeight"},{"artifact":"openai-kl-source","locator":"OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:993","format":"lean-location","note":"OAI.KLInvariance.TitsSpace.edgeFactor_degree_formula"},{"artifact":"openai-kl-paper","locator":"3. Dihedral intervals and transported reflection orders; sec:dihedral","format":"section","note":"Chapter organization follows the paper; Lean references identify the precise formal statements."}]}
verification: {"statement":"accepted","proof":"accepted","alignment":"aligned"}
generality: {"reviewed":true,"prompt":"Does the exposition preserve the mathematical scope of its Lean declarations?","verdict":"The stated hypotheses and conclusion follow the fixed source; explanatory derivations retain the original proof route."}
tags: ["Kazhdan-Lusztig","dihedral"]
---

# The sum of root-plane weights and the edge-factor degree

For an upward reflection edge \(x\to r_\alpha x\), group the change in inversion roots by planes containing \(\alpha\). The resulting nonnegative integral weights \(k_\Pi\) have finite support and satisfy
\[
2\sum_\Pi k_\Pi=\ell(r_\alpha x)-\ell(x)-1.
\]
The edge factor \(f_e\), formed from the corresponding reduced root factors, therefore has degree
\[
\deg f_e=\frac{\ell(r_\alpha x)-\ell(x)-1}{2}.
\]

*Proof.*

First compute the sum of the inversion defects grouped by planes. Each plane defect is twice its nonnegative weight. Summing over the finite support proves the first identity. The edge factor is the product with those weights as exponents, so its homogeneous degree is their sum.

## References

[3. Dihedral intervals and transported reflection orders](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L2).

## Lean formalization

`OAI.KLInvariance.TitsSpace.sum_planeWeight`: [ReflectionSchedules.lean:621](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L621).

`OAI.KLInvariance.TitsSpace.edgeFactor_degree_formula`: [ReflectionSchedules.lean:993](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L993).
