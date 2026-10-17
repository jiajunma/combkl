---
id: kl.detail.edge_factor
title: The reduced-root product attached to an edge
kind: definition
status: formalized
primary_topic: kl.06_reflection_orders
topics:
- kl.06_reflection_orders
uses:
- kl.detail.polynomial_labels
- kl.realization.reflection_plane
- kl.notes.reflection_order
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.TitsSpace.edgeFactor
  - OAI.KLInvariance.TitsSpace.edgeFactor_nonzero
  - OAI.KLInvariance.TitsSpace.edgeFactor_homogeneous
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:944
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.edgeFactor
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:954
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.edgeFactor_nonzero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:966
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.edgeFactor_homogeneous
  - artifact: openai-kl-paper
    locator: Related paper context; edge:lattice
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
- localization
---

# The reduced-root product attached to an edge

For an upward edge \(x\to r_\alpha x\), work in the edge coefficient ring
\[
A_\alpha=\operatorname{Sym}(V)/(\alpha)\simeq\operatorname{Sym}(V/\mathbb R\alpha).
\]
The inversion-root change determines finitely many root planes \(P\) containing \(\alpha\), each with a nonnegative integral weight \(k_P\). More concretely, the signed root-change contributions are paired by reflection in \(\alpha\), and one representative of each contributing pair is grouped by its root plane.

Choose the prescribed root representative \(\beta_P\) in each supported plane and let \(\overline\beta_P\) be its nonzero image modulo \(\alpha\). Define the edge factor
\[
f_e=\prod_P\overline\beta_P^{\,k_P}\in A_\alpha.
\]
This is the actual product used to scale upper edge images. It is nonzero and homogeneous of degree \(\sum_Pk_P\), because the quotient is a polynomial domain and every reduced root factor has degree one.

The separate degree theorem identifies this sum with
\((\ell(r_\alpha x)-\ell(x)-1)/2\). The factor itself retains the root-plane information; replacing it by an unrelated polynomial of the same degree would lose the local image comparison.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L26).

## Lean formalization



`OAI.KLInvariance.TitsSpace.edgeFactor`: [ReflectionSchedules.lean:944](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L944).

`OAI.KLInvariance.TitsSpace.edgeFactor_nonzero`: [ReflectionSchedules.lean:954](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L954).

`OAI.KLInvariance.TitsSpace.edgeFactor_homogeneous`: [ReflectionSchedules.lean:966](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L966).
