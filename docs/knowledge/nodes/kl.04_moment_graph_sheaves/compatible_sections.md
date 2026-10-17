---
id: kl.detail.compatible_sections
title: Compatible sections and restriction to a vertex subset
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
  - Sheaves
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.CompatibleOn
  - OAI.KLInvariance.MomentGraph.Sheaf.sections
  - OAI.KLInvariance.MomentGraph.Sheaf.Generated
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Sheaves:41
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.CompatibleOn
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Sheaves:161
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.sections
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Sheaves:175
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.Generated
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

# Compatible sections and restriction to a vertex subset

Let \(B\) be a sheaf on an ordered graph. A section over \(\Omega\subseteq V\) assigns an element \(f_x\in B^x\) to each \(x\in\Omega\), subject to
\[
\rho_{x,e}(f_x)=\rho_{y,e}(f_y)
\quad\text{whenever }e:x\to y\text{ has }x,y\in\Omega.
\]
These assignments form an \(A\)-module \(\Gamma(\Omega,B)\). Restriction to a smaller subset preserves compatibility.

The implementation represents an assignment on every vertex and ignores its coordinates outside \(\Omega\) when testing compatibility. Consequently its section module includes those unused coordinates. This bookkeeping convention preserves the extension statements used here; it should not be confused with imposing edge conditions outside \(\Omega\).

Global sections are sections over all vertices. A sheaf is globally generated at its stalks when every evaluation map
\[
\Gamma(V,B)\longrightarrow B^x
\]
is surjective. This is distinct from flabbiness, which concerns extending entire compatible assignments. On one edge, compatibility is equality of the two restriction values, not equality of the stalk elements themselves.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization



`OAI.KLInvariance.MomentGraph.Sheaf.CompatibleOn`: [Sheaves.lean:41](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L41).

`OAI.KLInvariance.MomentGraph.Sheaf.sections`: [Sheaves.lean:161](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L161).

`OAI.KLInvariance.MomentGraph.Sheaf.Generated`: [Sheaves.lean:175](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L175).
