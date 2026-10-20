---
id: kl.local.scaled_image_denominator
title: A localized scaled-image equality gives an original-module multiplier
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.detail.scaled_images
- kl.algebra.tensor_local_denominator
- kl.algebra.flat_embedded_modules
- kl.notes.sheaf_localization
lean:
  repository: openai-kl
  modules:
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.scaledImages_denominator
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:946
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.scaledImages_denominator
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, finiteness and freeness hypotheses, original embedded
    submodules, localization multipliers and schedule assumptions explicit?
  verdict: Verified arbitrary coefficient localization, finite-edge flat kernel/image
    identities, the actual upper witness, equality of base-changed scalar multiplication
    on pure tensors and the two-factor denominator lemma.
tags:
- Kazhdan-Lusztig
- global-inclusion
---

# A localized scaled-image equality gives an original-module multiplier

Let \(R\) be a commutative ring, \(P\subseteq R\) a multiplicative submonoid, and \(S=P^{-1}R\), with structure map \(\iota:R\to S\). Let \(\mathcal B\) be an \(R\)-linear sheaf on an ordered graph with finitely many edges.

Fix an edge \(e:x\to y\), outgoing selections \(F,H\) at \(x,y\), and \(a\in R\). Write
\[
L=\rho_e^-(K_x^{\mathcal B}(F)),\qquad
U=\rho_e^+(K_y^{\mathcal B}(H))
\]
inside \(\mathcal B^e\). Suppose the scalar-extended sheaf satisfies
\[
L_e^{\mathcal B_S}(F)=\iota(a)\,U_e^{\mathcal B_S}(H),
\qquad \mathcal B_S=S\otimes_R\mathcal B.
\]
Then every \(z\in L\) has a multiplier \(s\in P\) such that
\[
sz\in aU.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Two denominator factors convert localized membership into a scalar witness.**

**OpenAI notes:** The notes pass from localized image equality to local membership in the free target, using flatness to commute localization with the finite kernel and image constructions. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47), [edge:lattice](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L26).

**Lean (primary):** The embedded tensor image is identified with a localized submodule. A numerator denominator and a second factor clearing equality in the localized module give an original-module scalar witness. The sheaf application verifies flat lower/upper image identities and compatibility of the scalar map on pure tensors before applying this lemma. [TerminalKernels:909](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L909), [TerminalKernels:914](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L914), [TerminalKernels:946](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L946).

**Role in the proof:** The Blueprint displays both denominator factors and explains the exact transition from an equality of localized edge images to a multiplier outside the plane prime.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Put the original lower image into its localized image

A localization is flat. On the finite graph, the [[node:kl.notes.sheaf_localization|flat kernel-and-image theorem]] identifies the embedded scalar extension of \(L\) with \(L_e^{\mathcal B_S}(F)\), and that of \(U\) with \(U_e^{\mathcal B_S}(H)\).

Since \(z\in L\), the pure tensor \(1\otimes z\) belongs to the embedded scalar extension of \(L\), hence to the localized lower image.

### Step 2. Use the localized equality with an actual upper witness

By the assumed equality, there is a vector \(w\in K_y^{\mathcal B_S}(H)\) such that
\[
1\otimes z=\iota(a)\rho_e^{\mathcal B_S,+}(w).
\]
Thus \(1\otimes z\) lies in \(\iota(a)\) times the localized upper image.

### Step 3. Identify this scaled image with the scalar extension of aU

Let \(\mu_a:\mathcal B^e\to\mathcal B^e\) be multiplication by \(a\). Scalar extension sends it to multiplication by \(\iota(a)\). On pure tensors,
\[
(\mu_a)_S(r\otimes v)=r\otimes av
=\iota(a)(r\otimes v),
\]
and linearity extends the equality to every tensor.

The embedded-image scalar-extension identity therefore gives
\[
(aU)_S=\iota(a)U_S
=\iota(a)U_e^{\mathcal B_S}(H).
\]
Together with Step 2, this proves \(1\otimes z\in(aU)_S\).

### Step 4. Clear a denominator in the actual edge module

Apply the [[node:kl.algebra.tensor_local_denominator|tensor-localization denominator theorem]] to the original submodule \(aU\subseteq\mathcal B^e\) and the vector \(z\). It supplies \(s\in P\) with \(sz\in aU\), proving the claim.

For localization at a prime ideal \(\mathfrak p\), this says \(s\notin\mathfrak p\). It is the form used to turn a plane-local image equality into a multiplier outside the plane prime.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.scaledImages_denominator`: [TerminalKernels.lean:946](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L946).
