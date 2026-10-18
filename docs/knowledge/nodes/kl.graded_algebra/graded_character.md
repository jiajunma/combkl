---
id: kl.detail.graded_character
title: The graded-rank polynomial of a free module
kind: definition
status: formalized
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.sheaves.graded_module
- kl.sheaves.hilbert_free
- kl.notes.graded_projective_free
- kl.algebra.homogeneous_basis
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.Graded.character
  - OAI.KLInvariance.Graded.NonnegativeBasis.polynomial_eq
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:89
    format: lean-location
    note: OAI.KLInvariance.Graded.character
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:72
    format: lean-location
    note: OAI.KLInvariance.Graded.NonnegativeBasis.polynomial_eq
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
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- realizations_and_grading
---

# The graded-rank polynomial of a free module

Let \(A=k[X_1,\ldots,X_N]\) have variables in degree one, and let \(M\) be a finite free nonnegatively graded module with homogeneous basis \(m_i\) of degrees \(d_i\). Its graded-rank polynomial is
\[
\operatorname{ch}(M;q)=\sum_iq^{d_i}\in\mathbb Z[q].
\]
Its coefficients count homogeneous generators and are nonnegative. It is not the Hilbert series of the underlying graded vector space; the latter is
\[
H_M(q)=\frac{\operatorname{ch}(M;q)}{(1-q)^N}.
\]

The polynomial is independent of the homogeneous basis. For two such bases, the Hilbert-series formula gives equal evaluations of their numerator polynomials for every real \(0<q<1\). The common denominator is nonzero there. Equality at infinitely many real values implies equality of the polynomials.

For example, generators in degrees \(0,2,2\) give character \(1+2q^2\). Characters add under direct sums and acquire a factor \(q^d\) under a nonnegative degree shift \(d\).

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L34).

## Lean formalization



`OAI.KLInvariance.Graded.character`: [SheafMorphisms.lean:89](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L89).

`OAI.KLInvariance.Graded.NonnegativeBasis.polynomial_eq`: [SheafMorphisms.lean:72](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L72).
