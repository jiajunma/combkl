---
id: kl.algebra.kernel_saturation
title: Saturated kernels and their free reduced images
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.scalar_quotient
- kl.algebra.root_label_primes
lean:
  repository: openai-kl
  modules:
  - ModuleAlgebra
  declarations:
  - OAI.KLInvariance.EdgeImage.kernel_saturated
  - OAI.KLInvariance.EdgeImage.reduced_kernel_injective
  - OAI.KLInvariance.EdgeImage.reducedInclusion
  - OAI.KLInvariance.EdgeImage.range_reducedInclusion_free
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:381
    format: lean-location
    note: OAI.KLInvariance.EdgeImage.kernel_saturated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:394
    format: lean-location
    note: OAI.KLInvariance.EdgeImage.reduced_kernel_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:413
    format: lean-location
    note: OAI.KLInvariance.EdgeImage.reducedInclusion
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:420
    format: lean-location
    note: OAI.KLInvariance.EdgeImage.range_reducedInclusion_free
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the coefficient rings, module properties and actual maps explicit?
  verdict: Read kernel_saturated, reduced_kernel_injective and range_reducedInclusion_free.
    Preserved regularity on the constraint target, proved the quotient-basis assertion
    and transferred it through the actual reduced inclusion.
tags:
- Kazhdan-Lusztig
- module-algebra
---

# Saturated kernels and their free reduced images

Let \(A\) be a commutative ring, \(f:M\to N\) an \(A\)-linear map, and \(a\in A\). Assume multiplication by \(a\) on \(N\) is injective. For \(K=\ker f\),
\[
am\in K\quad\Longleftrightarrow\quad m\in K,
\]
and the reduced inclusion
\[
K/aK\longrightarrow M/aM
\]
is injective.

If \(K\) is free over \(A\), its image under this map is free over \(C=A/(a)\).

*Proof.*

### Step 1. Cancel the scalar in the constraint target

Linearity gives \(f(am)=af(m)\). If \(am\in K\), then \(af(m)=0=a0\). Injectivity of multiplication by \(a\) on \(N\) gives \(f(m)=0\), hence \(m\in K\).

Conversely, \(m\in K\) gives \(f(am)=af(m)=0\). This is saturation of the kernel with respect to \(a\).

### Step 2. Identify the kernel after reduction

Suppose the class of \(k\in K\) maps to zero in \(M/aM\). Then \(k=am\) for some \(m\in M\).

Since \(am=k\in K\), Step 1 gives \(m\in K\). Thus \(k\in aK\), so its original class in \(K/aK\) is zero. This proves injectivity.

The map is \(C\)-linear because multiplication by \(a\) is zero in both quotient modules.

### Step 3. Reduce a free basis

Suppose \(K\) has an \(A\)-basis \((b_i)\). Its classes span \(K/aK\) over \(C\): reduce the coefficients of any finite basis expression.

For independence, lift a finite relation among the classes to coefficients \(r_i\in A\). If \(\sum_i r_ib_i\in aK\), write it as \(ak\) and expand \(k=\sum_i c_ib_i\), using a finite union of the supports. Basis uniqueness gives \(r_i=ac_i\) in every coordinate. Therefore every coefficient class in \(C\) is zero.

Thus the classes form a \(C\)-basis of \(K/aK\).

### Step 4. Transfer the basis to the actual image

The reduced inclusion is a \(C\)-linear bijection from \(K/aK\) to its image. Transport the basis from Step 3 across this bijection. The image is therefore free over \(C\).

### Step 5. Apply the target regularity condition to several constraints

If \(f\) collects several linear restriction maps, \(K\) is the submodule satisfying all the corresponding vanishing conditions. Multiplication by \(a\) is injective on the product target whenever it is injective on every component.

For edge modules free over scalar quotients by distinct root labels, the [[node:kl.algebra.root_label_primes|root-label regularity theorem]] supplies those componentwise hypotheses. The reduced kernel is then identified with its actual image in the selected edge module.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.EdgeImage.kernel_saturated`: [ModuleAlgebra.lean:381](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L381).

`OAI.KLInvariance.EdgeImage.reduced_kernel_injective`: [ModuleAlgebra.lean:394](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L394).

`OAI.KLInvariance.EdgeImage.reducedInclusion`: [ModuleAlgebra.lean:413](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L413).

`OAI.KLInvariance.EdgeImage.range_reducedInclusion_free`: [ModuleAlgebra.lean:420](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L420).
