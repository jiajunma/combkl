---
id: kl.detail.hilbert_values
title: Hilbert values and degreewise defects of submodules
kind: definition
status: formalized
primary_topic: kl.03_realizations_and_grading
topics:
- kl.03_realizations_and_grading
uses:
- kl.sheaves.graded_module
lean:
  repository: openai-kl
  modules:
  - ModuleAlgebra
  declarations:
  - OAI.KLInvariance.Hilbert.piece
  - OAI.KLInvariance.Hilbert.term
  - OAI.KLInvariance.Hilbert.value
  - OAI.KLInvariance.Hilbert.defectPiece
  - OAI.KLInvariance.Hilbert.defectTerm
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:500
    format: lean-location
    note: OAI.KLInvariance.Hilbert.piece
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:503
    format: lean-location
    note: OAI.KLInvariance.Hilbert.term
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:506
    format: lean-location
    note: OAI.KLInvariance.Hilbert.value
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:571
    format: lean-location
    note: OAI.KLInvariance.Hilbert.defectPiece
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:574
    format: lean-location
    note: OAI.KLInvariance.Hilbert.defectTerm
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# Hilbert values and degreewise defects of submodules

Let \(M=\bigoplus_{n\in\mathbb Z}M_n\) be a graded vector space over a field \(k\), with finite-dimensional pieces. For a subspace \(S\subseteq M\), its degree-\(n\) piece in the fixed ambient grading is \(S_n=S\cap M_n\). Define
\[
h_{S,n}(q)=\dim_k(S_n)q^n,\qquad
H_S(q)=\sum_{n\in\mathbb Z}\dim_k(S_n)q^n.
\]
We use \(H_S(q)\) as a numerical Hilbert value only with an explicit convergence hypothesis. The comparison arguments take a positive convergent parameter, usually \(0<q<1\); positivity gives \(q^n>0\) even for negative integers \(n\).

If \(S\subseteq T\), the degreewise defect is
\[
D_n=T_n/S_n,\qquad d_n(q)=\dim_k(D_n)q^n.
\]
These definitions make sense without freeness of either submodule. If \(S,T\) are homogeneous, the spaces \(D_n\) are the homogeneous components of the quotient \(T/S\). Without homogeneity they remain the explicitly defined degreewise quotients.

Finite-dimensionality gives \(h_{S,n}(q)\le h_{T,n}(q)\) for \(q>0\). If the target series converges, comparison proves convergence of the smaller series. Rank-nullity gives \(d_n=h_{T,n}-h_{S,n}\), hence the convergent defect sum is \(H_T-H_S\). The equality-detection theorem further uses homogeneity of the target to recover the whole submodule from its components.

## References

The precise Lean sources are listed below.

## Lean formalization

`OAI.KLInvariance.Hilbert.piece`: [ModuleAlgebra.lean:500](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L500).

`OAI.KLInvariance.Hilbert.term`: [ModuleAlgebra.lean:503](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L503).

`OAI.KLInvariance.Hilbert.value`: [ModuleAlgebra.lean:506](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L506).

`OAI.KLInvariance.Hilbert.defectPiece`: [ModuleAlgebra.lean:571](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L571).

`OAI.KLInvariance.Hilbert.defectTerm`: [ModuleAlgebra.lean:574](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L574).
