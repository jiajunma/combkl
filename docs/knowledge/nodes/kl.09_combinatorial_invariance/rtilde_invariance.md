---
id: kl.comparison.rtilde_invariance
title: Simultaneous R-tilde invariance and terminal-kernel freeness
kind: theorem
status: proved
primary_topic: kl.09_combinatorial_invariance
topics:
- kl.09_combinatorial_invariance
uses:
- kl.comparison.rtilde_step
- kl.comparison.reverse_freeness
- kl.comparison.global_comparison
- kl.duality.actual_character_reciprocity
- kl.detail.endpoint_equality
- kl.comparison.no_deficit
- kl.foundations.rank_preservation
lean:
  repository: openai-kl
  modules:
  - Invariance
  declarations:
  - OAI.KLInvariance.BruhatGraph.rTilde_invariance_and_freeness
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Invariance:190
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.rTilde_invariance_and_freeness
  - artifact: openai-kl-paper
    locator: 6. Reciprocity and simultaneous induction; sec:induction
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
- induction
---

# Simultaneous R-tilde invariance and terminal-kernel freeness

For an interval isomorphism \(\phi:[u,b]\simeq[u',b']\) in finite-generator real realizations, the following hold simultaneously:

1. \(\widetilde R_{u,b}=\widetilde R'_{u',b'}\).
2. All terminal kernels for the schedule transported by \(\phi\) are free.
3. All terminal kernels for the schedule transported by \(\phi^{-1}\) are free.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different proof route.**

**OpenAI notes:** The simultaneous induction compares normalized KL vectors, obtains P-invariance from the strict half-degree bound, and then recovers bottom terminal-kernel freeness from endpoint equality. [sec:induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194), [eq:comparison](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L298), [eq:reciprocal-vector](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L311).

**Lean (primary):** The simultaneous induction first proves normalized R-invariance together with suffix-kernel freeness in both transported directions. It cancels known bottom R-row entries against one actual source-character vector. Canonical KL equality is proved afterwards in a separate induction using the now common R-matrix and the canonical degree bound. [Invariance:136](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L136), [Invariance:190](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L190), [Invariance:427](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L427).

**How to read this entry:** The detailed proof on this page follows Lean. Its induction inputs, the vector being compared, and the point where endpoint equality becomes available must be read in that order; they are not interchangeable with the preprint’s P-first steps.
<!-- source-comparison:end -->

*Proof.*

### Step 1. State an induction strong enough for every restriction

Fix the two finite-generator systems and their realizations. For each \(n\), prove the following statement simultaneously for every choice of endpoints and every interval isomorphism \(\phi:[a,b]\simeq[a',b']\) with \(d(a,b)=n\):
\[
\widetilde R_{a,b}=\widetilde R'_{a',b'},\qquad
\mathcal F(\phi),\qquad \mathcal F(\phi^{-1}).
\]
Here \(\mathcal F(\phi)\) says that every suffix kernel at every vertex of the restricted source sheaf is free. We induct strongly on \(n\), so all such statements at ranks strictly below \(n\) are available.

Quantifying over both endpoints is essential: the proof needs both \([a,z]\) and \([y,b]\), not only restrictions with a fixed bottom.

### Step 2. Check rank zero and the rank-drop calculation

If \(n=0\), comparability and length monotonicity give \(a=b\). Rank preservation under \(\phi\) gives \(a'=b'\). Both R-polynomials equal \(1\). The interval has no edges, its only schedule is empty, and its only stalk is the free top stalk. Thus both freeness assertions hold.

For \(a\le x\le z\le b\), subtraction of integer lengths gives
\[
d(a,b)-d(x,z)
=(\ell(x)-\ell(a))+(\ell(b)-\ell(z)).
\]
Both summands are nonnegative. If \(x\ne a\) or \(z\ne b\), strict length increase on a proper Bruhat comparison makes at least one positive. Hence every proper comparable subinterval has smaller rank.

### Step 3. Produce the forward and reverse row equalities

For each \(z<b\), restrict \(\phi\) to
\([a,z]\simeq[a',\phi(z)]\).
The restriction preserves order and has inverse given by restricting \(\phi^{-1}\). Step 2 makes its rank smaller, so the polynomial component of the induction hypothesis gives
\(\widetilde R_{a,z}=\widetilde R'_{a',\phi(z)}\).

For \(z'<b'\), do the same with \(\phi^{-1}\) on \([a',z']\). Rank preservation identifies its rank with that of the corresponding source subinterval, so this is again a legitimate smaller instance. It gives the reverse row equality.

### Step 4. Produce upper-interval freeness

For \(y>a\), restrict to
\([y,b]\simeq[\phi(y),b']\).
Step 2 again gives smaller rank. This time take the freeness component of the induction hypothesis. Repeat with \(\phi^{-1}\) for every \(y'>a'\).

The kernel-restriction calculation in [[node:kl.comparison.rtilde_step]] identifies these smaller-interval kernels with the upper kernels required by the current edge comparisons. This uses the same ambient sheaf and the same scores throughout each restriction.

### Step 5. Establish the new polynomial entry

Steps 3–4 supply all four hypotheses of [[node:kl.comparison.rtilde_step]]. It gives the equality
\(\widetilde R_{a,b}=\widetilde R'_{a',b'}\).
At this moment, the new bottom suffix freeness has not been assumed or used.

### Step 6. Obtain equality of every matrix entry

Take arbitrary \(x,z\in[a,b]\). If \(x\not\le z\), both entries are zero. If \(x=a,z=b\), use Step 5. In every other comparable case, Step 2 shows that \([x,z]\) is smaller, and the polynomial component of the induction hypothesis on the restricted isomorphism gives its equality. These cases exhaust all pairs.

### Step 7. Recover the new freeness assertions

All-entry equality from Step 6 gives exact endpoints by [[node:kl.detail.endpoint_equality]]. Upper freeness from Step 4 supplies each local image inclusion. The no-deficit theorem makes every state step exact; Hilbert detection gives equality of embedded edge images; reverse traversal then proves all suffix kernels free by [[node:kl.comparison.reverse_freeness]].

For the reverse direction, use the same all-entry equalities with \(\phi^{-1}\), and use the reverse upper-freeness hypotheses. This proves \(\mathcal F(\phi^{-1})\) as well. All three conclusions at rank \(n\) are established, completing strong induction.

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.rTilde_invariance_and_freeness`: [Invariance.lean:190](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L190).
