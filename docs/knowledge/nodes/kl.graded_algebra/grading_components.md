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
  - GradedModules
  - ModuleAlgebra
  declarations:
  - OAI.KLInvariance.Graded.polynomialGrading
  - OAI.KLInvariance.Graded.component
  - OAI.KLInvariance.Graded.component_smul_homogeneous
  - OAI.KLInvariance.Graded.polynomialGrading_negative
  - OAI.KLInvariance.Graded.polynomialGrading_zero
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
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:437
    format: lean-location
    note: OAI.KLInvariance.Graded.polynomialGrading_negative
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:452
    format: lean-location
    note: OAI.KLInvariance.Graded.polynomialGrading_zero
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

An integer grading of a module \(M\) over a commutative ring \(k\) is a family of submodules \(M_n\), \(n\in\mathbb Z\), such that every vector has a unique finite decomposition
\[
m=\sum_{n\in\mathbb Z}m_n,\qquad m_n\in M_n.
\]
Each vector has finitely many nonzero components. The set of degrees occurring across the module can be infinite. When \(k\) is a field, the pieces are vector subspaces.

The degree-\(n\) component map is
\[
\pi_n:M\to M,\qquad \pi_n(m)=m_n.
\]
Uniqueness gives linearity: decompose \(m+m'\) by adding the components and decompose \(cm\) by multiplying each component by \(c\). It also gives
\[
\pi_n^2=\pi_n,\qquad \pi_n\pi_j=0\quad(n\ne j).
\]
A vector is homogeneous of degree \(n\) when it lies in \(M_n\). Its component in degree \(n\) is itself and its other components are zero.

A grading is nonnegative if \(M_n=0\) for \(n<0\), and bounded below if some integer \(d_0\) satisfies \(M_n=0\) for all \(n<d_0\).

## Algebra and module compatibility

Applying the decomposition to an algebra \(A\) gives a graded algebra when \(1\in A_0\) and \(A_iA_j\subseteq A_{i+j}\). For an \(A\)-module \(M\) with compatible \(k\)-scalar action, a module grading also satisfies \(A_iM_j\subseteq M_{i+j}\). Thus multiplying a degree-\(i\) scalar and a degree-\(j\) vector gives degree \(i+j\).

If \(m\in M_d\) and \(a=\sum_i a_i\), the terms \(a_im\) have degrees \(i+d\). Selecting degree \(n\) therefore gives
\[
\pi_n(am)=a_{n-d}m.
\]
This component formula is the basic calculation in graded generation and lifting arguments.

## The polynomial grading

For a field \(k\), the polynomial grading gives each variable degree one. For \(A=k[X_i:i\in I]\), an exponent vector has finite support; the degree of its monomial is the sum of its nonnegative exponents. In a finite list of variables, a monomial \(X_1^{a_1}\cdots X_N^{a_N}\) has degree \(a_1+\cdots+a_N\). The subspace \(A_n\) consists of linear combinations of degree-\(n\) monomials.

For example,
\[
f=3+2X+Y+XY+X^3
\]
has components \(f_0=3\), \(f_1=2X+Y\), \(f_2=XY\), and \(f_3=X^3\). Every other component vanishes. A monomial has nonnegative degree, so \(A_n=0\) for \(n<0\), and \(A_0=k\).

The [[node:kl.algebra.coefficient_algebra|symmetric coefficient algebra]] transports this polynomial grading through a chosen coordinate isomorphism. Its construction is explained with that algebra.

## References

The local source declarations below define the constructions and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.Graded.polynomialGrading`: [GradedModules.lean:426](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L426).

`OAI.KLInvariance.Graded.component`: [ModuleAlgebra.lean:280](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L280).

`OAI.KLInvariance.Graded.component_smul_homogeneous`: [GradedModules.lean:99](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L99).

`OAI.KLInvariance.Graded.polynomialGrading_negative`: [GradedModules.lean:437](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L437).

`OAI.KLInvariance.Graded.polynomialGrading_zero`: [GradedModules.lean:452](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L452).
