---
id: kl.sheaves.upward_kernel
title: Kernels of upward edge conditions
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.graph_sheaf
- kl.notes.boundary_image
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.upwardKernel
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:599
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.upwardKernel
  - artifact: openai-kl-paper
    locator: Moment-graph background; bg:normalization
    format: section
    note: The source comparison locates the graded sheaf and support-duality context.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- background
---

# Kernels of upward edge conditions

Let \(B\) be a sheaf on an ordered graph, let \(x\) be a vertex, and let
\(U_x=\{e:s(e)=x\}\) be its set of outgoing edges. For \(F\subseteq U_x\), define
\[
K_x(F)=\{v\in B^x:\rho^-_e(v)=0\text{ for every }e\in F\}.
\]
This is the upward kernel for the selected edge conditions. Equivalently,
\[
K_x(F)=\ker\!\left(B^x\longrightarrow\prod_{e\in F}B^e\right)
       =\bigcap_{e\in F}\ker\rho^-_e.
\]
The map into the product sends \(v\) to all its selected lower restrictions. The intersection is a submodule because every restriction is linear.

## Ordering the conditions

With no equations, \(K_x(\varnothing)=B^x\). If \(F\subseteq G\), every vector satisfying all equations in \(G\) satisfies those in \(F\), so
\[
K_x(G)\subseteq K_x(F).
\]
For any two sets,
\[
K_x(F\cup G)=K_x(F)\cap K_x(G),
\]
because satisfying the equations in the union means satisfying both collections.

The full outgoing kernel is \(K_x=K_x(U_x)=\ker r_x\), where \(r_x\) is the stalk map into the boundary module. It is called the costalk in this blueprint. At a top vertex, \(U_x\) is empty and \(K_x=B^x\).

## One edge and one additional condition

For the congruence sheaf over \(A=\mathbb R[\alpha]\) on \(x\to y\),
\[
K_x(\varnothing)=A,\qquad K_x(\{e\})=\alpha A,\qquad K_y=A.
\]
The lower quotient map kills exactly the multiples of \(\alpha\).

More generally, restricting \(\rho^-_e\) to \(K_x(F)\) gives a map with kernel \(K_x(F\cup\{e\})\). Its image is the lower edge image, so
\[
0\longrightarrow K_x(F\cup\{e\})
\longrightarrow K_x(F)
\longrightarrow \rho^-_e(K_x(F))
\longrightarrow0
\]
is exact. The final arrow is onto its stated image by definition; its kernel is precisely the added vanishing equation.

## Gradings and schedules

For a graded sheaf, each restriction preserves degree. If \(v=\sum_n v_n\) satisfies an outgoing equation, then the degree-\(n\) component of that equation is \(\rho^-_e(v_n)=0\). Thus every \(K_x(F)\) is a homogeneous submodule.

A schedule orders the outgoing edges. A suffix kernel takes \(F\) to be the edges remaining after an initial segment has been removed. Successive removals enlarge these submodules; the exact sequence above measures each enlargement by an edge image. The simultaneous induction proves freeness for the suffix kernels used in the comparison.

## References

The source declarations below give the definitions and constructions used here.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.upwardKernel`: [GradedSheaves.lean:599](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L599).
