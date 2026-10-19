---
id: kl.foundations.rank_preservation
title: Interval isomorphisms preserve endpoints and rank differences
kind: theorem
status: proved
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.foundations.interval
- kl.coxeter.rank_embedding
lean:
  repository: openai-kl
  modules:
  - CanonicalKL
  declarations:
  - OAI.KLInvariance.intervalIso_rankDifference
  - OAI.KLInvariance.intervalIso_bottom
  - OAI.KLInvariance.intervalIso_top
  - OAI.KLInvariance.intervalIso_full_rankDifference
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:415
    format: lean-location
    note: OAI.KLInvariance.intervalIso_rankDifference
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:434
    format: lean-location
    note: OAI.KLInvariance.intervalIso_bottom
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:446
    format: lean-location
    note: OAI.KLInvariance.intervalIso_top
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:458
    format: lean-location
    note: OAI.KLInvariance.intervalIso_full_rankDifference
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the exact interval, order-map and rank hypotheses retained?
  verdict: Read all four interval-isomorphism lemmas. Followed the source proof through
    StrictMono inequalities in both directions, then both endpoint inequalities and
    the full-rank substitution.
tags:
- Kazhdan-Lusztig
- Bruhat
- intervals
---

# Interval isomorphisms preserve endpoints and rank differences

Let \(\phi:[u,b]\xrightarrow{\sim}[u',b']\) be an order isomorphism. For every comparable \(x\le y\) in the source interval,
\[
d(x,y)=d'(\phi(x),\phi(y)).
\]
For nonempty intervals it also satisfies
\[
\phi(u)=u',\qquad \phi(b)=b',\qquad d(u,b)=d'(u',b').
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit order-theoretic prerequisites.**

**OpenAI notes:** The introduction describes Bruhat intervals as finite graded posets. The comparison induction restricts its isomorphism to smaller upper intervals and uses the equal relative ranks to normalize both vectors. [sec:introduction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1), [sec:induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

**Lean (primary):** Subinterval restriction is constructed on the underlying interval elements. A simple-descent induction gives a length-one successor; rank induction shows that a strictly monotone map cannot decrease rank. Applying it to an isomorphism and its inverse proves rank preservation. [Dihedral:19](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L19), [CanonicalKL:297](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L297), [CanonicalKL:367](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L367), [CanonicalKL:415](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L415).

**Role in the proof:** These lemmas justify both the smaller induction instances and the common powers used when transporting interval-indexed vectors.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Apply the rank inequality to the isomorphism

An order isomorphism is strictly monotone. Indeed, \(x<y\) gives \(\phi(x)\le\phi(y)\) by monotonicity, and equality would imply \(x=y\) by injectivity.

The [[node:kl.coxeter.rank_embedding|strict-map rank theorem]] therefore gives
\[
d(x,y)\le d'(\phi(x),\phi(y)).
\]

### Step 2. Apply the same inequality to the inverse

The inverse is also strictly monotone. Apply the theorem to
\(\phi(x)\le\phi(y)\):
\[
d'(\phi(x),\phi(y))
\le d(\phi^{-1}\phi(x),\phi^{-1}\phi(y))
=d(x,y).
\]
The two inequalities prove equality for every comparable pair.

### Step 3. Identify the bottom

Assume both intervals are nonempty. Since \(\phi(u)\) is a target member, \(u'\le\phi(u)\).

The inverse image \(\phi^{-1}(u')\) is a source member, so \(u\le\phi^{-1}(u')\). Apply \(\phi\) to obtain \(\phi(u)\le u'\). Antisymmetry gives \(\phi(u)=u'\).

### Step 4. Identify the top

As a target member, \(\phi(b)\le b'\). The source member \(\phi^{-1}(b')\) satisfies \(\phi^{-1}(b')\le b\). Applying \(\phi\) gives \(b'\le\phi(b)\), hence \(\phi(b)=b'\).

### Step 5. Evaluate the full rank

Apply Step 2 to the source bottom and top, and substitute Steps 3–4:
\[
d(u,b)=d'(\phi(u),\phi(b))=d'(u',b').
\]

Together with subinterval restriction, this supplies the equal induction rank for every pair of corresponding subintervals.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.intervalIso_rankDifference`: [CanonicalKL.lean:415](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L415).

`OAI.KLInvariance.intervalIso_bottom`: [CanonicalKL.lean:434](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L434).

`OAI.KLInvariance.intervalIso_top`: [CanonicalKL.lean:446](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L446).

`OAI.KLInvariance.intervalIso_full_rankDifference`: [CanonicalKL.lean:458](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L458).
