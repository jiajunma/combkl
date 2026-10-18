---
id: kl.foundations.bruhat_order
title: Strong Bruhat order
kind: definition
status: formalized
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.foundations.bruhat_step
lean:
  repository: openai-kl
  modules:
  - Model
  - Bruhat
  declarations:
  - OAI.KLInvariance.BruhatLE
  - OAI.KLInvariance.bruhat_antisymm
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Model:18
    format: lean-location
    note: OAI.KLInvariance.BruhatLE
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:38
    format: lean-location
    note: OAI.KLInvariance.bruhat_antisymm
  - artifact: openai-kl-paper
    locator: 1. Introduction and conventions; sec:introduction
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- introduction
---

# Strong Bruhat order

The strong Bruhat order is the reflexive transitive closure of [[node:kl.foundations.bruhat_step]]. Thus \(x\le y\) means that a finite sequence of upward reflection edges joins \(x\) to \(y\), with the empty sequence allowed.

Length strictly increases along every nontrivial edge. Consequently \(x\le y\) implies \(\ell(x)\le\ell(y)\), and \(x\le y\le x\) forces \(x=y\). Together with reflexivity and transitivity, this gives a partial order.

## The first nontrivial example

Take \(W=S_3\), with \(s=(12)\) and \(t=(23)\). The interval from the identity to \(w_0=sts=tst\) has ranks
\[
\{1\},\quad \{s,t\},\quad\{st,ts\},\quad\{w_0\}.
\]
Each element in either middle rank is connected by covers to both elements in the adjacent rank where applicable.

The strong reflection graph contains more information than the Hasse diagram initially displays. In particular, \(w_0\) itself is a reflection, so \(1\to w_0\) is an edge of length difference three. It is not a cover. This distinction explains the graph-reconstruction step: an abstract interval first gives covers, whereas the local sheaf comparisons use every reflection edge.

A reduced subword is also different from a prefix. The word \(st\) occurs as a subword of \(sts\), and so does \(ts\), using its last two positions. Bruhat order retains all these subword relations; weak order would only track the appropriate prefix or suffix relations.

## References

[1. Introduction and conventions](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization

`OAI.KLInvariance.BruhatLE`: [Model.lean:18](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Model.lean#L18).

`OAI.KLInvariance.bruhat_antisymm`: [Bruhat.lean:38](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L38).
