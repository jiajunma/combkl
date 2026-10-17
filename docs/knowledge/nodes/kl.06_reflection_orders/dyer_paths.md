---
id: kl.paths.dyer_paths
title: The decreasing-path formula for a geometric reflection order
kind: theorem
status: proved
primary_topic: kl.06_reflection_orders
topics:
- kl.06_reflection_orders
uses:
- kl.foundations.rtilde
- kl.foundations.bruhat_step
- kl.notes.reflection_order
- kl.notes.path_product
lean:
  repository: openai-kl
  modules:
  - ReflectionOrders
  declarations:
  - OAI.KLInvariance.WallDyer.geometric_entry_eq_rTilde
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionOrders:1229
    format: lean-location
    note: OAI.KLInvariance.WallDyer.geometric_entry_eq_rTilde
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
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
- background
---

# The decreasing-path formula for a geometric reflection order

Fix a finite lower Bruhat region and the constructed geometric reflection order. The \(x,y\) entry of the ordered edge-transfer product is
\[
\widetilde R_{x,y}(T).
\]
Expanding the product assigns \(T\) to each edge, so a composable decreasing reflection path contributes \(T\) raised to its length.

*Proof.*

Express the matrix entry as a sum over ordered subpaths. For a reflection-ratio order adapted to the upper endpoint, this path polynomial satisfies the R-tilde recursion. Wall sweeps and dihedral-plane identities then show that the entry is independent of the generic linear functional defining the order. Compare the geometric functional with the adapted one to obtain the formula.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.WallDyer.geometric_entry_eq_rTilde`: [ReflectionOrders.lean:1229](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionOrders.lean#L1229).
