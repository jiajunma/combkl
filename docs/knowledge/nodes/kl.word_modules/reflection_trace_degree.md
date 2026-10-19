---
id: kl.word.reflection_trace_degree
title: The reflection trace lowers degree by one
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.reflection_trace
- kl.algebra.scalar_inverse_degree
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.ReflectionFrobenius.trace_difference
  - OAI.KLInvariance.ReflectionFrobenius.trace_homogeneous
  - OAI.KLInvariance.ReflectionFrobenius.coordinates_homogeneous
  - OAI.KLInvariance.ReflectionFrobenius.reflectionBasis_homogeneous
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:456
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.trace_difference
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:464
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.trace_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:483
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.coordinates_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:533
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.reflectionBasis_homogeneous
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read trace_difference, trace_homogeneous and coordinates_homogeneous. Expanded
    homogeneous component cancellation and separated the extra unit-degree condition
    for reflectionBasis_homogeneous.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# The reflection trace lowers degree by one

Let \(k\) be a characteristic-zero field, \(A\) a commutative domain over \(k\), and \((\tau,\alpha)\) reflection data with fixed algebra \(R=A^\tau\). Suppose
\[
A=\bigoplus_{n\in\mathbb Z} A_n,\qquad A_iA_j\subseteq A_{i+j},
\]
where the pieces are \(k\)-subspaces. Assume \(\alpha\in A_1\) and \(\tau(A_n)\subseteq A_n\) for every \(n\).

For homogeneous \(a\in A_n\), its reflection coordinates satisfy
\[
a=a_0+\alpha a_1,\qquad
a_0\in R\cap A_n,\qquad a_1=t(a)\in R\cap A_{n-1}.
\]
When \(1\in A_0\), the reflection basis \(1,\alpha\) has degrees \(0,1\).

*Proof.*

### Step 1. Express the trace by a homogeneous product

Applying \(\tau\) to the coordinate expansion gives
\(\tau(a)=a_0-\alpha a_1\). Subtracting yields
\[
2\alpha t(a)=a-\tau(a).
\]
The automorphism preserves \(A_n\). Since \(A_n\) is a \(k\)-subspace, both the difference and its half belong to \(A_n\). Thus
\[
\alpha t(a)=\frac12(a-\tau(a))\in A_n.
\]

### Step 2. Recover the degree of the trace

The [[node:kl.algebra.scalar_inverse_degree|homogeneous-scalar cancellation theorem]] applies to the nonzero homogeneous scalar \(\alpha\in A_1\). It gives \(t(a)\in A_{n-1}\).

Concretely, write \(t(a)=\sum_j c_j\), with \(c_j\in A_j\) and finite support. Then \(\alpha c_j\in A_{j+1}\). Uniqueness of homogeneous components in the equality \(\alpha t(a)\in A_n\) gives \(\alpha c_j=0\) for \(j+1\ne n\). Cancellation of \(\alpha\) gives \(c_j=0\) for these indices, leaving only \(c_{n-1}\). This also covers the zero trace value.

### Step 3. Recover the degree of the first coordinate

From the expansion,
\[
a_0=a-\alpha t(a).
\]
Both terms on the right lie in \(A_n\), so \(a_0\in A_n\). The coordinate construction already places \(a_0,t(a)\) in \(R\).

### Step 4. Read off the basis degrees

The source identifies reflectionBasis at indices \(0,1\) with \(1,\alpha\). The additional hypothesis \(1\in A_0\) and the given \(\alpha\in A_1\) supply their degrees.

For \(A=k[X]\) with \(\deg X=1\), the trace sends \(X^{2m}\) to zero and \(X^{2m+1}\) to \(X^{2m}\). Each nonzero image lowers degree by one, illustrating the general formula.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ReflectionFrobenius.trace_difference`: [Frobenius.lean:456](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L456).

`OAI.KLInvariance.ReflectionFrobenius.trace_homogeneous`: [Frobenius.lean:464](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L464).

`OAI.KLInvariance.ReflectionFrobenius.coordinates_homogeneous`: [Frobenius.lean:483](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L483).

`OAI.KLInvariance.ReflectionFrobenius.reflectionBasis_homogeneous`: [Frobenius.lean:533](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L533).
