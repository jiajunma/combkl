---
id: kl.detail.section_duality
title: Balanced perfect duality on global sections
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.notes.supported_pairings
- kl.sheaves.boundary_sheaf
- kl.detail.polynomial_labels
lean:
  repository: openai-kl
  modules:
  - Support
  declarations:
  - OAI.KLInvariance.BruhatGraph.SectionDuality
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1432
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.SectionDuality
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

# Balanced perfect duality on global sections

For a minimal-boundary sheaf \(B\), put \(\Gamma=\Gamma(V,B)\). A section duality is an \(A\)-linear isomorphism
\[
d:\Gamma\xrightarrow{\sim}\operatorname{Hom}_A(\Gamma,A),
\]
equivalently a perfect bilinear pairing \(\langle m,n\rangle=d(m)(n)\), satisfying balance with each integral vertex cut:
\[
\langle C_xm,n\rangle=\langle m,C_xn\rangle.
\]

A cut isolates the coordinate at \(x\) after multiplying by a common product of edge labels. This multiplication ensures that the isolated assignment is still an integral global section. It avoids treating a coordinate projection over the fraction field as an endomorphism of the original section module.

Perfection identifies every linear functional with pairing against a unique section. Cut balance then identifies the dual of a stalk with sections supported at that vertex. The resulting costalk identification includes the edge-label factors arising from support; it is not an ungraded restriction of a pairing to an arbitrary direct summand.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization

The fields `pairing` and `balanced` encode the linear equivalence with the dual and the cut-balance equation.

`OAI.KLInvariance.BruhatGraph.SectionDuality`: [Support.lean:1432](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1432).
