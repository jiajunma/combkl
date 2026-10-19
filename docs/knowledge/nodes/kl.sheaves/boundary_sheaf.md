---
id: kl.sheaves.boundary_sheaf
title: Minimal-boundary sheaves and their normalized stalk
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.graded_sheaf
- kl.sheaves.flabbiness
- kl.detail.upper_quotient
- kl.sheaves.minimal_cover
- kl.sheaves.upward_kernel
- kl.sheaves.boundary_image_identity
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  declarations:
  - OAI.KLInvariance.MomentGraph.BoundarySheaf
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:1138
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.BoundarySheaf
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

# Minimal-boundary sheaves and their normalized stalk

Let \(A=\bigoplus_{n\ge0}A_n\) be a nonnegatively graded commutative algebra over a field. Let \(G\) be an ordered graph with labels \(\alpha_e\in A\), and choose a distinguished vertex \(b\). On a Bruhat interval, \(b\) is its greatest vertex.

Put \(J=A_{>0}\). A minimal-boundary sheaf consists of a graded sheaf \(B\) with six properties:

1. Each stalk \(B^x\) is free over \(A\). The graded module data already include finite generation.
2. Every upper restriction is onto, with
   \[
   \ker\rho^+_e=\alpha_e B^{t(e)}.
   \]
3. Assignments compatible on a set closed under all directed edges extend to global sections agreeing on that set. This is edge flabbiness.
4. Every vector of every stalk is the value of a global section.
5. The distinguished stalk is the rank-one graded unit module:
   \[
   B^b=A,\qquad \deg 1=0.
   \]
6. At each \(x\ne b\), the full outgoing kernel satisfies
   \[
   K_x\subseteq JB^x.
   \]

The last condition is kernel minimality. It says that an element killed by every outgoing restriction becomes zero in the scalar quotient \(B^x/JB^x\).

## Stalks as minimal covers of boundary images

Suppose the graph is finite and the coefficient ring is Noetherian. Global generation and flabbiness identify the image of the outgoing stalk map
\[
r_x:B^x\longrightarrow\prod_{e:\,s(e)=x}B^e
\]
with the boundary image \(B^{\delta x}\) supplied by compatible upper sections.

The map \(B^x\to B^{\delta x}\) is therefore a degree-zero surjection. Its source is finite free, and its kernel is \(K_x\). For \(x\ne b\), condition 6 makes it a minimal graded free cover. This identifies the local construction at each vertex: compute the upper boundary image, then choose its minimal cover.

At the distinguished vertex the graded unit module is prescribed directly. The remaining stalks are controlled by their covers and outgoing restrictions.

## The one-edge construction

Take \(A=\mathbb R[\alpha]\), with one edge \(x\to b\) labelled \(\alpha\). Set
\[
B^b=A,\qquad B^e=A/(\alpha).
\]
The boundary image at \(x\) is \(A/(\alpha)\), whose minimal cover is the quotient map \(A\to A/(\alpha)\). Thus \(B^x=A\), and both restrictions are reduction modulo \(\alpha\).

The sections are the pairs \((f_x,f_b)\) with \(f_x-f_b\in\alpha A\). Diagonal sections \((f,f)\) prove generation at both stalks and extend any prescribed value at \(b\). The outgoing kernel at \(x\) is \(\alpha A\subseteq JA\), verifying minimality. The top stalk is \(A\) in degree zero.

For several outgoing edges, the boundary image records the compatibility equations already imposed above the new vertex. Covering this image preserves those equations throughout the descending construction.

## References

The source declarations below give the constructions and proofs.

## Lean formalization

The field `sheaf` is the underlying graded sheaf. The fields `free`, `quotient`, `flabby`, `generated`, `top`, and `minimal` are the six conditions stated above.

`OAI.KLInvariance.MomentGraph.BoundarySheaf`: [GradedSheaves.lean:1138](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L1138).
