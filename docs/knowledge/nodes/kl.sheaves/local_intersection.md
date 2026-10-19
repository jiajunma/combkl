---
id: kl.detail.local_intersection
title: The local intersection map and its matrix
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.costalk_duality
- kl.detail.boundary_pairing
- kl.sheaves.upward_kernel
- kl.algebra.dual_basis_degrees
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.BruhatGraph.ActualBoundary
  - OAI.KLInvariance.BruhatGraph.actualSymmetricPairing
  - OAI.KLInvariance.BruhatGraph.actualSectionDuality
  - OAI.KLInvariance.BruhatGraph.localIntersection
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:94
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.ActualBoundary
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:96
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.actualSymmetricPairing
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:100
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.actualSectionDuality
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:132
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.localIntersection
  - artifact: openai-kl-paper
    locator: Related paper context; bg:normalization
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Separated the actual construction and its matrix notation from the property
    proofs. Read ActualBoundary, the chosen symmetric pairing, actualSectionDuality
    and localIntersection; defined the outgoing kernel and both dual-function arguments
    explicitly.
tags:
- Kazhdan-Lusztig
- graded-duality
---

# The local intersection map and its matrix

Fix a finite-generator Coxeter system and a finite real basis of its extended realization. Let \(A=\mathbb R[X_1,\ldots,X_N]\) be the resulting polynomial coefficient algebra, with variables in degree one, and let \(B=B(b)\) be the chosen normalized boundary sheaf on \([1,b]\).

At \(x\in[1,b]\), write
\[
M_x=B^x,\qquad M_x^*=\operatorname{Hom}_A(M_x,A),
\]
\[
K_x=\{v\in M_x:\rho^-_e(v)=0
                 \text{ for every outgoing edge }e:x\to y\}.
\]
Thus \(K_x\) is the kernel of the combined outgoing restriction map \(\partial_x\).

The constructed symmetric section pairing has shift \(\ell(b)\), and its section duality supplies
\[
\kappa_x:K_x\xrightarrow{\sim}M_x^*.
\]
The **local intersection map** is
\[
I_x:M_x^*\longrightarrow M_x,\qquad
I_x=\iota_x\circ\kappa_x^{-1},
\]
where \(\iota_x:K_x\hookrightarrow M_x\) is the inclusion. A functional first determines its unique outgoing-kernel vector through the duality, and the inclusion regards that vector as a stalk element.

## The coefficient-valued local form

The same map defines an \(A\)-valued bilinear form on the stalk dual:
\[
b_x(\lambda,\mu)=\lambda(I_x\mu).
\]
Linearity of \(I_x\) and of the functionals proves linearity in each argument. The [[node:kl.sheaves.costalk_pairing_symmetry|stalk–costalk symmetry theorem]] gives
\[
b_x(\lambda,\mu)=b_x(\mu,\lambda).
\]
The [[node:kl.duality.local_intersection_properties|local intersection properties theorem]] proves that \(I_x\) is injective and has image \(K_x\).

## Coordinates in a homogeneous stalk basis

Choose a finite homogeneous \(A\)-basis \((m_i)\) of the stalk, with degrees \(d_i\), and let \(\lambda_i(m_j)=\delta_{ij}\) be its dual basis. Set
\[
a_{ij}=\lambda_i(I_x\lambda_j).
\]
Then
\[
I_x\lambda_j=\sum_i a_{ij}m_i.
\]
Thus the \(j\)-th matrix column consists of the coordinates of the outgoing-kernel vector representing \(\lambda_j\). The symmetric form has the same matrix: \(b_x(\lambda_i,\lambda_j)=a_{ij}\).

For \(d=\ell(b)-\ell(x)\), the [[node:kl.duality.local_intersection_properties|local intersection properties theorem]] gives
\[
a_{ij}\in A_{d-d_i-d_j},\qquad a_{ij}=a_{ji}.
\]
At a proper vertex \(x<b\), every \(a_{ij}\) also belongs to \(A_+\). These are the inputs to the [[node:kl.detail.local_diagonal_degree|strict diagonal-degree theorem]].

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate degree statement.**

**OpenAI notes:** The normalization proposition identifies stalk graded ranks with canonical KL polynomials using the cited character theorem and a conversion from degree-two to degree-one labels. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253), [eq:bg-ranks](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L257).

**Lean (primary):** The actual local intersection map is constructed from integral stalk–costalk duality. Boundary minimality puts its image in the positive ideal, and the strict degree theorem assumes that the specified diagonal coefficient is nonzero. [PositiveTransfer:132](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L132), [PositiveTransfer:160](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L160), [PositiveTransfer:186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L186).

**Role in the proof:** The local calculation gives \(2d_i<\ell(b)-\ell(x)\) for the basis generator named in that nonzero-diagonal hypothesis. Actual-character reciprocity supplies the endpoint identity in the comparison route.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.ActualBoundary`: [PositiveTransfer.lean:94](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L94).

`OAI.KLInvariance.BruhatGraph.actualSymmetricPairing`: [PositiveTransfer.lean:96](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L96).

`OAI.KLInvariance.BruhatGraph.actualSectionDuality`: [PositiveTransfer.lean:100](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L100).

`OAI.KLInvariance.BruhatGraph.localIntersection`: [PositiveTransfer.lean:132](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L132).
