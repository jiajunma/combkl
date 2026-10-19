---
id: kl.realization.common_reflection_plane
title: An equal product of two reflections determines the same root span
kind: theorem
status: proved
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.realization.reflection_plane
- kl.notes.extended_realization
- kl.realization.root_planes
lean:
  repository: openai-kl
  modules:
  - ReflectionPlane
  declarations:
  - OAI.KLInvariance.ReflectionPlane.range_reflection_product_sub_id
  - OAI.KLInvariance.ReflectionPlane.plane_eq_of_reflection_product_eq
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionPlane:68
    format: lean-location
    note: OAI.KLInvariance.ReflectionPlane.range_reflection_product_sub_id
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionPlane:84
    format: lean-location
    note: OAI.KLInvariance.ReflectionPlane.plane_eq_of_reflection_product_eq
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

# An equal product of two reflections determines the same root span

Let \(V\) be a vector space over a field \(k\), with a nondegenerate bilinear form \(B\). Suppose
\[
B(a,a)=B(b,b)=B(c,c)=B(d,d)=2,
\]
and both pairs \(a,b\) and \(c,d\) are linearly independent. Define
\(r_a(v)=v-B(a,v)a\), and similarly for the other roots.

If \(r_ar_b=r_cr_d\), then
\[
\operatorname{span}_k\{a,b\}
=\operatorname{span}_k\{c,d\}.
\]

*Proof.*

### Step 1. Obtain independent normal functionals

Consider the two functionals \(B(a,-)\) and \(B(b,-)\). If
\[
uB(a,-)+vB(b,-)=0,
\]
then \(B(ua+vb,-)=0\). Nondegeneracy gives \(ua+vb=0\), and independence of \(a,b\) gives \(u=v=0\). Thus the normal functionals are independent.

### Step 2. Recover the span as a displacement image

The [[node:kl.realization.reflection_plane|pre-reflection image formula]] applies to these independent functionals and gives
\[
\operatorname{im}(r_ar_b-1)=\operatorname{span}\{a,b\}.
\]
The same argument gives
\(\operatorname{im}(r_cr_d-1)=\operatorname{span}\{c,d\}\).

### Step 3. Use the equality of products

Equal products have equal differences from the identity and therefore equal images. The two expressions in Step 2 give the required span equality.

### Step 4. Apply the statement to Coxeter root planes

In the Coxeter development, apply this result in the nondegenerate extended realization. The original roots embed injectively there, retain norm \(2\), and represent the same reflection operators.

Equality of two group products gives equality of their represented operators, so the embedded root spans agree. Write \(\iota:V_0\to V\) for the injective embedding.

If \(v\) lies in the first original span, then \(\iota(v)\) lies in the embedded second span. Thus \(\iota(v)=\iota(u)\) for some \(u\) in the second original span. Injectivity gives \(v=u\), proving containment in that span. Exchanging the two pairs proves the reverse containment.

For two directed reflection paths \(x\to u\to y\) and \(x\to v\to y\), their two-reflection products are both \(yx^{-1}\). Since \(x<y\), each path uses two distinct reflections. Their labels therefore lie in the same root plane.

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.ReflectionPlane.range_reflection_product_sub_id`: [ReflectionPlane.lean:68](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionPlane.lean#L68).

`OAI.KLInvariance.ReflectionPlane.plane_eq_of_reflection_product_eq`: [ReflectionPlane.lean:84](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionPlane.lean#L84).
