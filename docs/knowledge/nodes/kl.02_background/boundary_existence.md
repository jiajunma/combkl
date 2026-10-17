---
id: kl.sheaves.boundary_existence
title: Existence of the Bruhat minimal-boundary sheaf
kind: theorem
status: proved
primary_topic: kl.02_background
topics:
- kl.02_background
uses:
- kl.sheaves.boundary_sheaf
- kl.sheaves.minimal_cover
- kl.foundations.finite_intervals
- kl.notes.boundary_image
- kl.notes.minimal_cover_existence
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.BruhatGraph.exists_boundarySheaf
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:172
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.exists_boundarySheaf
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
    format: section
    note: Chapter organization follows the paper; Lean references identify the precise
      formal statements.
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

# Existence of the Bruhat minimal-boundary sheaf

For a finite-generator Coxeter system and \(u\le b\), choose a real basis of the extended Tits realization and express roots as degree-one coordinate polynomials. The Bruhat interval graph admits a minimal-boundary sheaf with top \(b\).

*Proof.*

[[node:kl.foundations.finite_intervals]] makes the vertex and edge sets finite. The coordinate polynomial ring has no negative-degree part, reduction modulo positive degree leaves the real scalars, and root labels are homogeneous of degree one.

Apply the finite ordered-graph construction. Start with the unit module at the top and descend through the vertices. At each new vertex, take a minimal free cover of the boundary image determined by the already constructed upper part, and use it to define the outgoing restriction maps. Induction preserves the edge quotient conditions, extension and generation of sections, and minimality.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.exists_boundarySheaf`: [SheafMorphisms.lean:172](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L172).
