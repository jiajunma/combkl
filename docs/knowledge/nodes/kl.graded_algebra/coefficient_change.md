---
id: kl.detail.coefficient_change
title: Transport of coefficients along an algebra isomorphism
kind: definition
status: formalized
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.sheaves.graded_module
- kl.algebra.homogeneous_subquotients
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  - Support
  declarations:
  - OAI.KLInvariance.CoefficientChange
  - OAI.KLInvariance.CoefficientChange.equiv
  - OAI.KLInvariance.CoefficientChange.kEquiv
  - OAI.KLInvariance.Graded.ModuleData.change
  - OAI.KLInvariance.Graded.ModuleData.changeHom
  - OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange
  - OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChangeSections
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1777
    format: lean-location
    note: OAI.KLInvariance.CoefficientChange
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1805
    format: lean-location
    note: OAI.KLInvariance.CoefficientChange.equiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1815
    format: lean-location
    note: OAI.KLInvariance.CoefficientChange.kEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1873
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.change
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1896
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.changeHom
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:329
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:388
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChangeSections
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

# Transport of coefficients along an algebra isomorphism

Let \(e:A\xrightarrow{\sim}A'\) be an isomorphism of commutative \(k\)-algebras, and let \(M\) be an \(A\)-module. Its transported module \({}^eM\) has the same additive group, with \(A'\)-action
\[
a'\cdot_{{}^eM}m=e^{-1}(a')\cdot_Mm.
\]
The module axioms follow by applying the ring-homomorphism laws for \(e^{-1}\) to the scalar expressions.

The identification of underlying vectors is \(e\)-semilinear:
\[
am=e(a)\cdot_{{}^eM}m.
\]
It is \(k\)-linear because \(e\) fixes base-field scalars, so dimensions over \(k\) are preserved.

## Maps, bases, and grading

An \(A\)-linear map \(f:M\to N\) gives an \(A'\)-linear map on transported modules with the same values. Indeed,
\[
f(e^{-1}(a')m)=e^{-1}(a')f(m)
=a'\cdot_{{}^eN}f(m).
\]
Composition, zero maps, and identity maps retain their underlying formulas.

If \((b_i)\) is an \(A\)-basis, it is an \(A'\)-basis after transport: the old expression \(\sum_i a_i b_i\) becomes
\(\sum_i e(a_i)\cdot_{{}^eM}b_i\).
Both spanning and independence follow by translating coefficients through the bijection \(e\). The same argument transports finite generating sets.

Suppose \(e(A_n)=A'_n\) for every degree. Define
\[
({}^eM)_n=M_n
\]
under the underlying \(k\)-linear identification. The finite homogeneous decompositions stay the same. If \(a'\in A'_i\) and \(m\in M_j\), then \(e^{-1}(a')\in A_i\), so their new product lies in \(M_{i+j}\). Nonnegative support is preserved as well.

## Sheaves and sections

Transport every vertex and edge module of a graded sheaf, keeping the same underlying restriction maps. Their linearity and grading follow from the preceding calculation. The edge labels become \(e(\alpha_e)\).

For a transported stalk vector, multiplication by \(e(\alpha_e)\) is the old multiplication by \(\alpha_e\). Thus quotient kernels and compatibility equations have exactly the same underlying vectors.

A section is consequently transported coordinate by coordinate, giving an isomorphism
\[
{}^e\Gamma(B,U)\simeq\Gamma({}^eB,U).
\]
It sends the class of an assignment \(m\) to the assignment with the same coordinate values in the transported stalks. Its inverse forgets the scalar wrapper. The section equations are preserved in both directions.

## Polynomial coordinates for a symmetric algebra

Choose a basis \(v_1,\ldots,v_N\) of the extended realization. The resulting isomorphism
\[
\operatorname{Sym}(V)\xrightarrow{\sim}k[X_1,\ldots,X_N]
\]
sends the degree-one generator \(v_i\) to \(X_i\). It preserves every homogeneous degree.

Under this isomorphism, a scalar \(\sum_i c_i v_i\) becomes the linear polynomial \(\sum_i c_i X_i\), and a root-labelled sheaf acquires polynomial edge labels. Its additive stalks, section equations, and graded dimensions are transported by the formulas above.

## References

The source declarations below give the constructions and proofs.

## Lean formalization

The wrapper field `val` records the underlying vector. The new scalar action uses the inverse algebra isomorphism; all transported maps act on that underlying value.

`OAI.KLInvariance.CoefficientChange`: [BottSamelson.lean:1777](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1777).

`OAI.KLInvariance.CoefficientChange.equiv`: [BottSamelson.lean:1805](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1805).

`OAI.KLInvariance.CoefficientChange.kEquiv`: [BottSamelson.lean:1815](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1815).

`OAI.KLInvariance.Graded.ModuleData.change`: [BottSamelson.lean:1873](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1873).

`OAI.KLInvariance.Graded.ModuleData.changeHom`: [BottSamelson.lean:1896](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1896).

`OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange`: [Support.lean:329](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L329).

`OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChangeSections`: [Support.lean:388](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L388).
