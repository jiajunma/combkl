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
  - OAI.KLInvariance.Graded.ModuleData.Hom.id
  - OAI.KLInvariance.Graded.ModuleData.Hom.comp
  - OAI.KLInvariance.Graded.shift_isInternal
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
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1153
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.Hom.id
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1148
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.Hom.comp
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1226
    format: lean-location
    note: OAI.KLInvariance.Graded.shift_isInternal
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

## Maps and functionals of an integer degree

The dual module \(M^*=\operatorname{Hom}_A(M,A)\) consists of the \(A\)-linear functionals on \(M\), with addition and scalar multiplication defined pointwise.

More generally, an \(A\)-linear map has degree \(r\in\mathbb Z\) when
\[
f(M_n)\subseteq N_{n+r}\qquad(n\in\mathbb Z).
\]
A homogeneous functional of degree \(r\) is an \(A\)-linear map \(\lambda:M\to A\) satisfying
\[
\lambda(M_n)\subseteq A_{n+r}.
\]
Composition adds degrees: if \(f\) has degree \(r\) and \(g\) degree \(s\), then \(g(f(M_n))\subseteq P_{n+r+s}\).

For a basis vector of degree \(d\), its coordinate functional has degree \(-d\): on a degree-\(n\) vector it reads a coefficient of degree \(n-d\). The detailed coefficient argument is in [[node:kl.algebra.dual_basis_degrees]].

## Positive shifts of nonnegative module data

For \(d\in\mathbb N\), the positive shift \(M(d)\) has the same underlying module and
\[
M(d)_n=M_{n-d}.
\]
An element of original degree \(r\) has degree \(r+d\) after this shift. For example, the element \(1\) in \(A(2)\) has degree two. This sign convention gives \(\operatorname{ch}(M(d))=q^d\operatorname{ch}(M)\) when \(M\) is graded free.

The shifted map \(f(d):M(d)\to N(d)\) is the same linear map: a vector in degree \(n\) lies in \(M_{n-d}\), whose image lies in \(N_{n-d}\). Restricting to \(d\ge0\) preserves the nonnegative grading required by the module-data object. Degree-shifting linear maps appearing in pairing arguments are stated separately with their explicit integer degree.

## Identity, composition and shifted components

The identity map preserves every piece. If \(f:M\to N\) and \(g:N\to P\) have degree zero, their composite does too:
\(g(f(M_n))\subseteq g(N_n)\subseteq P_n\).
These are the source's Hom.id and Hom.comp operations.

The shifted component maps are
\[
\pi_n^{M(d)}(m)=\pi_{n-d}^M(m).
\]
The finite set of original component degrees is translated by \(d\), giving a finite shifted decomposition. Projection identities and uniqueness are inherited from \(M\).

For \(a\in A_i\) and \(m\in M(d)_j=M_{j-d}\), the product lies in
\(M_{i+j-d}=M(d)_{i+j}\).
If \(n<0\) and \(d\ge0\), then \(n-d<0\), proving nonnegativity of the shift. Its underlying module and finite generating family stay the same.

The [[node:kl.algebra.component_transport|component-transport theorem]] explains homogeneous preimages, degree preservation by inverse bijections, and the induced grading on kernels and images.

## References

The precise Lean sources are listed below.

## Lean formalization

The fields `map` and `graded` specify the A-linear map and its degree-zero preservation.

`OAI.KLInvariance.Graded.ModuleData.Hom`: [GradedModules.lean:1073](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1073).

`OAI.KLInvariance.Graded.ModuleData.shift`: [GradedModules.lean:1244](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1244).

`OAI.KLInvariance.Graded.ModuleData.Hom.shift`: [GradedModules.lean:1260](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1260).

`OAI.KLInvariance.Graded.ModuleData.Hom.id`: [GradedModules.lean:1153](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1153).

`OAI.KLInvariance.Graded.ModuleData.Hom.comp`: [GradedModules.lean:1148](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1148).

`OAI.KLInvariance.Graded.shift_isInternal`: [GradedModules.lean:1226](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1226).
