---
id: kl.local.localized_decomposition
title: Decomposition of the sheaf after root-plane localization
kind: theorem
status: proved
primary_topic: kl.07_localization
topics:
- kl.07_localization
uses:
- kl.sheaves.boundary_sheaf
- kl.sheaves.relative_flabbiness
- kl.notes.dihedral_models
- kl.notes.sheaf_localization
lean:
  repository: openai-kl
  modules:
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.localized_boundary_decomposition
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:200
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.localized_boundary_decomposition
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

# Decomposition of the sheaf after root-plane localization

In a finite-generator real realization, localize at a root plane and restrict to its dihedral coset. The constructed boundary sheaf is isomorphic to a finite sum of local dihedral models with finite multiplicities. This is an isomorphism of sheaves preserving vertex modules, edge modules, and both endpoint restriction maps.

*Proof.*

Verify the inputs of the local model decomposition theorem for the localized sheaf. Flat base change preserves freeness and finite generation of stalks. The localized restriction maps give the edge quotient conditions. Relative section extension supplies flabbiness, and generation by sections is transported as well.

Apply the descending construction using minimal covers and splittings of the local models. It produces the model sum together with the required sheaf isomorphism.

## References

[4. Localization at a root plane](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L2).

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.localized_boundary_decomposition`: [TerminalKernels.lean:200](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L200).
