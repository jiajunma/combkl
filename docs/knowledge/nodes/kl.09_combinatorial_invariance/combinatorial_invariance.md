---
id: kl.main.combinatorial_invariance
title: Combinatorial invariance of Kazhdan–Lusztig polynomials
kind: theorem
status: proved
primary_topic: kl.09_combinatorial_invariance
topics:
- kl.09_combinatorial_invariance
uses:
- kl.main.kl_finite
- kl.main.finite_model_transport
lean:
  repository: openai-kl
  modules:
  - Invariance
  declarations:
  - OAI.KLInvariance.combinatorial_invariance
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Invariance:547
    format: lean-location
    note: OAI.KLInvariance.combinatorial_invariance
  - artifact: openai-kl-paper
    locator: 1. Introduction and conventions; sec:introduction
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- introduction
---

# Combinatorial invariance of Kazhdan–Lusztig polynomials

Let \((W,S)\) and \((W',S')\) be arbitrary Coxeter systems, with \(u\le b\) and \(u'\le b'\). If
\[
\phi:[u,b]\simeq[u',b']
\]
is an isomorphism of abstract partially ordered sets, then the ordinary equal-parameter Kazhdan–Lusztig polynomials satisfy
\[
P^W_{u,b}(q)=P^{W'}_{u',b'}(q).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different proof route.**

**OpenAI notes:** The simultaneous induction compares normalized KL vectors, obtains P-invariance from the strict half-degree bound, and then recovers bottom terminal-kernel freeness from endpoint equality. [sec:induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194), [eq:comparison](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L298), [eq:reciprocal-vector](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L311).

**Lean (primary):** The simultaneous induction first proves normalized R-invariance together with suffix-kernel freeness in both transported directions. It cancels known bottom R-row entries against one actual source-character vector. Canonical KL equality is proved afterwards in a separate induction using the now common R-matrix and the canonical degree bound. [Invariance:136](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L136), [Invariance:190](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L190), [Invariance:427](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L427).

**How to read this entry:** The detailed proof on this page follows Lean. Its induction inputs, the vector being compared, and the point where endpoint equality becomes available must be read in that order; they are not interchangeable with the preprint’s P-first steps.
<!-- source-comparison:end -->

*Proof.*

### Step 1. State exactly what is given

We have arbitrary Coxeter systems \(W,W'\), comparable endpoints \(u\le b\), \(u'\le b'\), and an order isomorphism
\(\phi:[u,b]_W\simeq[u',b']_{W'}\).
Neither generating set is assumed finite, and no realization or basis is part of the hypothesis.

### Step 2. Replace each interval by a finite-generator model

Apply [[node:kl.main.finite_model_transport]] to obtain models \(W_J,W'_{J'}\), lifted endpoints \(\bar u,\bar b,\bar u',\bar b'\), and order isomorphisms
\[
j:[\bar u,\bar b]_{W_J}\simeq[u,b]_W,\qquad
j':[\bar u',\bar b']_{W'_{J'}}\simeq[u',b']_{W'}.
\]
The same result gives the two polynomial identities
\[
P^{W_J}_{\bar u,\bar b}=P^W_{u,b},
\qquad
P^{W'_{J'}}_{\bar u',\bar b'}=P^{W'}_{u',b'}.
\]

### Step 3. Form the comparison between the models

Compose the maps in the order
\[
\psi=(j')^{-1}\circ\phi\circ j.
\]
For a model vertex \(x\), first \(j(x)\) lies in the source ambient interval, then \(\phi(j(x))\) lies in the target ambient interval, and finally \((j')^{-1}\) returns a target model vertex. Each factor is an order isomorphism, so \(\psi\) is an order isomorphism between the two model intervals.

### Step 4. Apply the finite-generator theorem with internal choices

The sets \(J,J'\) are finite. Their extended real realizations are therefore finite-dimensional and admit bases. Choose such bases solely to invoke [[node:kl.main.kl_finite]]. The theorem gives
\[
P^{W_J}_{\bar u,\bar b}=P^{W'_{J'}}_{\bar u',\bar b'}.
\]
Its conclusion is an equality of the canonical polynomials; it contains neither chosen basis.

### Step 5. Write the final equality chain

Substitute the transport equalities from Step 2:
\[
P^W_{u,b}
=P^{W_J}_{\bar u,\bar b}
=P^{W'_{J'}}_{\bar u',\bar b'}
=P^{W'}_{u',b'}.
\]
The first and last equalities are parabolic transport, and the middle equality is finite-generator invariance. This proves the original assertion for the arbitrary systems in Step 1.

## References

[1. Introduction and conventions](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization

`OAI.KLInvariance.combinatorial_invariance`: [Invariance.lean:547](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L547).
