---
id: kl.comparison.rtilde_row_comparison
title: Extracting the bottom R-tilde row from character comparison
kind: theorem
status: proved
primary_topic: kl.09_combinatorial_invariance
topics:
- kl.09_combinatorial_invariance
uses:
- kl.comparison.global_comparison
- kl.duality.actual_character_reciprocity
lean:
  repository: openai-kl
  modules:
  - SimultaneousInvariance
  declarations:
  - OAI.KLInvariance.BruhatGraph.rTilde_eval_le_of_upper_freeness
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SimultaneousInvariance:444
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.rTilde_eval_le_of_upper_freeness
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

# Extracting the bottom R-tilde row from character comparison

Suppose two intervals are isomorphic and, for every \(z\) strictly below the top,
\[
\widetilde R_{u,z}=\widetilde R'_{u',\phi(z)}.
\]
If all upper kernels needed in the current schedule are free, then
\[
\widetilde R_{u,b}(t^{-1}-t)
\le \widetilde R'_{u',b'}(t^{-1}-t)
\qquad(0<t<1).
\]

*Proof.*

Subtract the source system's exact actual-character reciprocity identity from the bottom coordinate of [[node:kl.comparison.global_comparison]]. Every term below the top cancels by the row hypothesis. The normalized top character is one, leaving precisely the difference of the two displayed R-tilde values.

## Why the two sheaf characters need not be identified

Both matrices in the subtraction act on the same source-system vector \(c(t^{-1})\). The target matrix appears because the schedule was transported from the target reflection order; the exact identity uses the source matrix because it comes from the source sheaf's own reciprocity.

Their bottom-row difference is
\[
\sum_{z\in[u,b]}
\bigl(\widetilde R_{u,z}(T)
-\widetilde R'_{u',\phi(z)}(T)\bigr)c_z(t^{-1}).
\]
All coefficients with \(z\ne b\) vanish by induction. The remaining factor is \(c_b(t^{-1})=1\). Hence the comparison isolates a polynomial entry without asserting equality of source and target characters.

The reverse argument uses the target sheaf's own character vector. This is why the implementation can prove R-tilde invariance before invoking the canonical KL degree bound.

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.rTilde_eval_le_of_upper_freeness`: [SimultaneousInvariance.lean:444](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SimultaneousInvariance.lean#L444).
