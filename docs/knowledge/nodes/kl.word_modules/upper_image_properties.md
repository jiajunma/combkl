---
id: kl.word.upper_image_properties
title: Compatible tuples, upper-image projectivity and lifting
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.coordinate_images
- kl.word.reflected_sets
- kl.algebra.pair_projection
- kl.algebra.projective_presentations
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.BottCompatible
  - OAI.KLInvariance.TitsSpace.BottFlabby
  - OAI.KLInvariance.TitsSpace.BottProjectiveUpper
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:462
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BottCompatible
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:467
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BottFlabby
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:470
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BottProjectiveUpper
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, coordinate sets, kernel maps and induction hypotheses
    explicit?
  verdict: Read the three predicates and their actual quantifiers. Distinguished edge
    witnesses from a common word lift, defined the projective-image section, and recorded
    both inputs of bottProjectiveUpper_cons.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Compatible tuples, upper-image projectivity and lifting

Fix a finite-generator Coxeter system and a tensor word module \(M_{\mathbf t}\) over its symmetric coefficient algebra \(A\). For \(U\subseteq W\), a stalk tuple is a family
\[
z=(z_x)_{x\in U},\qquad z_x\in M_{\mathbf t}^x.
\]

The tuple is compatible if, for every upward reflection edge \(x\to y\) with \(x,y\in U\), there is a word vector \(m\) satisfying
\[
\pi_x(m)=z_x,\qquad \pi_y(m)=z_y.
\]
This is BottCompatible. By the pair-projection quotient criterion, it is exactly equality of the two endpoint restrictions on each such edge.

A vector in \(L_{\mathbf t}(U)\) has one common preimage for all coordinates. That preimage supplies each of the edge witnesses above, so every image tuple is compatible.

## Lifting compatible upper tuples

BottFlabby is the following property of the word:
\[
\text{for every Bruhat upper set }U,\quad
z\text{ compatible on }U
\Longrightarrow z\in L_{\mathbf t}(U).
\]
The conclusion means that one word vector has all prescribed stalk values simultaneously.

For the one-letter word in the two-element Coxeter group \(1<s\), compatibility on \(\{1,s\}\) is
\(f-g\in\alpha A\), precisely the common-image condition. On \(\{s\}\), every value is attained by a diagonal pair \((g,g)\).

## Projectivity of every upper image

BottProjectiveUpper is the property
\[
\text{for every Bruhat upper set }U,\quad
L_{\mathbf t}(U)\text{ is projective over }A.
\]
Projectivity means that linear maps out of this image lift through surjections. In particular, its surjective word projection admits a linear section
\[
\sigma:L_{\mathbf t}(U)\to M_{\mathbf t},
\qquad p_U\sigma=1.
\]
This produces an endomorphism \(\sigma p_U\) that preserves the coordinates on \(U\) and kills every word vector vanishing on \(U\).

The source's word-induction step takes both properties for the shorter word. Upper-image projectivity supplies split maps; compatible-tuple lifting identifies the common kernel in a two-stage projection. A separate prime-denominator argument proves the lifting property from upper-image projectivity for each fixed word.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.BottCompatible`: [IntegralPairings.lean:462](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L462).

`OAI.KLInvariance.TitsSpace.BottFlabby`: [IntegralPairings.lean:467](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L467).

`OAI.KLInvariance.TitsSpace.BottProjectiveUpper`: [IntegralPairings.lean:470](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L470).
