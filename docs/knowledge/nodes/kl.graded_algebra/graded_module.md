---
id: kl.sheaves.graded_module
title: Finite nonnegatively graded module data
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
  prompt: Are the grading, scalar, finiteness and convergence hypotheses retained?
  verdict: Read all eight ModuleData fields and its parameter context. Explained the
    scalar tower, finite decomposition versus finite A-generation, and the separate
    coefficient-family input.
tags:
- Kazhdan-Lusztig
- graded-algebra
---

# Finite nonnegatively graded module data

Fix a commutative \(k\)-algebra \(A\), with \(k\) a field, and an integer-indexed family of coefficient subspaces \(A_i\). The local structure ModuleData packages a module \(M\) with the following eight fields.

| Field | Mathematical content |
|---|---|
| `obj` | The additive group and \(A\)-module \(M\). |
| `kModule` | A \(k\)-vector-space structure on the same vectors. |
| `tower` | Compatibility of the \(k\)- and \(A\)-scalar actions. |
| `piece` | A \(k\)-subspace \(M_n\subseteq M\) for every \(n\in\mathbb Z\). |
| `decomposition` | Every vector has a unique finite sum of components in the \(M_n\). |
| `graded` | \(A_iM_j\subseteq M_{i+j}\). |
| `nonneg` | \(M_n=0\) whenever \(n<0\). |
| `finite` | Finitely many vectors generate \(M\) over \(A\). |

When the \(A_i\) form a graded algebra, these are finite nonnegatively graded \(A\)-modules. The structure takes the coefficient family as a parameter; its decomposition field concerns the module pieces.

## The scalar tower

For \(c\in k\), \(a\in A\), and \(m\in M\), compatibility says
\[
(c\cdot_Aa)\cdot_Mm=c\cdot_M(a\cdot_Mm).
\]
Taking \(a=1\) identifies multiplication by the coefficient \(c\,1_A\) with the given \(k\)-scalar action. This makes \(A\)-linear maps \(k\)-linear by restriction of scalars.

## Finite decompositions and generators

Write \(\pi_n(m)\) for the degree-\(n\) component. Only finitely many components of each fixed vector are nonzero, and
\[
m=\sum_n\pi_n(m),\qquad \pi_n(m)\in M_n.
\]
The decomposition is unique.

Finite generation means that some \(m_1,\ldots,m_r\) satisfy
\[
m=\sum_{j=1}^r a_jm_j\qquad(a_j\in A)
\]
for every \(m\in M\). For example, \(A=k[X]\) is generated over itself by \(1\), while its vectors \(1,X,X^2,\ldots\) are linearly independent over \(k\).

A [[node:kl.algebra.finite_graded_cover|finite homogeneous-cover theorem]] replaces an arbitrary finite generating family by homogeneous components and constructs a surjection from a finite shifted free module. Over a finite-variable polynomial ring, this also proves that each \(M_n\) is finite-dimensional over \(k\).

## Two examples

For \(A=k[X]\), the coefficient module \(A\) has \(A_n=kX^n\) for \(n\ge0\).

The quotient \(A/(X)\) has one generator, the class of \(1\), in degree zero. Multiplication by \(X\) kills it, and all positive-degree pieces vanish.

The free module \(Ae_0\oplus Ae_2\), with generator degrees zero and two, has
\[
M_n=A_ne_0\oplus A_{n-2}e_2.
\]
The second summand contributes zero when \(n<2\). Its dimensions over \(k\) are \(1,1,2,2,\ldots\).

The sheaf constructions use this module data at vertices and edges. Freeness and the choice of a homogeneous basis are additional properties used in the character formulas.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Graded.ModuleData`: [GradedModules.lean:1051](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1051).
