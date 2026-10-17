---
id: kl.notes.boundary_image
title: The boundary image that determines a new stalk
kind: definition
status: formalized
primary_topic: kl.02_background
topics:
- kl.02_background
uses:
- kl.sheaves.graph_sheaf
- kl.sheaves.graded_module
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.boundaryHom
  - OAI.KLInvariance.MomentGraph.GradedSheaf.boundaryImage
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:74
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.boundaryHom
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:81
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.boundaryImage
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; bg:bmp
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the mathematical hypotheses and scope retained from the referenced declarations?
  verdict: The exposition follows the fixed Lean source; worked calculations explain
    the constructions.
tags:
- Kazhdan-Lusztig
- background
---

# The boundary image that determines a new stalk

Suppose that the sheaf has already been constructed strictly above a vertex \(x\). A section on that upper region gives, by restriction from each upper endpoint, a tuple in
\[
\bigoplus_{e:x\to y}B^e.
\]
The image of this map from upper sections is the boundary image \(B^{\delta x}\).

The boundary image is generally smaller than the entire direct sum of outgoing edge modules: the edge values must come from a single compatible section above \(x\). The construction must therefore cover this image, rather than cover all possible edge tuples independently.

For a single outgoing edge, the boundary map is simply restriction from its upper stalk. With two outgoing edges whose upper endpoints are constrained by further edges, the two boundary values are linked by those upper compatibility relations. This is the local reason the construction remembers the entire upper graph.

The map is graded because all restriction maps preserve degrees. Over the Noetherian coefficient ring, its image is again finite graded data. A minimal graded free cover of \(B^{\delta x}\) becomes the stalk at \(x\); composing the cover with coordinate projections defines its outgoing restrictions.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.boundaryHom`: [GradedSheaves.lean:74](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L74).

`OAI.KLInvariance.MomentGraph.GradedSheaf.boundaryImage`: [GradedSheaves.lean:81](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L81).
