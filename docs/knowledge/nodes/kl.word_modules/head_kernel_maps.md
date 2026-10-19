---
id: kl.word.head_kernel_maps
title: The two head-projection kernels and their graded pieces
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.head_pair_equivalence
- kl.word.pair_lattice_exact_sequences
- kl.detail.word_standard_stalks
- kl.algebra.scalar_twist
- kl.algebra.component_transport
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  declarations:
  - OAI.KLInvariance.kernelSourceEquiv
  - OAI.KLInvariance.kernelTargetEquiv
  - OAI.KLInvariance.kernelMixedEquiv
  - OAI.KLInvariance.TitsSpace.bottHeadKernelEquiv
  - OAI.KLInvariance.TitsSpace.bottHeadKernelPiece
  - OAI.KLInvariance.TitsSpace.bottHeadRight_surjective
  - OAI.KLInvariance.TitsSpace.bottDescentKernel
  - OAI.KLInvariance.TitsSpace.bottHeadRightKernelEquiv
  - OAI.KLInvariance.TitsSpace.bottHeadRightKernelPiece
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1551
    format: lean-location
    note: OAI.KLInvariance.kernelSourceEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1971
    format: lean-location
    note: OAI.KLInvariance.kernelTargetEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1999
    format: lean-location
    note: OAI.KLInvariance.kernelMixedEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1578
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadKernelEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1597
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadKernelPiece
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:2031
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadRight_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:2037
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottDescentKernel
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:2045
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadRightKernelEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:2067
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadRightKernelPiece
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the gradings, scalar actions, coefficient variables and formal polynomial
    conclusions explicit?
  verdict: Read both head kernel constructors, the descent orientation, right-head
    surjectivity and kernel grading definitions. Explained the source/codomain kernel
    transports and the precise real-linear type after untwisting.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# The two head-projection kernels and their graded pieces

Fix a finite-generator Coxeter system, a finite basis of its extended realization, and the symmetric coefficient algebra \(A\) with its degree-one grading. Fix a word \(\mathbf t\), a simple reflection \(s\), and \(x\in W\). Put
\[
X=M_{\mathbf t}^x,\qquad Y=M_{\mathbf t}^{sx},\qquad
Z=M_{s\mathbf t}^x,\qquad \tau=\chi_s,\quad \alpha=\alpha_s.
\]

For \(y\in Y\), write \([y]_\tau\) for the same underlying vector in \({}^\tau Y\). Its scalar law is
\[
a[y]_\tau=[\tau(a)y]_\tau.
\]
The twist has the same real-vector-space structure because \(\tau\) fixes real scalars.

The reflected pair lattice \(L_x\subseteq X\oplus{}^\tau Y\) has an \(A\)-linear coordinate isomorphism \(C_x:L_x\to Z\). Its two head projections are
\[
h_0(C_x(p,[q]_\tau))=p,\qquad h_1(C_x(p,[q]_\tau))=q.
\]
The first map is \(A\)-linear. The second is \(\tau\)-semilinear over \(A\) and real-linear, with its value viewed in the underlying \(Y\). Both preserve degree.

Both maps are surjective: to attain a prescribed value in \(X\) or \(Y\), choose a tail-word lift of that value, take its two stalk projections as a lattice pair, and apply \(C_x\).

## The two kernels

Define
\[
K_0=\ker h_0,\qquad K_1=\ker h_1.
\]
The source records \(K_0\) as the kernel of the \(A\)-linear first projection and \(K_1\) as the kernel of the real-linear second projection. We use their real-vector-space gradings
\[
(K_i)_n=\{z\in K_i:z\in Z_n\}.
\]
These are bottHeadKernelPiece and bottHeadRightKernelPiece.

Since \(h_i\) preserves degree, it commutes with homogeneous components. If \(h_i(z)=0\), then \(h_i(z_n)=0\) for every component \(z_n\). Thus each kernel is closed under components, and these pieces give its direct-sum grading.

## The ascent kernel map

If \(\ell(x)<\ell(sx)\), exact reflection kernels for the tail identify the first lattice-projection kernel with pairs
\((0,[\alpha y]_\tau)\), \(y\in Y\). Transporting through \(C_x\) gives
\[
\kappa_0:Y\xrightarrow{\sim}K_0,\qquad
y\longmapsto C_x(0,[\alpha y]_\tau),
\]
as a real-linear equivalence. The map \([y]_\tau\mapsto C_x(0,[\alpha y]_\tau)\) is \(A\)-linear on the twisted copy of \(Y\); the real-linear identification with the underlying \(Y\) gives the displayed map.

This is bottHeadKernelEquiv. Injectivity uses the nonzero root acting on the stalk coordinates, and surjectivity is the exact lattice-kernel statement.

## The descent kernel map

If \(\ell(sx)<\ell(x)\), use the upward tail edge \(sx\to x\). The second lattice-projection kernel consists of
\((\alpha z,0)\), \(z\in X\). Therefore
\[
\kappa_1:X\xrightarrow{\sim}K_1,\qquad
z\longmapsto C_x(\alpha z,0)
\]
is a real-linear equivalence. It is bottHeadRightKernelEquiv.

## Transporting the kernel through coordinate isomorphisms

For a linear map \(f:L\to P\) and an isomorphism \(e:L\to Z\), the map \(u\mapsto e(u)\) identifies
\[
\ker f\ \simeq\ \ker(f e^{-1}).
\]
The inverse is \(e^{-1}\). If the target is also changed by an injective linear isomorphism \(g:P\to Q\), the condition \(g(f(e^{-1}z))=0\) is equivalent to \(f(e^{-1}z)=0\).

The source names these constructions kernelSourceEquiv, kernelTargetEquiv and kernelMixedEquiv. In the descent case, the last construction combines the \(A\)-linear lattice isomorphism with the real-linear map forgetting the scalar twist.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.kernelSourceEquiv`: [BottSamelson.lean:1551](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1551).

`OAI.KLInvariance.kernelTargetEquiv`: [BottSamelson.lean:1971](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1971).

`OAI.KLInvariance.kernelMixedEquiv`: [BottSamelson.lean:1999](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1999).

`OAI.KLInvariance.TitsSpace.bottHeadKernelEquiv`: [BottSamelson.lean:1578](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1578).

`OAI.KLInvariance.TitsSpace.bottHeadKernelPiece`: [BottSamelson.lean:1597](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1597).

`OAI.KLInvariance.TitsSpace.bottHeadRight_surjective`: [BottSamelson.lean:2031](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L2031).

`OAI.KLInvariance.TitsSpace.bottDescentKernel`: [BottSamelson.lean:2037](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L2037).

`OAI.KLInvariance.TitsSpace.bottHeadRightKernelEquiv`: [BottSamelson.lean:2045](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L2045).

`OAI.KLInvariance.TitsSpace.bottHeadRightKernelPiece`: [BottSamelson.lean:2067](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L2067).
