---
id: kl.detail.upper_quotient
title: The upper-end edge quotient rule
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.graded_sheaf
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.UpperQuotient
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:401
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.UpperQuotient
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

# The upper-end edge quotient rule

Let \(\alpha_e\in A_1\) label an edge \(e:x\to y\). The upper-end quotient rule requires that
\[
\rho_{y,e}:B^y\longrightarrow B^e
\]
be surjective and have kernel exactly \(\alpha_e B^y\). Equivalently,
\[
B^e\simeq B^y/\alpha_e B^y.
\]
This describes both the edge module and its distinguished map from the upper stalk. An abstract module isomorphism alone would not specify that map.

If multiplication by \(\alpha_e\) is injective on \(B^y\), the associated graded exact sequence is
\[
0\longrightarrow B^y(-1)\xrightarrow{\alpha_e}B^y
\longrightarrow B^e\longrightarrow0.
\]
The degree convention here is that multiplication by a linear label raises degree by one. It yields the factor \(1-q\) in the edge Hilbert series.

The quotient rule makes no corresponding assertion that the lower stalk is quotiented by the same principal submodule. The lower restriction and its images retain the boundary information that the comparison proof needs.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization



`OAI.KLInvariance.MomentGraph.GradedSheaf.UpperQuotient`: [GradedSheaves.lean:401](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L401).
