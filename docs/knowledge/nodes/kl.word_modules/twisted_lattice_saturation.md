---
id: kl.word.twisted_lattice_saturation
title: Saturation of a twisted pair lattice from quotient regularity
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.twisted_pair_lattice
- kl.algebra.pair_projection
- kl.algebra.scalar_quotient
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.ReflectionPairTranslation.lattice_saturated
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:2106
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.lattice_saturated
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the coefficient rings, module properties and actual maps explicit?
  verdict: Read lattice_saturated and PairProjection.compatible_iff. Expanded the
    twisted scalar equation, annihilation of the scalar difference, cancellation on
    the quotient and reconstruction of a common preimage.
tags:
- Kazhdan-Lusztig
- module-algebra
---

# Saturation of a twisted pair lattice from quotient regularity

Use the twisted pair lattice \(L\subseteq X\oplus{}^\tau Y\), with its two defining assumptions. Let \(Q\) be the pair-projection quotient of \(f,g\), with maps \(\ell:X\to Q\), \(u:Y\to Q\).

Assume \(\alpha Q=0\), and suppose multiplication by \(\beta\in R\) on \(Q\) is injective. Then
\[
\beta\cdot p\in L\quad\Longleftrightarrow\quad p\in L.
\]

*Proof.*

### Step 1. Translate a multiplied pair into an edge equation

Write \(p=(x,y)\). If \(\beta\cdot p\in L\), some \(n\) satisfies
\[
f(n)=\beta x,\qquad g(n)=\tau(\beta)y.
\]
Compatibility of the two projections gives
\[
\beta\,\ell(x)=\tau(\beta)\,u(y).
\]

### Step 2. Identify the two scalar actions on the quotient

The divisibility assumption supplies \(c\) with
\(\tau(\beta)-\beta=\alpha c\).
Since \(\alpha\) annihilates \(Q\),
\[
(\tau(\beta)-\beta)u(y)=\alpha c\,u(y)=0.
\]
Hence \(\tau(\beta)u(y)=\beta u(y)\).

### Step 3. Cancel the regular scalar

Substitute Step 2 into Step 1:
\[
\beta\ell(x)=\beta u(y).
\]
Injectivity of multiplication by \(\beta\) on \(Q\) gives \(\ell(x)=u(y)\).

The [[node:kl.algebra.pair_projection|pair-projection compatibility theorem]] now supplies \(m\in N\) with \(f(m)=x\), \(g(m)=y\), proving \(p\in L\).

### Step 4. Prove the reverse implication

If \(p\in L\), scalar closure of the twisted lattice gives \(\beta\cdot p\in L\). This proves the equivalence.

The regularity condition is imposed on the common quotient \(Q\), where the two coordinate values are compared.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ReflectionPairTranslation.lattice_saturated`: [Frobenius.lean:2106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2106).
