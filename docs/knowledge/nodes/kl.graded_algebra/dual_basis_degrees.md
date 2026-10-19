---
id: kl.algebra.dual_basis_degrees
title: Degrees of coefficients and dual basis functionals
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.homogeneous_basis
- kl.detail.graded_maps_shifts
lean:
  repository: openai-kl
  modules:
  - Support
  declarations:
  - OAI.KLInvariance.Graded.homogeneous_basis_repr
  - OAI.KLInvariance.Graded.dualBasis_homogeneous
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:709
    format: lean-location
    note: OAI.KLInvariance.Graded.homogeneous_basis_repr
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:724
    format: lean-location
    note: OAI.KLInvariance.Graded.dualBasis_homogeneous
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- duality_and_characters
---

# Degrees of coefficients and dual basis functionals

Let \(A=\bigoplus_{n\in\mathbb Z}A_n\) be a graded commutative algebra over a field \(k\), and let \(M=\bigoplus_n M_n\) be a graded \(A\)-module. Choose a finite \(A\)-basis \((b_i)_{i\in J}\) with \(b_i\in M_{d_i}\), where \(d_i\in\mathbb Z\).

Write \(b_i^*:M\to A\) for the coordinate functional:
\[
v=\sum_{i\in J}b_i^*(v)b_i.
\]
If \(v\in M_n\), then
\[
b_i^*(v)\in A_{n-d_i}.
\]
Thus \(b_i^*\) is a homogeneous functional of degree \(-d_i\).

*Proof.*

### Step 1. Decompose the coefficients

Write \(v=\sum_i a_i b_i\), and decompose each coefficient as \(a_i=\sum_r(a_i)_r\). There are finitely many \(i\), and each coefficient has finite degree support, so this is a finite sum of homogeneous vectors.

Since \((a_i)_r b_i\) has degree \(r+d_i\), its contribution to total degree \(m\) comes from \(r=m-d_i\). Consequently the degree-\(m\) component of \(v\) is
\[
v_m=\sum_i(a_i)_{m-d_i}b_i.
\]

### Step 2. Eliminate every other coefficient degree

The vector \(v\) lies in \(M_n\), so \(v_m=0\) for every \(m\ne n\). Basis independence applied to the preceding sum gives
\[
(a_i)_{m-d_i}=0\qquad(i\in J,\ m\ne n).
\]
For fixed \(i\), every integer \(r\ne n-d_i\) has the form \(r=m-d_i\) with \(m\ne n\). All those components of \(a_i\) vanish. Hence \(a_i\in A_{n-d_i}\).

### Step 3. Identify the dual degree

By definition \(b_i^*(v)=a_i\). Therefore
\[
b_i^*(M_n)\subseteq A_{n+(-d_i)}
\]
for every \(n\), which is exactly the degree-\(-d_i\) condition.

For example, let \(M=Ae_0\oplus Ae_2\), with basis degrees zero and two. A homogeneous degree-\(n\) vector is \(a e_0+c e_2\), with \(a\in A_n\) and \(c\in A_{n-2}\). The two coordinate functionals consequently have degrees zero and \(-2\).

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.Graded.homogeneous_basis_repr`: [Support.lean:709](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L709).

`OAI.KLInvariance.Graded.dualBasis_homogeneous`: [Support.lean:724](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L724).
