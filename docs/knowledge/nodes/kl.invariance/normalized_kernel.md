---
id: kl.comparison.normalized_kernel
title: Kernel Hilbert values and normalized states
kind: definition
status: formalized
primary_topic: kl.invariance
topics:
- kl.invariance
uses:
- kl.sheaves.upward_kernel
- kl.detail.hilbert_values
- kl.algebra.hilbert_convergence
- kl.sheaves.boundary_sheaf
- kl.sheaves.graded_module
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.kernelHilbert
  - OAI.KLInvariance.BruhatGraph.stateScale
  - OAI.KLInvariance.BruhatGraph.normalizedKernel
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:359
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.kernelHilbert
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:591
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.stateScale
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:599
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.normalizedKernel
  - artifact: openai-kl-paper
    locator: 6. Reciprocity and simultaneous induction; sec:induction
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the integer degree, scalar regularity, image inclusion, convergence
    and parameter assumptions explicit, and are source hypotheses separated from derived
    applications?
  verdict: Defined kernelHilbert on actual ModuleData stalks, including zero negative
    pieces and integer indexing; retained finite-piece convergence, the actual coefficient-basis
    cardinality and integer length exponents, and the conditional homogeneous-free-basis
    formula.
tags:
- Kazhdan-Lusztig
- Hilbert-comparison
---

# Kernel Hilbert values and normalized states

Let \(A=\mathbb R[X_i:i\in\Sigma]\), where \(\Sigma\) is finite and the variables have degree one. Let \(\mathcal B\) be a graded sheaf with graded module data at its vertices and edges, including finite generation and zero negative-degree pieces.

## The selected-kernel Hilbert value

For a vertex \(x\) and outgoing selection \(F\), let \(K_x(F)\) be the selected kernel. Its degree-\(n\) piece is the actual intersection
\[
K_x(F)_n=K_x(F)\cap(\mathcal B^x)_n.
\]
The kernel Hilbert value is
\[
H_x(F;q)=
\sum_{n\in\mathbb Z}\dim_{\mathbb R}K_x(F)_n\,q^n,
\qquad 0<q<1.
\]
This is the convergent polynomial-module specialization of `GradedSheaf.kernelHilbert`, which evaluates the source's `Hilbert.value` on this actual submodule.

The [[node:kl.algebra.hilbert_convergence|Hilbert-convergence theorem]] gives finite dimensions and convergence. The field `ModuleData.nonneg` sets every negative stalk piece to zero. The selected kernel inherits this support, so its Hilbert sum over \(\mathbb Z\) equals the sum over \(n\ge0\).

## The state scale on a Coxeter interval

Now fix a finite-generator real Coxeter system \(W\), \(u\le_Wb\), a finite real basis of its extended realization, and a boundary sheaf \(\mathcal B\) on \([u,b]_W\) over the corresponding polynomial algebra \(A\). Put
\[
N=|\Sigma|,
\]
the number of basis coordinates, equivalently the number of polynomial variables.

For \(x\in[u,b]_W\) and \(0<t<1\), the source's state scale and normalized kernel are
\[
s_x(t)=(1-t^2)^N\,t^{\,\ell_W(x)-\ell_W(b)},
\qquad
D_x(t,F)=s_x(t)\,H_x(F;t^2).
\]
These are `stateScale` and `normalizedKernel`. The exponent \(\ell_W(x)-\ell_W(b)\) is an integer. The comparison uses \(0<t<1\), so \(0<t^2<1\) and the Hilbert value converges.

The factor \((1-t^2)^N\) removes the coefficient-ring denominator. If the kernel has a finite homogeneous free basis with generator degrees \(d_1,\ldots,d_r\ge0\), the formula becomes
\[
D_x(t,F)=t^{\,\ell_W(x)-\ell_W(b)}
\sum_{i=1}^r t^{2d_i}.
\]
The definition by intersection dimensions also applies to partial kernels before their freeness is established.

## The coefficient used when a condition is removed

Define
\[
T(t)=t^{-1}-t.
\]
The [[node:kl.comparison.edge_normalization|edge-normalization theorem]] proves that the correction degree makes this same coefficient occur at every edge. It also proves \(s_x(t)>0\) and \(T(t)>0\) for \(0<t<1\).

A single-edge comparison uses the normalized values at the lower endpoint with and without its current condition, and the unchanged selected-kernel value at the upper endpoint. A full schedule collects these numbers into a vector indexed by the interval vertices.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Equivalent parameter conventions.**

**OpenAI notes:** The comparison uses \(0<q<1\), scale \(q^{-d/2}(1-q)^N\), and transfer coefficient \(q^{-1/2}-q^{1/2}\). [eq:state](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L243), [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275).

**Lean (primary):** The comparison uses \(0<t<1\) and substitutes \(q=t^2\). Its scale is \(t^{-d}(1-t^2)^N\) and its transfer coefficient is \(t^{-1}-t\). [Dihedral:730](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L730), [PositiveTransfer:591](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L591), [PositiveTransfer:621](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L621), [EdgeLocalization:377](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L377), [EdgeLocalization:423](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L423), [PositiveTransfer:535](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L535), [PositiveTransfer:603](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L603).

**Role in the proof:** The substitution \(q=t^2\) identifies the two normalizations. Linear root labels have degree one throughout the calculation.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.kernelHilbert`: [PositiveTransfer.lean:359](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L359).

`OAI.KLInvariance.BruhatGraph.stateScale`: [PositiveTransfer.lean:591](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L591).

`OAI.KLInvariance.BruhatGraph.normalizedKernel`: [PositiveTransfer.lean:599](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L599).
