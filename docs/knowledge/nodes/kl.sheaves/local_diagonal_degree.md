---
id: kl.detail.local_diagonal_degree
title: A nonzero local diagonal forces a strict half-degree bound
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.duality.local_intersection_properties
- kl.algebra.local_diagonal_bound
- kl.detail.local_intersection
- kl.algebra.homogeneous_basis
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.BruhatGraph.localIntersection_diagonal_strict_degree
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:186
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.localIntersection_diagonal_strict_degree
  - artifact: openai-kl-paper
    locator: Related paper context; bg:normalization
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the exact actual-stalk theorem and its generic algebra invocation.
    Made the finite-generator setting, actual sheaf, proper vertex, homogeneous nonnegative
    basis and single-index nonzero hypothesis explicit; replaced the former scope-warning
    paragraph by the natural/integer rank conversion.
tags:
- Kazhdan-Lusztig
- graded-duality
---

# A nonzero local diagonal forces a strict half-degree bound

Fix a finite-generator Coxeter system and the polynomial coefficient algebra \(A\) from a finite real basis of its extended realization. Let \(B(b)\) be the actual normalized boundary sheaf on \([1,b]\), and let \(x<b\).

Choose a finite nonnegative homogeneous \(A\)-basis \((m_i)\) of \(B(b)^x\), with degrees \(d_i\in\mathbb N\), and write \(\lambda_i=m_i^*\). Let \(I_x\) be the actual local intersection map. For any specified basis index \(i\), if
\[
a_{ii}:=\lambda_i(I_x\lambda_i)\ne0,
\]
then
\[
2d_i<d(x,b),\qquad d(x,b)=\ell(b)-\ell(x).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate degree statement.**

**OpenAI notes:** The normalization proposition identifies stalk graded ranks with canonical KL polynomials using the cited character theorem and a conversion from degree-two to degree-one labels. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253), [eq:bg-ranks](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L257).

**Lean (primary):** The actual local intersection map is constructed from integral stalk–costalk duality. Boundary minimality puts its image in the positive ideal, and the strict degree theorem assumes that the specified diagonal coefficient is nonzero. [PositiveTransfer:132](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L132), [PositiveTransfer:160](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L160), [PositiveTransfer:186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L186).

**Role in the proof:** The local calculation gives \(2d_i<\ell(b)-\ell(x)\) for the basis generator named in that nonzero-diagonal hypothesis. Actual-character reciprocity supplies the endpoint identity in the comparison route.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Determine the dual and image degrees

The coordinate functional \(\lambda_i\) has degree \(-d_i\):
\[
\lambda_i(B(b)^x_j)\subseteq A_{j-d_i}.
\]
The local intersection grading, with shift \(d=d(x,b)\), gives
\[
I_x\lambda_i\in B(b)^x_{d-d_i}.
\]
Applying \(\lambda_i\) once more yields
\[
a_{ii}\in A_{d-2d_i}.
\]

### Step 2. Use the proper-vertex minimality condition

The hypothesis \(x<b\) makes \(x\) a vertex different from the distinguished top. The [[node:kl.duality.local_intersection_properties|local intersection properties theorem]] gives
\[
\operatorname{im}I_x\subseteq A_+B(b)^x.
\]
Consequently \(I_x\lambda_i\) is a finite sum \(\sum_s c_sv_s\) with \(c_s\in A_+\). Linearity gives
\[
a_{ii}=\sum_s c_s\lambda_i(v_s)\in A_+.
\]

### Step 3. Apply the positive-ideal degree lemma

The coefficient \(a_{ii}\) is nonzero by the stated hypothesis. Together with Steps 1 and 2, the [[node:kl.algebra.local_diagonal_bound|positive-ideal diagonal-degree theorem]] gives
\[
d-2d_i>0.
\]
Its proof excludes negative degree using \(A_n=0\) for \(n<0\), and excludes degree zero using \(A_+=\ker\epsilon\) and \(\epsilon(a)=a\) on \(A_0\).

### Step 4. Convert to the natural rank difference

Bruhat comparison gives \(\ell(x)\le\ell(b)\), so the integer difference \(\ell(b)-\ell(x)\) equals the natural subtraction used in rankDifference. The basis degrees are natural numbers as well. Hence the integer inequality in Step 3 is exactly
\[
2d_i<\operatorname{rankDifference}(x,b).
\]
This is the conclusion of localIntersection_diagonal_strict_degree for the chosen index and nonzero diagonal coefficient.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.localIntersection_diagonal_strict_degree`: [PositiveTransfer.lean:186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L186).
