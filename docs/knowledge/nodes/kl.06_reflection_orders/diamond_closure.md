---
id: kl.detail.diamond_closure
title: The unlabelled diamond closure of cover edges
kind: definition
status: formalized
primary_topic: kl.06_reflection_orders
topics:
- kl.06_reflection_orders
uses:
- kl.foundations.interval
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.DiamondEdges
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1529
    format: lean-location
    note: OAI.KLInvariance.DiamondEdges
  - artifact: openai-kl-paper
    locator: Related paper context; sec:dihedral
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  definition: accepted
  proof: not_applicable
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

# The unlabelled diamond closure of cover edges

For a partially ordered set \(X\), define a relation \(D\) by the following two rules.

1. Every cover \(x\prec y\) belongs to \(D\).
2. If \(a\ne b\), \(c\ne d\), and the eight pairs
\[
(x,a),(x,b),(a,c),(a,d),(b,c),(b,d),(c,z),(d,z)
\]
belong to \(D\), then \((x,z)\) belongs to \(D\).

Take the smallest relation closed under these rules. Only the order is used: there are no reflection labels, roots, or Coxeter generators in the definition.

An order isomorphism preserves covers, distinctness, and every instance of the eight-edge rule. Induction on a derivation therefore transports \(D\). The substantial theorem is that, on a Bruhat interval, this combinatorially generated relation is exactly the full upward reflection-edge relation. That identification is not built into the definition.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L2).

## Lean formalization

The constructors `cover` and `diamond` implement the two rules, with eight recursive premises and the two distinctness conditions.

`OAI.KLInvariance.DiamondEdges`: [ReflectionSchedules.lean:1529](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1529).
