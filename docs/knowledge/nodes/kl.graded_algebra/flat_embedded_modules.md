---
id: kl.algebra.flat_embedded_modules
title: Scalar extension of embedded kernels and images
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses: []
lean:
  repository: openai-kl
  modules:
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.FlatSubmodule.baseChange_ker
  - OAI.KLInvariance.FlatSubmodule.baseChange_map
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:279
    format: lean-location
    note: OAI.KLInvariance.FlatSubmodule.baseChange_ker
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:284
    format: lean-location
    note: OAI.KLInvariance.FlatSubmodule.baseChange_map
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read both FlatSubmodule proofs. Defined the embedded base-change submodule
    as an image, proved image commutation by tensor generators in both directions,
    and retained flatness only for the kernel identity.
tags:
- Kazhdan-Lusztig
- sheaf-operations
---

# Scalar extension of embedded kernels and images

Let \(R\to S\) be a homomorphism of commutative rings, let \(M,N\) be \(R\)-modules, and let \(f:M\to N\) be \(R\)-linear.

For an actual submodule \(P\subseteq M\), write
\[
P_S=\operatorname{im}\bigl(S\otimes_R P\longrightarrow S\otimes_R M\bigr),
\]
where the map is induced by the inclusion. Thus \(P_S\) is an \(S\)-submodule of a specified ambient tensor module. Its elements are finite sums of tensors \(s\otimes p\), with \(p\in P\), interpreted in \(S\otimes_R M\). This is the embedded submodule operation baseChange.

Write \(f_S=1\otimes f\). Then
\[
(f(P))_S=f_S(P_S)
\quad\text{inside }S\otimes_R N.
\]
If \(S\) is flat as an \(R\)-module, then also
\[
(\ker f)_S=\ker f_S
\quad\text{inside }S\otimes_R M.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit finite-flat construction.**

**OpenAI notes:** The localization discussion uses flat extension of kernels and images and then decomposes the localized sheaf over the local ring on a dihedral coset. [loc:models](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L125), [loc:decomposition](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L285).

**Lean (primary):** The scalar-extension lemmas first treat general commutative rings and graph sheaves. Finite product maps identify tensor constraints; flat exactness gives section and selected-kernel identities. Image commutation is proved separately by tensor generators. [MinimalExtensions:1157](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1157), [MinimalExtensions:1162](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1162), [TerminalKernels:279](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L279), [TerminalKernels:360](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L360).

**Role in the proof:** These algebraic results precede the root-plane and coset specialization. The later pullback argument controls the surviving edges, while both localized edge images retain their common ambient module.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Map generators of the extended image

An element of \(f(P)\) has the form \(f(p)\) for some \(p\in P\). Hence a generating tensor of \((f(P))_S\) is
\[
s\otimes f(p)=f_S(s\otimes p).
\]
The vector \(s\otimes p\) lies in \(P_S\), so this generator belongs to \(f_S(P_S)\). The latter is a submodule, hence contains all finite sums of these generators. This proves
\((f(P))_S\subseteq f_S(P_S)\).

### Step 2. Map a general vector of the extended submodule

Write \(w\in P_S\) as \(\sum_i s_i\otimes p_i\), with \(p_i\in P\). Then
\[
f_S(w)=\sum_i s_i\otimes f(p_i).
\]
Every term belongs to \((f(P))_S\), proving the reverse inclusion. This image identity uses no flatness hypothesis.

### Step 3. Tensor the kernel inclusion under flatness

Let \(i:\ker f\hookrightarrow M\). The sequence
\[
0\longrightarrow\ker f\xrightarrow{i}M\xrightarrow{f}N
\]
is exact at \(\ker f\) and \(M\). Flatness gives
\[
\operatorname{im}(1\otimes i)=\ker(1\otimes f).
\]
The left side is precisely the defined embedded submodule \((\ker f)_S\), and the right side is \(\ker f_S\). This is the required equality in the ambient tensor module.

### Step 4. Interpret localization

If \(S=R_{\mathfrak p}\), this submodule is generated by the images \(1\otimes p\), with coefficients in the local ring. Under the usual fraction notation its elements are \(p/s\) with \(p\in P\) and \(s\notin\mathfrak p\), after combining finitely many denominators.

Localization is flat, so both identities apply. They preserve the inclusion of each kernel or image into its ambient module, which is the data used in the later edge-image comparison.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.FlatSubmodule.baseChange_ker`: [TerminalKernels.lean:279](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L279).

`OAI.KLInvariance.FlatSubmodule.baseChange_map`: [TerminalKernels.lean:284](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L284).
