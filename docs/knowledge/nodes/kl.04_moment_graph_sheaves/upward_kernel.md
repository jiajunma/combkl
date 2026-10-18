---
id: kl.sheaves.upward_kernel
title: Kernels of upward edge conditions
kind: definition
status: formalized
primary_topic: kl.04_moment_graph_sheaves
topics:
- kl.04_moment_graph_sheaves
uses:
- kl.sheaves.graph_sheaf
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.upwardKernel
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:599
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.upwardKernel
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
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
- background
---

# Kernels of upward edge conditions

For a vertex \(x\) and a set \(F\) of its upward edges, define
\[
L_x(F)=\{v\in B^x:\rho_{x,e}(v)=0\text{ for every }e\in F\}.
\]
The empty set gives \(L_x(\varnothing)=B^x\). Adding edge conditions decreases this submodule. For an edge \(e:x\to y\), map \(L_x(F)\) and \(L_y(G)\) into the common edge module to obtain the lower and upper images.

When \(F\) contains every outgoing edge at \(x\), this is the full outgoing kernel, called the costalk in this blueprint. At a top vertex there are no outgoing edges, so its full outgoing kernel is the whole stalk. A suffix kernel uses only the outgoing edges still present in a suffix of the chosen schedule.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.upwardKernel`: [GradedSheaves.lean:599](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L599).
