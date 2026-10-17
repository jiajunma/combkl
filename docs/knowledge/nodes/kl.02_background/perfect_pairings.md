---
id: kl.notes.perfect_pairings
title: Perfect pairings and balanced bimodules
kind: definition
status: formalized
primary_topic: kl.02_background
topics:
- kl.02_background
uses: []
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.FrobeniusDuality.PairedModule
  - OAI.KLInvariance.FrobeniusDuality.PairedBimodule
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:226
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.PairedModule
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:295
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.PairedBimodule
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; bg:normalization
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the mathematical hypotheses and scope retained from the referenced declarations?
  verdict: The exposition follows the fixed Lean source; worked calculations explain
    the constructions.
tags:
- Kazhdan-Lusztig
- background
---

# Perfect pairings and balanced bimodules

A perfect pairing on a finite free \(A\)-module \(M\) is an \(A\)-linear isomorphism
\[
M\longrightarrow\operatorname{Hom}_A(M,A),\qquad
m\longmapsto\langle m,-\rangle.
\]
Perfectness means that every linear functional is represented by a unique element of \(M\). Over a ring, mere nondegeneracy is weaker: multiplication by a nonunit can define an injective pairing map without making it surjective.

A paired bimodule additionally has a commuting right \(A\)-action and a symmetric pairing satisfying
\[
\langle m\cdot a,n\rangle=\langle m,n\cdot a\rangle,
\qquad
\langle m,n\rangle=\langle n,m\rangle.
\]
The first identity is balance. It permits scalar action on one argument to be moved to the other argument. The unit example is \(M=A\), with multiplication pairing \(\langle a,b\rangle=ab\).

These properties are retained through the tensor construction of word objects. Their later use is concrete: a perfect global pairing identifies supported sections with duals of stalk quotients, while balance ensures that support-cutting maps can be moved across the pairing without changing the value.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization

`PairedModule` has fields `carrier`, `add`, `module`, `free`, `finite`, and `pairing`. `PairedBimodule` has fields `obj`, `right`, `balanced`, and `symmetric`. The `add` and `module` fields supply the additive and scalar structures, rather than additional mathematical hypotheses.

`OAI.KLInvariance.FrobeniusDuality.PairedModule`: [Frobenius.lean:226](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L226).

`OAI.KLInvariance.FrobeniusDuality.PairedBimodule`: [Frobenius.lean:295](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L295).
