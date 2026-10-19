---
id: kl.coxeter.interval_restriction
title: Restricting an order isomorphism to a subinterval
kind: theorem
status: proved
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.foundations.interval
lean:
  repository: openai-kl
  modules:
  - Dihedral
  declarations:
  - OAI.KLInvariance.intervalIso_restrict
  - OAI.KLInvariance.intervalIso_restrict_val
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:19
    format: lean-location
    note: OAI.KLInvariance.intervalIso_restrict
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:58
    format: lean-location
    note: OAI.KLInvariance.intervalIso_restrict_val
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the exact interval, order-map and rank hypotheses retained?
  verdict: Read intervalIso_restrict and its value lemma. Wrote both ambient inclusions,
    endpoint checks, inverse maps and order equivalence, retaining the source scope
    for arbitrary endpoint members.
tags:
- Kazhdan-Lusztig
- Bruhat
- intervals
---

# Restricting an order isomorphism to a subinterval

Let
\[
\phi:[u,b]\xrightarrow{\sim}[u',b']
\]
be an order isomorphism, and let \(x,y\in[u,b]\). Restriction gives an order isomorphism
\[
\phi_{x,y}:[x,y]\xrightarrow{\sim}[\phi(x),\phi(y)].
\]
On underlying elements it is the original map \(\phi\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit order-theoretic prerequisites.**

**OpenAI notes:** The introduction describes Bruhat intervals as finite graded posets. The comparison induction restricts its isomorphism to smaller upper intervals and uses the equal relative ranks to normalize both vectors. [sec:introduction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1), [sec:induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

**Lean (primary):** Subinterval restriction is constructed on the underlying interval elements. A simple-descent induction gives a length-one successor; rank induction shows that a strictly monotone map cannot decrease rank. Applying it to an isomorphism and its inverse proves rank preservation. [Dihedral:19](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L19), [CanonicalKL:297](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L297), [CanonicalKL:367](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L367), [CanonicalKL:415](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L415).

**Role in the proof:** These lemmas justify both the smaller induction instances and the common powers used when transporting interval-indexed vectors.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Include the smaller interval in the original one

For \(z\in[x,y]\), we have \(x\le z\le y\). The ambient memberships of \(x,y\) give
\[
u\le x\le z\le y\le b.
\]
Thus the same group element \(z\) is a member of \([u,b]\). Apply \(\phi\) to that member.

### Step 2. Check the new endpoint inequalities

Monotonicity gives
\[
\phi(x)\le\phi(z)\le\phi(y).
\]
Hence the image belongs to the target subinterval. This defines \(\phi_{x,y}\).

### Step 3. Construct its inverse from the original inverse

For \(z'\in[\phi(x),\phi(y)]\), its endpoint inequalities place it in \([u',b']\). Apply \(\phi^{-1}\). Monotonicity of the inverse gives
\[
x=\phi^{-1}(\phi(x))
\le\phi^{-1}(z')
\le\phi^{-1}(\phi(y))=y.
\]
Thus its inverse image belongs to \([x,y]\).

The two composites return the same underlying element, because \(\phi^{-1}\phi\) and \(\phi\phi^{-1}\) are identities. Equality of interval members is equality of their underlying elements, so these are mutually inverse maps.

### Step 4. Preserve and reflect the smaller order

The order in each subinterval is its ambient order. For \(z,w\in[x,y]\),
\[
\phi_{x,y}(z)\le\phi_{x,y}(w)
\quad\Longleftrightarrow\quad z\le w
\]
by the original order isomorphism. Therefore the restricted bijection is an order isomorphism.

### Step 5. Transport indexed data through the restriction

For a function \(f\) on \([x,y]\), define \(f'(z')=f(\phi_{x,y}^{-1}(z'))\). Then
\(f'(\phi_{x,y}(z))=f(z)\).
This is the substitution used when an induction hypothesis compares data on the two smaller intervals.

The construction applies to any chosen \(x,y\) in the original interval. Their endpoint inequalities characterize the domain and target subintervals, including when those subintervals are empty.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.intervalIso_restrict`: [Dihedral.lean:19](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L19).

`OAI.KLInvariance.intervalIso_restrict_val`: [Dihedral.lean:58](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L58).
