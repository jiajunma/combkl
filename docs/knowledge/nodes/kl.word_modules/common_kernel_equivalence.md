---
id: kl.word.common_kernel_equivalence
title: The common kernel is a twist of an old restriction kernel
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.set_kernel_data
- kl.word.head_patch_lifting
- kl.word.upper_image_properties
- kl.algebra.scalar_twist
- kl.word.set_tail_detection
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.bottCommon_lift
  - OAI.KLInvariance.TitsSpace.bottCommon_patch_lift
  - OAI.KLInvariance.TitsSpace.bottCommon_range_of_patch
  - OAI.KLInvariance.TitsSpace.bottCommon_range_forward
  - OAI.KLInvariance.TitsSpace.bottCommon_range_backward
  - OAI.KLInvariance.projective_of_same_range
  - OAI.KLInvariance.projective_of_coordinates
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1152
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCommon_lift
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1167
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCommon_patch_lift
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1182
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCommon_range_of_patch
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1212
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCommon_range_forward
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1222
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCommon_range_backward
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:992
    format: lean-location
    note: OAI.KLInvariance.projective_of_same_range
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1038
    format: lean-location
    note: OAI.KLInvariance.projective_of_coordinates
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, coordinate sets, kernel maps and induction hypotheses
    explicit?
  verdict: Read the common lift, patch lift and both coordinate-range containments.
    Constructed the isomorphism through unique matching coordinates and proved linearity
    there, without assuming a linear choice of patch lifts.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# The common kernel is a twist of an old restriction kernel

Fix a finite-generator Coxeter system with symmetric coefficient algebra \(A\), a simple reflection \(s\), and a tail word \(\mathbf t\) with compatible-tuple lifting on upper sets. Let \(U\) be upper, put \(J=U\cup sU\), \(K=U\cap sU\), and use the two-stage kernel data
\[
D=\ker(L_{s\mathbf t}(U)\to L_{s\mathbf t}(K))\cap\ker F_U,
\qquad
T=\ker(L_{\mathbf t}(J)\to L_{\mathbf t}(U)).
\]
Then the injective second-coordinate maps
\[
\gamma:D\to{}^\tau L_{\mathbf t}(sU),\qquad
{}^\tau j:{}^\tau T\to{}^\tau L_{\mathbf t}(sU)
\]
have equal images. They therefore induce an \(A\)-linear isomorphism
\(D\simeq{}^\tau T\).

*Proof.*

### Step 1. Lift an element of the common kernel

Take \(z\in D\). Choose \(m\in M_{s\mathbf t}\) with \(p_U'(m)=z\). The two defining conditions of \(D\), together with the restriction and first-map formulas, give
\[
p_K'(m)=0,\qquad p_U(\mu(m))=0.
\]

### Step 2. Patch its second component to a tail vector

The zero-overlap version of [[node:kl.word.head_patch_lifting|patched-tail lifting]] applies to \(m\). It supplies \(n\in M_{\mathbf t}\) matching \(\mu(m)\) on \(U\) and matching the underlying \(\nu(m)\) on \(sU\).

Since \(p_U(\mu(m))=0\), the matching values on \(U\) give \(p_U(n)=0\). The old vector
\(d=p_J(n)\) lies in \(T\), and its restriction to \(sU\) is \(p_{sU}(\nu(m))\). Thus
\[
\gamma(z)={}^\tau j(d),
\]
where \(d\) is now regarded as an element of \({}^\tau T\). This proves one image inclusion.

### Step 3. Insert a lift from the old kernel

Conversely, take \(d\in{}^\tau T\). Choose \(n\in M_{\mathbf t}\) whose projection on \(J\) is the underlying image vector \(d\). Since \(d\) restricts to zero on \(U\), we have \(p_U(n)=0\).

Set
\[
z=p_U'(1\otimes n).
\]
Its first image is \(p_U(n)=0\). The [[node:kl.word.set_tail_detection|seed-vanishing theorem]] gives
\(p_K'(1\otimes n)=0\), so \(z\in D\). Its second image is the twisted \(p_{sU}(n)\), which is exactly \({}^\tau j(d)\).

This proves the reverse image inclusion.

### Step 4. Use injectivity to obtain the linear isomorphism

For each \(z\in D\), Steps 1–2 give an element \(d\) with
\(\gamma(z)={}^\tau j(d)\). Injectivity of \({}^\tau j\) makes that \(d\) unique. Define \(\Phi(z)=d\).

Linearity follows by applying \({}^\tau j\): the image of
\(\Phi(z+z')\) equals \(\gamma(z+z')=\gamma(z)+\gamma(z')\), so injectivity gives
\(\Phi(z+z')=\Phi(z)+\Phi(z')\). The same argument proves scalar linearity.

Step 3 and injectivity of \(\gamma\) give the inverse map. Thus \(\Phi\) is the required linear isomorphism. In particular, projectivity of \(T\) implies projectivity of \(D\), because twisting preserves projectivity.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottCommon_lift`: [IntegralPairings.lean:1152](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1152).

`OAI.KLInvariance.TitsSpace.bottCommon_patch_lift`: [IntegralPairings.lean:1167](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1167).

`OAI.KLInvariance.TitsSpace.bottCommon_range_of_patch`: [IntegralPairings.lean:1182](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1182).

`OAI.KLInvariance.TitsSpace.bottCommon_range_forward`: [IntegralPairings.lean:1212](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1212).

`OAI.KLInvariance.TitsSpace.bottCommon_range_backward`: [IntegralPairings.lean:1222](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1222).

`OAI.KLInvariance.projective_of_same_range`: [IntegralPairings.lean:992](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L992).

`OAI.KLInvariance.projective_of_coordinates`: [IntegralPairings.lean:1038](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1038).
