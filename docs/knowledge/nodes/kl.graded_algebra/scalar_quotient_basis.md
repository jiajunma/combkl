---
id: kl.algebra.scalar_quotient_basis
title: A basis descends through a scalar-kernel presentation
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
  - OAI.KLInvariance.ScalarQuotient.coordinateReduction
  - OAI.KLInvariance.ScalarQuotient.coordinateReduction_surjective
  - OAI.KLInvariance.ScalarQuotient.coordinateReduction_kernel
  - OAI.KLInvariance.ScalarQuotient.free_of_scalar_presentation
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:573
    format: lean-location
    note: OAI.KLInvariance.ScalarQuotient.coordinateReduction
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:578
    format: lean-location
    note: OAI.KLInvariance.ScalarQuotient.coordinateReduction_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:586
    format: lean-location
    note: OAI.KLInvariance.ScalarQuotient.coordinateReduction_kernel
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:595
    format: lean-location
    note: OAI.KLInvariance.ScalarQuotient.free_of_scalar_presentation
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read coordinateReduction, its surjectivity and exact scalar kernel, and
    the quotient comparison in free_of_scalar_presentation. Retained arbitrary commutative
    R and scalar a, a finite source basis, surjectivity, the exact kernel and the
    compatible quotient-ring action.
tags:
- Kazhdan-Lusztig
- coefficient-rings
---

# A basis descends through a scalar-kernel presentation

Let \(R\) be a commutative ring, \(a\in R\), and \(M\) an \(R\)-module with a finite basis \((b_i)_{i\in I}\). Put \(C=R/(a)\).

Let \(N\) be a \(C\)-module whose \(R\)-action is induced by the quotient map. Suppose \(q:M\to N\) is \(R\)-linear, surjective, and
\[
\ker q=aM.
\]
Then \(N\) is free over \(C\). More precisely, the vectors \(q(b_i)\) form a \(C\)-basis.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Coordinate construction of the edge coefficient module.**

**OpenAI notes:** The upper-end quotient rule presents the edge module as the upper stalk modulo its root label. The edge comparison regards it as a free module over the corresponding coefficient quotient. [bg:bmp](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225), [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The root label first annihilates the edge module, defining its quotient-ring action and scalar compatibility. Coordinate reduction of a finite upper-stalk basis has the same scalar kernel as the upper restriction, and the quotient comparison gives a basis of the actual edge module. [TerminalKernels:516](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L516), [TerminalKernels:573](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L573), [TerminalKernels:595](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L595), [TerminalKernels:669](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L669), [TerminalKernels:681](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L681).

**Role in the proof:** Both the coefficient ring and its module action are fixed before comparing lower and upper images. Their elements remain in the original edge module with its induced quotient-ring scalars.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Reduce the basis coordinates

For \(m=\sum_i r_i b_i\), define
\[
\rho:M\to C^I,\qquad \rho(m)=([r_i])_i.
\]
Each coordinate is the original \(R\)-linear coordinate functional followed by the quotient map, so \(\rho\) is \(R\)-linear.

It is surjective: choose an \(R\)-representative \(r_i\) for each coordinate of a given tuple in \(C^I\), and take \(\sum_i r_i b_i\).

### Step 2. Compute the coordinate-reduction kernel

If \(m=aw\), its coordinates are multiples of \(a\), so \(\rho(m)=0\).

Conversely, if \(\rho(m)=0\), write each coordinate \(r_i=as_i\). Then
\[
m=\sum_i as_i b_i=a\left(\sum_i s_i b_i\right).
\]
Thus \(\ker\rho=aM\), the same kernel as \(q\).

### Step 3. Compare the two quotient presentations

Define
\[
j:N\to C^I,\qquad j(q(m))=\rho(m).
\]
If \(q(m)=q(m')\), then \(m-m'\in aM=\ker\rho\), so the value is independent of the chosen preimage. Surjectivity of \(q\) defines \(j\) on all of \(N\).

On preimages, additivity and scalar compatibility are explicit:
\[
j(q(m)+q(n))=\rho(m+n)=\rho(m)+\rho(n),
\]
\[
j(rq(m))=\rho(rm)=r\rho(m)\qquad(r\in R).
\]
Surjectivity of \(q\) makes these the linearity equations on all of \(N\).

The same reasoning defines an inverse by \(\rho(m)\mapsto q(m)\), using surjectivity of \(\rho\) and equality of the kernels. Hence \(j\) is an \(R\)-linear equivalence. This is the quotient comparison used by free_of_scalar_presentation.

### Step 4. Verify linearity over the quotient ring

Take \(c\in C\), choose \(r\in R\) with \(c=[r]\), and let \(n\in N\). Compatibility of the scalar actions and \(R\)-linearity give
\[
j(cn)=j(rn)=rj(n)=cj(n).
\]
Thus \(j\) is \(C\)-linear. The same is true of its inverse.

### Step 5. Identify the descended basis

The coordinate vector \(\rho(b_i)\) is the \(i\)-th standard basis vector of \(C^I\). Since \(j(q(b_i))=\rho(b_i)\), the inverse of \(j\) carries the standard basis to \((q(b_i))\). These vectors therefore form a \(C\)-basis of \(N\).

For an upper stalk \(A^r\) with edge quotient by a root label \(\alpha\), this construction gives the \(r\) residue vectors as a basis over \(A/(\alpha)\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ScalarQuotient.coordinateReduction`: [TerminalKernels.lean:573](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L573).

`OAI.KLInvariance.ScalarQuotient.coordinateReduction_surjective`: [TerminalKernels.lean:578](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L578).

`OAI.KLInvariance.ScalarQuotient.coordinateReduction_kernel`: [TerminalKernels.lean:586](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L586).

`OAI.KLInvariance.ScalarQuotient.free_of_scalar_presentation`: [TerminalKernels.lean:595](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L595).
