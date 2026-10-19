---
id: kl.sheaves.finite_operations
title: Zero sheaves, finite sums, and grading shifts
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.graded_sheaf
- kl.detail.graded_maps_shifts
- kl.algebra.homogeneous_subquotients
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.zero
  - OAI.KLInvariance.MomentGraph.GradedSheaf.prod
  - OAI.KLInvariance.MomentGraph.GradedSheaf.pi
  - OAI.KLInvariance.MomentGraph.GradedSheaf.shift
  - OAI.KLInvariance.MomentGraph.GradedSheaf.shift_forget
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:471
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:477
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.prod
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:483
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.pi
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:465
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.shift
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:498
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.shift_forget
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

# Zero sheaves, finite sums, and grading shifts

Fix an ordered graph and a graded coefficient algebra \(A\). The following constructions act on the vertex modules, edge modules, and restriction maps of graded sheaves.

## The zero sheaf

The zero sheaf has the zero module at every vertex and edge, with the unique zero restriction maps. Its only assignment is zero, which is compatible on every vertex subset. The zero module is finite free of rank zero.

## A finite sum of sheaves

For a finite family \((B_i)_{i\in I}\), define
\[
\left(\bigoplus_{i\in I}B_i\right)^x=\prod_{i\in I}B_i^x,
\qquad
\left(\bigoplus_{i\in I}B_i\right)^e=\prod_{i\in I}B_i^e.
\]
The product equals the direct sum for a finite index set. The restrictions act componentwise:
\[
\rho^\pm_e((v_i)_i)=(\rho^{i,\pm}_e(v_i))_i.
\]
A tuple is homogeneous of degree \(n\) when every component lies in degree \(n\).

For two sheaves this gives \(B\oplus C\), with modules \(B^x\times C^x\) and \(B^e\times C^e\). The source represents these finite sums by its product constructions.

A section of the sum is a tuple of sections. Explicitly, the assignment \(x\mapsto(m_{x,i})_i\) is compatible on \(U\) exactly when each assignment \(x\mapsto m_{x,i}\) is compatible on \(U\). Hence
\[
\Gamma\!\left(\bigoplus_iB_i,U\right)\simeq\prod_i\Gamma(B_i,U),
\]
by exchanging the vertex and summand indices.

## A nonnegative grading shift

For \(d\in\mathbb N\), the shifted sheaf \(B(d)\) has the same underlying modules and maps, with
\[
B(d)^x_n=B^x_{n-d},\qquad B(d)^e_n=B^e_{n-d}.
\]
A degree-\(r\) vector acquires degree \(r+d\). Shifting both endpoints and the edge by the same amount keeps each restriction degree zero. Nonnegative shifts retain the nonnegative grading of the module data.

## A sum on one edge

Let \(A=\mathbb R[\alpha]\), and let \(O_y\) be the congruence sheaf on \(x\to y\), with stalks \(A,A\), edge module \(A/(\alpha)\), and quotient restrictions. Let \(O_x\) have stalk \(A\) at \(x\), zero at \(y\), and zero edge module.

The sum \(C=O_y\oplus O_x(2)\) has
\[
C^x=A\oplus A(2),\qquad C^y=A,\qquad C^e=A/(\alpha).
\]
The lower restriction sends \((f,g)\) to \(f\bmod\alpha\), and the upper restriction sends \(h\) to \(h\bmod\alpha\). Thus a global section is \(((f,g),h)\) with \(f-h\in\alpha A\), while \(g\) is an arbitrary value in the shifted summand.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.zero`: [MinimalExtensions.lean:471](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L471).

`OAI.KLInvariance.MomentGraph.GradedSheaf.prod`: [MinimalExtensions.lean:477](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L477).

`OAI.KLInvariance.MomentGraph.GradedSheaf.pi`: [MinimalExtensions.lean:483](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L483).

`OAI.KLInvariance.MomentGraph.GradedSheaf.shift`: [MinimalExtensions.lean:465](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L465).

`OAI.KLInvariance.MomentGraph.GradedSheaf.shift_forget`: [MinimalExtensions.lean:498](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L498).
