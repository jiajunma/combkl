---
id: kl.algebra.finite_graded_cover
title: A finite homogeneous free cover from arbitrary generators
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.sheaves.graded_module
- kl.algebra.module_operations
- kl.algebra.grading_components
- kl.algebra.component_transport
lean:
  repository: openai-kl
  modules:
  - GradedModules
  - HilbertSeries
  declarations:
  - OAI.KLInvariance.Graded.exists_finite_homogeneous_generators
  - OAI.KLInvariance.Hilbert.exists_finite_graded_cover
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:129
    format: lean-location
    note: OAI.KLInvariance.Graded.exists_finite_homogeneous_generators
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:178
    format: lean-location
    note: OAI.KLInvariance.Hilbert.exists_finite_graded_cover
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the grading, scalar, finiteness and convergence hypotheses retained?
  verdict: Read finite homogeneous generators and exists_finite_graded_cover. Explained
    the finite union of component supports, spanning, the exact shifted coefficient
    condition and its lower-bound consequence.
tags:
- Kazhdan-Lusztig
- graded-algebra
---

# A finite homogeneous free cover from arbitrary generators

Let \(k\) be a field and \(M\) a finitely generated module over a commutative \(k\)-algebra \(A\), with a direct-sum \(k\)-grading \(M=\bigoplus_nM_n\). Suppose the coefficient subspaces satisfy \(A_iM_j\subseteq M_{i+j}\).

There exist a finite index set \(I\), integers \(d_i\), and a surjective \(A\)-linear map
\[
f:A^I\longrightarrow M
\]
such that
\[
a_i\in A_{n-d_i}\ \text{for all }i
\quad\Longrightarrow\quad f((a_i))\in M_n.
\]
When the coefficient pieces form a grading of \(A\), this is a degree-zero surjection from the shifted free module with basis degrees \(d_i\).

*Proof.*

### Step 1. Split a finite generating family into components

Choose generators \(m_1,\ldots,m_r\) of \(M\). Each \(m_j\) has a finite homogeneous decomposition. Collect all the component vectors occurring in these finitely many decompositions into a finite set \(T\).

Each element \(v\in T\) lies in some \(M_{d(v)}\), by its construction as a component.

### Step 2. Verify that the homogeneous vectors still generate

The \(A\)-span of \(T\) contains every original \(m_j\), because \(m_j\) is a sum of its component vectors. Those \(m_j\) generate \(M\), so \(T\) generates \(M\) as well.

Use the finite set \(T\) itself as the index set \(I\). Write its indexed vectors as \(v_i\), with chosen degrees \(d_i\).

### Step 3. Define the free-cover map

Set
\[
f((a_i))=\sum_{i\in I}a_iv_i.
\]
This is \(A\)-linear by distributivity. Since the \(v_i\) span \(M\), every vector has such an expression, so \(f\) is surjective.

### Step 4. Verify the degree condition

If \(a_i\in A_{n-d_i}\) and \(v_i\in M_{d_i}\), graded scalar compatibility gives
\[
a_iv_i\in M_{(n-d_i)+d_i}=M_n.
\]
Their finite sum lies in the same subspace, proving that the map preserves the shifted degrees.

### Step 5. Obtain a lower bound over nonnegative coefficients

If the coefficient family is a nonnegative algebra grading, the shifted free source is zero in every degree smaller than all the \(d_i\). The surjective map is surjective degree by degree, by homogeneous component projection. Hence the same lower bound holds for \(M\).

When \(I\) is nonempty, the minimum of its finitely many \(d_i\) is such a bound. If \(I\) is empty, surjectivity makes \(M=0\), so every degree is zero.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Graded.exists_finite_homogeneous_generators`: [GradedModules.lean:129](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L129).

`OAI.KLInvariance.Hilbert.exists_finite_graded_cover`: [HilbertSeries.lean:178](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L178).
