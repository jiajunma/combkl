---
id: kl.comparison.rtilde_step
title: The R-tilde induction step from smaller intervals
kind: theorem
status: proved
primary_topic: kl.09_combinatorial_invariance
topics:
- kl.09_combinatorial_invariance
uses:
- kl.comparison.rtilde_row_comparison
- kl.comparison.free_suffixes
- kl.foundations.rank_preservation
lean:
  repository: openai-kl
  modules:
  - Invariance
  declarations:
  - OAI.KLInvariance.BruhatGraph.rTilde_eq_of_smaller_data
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Invariance:95
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.rTilde_eq_of_smaller_data
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

# The R-tilde induction step from smaller intervals

Consider isomorphic intervals in two finite-generator Coxeter systems. Suppose the shorter bottom-row R-tilde entries agree in both directions, and every strictly higher upper interval already has terminal-kernel freeness. Then
\[
\widetilde R_{u,b}=\widetilde R'_{u',b'}.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different proof route.**

**OpenAI notes:** The simultaneous induction compares normalized KL vectors, obtains P-invariance from the strict half-degree bound, and then recovers bottom terminal-kernel freeness from endpoint equality. [sec:induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194), [eq:comparison](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L298), [eq:reciprocal-vector](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L311).

**Lean (primary):** The simultaneous induction first proves normalized R-invariance together with suffix-kernel freeness in both transported directions. It cancels known bottom R-row entries against one actual source-character vector. Canonical KL equality is proved afterwards in a separate induction using the now common R-matrix and the canonical degree bound. [Invariance:136](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L136), [Invariance:190](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L190), [Invariance:427](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L427).

**How to read this entry:** The detailed proof on this page follows Lean. Its induction inputs, the vector being compared, and the point where endpoint equality becomes available must be read in that order; they are not interchangeable with the preprint’s P-first steps.
<!-- source-comparison:end -->

*Proof.*

### Step 1. List the four induction inputs

For \(\phi:[a,b]\simeq[a',b']\), the hypotheses provide:
the row equalities on \([a,z]\) for \(z<b\);
the reverse row equalities on \([a',z']\) for \(z'<b'\);
terminal-kernel freeness on each \([y,b]\) with \(y>a\);
and the corresponding freeness on each \([y',b']\) with \(y'>a'\).

The latter two statements refer to restrictions of the same ambient sheaves and the same transported reflection scores. They do not assert new freeness at the current bottom.

### Step 2. Match an upper kernel to a smaller interval

Consider a suffix \(e::q\) of the chronological schedule, with \(e:x\to y\). Since \(a\le x<y\), we have \(y>a\). Thus the upper-interval freeness hypothesis is available on \([y,b]\).

We must check that it concerns the kernel needed at this step. The edges from \(y\) remaining in \(q\) are exactly those with score strictly larger than the score of \(e\). Indeed, the schedule is sorted, and an outgoing edge at \(y\) cannot have the same reflection label as the incoming edge \(e\): that reflection would send \(y\) back to \(x\), not upward. Distinct labels have distinct geometric scores.

Restriction to \([y,b]\) retains all outgoing edges at \(y\) and their scores. Cutting that restricted sorted list at the score of \(e\) produces a suffix with exactly the same outgoing conditions. The stalk, restriction maps, and ambient sheaf are unchanged under this upper restriction. Its free suffix kernel is therefore the required upper kernel in the original interval.

### Step 3. Obtain inequalities in both directions

Fix \(0<t<1\). Apply [[node:kl.comparison.rtilde_row_comparison]] using the forward row data and the kernels from Step 2:
\[
\widetilde R_{a,b}(t^{-1}-t)\le
\widetilde R'_{a',b'}(t^{-1}-t).
\]
Repeat with \(\phi^{-1}\), the reverse row data, and the reverse upper-freeness data. This gives the opposite inequality at the same real parameter. Hence the two evaluations are equal for every \(0<t<1\).

### Step 4. Pass from evaluations to polynomials

The map \(T(t)=t^{-1}-t\) is injective on \((0,1)\). For \(0<s<t<1\),
\[
T(s)-T(t)=\frac1s-\frac1t+t-s
=(t-s)\left(\frac1{st}+1\right)>0.
\]
Its image is therefore infinite. The difference of the two R-polynomials, regarded over \(\mathbb R\), vanishes on that infinite image. A nonzero polynomial of degree \(m\) has at most \(m\) roots, so the difference is zero. The coefficient map \(\mathbb Z\to\mathbb R\) is injective, hence equality holds already in \(\mathbb Z[a]\).

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.rTilde_eq_of_smaller_data`: [Invariance.lean:95](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L95).
