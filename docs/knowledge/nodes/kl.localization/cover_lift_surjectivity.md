---
id: kl.local.cover_lift_surjectivity
title: Surjectivity of a lift over a local ring
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.minimal_covers
- kl.algebra.projective_presentations
lean:
  repository: openai-kl
  modules:
  - ModuleAlgebra
  declarations:
  - OAI.KLInvariance.LocalCover.lift_surjective
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:165
    format: lean-location
    note: OAI.KLInvariance.LocalCover.lift_surjective
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read lift_surjective with only Module.Finite on P and no freeness assumptions.
    Expanded the source residue-class construction, the finite cokernel reduction,
    and the determinant form of the standard Nakayama implication invoked there.
tags:
- Kazhdan-Lusztig
- local-decomposition
---

# Surjectivity of a lift over a local ring

Let \(R\) be a commutative local ring with maximal ideal \(\mathfrak m\). Let \(B,P,N\) be \(R\)-modules, with \(P\) finitely generated. Suppose linear maps
\[
\pi:P\to N,\qquad \varphi:B\to N,\qquad g:B\to P
\]
satisfy
\[
\varphi\text{ is surjective},\qquad
\pi g=\varphi,\qquad
\ker\pi\subseteq\mathfrak mP.
\]
Then \(g\) is surjective.

This is lift_surjective. Its conclusion uses finiteness of \(P\); the modules in the statement are otherwise arbitrary.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The same single-lift local-ring argument.**

**OpenAI notes:** The local decomposition lifts the given stalk map through the existing model stalk cover. Minimality makes the lift surjective after reduction modulo the maximal ideal; Nakayama gives surjectivity, the free target supplies a section, and the finite projective kernel is free over the local ring. [loc:decomposition](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L285).

**Lean (primary):** LocalCover first proves the surjectivity of a single lift with a finite target and the displayed kernel condition. It then constructs the lift and right inverse, gives the explicit splitting map and proves the kernel finite projective and free. AboveIso.extend_stalk constructs the common outgoing image and applies this algebraic theorem. [ModuleAlgebra:165](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L165), [ModuleAlgebra:206](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L206), [GradedSheaves:766](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L766).

**Role in the proof:** The Blueprint follows the single-lift proof and writes the cover triangle, splitting inverse, kernel projection and each outgoing restriction equality. The graded two-lift argument belongs to the separate graded construction.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Lift a target vector modulo the maximal ideal

Take \(p\in P\). Surjectivity of \(\varphi\) supplies \(b\in B\) with
\[
\varphi(b)=\pi(p).
\]
Since \(\pi g=\varphi\),
\[
\pi(g(b)-p)=\varphi(b)-\pi(p)=0.
\]
The kernel hypothesis gives \(g(b)-p\in\mathfrak mP\). Hence \(g(b)\) and \(p\) have the same residue in \(P/\mathfrak mP\).

Thus the composite \(B\xrightarrow{g}P\to P/\mathfrak mP\) is surjective.

### Step 2. Express the obstruction as a finite module

Put \(Q=P/\operatorname{im}g\). It is finitely generated because it is a quotient of \(P\).

Step 1 says
\[
P=\operatorname{im}g+\mathfrak mP.
\]
Passing to \(Q\) gives \(Q=\mathfrak mQ\). We now apply the finite local-ring form of Nakayama's lemma, whose calculation is given in Step 3.

### Step 3. Prove the needed Nakayama assertion

Choose generators \(q_1,\ldots,q_n\) of a finitely generated module \(Q\) with
\(Q=\mathfrak mQ\). Express each \(q_i\) as a finite sum of ideal scalars times vectors, then express those vectors in the chosen generators. Collecting coefficients gives
\[
q_i=\sum_{j=1}^n a_{ij}q_j,\qquad a_{ij}\in\mathfrak m.
\]
For the column \(q=(q_i)_i\) and matrix \(A=(a_{ij})\),
\[
(I-A)q=0.
\]
Multiply by the adjugate matrix to obtain
\[
\det(I-A)\,q=0.
\]
Modulo \(\mathfrak m\), the matrix \(I-A\) becomes the identity, so
\(\det(I-A)\equiv1\pmod{\mathfrak m}\). The local-ring unit criterion makes this determinant invertible. Therefore every \(q_i=0\), and \(Q=0\). If the chosen generating family is empty, \(Q=0\) already.

This is the Nakayama implication used by the source's surjectivity-modulo-the-maximal-ideal theorem.

### Step 4. Conclude surjectivity

Apply Step 3 to the quotient \(Q\) from Step 2. Then
\(P/\operatorname{im}g=0\), so \(\operatorname{im}g=P\). Thus every target vector has an actual preimage under \(g\), proving the theorem.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.LocalCover.lift_surjective`: [ModuleAlgebra.lean:165](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L165).
