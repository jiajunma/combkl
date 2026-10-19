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
- kl.word.evaluation_grading
- kl.detail.coefficient_change
- kl.sheaves.graded_module
- kl.detail.graded_sheaf
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  - Decomposition
  - Frobenius
  - Support
  declarations:
  - OAI.KLInvariance.TitsSpace.bottProjectionSheaf
  - OAI.KLInvariance.PairProjection.relation
  - OAI.KLInvariance.PairProjection.compatible_iff
  - OAI.KLInvariance.TitsSpace.bottWordData
  - OAI.KLInvariance.TitsSpace.bottStalkData
  - OAI.KLInvariance.TitsSpace.bottStalkHom
  - OAI.KLInvariance.TitsSpace.bottEdgeData
  - OAI.KLInvariance.TitsSpace.bottLowerHom
  - OAI.KLInvariance.TitsSpace.bottUpperHom
  - OAI.KLInvariance.TitsSpace.bottGradedProjectionSheaf
  - OAI.KLInvariance.TitsSpace.bottPolynomialSheaf
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
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1449
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottWordData
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1427
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkData
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1459
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkHom
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1468
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEdgeData
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1472
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottLowerHom
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1477
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottUpperHom
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1482
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottGradedProjectionSheaf
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:417
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottPolynomialSheaf
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

Fix a finite-generator Coxeter system, its real extended realization \(V\), and a Bruhat interval \([u,b]\). Let \(M_{\mathbf s}\) be a Bott–Samelson word module over \(A=\operatorname{Sym}_{\mathbb R}(V)\), and let
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

For a reduced word, the [[node:kl.detail.word_flabbiness|word-lifting theorem]] proves that every compatible global section arises this way. Full evaluation is injective, so the section map is then an isomorphism. This identifies sheaf endomorphisms with word-module endomorphisms preserving the coordinate conditions.

## Graded maps and pair quotients

The evaluation projections preserve degree, and their image stalks inherit the image grading. Each pair relation is a homogeneous image, so its edge quotient has the quotient grading. Both restriction maps have degree zero.

An endomorphism of the word module preserving the kernels of both endpoint projections descends to their stalks. The quotient-descent theorem then supplies an edge endomorphism satisfying both commuting squares. This construction is used to turn the integral word adjoint into a graded sheaf endomorphism.

## The actual finite graded module data

Choose a finite basis of \(V\) and use the associated degree-one grading of \(A\). The source packages the constructions as follows.

| Construction | Module or map |
|---|---|
| `bottWordData` | The tensor word module with its word-basis grading. |
| `bottStalkData` | The evaluation image stalk with its coordinatewise image grading. |
| `bottStalkHom` | The degree-zero surjection from the word module to the stalk. |
| `bottEdgeData` | The graded quotient of the two endpoint stalks by their simultaneous image. |
| `bottLowerHom` and `bottUpperHom` | The degree-zero lower and upper maps into that quotient. |
| `bottGradedProjectionSheaf` | These vertex modules, edge modules and restrictions, assembled on the interval. |

The word module is finitely generated by its finite tensor basis. Its stalks are finite images, and the edge quotient is a quotient of the direct sum of two finite stalks.

The gradings are nonnegative. For a negative-degree word vector, every evaluation lies in a negative coefficient piece, hence is zero; evaluation injectivity forces the word vector to be zero. For a negative-degree stalk vector, every coordinate is zero. The pair quotient inherits nonnegativity from the two stalks.

These facts supply the finite graded module data used at every vertex and edge.

## Polynomial coordinates

The chosen basis induces a graded isomorphism
\[
e:A\xrightarrow{\sim}P,\qquad
P=\mathbb R[X_i:i\text{ indexes the basis}].
\]
The polynomial word sheaf transports each vertex and edge module through \(e\), and transports the restriction maps by their underlying functions. Its \(P\)-action on an old vector is \(p\cdot m=e^{-1}(p)m\). This is `bottPolynomialSheaf`.

Write \(S_P\) for this polynomial sheaf. A symmetric root label \(\alpha_E\) becomes the linear coordinate polynomial \(e(\alpha_E)\). The [[node:kl.sheaves.word_polynomial_stalks|polynomial word-stalk theorem]] proves that this transport preserves stalk freeness and gives the exact upper edge kernel \(e(\alpha_E)S_P^y\).

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization



`OAI.KLInvariance.TitsSpace.bottProjectionSheaf`: [Frobenius.lean:1761](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1761).

`OAI.KLInvariance.PairProjection.relation`: [Decomposition.lean:153](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L153).

`OAI.KLInvariance.PairProjection.compatible_iff`: [Decomposition.lean:168](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L168).

`OAI.KLInvariance.TitsSpace.bottWordData`: [BottSamelson.lean:1449](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1449).

`OAI.KLInvariance.TitsSpace.bottStalkData`: [BottSamelson.lean:1427](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1427).

`OAI.KLInvariance.TitsSpace.bottStalkHom`: [BottSamelson.lean:1459](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1459).

`OAI.KLInvariance.TitsSpace.bottEdgeData`: [BottSamelson.lean:1468](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1468).

`OAI.KLInvariance.TitsSpace.bottLowerHom`: [BottSamelson.lean:1472](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1472).

`OAI.KLInvariance.TitsSpace.bottUpperHom`: [BottSamelson.lean:1477](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1477).

`OAI.KLInvariance.TitsSpace.bottGradedProjectionSheaf`: [BottSamelson.lean:1482](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1482).

`OAI.KLInvariance.TitsSpace.bottPolynomialSheaf`: [Support.lean:417](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L417).
