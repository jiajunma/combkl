---
id: kl.word.kernel_exactness
title: Exact reflection kernels for a tensor word
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.notes.word_stalks
- kl.word.edge_annihilation
- kl.algebra.pair_projection
- kl.detail.root_reflection_correspondence
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  declarations:
  - OAI.KLInvariance.TitsSpace.BottKernelExact
  - OAI.KLInvariance.TitsSpace.BottKernelExact.upper_kernel
  - OAI.KLInvariance.TitsSpace.BottKernelExact.kernel_iff
  - OAI.KLInvariance.TitsSpace.BottKernelExact.kernel_iff_of_mul
  - OAI.KLInvariance.TitsSpace.BottKernelExact.projection_of_mul
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:964
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BottKernelExact
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1012
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BottKernelExact.upper_kernel
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1020
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BottKernelExact.kernel_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1028
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BottKernelExact.kernel_iff_of_mul
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1036
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BottKernelExact.projection_of_mul
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read BottKernelExact and its four endpoint/kernel consequences. Preserved
    the universal root quantifier, strict upward length hypothesis and divisibility
    in the image stalk; explained the reverse inclusion using the separate annihilation
    theorem.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Exact reflection kernels for a tensor word

Fix a finite-generator Coxeter system and its symmetric coefficient algebra \(A\). A word \(\mathbf t\) satisfies exact reflection kernels if the following condition holds for every group element \(x\), every reflection \(t\), and every root \(a\) representing \(t\).

Put \(\beta=\iota(\operatorname{embed}(a))\). Whenever
\[
\ell(x)<\ell(tx),
\]
every vector \(m\in M_{\mathbf t}\) with \(\pi_x(m)=0\) has
\[
\pi_{tx}(m)=\beta z
\quad\text{for some }z\in M_{\mathbf t}^{tx}.
\]
This is the source's proposition `BottKernelExact`. The length inequality orients the reflection edge upward. The divisibility takes place in the actual image stalk \(M_{\mathbf t}^{tx}\).

## Equivalent kernel formulations

For an upward edge, let \(f=\pi_x\), \(g=\pi_{tx}\), and \(u:M_{\mathbf t}^{tx}\to Q\) be the upper map to their pair-projection quotient. The condition gives
\[
g(\ker f)\subseteq\beta M_{\mathbf t}^{tx}.
\]
Reflection-label annihilation supplies the reverse inclusion: \(u(\beta z)=0\), and the pair-projection criterion lifts \((0,\beta z)\). Therefore exact reflection kernels give
\[
g(\ker f)=\ker u=\beta M_{\mathbf t}^{tx}.
\]
Equivalently,
\[
\bigl(\exists m,\ f(m)=0,\ g(m)=y\bigr)
\quad\Longleftrightarrow\quad
\bigl(\exists z,\ y=\beta z\bigr).
\]
These are the source's upper_kernel and kernel_iff consequences.

## Reindexing an edge

If the upper endpoint is written as \(y\) with \(tx=y\), the same condition reads
\[
\ell(x)<\ell(y),\quad \pi_x(m)=0
\quad\Longrightarrow\quad
\pi_y(m)=\beta z.
\]
The source's kernel_iff_of_mul and projection_of_mul provide this substitution explicitly. They let the word induction compare the original edge with its conjugated edge after prepending a simple reflection.

The [[node:kl.detail.word_standard_stalks|free-word-stalk theorem]] proves this property for every word together with stalk freeness. In that simultaneous induction, the first-reflection case uses the reflection flip; the other reflections use the tail's exact kernels and saturation of the head pair lattice.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.BottKernelExact`: [BottSamelson.lean:964](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L964).

`OAI.KLInvariance.TitsSpace.BottKernelExact.upper_kernel`: [BottSamelson.lean:1012](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1012).

`OAI.KLInvariance.TitsSpace.BottKernelExact.kernel_iff`: [BottSamelson.lean:1020](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1020).

`OAI.KLInvariance.TitsSpace.BottKernelExact.kernel_iff_of_mul`: [BottSamelson.lean:1028](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1028).

`OAI.KLInvariance.TitsSpace.BottKernelExact.projection_of_mul`: [BottSamelson.lean:1036](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1036).
