---
id: kl.detail.base_change
title: Tensor base change of a graph sheaf
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.graph_sheaf
- kl.detail.compatible_sections
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChange
  - OAI.KLInvariance.MomentGraph.Sheaf.tensorAssignments
  - OAI.KLInvariance.MomentGraph.Sheaf.tensorAssignments_tmul
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChange_tmul_compatible
  - OAI.KLInvariance.MomentGraph.Sheaf.tensorSections
  - OAI.KLInvariance.MomentGraph.Sheaf.tensorSections_tmul
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:989
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChange
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:995
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.tensorAssignments
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:998
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.tensorAssignments_tmul
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1001
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChange_tmul_compatible
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1007
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.tensorSections
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1016
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.tensorSections_tmul
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read baseChange and both natural tensor maps. Retained arbitrary commutative
    scalar extension and graph, the full-assignment convention, and pure-tensor/additivity
    verification before the later finite-flat isomorphism.
tags:
- Kazhdan-Lusztig
- sheaf-operations
---

# Tensor base change of a graph sheaf

Let \(R,S\) be commutative rings with a fixed homomorphism \(\varphi:R\to S\), making \(S\) an \(R\)-algebra. Let \(B\) be an \(R\)-linear sheaf on an ordered graph \(G\), with vertex set \(V\), edge set \(E\), endpoint maps \(s(e),t(e)\), and restrictions \(\rho^-_e,\rho^+_e\).

Its **tensor base change** \(B_S\) is the \(S\)-linear sheaf with
\[
B_S^x=S\otimes_R B^x,\qquad B_S^e=S\otimes_R B^e,
\]
\[
\rho^{S,-}_e(s\otimes v)=s\otimes\rho^-_e(v),
\qquad
\rho^{S,+}_e(s\otimes w)=s\otimes\rho^+_e(w).
\]
Scalars in \(S\) act on the first tensor factor. The balancing relation
\(s\varphi(r)\otimes v=s\otimes rv\) makes these formulas well defined.

## Assignments after scalar extension

An assignment has one value at every vertex:
\[
P_B=\prod_{x\in V}B^x.
\]
The source's tensorAssignments map is
\[
\Phi_B:S\otimes_R P_B\longrightarrow\prod_{x\in V}(S\otimes_R B^x),
\qquad
\Phi_B(s\otimes f)_x=s\otimes f_x.
\]
For a finite sum of pure tensors, its \(x\)-coordinate is the sum of their \(x\)-coordinates.

## The natural map on sections

For a subset \(\Omega\subseteq V\), the section module \(\Gamma_\Omega(B)\) consists of full assignments satisfying the edge equation whenever both endpoints lie in \(\Omega\).

If \(f\in\Gamma_\Omega(B)\), then for such an edge
\[
\rho^{S,-}_e(s\otimes f_{s(e)})
=s\otimes\rho^-_e(f_{s(e)})
=s\otimes\rho^+_e(f_{t(e)})
=\rho^{S,+}_e(s\otimes f_{t(e)}).
\]
Thus \((s\otimes f_x)_x\) is compatible. Additivity gives the natural \(S\)-linear section map
\[
\Theta_\Omega:S\otimes_R\Gamma_\Omega(B)\longrightarrow\Gamma_\Omega(B_S),
\qquad
\Theta_\Omega(s\otimes f)_x=s\otimes f_x.
\]
The construction is the composite of the tensor of the section inclusion with \(\Phi_B\), with codomain restricted to compatible assignments.

The [[node:kl.sheaves.flat_section_base_change|flat section base-change theorem]] proves that \(\Theta_\Omega\) is an isomorphism when the vertex and edge sets are finite and \(S\) is flat over \(R\).

## A one-edge calculation

For \(R=k[\alpha]\), take the congruence sheaf with stalks \(R\), edge module \(R/(\alpha)\), and both restrictions the quotient map. A global section is a pair \((a,b)\) with \(a-b\in(\alpha)\). Its pure tensor image is \((s\otimes a,s\otimes b)\), and the difference of the two edge restrictions is
\[
s\otimes[a-b]=0.
\]
This is the compatibility calculation used in the general construction.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.baseChange`: [MinimalExtensions.lean:989](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L989).

`OAI.KLInvariance.MomentGraph.Sheaf.tensorAssignments`: [MinimalExtensions.lean:995](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L995).

`OAI.KLInvariance.MomentGraph.Sheaf.tensorAssignments_tmul`: [MinimalExtensions.lean:998](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L998).

`OAI.KLInvariance.MomentGraph.Sheaf.baseChange_tmul_compatible`: [MinimalExtensions.lean:1001](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1001).

`OAI.KLInvariance.MomentGraph.Sheaf.tensorSections`: [MinimalExtensions.lean:1007](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1007).

`OAI.KLInvariance.MomentGraph.Sheaf.tensorSections_tmul`: [MinimalExtensions.lean:1016](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1016).
