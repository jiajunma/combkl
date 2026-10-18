---
id: kl.notes.reflection_order
title: Geometric reflection orders
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.notes.extended_realization
- kl.detail.geometric_functional
- kl.detail.positive_roots
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.TitsSpace.RatioOrder
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1181
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.RatioOrder
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; bg:paths
    format: section
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the source hypotheses retained?
  verdict: The statement and proof follow the fixed formal development and its paper
    counterpart.
tags:
- Kazhdan-Lusztig
- background
---

# Geometric reflection orders

A reflection order is a total order on the positive roots whose restriction to every rank-two root subsystem is one of its two angular orders.

Choose a linear form \(h\) strictly positive on the simple roots. It is then positive on every positive root. Choose another linear form \(f\) for which all slopes
\[
s(\alpha)=\frac{f(\alpha)}{h(\alpha)}
\]
are distinct, and order the positive roots by these slopes.

To understand the rank-two condition, normalize each root to \(\alpha/h(\alpha)\). In a fixed root plane, these normalized roots lie on the affine line \(h=1\). Restricting \(f\) to that line puts them in one of the two possible angular orders. Reversing \(f\) reverses the reflection order.

The root set is countable in finite generator rank. Each equality between two slopes excludes a proper hyperplane of choices for \(f\). A linear form avoiding this countable family can therefore be chosen. This construction still applies when the group and its root system are infinite.

Only finitely many edges occur in a fixed Bruhat interval. Their labels can be scheduled by the reflection order. Edges with the same reflection label are disjoint, because a reflection pairs a vertex \(w\) only with \(tw\); hence there are no interacting ties at a vertex.

Under an unlabelled interval isomorphism, the target order is used to schedule source edges. The transported schedule is not assumed to be a reflection order for the source root system. The dihedral transport and counting arguments establish exactly the properties needed from it.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185).

## Lean formalization

The fields `denominator`, `numerator`, `positive`, and `generic` specify (h), (f), positivity of the denominator, and injectivity of the resulting slope function.

`OAI.KLInvariance.TitsSpace.RatioOrder`: [DyerPaths.lean:1181](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1181).
