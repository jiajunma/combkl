---
id: kl.notes.reflection_frobenius
title: The perfect trace pairing of a reflection extension
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.frobenius_data
- kl.word.reflection_coordinates
- kl.word.reflection_trace
lean:
  repository: openai-kl
  modules:
  - Decomposition
  declarations:
  - OAI.KLInvariance.ReflectionFrobenius.crossPair
  - OAI.KLInvariance.ReflectionFrobenius.crossPair_bijective
  - OAI.KLInvariance.ReflectionFrobenius.crossPairEquiv
  - OAI.KLInvariance.ReflectionFrobenius.duality
  - OAI.KLInvariance.ReflectionFrobenius.duality_apply
  - OAI.KLInvariance.ReflectionFrobenius.duality_balanced
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1552
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.crossPair
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1560
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.crossPair_bijective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1577
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.crossPairEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1583
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.duality
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1588
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.duality_apply
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1593
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.duality_balanced
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; bg:normalization
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Replaced the former combined summary with the actual coordinate/crossPair/dualMap
    composite. Checked its explicit inverse, finite basis and balance equation in
    the local proof.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# The perfect trace pairing of a reflection extension

Let \(A\) be a commutative domain over a characteristic-zero field \(k\), and let \(\tau:A\to A\) be a \(k\)-algebra involution. Suppose
\[
\alpha\ne0,\qquad \tau(\alpha)=-\alpha,\qquad
\alpha\mid a-\tau(a)\quad(a\in A).
\]
With \(R=A^\tau\) and the reflection trace \(t\), the map
\[
D:A\longrightarrow\operatorname{Hom}_R(A,R),
\qquad D(a)(b)=t(ab)
\]
is an \(R\)-linear isomorphism. Thus \(R\to A\) is a finite free Frobenius extension with basis \(1,\alpha\), and
\[
D(ca)(b)=D(a)(cb).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit tensor construction underlying the duality.**

**OpenAI notes:** The grading-normalization proof starts from a normalized self-dual projective, uses the cited moment-graph/Soergel equivalence and character theorem, and translates doubled degrees back to the degree-one convention. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The local construction begins with the simple reflection fixed algebra and the trace extracting the root coefficient, normalized by t(alpha)=1. It recovers linear functionals through the trace, extends the resulting duality by tensor product, and proves a one-degree pairing shift for each letter. [Decomposition:1588](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1588), [Frobenius:168](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L168), [Frobenius:270](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L270), [Frobenius:602](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L602).

**Role in the proof:** These nodes supply the actual word-module pairing and its homogeneous basis calculation. The boundary-pairing construction subsequently transports this pairing to a boundary summand. The source uses roots of degree one throughout this tensor calculation.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Express the pairing in invariant coordinates

The [[node:kl.word.reflection_coordinates|reflection coordinate theorem]] gives
\[
C:A\xrightarrow{\sim}R^2,\qquad a\mapsto(a_0,a_1).
\]
The trace-product formula states
\[
t(ab)=a_0b_1+a_1b_0.
\]
Consequently, in these coordinates the duality is the map
\[
K:R^2\longrightarrow\operatorname{Hom}_R(R^2,R),\qquad
K(c_0,c_1)(b_0,b_1)=c_0b_1+c_1b_0.
\]
Each formula is linear over \(R\), including linearity in the representing vector \((c_0,c_1)\).

### Step 2. Invert the coordinate pairing

For an \(R\)-linear functional \(\lambda:R^2\to R\), define
\[
J(\lambda)=(\lambda(0,1),\lambda(1,0)).
\]
Every vector decomposes as
\[
(b_0,b_1)=b_0(1,0)+b_1(0,1).
\]
Hence
\[
K(J(\lambda))(b_0,b_1)
=\lambda(0,1)b_1+\lambda(1,0)b_0
=\lambda(b_0,b_1).
\]
Conversely, evaluating \(K(c_0,c_1)\) at \((0,1)\) gives \(c_0\), and evaluating at \((1,0)\) gives \(c_1\). Thus \(J K\) and \(K J\) are identities. This is the source's crossPairEquiv.

### Step 3. Transport the isomorphism back to the algebra

Precomposition with \(C\) identifies functionals on \(R^2\) with functionals on \(A\):
\[
\lambda\longmapsto \lambda\circ C.
\]
It is an isomorphism with inverse precomposition by \(C^{-1}\). Compose it with \(K\) and \(C\). For \(a,b\in A\), the composite has value \(a_0b_1+a_1b_0=t(ab)\), so it is precisely \(D\).

An explicit inverse sends a functional \(f:A\to R\) to
\[
D^{-1}(f)=f(\alpha)+\alpha f(1).
\]
Testing on the basis \(1,\alpha\) verifies the formula. Equivalently, the trace-pairing matrix is
\[
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]
whose square is the identity over \(R\).

### Step 4. Verify the multiplication compatibility

For \(a,b,c\in A\), associativity and commutativity give
\[
D(ca)(b)=t(cab)=t(a(cb))=D(a)(cb).
\]
The basis \(1,\alpha\) already proves finite freeness over \(R\). Together with \(D\) and its trace formula, this supplies every part of the Frobenius extension data.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ReflectionFrobenius.crossPair`: [Decomposition.lean:1552](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1552).

`OAI.KLInvariance.ReflectionFrobenius.crossPair_bijective`: [Decomposition.lean:1560](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1560).

`OAI.KLInvariance.ReflectionFrobenius.crossPairEquiv`: [Decomposition.lean:1577](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1577).

`OAI.KLInvariance.ReflectionFrobenius.duality`: [Decomposition.lean:1583](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1583).

`OAI.KLInvariance.ReflectionFrobenius.duality_apply`: [Decomposition.lean:1588](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1588).

`OAI.KLInvariance.ReflectionFrobenius.duality_balanced`: [Decomposition.lean:1593](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1593).
