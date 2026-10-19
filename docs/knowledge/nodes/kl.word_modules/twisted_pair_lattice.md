---
id: kl.word.twisted_pair_lattice
title: A pair lattice with a twisted second scalar action
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.algebra.scalar_twist
- kl.algebra.pair_projection
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.ReflectionPairTranslation.lattice
  - OAI.KLInvariance.ReflectionPairTranslation.left
  - OAI.KLInvariance.ReflectionPairTranslation.left_surjective
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:2086
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.lattice
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:2127
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.left
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:2130
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.left_surjective
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the coefficient rings, module properties and actual maps explicit?
  verdict: Read lattice and its scalar-closure witness, plus left/left_surjective.
    Kept both hdiv and hinc hypotheses and wrote the correcting vector rn+m explicitly.
tags:
- Kazhdan-Lusztig
- module-algebra
---

# A pair lattice with a twisted second scalar action

Let \(R\) be a commutative ring, \(f:N\to X\) and \(g:N\to Y\) linear maps, and \(\tau:R\to R\) a ring automorphism. Let \(\alpha\in R\). Assume
\[
\alpha\mid\tau(r)-r\quad\text{for every }r\in R,
\]
and
\[
\text{for every }y\in Y,\ \text{some }m\in N
\text{ satisfies }f(m)=0,\quad g(m)=\alpha y.
\]

The twisted pair lattice is the set
\[
L=\{(f(n),g(n)):n\in N\}\subseteq X\oplus{}^\tau Y,
\]
where the scalar action is
\[
r\cdot(x,y)=(rx,\tau(r)y).
\]
Its second coordinate is the underlying vector of the twist. The two displayed assumptions make this set an \(R\)-submodule.

## Closure under addition and zero

The element \(0\in N\) represents the zero pair. If \(n,m\) represent two pairs, their sum is represented by \(n+m\), because \(f,g\) are linear.

## Closure under the twisted scalar action

Suppose \(n\) represents \((x,y)\), so \(f(n)=x\), \(g(n)=y\). For a scalar \(r\), choose \(c\) such that
\[
\tau(r)-r=\alpha c.
\]
The second assumption, applied to \(cy\), supplies \(m\) with \(f(m)=0\) and
\(g(m)=\alpha cy=(\tau(r)-r)y\).

The vector \(rn+m\) now represents the required twisted product:
\[
f(rn+m)=rx,\qquad
g(rn+m)=ry+(\tau(r)-r)y=\tau(r)y.
\]
Thus \(L\) is closed under the prescribed scalar action.

## Projection to the first coordinate

The map
\[
L\to X,\qquad (x,y)\mapsto x
\]
is \(R\)-linear because the first coordinate has its ordinary action. If \(f\) is surjective, this projection is surjective: choose \(n\) with \(f(n)=x\), and use the lattice pair \((f(n),g(n))\).

## The reflection congruence example

Take \(R=\mathbb R[\alpha]\), \(\tau(\alpha)=-\alpha\), and
\[
N=\{(x,y)\in R^2:x-y\in\alpha R\}
\]
with coordinate projections.

For every polynomial \(r\), \(\tau(r)-r\) has zero constant term and is divisible by \(\alpha\). The pair \((0,\alpha y)\) lies in \(N\), giving the second assumption.

The same congruence pairs therefore form a module for the action
\(r\cdot(x,y)=(rx,\tau(r)y)\).
This construction is the local algebra behind the twisted two-stalk coordinates in reflection translation.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ReflectionPairTranslation.lattice`: [Frobenius.lean:2086](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2086).

`OAI.KLInvariance.ReflectionPairTranslation.left`: [Frobenius.lean:2127](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2127).

`OAI.KLInvariance.ReflectionPairTranslation.left_surjective`: [Frobenius.lean:2130](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2130).
