---
id: kl.detail.reverse_projectivity
title: Recovering a projective kernel from scaled image equality
kind: theorem
status: proved
primary_topic: kl.invariance
topics:
- kl.invariance
uses:
- kl.detail.scaled_images
- kl.algebra.kernel_projectivity
- kl.algebra.scalar_quotient
- kl.algebra.projective_presentations
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.ReverseFiltration.scalarKernelEquiv
  - OAI.KLInvariance.ReverseFiltration.projective_kernel_of_scalar_presentation
  - OAI.KLInvariance.ReverseFiltration.imageMapKernelEquiv
  - OAI.KLInvariance.ReverseFiltration.inf_kernel_projective_of_image_eq
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:931
    format: lean-location
    note: OAI.KLInvariance.ReverseFiltration.scalarKernelEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:947
    format: lean-location
    note: OAI.KLInvariance.ReverseFiltration.projective_kernel_of_scalar_presentation
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:958
    format: lean-location
    note: OAI.KLInvariance.ReverseFiltration.imageMapKernelEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:970
    format: lean-location
    note: OAI.KLInvariance.ReverseFiltration.inf_kernel_projective_of_image_eq
  - artifact: openai-kl-paper
    locator: Related paper context; sec:induction
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the coefficient rings, module properties and actual maps explicit?
  verdict: Read scalarKernelEquiv, projective_kernel_of_scalar_presentation and the
    actual imageMapKernelEquiv proof. Replaced the earlier pullback presentation by
    the source explicit two-lift retraction, checking every supplied hypothesis.
tags:
- Kazhdan-Lusztig
- module-algebra
---

# Recovering a projective kernel from scaled image equality

Let \(A\) be a commutative ring. Suppose \(S\subseteq M\) and \(T\subseteq P\) are projective \(A\)-modules. Let
\[
f:M\to N,\qquad g:P\to N,\qquad \psi:N\to N
\]
be linear maps, with \(\psi\) injective. Assume
\[
f(S)=\psi(g(T)),\qquad \ker g=\alpha P,
\]
multiplication by \(\alpha\) on \(P\) is injective, and \(T\) is saturated with respect to \(\alpha\). Then \(S\cap\ker f\) is projective.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The kernel comparison through explicit splitting maps.**

**OpenAI notes:** After image equality, the notes use a length-one graded free resolution of the edge image and graded Schanuel comparison to obtain a projective kernel. [eq:image-equality](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L370), [sec:induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

**Lean (primary):** The module comparison lifts each presentation map through the other and writes an explicit retraction from the sum of one source and the other kernel. The scalar-quotient presentation and actual-image equality supply the required projective kernel. The graded projective-to-free theorem is applied separately. [ModuleAlgebra:246](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L246), [GradedModules:538](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L538), [PositiveTransfer:970](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L970).

**Role in the proof:** The KB follows the maps used by Lean, with the common image, its two surjections, the regular scalar kernel and the retraction equation all displayed.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Construct the two maps onto the common image

Put \(U=f(S)\). The first map is
\[
u:S\to U,\qquad s\mapsto f(s),
\]
which is surjective by the definition of \(U\).

Image equality gives a second well-defined map
\[
v:T\to U,\qquad t\mapsto\psi(g(t)).
\]
Every \(z\in U=\psi(g(T))\) has a representation \(z=\psi(g(t))\) with \(t\in T\), proving its surjectivity.

### Step 2. Identify the second kernel as a scalar multiple

If \(v(t)=0\), injectivity of \(\psi\) gives \(g(t)=0\). Since \(\ker g=\alpha P\), write \(t=\alpha p\), \(p\in P\).

The vector \(t\) belongs to \(T\), so saturation implies \(p\in T\). Hence \(t\in\alpha T\).

Conversely, for \(t=\alpha p\) with \(p\in T\), the scalar-kernel assumption gives \(g(t)=0\), so \(v(t)=0\). Thus \(\ker v=\alpha T\).

### Step 3. Transfer projectivity to this kernel

Multiplication by \(\alpha\) defines
\[
T\longrightarrow\ker v,\qquad t\longmapsto\alpha t.
\]
It is surjective by Step 2, and injective because the action on the ambient \(P\) is injective. It is therefore a linear isomorphism.

Since \(T\) is projective, this makes \(\ker v\) projective.

### Step 4. Apply the two-presentation construction

The [[node:kl.algebra.kernel_projectivity|common-target theorem]] applies with
\[
F=S,\qquad E=T,\qquad I=U,\qquad f=u,\qquad g=v.
\]
Both maps are surjective; \(S,T\) are projective by hypothesis; and \(\ker v\) is projective by Step 3.

It chooses lifts \(a:S\to T\), \(b:T\to S\) with \(va=u\), \(ub=v\), and exhibits \(\ker u\) as a retract of \(S\oplus\ker v\) by
\[
x\longmapsto(x,a(x)),\qquad
(s,k)\longmapsto s-ba(s)+b(k).
\]
The two-presentation proof checks both the kernel equation and the identity of the composite. Thus \(\ker u\) is projective.

### Step 5. Identify the submodule in the statement

A vector of \(\ker u\) is a vector \(s\in S\) with \(f(s)=0\). Forgetting the subtype identifies it linearly with \(S\cap\ker f\); the inverse equips such a vector with those same two membership conditions.

Transporting projectivity along this equivalence proves the result.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ReverseFiltration.scalarKernelEquiv`: [PositiveTransfer.lean:931](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L931).

`OAI.KLInvariance.ReverseFiltration.projective_kernel_of_scalar_presentation`: [PositiveTransfer.lean:947](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L947).

`OAI.KLInvariance.ReverseFiltration.imageMapKernelEquiv`: [PositiveTransfer.lean:958](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L958).

`OAI.KLInvariance.ReverseFiltration.inf_kernel_projective_of_image_eq`: [PositiveTransfer.lean:970](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L970).
