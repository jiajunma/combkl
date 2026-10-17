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

### Step 1. Construct the new modules and restrictions

Let \(x\) be the new bottom vertex and let the old graph contain all its upper targets \(y_e\). Set
\(Q_e=B^{y_e}/\alpha_eB^{y_e}\).
For an old global section \(f\), take its tuple of quotient values \((f_{y_e}\bmod\alpha_e)_e\). Let \(D_x\) be the image of this map.

Choose a minimal graded free cover \(p:F_x\twoheadrightarrow D_x\), as constructed in [[node:kl.notes.minimal_cover_existence]]. The new stalk is \(F_x\); the lower map along \(e\) is its \(e\)-component under \(F_x\to D_x\subseteq\bigoplus_eQ_e\). The upper map is the quotient map \(B^{y_e}\to Q_e\). Old modules and restrictions are unchanged.

### Step 2. Characterize a global section of the extension

A pair \((v,f)\), with \(v\in F_x\) and \(f\) an old global section, is a new global section exactly when \(p(v)\) equals the boundary tuple of \(f\). Old edges are compatible because \(f\) is; each new edge imposes exactly one coordinate of this equality.

Every old global section extends: its boundary tuple belongs to \(D_x\) by definition, so choose a preimage under the surjection \(p\).

### Step 3. Prove extension from an edge-closed subset

Let \(\Omega\) be closed upward along the actual edges, and let a compatible assignment be given there. Restrict to the old vertices, obtaining an edge-closed subset of the old graph. Use its extension property to get an old global section \(g\).

If \(x\notin\Omega\), choose any lift of the boundary tuple of \(g\) under \(p\), as in Step 2. This changes none of the prescribed coordinates.

If \(x\in\Omega\), edge closure forces every target \(y_e\) into \(\Omega\). Thus \(g\) agrees with the prescribed assignment at each \(y_e\). Its boundary tuple equals \(p(v)\) for the already prescribed \(v\in F_x\), by compatibility on the new edges. Retain that \(v\). Again Step 2 proves global compatibility.

### Step 4. Prove global generation

At an old vertex, choose an old global section realizing the desired stalk value and extend it using Step 2. At \(x\), start with an arbitrary \(v\in F_x\). Its image \(p(v)\in D_x\) is, by the definition of \(D_x\), the boundary tuple of some old global section \(f\). The pair \((v,f)\) is then global and realizes \(v\).

### Step 5. Check the remaining construction data

The new stalk is free by the cover construction. New upper maps satisfy the quotient rule by definition. The outgoing boundary map at \(x\) has kernel \(\ker p\), contained in \(A_{>0}F_x\), so it is minimal. At every old vertex no outgoing edge or stalk changed, so its previous minimality condition remains valid.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization



`OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom`: [GradedSheaves.lean:150](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L150).

`OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_edgeFlabby`: [GradedSheaves.lean:207](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L207).

`OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_generated`: [GradedSheaves.lean:190](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L190).
