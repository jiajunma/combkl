---
id: kl.algebra.kernel_saturation
title: Regular scalars make kernels saturated
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.scalar_quotient
lean:
  repository: openai-kl
  modules:
  - ModuleAlgebra
  declarations:
  - OAI.KLInvariance.EdgeImage.kernel_saturated
  - OAI.KLInvariance.EdgeImage.reduced_kernel_injective
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
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source assumptions and maps?
  verdict: Read the local definitions and supporting proof bodies; stated the scalar
    direction, degree convention, and finite-generation hypotheses explicitly.
tags:
- Kazhdan-Lusztig
- graded-algebra
---

# Regular scalars make kernels saturated

Let \(A\) be a commutative ring, \(f:M\to N\) an \(A\)-linear map, and \(a\in A\). Assume multiplication by \(a\) on \(N\) is injective. Put \(K=\ker f\). Then
\[
am\in K\quad\Longleftrightarrow\quad m\in K,
\]
and the induced map
\[
K/aK\longrightarrow M/aM
\]
is injective.

*Proof.*

### Step 1. Move the scalar through the map

By linearity, \(f(am)=af(m)\). If \(am\in K\), then \(af(m)=0=a0\). Injectivity of multiplication by \(a\) on \(N\) gives \(f(m)=0\), so \(m\in K\).

Conversely, if \(m\in K\), linearity gives \(f(am)=a0=0\). Thus \(K\) is saturated with respect to \(a\).

### Step 2. Calculate the reduced kernel

Let the class of \(k\in K\) map to zero in \(M/aM\). There is \(m\in M\) with \(k=am\). Since \(am=k\in K\), Step 1 gives \(m\in K\). Hence \(k\in aK\), and its class in \(K/aK\) was already zero. This proves injectivity.

### Step 3. Interpret the simultaneous constraints

If \(f\) collects several outgoing restriction maps, its kernel consists of the stalk vectors satisfying all the chosen vanishing conditions. To apply the theorem, multiplication by the selected edge root must be injective on the product of the other edge targets. Componentwise injectivity proves that product injectivity.

Reducing \(K\) modulo the selected root therefore introduces exactly the scalar multiples already present in \(K\). This is the inclusion used to identify the upper edge image with a scalar quotient of the upper kernel.

## References

The local source declarations below define the constructions and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.EdgeImage.kernel_saturated`: [ModuleAlgebra.lean:381](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L381).

`OAI.KLInvariance.EdgeImage.reduced_kernel_injective`: [ModuleAlgebra.lean:394](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L394).
