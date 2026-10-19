---
id: kl.detail.graded_character
title: The intrinsic graded-rank polynomial of a free module
kind: definition
status: formalized
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.sheaves.graded_module
- kl.algebra.homogeneous_basis
- kl.notes.graded_projective_free
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.Graded.NonnegativeBasis.polynomial
  - OAI.KLInvariance.Graded.NonnegativeBasis.coeff_nonneg
  - OAI.KLInvariance.Graded.NonnegativeBasis.eval₂_eq
  - OAI.KLInvariance.Graded.character
  - OAI.KLInvariance.Graded.character_coeff_nonneg
  - OAI.KLInvariance.Graded.character_eq
  - OAI.KLInvariance.Graded.ModuleData.char
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:47
    format: lean-location
    note: OAI.KLInvariance.Graded.NonnegativeBasis.polynomial
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:51
    format: lean-location
    note: OAI.KLInvariance.Graded.NonnegativeBasis.coeff_nonneg
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:58
    format: lean-location
    note: OAI.KLInvariance.Graded.NonnegativeBasis.eval₂_eq
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:89
    format: lean-location
    note: OAI.KLInvariance.Graded.character
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:93
    format: lean-location
    note: OAI.KLInvariance.Graded.character_coeff_nonneg
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:98
    format: lean-location
    note: OAI.KLInvariance.Graded.character_eq
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1742
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.char
  - artifact: openai-kl-paper
    locator: Related paper context; bg:realization
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the grading, scalar, finiteness and convergence hypotheses retained?
  verdict: Read NonnegativeBasis.polynomial, Graded.character and ModuleData.char.
    Distinguished basis-degree polynomial selection, basis independence, graded rank
    and Hilbert numerator; retained finite free nonnegative polynomial hypotheses.
tags:
- Kazhdan-Lusztig
- graded-algebra
---

# The intrinsic graded-rank polynomial of a free module

Let \(k\) be a field and \(A=k[X_1,\ldots,X_N]\) with variables in degree one, and let \(M\) be finite free and nonnegatively graded. Choose a finite homogeneous basis \(e_i\), with degrees \(d_i\in\mathbb N\). Its basis-degree polynomial is
\[
p_e(z)=\sum_i z^{d_i}\in\mathbb Z[z].
\]
The coefficient of \(z^n\) counts basis vectors of degree \(n\), so every coefficient is a nonnegative integer.

The homogeneous-basis theorem supplies such a basis. Nonnegativity of the grading makes its degrees nonnegative: a nonzero basis vector cannot belong to a negative piece, because that piece is zero.

## The source's character

The source selects a nonnegative homogeneous basis and defines
\[
\operatorname{ch}(M;z)=p_e(z).
\]
[[node:kl.algebra.character_basis_independence|Basis independence]] proves that every homogeneous basis yields the same polynomial. Thus it is intrinsic to the graded module.

The notes denote this same generator-counting expression by
\[
\operatorname{grk}_A(M;z)=\operatorname{ch}(M;z).
\]
The local names are Graded.character and, for bundled module data, ModuleData.char.

For basis degrees \(0,2,2\), the character is \(1+2z^2\). Evaluation at \(z=1\) counts the three \(A\)-basis vectors.

## Relation to the full graded vector space

Every basis generator can be multiplied by coefficient monomials. The Hilbert formula counts all those resulting vectors:
\[
\operatorname{Hilb}(M;z)
=\frac{\operatorname{ch}(M;z)}{(1-z)^N}.
\]
At \(0<q<1\), the corresponding convergent value is
\[
H_M(q)=\frac{\operatorname{ch}(M;q)}{(1-q)^N}.
\]
Thus the character is the numerator after removing the polynomial-ring contribution.

For \(A=k[X]\) and \(M=A\oplus A(2)\), the character is \(1+z^2\). The Hilbert coefficients are \(1,1,2,2,\ldots\), because every generator has its full sequence of powers of \(X\) as multiples.

Characters add under finite graded sums, and shifting all generator degrees upward by \(d\) multiplies the character by \(z^d\). The [[node:kl.algebra.character_operations|character-operations theorem]] proves these formulas by transporting actual bases.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Graded.NonnegativeBasis.polynomial`: [SheafMorphisms.lean:47](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L47).

`OAI.KLInvariance.Graded.NonnegativeBasis.coeff_nonneg`: [SheafMorphisms.lean:51](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L51).

`OAI.KLInvariance.Graded.NonnegativeBasis.eval₂_eq`: [SheafMorphisms.lean:58](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L58).

`OAI.KLInvariance.Graded.character`: [SheafMorphisms.lean:89](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L89).

`OAI.KLInvariance.Graded.character_coeff_nonneg`: [SheafMorphisms.lean:93](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L93).

`OAI.KLInvariance.Graded.character_eq`: [SheafMorphisms.lean:98](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L98).

`OAI.KLInvariance.Graded.ModuleData.char`: [SheafMorphisms.lean:1742](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1742).
