---
id: kl.foundations.rtilde
title: Normalized R-polynomials and the square parameter
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.foundations.canonical_kl
- kl.notes.hecke_action
- kl.detail.rtilde_family
- kl.detail.rtilde_recursion
- kl.detail.ordinary_r
- kl.hecke.ordinary_r_construction
- kl.hecke.selected_families
lean:
  repository: openai-kl
  modules:
  - Hecke
  - Dihedral
  declarations:
  - OAI.KLInvariance.Hecke.rTilde
  - OAI.KLInvariance.rPolynomial_normalization
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:482
    format: lean-location
    note: OAI.KLInvariance.Hecke.rTilde
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:676
    format: lean-location
    note: OAI.KLInvariance.rPolynomial_normalization
  - artifact: openai-kl-paper
    locator: 1. Introduction and conventions; sec:introduction
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- introduction
---

# Normalized R-polynomials and the square parameter

The normalized polynomial \(\widetilde R_{x,y}(T)\) is constructed from coefficients of the Hecke bar action. For every nonzero element \(v\) of a field,
\[
R_{x,y}(v^2)=v^{\ell(y)-\ell(x)}
 \widetilde R_{x,y}(v-v^{-1}).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same polynomial, different construction order.**

**OpenAI notes:** The path-formula theorem introduces the normalized R-polynomial through increasing reflection paths and relates it to the ordinary R-polynomial; decreasing paths follow by reversing the reflection order. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [eq:bg-path-formula](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L191).

**Lean (primary):** The normalized R-family is defined first as a coefficient of the Hecke bar transform. Its recursion is proved algebraically, and the geometric path product is later proved equal to that independently constructed family. [Hecke:482](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L482), [Hecke:491](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L491), [ReflectionOrders:1229](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionOrders.lean#L1229).

**Role in the proof:** The bar construction supplies the R-family and its recursion. The path theorem then identifies that family with the ordered path polynomial.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Set up induction with integer exponents

Fix a nonzero field element \(v\), and write \(a=v-v^{-1}\). Induct on \(\ell(y)\), with the statement for every \(x\):
\[
R_{x,y}(v^2)=v^{\ell(y)-\ell(x)}\widetilde R_{x,y}(a).
\]
The exponent is an integer, so the formula also makes sense for incomparable pairs. Both families vanish outside Bruhat order.

When \(y=1\), the only comparable \(x\) is \(1\). Both sides are one for \(x=1\), and zero otherwise.

### Step 2. Choose a descent and write both recursions

For \(y\ne1\), choose a simple reflection \(s\) with \(sy<y\). Put \(d=\ell(y)-\ell(x)\). Every term with upper endpoint \(sy\) falls under induction.

If \(sx<x\), both recursions replace \((x,y)\) by \((sx,sy)\). Both lengths decrease by one, so
\(\ell(sy)-\ell(sx)=d\).
The induction formula for that pair is exactly the desired formula.

### Step 3. Compute the ascent branch without suppressing its powers

Suppose \(sx>x\). Then
\(\ell(sy)-\ell(x)=d-1\) and
\(\ell(sy)-\ell(sx)=d-2\).
The ordinary recursion and induction give
\[
\begin{aligned}
R_{x,y}(v^2)
&=(v^2-1)R_{x,sy}(v^2)+v^2R_{sx,sy}(v^2)\\
&=(v^2-1)v^{d-1}\widetilde R_{x,sy}(a)
  +v^2v^{d-2}\widetilde R_{sx,sy}(a)\\
&=v^d\bigl((v-v^{-1})\widetilde R_{x,sy}(a)
  +\widetilde R_{sx,sy}(a)\bigr).
\end{aligned}
\]
The two scalar equalities used are
\((v^2-1)v^{d-1}=v^d(v-v^{-1})\) and
\(v^2v^{d-2}=v^d\), valid because \(v\ne0\).
The expression in parentheses is the normalized R-recursion. This completes induction.

## References

[1. Introduction and conventions](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization

`OAI.KLInvariance.Hecke.rTilde`: [Hecke.lean:482](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L482).

`OAI.KLInvariance.rPolynomial_normalization`: [Dihedral.lean:676](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L676).
