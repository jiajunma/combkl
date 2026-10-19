---
id: kl.word.pair_lattice_exact_sequences
title: Projection kernels and split exact sequences of a twisted pair lattice
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.twisted_pair_lattice
- kl.algebra.scalar_twist
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  - Frobenius
  declarations:
  - OAI.KLInvariance.ReflectionPairTranslation.left_surjective
  - OAI.KLInvariance.ReflectionPairTranslation.kernelMap
  - OAI.KLInvariance.ReflectionPairTranslation.kernelMap_surjective
  - OAI.KLInvariance.ReflectionPairTranslation.kernelMap_injective
  - OAI.KLInvariance.ReflectionPairTranslation.kernelEquiv
  - OAI.KLInvariance.ReflectionPairTranslation.free_of_surjective_of_ker_free
  - OAI.KLInvariance.ReflectionPairTranslation.lattice_free
  - OAI.KLInvariance.ReflectionPairTranslation.right
  - OAI.KLInvariance.ReflectionPairTranslation.right_surjective
  - OAI.KLInvariance.ReflectionPairTranslation.rightKernelMap
  - OAI.KLInvariance.ReflectionPairTranslation.rightKernelEquiv
  - OAI.KLInvariance.ReflectionPairTranslation.lattice_free_right
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:2130
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.left_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:2137
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.kernelMap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:2155
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.kernelMap_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:2165
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.kernelMap_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:2171
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.kernelEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:2178
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.free_of_surjective_of_ker_free
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:2206
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.lattice_free
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1212
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.right
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1215
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.right_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1221
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.rightKernelMap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1253
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.rightKernelEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1260
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.lattice_free_right
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read left/right kernel maps and equivalences in Frobenius and BottSamelson.
    Preserved the separate kernel equality and regular-scalar hypotheses for each
    orientation, and expanded the source splitting isomorphism.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Projection kernels and split exact sequences of a twisted pair lattice

Let \(R\) be a commutative ring, \(f:N\to X\) and \(g:N\to Y\) linear maps, and \(\tau:R\to R\) an automorphism. Let \(\alpha\in R\) satisfy
\[
\alpha\mid\tau(r)-r\quad(r\in R),\qquad
\forall y\in Y,\ \exists n,\ f(n)=0,\ g(n)=\alpha y.
\]
These data define the twisted pair lattice
\(L\subseteq X\oplus{}^\tau Y\).

There are two projection-kernel statements.

- Suppose \(f\) is surjective, multiplication by \(\alpha\) is injective on \(Y\), and
  \[
  \{g(n):f(n)=0\}=\alpha Y.
  \]
  Then the following sequence is exact:
  \[
  0\longrightarrow{}^\tau Y
  \xrightarrow{\,y\mapsto(0,\alpha y)\,}L
  \xrightarrow{\,(x,y)\mapsto x\,}X
  \longrightarrow0.
  \]
- Suppose \(g\) is surjective, multiplication by \(\alpha\) is injective on \(X\), and
  \[
  \{f(n):g(n)=0\}=\alpha X.
  \]
  Then the following sequence is exact:
  \[
  0\longrightarrow X
  \xrightarrow{\,x\mapsto(\alpha x,0)\,}L
  \xrightarrow{\,(x,y)\mapsto y\,}{}^\tau Y
  \longrightarrow0.
  \]

In either case, if \(X,Y\) are free, then \(L\) is free.

*Proof.*

### Step 1. Identify the first projection and its kernel

The map \(\ell_L:L\to X\), \((x,y)\mapsto x\), is linear. If \(f\) is surjective, choose a preimage \(n\) of any \(x\); the pair \((f(n),g(n))\) proves that \(\ell_L\) is surjective.

A vector in its kernel is exactly a pair \((0,y)\) with a common preimage under \(f,g\). The first kernel hypothesis says precisely that such a \(y\) is of the form \(\alpha z\).

### Step 2. Prove the first kernel isomorphism

Define
\[
j:{}^\tau Y\to\ker\ell_L,\qquad z\mapsto(0,\alpha z).
\]
The lattice hypothesis supplies a common preimage, so this is well defined. The source and target use the same twisted action in their second coordinate. Hence for \(r\in R\),
\[
j(r\cdot z)=(0,\alpha\tau(r)z)
=r\cdot(0,\alpha z).
\]
It is additive as well. Injectivity follows by cancelling the scalar action of \(\alpha\) on \(Y\). Step 1 and the kernel equality prove surjectivity. Thus \(j\) is the source's kernelEquiv, establishing the first exact sequence.

### Step 3. Prove the second kernel isomorphism

Projection \(r_L:L\to{}^\tau Y\) is linear. Surjectivity of \(g\) gives a lattice pair above every second coordinate.

The second kernel hypothesis identifies \(\ker r_L\) with the pairs \((\alpha z,0)\). The map
\[
j':X\to\ker r_L,\qquad z\mapsto(\alpha z,0)
\]
is linear by commutativity of \(R\). It is surjective by that kernel description and injective by the assumed injectivity of multiplication by \(\alpha\) on \(X\). This is rightKernelEquiv and proves the second exact sequence.

### Step 4. Split a surjection onto a free module

For either sequence, denote the surjection by \(\pi:L\to Q\), where \(Q=X\) or \(Q={}^\tau Y\). A twist of a free module is free: if \((e_i)\) is an old basis, the same underlying vectors form a twisted basis, with coefficients transformed by \(\tau^{-1}\). Thus \(Q\) is free in both cases.

Choose a basis \((e_i)\) of \(Q\) and lifts \(\widetilde e_i\in L\) with
\(\pi(\widetilde e_i)=e_i\). Extending these assignments linearly gives
\(s:Q\to L\) with \(\pi s=1\).

### Step 5. Exhibit the direct-sum isomorphism

Define
\[
\Phi:\ker\pi\oplus Q\to L,\qquad (k,q)\mapsto k+s(q).
\]
Its inverse is
\[
v\longmapsto(v-s(\pi(v)),\,\pi(v)).
\]
The first component lies in the kernel because
\(\pi(v)-\pi(s(\pi(v)))=0\).
Substitution proves both composite identities: the recovered sum is \(v\), and the recovered pair from \(k+s(q)\) is \((k,q)\).

The kernel is free by Step 2 or Step 3, and the quotient is free by Step 4. Their direct sum is free, so this isomorphism proves freeness of \(L\). These are the two lattice_free theorems used for the two Bruhat orientations.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ReflectionPairTranslation.left_surjective`: [Frobenius.lean:2130](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2130).

`OAI.KLInvariance.ReflectionPairTranslation.kernelMap`: [Frobenius.lean:2137](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2137).

`OAI.KLInvariance.ReflectionPairTranslation.kernelMap_surjective`: [Frobenius.lean:2155](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2155).

`OAI.KLInvariance.ReflectionPairTranslation.kernelMap_injective`: [Frobenius.lean:2165](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2165).

`OAI.KLInvariance.ReflectionPairTranslation.kernelEquiv`: [Frobenius.lean:2171](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2171).

`OAI.KLInvariance.ReflectionPairTranslation.free_of_surjective_of_ker_free`: [Frobenius.lean:2178](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2178).

`OAI.KLInvariance.ReflectionPairTranslation.lattice_free`: [Frobenius.lean:2206](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2206).

`OAI.KLInvariance.ReflectionPairTranslation.right`: [BottSamelson.lean:1212](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1212).

`OAI.KLInvariance.ReflectionPairTranslation.right_surjective`: [BottSamelson.lean:1215](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1215).

`OAI.KLInvariance.ReflectionPairTranslation.rightKernelMap`: [BottSamelson.lean:1221](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1221).

`OAI.KLInvariance.ReflectionPairTranslation.rightKernelEquiv`: [BottSamelson.lean:1253](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1253).

`OAI.KLInvariance.ReflectionPairTranslation.lattice_free_right`: [BottSamelson.lean:1260](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1260).
