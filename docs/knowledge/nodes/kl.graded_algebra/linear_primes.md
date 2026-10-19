---
id: kl.algebra.linear_primes
title: Prime linear generators and divisibility by a root line
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.linear_ideals
- kl.detail.linear_quotient
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.EdgeAlgebra.symmetric_ι_injective
  - OAI.KLInvariance.EdgeAlgebra.rootIdeal_eq_ker
  - OAI.KLInvariance.EdgeAlgebra.rootIdeal_isPrime
  - OAI.KLInvariance.EdgeAlgebra.symmetric_ι_prime
  - OAI.KLInvariance.EdgeAlgebra.symmetric_ι_dvd_iff
  - OAI.KLInvariance.EdgeAlgebra.reducedRoot_ne_zero
  - OAI.KLInvariance.EdgeAlgebra.reducedRoot_prime
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:759
    format: lean-location
    note: OAI.KLInvariance.EdgeAlgebra.symmetric_ι_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1009
    format: lean-location
    note: OAI.KLInvariance.EdgeAlgebra.rootIdeal_eq_ker
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1018
    format: lean-location
    note: OAI.KLInvariance.EdgeAlgebra.rootIdeal_isPrime
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1022
    format: lean-location
    note: OAI.KLInvariance.EdgeAlgebra.symmetric_ι_prime
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1047
    format: lean-location
    note: OAI.KLInvariance.EdgeAlgebra.symmetric_ι_dvd_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:850
    format: lean-location
    note: OAI.KLInvariance.EdgeAlgebra.reducedRoot_ne_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1030
    format: lean-location
    note: OAI.KLInvariance.EdgeAlgebra.reducedRoot_prime
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the coefficient rings, module properties and actual maps explicit?
  verdict: Read the actual root-quotient kernel, symmetric generator injectivity/primality,
    divisibility iff line membership and reducedRoot_prime. Explained the zero-vector
    divisibility case and the quotient-space proof.
tags:
- Kazhdan-Lusztig
- module-algebra
---

# Prime linear generators and divisibility by a root line

Let \(A=\operatorname{Sym}_k(V)\) for a vector space over a field. If \(a\ne0\), the linear polynomial \(\iota(a)\) is a prime element. For arbitrary \(a,v\),
\[
\iota(a)\mid\iota(v)\quad\Longleftrightarrow\quad v\in ka.
\]
If \(v\notin ka\), its class in \(A/(\iota(a))\) is nonzero and prime.

A prime element is a nonzero nonunit \(p\) such that \(p\mid fg\) implies \(p\mid f\) or \(p\mid g\).

*Proof.*

### Step 1. Prove injectivity of the linear generator map

If \(v\ne0\), choose a linear functional \(\lambda\) with \(\lambda(v)\ne0\). Its symmetric-algebra extension sends \(\iota(v)\) to \(\lambda(v)\), so \(\iota(v)\ne0\). Thus \(\iota\) is injective.

### Step 2. Prove that a nonzero linear generator is prime

The quotient theorem for \(P=ka\) gives
\[
A/(\iota(a))\simeq\operatorname{Sym}_k(V/ka),
\]
a nonzero domain. Hence \((\iota(a))\) is a proper prime ideal.

Since \(\iota(a)\ne0\), the ideal's primality is the prime-element condition: if \(\iota(a)\mid fg\), then \(fg\) lies in this ideal, so one factor lies in it and is divisible by \(\iota(a)\). Properness makes the generator a nonunit.

### Step 3. Translate divisibility into vector-space membership

Divisibility \(\iota(a)\mid\iota(v)\) means \(\iota(v)\in(\iota(a))=I_{ka}\). The [[node:kl.detail.linear_quotient|linear-membership theorem]] identifies this with \(v\in ka\).

This calculation also includes \(a=0\), when both sides express \(v=0\).

### Step 4. Identify a surviving reduced root

Under the root-quotient isomorphism, the class of \(\iota(v)\) becomes
\(\iota_{V/ka}([v])\).
If \(v\notin ka\), then \([v]\ne0\).

Apply Steps 1–2 in the vector space \(V/ka\). The resulting linear generator is nonzero and prime. Algebra isomorphisms preserve these properties, giving the assertion in the original quotient.

For \(A=k[X,Y]\) and \(a=X\), the class of \(X+Y\) is \(Y\) in \(A/(X)\simeq k[Y]\). It is a nonzero prime element there.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.EdgeAlgebra.symmetric_ι_injective`: [ReflectionSchedules.lean:759](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L759).

`OAI.KLInvariance.EdgeAlgebra.rootIdeal_eq_ker`: [ReflectionSchedules.lean:1009](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1009).

`OAI.KLInvariance.EdgeAlgebra.rootIdeal_isPrime`: [ReflectionSchedules.lean:1018](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1018).

`OAI.KLInvariance.EdgeAlgebra.symmetric_ι_prime`: [ReflectionSchedules.lean:1022](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1022).

`OAI.KLInvariance.EdgeAlgebra.symmetric_ι_dvd_iff`: [ReflectionSchedules.lean:1047](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1047).

`OAI.KLInvariance.EdgeAlgebra.reducedRoot_ne_zero`: [ReflectionSchedules.lean:850](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L850).

`OAI.KLInvariance.EdgeAlgebra.reducedRoot_prime`: [ReflectionSchedules.lean:1030](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1030).
