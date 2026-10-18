---
id: kl.detail.polynomial_labels
title: Reflection roots as polynomial edge labels
kind: definition
status: formalized
primary_topic: kl.03_realizations_and_grading
topics:
- kl.03_realizations_and_grading
uses:
- kl.foundations.bruhat_step
- kl.notes.extended_realization
- kl.detail.positive_roots
- kl.detail.root_reflection_correspondence
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.BruhatGraph.root
  - OAI.KLInvariance.BruhatGraph.polynomialLabel
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:141
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.root
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:144
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.polynomialLabel
  - artifact: openai-kl-paper
    locator: Related paper context; bg:realization
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
- realizations_and_grading
---

# Reflection roots as polynomial edge labels

Fix a finite-generator real realization \(V\) and its symmetric algebra \(A=\operatorname{Sym}_{\mathbb R}(V)\). For an upward edge \(e:x\to y\), the group element \(yx^{-1}\) is a reflection. Choose its distinguished positive root \(\alpha_e\), embed that root in the extended realization, and take its degree-one image in \(A\).

After choosing a basis of \(V\), this is a linear polynomial in a polynomial ring:
\[
\alpha_e=\sum_i a_iX_i.
\]
The coordinates describe the same symmetric-algebra element; they do not change which reflection labels the edge.

The resulting nonzero linear form generates the edge ideal \((\alpha_e)\). Thus the edge coefficient ring is \(A/(\alpha_e)\), and root-plane localization is controlled by which of these linear forms remain nonunits. Keeping the reflection, its root vector, its linear polynomial, and its quotient ring distinct avoids conflating four different objects that participate in the proof.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L34).

## Lean formalization



`OAI.KLInvariance.BruhatGraph.root`: [SheafMorphisms.lean:141](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L141).

`OAI.KLInvariance.BruhatGraph.polynomialLabel`: [SheafMorphisms.lean:144](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L144).
