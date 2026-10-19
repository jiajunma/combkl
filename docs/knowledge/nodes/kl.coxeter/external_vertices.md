---
id: kl.coxeter.external_vertices
title: External lower vertices and their parity classes
kind: definition
status: formalized
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.foundations.bruhat_order
- kl.foundations.interval
- kl.coxeter.word_data
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.externalLower
  - OAI.KLInvariance.mem_externalLower
  - OAI.KLInvariance.Dihedral.oppositeExternal
  - OAI.KLInvariance.Dihedral.sameExternal
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:275
    format: lean-location
    note: OAI.KLInvariance.externalLower
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:279
    format: lean-location
    note: OAI.KLInvariance.mem_externalLower
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:235
    format: lean-location
    note: OAI.KLInvariance.Dihedral.oppositeExternal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:239
    format: lean-location
    note: OAI.KLInvariance.Dihedral.sameExternal
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the general finite set difference and its membership theorem, then
    both dihedral parity filters. Kept x<=c as the later theorem hypothesis rather
    than a restriction on the definition.
tags:
- Kazhdan-Lusztig
- interpolation
---

# External lower vertices and their parity classes

Let \(W\) be a Coxeter system with length \(\ell\) and strong Bruhat order. For \(x,c\in W\), define the finite **external lower set**
\[
E(x,c)=[1,c]\setminus[1,x]
=\{z:z\le c,\ z\not\le x\}.
\]
This is externalLower. The definition makes sense for any \(x,c\); the parity comparison used later assumes \(x\le c\).

Partition it according to the parity of \(\ell(x)\):
\[
Y(x,c)=\{z\in E(x,c):\ell(z)\not\equiv\ell(x)\pmod2\},
\]
\[
Z(x,c)=\{z\in E(x,c):\ell(z)\equiv\ell(x)\pmod2\}.
\]
These are the opposite-parity and same-parity external vertices. The source names these two filters oppositeExternal and sameExternal in its dihedral interpolation section.

Every external vertex belongs to exactly one of \(Y,Z\). In particular, \(x\) belongs to neither class, since \(x\le x\).

## A two-generator example

Take a reduced word \(st\) and \(x=s,\ c=st\). The lower intervals are
\[
[1,st]=\{1,s,t,st\},\qquad [1,s]=\{1,s\}.
\]
Thus \(E(s,st)=\{t,st\}\). Since \(\ell(s)=1\),
\[
Y(s,st)=\{st\},\qquad Z(s,st)=\{t\}.
\]

For \(x=c\), the external set is empty. For \(x=1\), it consists of all nonidentity vertices below \(c\).

The [[node:kl.coxeter.lower_interval_parity|lower-interval parity theorem]] proves \(|Z(x,c)|\le|Y(x,c)|\) when \(x\le c\). In a dihedral system, the opposite-parity class corresponds to the outgoing reflection edges from \(x\) whose targets lie below \(c\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.externalLower`: [SheafMorphisms.lean:275](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L275).

`OAI.KLInvariance.mem_externalLower`: [SheafMorphisms.lean:279](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L279).

`OAI.KLInvariance.Dihedral.oppositeExternal`: [DihedralIntervals.lean:235](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L235).

`OAI.KLInvariance.Dihedral.sameExternal`: [DihedralIntervals.lean:239](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L239).
