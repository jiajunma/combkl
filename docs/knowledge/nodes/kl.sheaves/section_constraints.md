---
id: kl.sheaves.section_constraints
title: Section and outgoing-kernel constraint maps
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.compatible_sections
- kl.sheaves.upward_kernel
- kl.sheaves.graph_sheaf
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.constraint
  - OAI.KLInvariance.MomentGraph.Sheaf.ker_constraint
  - OAI.KLInvariance.MomentGraph.Sheaf.kernelConstraint
  - OAI.KLInvariance.MomentGraph.Sheaf.ker_kernelConstraint
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1031
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.constraint
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1036
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.ker_constraint
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:317
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.kernelConstraint
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:321
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.ker_kernelConstraint
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read both constraint definitions and their kernel equalities. Specified
    the internal-edge subtype for sections, the selected outgoing-edge subtype for
    a stalk, and both coordinatewise equivalences.
tags:
- Kazhdan-Lusztig
- sheaf-operations
---

# Section and outgoing-kernel constraint maps

Let \(R\) be a commutative ring and \(B\) an \(R\)-linear sheaf on an ordered graph with vertices \(V\), edges \(E\), and source and target maps \(s,t\).

## The section constraint

For \(\Omega\subseteq V\), let
\[
E_\Omega=\{e\in E:s(e)\in\Omega,\ t(e)\in\Omega\}.
\]
Define
\[
\delta_\Omega:\prod_{x\in V}B^x\longrightarrow\prod_{e\in E_\Omega}B^e,
\qquad
(\delta_\Omega f)_e
=\rho^-_e(f_{s(e)})-\rho^+_e(f_{t(e)}).
\]
This is the source's constraint map. It is linear because each coordinate is the difference of two composites of linear maps.

The kernel is exactly the section module:
\[
\ker\delta_\Omega=\Gamma_\Omega(B).
\]
Indeed \(\delta_\Omega f=0\) means that every displayed coordinate difference is zero, which is precisely the compatibility equation on each edge with both endpoints in \(\Omega\).

The domain retains every vertex coordinate. The subset \(\Omega\) selects the equations. In particular, if \(E_\Omega\) is empty, the target is the zero module and every full assignment is a section over \(\Omega\).

## The selected outgoing constraint

Fix \(x\in V\), and let \(F\) be a subset of the outgoing edges \(e\) with \(s(e)=x\). Define
\[
\kappa_{x,F}:B^x\longrightarrow\prod_{e\in F}B^e,
\qquad
\kappa_{x,F}(v)_e=\rho^-_e(v).
\]
This is kernelConstraint. It takes the relevant coordinates of the combined outgoing stalk map.

Its kernel is the selected outgoing kernel:
\[
\ker\kappa_{x,F}
=K_x(F)
=\{v:\rho^-_e(v)=0\text{ for every }e\in F\}.
\]
For the forward implication, evaluate the zero tuple at a chosen \(e\in F\). For the reverse implication, all tuple coordinates vanish by the defining condition, so the tuple is zero.

If \(F=\varnothing\), then \(K_x(F)=B^x\). If \(F\) contains every outgoing edge, this is the full outgoing kernel.

## The one-edge congruence model

Over a commutative ring \(A\), take an edge \(x\to y\) labelled by \(\alpha\in A\), with stalks \(A\), edge module \(A/(\alpha)\), and quotient restrictions. The full section constraint is
\[
\delta(a,b)=[a-b].
\]
Its kernel consists of congruent pairs. The single outgoing constraint at \(x\) is
\[
\kappa_{x,\{e\}}(a)=[a],
\]
whose kernel is \(\alpha A\).

The flat base-change arguments apply to these two constraint maps. Their product targets are finite when the graph has finitely many edges.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.constraint`: [MinimalExtensions.lean:1031](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1031).

`OAI.KLInvariance.MomentGraph.Sheaf.ker_constraint`: [MinimalExtensions.lean:1036](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1036).

`OAI.KLInvariance.MomentGraph.Sheaf.kernelConstraint`: [TerminalKernels.lean:317](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L317).

`OAI.KLInvariance.MomentGraph.Sheaf.ker_kernelConstraint`: [TerminalKernels.lean:321](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L321).
