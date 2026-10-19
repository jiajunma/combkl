---
id: kl.word.invariant_subalgebra
title: The fixed subalgebra and reflection data
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses: []
lean:
  repository: openai-kl
  modules:
  - Decomposition
  declarations:
  - OAI.KLInvariance.ReflectionFrobenius.fixed
  - OAI.KLInvariance.ReflectionFrobenius.mem_fixed
  - OAI.KLInvariance.ReflectionFrobenius.fixed_val
  - OAI.KLInvariance.ReflectionFrobenius.expand
  - OAI.KLInvariance.ReflectionFrobenius.expand_apply
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1435
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.fixed
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1439
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.mem_fixed
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1443
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.fixed_val
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1447
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.expand
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1454
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.expand_apply
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read fixed, membership and expansion with their surrounding reflection
    hypotheses. Separated the general equalizer definition from the domain/characteristic-zero
    conditions used to prove its two-coordinate decomposition.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# The fixed subalgebra and reflection data

Let \(A\) be a commutative algebra over a field \(k\), and let \(\tau:A\to A\) be a \(k\)-algebra automorphism. Its fixed subalgebra is
\[
A^\tau=\{a\in A:\tau(a)=a\}.
\]
It contains the scalar image of \(k\) because \(\tau\) is a \(k\)-algebra map. It is closed under addition, multiplication, negation and scalar multiplication: for example, if \(\tau(a)=a\) and \(\tau(b)=b\), then
\[
\tau(ab)=\tau(a)\tau(b)=ab.
\]
Write \(R=A^\tau\). The \(R\)-action on \(A\) is multiplication by the included element. The source defines \(R\) as `fixed`, the equalizer of \(\tau\) and the identity.

## Reflection data for the two-coordinate construction

The [[node:kl.word.reflection_coordinates|reflection coordinate theorem]] uses a characteristic-zero field \(k\), a commutative domain \(A\) over \(k\), and the following data:
\[
\tau^2=1,\qquad
\alpha\in A,\quad \alpha\ne0,\qquad
\tau(\alpha)=-\alpha,\qquad
\alpha\mid a-\tau(a)\ \text{for every }a\in A.
\]
The last condition means that, for each \(a\), an element \(d\in A\) satisfies
\(a-\tau(a)=\alpha d\). The source names these conditions `hinv`, `hα`, `hanti` and `hdiv`.

An invariant element satisfies \(\tau(a)=a\); an anti-invariant element satisfies \(\tau(a)=-a\). Multiplying an invariant element by \(\alpha\) gives an anti-invariant element.

## The expansion map

Define the \(R\)-linear map
\[
E:R\oplus R\longrightarrow A,\qquad E(c_0,c_1)=c_0+\alpha c_1.
\]
For \(r\in R\),
\[
E(rc_0,rc_1)=r(c_0+\alpha c_1),
\]
which is its scalar-linearity identity. Reflection coordinates prove that \(E\) is an isomorphism and define its inverse. The two standard coordinate vectors then become the basis \(1,\alpha\) of \(A\) over \(R\).

For \(A=k[X,Y]\) with \(\tau(X)=-X\) and \(\tau(Y)=Y\), the fixed algebra is \(k[X^2,Y]\). Separating even and odd powers of \(X\) is the expansion \(E\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ReflectionFrobenius.fixed`: [Decomposition.lean:1435](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1435).

`OAI.KLInvariance.ReflectionFrobenius.mem_fixed`: [Decomposition.lean:1439](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1439).

`OAI.KLInvariance.ReflectionFrobenius.fixed_val`: [Decomposition.lean:1443](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1443).

`OAI.KLInvariance.ReflectionFrobenius.expand`: [Decomposition.lean:1447](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1447).

`OAI.KLInvariance.ReflectionFrobenius.expand_apply`: [Decomposition.lean:1454](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1454).
