---
id: kl.detail.rtilde_family
title: The normalized R-family as bar coefficients
kind: definition
status: formalized
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.definitions.bar_involution
- kl.foundations.bruhat_order
lean:
  repository: openai-kl
  modules:
  - Hecke
  declarations:
  - OAI.KLInvariance.Hecke.rTilde
  - OAI.KLInvariance.Hecke.rTilde_diagonal
  - OAI.KLInvariance.Hecke.rTilde_zero
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:482
    format: lean-location
    note: OAI.KLInvariance.Hecke.rTilde
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:485
    format: lean-location
    note: OAI.KLInvariance.Hecke.rTilde_diagonal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:488
    format: lean-location
    note: OAI.KLInvariance.Hecke.rTilde_zero
  - artifact: openai-kl-paper
    locator: Related paper context; sec:introduction
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
- hecke_polynomials
---

# The normalized R-family as bar coefficients

Let \(a\) be an indeterminate. In the normalized Hecke module over \(\mathbb Z[a]\), form the inverse-word bar basis with operator parameter \(-a\). Define
\[
\widetilde R_{x,y}(a)
=\text{the coefficient of }e_x\text{ in that bar-basis vector at }y.
\]
The minus sign belongs to the defining parameter convention. It makes the simple-edge coefficient \(a\), matching the positive path parameter used later.

Triangularity of the bar basis gives
\[
\widetilde R_{x,x}=1,\qquad
\widetilde R_{x,y}=0\quad\text{if }x\not\leq y.
\]
These are polynomials with integer coefficients, constructed from operators rather than postulated as solutions of a recursion.

The descent recursion is a theorem about this family. The relation to ordinary \(R_{x,y}(q)\) after the square-parameter substitution is another theorem, with its own normalization factors. Keeping the definition and these two identities separate makes the later path evaluation unambiguous.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same polynomial, different construction order.**

**OpenAI notes:** The path-formula theorem introduces the normalized R-polynomial through increasing reflection paths and relates it to the ordinary R-polynomial; decreasing paths follow by reversing the reflection order. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [eq:bg-path-formula](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L191).

**Lean (primary):** The normalized R-family is defined first as a coefficient of the Hecke bar transform. Its recursion is proved algebraically, and the geometric path product is later proved equal to that independently constructed family. [Hecke:482](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L482), [Hecke:491](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L491), [ReflectionOrders:1229](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionOrders.lean#L1229).

**Role in the proof:** The bar construction supplies the R-family and its recursion. The path theorem then identifies that family with the ordered path polynomial.
<!-- source-comparison:end -->

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization



`OAI.KLInvariance.Hecke.rTilde`: [Hecke.lean:482](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L482).

`OAI.KLInvariance.Hecke.rTilde_diagonal`: [Hecke.lean:485](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L485).

`OAI.KLInvariance.Hecke.rTilde_zero`: [Hecke.lean:488](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L488).
