---
id: kl.notes.word_stalks
title: Weight-stalk images and supported word elements
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.notes.bott_samelson
- kl.algebra.coefficient_algebra
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.TitsSpace.bottWeightProjection
  - OAI.KLInvariance.TitsSpace.bottStalk
  - OAI.KLInvariance.TitsSpace.bottStalkProjection
  - OAI.KLInvariance.TitsSpace.bottStalkProjection_surjective
  - OAI.KLInvariance.TitsSpace.bottWeightSupported
  - OAI.KLInvariance.TitsSpace.bottCoordinateDenominator
  - OAI.KLInvariance.TitsSpace.bottCoordinateLift
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1497
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottWeightProjection
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1558
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalk
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1562
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkProjection
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1566
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkProjection_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1403
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottWeightSupported
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1317
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCoordinateDenominator
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1448
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCoordinateLift
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the mathematical hypotheses and scope retained from the referenced declarations?
  verdict: The exposition follows the fixed Lean source; worked calculations explain
    the constructions.
tags:
- Kazhdan-Lusztig
- background
---

# Weight-stalk images and supported word elements

Fix a finite-generator Coxeter system, its extended realization, and the symmetric coefficient algebra \(A\). Let \(\mathbf s\) be a word, let \(M_{\mathbf s}\) be its Bott–Samelson module, and let \(J\) be its finite set of subexpressions.

Every subexpression \(\varepsilon\) has a group weight \(w(\varepsilon)\) and an \(A\)-linear evaluation \(E_\varepsilon:M_{\mathbf s}\to A\). For a group element \(x\), put
\[
J_x=\{\varepsilon\in J:w(\varepsilon)=x\}.
\]
Collecting these coordinates gives
\[
E_x:M_{\mathbf s}\longrightarrow A^{J_x},
\qquad m\longmapsto(E_\varepsilon(m))_{\varepsilon\in J_x}.
\]

The weight stalk is the image module
\[
M_{\mathbf s}^x=\operatorname{im}E_x\subseteq A^{J_x}.
\]
Its stalk projection is the same evaluation with codomain restricted to the image:
\[
\pi_x:M_{\mathbf s}\twoheadrightarrow M_{\mathbf s}^x.
\]
Surjectivity holds because membership in the image supplies a word element with exactly those coordinates.

## Elements supported at one weight

The weight-supported submodule is
\[
S_x=\{m\in M_{\mathbf s}:E_\varepsilon(m)=0
                 \text{ whenever }w(\varepsilon)\ne x\}.
\]
It is a submodule of the original word module. The stalk \(M_{\mathbf s}^x\), by contrast, consists of the selected coordinate tuples obtained by projecting arbitrary word elements.

The evaluation kernel is
\[
\ker\pi_x=\{m:E_\varepsilon(m)=0
                       \text{ whenever }w(\varepsilon)=x\}.
\]
Thus support at \(x\) means vanishing outside the \(x\)-block, while the projection kernel means vanishing on the \(x\)-block. The perfect word pairing relates these two conditions through annihilators.

## One reflection

For the one-letter word \(s\), the evaluations of a pure tensor are
\[
E_0(a\otimes b)=ab,\qquad E_1(a\otimes b)=a\,s(b).
\]
Write \(\alpha\) for the root polynomial, with \(s(\alpha)=-\alpha\). In the left-module basis \(1\otimes1,1\otimes\alpha\), a vector with coefficients \(u,v\in A\) evaluates to
\[
(u+\alpha v,\ u-\alpha v).
\]
Its two coordinates differ by \(2\alpha v\). Conversely, if \(f-g\in\alpha A\), then
\[
u=(f+g)/2,\qquad v=(f-g)/(2\alpha)
\]
belong to \(A\) and reconstruct the pair. Hence full evaluation identifies this word module with
\[
\{(f,g)\in A^2:f-g\in\alpha A\}.
\]

Each individual weight stalk is \(A\), because diagonal pairs attain every coordinate. Supported elements are the pairs \((\alpha h,0)\) and \((0,\alpha h)\). This is the word-module source of the one-edge sheaf example.

## Scaled coordinate data

In the standard word basis, full evaluation has a square matrix \(E\). Its determinant
\[
\Delta=\det E
\]
is the evaluation denominator. A scaled coordinate lift \(c_\varepsilon\) is a word element with full evaluation \(\Delta\) in coordinate \(\varepsilon\) and zero in every other coordinate.

The theorem [[node:kl.word.scaled_coordinate_lifts]] proves \(\Delta\ne0\), constructs these elements by the adjugate matrix, and derives a reconstruction formula for \(\Delta m\).

## Subsequent constructions

The injectivity theorem identifies a word element by all its evaluations. Scaled coordinate lifts provide explicit supported elements after multiplication by a common polynomial. The support-duality theorem identifies \(S_x\) with the \(A\)-linear dual of the actual image stalk \(M_{\mathbf s}^x\). Pairing the projections at adjacent vertices then defines the edge quotients of the word sheaf.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottWeightProjection`: [Frobenius.lean:1497](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1497).

`OAI.KLInvariance.TitsSpace.bottStalk`: [Frobenius.lean:1558](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1558).

`OAI.KLInvariance.TitsSpace.bottStalkProjection`: [Frobenius.lean:1562](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1562).

`OAI.KLInvariance.TitsSpace.bottStalkProjection_surjective`: [Frobenius.lean:1566](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1566).

`OAI.KLInvariance.TitsSpace.bottWeightSupported`: [Frobenius.lean:1403](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1403).

`OAI.KLInvariance.TitsSpace.bottCoordinateDenominator`: [Frobenius.lean:1317](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1317).

`OAI.KLInvariance.TitsSpace.bottCoordinateLift`: [Frobenius.lean:1448](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1448).
