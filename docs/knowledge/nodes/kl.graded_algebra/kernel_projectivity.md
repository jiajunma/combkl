---
id: kl.algebra.kernel_projectivity
title: Kernel projectivity from two presentations of one module
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.projective_presentations
lean:
  repository: openai-kl
  modules:
  - ModuleAlgebra
  declarations:
  - OAI.KLInvariance.ReverseFiltration.kernel_projective_of_presentation
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:246
    format: lean-location
    note: OAI.KLInvariance.ReverseFiltration.kernel_projective_of_presentation
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the coefficient rings, module properties and actual maps explicit?
  verdict: Read the complete explicit retraction proof in ModuleAlgebra. Preserved
    the three projectivity hypotheses and both surjections, and checked the kernel
    equation and retraction componentwise.
tags:
- Kazhdan-Lusztig
- module-algebra
---

# Kernel projectivity from two presentations of one module

Let \(R\) be a commutative ring, and let
\[
f:F\twoheadrightarrow I,\qquad g:E\twoheadrightarrow I
\]
be linear surjections. Assume \(F,E,\ker g\) are projective. Then \(\ker f\) is projective.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The kernel comparison through explicit splitting maps.**

**OpenAI notes:** After image equality, the notes use a length-one graded free resolution of the edge image and graded Schanuel comparison to obtain a projective kernel. [eq:image-equality](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L370), [sec:induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

**Lean (primary):** The module comparison lifts each presentation map through the other and writes an explicit retraction from the sum of one source and the other kernel. The scalar-quotient presentation and actual-image equality supply the required projective kernel. The graded projective-to-free theorem is applied separately. [ModuleAlgebra:246](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L246), [GradedModules:538](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L538), [PositiveTransfer:970](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L970).

**Role in the proof:** The KB follows the maps used by Lean, with the common image, its two surjections, the regular scalar kernel and the retraction equation all displayed.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Lift the two presentation maps

Projectivity of \(F\) lifts \(f\) through \(g\), giving \(a:F\to E\) with \(ga=f\).

Projectivity of \(E\) lifts \(g\) through \(f\), giving \(b:E\to F\) with \(fb=g\).

Thus, for every \(v\in F\), \(ga(v)=f(v)\), and for every \(e\in E\), \(fb(e)=g(e)\).

### Step 2. Map the first kernel into a projective sum

For \(x\in\ker f\), \(g(a(x))=f(x)=0\), so \(a(x)\in\ker g\). Define
\[
i:\ker f\longrightarrow F\oplus\ker g,\qquad i(x)=(x,a(x)).
\]
This is linear, with its second component justified by the displayed kernel equation.

### Step 3. Construct the retraction

For \(v\in F\) and \(k\in\ker g\), set
\[
r(v,k)=v-ba(v)+b(k).
\]
It belongs to \(\ker f\), since
\[
\begin{aligned}
f(r(v,k))
&=f(v)-fb(a(v))+fb(k)\\
&=f(v)-ga(v)+g(k)\\
&=f(v)-f(v)+0=0.
\end{aligned}
\]
The formula is linear in \((v,k)\), so it defines a linear map into the kernel.

### Step 4. Verify the splitting equation

For \(x\in\ker f\),
\[
ri(x)=r(x,a(x))=x-ba(x)+ba(x)=x.
\]
Hence \(ri=1_{\ker f}\). This exhibits the new kernel as a direct summand of \(F\oplus\ker g\).

### Step 5. Transfer projectivity

Both summands of \(F\oplus\ker g\) are projective, so the finite sum is projective. The split-summand lifting argument then makes \(\ker f\) projective.

The source constructs exactly the maps \(a,b,i,r\) above. The common target \(I\) is the module whose two actual surjections are compared.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ReverseFiltration.kernel_projective_of_presentation`: [ModuleAlgebra.lean:246](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L246).
