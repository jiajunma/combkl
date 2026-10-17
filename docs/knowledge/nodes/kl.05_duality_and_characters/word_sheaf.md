---
id: kl.detail.word_sheaf
title: The pair-projection sheaf of a Bott–Samelson module
kind: definition
status: formalized
primary_topic: kl.05_duality_and_characters
topics:
- kl.05_duality_and_characters
uses:
- kl.notes.bott_samelson
- kl.notes.word_stalks
- kl.sheaves.graph_sheaf
lean:
  repository: openai-kl
  modules:
  - Frobenius
  - Decomposition
  declarations:
  - OAI.KLInvariance.TitsSpace.bottProjectionSheaf
  - OAI.KLInvariance.PairProjection.relation
  - OAI.KLInvariance.PairProjection.compatible_iff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1761
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottProjectionSheaf
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:153
    format: lean-location
    note: OAI.KLInvariance.PairProjection.relation
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:168
    format: lean-location
    note: OAI.KLInvariance.PairProjection.compatible_iff
  - artifact: openai-kl-paper
    locator: Related paper context; bg:normalization
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
- duality_and_characters
---

# The pair-projection sheaf of a Bott–Samelson module

Let \(M_{\mathbf s}\) be a Bott–Samelson word module and let
\(p_x:M_{\mathbf s}\twoheadrightarrow M_{\mathbf s}^x\) be its weight-stalk projections. On an edge \(e:x\to y\), form
\[
B^e=(M_{\mathbf s}^x\oplus M_{\mathbf s}^y)/
\operatorname{im}(p_x,p_y).
\]
The lower map sends \(v\) to the class of \((v,0)\); the upper map sends \(w\) to the negative of the class of \((0,w)\). Consequently
\[
\rho_{x,e}(v)=\rho_{y,e}(w)
\quad\Longleftrightarrow\quad
(v,w)=(p_x(m),p_y(m))\text{ for some }m\in M_{\mathbf s}.
\]
This is the pair-projection sheaf: its edge compatibility records simultaneous lifting of two stalk coordinates.

Every word-module element supplies a global section by applying all the projections. Since the projections onto stalk images are surjective, these sections generate every stalk. Surjectivity onto all compatible sections is a separate theorem; pairwise lifting alone does not automatically supply a single simultaneous lift over an arbitrary subset.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization



`OAI.KLInvariance.TitsSpace.bottProjectionSheaf`: [Frobenius.lean:1761](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1761).

`OAI.KLInvariance.PairProjection.relation`: [Decomposition.lean:153](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L153).

`OAI.KLInvariance.PairProjection.compatible_iff`: [Decomposition.lean:168](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L168).
