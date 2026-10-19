---
id: kl.hecke.proper_r_kernel
title: The reversed R-kernel with its bottom term removed
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.detail.r_kernel
- kl.detail.ordinary_r
- kl.foundations.interval
- kl.hecke.polynomial_reflection
lean:
  repository: openai-kl
  modules:
  - CanonicalKL
  - OrdinaryR
  declarations:
  - OAI.KLInvariance.sum_proper_eq_sub
  - OAI.KLInvariance.CanonicalP.reversed_kernel_on_lower
  - OAI.KLInvariance.CanonicalP.reversed_kernel_on_proper
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.OrdinaryR:278
    format: lean-location
    note: OAI.KLInvariance.sum_proper_eq_sub
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:133
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.reversed_kernel_on_lower
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:149
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.reversed_kernel_on_proper
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the exact domain, degree conventions and source
    argument?
  verdict: Read reversed_kernel_on_lower/proper and sum_proper_eq_sub. Explained extension
    by zero terms to a common lower ideal, removal of incomparable indices and subtraction
    of the bottom term.
tags:
- Kazhdan-Lusztig
- Hecke
---

# The reversed R-kernel with its bottom term removed

Let \(x\le y\) and \(t\le y\). For comparable pairs write
\[
\overline R_{x,z}=\operatorname{reflect}_{d(x,z)}R_{x,z};
\]
set this value to zero outside Bruhat order. Then
\[
\sum_{x<z\le y}\overline R_{x,z}R_{z,t}
=\delta_{x,t}-R_{x,t}.
\]
Here \(\delta_{x,t}\) is one if \(x=t\) and zero otherwise.

*Proof.*

### Step 1. Extend the kernel sum to the common lower ideal

The [[node:kl.detail.r_kernel|reversed R-kernel identity]] gives
\[
\sum_{z\le t}\overline R_{x,z}R_{z,t}=\delta_{x,t}.
\]
Since \(t\le y\), every \(z\le t\) also belongs to \(L(y)\). For an extra index \(z\le y\) with \(z\not\le t\), the factor \(R_{z,t}\) is zero.

Thus adding those zero terms gives
\[
\sum_{z\le y}\overline R_{x,z}R_{z,t}=\delta_{x,t}.
\]
This places every value of \(t\le y\) on the same finite index set.

### Step 2. Restrict to indices above x

If \(x\not\le z\), then \(R_{x,z}=0\), and its reflected polynomial is zero. Therefore the terms outside \(x\le z\) vanish.

The full lower-ideal sum is consequently the sum over \(x\le z\le y\).

### Step 3. Remove the bottom contribution

Because \(x\le y\), the index \(z=x\) occurs. Its value is
\[
\overline R_{x,x}R_{x,t}
=\operatorname{reflect}_0(1)R_{x,t}
=R_{x,t}.
\]
Subtracting it from Step 1 leaves exactly the sum over \(x<z\le y\), proving the formula.

If \(t=x\), its right side is \(1-R_{x,x}=0\). If \(x<t\), it is \(-R_{x,t}\). If \(x\not\le t\), it is zero by support. These cases account for all terms when the identity is used inside a sum over \(t\in L(y)\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.sum_proper_eq_sub`: [OrdinaryR.lean:278](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L278).

`OAI.KLInvariance.CanonicalP.reversed_kernel_on_lower`: [CanonicalKL.lean:133](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L133).

`OAI.KLInvariance.CanonicalP.reversed_kernel_on_proper`: [CanonicalKL.lean:149](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L149).
