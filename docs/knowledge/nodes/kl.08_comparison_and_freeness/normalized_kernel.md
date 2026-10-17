---
id: kl.comparison.normalized_kernel
title: Normalized Hilbert states along an edge schedule
kind: definition
status: formalized
primary_topic: kl.08_comparison_and_freeness
topics:
- kl.08_comparison_and_freeness
uses:
- kl.sheaves.upward_kernel
- kl.sheaves.hilbert_free
- kl.foundations.scaled_kl
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.BruhatGraph.normalizedKernel
  - OAI.KLInvariance.BruhatGraph.stateScale
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:599
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.normalizedKernel
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:591
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.stateScale
  - artifact: openai-kl-paper
    locator: 6. Reciprocity and simultaneous induction; sec:induction
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- induction
---

# Normalized Hilbert states along an edge schedule

Let \(A\) be a real polynomial ring in \(N\) variables and fix \(0<t<1\). For remaining edge conditions \(F\) at \(x\), define
\[
D_x(t,F)=(1-t^2)^N t^{\ell(x)-\ell(b)}
 \operatorname{Hilb}(L_x(F);t^2).
\]
Removing the conditions in schedule order produces a sequence of state vectors. The ordinary polynomial parameter is \(q=t^2\), and the common transfer coefficient is \(T=t^{-1}-t\). The Hilbert value defines the state even before an intermediate kernel is expressed in a free basis.

## Deriving the transfer coefficient

Put \(q=t^2\), let \(d_x=\ell(b)-\ell(x)\), and consider \(e:x\to y\). The edge factor has degree
\[
k=\frac{\ell(y)-\ell(x)-1}{2}.
\]
Taking the quotient by a regular linear label contributes \(1-q\) to the Hilbert series; multiplying by the correction factor contributes \(q^k\).

After state normalization, the ratio between the \(x\)-scale and the \(y\)-scale is
\[
q^{-d_x/2}\,q^k(1-q)\,q^{d_y/2}
=q^{-1/2}(1-q)=t^{-1}-t.
\]
The dependence on the length of the individual edge cancels completely. Every edge therefore uses the same positive scalar, making the transfer product comparable with the normalized R-path matrix.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Equivalent parameter conventions.**

**OpenAI notes:** The comparison uses \(0<q<1\), scale \(q^{-d/2}(1-q)^N\), and transfer coefficient \(q^{-1/2}-q^{1/2}\). [eq:state](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L243), [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275).

**Lean (primary):** The comparison uses \(0<t<1\) and substitutes \(q=t^2\). Its scale is \(t^{-d}(1-t^2)^N\) and its transfer coefficient is \(t^{-1}-t\). [Dihedral:730](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L730), [PositiveTransfer:591](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L591), [PositiveTransfer:621](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L621).

**How to read this entry:** These are the same normalization after \(q=t^2\). The proof spells out this substitution and retains the degree-one convention for linear root labels.
<!-- source-comparison:end -->

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.normalizedKernel`: [PositiveTransfer.lean:599](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L599).

`OAI.KLInvariance.BruhatGraph.stateScale`: [PositiveTransfer.lean:591](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L591).
