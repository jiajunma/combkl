---
id: kl.realization.extension_minimality
title: The minimal dimension of a nondegenerate extension
kind: theorem
status: proved
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.realization.radical_extension
- kl.notes.extended_realization
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.Realization.extension_dimension_minimal
  - OAI.KLInvariance.Realization.extension_finrank
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:522
    format: lean-location
    note: OAI.KLInvariance.Realization.extension_dimension_minimal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:517
    format: lean-location
    note: OAI.KLInvariance.Realization.extension_finrank
  - artifact: openai-kl-paper
    locator: Real realizations; bg:realization
    format: section
    note: Construction and normalization of the realization.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition retain the local source hypotheses and construction?
  verdict: Source statements and construction read directly; dimensions, normalization,
    and orthogonality direction stated explicitly.
tags:
- Kazhdan-Lusztig
- realization
---

# The minimal dimension of a nondegenerate extension

Let \(V_0,E\) be finite-dimensional real vector spaces and \(B\) a bilinear form on \(V_0\). Put
\[
K=\{v\in V_0:B(v,w)=0\text{ for every }w\in V_0\}.
\]
Let \(C\) be a nondegenerate bilinear form on \(E\). Suppose an injective linear map \(\iota:V_0\to E\) satisfies
\[
C(\iota(v),\iota(w))=B(v,w).
\]
Then
\[
\dim E\ge\dim V_0+\dim K.
\]
For symmetric \(B\), the dual extension \(V_0\oplus K^*\) attains this bound.

*Proof.*

### Step 1. Locate the embedded subspaces

Set \(U=\iota(V_0)\), \(L=\iota(K)\). Injectivity gives \(\dim U=\dim V_0\) and \(\dim L=\dim K\). For \(k\in K\), \(v\in V_0\),
\[
C(\iota(k),\iota(v))=B(k,v)=0.
\]
Define \(L^\perp=\{x\in E:C(l,x)=0\text{ for every }l\in L\}\). The displayed equality proves \(U\subseteq L^\perp\).

### Step 2. Compute the orthogonal-complement dimension

Consider
\[
\Phi:E\longrightarrow L^*,\qquad \Phi(x)(l)=C(l,x).
\]
Its kernel is \(L^\perp\). We show it is surjective.

Take \(\eta\in L^*\). Extend a basis of \(L\) to one of \(E\), and assign value zero to the added basis vectors. This extends \(\eta\) to \(\widehat\eta\in E^*\).

Nondegeneracy makes \(x\mapsto C(-,x)\) an injective map \(E\to E^*\). Both spaces have the same finite dimension, so the map is surjective. Choose \(x\) representing \(\widehat\eta\). Restricting to \(L\) gives \(\Phi(x)=\eta\).

Rank–nullity therefore gives
\[
\dim L^\perp=\dim E-\dim L.
\]

### Step 3. Deduce the lower bound

Using \(U\subseteq L^\perp\),
\[
\dim V_0=\dim U\le\dim L^\perp=\dim E-\dim K.
\]
Rearrange to obtain the assertion. This is the orthogonal-subspace argument of the local Lean proof.

### Step 4. Attain the bound

For symmetric \(B\), the dual-extension theorem gives a nondegenerate form on \(V_0\oplus K^*\) preserving \(B\). A basis of \(K\) and its dual basis have the same number of elements. Thus
\[
\dim(V_0\oplus K^*)=\dim V_0+\dim K,
\]
as required.

## References

[Realizations in the OpenAI notes](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L34).

## Lean formalization

`OAI.KLInvariance.Realization.extension_dimension_minimal`: [Tits.lean:522](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L522).

`OAI.KLInvariance.Realization.extension_finrank`: [Tits.lean:517](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L517).
