---
id: kl.algebra.scalar_inverse_degree
title: Cancelling a homogeneous scalar recovers the input degree
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.grading_components
lean:
  repository: openai-kl
  modules:
  - Support
  declarations:
  - OAI.KLInvariance.Graded.mem_of_homogeneous_smul
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1523
    format: lean-location
    note: OAI.KLInvariance.Graded.mem_of_homogeneous_smul
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

# Cancelling a homogeneous scalar recovers the input degree

Let \(M=\bigoplus_j M_j\) be a graded module over a graded algebra \(A\). Let \(a\in A_d\), and suppose multiplication by \(a\) on \(M\) is injective. If \(am\in M_n\), then
\[
m\in M_{n-d}.
\]

*Proof.*

### Step 1. Take the required component

Write \(m=\sum_j m_j\). The product \(am_j\) lies in \(M_{d+j}\), so the degree-\(n\) component of \(am\) is \(a m_{n-d}\).

Since \(am\) is homogeneous of degree \(n\), its degree-\(n\) component equals \(am\). Hence
\[
a m_{n-d}=am.
\]

### Step 2. Use injectivity

Injectivity of multiplication by \(a\) gives \(m_{n-d}=m\). The left side lies in \(M_{n-d}\), proving the result.

For a free module over a polynomial domain, every nonzero scalar acts injectively by cancellation in basis coordinates. In particular, a nonzero product of \(d\) degree-one edge labels raises each degree by \(d\), and this theorem recovers the original degree when the product is removed.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.Graded.mem_of_homogeneous_smul`: [Support.lean:1523](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1523).
