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

### Step 1. Expand the composite in the stated order

Write \(r_{\alpha,f}(v)=v-f(v)\alpha\) and \(r_{\beta,g}(v)=v-g(v)\beta\). First apply the second map:
\[
r_{\alpha,f}(r_{\beta,g}(v))
=v-g(v)\beta-f(v-g(v)\beta)\alpha.
\]
Linearity of \(f\) gives
\[
(r_{\alpha,f}r_{\beta,g}-1)(v)
=(-f(v)+f(\beta)g(v))\alpha-g(v)\beta.
\]
Thus every image vector lies in \(\operatorname{span}\{\alpha,\beta\}\).

### Step 2. Explain why the pair of functionals is surjective

Consider \(F:V\to k^2\), \(F(v)=(f(v),g(v))\). If its image were a proper subspace of the two-dimensional space \(k^2\), some nonzero linear functional on \(k^2\), say \((a,b)\mapsto ca+db\), would vanish on that image.

Then \(cf+dg=0\), with \((c,d)\ne(0,0)\), contradicting the assumed independence of \(f,g\). Hence \(F\) is surjective.

### Step 3. Produce a preimage for an arbitrary vector in the plane

Take \(a\alpha+b\beta\). By Step 2 choose \(v\) satisfying
\[
g(v)=-b,\qquad f(v)=-a-bf(\beta).
\]
Substitution into the expression in Step 1 gives coefficient
\(-f(v)+f(\beta)g(v)=a\) at \(\alpha\), and coefficient \(-g(v)=b\) at \(\beta\). Therefore the chosen plane vector lies in the image.

The two containments prove equality. Independence of \(\alpha,\beta\) is not needed for this abstract formula; independence of the functionals is the hypothesis that supplies the chosen values in Step 3.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.ReflectionPlane.range_preReflection_product_sub_id`: [ReflectionPlane.lean:44](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionPlane.lean#L44).
