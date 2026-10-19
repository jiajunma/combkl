---
id: kl.word.reflection_algebra_action
title: A linear reflection induces Frobenius data on its symmetric algebra
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.invariant_subalgebra
- kl.notes.reflection_frobenius
- kl.algebra.linear_ideals
lean:
  repository: openai-kl
  modules:
  - Decomposition
  declarations:
  - OAI.KLInvariance.ReflectionFrobenius.symmetricMap
  - OAI.KLInvariance.ReflectionFrobenius.symmetricAction
  - OAI.KLInvariance.ReflectionFrobenius.symmetricAction_ι
  - OAI.KLInvariance.ReflectionFrobenius.reflectionAction
  - OAI.KLInvariance.ReflectionFrobenius.reflectionAction_involutive
  - OAI.KLInvariance.ReflectionFrobenius.reflectionAction_anti
  - OAI.KLInvariance.ReflectionFrobenius.reflectionRoot_ne_zero
  - OAI.KLInvariance.ReflectionFrobenius.reflectionAction_divisible
  - OAI.KLInvariance.ReflectionFrobenius.reflectionDuality
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1604
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.symmetricMap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1627
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.symmetricAction
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1633
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.symmetricAction_ι
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1639
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.reflectionAction
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1643
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.reflectionAction_involutive
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1654
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.reflectionAction_anti
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1660
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.reflectionRoot_ne_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1667
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.reflectionAction_divisible
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1687
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.reflectionDuality
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read the symmetric-algebra lift and all four divisibility induction cases.
    Verified the root-coroot normalization, nonzero generator via the lifted functional,
    and the absence of a finite-dimensional hypothesis.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# A linear reflection induces Frobenius data on its symmetric algebra

Let \(V\) be a vector space over a characteristic-zero field \(k\). Choose a vector \(r\in V\) and a linear functional \(\varphi:V\to k\) with \(\varphi(r)=2\). Put
\[
s(v)=v-\varphi(v)r,\qquad
A=\operatorname{Sym}_k(V),\qquad \alpha=\iota(r),
\]
where \(\iota:V\to A\) is the symmetric-algebra generator map.

The linear reflection induces a \(k\)-algebra automorphism \(\tau\) determined by
\[
\tau(\iota(v))=\iota(s(v)).
\]
It satisfies
\[
\tau^2=1,\qquad \alpha\ne0,\qquad \tau(\alpha)=-\alpha,\qquad
\alpha\mid a-\tau(a)\quad(a\in A).
\]
Thus \(A^\tau\to A\) has the reflection coordinates and perfect trace pairing.

*Proof.*

### Step 1. Construct the involution on generators

The root-coroot normalization gives
\[
\varphi(s(v))=\varphi(v)-\varphi(v)\varphi(r)=-\varphi(v).
\]
Therefore
\[
s(s(v))=v-\varphi(v)r+\varphi(v)r=v.
\]
The symmetric-algebra universal property extends the linear map \(\iota\circ s\) to an algebra homomorphism \(\tau:A\to A\).

On each generator, \(\tau^2(\iota(v))=\iota(s^2(v))=\iota(v)\), and \(\tau\) fixes scalar constants. Since these generate \(A\), \(\tau^2=1\). It follows that \(\tau\) is an automorphism with inverse itself.

### Step 2. Check the root polynomial

The identity \(\varphi(r)=2\) gives \(s(r)=r-2r=-r\), so
\[
\tau(\alpha)=\iota(-r)=-\alpha.
\]
To prove \(\alpha\ne0\), extend \(\varphi\) to an algebra map \(F:A\to k\). Then \(F(\alpha)=\varphi(r)=2\). If \(\alpha=0\), this would give \(2=0\) in \(k\), contradicting characteristic zero.

### Step 3. Prove divisibility on constants and generators

For a constant \(c\in k\), the difference is zero because \(\tau(c)=c\). For a vector generator,
\[
\iota(v)-\tau(\iota(v))
=\iota(v)-\iota(v-\varphi(v)r)
=\varphi(v)\alpha.
\]
Both differences are multiples of \(\alpha\).

### Step 4. Extend divisibility through polynomial operations

If
\(a-\tau(a)=\alpha c\) and \(b-\tau(b)=\alpha d\), then
\[
(a+b)-\tau(a+b)=\alpha(c+d).
\]
For a product, insert and subtract \(\tau(a)b\):
\[
\begin{aligned}
ab-\tau(ab)
&=(a-\tau(a))b+\tau(a)(b-\tau(b))\\
&=\alpha\bigl(cb+\tau(a)d\bigr).
\end{aligned}
\]
Every symmetric-algebra element is built from constants and vector generators by addition and multiplication. Structural induction using Steps 3–4 proves divisibility for every \(a\in A\). These are the four cases of the source's reflectionAction_divisible proof.

### Step 5. Apply the reflection trace construction

A basis of \(V\) identifies \(\operatorname{Sym}_k(V)\) with a polynomial algebra, so \(A\) is a commutative domain. Steps 1–4 supply the remaining hypotheses of the [[node:kl.notes.reflection_frobenius|reflection Frobenius theorem]].

Its basis \(1,\alpha\), coordinate trace and trace duality now apply to the actual induced reflection. This is the source's reflectionDuality construction. The argument permits an arbitrary-dimensional \(V\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ReflectionFrobenius.symmetricMap`: [Decomposition.lean:1604](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1604).

`OAI.KLInvariance.ReflectionFrobenius.symmetricAction`: [Decomposition.lean:1627](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1627).

`OAI.KLInvariance.ReflectionFrobenius.symmetricAction_ι`: [Decomposition.lean:1633](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1633).

`OAI.KLInvariance.ReflectionFrobenius.reflectionAction`: [Decomposition.lean:1639](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1639).

`OAI.KLInvariance.ReflectionFrobenius.reflectionAction_involutive`: [Decomposition.lean:1643](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1643).

`OAI.KLInvariance.ReflectionFrobenius.reflectionAction_anti`: [Decomposition.lean:1654](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1654).

`OAI.KLInvariance.ReflectionFrobenius.reflectionRoot_ne_zero`: [Decomposition.lean:1660](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1660).

`OAI.KLInvariance.ReflectionFrobenius.reflectionAction_divisible`: [Decomposition.lean:1667](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1667).

`OAI.KLInvariance.ReflectionFrobenius.reflectionDuality`: [Decomposition.lean:1687](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1687).
