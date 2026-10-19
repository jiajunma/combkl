---
id: kl.detail.graded_sheaf
title: Graded sheaves and homogeneous restriction maps
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.graph_sheaf
- kl.sheaves.graded_module
- kl.detail.graded_maps_shifts
- kl.algebra.homogeneous_subquotients
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf
  - OAI.KLInvariance.MomentGraph.GradedSheaf.sections_homogeneous
  - OAI.KLInvariance.MomentGraph.GradedSheaf.sections
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:20
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:57
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.sections_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:65
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.sections
  - artifact: openai-kl-paper
    locator: Related paper context; bg:bmp
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
- moment_graph_sheaves
---

# Graded sheaves and homogeneous restriction maps

Fix a graded coefficient algebra \(A=\bigoplus_nA_n\). A graded sheaf assigns a finite nonnegatively graded \(A\)-module \(B^x\) to every vertex and one \(B^e\) to every edge. The lower and upper restrictions preserve degree:
\[
\rho^-_e(B^{s(e)}_n)\subseteq B^e_n,\qquad
\rho^+_e(B^{t(e)}_n)\subseteq B^e_n.
\]
These vertex modules, edge modules, and two families of degree-zero maps are the complete graded sheaf data.

Forgetting the homogeneous components gives its underlying module-valued sheaf.

## Homogeneous sections

Call a section homogeneous of degree \(n\) when its value at every vertex lies in the degree-\(n\) part of that stalk.

Suppose \(m\) is compatible on a set \(\Omega\). Applying the degree-\(n\) component map to an edge equation gives
\[
\rho^-_e((m_{s(e)})_n)=\rho^+_e((m_{t(e)})_n),
\]
because the restrictions preserve degree. Thus the coordinatewise degree-\(n\) component is compatible on \(\Omega\).

When the vertex set is finite, each assignment is a finite sum of its homogeneous components: take the union of the finitely many degree supports of its stalk coordinates. Uniqueness holds at every coordinate. The compatible assignments therefore form a graded submodule of the assignment module.

If \(A\) is Noetherian, that submodule is finitely generated, since the finite product of stalks is finitely generated. It is then itself finite graded module data, as used by the sheaf construction.

## Boundaries and kernels

For a finite edge set, the boundary module at a vertex is a finite product of graded edge modules. The boundary map is degree zero, so its image has the quotient/image grading.

Intersections of outgoing restriction kernels are homogeneous: if every selected restriction annihilates a vector, it also annihilates each of its homogeneous components. These gradings supply the pieces measured by the Hilbert values.

For the one-edge congruence sheaf over \(k[\alpha]\), the section basis \((1,1),(\alpha,0)\) has degrees zero and one. The component decomposition is obtained by taking polynomial components in both coordinates.

## References

The local definitions and constructions are listed below.

## Lean formalization

The same four fields carry graded module data and degree-zero maps.

`OAI.KLInvariance.MomentGraph.GradedSheaf`: [GradedSheaves.lean:20](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L20).

`OAI.KLInvariance.MomentGraph.GradedSheaf.sections_homogeneous`: [GradedSheaves.lean:57](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L57).

`OAI.KLInvariance.MomentGraph.GradedSheaf.sections`: [GradedSheaves.lean:65](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L65).
