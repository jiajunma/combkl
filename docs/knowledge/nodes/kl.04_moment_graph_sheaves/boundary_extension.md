---
id: kl.detail.boundary_extension
title: Attaching a new bottom stalk by a minimal cover
kind: theorem
status: proved
primary_topic: kl.04_moment_graph_sheaves
topics:
- kl.04_moment_graph_sheaves
uses:
- kl.notes.boundary_image
- kl.notes.minimal_cover_existence
- kl.detail.upper_quotient
- kl.detail.compatible_sections
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom
  - OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_edgeFlabby
  - OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_generated
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:150
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:207
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_edgeFlabby
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:190
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_generated
  - artifact: openai-kl-paper
    locator: Related paper context; bg:bmp
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- moment_graph_sheaves
---

# Attaching a new bottom stalk by a minimal cover

Suppose a graded sheaf is already constructed on a finite upper part of an ordered graph. Add a new bottom vertex \(x\), with outgoing edges \(e:x\to y_e\) labelled by homogeneous linear forms. Form the edge quotients
\[
Q_e=B^{y_e}/\alpha_eB^{y_e}
\]
and the boundary image \(D_x\subseteq\bigoplus_eQ_e\) of compatible sections above \(x\). Choose a minimal graded free cover \(p:F_x\twoheadrightarrow D_x\).

Set \(B^x=F_x\); its lower restriction maps are the components of \(F_x\to D_x\hookrightarrow\bigoplus_eQ_e\). This extension preserves extension from edge-closed sets, and preserves global generation if the original sheaf was globally generated.

*Proof.*

Any old global section determines an element of \(D_x\), which lifts through the surjection \(p\). That lift supplies the new stalk coordinate, hence a new global section. If a prescribed edge-closed set contains \(x\), it also contains every adjacent upper vertex, so the old extension already has the required boundary values and the prescribed \(x\)-coordinate can be retained. If it omits \(x\), choose a lift freely.

For global generation at \(x\), start with any vector of \(F_x\); its boundary belongs to \(D_x\), so some old global section realizes it. At old vertices, extend a previously generating section by the same lifting argument.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization



`OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom`: [GradedSheaves.lean:150](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L150).

`OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_edgeFlabby`: [GradedSheaves.lean:207](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L207).

`OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_generated`: [GradedSheaves.lean:190](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L190).
