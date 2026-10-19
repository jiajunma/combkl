---
id: kl.word.diagonal_stabilizer
title: Diagonal operators preserving a coordinate submodule
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.coordinate_images
- kl.word.evaluation_right_action
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.FiniteCharacterLocalization.diagonal
  - OAI.KLInvariance.FiniteCharacterLocalization.stabilizer
  - OAI.KLInvariance.FiniteCharacterLocalization.diagonal_mem
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1664
    format: lean-location
    note: OAI.KLInvariance.FiniteCharacterLocalization.diagonal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1669
    format: lean-location
    note: OAI.KLInvariance.FiniteCharacterLocalization.stabilizer
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1694
    format: lean-location
    note: OAI.KLInvariance.FiniteCharacterLocalization.diagonal_mem
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the bilinear form, coefficient ring, finite coordinate presentation
    and lifting hypotheses explicit?
  verdict: Read diagonal and all stabilizer subalgebra closure fields. Explained polynomial
    closure and the actual right-action source of stable weights, with the congruence-pair
    example.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Diagonal operators preserving a coordinate submodule

Let \(R\) be a commutative ring, \(X\) an index set, and \(E_x\) an \(R\)-module for each \(x\). A scalar weight function \(f:X\to R\) defines the diagonal operator
\[
D_f:\prod_{x\in X}E_x\to\prod_{x\in X}E_x,\qquad
(D_fm)_x=f(x)m_x.
\]
It is \(R\)-linear by the module laws and commutativity of \(R\).

For a submodule \(L\subseteq\prod_xE_x\), its diagonal stabilizer is
\[
\operatorname{Stab}(L)
=\{f\in R^X:D_f(L)\subseteq L\}.
\]
This is the source's stabilizer subalgebra. Membership means that applying the coordinate weights to any vector already in \(L\) produces another vector in \(L\).

## Algebra operations on stable weights

Pointwise addition and multiplication satisfy
\[
D_{f+g}=D_f+D_g,\qquad D_{fg}=D_fD_g.
\]
Thus stable weights are closed under addition and multiplication. The zero and constant-one functions give the zero and identity operators. A constant function with value \(r\) acts by scalar multiplication by \(r\), preserving every submodule.

Negation and subtraction follow from the same formulas. Therefore every polynomial expression in stable weights and constant functions remains in \(\operatorname{Stab}(L)\). This is the algebra used to construct the class projectors.

## Scaled block projections

A class projector in this construction is a stable weight \(g\) that equals one common scalar \(d\) on a selected class \(C\) and is zero outside \(C\). Its diagonal operator sends a vector to its \(C\)-coordinates multiplied by \(d\).

It satisfies \(D_g^2=dD_g\). In a localization where \(d\) is invertible, dividing by \(d\) gives an idempotent projection. The [[node:kl.word.residue_class_projector|class-projector theorem]] constructs \(d\) outside the chosen prime, which is the condition needed for a prime-local denominator.

## The congruence-pair example

Take \(R=\mathbb R[\alpha]\) and
\[
L=\{(u,v)\in R^2:u-v\in\alpha R\}.
\]
A weight pair \((a,b)\) stabilizes \(L\) exactly when \(a-b\in\alpha R\).

Necessity follows by applying it to \((1,1)\in L\). For sufficiency,
\[
au-bv=a(u-v)+(a-b)v\in\alpha R.
\]
Thus the stabilizer condition has an explicit congruence interpretation.

## Coefficient-action weights

For a word coordinate image over its symmetric coefficient algebra \(A\), the weight function associated to a coefficient \(a\) is
\[
x\longmapsto\chi_x(a).
\]
It is stable because right multiplication by \(a\) on a word vector satisfies
\[
\pi_x(m\cdot a)=\chi_x(a)\pi_x(m).
\]
Consequently the diagonal operator on an image tuple is the projection of another actual word vector. The finite-coordinate construction uses these stable weights as its scalar tests.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.FiniteCharacterLocalization.diagonal`: [IntegralPairings.lean:1664](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1664).

`OAI.KLInvariance.FiniteCharacterLocalization.stabilizer`: [IntegralPairings.lean:1669](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1669).

`OAI.KLInvariance.FiniteCharacterLocalization.diagonal_mem`: [IntegralPairings.lean:1694](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1694).
