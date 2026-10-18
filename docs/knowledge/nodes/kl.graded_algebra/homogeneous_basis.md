---
id: kl.algebra.homogeneous_basis
title: Finite homogeneous bases and their degrees
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
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.Graded.NonnegativeBasis
  - OAI.KLInvariance.Graded.NonnegativeBasis.polynomial
  - OAI.KLInvariance.Graded.shiftedPiece
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:20
    format: lean-location
    note: OAI.KLInvariance.Graded.NonnegativeBasis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:47
    format: lean-location
    note: OAI.KLInvariance.Graded.NonnegativeBasis.polynomial
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:813
    format: lean-location
    note: OAI.KLInvariance.Graded.shiftedPiece
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

# Finite homogeneous bases and their degrees

Let \(A=k[X_1,\ldots,X_N]\) have variables in degree one, and let \(M=\bigoplus_nM_n\) be an \(A\)-module graded in nonnegative degrees. A finite nonnegative homogeneous basis consists of:

- a finite index set \(J\);
- an \(A\)-basis \((b_j)_{j\in J}\) of \(M\);
- a degree \(d_j\in\mathbb N\) for each index;
- the condition \(b_j\in M_{d_j}\).

Being a basis means that every \(m\in M\) has a unique expression \(\sum_j a_jb_j\) with \(a_j\in A\). Homogeneity specifies how this free-module description interacts with the grading.

## The coefficient test for degree

A vector \(\sum_j a_jb_j\) is homogeneous of degree \(n\) exactly when
\[
a_j\in A_{n-d_j}\quad\text{for every }j.
\]
For the forward implication, decompose every \(a_j\) into homogeneous parts. The part of total degree \(m\) is \(\sum_j(a_j)_{m-d_j}b_j\). If the vector belongs to degree \(n\), all these sums vanish for \(m\ne n\). Basis independence forces each coefficient in those sums to vanish. Thus only the degrees \(n-d_j\) remain in \(a_j\).

The reverse implication follows directly from \(A_{n-d_j}M_{d_j}\subseteq M_n\).

Consequently
\[
M_n\simeq\bigoplus_{j\in J}A_{n-d_j}
\]
as vector spaces over \(k\). This is the degreewise decomposition behind the Hilbert formula.

## Basis degrees and shifted free modules

If \(M=Ae_0\oplus Ae_2\), with degrees zero and two, then
\[
M_n=A_ne_0\oplus A_{n-2}e_2.
\]
For \(A=k[\alpha]\), the dimensions in degrees \(0,1,2,3,\ldots\) are \(1,1,2,2,\ldots\).

The basis-degree polynomial is
\[
\sum_{j\in J}q^{d_j}.
\]
It is \(1+q^2\) in this example. Its degree-\(n\) coefficient counts basis vectors of degree \(n\).

The homogeneous-basis existence theorem supplies such a basis for the finite nonnegative graded free modules used here. The graded-character entry proves that the resulting polynomial is independent of the chosen homogeneous basis.

## References

The local source declarations below define the constructions and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.Graded.NonnegativeBasis`: [SheafMorphisms.lean:20](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L20).

`OAI.KLInvariance.Graded.NonnegativeBasis.polynomial`: [SheafMorphisms.lean:47](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L47).

`OAI.KLInvariance.Graded.shiftedPiece`: [GradedModules.lean:813](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L813).

The fields `index`, `finite`, `basis`, `degree`, and `homogeneous` record the index set, its finiteness, the free basis, its degrees, and the degree-membership conditions described above.
