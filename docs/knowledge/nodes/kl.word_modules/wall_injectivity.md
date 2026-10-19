---
id: kl.word.wall_injectivity
title: Injectivity of the reflection block-coordinate map
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.wall_coordinates
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.ReflectionFrobenius.matrixTwist_injective
  - OAI.KLInvariance.ReflectionFrobenius.wallCoordinate_injective
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1158
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.matrixTwist_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1170
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.wallCoordinate_injective
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read matrixTwist_injective and wallCoordinate_injective. Kept the generic
    automorphism hypothesis, isolated the weaker first step, and stated the exact
    characteristic-zero/domain conditions for cancellation.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Injectivity of the reflection block-coordinate map

Let \(A\) be a commutative domain of characteristic zero, let \(\tau:A\to A\) be a ring automorphism, and let \(0\ne\alpha\in A\). Let \(E\) be a square matrix indexed by a finite set \(J\). Suppose multiplication by \(E\) is injective on \(A^J\).

Then multiplication by the entrywise transformed matrix \(\tau E\) is injective, and so is
\[
\mathcal W_E(v_0,v_1)
=\bigl(E(v_0+\alpha v_1),\,(\tau E)(v_0-\alpha v_1)\bigr).
\]

*Proof.*

### Step 1. Transfer injectivity through the ring automorphism

Suppose \((\tau E)v=(\tau E)w\). Apply \(\tau^{-1}\) to each output coordinate. Since it preserves finite sums and products,
\[
\tau^{-1}\left(\sum_j\tau(E_{ij})v_j\right)
=\sum_j E_{ij}\tau^{-1}(v_j).
\]
The equality becomes
\(E(\tau^{-1}v)=E(\tau^{-1}w)\).
Injectivity of \(E\) gives equality of the two transformed input vectors. Applying \(\tau\) coordinatewise gives \(v=w\). This step uses only a commutative ring and its automorphism.

### Step 2. Recover the two sums from equal wall coordinates

Suppose
\(\mathcal W_E(v_0,v_1)=\mathcal W_E(w_0,w_1)\).
Injectivity of \(E\), and then of \(\tau E\), gives
\[
v_0+\alpha v_1=w_0+\alpha w_1,\qquad
v_0-\alpha v_1=w_0-\alpha w_1.
\]

### Step 3. Cancel the root coefficient

Subtract the second vector equality from the first. For each coordinate \(j\),
\[
2\alpha(v_{1,j}-w_{1,j})=0.
\]
Characteristic zero gives \(2\ne0\). The domain property and \(\alpha\ne0\) imply \(2\alpha\ne0\), so cancellation gives \(v_{1,j}=w_{1,j}\) for every \(j\). Hence \(v_1=w_1\).

Substitute this equality into the first vector equation to obtain \(v_0=w_0\). Therefore the wall-coordinate map is injective.

This argument applies directly to polynomial coefficients: it recovers both input vectors through multiplication and cancellation in \(A\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ReflectionFrobenius.matrixTwist_injective`: [Frobenius.lean:1158](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1158).

`OAI.KLInvariance.ReflectionFrobenius.wallCoordinate_injective`: [Frobenius.lean:1170](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1170).
