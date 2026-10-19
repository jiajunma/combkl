---
id: kl.word.reflected_sets
title: Bruhat upper sets and their reflected union and intersection
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.foundations.bruhat_order
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.BruhatUpper
  - OAI.KLInvariance.TitsSpace.simplePull
  - OAI.KLInvariance.TitsSpace.simpleUnion
  - OAI.KLInvariance.TitsSpace.simpleInter
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:384
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BruhatUpper
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:630
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simplePull
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:387
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simpleUnion
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:388
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simpleInter
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, coordinate sets, kernel maps and induction hypotheses
    explicit?
  verdict: Read BruhatUpper/simplePull/simpleUnion/simpleInter. Defined ambient upper
    sets, the preimage convention and the union/intersection names used uniformly
    in the new proof chain.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Bruhat upper sets and their reflected union and intersection

Let \(W\) be a Coxeter group with strong Bruhat order. A Bruhat upper set is a subset \(U\subseteq W\) such that
\[
x\in U,\quad x\le y\quad\Longrightarrow\quad y\in U.
\]
This is the source's BruhatUpper predicate on the ambient group.

Fix a simple reflection \(s\). Its reflected preimage is
\[
sU=\{x\in W:sx\in U\}.
\]
Because \(s^2=1\), this is also the image \(\{sx:x\in U\}\). The source calls it simplePull.

Define
\[
J=U\cup sU,\qquad K=U\cap sU.
\]
These are simpleUnion and simpleInter:
\[
x\in J\iff(x\in U\text{ or }sx\in U),\qquad
x\in K\iff(x\in U\text{ and }sx\in U).
\]
The four natural inclusions are \(K\subseteq U\), \(K\subseteq sU\), \(U\subseteq J\), and \(sU\subseteq J\).

A set is reflection-stable when \(sx\in U\) if and only if \(x\in U\). Exchanging \(x\) and \(sx\) in the two membership formulas proves that both \(J\) and \(K\) are reflection-stable.

## A single simple reflection

For the two-element Coxeter group \(1<s\), take \(U=\{s\}\). Then
\[
sU=\{1\},\qquad J=\{1,s\},\qquad K=\varnothing.
\]
The upper set \(U\) selects the higher endpoint. Its reflected union fills the pair, and its reflected intersection is empty.

The [[node:kl.word.upper_set_reflection|reflected upper-set theorem]] proves that \(J,K\) are upper whenever \(U\) is. These sets control the restriction maps used to prove projectivity of word-coordinate images.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.BruhatUpper`: [IntegralPairings.lean:384](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L384).

`OAI.KLInvariance.TitsSpace.simplePull`: [IntegralPairings.lean:630](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L630).

`OAI.KLInvariance.TitsSpace.simpleUnion`: [IntegralPairings.lean:387](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L387).

`OAI.KLInvariance.TitsSpace.simpleInter`: [IntegralPairings.lean:388](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L388).
