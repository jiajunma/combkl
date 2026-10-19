---
id: kl.foundations.interval
title: Bruhat intervals, endpoints and rank differences
kind: definition
status: formalized
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.foundations.bruhat_order
- kl.coxeter.word_data
lean:
  repository: openai-kl
  modules:
  - CanonicalKL
  - Model
  - OrdinaryR
  declarations:
  - OAI.KLInvariance.Interval
  - OAI.KLInvariance.rankDifference
  - OAI.KLInvariance.intervalBottom
  - OAI.KLInvariance.intervalTop
  - OAI.KLInvariance.rankDifference_add
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Model:22
    format: lean-location
    note: OAI.KLInvariance.Interval
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Model:45
    format: lean-location
    note: OAI.KLInvariance.rankDifference
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:428
    format: lean-location
    note: OAI.KLInvariance.intervalBottom
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:431
    format: lean-location
    note: OAI.KLInvariance.intervalTop
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.OrdinaryR:228
    format: lean-location
    note: OAI.KLInvariance.rankDifference_add
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
  prompt: Are the exact interval, order-map and rank hypotheses retained?
  verdict: Read Interval, named endpoints, natural rankDifference and rankDifference_add.
    Expanded nonemptiness, initial/upper/general subintervals, proper-rank arithmetic
    and the order-isomorphism/function transport data.
tags:
- Kazhdan-Lusztig
- Bruhat
- intervals
---

# Bruhat intervals, endpoints and rank differences

For elements \(u,b\) of a Coxeter system, define the interval
\[
[u,b]=\{x:u\le x\le b\}
\]
with the induced strong Bruhat order. An element of the source's interval type consists of its underlying group element and the two endpoint inequalities.

The interval is nonempty exactly when \(u\le b\). A member \(x\) gives \(u\le x\le b\), hence \(u\le b\). Conversely, when \(u\le b\), both \(u\) and \(b\) are members.

## The endpoints and subintervals

For \(u\le b\), the interval bottom is \(u\), with evidence \(u\le u\le b\); the interval top is \(b\), with evidence \(u\le b\le b\). Every member lies above the bottom and below the top.

Given \(u\le x\le y\le b\), the subinterval \([x,y]\) has its natural inclusion in \([u,b]\), because
\(u\le x\le z\le y\le b\).
The cases \([u,y]\) and \([x,b]\) are initial and upper subintervals. A singleton \([x,x]\) consists of \(x\).

## Rank difference and its arithmetic

The source defines the natural number
\[
\delta(x,y)=\max\{\ell(y)-\ell(x),0\},
\]
where the difference inside the maximum is an integer. For comparable \(x\le y\), length monotonicity makes this
\[
d(x,y)=\ell(y)-\ell(x).
\]

For \(x\le z\le y\), the differences add:
\[
d(x,y)=d(x,z)+d(z,y).
\]
This follows by adding
\((\ell(z)-\ell(x))+(\ell(y)-\ell(z))\); the middle lengths cancel.

For \(u\le x\le y\le b\), apply this twice:
\[
d(u,b)=d(u,x)+d(x,y)+d(y,b).
\]
If \(x\ne u\) or \(y\ne b\), at least one outer term is positive by strict Bruhat length increase. Thus every such proper subinterval has smaller rank.

For \([1,st]\), the rank is two. Its upper interval \([s,st]\) and initial interval \([1,s]\) have rank one, while \([s,s]\) has rank zero.

## Interval order isomorphisms

An interval order isomorphism
\(\phi:[u,b]\to[u',b']\)
is a bijection satisfying
\[
x\le y\quad\Longleftrightarrow\quad\phi(x)\le\phi(y).
\]
Its inverse preserves order as well. It transports a subinterval by restricting to its members, and it transports an interval-indexed function \(f\) by
\[
f'(x')=f(\phi^{-1}(x')).
\]
Composition with \(\phi\) recovers the original function.

The [[node:kl.foundations.rank_preservation|endpoint-and-rank theorem]] proves that the isomorphism carries the named bottom and top to their counterparts and preserves every relative rank \(d(x,y)\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Interval`: [Model.lean:22](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Model.lean#L22).

`OAI.KLInvariance.rankDifference`: [Model.lean:45](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Model.lean#L45).

`OAI.KLInvariance.intervalBottom`: [CanonicalKL.lean:428](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L428).

`OAI.KLInvariance.intervalTop`: [CanonicalKL.lean:431](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L431).

`OAI.KLInvariance.rankDifference_add`: [OrdinaryR.lean:228](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L228).
