---
id: kl.detail.compatible_sections
title: Compatible assignments and sections on a vertex subset
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
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

# Compatible assignments and sections on a vertex subset

Let \(B\) be a sheaf on an ordered graph with vertex set \(V\) and coefficient ring \(A\). An assignment is a tuple
\[
f=(f_x)_{x\in V}\in\prod_{x\in V}B^x.
\]
For \(\Omega\subseteq V\), it is compatible on \(\Omega\) when
\[
\rho_{s(e),e}(f_{s(e)})=\rho_{t(e),e}(f_{t(e)})
\]
for every edge whose two endpoints belong to \(\Omega\).

The section module used by the local development is the submodule of ambient assignments
\[
\Gamma(\Omega,B)=
\{f\in\prod_{x\in V}B^x:f\text{ is compatible on }\Omega\}.
\]
Linearity of the restriction maps makes the zero assignment compatible and preserves compatibility under addition and scalar multiplication. This proves that the displayed set is an \(A\)-module.

## Coordinates on the subset

Let \(\Gamma_{\mathrm{res}}(\Omega,B)\) denote compatible tuples indexed just by \(x\in\Omega\). Projection to these coordinates gives
\[
\Gamma(\Omega,B)\longrightarrow\Gamma_{\mathrm{res}}(\Omega,B).
\]
Its kernel consists of arbitrary assignments supported on \(V\setminus\Omega\). Extending a tuple by zero outside \(\Omega\) is a right inverse: every tested edge has both endpoints in \(\Omega\). Hence
\[
\Gamma(\Omega,B)\simeq
\Gamma_{\mathrm{res}}(\Omega,B)\times
\prod_{x\notin\Omega}B^x.
\]

For \(\Omega'\subseteq\Omega\), compatibility on \(\Omega\) implies compatibility on \(\Omega'\), because fewer edges are tested. Thus the ambient modules have an inclusion \(\Gamma(\Omega,B)\subseteq\Gamma(\Omega',B)\). On restricted tuples, forgetting coordinates gives the usual restriction map to \(\Gamma_{\mathrm{res}}(\Omega',B)\).

## One edge

Take one edge \(x\to y\), with \(B^x=B^y=A\), edge module \(A/(\alpha)\), and quotient restrictions. On all vertices,
\[
\Gamma(\{x,y\},B)=\{(f_x,f_y):f_x-f_y\in\alpha A\}.
\]
For \(\Omega=\{y\}\), no edge has both endpoints in \(\Omega\), so
\[
\Gamma(\{y\},B)=A\times A,\qquad
\Gamma_{\mathrm{res}}(\{y\},B)=A.
\]
Projection to the second coordinate relates these two descriptions.

## Global generation and boundary evaluation

Global sections are \(\Gamma(V,B)\). The sheaf is globally generated when every evaluation map \(\Gamma(V,B)\to B^x\) is surjective. In the example, the pair \((a,a)\) gives a global section taking value \(a\) at either vertex.

To construct the boundary image at \(x\), the development uses compatible ambient assignments on the vertices strictly above \(x\). The boundary map evaluates their coordinates at the upper endpoints of outgoing edges and applies the upper restriction maps. The coordinates read by this map all lie in that upper subset.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization



`OAI.KLInvariance.MomentGraph.Sheaf.CompatibleOn`: [Sheaves.lean:41](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L41).

`OAI.KLInvariance.MomentGraph.Sheaf.sections`: [Sheaves.lean:161](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L161).

`OAI.KLInvariance.MomentGraph.Sheaf.Generated`: [Sheaves.lean:175](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L175).
