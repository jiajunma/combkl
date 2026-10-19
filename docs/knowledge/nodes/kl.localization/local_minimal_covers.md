---
id: kl.local.minimal_covers
title: Minimal free covers over a local ring
kind: definition
status: formalized
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.algebra.projective_presentations
lean:
  repository: openai-kl
  modules:
  - ModuleAlgebra
  declarations:
  - OAI.KLInvariance.LocalCover.lift_surjective
  - OAI.KLInvariance.LocalCover.exists_split_minimal_cover
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:165
    format: lean-location
    note: OAI.KLInvariance.LocalCover.lift_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:206
    format: lean-location
    note: OAI.KLInvariance.LocalCover.exists_split_minimal_cover
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the exact local-ring cover hypotheses of LocalCover.lift_surjective
    and exists_split_minimal_cover. Defined the residue module, proved the preimage
    identity and equivalence with residue-field minimality, and separated a minimal
    rank-one quotient from a free cover with an extra generator.
tags:
- Kazhdan-Lusztig
- local-decomposition
---

# Minimal free covers over a local ring

Let \(R\) be a commutative local ring with maximal ideal \(\mathfrak m\) and residue field \(k=R/\mathfrak m\). For an \(R\)-module \(M\), its residue module is
\[
\overline M=M/\mathfrak mM.
\]
It is a \(k\)-vector space: a scalar class \([r]\) acts by \([m]\mapsto[rm]\).

A **local minimal free cover** of \(N\) is a surjective \(R\)-linear map
\[
\pi:P\longrightarrow N
\]
such that \(P\) is finite free and
\[
\ker\pi\subseteq\mathfrak mP.
\]
These are the cover hypotheses used by the source's LocalCover splitting theorem.

## Minimality after residue-field reduction

Surjectivity of \(\pi\) implies
\[
\pi^{-1}(\mathfrak mN)=\mathfrak mP+\ker\pi.
\]
For the nontrivial containment, write \(\pi(p)\) as a finite sum
\(\sum_i a_i n_i\), with \(a_i\in\mathfrak m\), and choose \(p_i\) with
\(\pi(p_i)=n_i\). Then \(p-\sum_i a_ip_i\) is in the kernel.

Consequently the induced surjection
\[
\overline\pi:P/\mathfrak mP\longrightarrow N/\mathfrak mN
\]
is an isomorphism exactly when \(\ker\pi\subseteq\mathfrak mP\). Thus the images of a basis of \(P\) form a basis of \(N/\mathfrak mN\). Each basis vector contributes a generator that remains necessary after reduction.

For a local boundary model \(O_c\) at \(x\ne c\), the stalk map onto its outgoing image is such a cover. Its local minimality field supplies the kernel inclusion.

## A quotient by one label

If \(\alpha\in\mathfrak m\), the quotient
\[
R\longrightarrow R/(\alpha)
\]
is a local minimal free cover. Its kernel is \(\alpha R\subseteq\mathfrak m\), and both residue modules are \(k\).

For \(R=k[t]_{(t)}\), the map \(R^2\to R/(t)\) given by
\((u,v)\mapsto[u]\) is a finite free cover with an additional generator: the vector \((0,1)\) is in its kernel and has nonzero residue in \(k^2\). The [[node:kl.local.cover_splitting|local cover-splitting theorem]] isolates that extra direction as a finite free summand.

## The local-ring unit criterion

An element of \(R\) is a unit exactly when it lies outside \(\mathfrak m\). A nonunit generates a proper ideal, contained in a maximal ideal; uniqueness puts it in \(\mathfrak m\). Conversely a unit cannot belong to a proper ideal.

This criterion is used in the Nakayama argument: an element congruent to \(1\) modulo \(\mathfrak m\) is a unit. It is the algebraic mechanism that turns surjectivity after reduction into surjectivity of a map onto a finitely generated module.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The same single-lift local-ring argument.**

**OpenAI notes:** The local decomposition lifts the given stalk map through the existing model stalk cover. Minimality makes the lift surjective after reduction modulo the maximal ideal; Nakayama gives surjectivity, the free target supplies a section, and the finite projective kernel is free over the local ring. [loc:decomposition](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L285).

**Lean (primary):** LocalCover first proves the surjectivity of a single lift with a finite target and the displayed kernel condition. It then constructs the lift and right inverse, gives the explicit splitting map and proves the kernel finite projective and free. AboveIso.extend_stalk constructs the common outgoing image and applies this algebraic theorem. [ModuleAlgebra:165](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L165), [ModuleAlgebra:206](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L206), [GradedSheaves:766](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L766).

**Role in the proof:** The Blueprint follows the single-lift proof and writes the cover triangle, splitting inverse, kernel projection and each outgoing restriction equality. The graded two-lift argument belongs to the separate graded construction.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.LocalCover.lift_surjective`: [ModuleAlgebra.lean:165](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L165).

`OAI.KLInvariance.LocalCover.exists_split_minimal_cover`: [ModuleAlgebra.lean:206](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L206).
