---
id: kl.detail.endpoint_equality
title: R-matrix equality makes the comparison endpoints exact
kind: theorem
status: proved
primary_topic: kl.09_combinatorial_invariance
topics:
- kl.09_combinatorial_invariance
uses:
- kl.detail.schedule_state
- kl.duality.actual_character_reciprocity
- kl.paths.dyer_paths
- kl.detail.transported_schedule
lean:
  repository: openai-kl
  modules:
  - SimultaneousInvariance
  declarations:
  - OAI.KLInvariance.BruhatGraph.actual_endpoint_of_rTilde_eq
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SimultaneousInvariance:278
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.actual_endpoint_of_rTilde_eq
  - artifact: openai-kl-paper
    locator: Related paper context; sec:induction
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- combinatorial_invariance
---

# R-matrix equality makes the comparison endpoints exact

Let \(\phi:[a,b]\simeq[a',b']\), and assume equality of the normalized R-polynomials for every corresponding subinterval:
\[
\widetilde R_{x,z}=\widetilde R'_{\phi(x),\phi(z)}
\qquad(a\leq x\leq z\leq b).
\]
For the actual boundary sheaf restricted to \([a,b]\), the schedule comparison has equal endpoints for every \(0<t<1\).

*Proof.*

At the empty schedule, rewrite the state using scaled stalk characters. At the full schedule, use stalk–costalk reciprocity to rewrite it using the reciprocal scaled character vector.

The transfer product for the transported schedule is the target interval's R-matrix by the decreasing-path formula. Replace every entry by the equal source R-entry. Actual-character reciprocity says that this source R-matrix sends the initial reciprocal vector exactly to the final stalk vector. This proves endpoint equality.

The hypothesis concerns all matrix entries, not just the bottom-to-top one. The simultaneous induction obtains those entries by restricting to subintervals after establishing the new bottom entry. Equality at the single choice \(t=\tfrac12\) already suffices for the subsequent deficit and freeness argument.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization



`OAI.KLInvariance.BruhatGraph.actual_endpoint_of_rTilde_eq`: [SimultaneousInvariance.lean:278](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SimultaneousInvariance.lean#L278).
