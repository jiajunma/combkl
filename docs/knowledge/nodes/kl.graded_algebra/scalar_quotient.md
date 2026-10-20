---
id: kl.algebra.scalar_quotient
title: Scalar quotients and saturated submodules
kind: definition
status: formalized
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.homogeneous_subquotients
lean:
  repository: openai-kl
  modules:
  - GradedModules
  - ModuleAlgebra
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.Graded.ModuleData.scalarQuotient
  - OAI.KLInvariance.EdgeImage.reducedInclusion
  - OAI.KLInvariance.ScalarQuotient.submodule
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1122
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.scalarQuotient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:413
    format: lean-location
    note: OAI.KLInvariance.EdgeImage.reducedInclusion
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:613
    format: lean-location
    note: OAI.KLInvariance.ScalarQuotient.submodule
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, finiteness and freeness hypotheses, original embedded
    submodules, localization multipliers and schedule assumptions explicit?
  verdict: Read the local definitions and supporting proof bodies; stated the scalar
    direction, degree convention, and finite-generation hypotheses explicitly.
tags:
- Kazhdan-Lusztig
- global-inclusion
---

# Scalar quotients and saturated submodules

Let \(A\) be a commutative ring, \(M\) an \(A\)-module, and \(a\in A\). The scalar multiple submodule is
\[
aM=\{am:m\in M\}.
\]
The scalar quotient \(M/aM\) consists of classes with \(m\sim m'\) exactly when \(m-m'\in aM\).

Multiplication by \(a\) acts as zero on this quotient. Therefore its scalar action factors through \(A/(a)\):
\[
[r]\,[m]=[rm].
\]
Changing \(r\) by a multiple of \(a\), or \(m\) by an element of \(aM\), leaves the class unchanged.

A scalar \(a\) is regular on \(M\) when multiplication \(m\mapsto am\) is injective. Equivalently, \(am=0\) implies \(m=0\). This property specifies the module on which cancellation is valid.

## Reduction of an inclusion

For \(S\subseteq M\), inclusion induces
\[
S/aS\longrightarrow M/aM,\qquad [s]\longmapsto[s].
\]
Its kernel consists of classes represented by \(S\cap aM\). Thus it is injective exactly when
\[
S\cap aM=aS.
\]

Call \(S\) saturated with respect to \(a\) when \(am\in S\) implies \(m\in S\). Then an element \(s=am\in S\cap aM\) has \(m\in S\), so \(s\in aS\). The reverse inclusion is immediate. Saturation therefore makes the reduced inclusion injective.

## A submodule in a module already acted on by the quotient

Let \(N\) have compatible actions of \(A\) and \(C=A/(a)\), meaning
\[
r v=\overline r\,v\qquad(r\in A,\ v\in N).
\]
For an \(A\)-submodule \(S\subseteq N\), the same subset is a \(C\)-submodule. Indeed, for \(c\in C\), choose a representative \(r\in A\). If \(v\in S\), then \(cv=rv\in S\). Closure under addition and zero is unchanged.

Lean calls this object `ScalarQuotient.submodule a S`. It retains the original vectors and membership condition while expressing their scalar stability over \(C\). The [[node:kl.algebra.scalar_image_free|scalar-image theorem]] uses this coefficient action for the actual upper edge image and its correction multiple.

## A homogeneous scalar

If \(M\) is graded and \(a\) is homogeneous, \(aM\) is a homogeneous submodule, so \(M/aM\) has an induced grading. The quotient map has degree zero. The multiplication map \(m\mapsto am\) changes degree by \(\deg a\).

For \(A=k[X,Y]\), the quotient \(A/XA\) is \(k[Y]\). The element \(Y\) remains nonzero, while every multiple of \(X\) vanishes.

In an edge calculation, \(a\) is the root label and \(A/(a)\) is the edge coefficient ring. Saturation identifies the reduced upper kernel with its actual image in the edge module.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Compatible quotient actions and the actual free upper image.**

**OpenAI notes:** The notes identify the upper image with the selected upper kernel modulo the current root label. Saturation gives this quotient, and freeness of the upper kernel gives freeness over the edge coefficient ring. Multiplication by the nonzero correction then gives the free target. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The quotient action and its scalar tower are explicit. A finite free scalar presentation gives the edge-module basis. Regularity of the incoming label on every outgoing edge module gives saturation; Noetherian finiteness permits the finite quotient presentation. A separate same-carrier quotient-submodule construction and injective scalar-image map give freeness of the corrected target. [TerminalKernels:613](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L613), [TerminalKernels:624](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L624), [TerminalKernels:681](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L681), [TerminalKernels:691](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L691), [TerminalKernels:880](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L880).

**Role in the proof:** The Blueprint retains the precise coefficient ring of each freeness statement, all action compatibilities, the arbitrary outgoing selection and the finite-basis hypothesis used for finiteness.
<!-- source-comparison:end -->

## References

The local source declarations below define the constructions and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.Graded.ModuleData.scalarQuotient`: [GradedModules.lean:1122](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1122).

`OAI.KLInvariance.EdgeImage.reducedInclusion`: [ModuleAlgebra.lean:413](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L413).

`OAI.KLInvariance.ScalarQuotient.submodule`: [TerminalKernels.lean:613](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L613).
