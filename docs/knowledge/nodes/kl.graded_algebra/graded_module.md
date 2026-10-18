---
id: kl.sheaves.graded_module
title: Finite nonnegatively graded modules
kind: definition
status: formalized
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.grading_components
lean:
  repository: openai-kl
  modules:
  - GradedModules
  declarations:
  - OAI.KLInvariance.Graded.ModuleData
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1051
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- background
---

# Finite nonnegatively graded modules

Let \(k\) be a field and let \(A=\bigoplus_{i\in\mathbb Z}A_i\) be a commutative graded \(k\)-algebra. A finite nonnegatively graded \(A\)-module consists of an \(A\)-module \(M\), a compatible \(k\)-vector-space structure, and subspaces \(M_n\subseteq M\) such that:

- every vector has a unique finite decomposition \(m=\sum_n m_n\), \(m_n\in M_n\);
- \(A_iM_j\subseteq M_{i+j}\) for all integer degrees \(i,j\);
- \(M_n=0\) whenever \(n<0\);
- finitely many vectors generate \(M\) over \(A\).

Compatibility of the scalar actions means \((ca)m=c(am)\) for \(c\in k\), \(a\in A\), \(m\in M\), where \(c\) acts on \(A\) through its algebra structure. This identifies constant-polynomial multiplication with the given vector-space multiplication.

Finite generation means there are \(m_1,\ldots,m_r\) such that every vector is \(\sum_j a_jm_j\), with coefficients \(a_j\in A\).

## Components and homogeneity

The decomposition provides component maps \(\pi_n(m)=m_n\). A vector in \(M_n\) is homogeneous of degree \(n\). A degree-zero module map preserves each \(M_n\), which makes it compatible with the component maps and with the induced gradings on kernels and images.

For \(A=k[X]\), the coefficient module \(A\) itself has \(A_n=kX^n\) for \(n\ge0\). The quotient \(A/(X)\) is generated over \(A\) by the class of one and has only its degree-zero component. Multiplication by \(X\) kills that generator.

The free module \(Ae_0\oplus Ae_2\), with generator degrees zero and two, has
\[
M_n=A_ne_0\oplus A_{n-2}e_2.
\]
This formula specifies every component, including the zero contribution from \(A_{n-2}\) when \(n<2\).

## Homogeneous generators

A finite generating family can be replaced by a finite homogeneous generating family. Decompose each generator \(m_j\) into its finitely many components and collect those components into one finite set \(T\).

The span of \(T\) contains every \(m_j\), since each original generator is the sum of its components. It therefore contains all of \(M\). Each member of \(T\) is homogeneous by construction.

For \(A=k[X_1,\ldots,X_N]\), each \(A_n\) is finite-dimensional over \(k\), because there are finitely many monomials of a fixed total degree. If the homogeneous generators have degrees \(d_j\), the map
\[
\bigoplus_j A_{n-d_j}\longrightarrow M_n,\qquad
(a_j)\longmapsto\sum_j a_jm_j
\]
is surjective: take any expression in the generators and retain its degree-\(n\) component. Hence each \(M_n\) is finite-dimensional. Its dimension is the coefficient used in the Hilbert series.

The sheaf construction uses this finite graded module data at every vertex and edge. Freeness of a stalk and the existence of a homogeneous basis are further properties established at the relevant construction steps.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

The fields `obj`, `kModule`, `tower`, `piece`, `decomposition`, `graded`, `nonneg`, and `finite` record the underlying module, scalar structures and their compatibility, graded pieces, direct-sum decomposition, graded multiplication, nonnegativity, and finite generation.

`OAI.KLInvariance.Graded.ModuleData`: [GradedModules.lean:1051](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1051).
