---
id: kl.word.reflection_coordinates
title: Invariant and anti-invariant reflection coordinates
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.invariant_subalgebra
lean:
  repository: openai-kl
  modules:
  - Decomposition
  - Frobenius
  declarations:
  - OAI.KLInvariance.ReflectionFrobenius.quotient_fixed
  - OAI.KLInvariance.ReflectionFrobenius.expand_injective
  - OAI.KLInvariance.ReflectionFrobenius.expand_surjective
  - OAI.KLInvariance.ReflectionFrobenius.coordinates
  - OAI.KLInvariance.ReflectionFrobenius.expand_coordinates
  - OAI.KLInvariance.ReflectionFrobenius.coordinates_expand
  - OAI.KLInvariance.ReflectionFrobenius.reflectionBasis
  - OAI.KLInvariance.ReflectionFrobenius.reflectionBasis_zero
  - OAI.KLInvariance.ReflectionFrobenius.reflectionBasis_one
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1462
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.quotient_fixed
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1469
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.expand_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1486
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.expand_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1504
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.coordinates
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1508
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.expand_coordinates
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1512
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.coordinates_expand
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:522
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.reflectionBasis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:525
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.reflectionBasis_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:529
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.reflectionBasis_one
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Checked the quotient_fixed cancellation, explicit half-sum coordinates,
    injectivity and transported two-element basis against Decomposition and Frobenius.
    Included the eigenspace calculation as a consequence of the proved coordinates.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Invariant and anti-invariant reflection coordinates

Let \(k\) be a characteristic-zero field, \(A\) a commutative domain over \(k\), and \(\tau\) a \(k\)-algebra involution. Suppose
\[
\alpha\ne0,\qquad \tau(\alpha)=-\alpha,\qquad
\alpha\mid a-\tau(a)\quad(a\in A).
\]
Put \(R=A^\tau\). Every \(a\in A\) has a unique expression
\[
a=a_0+\alpha a_1,\qquad a_0,a_1\in R.
\]
Consequently the expansion \(E:R^2\to A\) is an \(R\)-linear isomorphism; its inverse is the reflection coordinate map \(C\). The elements \(1,\alpha\) form an \(R\)-basis.

*Proof.*

### Step 1. Show that the divided difference is invariant

Choose \(d\in A\) with
\[
a-\tau(a)=\alpha d.
\]
Applying \(\tau\) and using \(\tau^2=1\) gives
\[
\tau(a)-a=-\alpha\,\tau(d).
\]
Negating the original equality gives the same left side as \(-\alpha d\). Thus
\(\alpha\tau(d)=\alpha d\). Since \(A\) is a domain and \(\alpha\ne0\), cancellation gives \(\tau(d)=d\).

### Step 2. Construct both coordinates

Let \(h\) be the image of \(1/2\in k\) in \(A\). Characteristic zero gives \(2h=1\). Set
\[
a_0=h(a+\tau(a)),\qquad a_1=hd.
\]
The automorphism fixes \(h\), and it exchanges \(a\) with \(\tau(a)\). Hence \(\tau(a_0)=a_0\). Step 1 gives \(\tau(a_1)=a_1\). Both coordinates therefore lie in \(R\).

Their expansion is
\[
a_0+\alpha a_1
=h(a+\tau(a))+h(a-\tau(a))=2ha=a.
\]
This proves surjectivity of \(E\).

### Step 3. Prove uniqueness

Suppose \(a_0+\alpha a_1=b_0+\alpha b_1\), with all four coefficients invariant. Applying \(\tau\) yields
\[
a_0-\alpha a_1=b_0-\alpha b_1.
\]
Subtracting gives \(2\alpha(a_1-b_1)=0\). The scalar map \(k\to A\) is injective because \(k\) is a field and \(A\) is a nonzero algebra. Thus \(2\ne0\) in \(A\), and the domain property gives \(2\alpha\ne0\). It follows that \(a_1=b_1\), and the original equality then gives \(a_0=b_0\).

### Step 4. Obtain the linear coordinates and the basis

The expansion map is \(R\)-linear by its definition. Its bijectivity gives the inverse \(R\)-linear map
\[
C:A\longrightarrow R^2,\qquad C(a)=(a_0,a_1).
\]
The source's two inverse identities are
\[
E(C(a))=a,\qquad C(E(c_0,c_1))=(c_0,c_1).
\]
Transporting the standard basis of \(R^2\) through \(E\) gives \(E(1,0)=1\) and \(E(0,1)=\alpha\). These are the source's reflectionBasis vectors.

### Step 5. Identify the two eigenspaces

For \(a=a_0+\alpha a_1\), one has \(\tau(a)=a_0-\alpha a_1\). Thus \(\tau(a)=a\) forces \(2\alpha a_1=0\), giving \(a_1=0\). Likewise \(\tau(a)=-a\) forces \(2a_0=0\), giving \(a_0=0\).

The invariant summand is therefore \(R\), and the anti-invariant summand is \(\alpha R\). This explains the direct-sum expression \(A=R\oplus\alpha R\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ReflectionFrobenius.quotient_fixed`: [Decomposition.lean:1462](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1462).

`OAI.KLInvariance.ReflectionFrobenius.expand_injective`: [Decomposition.lean:1469](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1469).

`OAI.KLInvariance.ReflectionFrobenius.expand_surjective`: [Decomposition.lean:1486](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1486).

`OAI.KLInvariance.ReflectionFrobenius.coordinates`: [Decomposition.lean:1504](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1504).

`OAI.KLInvariance.ReflectionFrobenius.expand_coordinates`: [Decomposition.lean:1508](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1508).

`OAI.KLInvariance.ReflectionFrobenius.coordinates_expand`: [Decomposition.lean:1512](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1512).

`OAI.KLInvariance.ReflectionFrobenius.reflectionBasis`: [Frobenius.lean:522](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L522).

`OAI.KLInvariance.ReflectionFrobenius.reflectionBasis_zero`: [Frobenius.lean:525](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L525).

`OAI.KLInvariance.ReflectionFrobenius.reflectionBasis_one`: [Frobenius.lean:529](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L529).
