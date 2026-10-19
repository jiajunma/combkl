---
id: kl.word.tail_maps
title: The ordinary and reflected tail maps of a tensor word
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.tensor_induction
- kl.algebra.scalar_twist
- kl.word.head_pair_coordinates
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  declarations:
  - OAI.KLInvariance.ReflectionPairTranslation.tensorFirst
  - OAI.KLInvariance.ReflectionPairTranslation.tensorFirst_tmul
  - OAI.KLInvariance.ReflectionPairTranslation.tensorSecond
  - OAI.KLInvariance.ReflectionPairTranslation.tensorSecond_tmul
  - OAI.KLInvariance.ReflectionPairTranslation.twistMap
  - OAI.KLInvariance.TitsSpace.bottHeadTail
  - OAI.KLInvariance.TitsSpace.bottHeadReflectedTail
  - OAI.KLInvariance.TitsSpace.bottHeadTail_seed
  - OAI.KLInvariance.TitsSpace.bottHeadReflectedTail_seed
  - OAI.KLInvariance.TitsSpace.bottHeadLocalPair
  - OAI.KLInvariance.TitsSpace.bottHeadLocalPair_seed
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:706
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.tensorFirst
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:710
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.tensorFirst_tmul
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:713
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.tensorSecond
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:726
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.tensorSecond_tmul
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:729
    format: lean-location
    note: OAI.KLInvariance.ReflectionPairTranslation.twistMap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:750
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadTail
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:754
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadReflectedTail
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:760
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadTail_seed
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:764
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadReflectedTail_seed
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:769
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadLocalPair
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:777
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadLocalPair_seed
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read tensorFirst, tensorSecond and twistMap with the general fixed-subalgebra
    hypothesis, then the actual tail and local-pair definitions. Made both scalar
    actions and the finite-sum formulas explicit.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# The ordinary and reflected tail maps of a tensor word

Let \(C\to A\) be an algebra map between commutative rings, let \(N\) be an \(A\)-module with its restricted \(C\)-action, and let \(\tau:A\to A\) be a ring automorphism fixing the image of \(C\).

There are two \(A\)-linear maps
\[
\mu:A\otimes_C N\to N,\qquad \mu(a\otimes n)=an,
\]
and
\[
\nu:A\otimes_C N\to{}^\tau N,\qquad
\nu(a\otimes n)=\tau(a)n.
\]
The second formula denotes the underlying vector in the twisted module, whose action is \(r\star n=\tau(r)n\). These are the source's tensorFirst and tensorSecond.

## Tensor relations and the scalar twist

For \(c\in C\), the ordinary formula sends both \(ac\otimes n\) and \(a\otimes cn\) to \(acn\). The reflected formula sends them to
\[
\tau(ac)n=\tau(a)c n,
\]
because \(\tau(c)=c\). Both maps are therefore well defined on the tensor product.

The first map is \(A\)-linear by ordinary multiplication. For the second,
\[
\nu(r(a\otimes n))=\tau(ra)n
=\tau(r)\tau(a)n=r\star\nu(a\otimes n),
\]
which proves linearity into its twisted target.

If \(h:N\to P\) is \(A\)-linear, the same underlying formula \(n\mapsto h(n)\) defines
\({}^\tau h:{}^\tau N\to{}^\tau P\): the equality
\(h(\tau(r)n)=\tau(r)h(n)\) gives the required scalar law.

## Applying the maps to a word

For a finite-generator Coxeter system, let \(A\) be its symmetric coefficient algebra, fix a simple reflection \(s\), and put \(C=A^s\), \(\tau=\chi_s\), \(N=M_{\mathbf t}\). Then
\[
\mu:M_{s\mathbf t}\to M_{\mathbf t},\qquad
\nu:M_{s\mathbf t}\to{}^\tau M_{\mathbf t}
\]
are bottHeadTail and bottHeadReflectedTail.

For a finite tensor sum \(m=\sum_j a_j\otimes n_j\), their underlying vectors are
\[
\mu(m)=\sum_j a_jn_j,\qquad
\nu(m)=\sum_j\tau(a_j)n_j.
\]
In particular, both send \(1\otimes n\) to the underlying vector \(n\).

## The local pair of tail projections

For each group weight \(x\), define
\[
P_x(m)=
\bigl(\pi_x(\mu(m)),\ \pi_{sx}(\nu(m))\bigr)
\in M_{\mathbf t}^x\oplus{}^\tau M_{\mathbf t}^{sx}.
\]
The second projection here is the twisted map on the underlying vector of \(\nu(m)\). Hence \(P_x\) is \(A\)-linear. It is bottHeadLocalPair.

For \(1\otimes n\), it is the common-preimage pair
\[
P_x(1\otimes n)=(\pi_x(n),\pi_{sx}(n)).
\]
The [[node:kl.word.local_pair_maps|local-pair theorem]] shows that \(P_x(m)\) always lies in the head pair lattice and represents the new weight-stalk projection.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ReflectionPairTranslation.tensorFirst`: [BottSamelson.lean:706](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L706).

`OAI.KLInvariance.ReflectionPairTranslation.tensorFirst_tmul`: [BottSamelson.lean:710](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L710).

`OAI.KLInvariance.ReflectionPairTranslation.tensorSecond`: [BottSamelson.lean:713](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L713).

`OAI.KLInvariance.ReflectionPairTranslation.tensorSecond_tmul`: [BottSamelson.lean:726](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L726).

`OAI.KLInvariance.ReflectionPairTranslation.twistMap`: [BottSamelson.lean:729](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L729).

`OAI.KLInvariance.TitsSpace.bottHeadTail`: [BottSamelson.lean:750](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L750).

`OAI.KLInvariance.TitsSpace.bottHeadReflectedTail`: [BottSamelson.lean:754](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L754).

`OAI.KLInvariance.TitsSpace.bottHeadTail_seed`: [BottSamelson.lean:760](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L760).

`OAI.KLInvariance.TitsSpace.bottHeadReflectedTail_seed`: [BottSamelson.lean:764](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L764).

`OAI.KLInvariance.TitsSpace.bottHeadLocalPair`: [BottSamelson.lean:769](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L769).

`OAI.KLInvariance.TitsSpace.bottHeadLocalPair_seed`: [BottSamelson.lean:777](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L777).
