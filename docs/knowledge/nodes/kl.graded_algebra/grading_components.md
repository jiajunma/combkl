---
id: kl.algebra.grading_components
title: Graded components and homogeneous projection
kind: definition
status: formalized
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses: []
lean:
  repository: openai-kl
  modules:
  - Frobenius
  - GradedModules
  - ModuleAlgebra
  declarations:
  - OAI.KLInvariance.Graded.polynomialGrading
  - OAI.KLInvariance.Graded.component
  - OAI.KLInvariance.Graded.component_smul_homogeneous
  - OAI.KLInvariance.TitsSpace.symmetricGrading
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:426
    format: lean-location
    note: OAI.KLInvariance.Graded.polynomialGrading
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:280
    format: lean-location
    note: OAI.KLInvariance.Graded.component
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:99
    format: lean-location
    note: OAI.KLInvariance.Graded.component_smul_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:777
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.symmetricGrading
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

# Graded components and homogeneous projection

An integer grading of a vector space \(M\) over a field \(k\) is a family of subspaces \(M_n\), \(n\in\mathbb Z\), such that every vector has a unique finite decomposition
\[
m=\sum_{n\in\mathbb Z}m_n,\qquad m_n\in M_n.
\]
Finite means that only finitely many terms of this particular vector are nonzero. The set of degrees occurring across the whole space can be infinite.

The degree-\(n\) component map is
\[
\pi_n:M\to M,\qquad \pi_n(m)=m_n.
\]
Uniqueness gives linearity: decompose \(m+m'\) by adding the components and decompose \(cm\) by multiplying each component by \(c\). It also gives
\[
\pi_n^2=\pi_n,\qquad \pi_n\pi_j=0\quad(n\ne j).
\]
A vector is homogeneous of degree \(n\) when it lies in \(M_n\). Its component in degree \(n\) is itself and its other components are zero.

## Algebra and module compatibility

A graded algebra has \(1\in A_0\) and \(A_iA_j\subseteq A_{i+j}\). A graded module over it satisfies \(A_iM_j\subseteq M_{i+j}\). Thus multiplying a degree-\(i\) scalar and a degree-\(j\) vector gives degree \(i+j\).

If \(m\in M_d\) and \(a=\sum_i a_i\), the terms \(a_im\) have degrees \(i+d\). Selecting degree \(n\) therefore gives
\[
\pi_n(am)=a_{n-d}m.
\]
This component formula is the basic calculation in graded generation and lifting arguments.

## The polynomial grading

In \(A=k[X_1,\ldots,X_N]\), give every variable degree one. A monomial \(X_1^{a_1}\cdots X_N^{a_N}\) has degree \(a_1+\cdots+a_N\). The subspace \(A_n\) consists of linear combinations of degree-\(n\) monomials.

For example,
\[
f=3+2X+Y+XY+X^3
\]
has components \(f_0=3\), \(f_1=2X+Y\), \(f_2=XY\), and \(f_3=X^3\). Every other component vanishes. A monomial has nonnegative degree, so \(A_n=0\) for \(n<0\), and \(A_0=k\).

The symmetric-algebra grading is transported through a chosen polynomial-coordinate isomorphism. A symmetric-algebra element belongs to degree \(n\) precisely when its coordinate polynomial belongs to \(A_n\). This gives the grading used on word modules before changing to polynomial coordinates.

## References

The local source declarations below define the constructions and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.Graded.polynomialGrading`: [GradedModules.lean:426](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L426).

`OAI.KLInvariance.Graded.component`: [ModuleAlgebra.lean:280](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L280).

`OAI.KLInvariance.Graded.component_smul_homogeneous`: [GradedModules.lean:99](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L99).

`OAI.KLInvariance.TitsSpace.symmetricGrading`: [Frobenius.lean:777](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L777).
