---
id: kl.algebra.scalar_free_presentation
title: Free presentations over a scalar quotient and their kernels
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.scalar_quotient
- kl.algebra.projective_presentations
- kl.algebra.kernel_projectivity
lean:
  repository: openai-kl
  modules:
  - GradedModules
  declarations:
  - OAI.KLInvariance.ReverseFiltration.scalarQuotientMap
  - OAI.KLInvariance.ReverseFiltration.scalarQuotientMap_surjective
  - OAI.KLInvariance.ReverseFiltration.scalarKernelMap
  - OAI.KLInvariance.ReverseFiltration.scalarKernelMap_bijective
  - OAI.KLInvariance.ReverseFiltration.scalarKernel_projective
  - OAI.KLInvariance.ReverseFiltration.exists_scalar_presentation
  - OAI.KLInvariance.ReverseFiltration.kernel_projective_of_free_scalar_quotient
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:491
    format: lean-location
    note: OAI.KLInvariance.ReverseFiltration.scalarQuotientMap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:498
    format: lean-location
    note: OAI.KLInvariance.ReverseFiltration.scalarQuotientMap_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:507
    format: lean-location
    note: OAI.KLInvariance.ReverseFiltration.scalarKernelMap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:517
    format: lean-location
    note: OAI.KLInvariance.ReverseFiltration.scalarKernelMap_bijective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:531
    format: lean-location
    note: OAI.KLInvariance.ReverseFiltration.scalarKernel_projective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:538
    format: lean-location
    note: OAI.KLInvariance.ReverseFiltration.exists_scalar_presentation
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:561
    format: lean-location
    note: OAI.KLInvariance.ReverseFiltration.kernel_projective_of_free_scalar_quotient
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the coefficient rings, module properties and actual maps explicit?
  verdict: Read every scalarQuotientMap/scalarKernelMap declaration and both presentation
    theorems. Kept the domain and nonzero-label assumptions, induced A-action on P,
    finite quotient basis and explicit regular-scalar kernel.
tags:
- Kazhdan-Lusztig
- module-algebra
---

# Free presentations over a scalar quotient and their kernels

Let \(A\) be a commutative domain and \(a\ne0\). Put \(C=A/(a)\). Suppose \(P\) is finite free over \(C\), with its \(A\)-action induced by the quotient map.

There is a finite free \(A\)-module \(A^J\) and a surjection \(g:A^J\to P\) whose kernel is isomorphic to \(A^J\). In particular the kernel is projective.

Consequently, if \(F\) is projective over \(A\) and \(f:F\twoheadrightarrow P\), then \(\ker f\) is projective over \(A\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The kernel comparison through explicit splitting maps.**

**OpenAI notes:** After image equality, the notes use a length-one graded free resolution of the edge image and graded Schanuel comparison to obtain a projective kernel. [eq:image-equality](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L370), [sec:induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

**Lean (primary):** The module comparison lifts each presentation map through the other and writes an explicit retraction from the sum of one source and the other kernel. The scalar-quotient presentation and actual-image equality supply the required projective kernel. The graded projective-to-free theorem is applied separately. [ModuleAlgebra:246](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L246), [GradedModules:538](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L538), [PositiveTransfer:970](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L970).

**Role in the proof:** The KB follows the maps used by Lean, with the common image, its two surjections, the regular scalar kernel and the retraction equation all displayed.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Reduce a finite coordinate module

For a finite set \(J\), define
\[
\rho:A^J\to C^J,\qquad (v_j)\mapsto([v_j]).
\]
It is \(A\)-linear and surjective: choose a representative in \(A\) for each of the finitely many quotient coordinates.

Its kernel consists of the tuples whose every coordinate is divisible by \(a\).

### Step 2. Identify the reduction kernel by multiplication

Define
\[
\mu:A^J\to\ker\rho,\qquad (w_j)\mapsto(aw_j).
\]
It lands in the kernel because each \(aw_j\) is zero modulo \((a)\).

If \(\mu(w)=\mu(w')\), then \(aw_j=aw'_j\) in every coordinate. Since \(A\) is a domain and \(a\ne0\), cancellation gives \(w_j=w'_j\), proving injectivity.

For a kernel tuple \(v\), each \(v_j\in(a)\), so choose \(w_j\) with \(v_j=aw_j\). This proves surjectivity. Therefore \(\mu\) is an \(A\)-linear isomorphism, making \(\ker\rho\) free and projective.

### Step 3. Use a C-basis of P

Choose a finite \(C\)-basis of \(P\), giving a linear equivalence \(e:P\to C^J\). It is also \(A\)-linear because the \(A\)-actions factor through \(C\).

Define \(g=e^{-1}\rho:A^J\to P\). Both factors are surjective. Since \(e^{-1}\) is injective,
\(\ker g=\ker\rho\).
Step 2 supplies the required projective kernel.

### Step 4. Compare with the given surjection

The maps \(f:F\to P\) and \(g:A^J\to P\) are surjective. The modules \(F,A^J,\ker g\) are projective. The [[node:kl.algebra.kernel_projectivity|two-presentation theorem]] therefore gives projectivity of \(\ker f\).

For \(P=(A/(a))^r\), the presentation in Step 1 is the usual coordinate reduction, with kernel \(aA^r\). Step 2 identifies that kernel with \(A^r\) by the actual multiplication map.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ReverseFiltration.scalarQuotientMap`: [GradedModules.lean:491](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L491).

`OAI.KLInvariance.ReverseFiltration.scalarQuotientMap_surjective`: [GradedModules.lean:498](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L498).

`OAI.KLInvariance.ReverseFiltration.scalarKernelMap`: [GradedModules.lean:507](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L507).

`OAI.KLInvariance.ReverseFiltration.scalarKernelMap_bijective`: [GradedModules.lean:517](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L517).

`OAI.KLInvariance.ReverseFiltration.scalarKernel_projective`: [GradedModules.lean:531](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L531).

`OAI.KLInvariance.ReverseFiltration.exists_scalar_presentation`: [GradedModules.lean:538](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L538).

`OAI.KLInvariance.ReverseFiltration.kernel_projective_of_free_scalar_quotient`: [GradedModules.lean:561](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L561).
