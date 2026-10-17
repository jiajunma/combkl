---
id: kl.detail.geometric_functional
title: Existence of a generic functional ordering all positive roots
kind: theorem
status: proved
primary_topic: kl.06_reflection_orders
topics:
- kl.06_reflection_orders
uses:
- kl.notes.extended_realization
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.TitsSpace.exists_geometric_functional
  - OAI.KLInvariance.TitsSpace.functionalRatio_between
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:126
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.exists_geometric_functional
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:138
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.functionalRatio_between
  - artifact: openai-kl-paper
    locator: Related paper context; sec:dihedral
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- reflection_orders
---

# Existence of a generic functional ordering all positive roots

For a finite-generator Coxeter system, there exists a real linear functional \(f\) such that the slopes
\[
\lambda(\alpha)=\frac{f(\alpha)}{\operatorname{ht}(\alpha)}
\]
are distinct for distinct positive roots. Ordering roots by these slopes gives the required geometric reflection order.

*Proof.*

Positive roots have positive height, so normalization to height one is defined and injective. There are only countably many roots. The generic-functional construction separates this countable family of distinct normalized vectors: in coordinates, each unwanted equality is the zero set of a nonzero polynomial along a suitable one-parameter family of functionals, and the union of the forbidden parameter sets is countable.

The geometric property follows directly. If
\(\gamma=r\alpha+s\beta\) with \(r,s>0\), its normalized slope is the weighted average
\[
\lambda(\gamma)=
\frac{r\operatorname{ht}(\alpha)\lambda(\alpha)+s\operatorname{ht}(\beta)\lambda(\beta)}
{r\operatorname{ht}(\alpha)+s\operatorname{ht}(\beta)}.
\]
It lies strictly between two distinct endpoint slopes. Thus the order restricts to the correct angular order on each root plane.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L2).

## Lean formalization



`OAI.KLInvariance.TitsSpace.exists_geometric_functional`: [ReflectionSchedules.lean:126](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L126).

`OAI.KLInvariance.TitsSpace.functionalRatio_between`: [ReflectionSchedules.lean:138](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L138).
