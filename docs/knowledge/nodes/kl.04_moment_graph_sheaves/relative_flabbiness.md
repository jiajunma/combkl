---
id: kl.sheaves.relative_flabbiness
title: Extension from subsets closed under surviving edges
kind: theorem
status: proved
primary_topic: kl.04_moment_graph_sheaves
topics:
- kl.04_moment_graph_sheaves
uses:
- kl.sheaves.flabbiness
lean:
  repository: openai-kl
  modules:
  - Sheaves
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.extend_closedUnder
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Sheaves:106
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.extend_closedUnder
  - artifact: openai-kl-paper
    locator: 4. Localization at a root plane; sec:localization
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
- localization
---

# Extension from subsets closed under surviving edges

Let the vertex set be finite and let \(B\) be flabby. Choose a set \(E_0\) of surviving edges, and assume that every edge module outside \(E_0\) is zero. If
\[
e\in E_0,\ s(e)\in\Omega\Longrightarrow t(e)\in\Omega,
\]
every compatible section on \(\Omega\) extends to a global section.

*Proof.*

Induct on the number of vertices not yet assigned. Choose a maximal such vertex \(a\). Every vertex strictly above \(a\) already has a value, so flabbiness supplies a value at \(a\) compatible with those values. A surviving edge from an assigned lower vertex to \(a\) would force \(a\in\Omega\), contrary to its choice. All remaining such edges have zero modules, and impose no condition. Add \(a\) and continue the induction.

## References

[4. Localization at a root plane](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L2).

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.extend_closedUnder`: [Sheaves.lean:106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L106).
