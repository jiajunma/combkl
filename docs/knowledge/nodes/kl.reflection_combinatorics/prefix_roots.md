---
id: kl.dihedral.prefix_roots
title: Actual plane edge roots and the two prefix sequences
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.detail.plane_basis
- kl.dihedral.induced_system
- kl.dihedral.plane_coset_graph
- kl.dihedral.signed_words
- kl.dihedral.signed_lengths
- kl.dihedral.signed_reflection_action
- kl.realization.plane_reflection_membership
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  - DyerPaths
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot
  - OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_plane
  - OAI.KLInvariance.TitsSpace.PlaneBasis.prefixRoot
  - OAI.KLInvariance.TitsSpace.PlaneBasis.negPrefixRoot
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1094
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1097
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_plane
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:826
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.prefixRoot
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:829
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.negPrefixRoot
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient and intrinsic systems, root signs, signed lengths, finite
    representative bounds and counting domains explicit?
  verdict: Defined edgeRoot in the actual ambient realization, justified plane membership,
    and stated both total prefix definitions including fallback values, witness range,
    positive-root codomain and exact signed labels.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Actual plane edge roots and the two prefix sequences

Fix a finite-generator real Coxeter system \(W\), a root plane \(P\), and a plane basis \(B=(a_L,a_R)\), ordered by the geometric slope \(\sigma\). Its induced dihedral subgroup is \(D\), with simple generators \(s\) and \(t\) represented by \(a_L\) and \(a_R\). Write \(\ell_D\) for intrinsic length and \(w_i\) for the signed word value of an integer \(i\).

## The actual root of an intrinsic edge

For an intrinsic Bruhat edge \(e:x\to_Dy\), the [[node:kl.dihedral.plane_coset_graph|plane-coset graph comparison]], at the identity coset representative, gives an ambient upward edge \(x\to_Wy\). Define
\[
\alpha_e=\operatorname{edgeRoot}_B(e)
\]
to be its unique positive ambient root, representing the left reflection \(yx^{-1}\).

This root lies in \(P\): the element \(yx^{-1}\) belongs to \(D\), and the [[node:kl.realization.plane_reflection_membership|root-plane membership criterion]] identifies reflections in \(D\) with positive roots in \(P\). Thus the slope \(\sigma(\alpha_e)\) is measured using the original ambient root space.

For example, the edges \(1\to_Ds\) and \(1\to_Dt\) have roots \(a_L\) and \(a_R\). Two edges with the same left reflection have the same root, since a reflection has a unique positive representing root.

## The two sequences with a length witness

Choose \(v\in D\), and put \(N=\ell_D(v)\). The [[node:kl.dihedral.signed_lengths|signed-length theorem]] gives upward edges
\[
w_n\longrightarrow_Dw_{n+1},\qquad
w_{-n}\longrightarrow_Dw_{-(n+1)}
\qquad(0\le n<N).
\]
Define total functions on \(n\in\mathbb N\):
\[
\beta_n^+(v)=
\begin{cases}
\alpha_{w_n\to w_{n+1}},&n<N,\\
a_L,&n\ge N,
\end{cases}
\qquad
\beta_n^-(v)=
\begin{cases}
\alpha_{w_{-n}\to w_{-(n+1)}},&n<N,\\
a_R,&n\ge N.
\end{cases}
\]
These are Lean's `prefixRoot` and `negPrefixRoot`. Both functions take values in the positive ambient roots. The superscripts distinguish the positive and negative signed paths.

The witness \(v\) supplies a range on which the alternating words are reduced. On that range the root is determined by the indicated edge, so different sufficiently long witnesses give the same value. Outside the range Lean assigns the endpoint roots to make both functions total.

## Initial labels

The [[node:kl.dihedral.signed_reflection_action|signed reflection-action formula]] gives
\[
w_{n+1}w_n^{-1}=w_{2n+1},\qquad
w_{-(n+1)}w_{-n}^{-1}=w_{-(2n+1)}.
\]
In particular, \(\beta_0^+(v)=a_L\) and \(\beta_0^-(v)=a_R\) whenever \(N>0\). The next positive root represents \(sts=w_3\); the next negative-path root represents \(tst=w_{-3}\), provided \(N>1\).

The [[node:kl.dihedral.prefix_order|prefix-order theorem]] proves that the first sequence increases in slope and the second decreases, on precisely the range \(n<N\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Ambient inversion cuts in place of a root-coordinate recurrence.**

**OpenAI notes:** The notes set \(\kappa=-(a_L,a_R)/2\), where the parentheses denote the ambient Tits form. The midpoint-order lemma writes prefix roots using \(p_0=0\), \(p_1=1\) and \(p_{n+1}=2\kappa p_n-p_{n-1}\). It obtains \(\kappa=\cos(\pi/m)\) in finite type and \(\kappa\ge1\) in infinite type, then compares the resulting coordinate ratios. The functional ratio gives that angular order or its reverse. [dih:midpoint-order](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L358).

**Lean (primary):** PlaneBasis chooses its endpoint roots in increasing geometric slope. Convexity of inversion signs gives a middle-descent test, which orders the two actual ambient prefix-root sequences. A separating element \(w_{k+1}\) compares the two rays. Unbounded lengths give the signed Before order; a maximum length gives the odd residue order modulo 2m. [DyerPaths:923](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L923), [DyerPaths:1106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1106), [DihedralIntervals:832](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L832), [DihedralIntervals:844](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L844), [DihedralIntervals:1101](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1101), [DihedralIntervals:1143](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1143), [DihedralIntervals:1251](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1251).

**Role in the proof:** The ordering conclusion is developed along Lean’s inversion and length proof. The additional classification of \(\kappa\) in the notes is not a conclusion of these Lean angular-order declarations.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot`: [DyerPaths.lean:1094](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1094).

`OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_plane`: [DyerPaths.lean:1097](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1097).

`OAI.KLInvariance.TitsSpace.PlaneBasis.prefixRoot`: [DihedralIntervals.lean:826](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L826).

`OAI.KLInvariance.TitsSpace.PlaneBasis.negPrefixRoot`: [DihedralIntervals.lean:829](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L829).
