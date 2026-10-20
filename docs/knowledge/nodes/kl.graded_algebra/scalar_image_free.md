---
id: kl.algebra.scalar_image_free
title: Scalar images over a quotient ring preserve freeness under injectivity
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
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.ScalarQuotient.scalarImage
  - OAI.KLInvariance.ScalarQuotient.free_scalarImage
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:867
    format: lean-location
    note: OAI.KLInvariance.ScalarQuotient.scalarImage
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:880
    format: lean-location
    note: OAI.KLInvariance.ScalarQuotient.free_scalarImage
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, finiteness and freeness hypotheses, original embedded
    submodules, localization multipliers and schedule assumptions explicit?
  verdict: Checked arbitrary commutative coefficients, quotient-action compatibility,
    same-carrier images, injectivity on the ambient module and basis transfer without
    a finiteness hypothesis.
tags:
- Kazhdan-Lusztig
- global-inclusion
---

# Scalar images over a quotient ring preserve freeness under injectivity

Let \(R\) be a commutative ring, \(a,z\in R\), and \(C=R/(a)\). Let \(N\) be a module over both \(R\) and \(C\), with compatible scalar actions
\[
r v=\overline r\,v\qquad(r\in R,\ v\in N).
\]
For an \(R\)-submodule \(S\subseteq N\), write \(S_C\) for its same-carrier quotient-ring submodule. Define
\[
zS=\{zv:v\in S\}\subseteq N.
\]
Then
\[
(zS)_C=\overline z\,S_C.
\]
If \(S_C\) is free over \(C\) and multiplication by \(z\) is injective on \(N\), then \((zS)_C\) is free over \(C\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Compatible quotient actions and the actual free upper image.**

**OpenAI notes:** The notes identify the upper image with the selected upper kernel modulo the current root label. Saturation gives this quotient, and freeness of the upper kernel gives freeness over the edge coefficient ring. Multiplication by the nonzero correction then gives the free target. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The quotient action and its scalar tower are explicit. A finite free scalar presentation gives the edge-module basis. Regularity of the incoming label on every outgoing edge module gives saturation; Noetherian finiteness permits the finite quotient presentation. A separate same-carrier quotient-submodule construction and injective scalar-image map give freeness of the corrected target. [TerminalKernels:613](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L613), [TerminalKernels:624](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L624), [TerminalKernels:681](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L681), [TerminalKernels:691](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L691), [TerminalKernels:880](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L880).

**Role in the proof:** The Blueprint retains the precise coefficient ring of each freeness statement, all action compatibilities, the arbitrary outgoing selection and the finite-basis hypothesis used for finiteness.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Identify the two image membership conditions

A vector \(v\) belongs to \((zS)_C\) exactly when \(v=zw\) for some \(w\in S\). Compatibility of the scalar actions gives \(zw=\overline z\,w\). The same witness \(w\) therefore proves membership in \(\overline z\,S_C\).

Conversely, a witness \(v=\overline z\,w\) with \(w\in S_C\) is also a witness \(v=zw\) with \(w\in S\). Both containments hold in the same underlying module \(N\), proving the submodule equality.

### Step 2. Construct the scalar-image isomorphism

Define
\[
\mu:S_C\longrightarrow \overline z\,S_C,\qquad w\longmapsto\overline z\,w.
\]
This is \(C\)-linear because \(C\) is commutative. It is surjective by the definition of its codomain.

If \(\mu(w)=\mu(w')\), compatibility gives \(zw=zw'\) in \(N\). The assumed injectivity of multiplication by \(z\) implies \(w=w'\). Hence \(\mu\) is an isomorphism.

### Step 3. Transfer a free basis

Choose a \(C\)-basis \((e_i)\) of \(S_C\). Its image \((\overline z\,e_i)\) spans the target because \(\mu\) is surjective. A finite linear relation among these images pulls back through injectivity of \(\mu\) to the corresponding relation among the \(e_i\), whose coefficients all vanish.

Thus the images form a free basis of \(\overline z\,S_C\). Step 1 identifies this target with \((zS)_C\), proving the result.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ScalarQuotient.scalarImage`: [TerminalKernels.lean:867](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L867).

`OAI.KLInvariance.ScalarQuotient.free_scalarImage`: [TerminalKernels.lean:880](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L880).
