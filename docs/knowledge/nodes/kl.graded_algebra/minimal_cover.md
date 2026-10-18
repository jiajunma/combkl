---
id: kl.sheaves.minimal_cover
title: Minimal graded free covers
kind: definition
status: formalized
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.sheaves.graded_module
- kl.algebra.positive_ideal
lean:
  repository: openai-kl
  modules:
  - GradedModules
  declarations:
  - OAI.KLInvariance.Graded.ModuleData.MinimalCover
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1175
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.MinimalCover
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
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
- background
---

# Minimal graded free covers

Let \(A\) be a nonnegatively graded commutative \(k\)-algebra, and let \(A_+\) be its positive ideal. Let \(M\) be a finite nonnegatively graded \(A\)-module.

A minimal graded free cover consists of a finite nonnegatively graded free module \(F\) and a surjective degree-zero \(A\)-linear map
\[
\pi:F\longrightarrow M
\]
with
\[
\ker\pi\subseteq A_+F.
\]
These conditions specify the source, its freeness, the homogeneous map, its surjectivity, and the minimality of its kernel.

## Reduction modulo the positive ideal

The map induces
\[
\overline\pi:F/A_+F\longrightarrow M/A_+M.
\]
It is surjective because \(\pi\) is. It is also injective. If \(\pi(f)\in A_+M\), express \(\pi(f)=\sum_j a_jm_j\) with \(a_j\in A_+\). Lift each \(m_j\) to \(f_j\in F\). Then
\[
f-\sum_j a_jf_j\in\ker\pi\subseteq A_+F.
\]
Since \(\sum_j a_jf_j\in A_+F\), it follows that \(f\in A_+F\). Thus \(\overline\pi\) is an isomorphism.

When \(A_0=k\), a homogeneous basis of \(F\) consequently reduces to a homogeneous \(k\)-basis of \(M/A_+M\). This is the precise sense in which the cover chooses the necessary generators and their degrees.

## Constructing the cover

For a polynomial coefficient algebra, choose a homogeneous basis of \(M/A_+M\), lift its elements homogeneously to \(M\), and give a free generator the degree of each lift. Sending those free generators to the chosen lifts defines a degree-zero map.

The graded Nakayama theorem proves surjectivity, and reduction to the chosen basis shows its kernel lies in \(A_+F\). The detailed construction is [[node:kl.notes.minimal_cover_existence]].

For \(A=k[X]\) and \(M=A/(X)\), the quotient map \(A\to A/(X)\) is a minimal cover: its kernel is \(XA=A_+A\), and both reductions are \(k\). If \(M=Ae_0\oplus Ae_2\), the identity is a minimal cover and the degrees of its reduced generators are zero and two.

Boundary sheaves apply this construction to the boundary image at a vertex. The chosen free source becomes the new stalk, and the cover map supplies its outgoing restrictions.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

The fields are `source` for (F), `free` for its freeness, `hom` for the graded map, `surjective` for surjectivity, and `minimal` for the kernel containment.

`OAI.KLInvariance.Graded.ModuleData.MinimalCover`: [GradedModules.lean:1175](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1175).
