---
id: kl.detail.graded_maps_shifts
title: Homogeneous maps and grading shifts
kind: definition
status: formalized
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.sheaves.graded_module
lean:
  repository: openai-kl
  modules:
  - GradedModules
  declarations:
  - OAI.KLInvariance.Graded.ModuleData.Hom
  - OAI.KLInvariance.Graded.ModuleData.shift
  - OAI.KLInvariance.Graded.ModuleData.Hom.shift
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1073
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.Hom
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1244
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.shift
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1260
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.Hom.shift
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# Homogeneous maps and grading shifts

For graded \(A\)-modules \(M=\bigoplus_n M_n\) and \(N=\bigoplus_n N_n\), a homogeneous map of degree zero is an \(A\)-linear map \(f:M\to N\) satisfying \(f(M_n)\subseteq N_n\) for every integer \(n\). These are two pieces of data: the linear map and its grading-preservation condition.

For an integer \(d\ge0\), the positive shift \(M(d)\) has the same underlying module and
\[
M(d)_n=M_{n-d}.
\]
An element of original degree \(r\) has degree \(r+d\) after this shift. For example, the element \(1\) in \(A(2)\) has degree two. This sign convention gives \(\operatorname{ch}(M(d))=q^d\operatorname{ch}(M)\) when \(M\) is graded free.

The shifted map \(f(d):M(d)\to N(d)\) is the same linear map: a vector in degree \(n\) lies in \(M_{n-d}\), whose image lies in \(N_{n-d}\). Restricting to \(d\ge0\) preserves the nonnegative grading required by the module-data object. Degree-shifting linear maps appearing in pairing arguments are stated separately with their explicit integer degree.

## References

The precise Lean sources are listed below.

## Lean formalization

The fields `map` and `graded` record the linear map and degree-zero preservation, respectively.

`OAI.KLInvariance.Graded.ModuleData.Hom`: [GradedModules.lean:1073](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1073).

`OAI.KLInvariance.Graded.ModuleData.shift`: [GradedModules.lean:1244](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1244).

`OAI.KLInvariance.Graded.ModuleData.Hom.shift`: [GradedModules.lean:1260](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1260).
