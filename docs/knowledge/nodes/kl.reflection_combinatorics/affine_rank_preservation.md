---
id: kl.dihedral.affine_rank_preservation
title: Rank-two preservation forces every relative rank difference
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.relative_rank_fibers
- kl.dihedral.odd_reflection_edges
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.Dihedral.map_cover_length
  - OAI.KLInvariance.Dihedral.map_length_affine
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:504
    format: lean-location
    note: OAI.KLInvariance.Dihedral.map_cover_length
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:536
    format: lean-location
    note: OAI.KLInvariance.Dihedral.map_length_affine
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient/coset domains, intrinsic ranks, injectivity, full-range
    and exact-intermediate hypotheses explicit?
  verdict: Read the exact two hypotheses without assuming injectivity, expanded the
    extension-above and top-boundary extension-below cases, and checked the strong-induction
    predecessor and affine identity.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Rank-two preservation forces every relative rank difference

Let \(D,D'\) be Coxeter systems with two simple generators and lengths \(\ell,\ell'\). Fix \(l\le r\) in \(D\), with \(\ell(l)+2\le\ell(r)\), and a map
\(f:J=[l,r]_D\to D'\).
Assume:

- Every edge \(x\to_Dy\) between vertices of \(J\) maps to an edge \(f(x)\to_{D'}f(y)\).
- Whenever \(x,y\in J\) satisfy \(\ell(y)=\ell(x)+2\), their images satisfy \(\ell'(f(y))=\ell'(f(x))+2\).

Then every consecutive-rank pair satisfies
\[
\ell(y)=\ell(x)+1\quad\Longrightarrow\quad
\ell'(f(y))=\ell'(f(x))+1.
\]
For every \(z\in J\), the lengths obey the affine identity
\[
\ell'(f(z))+\ell(l)=\ell'(f(l))+\ell(z).
\]
In particular, for all \(x,y\in J\), subtracting their two identities gives
\[
\ell'(f(y))-\ell'(f(x))=\ell(y)-\ell(x)
\]
as an equality of integer differences.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit coordinates, affine lengths and full target range.**

**OpenAI notes:** The proposition describes the image directly as a full relative interval in a target plane coset. Its proof recovers covers from rank-two intervals and exhausts each internal target rank with two image vertices. [dih:transport](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L276).

**Lean (primary):** The construction chooses a least target representative and writes F(z) as the ambient image multiplied on the right by its inverse. Rank-two preservation gives consecutive-rank preservation, then an affine length identity by induction. Injectivity and the two-element internal ranks give the exact full range. The theorem returns all coordinate, order, edge and length properties explicitly. [DyerPaths:676](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L676), [DyerPaths:504](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L504), [DyerPaths:536](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L536), [DyerPaths:567](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L567), [DyerPaths:736](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L736).

**Role in the proof:** The Blueprint uses the intrinsic coordinate map F and retains every ambient endpoint bound. The source and target bottom lengths may differ by the constant prescribed by the affine identity.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Consecutive source ranks strictly increase target length

A source length difference of one is positive and odd, hence gives an edge by the [[node:kl.dihedral.odd_reflection_edges|odd-gap edge criterion]]. Edge preservation therefore gives
\(\ell'(f(x))<\ell'(f(y))\)
for every pair of consecutive source ranks.

### Step 2. Extend a consecutive pair above its upper vertex

Suppose \(\ell(y)=\ell(x)+1\) and \(\ell(y)<\ell(r)\).
The [[node:kl.dihedral.relative_rank_fibers|relative-rank fiber theorem]] supplies \(z\in J\) with
\(\ell(z)=\ell(y)+1\).
Step 1 gives
\[
\ell'(f(x))<\ell'(f(y))<\ell'(f(z)).
\]
The gap from \(x\) to \(z\) is two, so the hypothesis gives
\(\ell'(f(z))=\ell'(f(x))+2\).
The only integer strictly between \(A\) and \(A+2\) is \(A+1\). Taking \(A=\ell'(f(x))\) proves the desired gap one.

### Step 3. Extend a consecutive pair below its lower vertex

If \(\ell(y)=\ell(r)\), then \(\ell(x)=\ell(r)-1\).
The overall rank assumption gives
\[
\ell(x)-1=\ell(r)-2\ge\ell(l).
\]
Thus the [[node:kl.dihedral.relative_rank_fibers|rank-existence theorem]] supplies \(z\in J\) with
\(\ell(z)=\ell(x)-1\).

Now
\[
\ell'(f(z))<\ell'(f(x))<\ell'(f(y)),
\qquad
\ell'(f(y))=\ell'(f(z))+2.
\]
The same integer argument forces both gaps to be one. This completes the proof for every consecutive-rank pair.

### Step 4. Induct from the bottom rank

Use strong induction on \(n=\ell(z)\) for vertices \(z\in J\).
At \(z=l\), the affine identity is the same sum on both sides.

For \(z\ne l\), the comparison \(l\le z\) gives \(\ell(l)<\ell(z)\). The [[node:kl.dihedral.relative_rank_fibers|relative-rank fiber theorem]] supplies a vertex \(p\in J\) with
\(\ell(p)=\ell(z)-1\).
Its length is strictly smaller than \(n\), so induction gives
\[
\ell'(f(p))+\ell(l)=\ell'(f(l))+\ell(p).
\]
Steps 2–3 give \(\ell'(f(z))=\ell'(f(p))+1\). Adding one to the induction identity yields
\[
\ell'(f(z))+\ell(l)
=\ell'(f(l))+\ell(p)+1
=\ell'(f(l))+\ell(z).
\]
This proves the affine identity. Subtracting the identities for two vertices proves preservation of their relative length differences.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.map_cover_length`: [DyerPaths.lean:504](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L504).

`OAI.KLInvariance.Dihedral.map_length_affine`: [DyerPaths.lean:536](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L536).
