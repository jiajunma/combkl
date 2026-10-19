---
id: kl.sheaves.lower_extension
title: Extension by zero from a lower ideal
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.ordered_graph
- kl.detail.graded_sheaf
- kl.sheaves.finite_operations
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.lowerGraph
  - OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend
  - OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtendVertex
  - OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend_support
  - OAI.KLInvariance.MomentGraph.GradedSheaf.liftLowerAssignment
  - OAI.KLInvariance.MomentGraph.GradedSheaf.projectLowerAssignment
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:522
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.lowerGraph
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:535
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:546
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtendVertex
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:560
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend_support
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:569
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.liftLowerAssignment
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:572
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.projectLowerAssignment
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

# Extension by zero from a lower ideal

Let \(K\subseteq V\) be a lower ideal of an ordered vertex set: if \(y\in K\) and \(x\le y\), then \(x\in K\).

The lower graph on \(K\) has vertices \(x\in K\) and edges whose targets lie in \(K\). Their sources also lie in \(K\), since every edge is increasing. Thus these are exactly the edges with both endpoints in the lower ideal.

Let \(B\) be a graded sheaf on this lower graph. Its extension by zero, denoted \(\widetilde B\), has
\[
\widetilde B^x=
\begin{cases}
B^x,&x\in K,\\
0,&x\notin K,
\end{cases}
\qquad
\widetilde B^e=
\begin{cases}
B^e,&t(e)\in K,\\
0,&t(e)\notin K.
\end{cases}
\]

## The restriction maps

If \(t(e)\in K\), both endpoints are in \(K\), and the restrictions are those of \(B\).

If \(t(e)\notin K\), the edge module is zero, and both restrictions are the zero maps into it. This includes edges leaving the lower ideal. An edge entering \(K\) from outside cannot occur, by the lower-ideal property.

For \(x\in K\), evaluation at the inside component gives a canonical degree-preserving identification \(\widetilde B^x\simeq B^x\). Outside \(K\), the stalk is the zero module.

## Assignments and compatible sections

An assignment of \(B\) extends to an assignment of \(\widetilde B\) by giving zero values outside \(K\). Conversely, restrict an assignment of \(\widetilde B\) to the vertices in \(K\).

For \(U\subseteq V\), compatibility on \(U\) is equivalent to compatibility of the restricted assignment on \(U\cap K\) in the lower graph. Edges with targets outside \(K\) have zero edge modules, while the other edge equations are exactly the old equations.

These maps also respect the ambient-assignment convention: assignments in the lower graph have coordinates at every vertex of \(K\), including those outside \(U\cap K\), and the extension fills every vertex outside \(K\) with zero.

## A one-vertex lower ideal

For an edge \(x\to y\), take \(K=\{x\}\) and the normalized sheaf \(A\) on its one-vertex graph. Its extension \(O_x\) has stalk \(A\) at \(x\), zero at \(y\), and zero edge module. Every value at \(x\) is a global section, and the full outgoing kernel at \(x\) is \(A\).

This is the lower-vertex model used in finite sums such as \(O_y\oplus O_x(2)\).

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

Lean represents the inside/outside cases by products indexed by `Witness` of the membership proposition. Inside the ideal this index has one value, and outside it is empty; the corresponding modules identify with the original module and the zero module, respectively.

`OAI.KLInvariance.MomentGraph.lowerGraph`: [MinimalExtensions.lean:522](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L522).

`OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend`: [MinimalExtensions.lean:535](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L535).

`OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtendVertex`: [MinimalExtensions.lean:546](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L546).

`OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend_support`: [MinimalExtensions.lean:560](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L560).

`OAI.KLInvariance.MomentGraph.GradedSheaf.liftLowerAssignment`: [MinimalExtensions.lean:569](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L569).

`OAI.KLInvariance.MomentGraph.GradedSheaf.projectLowerAssignment`: [MinimalExtensions.lean:572](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L572).
