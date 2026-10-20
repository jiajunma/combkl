---
id: kl.dihedral.full_interval_range
title: An injective rank-preserving dihedral map fills its target interval
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.affine_rank_preservation
- kl.dihedral.relative_rank_fibers
- kl.coxeter.dihedral_bruhat_order
- kl.dihedral.internal_ranks
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.Dihedral.range_eq_interval_of_rank_two
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:567
    format: lean-location
    note: OAI.KLInvariance.Dihedral.range_eq_interval_of_rank_two
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient/coset domains, intrinsic ranks, injectivity, full-range
    and exact-intermediate hypotheses explicit?
  verdict: Verified order reflection via affine ranks and injectivity, both endpoint
    cases, the natural source-rank construction, exact strict bounds and exhaustion
    of the two-element target rank.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# An injective rank-preserving dihedral map fills its target interval

Let \(D,D'\) be two-generator Coxeter systems with lengths \(\ell,\ell'\). Suppose \(l\le_Dr\), \(\ell(l)+2\le\ell(r)\), and
\(f:J=[l,r]_D\to D'\)
is injective, preserves upward reflection edges, and sends every source length gap two to a target length gap two.

Then
\[
f(x)\le_{D'}f(y)\quad\Longleftrightarrow\quad x\le_Dy
\qquad(x,y\in J),
\]
and
\[
\operatorname{range}(f)=[f(l),f(r)]_{D'}.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit coordinates, affine lengths and full target range.**

**OpenAI notes:** The proposition describes the image directly as a full relative interval in a target plane coset. Its proof recovers covers from rank-two intervals and exhausts each internal target rank with two image vertices. [dih:transport](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L276).

**Lean (primary):** The construction chooses a least target representative and writes F(z) as the ambient image multiplied on the right by its inverse. Rank-two preservation gives consecutive-rank preservation, then an affine length identity by induction. Injectivity and the two-element internal ranks give the exact full range. The theorem returns all coordinate, order, edge and length properties explicitly. [DyerPaths:676](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L676), [DyerPaths:504](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L504), [DyerPaths:536](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L536), [DyerPaths:567](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L567), [DyerPaths:736](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L736).

**Role in the proof:** The Blueprint uses the intrinsic coordinate map F and retains every ambient endpoint bound. The source and target bottom lengths may differ by the constant prescribed by the affine identity.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Obtain the affine rank identity

The [[node:kl.dihedral.affine_rank_preservation|affine-rank theorem]] applies to the edge and gap-two hypotheses. Put
\[
L=\ell(l),\quad R=\ell(r),\quad
A=\ell'(f(l)),\quad B=\ell'(f(r)).
\]
For every \(x\in J\), it gives
\[
\ell'(f(x))+L=A+\ell(x),
\qquad B+L=A+R.
\]

### Step 2. Recover order in both directions

In a two-generator Coxeter system, \(p\le q\) means
\(\ell(p)<\ell(q)\) or \(p=q\), by the [[node:kl.coxeter.dihedral_bruhat_order|dihedral Bruhat comparison theorem]].

The identities in Step 1 show that
\[
\ell'(f(x))<\ell'(f(y))
\quad\Longleftrightarrow\quad
\ell(x)<\ell(y).
\]
Equality \(x=y\) gives equality of images, and injectivity gives the converse. Thus both alternatives of the Bruhat criterion agree, proving the order equivalence.

For \(x\in J\), the comparisons \(l\le x\le r\) now give
\(f(l)\le f(x)\le f(r)\).
This proves that the image is contained in the target interval.

### Step 3. Match an interior target rank with a source rank

Take \(z\in[f(l),f(r)]_{D'}\). If \(z=f(l)\) or \(z=f(r)\), the required preimage is an endpoint.

Otherwise strict Bruhat length gives
\[
A<\ell'(z)<B.
\]
Define the natural number
\[
n=L+\bigl(\ell'(z)-A\bigr).
\]
The difference is positive. Using \(B+L=A+R\), the displayed inequalities give
\[
L<n<R.
\]
The [[node:kl.dihedral.relative_rank_fibers|relative-rank fiber theorem]] supplies two distinct vertices \(a,b\in J\) of length \(n\).

### Step 4. Exhaust the target rank

Substituting \(\ell(a)=\ell(b)=n\) into the affine identities gives
\[
\ell'(f(a))=\ell'(z)=\ell'(f(b)).
\]
Injectivity makes \(f(a)\ne f(b)\).

This common target length is positive, because it is greater than \(A\ge0\), and strictly smaller than the length \(B\) of \(f(r)\). The [[node:kl.dihedral.internal_ranks|internal-rank fiber statement]] therefore gives exactly two elements of \(D'\) at this length. They are already \(f(a),f(b)\), so \(z\) equals one of them.

Every target interval vertex is consequently in the image. Together with Step 2, this proves the full range equality.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.range_eq_interval_of_rank_two`: [DyerPaths.lean:567](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L567).
