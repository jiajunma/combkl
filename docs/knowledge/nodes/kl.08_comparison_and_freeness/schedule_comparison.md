---
id: kl.detail.schedule_comparison
title: From one-edge bounds to the full transfer inequality
kind: theorem
status: proved
primary_topic: kl.08_comparison_and_freeness
topics:
- kl.08_comparison_and_freeness
uses:
- kl.detail.schedule_state
- kl.comparison.edge_increment
- kl.detail.transfer_properties
- kl.notes.path_product
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.BruhatGraph.scheduleState_le
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1148
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.scheduleState_le
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
- comparison_and_freeness
---

# From one-edge bounds to the full transfer inequality

Suppose every suffix \(e::q\) of a finite edge list \(p\) satisfies the required edge-image inclusion. Put \(T=t^{-1}-t>0\), with \(0<t<1\). Then
\[
D_{\varnothing}(t)\leq
\operatorname{Dispatch}_{p^{\mathrm{rev}}}(T)\,D_p(t)
\]
coordinatewise.

*Proof.*

For a suffix \(e::q\), the one-edge estimate says
\[
D_q\leq\tau_{e,T}D_{e::q}.
\]
Only the source coordinate changes; all others have identical remaining conditions. Starting with the full list, substitute these inequalities successively. Each substitution is valid because elementary transfers preserve the coordinatewise order for \(T\geq0\).

The resulting product appears in reverse list order because the first removed edge acts nearest to the initial vector and the last removed edge acts outermost. Expanding this product produces the ordered-path matrix, so the geometric reflection schedule connects the sheaf filtration to the R-polynomial path formula.

No equality is asserted yet. The discrepancy measures possible edge-image deficits that the endpoint-rigidity argument will later eliminate.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization



`OAI.KLInvariance.BruhatGraph.scheduleState_le`: [PositiveTransfer.lean:1148](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1148).
