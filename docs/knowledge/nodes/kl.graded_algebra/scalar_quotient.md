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
  declarations:
  - OAI.KLInvariance.Graded.ModuleData.scalarQuotient
  - OAI.KLInvariance.EdgeImage.reducedInclusion
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
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source assumptions and maps?
  verdict: Read the local definitions and supporting proof bodies; stated the scalar
    direction, degree convention, and finite-generation hypotheses explicitly.
tags:
- Kazhdan-Lusztig
- graded-algebra
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

## A homogeneous scalar

If \(M\) is graded and \(a\) is homogeneous, \(aM\) is a homogeneous submodule, so \(M/aM\) has an induced grading. The quotient map has degree zero. The multiplication map \(m\mapsto am\) changes degree by \(\deg a\).

For \(A=k[X,Y]\), the quotient \(A/XA\) is \(k[Y]\). The element \(Y\) remains nonzero, while every multiple of \(X\) vanishes.

In an edge calculation, \(a\) is the root label and \(A/(a)\) is the edge coefficient ring. Saturation identifies the reduced upper kernel with its actual image in the edge module.

## References

The local source declarations below define the constructions and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.Graded.ModuleData.scalarQuotient`: [GradedModules.lean:1122](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1122).

`OAI.KLInvariance.EdgeImage.reducedInclusion`: [ModuleAlgebra.lean:413](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L413).
