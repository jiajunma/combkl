---
id: kl.detail.word_sheaf
title: The pair-projection sheaf of a Bott–Samelson module
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.notes.bott_samelson
- kl.notes.word_stalks
- kl.sheaves.graph_sheaf
- kl.algebra.pair_projection
lean:
  repository: openai-kl
  modules:
  - Frobenius
  - Decomposition
  declarations:
  - OAI.KLInvariance.TitsSpace.bottProjectionSheaf
  - OAI.KLInvariance.PairProjection.relation
  - OAI.KLInvariance.PairProjection.compatible_iff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1761
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottProjectionSheaf
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:153
    format: lean-location
    note: OAI.KLInvariance.PairProjection.relation
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:168
    format: lean-location
    note: OAI.KLInvariance.PairProjection.compatible_iff
  - artifact: openai-kl-paper
    locator: Related paper context; bg:normalization
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
- duality_and_characters
---

# The pair-projection sheaf of a Bott–Samelson module

Let \(M_{\mathbf s}\) be a Bott–Samelson word module over the symmetric coefficient algebra \(A\), and let
\(\pi_x:M_{\mathbf s}\twoheadrightarrow M_{\mathbf s}^x\) be its weight-stalk projections. On an edge \(e:x\to y\), form the pair-projection quotient
\[
B^e=(M_{\mathbf s}^x\oplus M_{\mathbf s}^y)/
\operatorname{im}(\pi_x,\pi_y).
\]
The lower map sends \(v\) to \([(v,0)]\), and the upper map sends \(w\) to \(-[(0,w)]\). The pair-projection calculation gives
\[
\rho^-_e(v)=\rho^+_e(w)
\quad\Longleftrightarrow\quad
\exists m\in M_{\mathbf s},\ (\pi_x(m),\pi_y(m))=(v,w).
\]
Thus edge compatibility expresses simultaneous lifting of the two endpoint values.

For one reflection, the full evaluation image is
\(\{(f,g):f-g\in\alpha A\}\). Both stalk images are \(A\), and the quotient above is \(A/(\alpha)\), via \([(f,g)]\mapsto f-g\bmod\alpha\). The lower and upper maps both become reduction modulo \(\alpha\).

## Sections supplied by word elements

Every \(m\in M_{\mathbf s}\) gives a global section \((\pi_x(m))_x\), because it lifts its own two projections on every edge. Since each stalk projection is onto its image, these global sections generate every stalk.

For a reduced word, the word-lifting theorem proves that every compatible global section arises this way. Full evaluation is injective, so the section map is then an isomorphism. This identifies sheaf endomorphisms with word-module endomorphisms preserving the coordinate conditions.

## Graded maps and pair quotients

The evaluation projections preserve degree, and their image stalks inherit the image grading. Each pair relation is a homogeneous image, so its edge quotient has the quotient grading. Both restriction maps have degree zero.

An endomorphism of the word module preserving the kernels of both endpoint projections descends to their stalks. The quotient-descent theorem then supplies an edge endomorphism satisfying both commuting squares. This construction is used to turn the integral word adjoint into a graded sheaf endomorphism.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization



`OAI.KLInvariance.TitsSpace.bottProjectionSheaf`: [Frobenius.lean:1761](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1761).

`OAI.KLInvariance.PairProjection.relation`: [Decomposition.lean:153](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L153).

`OAI.KLInvariance.PairProjection.compatible_iff`: [Decomposition.lean:168](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L168).
