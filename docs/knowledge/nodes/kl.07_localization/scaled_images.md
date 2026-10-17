---
id: kl.detail.scaled_images
title: Scaled equality of embedded edge images
kind: definition
status: formalized
primary_topic: kl.07_localization
topics:
- kl.07_localization
uses:
- kl.detail.edge_images
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.ScaledImages
  - OAI.KLInvariance.MomentGraph.Sheaf.scaledImages_iff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:443
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.ScaledImages
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:450
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.scaledImages_iff
  - artifact: openai-kl-paper
    locator: Related paper context; edge:lattice
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- localization
---

# Scaled equality of embedded edge images

For \(r\in A\), scaled image equality along \(e:x\to y\) means
\[
L_e(F)=r\,U_e(H)\quad\text{inside }B^e.
\]
Equivalently, every edge value \(z\) satisfies
\[
\bigl(\exists v\in K_x(F),\ \rho_{x,e}(v)=z\bigr)
\Longleftrightarrow
\bigl(\exists w\in K_y(H),\ r\rho_{y,e}(w)=z\bigr).
\]
This elementwise formulation is convenient when transporting the statement through actual sheaf isomorphisms.

The scalar is the reduced-root product in the edge comparison. The quotient by the edge label is already built into \(B^e\); scaling by \(r\) is an additional operation in that quotient module.

The main argument first proves one-sided inclusion. Endpoint equality of Hilbert states then upgrades the inclusion to this equality of embedded submodules, providing the hypothesis needed to recover freeness in reverse order.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L26).

## Lean formalization



`OAI.KLInvariance.MomentGraph.Sheaf.ScaledImages`: [CharacterReciprocity.lean:443](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L443).

`OAI.KLInvariance.MomentGraph.Sheaf.scaledImages_iff`: [CharacterReciprocity.lean:450](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L450).
