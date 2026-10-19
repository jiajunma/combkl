---
id: kl.word.coordinate_images
title: Images in sets of module coordinates
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses: []
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.CoordinateProjection.eval
  - OAI.KLInvariance.CoordinateProjection.image
  - OAI.KLInvariance.CoordinateProjection.project
  - OAI.KLInvariance.CoordinateProjection.project_surjective
  - OAI.KLInvariance.CoordinateProjection.project_apply
  - OAI.KLInvariance.CoordinateProjection.project_zero_iff
  - OAI.KLInvariance.CoordinateProjection.restrict
  - OAI.KLInvariance.CoordinateProjection.restrict_project
  - OAI.KLInvariance.CoordinateProjection.restrict_surjective
  - OAI.KLInvariance.CoordinateProjection.restrict_zero_iff
  - OAI.KLInvariance.CoordinateProjection.restrict_joint_injective
  - OAI.KLInvariance.TitsSpace.bottSetImage
  - OAI.KLInvariance.TitsSpace.bottSetProjection
  - OAI.KLInvariance.TitsSpace.bottSetRestrict
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:321
    format: lean-location
    note: OAI.KLInvariance.CoordinateProjection.eval
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:322
    format: lean-location
    note: OAI.KLInvariance.CoordinateProjection.image
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:323
    format: lean-location
    note: OAI.KLInvariance.CoordinateProjection.project
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:325
    format: lean-location
    note: OAI.KLInvariance.CoordinateProjection.project_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:330
    format: lean-location
    note: OAI.KLInvariance.CoordinateProjection.project_apply
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:332
    format: lean-location
    note: OAI.KLInvariance.CoordinateProjection.project_zero_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:341
    format: lean-location
    note: OAI.KLInvariance.CoordinateProjection.restrict
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:350
    format: lean-location
    note: OAI.KLInvariance.CoordinateProjection.restrict_project
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:353
    format: lean-location
    note: OAI.KLInvariance.CoordinateProjection.restrict_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:358
    format: lean-location
    note: OAI.KLInvariance.CoordinateProjection.restrict_zero_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1062
    format: lean-location
    note: OAI.KLInvariance.CoordinateProjection.restrict_joint_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:453
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSetImage
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:459
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSetProjection
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:898
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSetRestrict
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, coordinate sets, kernel maps and induction hypotheses
    explicit?
  verdict: Read generic coordinate eval/image/project/restrict, kernel criteria and
    joint injectivity, then the word instances. Defined actual common-preimage images
    for arbitrary coordinate sets and included the one-edge example.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Images in sets of module coordinates

Let \(R\) be a commutative ring, \(N\) an \(R\)-module, and \(f_x:N\to X_x\) a family of linear maps indexed by a set \(V\). For any subset \(U\subseteq V\), define
\[
E_U:N\to\prod_{x\in U}X_x,\qquad
E_U(n)=(f_x(n))_{x\in U}.
\]
Its coordinate image is
\[
L(U)=\operatorname{im}E_U.
\]
Thus \(z\in L(U)\) means that a single \(n\in N\) satisfies \(f_x(n)=z_x\) for every \(x\in U\). The source calls these maps and modules eval and image.

Restricting the codomain to the image gives the surjection
\[
p_U:N\twoheadrightarrow L(U),\qquad p_U(n)=E_U(n),
\]
called project. Its kernel is
\[
\ker p_U=\{n:f_x(n)=0\text{ for every }x\in U\}.
\]

## Restriction to fewer coordinates

For \(U\subseteq K\), define
\[
r_{K,U}:L(K)\to L(U),\qquad z\mapsto(z_x)_{x\in U}.
\]
This is well defined: a common preimage \(n\) for all coordinates in \(K\) is also a preimage for the selected coordinates in \(U\). It is linear and satisfies
\[
r_{K,U}p_K=p_U.
\]
It is surjective. Given \(z=p_U(n)\), use \(p_K(n)\) as its preimage. Its kernel consists precisely of the image vectors on \(K\) whose coordinates at every \(x\in U\) vanish.

These statements allow arbitrary index sets and subsets; the products consist of coordinate assignments.

## Recovering an image from two restrictions

If \(K=U\cup U'\), the pair of restrictions
\[
L(K)\longrightarrow L(U)\oplus L(U')
\]
is injective. Equal restrictions mean equal coordinates on \(U\) and on \(U'\). Every coordinate of \(K\) occurs in one of these two sets, so the two original assignments agree.

This is the source's restrict_joint_injective lemma. It will identify kernels through their remaining coordinates.

## Word-module coordinate images

For a finite-generator Coxeter system, take \(N=M_{\mathbf t}\), \(R=A\) its symmetric coefficient algebra, and \(f_x=\pi_x:M_{\mathbf t}\to M_{\mathbf t}^x\). Then
\[
L_{\mathbf t}(U)
=\{(\pi_x(m))_{x\in U}:m\in M_{\mathbf t}\}.
\]
The source names this module bottSetImage and its projection bottSetProjection. The restriction maps are bottSetRestrict.

Projecting the finite word basis gives a finite generating family for every image, even when \(U\) is infinite. Indeed, from \(m=\sum_i a_i b_i\), linearity gives
\[
p_U(m)=\sum_i a_i p_U(b_i).
\]
Thus all image vectors are linear combinations of the finitely many projected basis vectors.

For the one-letter word \(s\) over \(A=\mathbb R[\alpha]\),
\[
L_s(\{1,s\})=\{(f,g)\in A^2:f-g\in\alpha A\},\qquad
L_s(\{s\})=A.
\]
Restriction is \((f,g)\mapsto g\), and the common-preimage description explains its surjectivity.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.CoordinateProjection.eval`: [IntegralPairings.lean:321](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L321).

`OAI.KLInvariance.CoordinateProjection.image`: [IntegralPairings.lean:322](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L322).

`OAI.KLInvariance.CoordinateProjection.project`: [IntegralPairings.lean:323](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L323).

`OAI.KLInvariance.CoordinateProjection.project_surjective`: [IntegralPairings.lean:325](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L325).

`OAI.KLInvariance.CoordinateProjection.project_apply`: [IntegralPairings.lean:330](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L330).

`OAI.KLInvariance.CoordinateProjection.project_zero_iff`: [IntegralPairings.lean:332](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L332).

`OAI.KLInvariance.CoordinateProjection.restrict`: [IntegralPairings.lean:341](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L341).

`OAI.KLInvariance.CoordinateProjection.restrict_project`: [IntegralPairings.lean:350](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L350).

`OAI.KLInvariance.CoordinateProjection.restrict_surjective`: [IntegralPairings.lean:353](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L353).

`OAI.KLInvariance.CoordinateProjection.restrict_zero_iff`: [IntegralPairings.lean:358](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L358).

`OAI.KLInvariance.CoordinateProjection.restrict_joint_injective`: [IntegralPairings.lean:1062](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1062).

`OAI.KLInvariance.TitsSpace.bottSetImage`: [IntegralPairings.lean:453](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L453).

`OAI.KLInvariance.TitsSpace.bottSetProjection`: [IntegralPairings.lean:459](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L459).

`OAI.KLInvariance.TitsSpace.bottSetRestrict`: [IntegralPairings.lean:898](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L898).
