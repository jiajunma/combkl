---
id: kl.dihedral.image_plane_coset
title: A dihedral interval graph image lies in one root-plane coset
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.two_step_planes
- kl.dihedral.relative_rank_fibers
- kl.dihedral.odd_reflection_edges
- kl.realization.root_planes
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.TitsSpace.dihedral_image_in_plane
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:400
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.dihedral_image_in_plane
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient/coset domains, intrinsic ranks, injectivity, full-range
    and exact-intermediate hypotheses explicit?
  verdict: Expanded the graph-image construction with its general source/finite-generator
    target hypotheses, injectivity, initial roots, complete strong induction, n-2
    boundary case, exact two-vertex rank and plane/coset propagation.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# A dihedral interval graph image lies in one root-plane coset

Let \(D\) be any Coxeter system with two simple generators, length \(\ell_D\), and \(l\le_Dr\) with
\[
\ell_D(l)+2\le\ell_D(r).
\]
Let \(W\) be a finite-generator real Coxeter system. Suppose
\[
f:J=[l,r]_D\longrightarrow W
\]
is injective and sends every intrinsic upward reflection edge in \(J\) to an ambient upward reflection edge.

Then there are distinct positive ambient roots \(\alpha,\beta\) such that, with
\(P=P(\alpha,\beta)\) and its plane subgroup \(D_P\),
\[
f(z)f(l)^{-1}\in D_P\qquad(z\in J).
\]
Equivalently, the entire image lies in the coset \(D_Pf(l)\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The common-plane argument in the actual ambient realization.**

**OpenAI notes:** The notes identify the root plane of two paths by equality of their two-reflection products. In the transport proof, diamonds propagate the initial plane through all relative ranks. [dih:plane](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L20), [dih:transport](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L276).

**Lean (primary):** The product argument is applied in the nondegenerate extended realization and projected to the original root space. Coset membership propagates along a root in that plane. dihedral_image_in_plane organizes the propagation as strong induction on the absolute source length, selecting one vertex two ranks below and two vertices one rank below. [ReflectionSchedules:1447](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1447), [DyerPaths:283](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L283), [DyerPaths:400](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L400).

**Role in the proof:** The Blueprint states the plane equality, the coset-confinement result and the entire graph-image induction separately, including the first two ranks and the boundary case for the predecessor.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Choose the initial plane from the first internal rank

The [[node:kl.dihedral.relative_rank_fibers|relative-rank fiber theorem]] gives distinct vertices \(a,b\in J\) of length \(\ell_D(l)+1\). The [[node:kl.dihedral.odd_reflection_edges|odd-gap edge criterion]] gives \(l\to_Da\) and \(l\to_Db\). Applying \(f\) gives ambient edges with roots
\[
\alpha=\alpha_{f(l)f(a)},\qquad \beta=\alpha_{f(l)f(b)}.
\]
Injectivity implies \(f(a)\ne f(b)\), so their roots are distinct by the same-source argument of the [[node:kl.dihedral.two_step_planes|two-edge plane theorem]]. Define \(P=P(\alpha,\beta)\).

The bottom satisfies \(f(l)f(l)^{-1}=1\in D_P\). Since \(\alpha,\beta\in P\), propagation along each initial edge also gives
\[
f(a)f(l)^{-1}\in D_P,\qquad f(b)f(l)^{-1}\in D_P.
\]

### Step 2. State the induction and settle its first two ranks

Use strong induction on the absolute intrinsic length \(n=\ell_D(z)\). The induction assertion is that every vertex of \(J\) of length \(n\) has image in \(D_Pf(l)\). Interval membership gives \(n\ge\ell_D(l)\).

A vertex of length \(\ell_D(l)\) is \(l\), because it lies above \(l\). A vertex of length \(\ell_D(l)+1\) is either \(a\) or \(b\): that rank has exactly two vertices and both were selected in Step 1. Their membership has been established.

### Step 3. Select a diamond below a higher vertex

Take \(z\in J\) of length \(n\ge\ell_D(l)+2\). Choose \(p\in J\) of length \(n-2\). When \(n=\ell_D(l)+2\), take \(p=l\); otherwise the rank-existence part of the [[node:kl.dihedral.relative_rank_fibers|relative-rank fiber theorem]] supplies \(p\).

Choose distinct \(q,s\in J\) of length \(n-1\), using the two-vertex rank between \(l\) and \(z\). The four length differences are one, so there are edges
\[
p\to_Dq,\quad p\to_Ds,\quad q\to_Dz,\quad s\to_Dz.
\]
Their images are ambient edges by hypothesis. The three source lengths \(n-2,n-1,n-1\) are strictly smaller than \(n\), so induction puts \(f(p),f(q),f(s)\) in \(D_Pf(l)\).

### Step 4. Propagate the plane and coset membership to the next vertex

The roots of \(f(p)\to f(q)\) and \(f(p)\to f(s)\) lie in \(P\), by coset membership of their endpoints. Since \(q\ne s\) and \(f\) is injective, their target vertices are distinct; their roots are therefore independent and span \(P\).

Apply the [[node:kl.dihedral.two_step_planes|two-edge plane theorem]] to the image diamond. Its four edge roots lie in the plane spanned by these two incoming roots, so the root of \(f(q)\to f(z)\) belongs to \(P\).

The coset-propagation statement, starting from \(f(q)\in D_Pf(l)\), now gives \(f(z)\in D_Pf(l)\). This completes the induction and proves the whole-image assertion.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.dihedral_image_in_plane`: [DyerPaths.lean:400](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L400).
