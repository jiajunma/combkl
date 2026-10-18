---
id: kl.algebra.homogeneous_subquotients
title: Homogeneous submodules, quotients, and map images
kind: definition
status: formalized
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.sheaves.graded_module
- kl.algebra.grading_components
lean:
  repository: openai-kl
  modules:
  - GradedModules
  declarations:
  - OAI.KLInvariance.Graded.subPiece
  - OAI.KLInvariance.Graded.quotientPiece
  - OAI.KLInvariance.Graded.ModuleData.sub
  - OAI.KLInvariance.Graded.ModuleData.quotient
  - OAI.KLInvariance.Graded.ModuleData.kernel
  - OAI.KLInvariance.Graded.ModuleData.range
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:743
    format: lean-location
    note: OAI.KLInvariance.Graded.subPiece
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:771
    format: lean-location
    note: OAI.KLInvariance.Graded.quotientPiece
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1077
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.sub
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1089
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.quotient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1112
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.kernel
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1117
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.range
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

# Homogeneous submodules, quotients, and map images

Let \(M=\bigoplus_nM_n\) be a graded \(A\)-module. A submodule \(S\subseteq M\) is homogeneous when every component of each of its elements still belongs to \(S\):
\[
m\in S\Longrightarrow \pi_n(m)\in S\quad\text{for every }n.
\]
It then has the grading \(S_n=S\cap M_n\). Every element of \(S\) is the finite sum of these components, and their uniqueness follows from uniqueness in \(M\).

## The quotient grading

The degree-\(n\) subspace of \(M/S\) is the image of \(M_n\) under the quotient map:
\[
(M/S)_n=(M_n+S)/S.
\]
Every class \([m]\) is the sum of the classes of the components of \(m\).

To check uniqueness, suppose a finite sum of homogeneous representatives \(m_n\) has zero class. Then \(\sum_n m_n\in S\). Homogeneity of \(S\) gives \(m_n\in S\) for every \(n\), so every summand already has zero class. Thus the quotient pieces form a direct sum.

The component of \([m]\) is \([\pi_n(m)]\). If \(m\) is replaced by \(m+s\) with \(s\in S\), its component changes by \(\pi_n(s)\in S\), so this formula is well defined.

## Kernels and images of homogeneous maps

Let \(f:M\to N\) preserve degrees. Decomposing \(m\) and using uniqueness in \(N\) gives
\[
\pi_n(f(m))=f(\pi_n(m)).
\]
If \(m\in\ker f\), the left side is zero; therefore every component lies in \(\ker f\). The kernel is homogeneous.

If \(y=f(m)\), its component is \(f(\pi_n(m))\), again in the image. Hence the image is homogeneous as well. These constructions supply the graded kernels and ranges used in exact sequences.

## A scalar quotient

For a homogeneous \(a\in A_d\), the image \(aM\) is homogeneous: the degree-\(n\) component of \(am\) is \(a\,m_{n-d}\). Thus \(M/aM\) inherits the quotient grading.

Take \(A=k[X,Y]\) and \(a=X\). The degree-\(n\) part of \(A/(X)\) is spanned by the class of \(Y^n\). All monomials containing \(X\) vanish in the quotient.

In the finite-module data used by sheaves, quotients retain finite generation. Submodules, kernels, and images retain finite generation over a Noetherian coefficient ring. The polynomial rings in this development satisfy that hypothesis.

## References

The local source declarations below define the constructions and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.Graded.subPiece`: [GradedModules.lean:743](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L743).

`OAI.KLInvariance.Graded.quotientPiece`: [GradedModules.lean:771](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L771).

`OAI.KLInvariance.Graded.ModuleData.sub`: [GradedModules.lean:1077](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1077).

`OAI.KLInvariance.Graded.ModuleData.quotient`: [GradedModules.lean:1089](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1089).

`OAI.KLInvariance.Graded.ModuleData.kernel`: [GradedModules.lean:1112](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1112).

`OAI.KLInvariance.Graded.ModuleData.range`: [GradedModules.lean:1117](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1117).
