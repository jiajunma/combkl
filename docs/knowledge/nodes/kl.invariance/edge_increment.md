---
id: kl.comparison.edge_increment
title: The uniform positive bound for a single edge increment
kind: theorem
status: proved
primary_topic: kl.invariance
topics:
- kl.invariance
uses:
- kl.local.edge_inclusion
- kl.comparison.normalized_kernel
- kl.detail.kernel_exact_sequence
- kl.detail.edge_images
- kl.paths.plane_degree
- kl.detail.quotient_image_free
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.BruhatGraph.normalized_edge_increment_le
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:621
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.normalized_edge_increment_le
  - artifact: openai-kl-paper
    locator: 6. Reciprocity and simultaneous induction; sec:induction
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
- induction
---

# The uniform positive bound for a single edge increment

Under the hypotheses of [[node:kl.local.edge_inclusion]], removing the condition at \(e:x\to y\) changes only the \(x\) coordinate, and
\[
D_x^{\mathrm{after}}\le D_x^{\mathrm{before}}
 +(t^{-1}-t)D_y,\qquad 0<t<1.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Equivalent parameter conventions.**

**OpenAI notes:** The comparison uses \(0<q<1\), scale \(q^{-d/2}(1-q)^N\), and transfer coefficient \(q^{-1/2}-q^{1/2}\). [eq:state](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L243), [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275).

**Lean (primary):** The comparison uses \(0<t<1\) and substitutes \(q=t^2\). Its scale is \(t^{-d}(1-t^2)^N\) and its transfer coefficient is \(t^{-1}-t\). [Dihedral:730](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L730), [PositiveTransfer:591](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L591), [PositiveTransfer:621](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L621), [EdgeLocalization:377](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L377), [EdgeLocalization:423](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L423).

**Role in the proof:** The substitution \(q=t^2\) identifies the two normalizations. Linear root labels have degree one throughout the calculation.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Name the two edge images

Fix \(e:x\to y\), outgoing condition sets \(F,H\), and \(0<t<1\). Put \(q=t^2\), so \(0<q<1\). Let
\[
I=\rho_{x,e}(K_x(F)),\qquad J=\rho_{y,e}(K_y(H)).
\]
The hypothesis is the inclusion \(I\subseteq f_eJ\) inside the same edge module. Write \(k=\deg f_e\).

### Step 2. Compute the change at the lower stalk

The one-condition exact sequence, proved in [[node:kl.detail.kernel_exact_sequence]], gives
\[
H_{K_x(F)}(q)-H_{K_x(F\cup\{e\})}(q)=H_I(q).
\]
The inclusion \(I\subseteq f_eJ\) implies an inclusion of every homogeneous piece. Its dimensions are therefore ordered; multiplying by the positive weights \(q^n\) and summing gives \(H_I(q)\le H_{f_eJ}(q)\).

### Step 3. Compute the upper-image Hilbert value

The upper restriction is quotient by the linear edge label \(\alpha_e\). Saturation of \(K_y(H)\) under division by \(\alpha_e\) identifies its restricted kernel with \(\alpha_eK_y(H)\). Multiplication by \(\alpha_e\) is injective and raises degree by one, so
\[
H_J(q)=(1-q)H_{K_y(H)}(q).
\]
The edge-factor map is injective and homogeneous of degree \(k\). It identifies \(J\), shifted by \(k\), with \(f_eJ\), giving
\(H_{f_eJ}(q)=q^kH_J(q)\).
The label regularity and edge-factor regularity needed here are properties of the actual Bruhat sheaf. No freeness of the current lower kernel is assumed.

### Step 4. Normalize and check the coefficient

Let \(s_z=(1-t^2)^N t^{\ell(z)-\ell(b)}>0\). Combining Steps 2–3 and multiplying by \(s_x\) yields
\[
D_x(F)-D_x(F\cup\{e\})
\le \frac{s_x}{s_y}q^k(1-q)D_y(H).
\]
Use \(2k=\ell(y)-\ell(x)-1\) from the edge-factor degree theorem:
\[
\frac{s_x}{s_y}q^k(1-q)
=t^{\ell(x)-\ell(y)+2k}(1-t^2)
=t^{-1}(1-t^2)=t^{-1}-t.
\]
Moving the second lower-state term to the right gives the claimed inequality. Every multiplication of an inequality used a positive factor.

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.normalized_edge_increment_le`: [PositiveTransfer.lean:621](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L621).
