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

### Step 1. Fix the order conventions

Write the chronological edge list as \(p=[e_1,\ldots,e_r]\), with \(e_i:x_i\to y_i\). Let \(p_i=[e_{i+1},\ldots,e_r]\), so \(p_0=p\) and \(p_r=[]\). Denote the actual state by \(D_i=D_{p_i}(t)\), and put \(M_i=\tau_{x_i,y_i,T}\), \(T=t^{-1}-t>0\).

The edge-image inclusion hypothesis is supplied for every suffix \(e_i::p_i\). It therefore permits the one-edge estimate at each of the following steps.

### Step 2. Verify the vector inequality for one removal

At \(x_i\), removing \(e_i\) replaces \(F\cup\{e_i\}\) by \(F\), where \(F\) is the set of outgoing edges in \(p_i\). The one-edge estimate reads
\[
(D_i)_{x_i}\le(D_{i-1})_{x_i}+T(D_{i-1})_{y_i}.
\]
Here the upper state can be taken from \(i-1\), because \(x_i\ne y_i\), so removing an edge with source \(x_i\) does not alter the remaining conditions at \(y_i\).

At any \(z\ne x_i\), no outgoing condition changes, so
\((D_i)_z=(D_{i-1})_z=(M_iD_{i-1})_z\).
Thus \(D_i\le M_iD_{i-1}\) in every coordinate.

### Step 3. Induct through the complete list

For \(i=0\), the statement \(D_0\le D_0\) is equality.
Assume
\(D_{i-1}\le M_{i-1}\cdots M_1D_0\).
By transfer monotonicity,
\(M_iD_{i-1}\le M_iM_{i-1}\cdots M_1D_0\).
Combine this with Step 2 to get the induction conclusion
\(D_i\le M_i\cdots M_1D_0\).

At \(i=r\), this is
\[
D_{[]}(t)\le M_r\cdots M_1D_p(t).
\]

### Step 4. Identify the product notation

The dispatch convention lists the outermost operator first. Consequently the product \(M_r\cdots M_1\) is dispatch along \(p^{\mathrm{rev}}\). This proves the displayed theorem, including its list reversal. For an empty list, Step 3 already gives equality with the identity operator.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization



`OAI.KLInvariance.BruhatGraph.scheduleState_le`: [PositiveTransfer.lean:1148](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1148).
