---
id: kl.local.cover_splitting
title: A finite free cover splits over a local minimal cover
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.minimal_covers
- kl.local.cover_lift_surjectivity
- kl.algebra.projective_presentations
lean:
  repository: openai-kl
  modules:
  - ModuleAlgebra
  declarations:
  - OAI.KLInvariance.LocalCover.splitEquiv
  - OAI.KLInvariance.LocalCover.exists_split_minimal_cover
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:184
    format: lean-location
    note: OAI.KLInvariance.LocalCover.splitEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:206
    format: lean-location
    note: OAI.KLInvariance.LocalCover.exists_split_minimal_cover
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the single projective lift, lift_surjective, chosen right inverse,
    explicit splitEquiv, finite kernel projection and split-projective kernel in exists_split_minimal_cover.
    Expanded the standard finite-projective-over-local-ring implication and checked
    the quotient triangle and a rank-two example.
tags:
- Kazhdan-Lusztig
- local-decomposition
---

# A finite free cover splits over a local minimal cover

Let \(R\) be a commutative local ring with maximal ideal \(\mathfrak m\). Let \(B,P\) be finite free \(R\)-modules, \(N\) an \(R\)-module, and
\[
\pi:P\to N,\qquad \varphi:B\to N
\]
surjective linear maps. Assume \(\ker\pi\subseteq\mathfrak mP\).

There is a surjective lift \(g:B\to P\), with \(\pi g=\varphi\), and a linear isomorphism
\[
e:B\xrightarrow{\sim}P\oplus Q,\qquad Q=\ker g,
\]
such that \(Q\) is finite free and
\[
(e(b))_1=g(b),\qquad \pi((e(b))_1)=\varphi(b).
\]
Thus the original map becomes \((\pi,0)\) under this isomorphism.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The same single-lift local-ring argument.**

**OpenAI notes:** The local decomposition lifts the given stalk map through the existing model stalk cover. Minimality makes the lift surjective after reduction modulo the maximal ideal; Nakayama gives surjectivity, the free target supplies a section, and the finite projective kernel is free over the local ring. [loc:decomposition](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L285).

**Lean (primary):** LocalCover first proves the surjectivity of a single lift with a finite target and the displayed kernel condition. It then constructs the lift and right inverse, gives the explicit splitting map and proves the kernel finite projective and free. AboveIso.extend_stalk constructs the common outgoing image and applies this algebraic theorem. [ModuleAlgebra:165](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L165), [ModuleAlgebra:206](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L206), [GradedSheaves:766](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L766).

**Role in the proof:** The Blueprint follows the single-lift proof and writes the cover triangle, splitting inverse, kernel projection and each outgoing restriction equality. The graded two-lift argument belongs to the separate graded construction.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Construct the lift from a basis of the source

Choose a basis of \(B\). For each basis vector \(b_i\), surjectivity of \(\pi\) supplies \(p_i\in P\) with \(\pi(p_i)=\varphi(b_i)\). Extend \(b_i\mapsto p_i\) linearly to obtain \(g:B\to P\).

The equality \(\pi g=\varphi\) holds on the basis, hence on every vector. This is the projective lifting step in the source.

### Step 2. Prove the lift surjective and choose a section

The [[node:kl.local.cover_lift_surjectivity|local lift-surjectivity theorem]] applies: \(P\) is finite, \(\varphi\) is onto, the triangle commutes, and \(\ker\pi\subseteq\mathfrak mP\). Hence \(g\) is onto.

Choose a preimage under \(g\) of each basis vector of \(P\), and extend linearly. This gives a section \(s:P\to B\) with \(gs=1_P\).

### Step 3. Write the splitting and its inverse

Set \(Q=\ker g\). Define
\[
e(b)=(g(b),\,b-s(g(b))).
\]
The second coordinate belongs to \(Q\), since
\(g(b-s(g(b)))=g(b)-g(b)=0\).

The inverse is
\[
e^{-1}(p,q)=s(p)+q.
\]
For \(b\in B\), it gives \(s(g(b))+b-s(g(b))=b\). For \((p,q)\), the first component is \(g(s(p)+q)=p\), and the second is \(s(p)+q-s(p)=q\). These formulas also show linearity.

### Step 4. Prove finiteness and projectivity of the kernel

The projection
\[
k:B\to Q,\qquad k(b)=b-s(g(b))
\]
is onto, since \(k(q)=q\) for \(q\in Q\). Images of a finite generating family of \(B\) therefore generate \(Q\).

Let \(i:Q\hookrightarrow B\) be inclusion. The identity \(ki=1_Q\) makes \(Q\) a direct summand of the free module \(B\), hence projective. Explicitly, a lifting problem for \(Q\) extends to one for \(B\) by composing with \(k\); solve it on the free basis of \(B\) and restrict along \(i\).

### Step 5. Obtain a basis over the local ring

The source uses the fact that a finite projective module over a local ring is free. The underlying local argument is as follows.

Choose a basis of the finite-dimensional residue space \(Q/\mathfrak mQ\), and lift it to vectors \(q_1,\ldots,q_n\in Q\). The resulting map \(h:R^n\to Q\) is onto modulo \(\mathfrak m\). Its finite cokernel has zero residue module, so the Nakayama calculation in the [[node:kl.local.cover_lift_surjectivity|local lift-surjectivity theorem]] makes \(h\) onto.

Projectivity of \(Q\) splits \(h\), giving \(R^n\simeq Q\oplus L\), where \(L=\ker h\). The complementary projection makes \(L\) finitely generated. Reducing this direct sum modulo \(\mathfrak m\), the map induced by \(h\) is the basis isomorphism
\[
(R/\mathfrak m)^n\simeq Q/\mathfrak mQ.
\]
Its kernel is \(L/\mathfrak mL\), so that quotient is zero. Nakayama gives \(L=0\). Hence \(h\) is an isomorphism and the lifted vectors form a basis of \(Q\).

### Step 6. Check the map to the common image

The first coordinate of \(e(b)\) is \(g(b)\) by definition. Therefore
\[
\pi((e(b))_1)=\pi(g(b))=\varphi(b).
\]
For \(q\in Q\), \(\varphi(q)=\pi(g(q))=0\). The map to \(N\) is consequently \((p,q)\mapsto\pi(p)\).

### Step 7. Calculate a rank-two example

Take \(R=k[t]_{(t)}\) over a field \(k\), \(P=R\), \(N=R/(t)\), the quotient map \(\pi(p)=[p]\), and
\(\varphi:R^2\to N\), \(\varphi(u,v)=[u]\). One lift is
\[
g(u,v)=u+tv,
\]
because \([u+tv]=[u]\). Use \(s(p)=(p,0)\). Then
\[
Q=\{(-tv,v):v\in R\},
\]
with basis \((-t,1)\). In that basis, the splitting is
\[
(u,v)\longmapsto(u+tv,v),\qquad
(p,q)\longmapsto(p-tq,q).
\]
The quotient map becomes \((p,q)\mapsto[p]\), displaying the extra free direction explicitly.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.LocalCover.splitEquiv`: [ModuleAlgebra.lean:184](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L184).

`OAI.KLInvariance.LocalCover.exists_split_minimal_cover`: [ModuleAlgebra.lean:206](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L206).
