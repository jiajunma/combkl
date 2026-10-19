---
id: kl.detail.integral_adjoints
title: Integral adjoints for a perfect pairing
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.notes.perfect_pairings
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.PerfectAdjoint.adjoint
  - OAI.PerfectAdjoint.pairing
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2220
    format: lean-location
    note: OAI.PerfectAdjoint.adjoint
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2223
    format: lean-location
    note: OAI.PerfectAdjoint.pairing
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# Integral adjoints for a perfect pairing

Let \(R\) be a commutative ring, \(M\) an \(R\)-module, and
\[
D:M\xrightarrow{\sim}M^*,\qquad
\langle m,n\rangle=D(m)(n)
\]
a perfect pairing. Given an \(R\)-linear endomorphism \(f:M\to M\), its dual map is precomposition:
\[
f^\vee:M^*\to M^*,\qquad f^\vee(\lambda)=\lambda\circ f.
\]
The adjoint of \(f\) is the endomorphism
\[
f^*=D^{-1}\circ f^\vee\circ D.
\]

For each \(m\), this formula represents the functional \(n\mapsto\langle m,fn\rangle\) by its unique first argument. Thus
\[
\langle f^*m,n\rangle=\langle m,fn\rangle.
\]
The equivalence \(D\) and its inverse are \(R\)-linear, so the adjoint is defined over \(R\).

## The matrix formula

Choose a finite free basis and let \(G_{ij}=\langle b_i,b_j\rangle\). For column vectors, the pairing is \(m^{\mathsf T}Gn\). If \(F\) represents \(f\) and \(F^*\) represents its adjoint, the defining equation reads
\[
(F^*)^{\mathsf T}G=GF.
\]
Perfection makes \(G\) invertible over \(R\), so
\[
F^*=(G^{\mathsf T})^{-1}F^{\mathsf T}G^{\mathsf T}.
\]
For a symmetric pairing, this simplifies to \(F^*=G^{-1}F^{\mathsf T}G\).

## A projector and its adjoint

Take \(M=R^2\) with
\[
\langle(a,b),(c,d)\rangle=ad+bc,\qquad
G=\begin{pmatrix}0&1\\ 1&0\end{pmatrix}.
\]
The projector \(e(a,b)=(a,0)\) has adjoint \(e^*(a,b)=(0,b)\), because
\[
\langle e^*(a,b),(c,d)\rangle=bc
=\langle(a,b),e(c,d)\rangle.
\]
Its image and adjoint image are the two coordinate lines. Pairing between them is multiplication of their coordinates, and hence perfect.

Composition, idempotence, symmetry, and grading properties of adjoints are proved in [[node:kl.sheaves.adjoint_properties]]. The image-duality construction gives the corresponding equivalence for an arbitrary split module.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.PerfectAdjoint.adjoint`: [IntegralPairings.lean:2220](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2220).

`OAI.PerfectAdjoint.pairing`: [IntegralPairings.lean:2223](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2223).
