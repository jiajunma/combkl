---
id: kl.algebra.local_diagonal_bound
title: Positive-ideal coordinates and strict diagonal degree
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.positive_ideal
- kl.algebra.augmentation_kernel
- kl.algebra.dual_basis_degrees
lean:
  repository: openai-kl
  modules:
  - EdgeLocalization
  declarations:
  - OAI.KLInvariance.Graded.homogeneous_positive_nonzero
  - OAI.KLInvariance.Graded.dual_mem_ideal
  - OAI.KLInvariance.Graded.local_diagonal_strict_degree
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:1043
    format: lean-location
    note: OAI.KLInvariance.Graded.homogeneous_positive_nonzero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:1060
    format: lean-location
    note: OAI.KLInvariance.Graded.dual_mem_ideal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:1077
    format: lean-location
    note: OAI.KLInvariance.Graded.local_diagonal_strict_degree
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read all three generic EdgeLocalization lemmas. Kept integer basis degrees,
    a nonnegative coefficient grading, the finite homogeneous basis and the exact
    range/nonzero hypotheses; no domain, symmetry or polynomial-ring hypothesis is
    added.
tags:
- Kazhdan-Lusztig
- graded-duality
---

# Positive-ideal coordinates and strict diagonal degree

Let \(k\) be a field and \(A=\bigoplus_{n\in\mathbb Z}A_n\) a commutative graded \(k\)-algebra, with \(A_n=0\) for \(n<0\). Let \(M=\bigoplus_nM_n\) be a graded \(A\)-module with a finite homogeneous \(A\)-basis \((m_i)\), where \(m_i\in M_{d_i}\) and \(d_i\in\mathbb Z\). Write \(\lambda_i=m_i^*\) for its dual basis.

Suppose \(D\in\mathbb Z\) and an \(A\)-linear map
\[
Q:\operatorname{Hom}_A(M,A)\longrightarrow M
\]
satisfy
\[
Q(\lambda_i)\in M_{D-d_i}\quad\text{for every }i,
\qquad
\operatorname{im}Q\subseteq A_+M.
\]
For a specified index \(i\), the hypothesis
\[
a_{ii}:=\lambda_i(Q(\lambda_i))\ne0
\]
implies
\[
2d_i<D.
\]

*Proof.*

### Step 1. Evaluate an ideal multiple by a linear functional

For any ideal \(J\subseteq A\), a vector \(v\in JM\) is a finite sum
\[
v=\sum_r a_rv_r,\qquad a_r\in J,\quad v_r\in M.
\]
An \(A\)-linear functional \(f\) gives
\[
f(v)=\sum_r a_rf(v_r).
\]
Each term lies in \(J\), and \(J\) is closed under addition. Hence \(f(v)\in J\). This is the source's dual_mem_ideal.

In particular, \(Q(\lambda_i)\in A_+M\) implies \(a_{ii}\in A_+\).

### Step 2. Compute the homogeneous degree of a coordinate

The [[node:kl.algebra.dual_basis_degrees|dual-basis degree theorem]] says
\[
\lambda_i(M_n)\subseteq A_{n-d_i}.
\]
Apply it to \(Q(\lambda_i)\in M_{D-d_i}\):
\[
a_{ii}\in A_{D-d_i-d_i}=A_{D-2d_i}.
\]

More generally, the matrix coefficient \(a_{ij}=\lambda_i(Q(\lambda_j))\) lies in \(A_{D-d_j-d_i}\), and Step 1 puts it in \(A_+\). This follows from the same coordinate calculation.

### Step 3. Detect positive degree

Let \(a\ne0\) be homogeneous of degree \(n\) and belong to \(A_+\). If \(n<0\), then \(A_n=0\), contradicting \(a\ne0\).

If \(n=0\), the augmentation is the degree-zero projection, so \(\epsilon(a)=a\). But the [[node:kl.algebra.augmentation_kernel|augmentation-kernel theorem]] gives \(A_+=\ker\epsilon\), hence \(\epsilon(a)=0\), again a contradiction.

Thus \(n>0\). This is homogeneous_positive_nonzero.

### Step 4. Apply positivity to the diagonal coefficient

The specified \(a_{ii}\) is nonzero by hypothesis, homogeneous of degree \(D-2d_i\) by Step 2, and in \(A_+\) by Step 1. Step 3 gives
\[
D-2d_i>0.
\]
Rearranging proves \(2d_i<D\).

### Step 5. Calculate a rank-one example

As an illustrative graded-module calculation, take \(A=k[\alpha]\), \(\deg\alpha=1\), \(M=Ae\) with \(\deg e=r\in\mathbb Z\), and let \(\lambda(e)=1\). Choose
\[
Q(\lambda)=\alpha^s e,\qquad s\in\mathbb N,\ s>0.
\]
Its image is contained in \(A_+M\). The homogeneity condition has \(D=2r+s\), since \(Q(\lambda)\) has degree \(r+s=D-r\). The diagonal coefficient is \(\alpha^s\), and the conclusion is \(2r<2r+s\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Graded.homogeneous_positive_nonzero`: [EdgeLocalization.lean:1043](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L1043).

`OAI.KLInvariance.Graded.dual_mem_ideal`: [EdgeLocalization.lean:1060](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L1060).

`OAI.KLInvariance.Graded.local_diagonal_strict_degree`: [EdgeLocalization.lean:1077](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L1077).
