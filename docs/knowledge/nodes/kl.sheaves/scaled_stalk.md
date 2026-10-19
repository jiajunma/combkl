---
id: kl.duality.scaled_stalk
title: The scaled actual-stalk character vector
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.duality.stalk_character
lean:
  repository: openai-kl
  modules:
  - EdgeLocalization
  declarations:
  - OAI.KLInvariance.BruhatGraph.scaledStalk
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:377
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.scaledStalk
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read scaledStalk and separated its actual integer character, scalar evaluation
    field and nonzero reciprocal parameter. Explained q=t^2 and the real Hilbert scale
    used at comparison endpoints.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# The scaled actual-stalk character vector

Fix a finite-generator Coxeter system, the real polynomial coefficient algebra of its extended realization, and \(b\in W\). The actual character
\(C_{x,b}(q)\in\mathbb Z[q]\) counts homogeneous generators of the chosen boundary stalk on \([1,b]\).

For \(x\in[1,b]\) and a nonzero parameter \(t\) in a field \(F\), define
\[
c_x^b(t)
=t^{\ell(x)-\ell(b)}C_{x,b}(t^2)
=t^{-d(x,b)}C_{x,b}(t^2),
\qquad d(x,b)=\ell(b)-\ell(x).
\]
The integer coefficients are mapped into \(F\) by its canonical ring homomorphism from \(\mathbb Z\). The sheaf still supplies the same integer polynomial; \(F\) is the field in which that polynomial is evaluated.

This is the nonzero-parameter expression of the source's scaledStalk. As \(x\) varies, it gives a vector \(c^b(t)\) indexed by \([1,b]\).

## Reciprocal evaluation

Replacing \(t\) by \(t^{-1}\) gives
\[
c_x^b(t^{-1})
=t^{d(x,b)}C_{x,b}(t^{-2}).
\]
These are finite polynomial evaluations multiplied by integer powers of the nonzero field parameter.

The ordinary polynomial parameter is \(q=t^2\). The normalized R-family uses \(t-t^{-1}\) in the inverse-reciprocity form and \(t^{-1}-t\) after the parameter is inverted.

## Real Hilbert normalization

In the comparison range \(0<t<1\), if the coefficient algebra has \(N\) degree-one variables, multiplication by
\[
(1-t^2)^Nt^{-d(x,b)}
\]
removes the polynomial coefficient Hilbert factor from a stalk Hilbert sum at \(t^2\). The result is \(c_x^b(t)\).

For a full outgoing kernel, the reflected character gives \(c_x^b(t^{-1})\). The [[node:kl.duality.normalized_character_endpoints|normalized-endpoint theorem]] proves both identities directly.

For the one-edge interval \([1,s]\), both stalk characters are \(1\), so
\(c_1^s(t)=t^{-1}\) and \(c_s^s(t)=1\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Equivalent parameter conventions.**

**OpenAI notes:** The comparison uses \(0<q<1\), scale \(q^{-d/2}(1-q)^N\), and transfer coefficient \(q^{-1/2}-q^{1/2}\). [eq:state](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L243), [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275).

**Lean (primary):** The comparison uses \(0<t<1\) and substitutes \(q=t^2\). Its scale is \(t^{-d}(1-t^2)^N\) and its transfer coefficient is \(t^{-1}-t\). [Dihedral:730](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L730), [PositiveTransfer:591](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L591), [PositiveTransfer:621](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L621), [EdgeLocalization:377](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L377), [EdgeLocalization:423](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L423).

**Role in the proof:** The substitution \(q=t^2\) identifies the two normalizations. Linear root labels have degree one throughout the calculation.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.scaledStalk`: [EdgeLocalization.lean:377](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L377).
