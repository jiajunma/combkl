---
id: kl.dihedral.relative_rank_fibers
title: Relative rank fibers and two-edge detection of rank two
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.internal_ranks
- kl.coxeter.dihedral_bruhat_order
- kl.dihedral.odd_reflection_edges
- kl.foundations.interval
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.Dihedral.two_interval_elements_length
  - OAI.KLInvariance.Dihedral.exists_interval_length
  - OAI.KLInvariance.Dihedral.two_step_rank_two
  - OAI.KLInvariance.Dihedral.rank_two_of_two_step_bound
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1717
    format: lean-location
    note: OAI.KLInvariance.Dihedral.two_interval_elements_length
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:488
    format: lean-location
    note: OAI.KLInvariance.Dihedral.exists_interval_length
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1673
    format: lean-location
    note: OAI.KLInvariance.Dihedral.two_step_rank_two
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:341
    format: lean-location
    note: OAI.KLInvariance.Dihedral.rank_two_of_two_step_bound
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient/coset domains, intrinsic ranks, injectivity, full-range
    and exact-intermediate hypotheses explicit?
  verdict: Expanded exact relative rank fibers and existence, the gap-two intermediate
    equivalence, and Lean’s three-intermediate contradiction for the converse, including
    parity and strict internal-rank bounds.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Relative rank fibers and two-edge detection of rank two

Let \(D\) be a Coxeter system with two simple generators, intrinsic length \(\ell\), and Bruhat order \(\le\). Fix \(l\le r\) and write \(J=[l,r]_D\).

Every integer \(n\) with \(\ell(l)\le n\le\ell(r)\) occurs as the length of a vertex of \(J\). At each strict internal rank
\[
\ell(l)<n<\ell(r)
\]
there are exactly two vertices. Each endpoint rank contains just its endpoint.

Two-edge paths detect relative rank two in the following precise forms.

If \(\ell(y)=\ell(x)+2\), there are distinct \(a,b\in D\) such that
\[
x\to z\to y\quad\Longleftrightarrow\quad z=a\text{ or }z=b.
\]

Conversely, suppose \(x\to a\to y\), and suppose every \(z\) with \(x\to z\to y\) equals \(a\) or a specified vertex \(b\). Then \(\ell(y)=\ell(x)+2\).

Here a two-edge path uses upward reflection edges; their individual length gaps can be odd integers larger than one.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Exact intermediates and the three-vertex contradiction.**

**OpenAI notes:** The interval-shape lemma counts exactly r two-edge paths when the positive relative length gap r is even. The transport proof uses the equality of ambient intermediate sets to conclude that the target gap is two. [dih:shape](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L112), [dih:relative-paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L148), [dih:transport](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L276).

**Lean (primary):** The native gap-two result lists two intermediates. For the converse, a gap at least four produces two distinct vertices one rank above the bottom and a third three ranks above it. All three are two-edge intermediates, contradicting the assumed two-value bound. Ambient interval membership then permits inverse transport of every target intermediate. [ReflectionSchedules:1717](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1717), [ReflectionSchedules:1673](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1673), [DyerPaths:302](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L302), [DyerPaths:341](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L341), [DyerPaths:634](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L634).

**Role in the proof:** The Blueprint follows the three-intermediate contradiction and proves the ambient and transported intermediate-set equivalences in both directions.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Identify the fibers inside the interval

For a strict internal rank \(n\), one has \(0<n<\ell(r)\). The [[node:kl.dihedral.internal_ranks|internal-rank theorem]] gives exactly two distinct elements of \(D\) of length \(n\).

Every such element \(z\) satisfies
\(\ell(l)<\ell(z)<\ell(r)\).
The [[node:kl.coxeter.dihedral_bruhat_order|dihedral Bruhat comparison theorem]] turns each strict length comparison into a strict Bruhat comparison, so \(l<z<r\). Thus both elements lie in \(J\), and no third vertex can have that length.

At the lower endpoint rank, \(l\le z\) together with \(\ell(l)=\ell(z)\) forces \(z=l\). The analogous argument at the upper endpoint gives \(z=r\). These endpoint vertices and the two internal vertices supply every rank, proving the fiber and existence assertions.

The same reasoning works between any two vertices \(x,y\) of a larger interval: if \(\ell(x)<n<\ell(y)\), the two elements of length \(n\) lie above \(x\) and below \(y\), hence remain in that larger interval. This is the form used by the source's `two_interval_elements_length`.

### Step 2. Describe the two intermediates at gap two

Assume \(\ell(y)=\ell(x)+2\). A path \(x\to z\to y\) gives
\[
\ell(x)<\ell(z)<\ell(y),
\]
so the only possible length is \(\ell(z)=\ell(x)+1\).

Conversely, for every element \(z\) of that length, both differences are one. The [[node:kl.dihedral.odd_reflection_edges|odd-gap edge criterion]] therefore gives both edges. Since
\(0<\ell(x)+1<\ell(y)\), the [[node:kl.dihedral.internal_ranks|internal-rank theorem]] supplies exactly two such elements \(a,b\). This proves the stated equivalence for all \(z\in D\).

### Step 3. Bound the possible total gap in the converse

Suppose \(x\to a\to y\). Each edge has a positive odd length difference, so
\[
d=\ell(y)-\ell(x)
\]
is a positive even integer, with \(d\ge2\). If \(d\ne2\), then \(d\ge4\).

The rank \(\ell(x)+1\) is positive and strictly below \(\ell(y)\), so choose two distinct elements \(p,q\) of that length. The rank \(\ell(x)+3\) is also positive and strictly below \(\ell(y)\), so choose an element \(v\) of that length.

### Step 4. Produce three distinct intermediates when the gap is too large

The gaps from \(x\) to \(p,q\) are one, and their gaps to \(y\) are \(d-1\), a positive odd integer. Thus both \(p,q\) are intermediates of two-edge paths.

The gaps through \(v\) are three and \(d-3\), also positive and odd. Thus \(v\) is a third intermediate. It is distinct from \(p,q\) because its length differs from theirs.

The assumed two-value bound would put the three distinct elements \(p,q,v\) in the set \(\{a,b\}\), which has at most two members. This is impossible. Therefore \(d=2\), proving the converse.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.two_interval_elements_length`: [ReflectionSchedules.lean:1717](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1717).

`OAI.KLInvariance.Dihedral.exists_interval_length`: [DyerPaths.lean:488](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L488).

`OAI.KLInvariance.Dihedral.two_step_rank_two`: [ReflectionSchedules.lean:1673](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1673).

`OAI.KLInvariance.Dihedral.rank_two_of_two_step_bound`: [DyerPaths.lean:341](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L341).
