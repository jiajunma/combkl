---
id: kl.detail.schedule_state
title: Remaining conditions and the Hilbert-state vector
kind: definition
status: formalized
primary_topic: kl.invariance
topics:
- kl.invariance
uses:
- kl.detail.transported_schedule
- kl.comparison.normalized_kernel
- kl.sheaves.upward_kernel
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.BruhatGraph.remainingConditions
  - OAI.KLInvariance.BruhatGraph.scheduleState
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1089
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.remainingConditions
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1114
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.scheduleState
  - artifact: openai-kl-paper
    locator: Related paper context; sec:induction
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  definition: accepted
  proof: not_applicable
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

# Remaining conditions and the Hilbert-state vector

Let \(p\) be the list of edges still to be processed. For each vertex \(x\), define
\[
F_p(x)=\{e:s(e)=x,\ e\text{ occurs in }p\}.
\]
The schedule state \(D_p(t)\), for \(0<t<1\), has coordinates
\[
D_p(t)_x=\operatorname{scale}_x(t)\,
H_{K_x(F_p(x))}(t^2),
\]
using the normalized Hilbert state defined earlier.

If \(p\) contains every edge, the coordinate uses the full outgoing kernel. If \(p\) is empty, it uses the entire stalk. Removing the first edge \(e:x\to y\) changes the conditions at \(x\) only. The conditions at \(y\) remain unchanged because \(x\ne y\).

Thus the process starts at costalk data and ends at stalk data. The simultaneous induction must prove freeness for all suffix kernels, not just these two endpoint modules.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Equivalent parameter conventions.**

**OpenAI notes:** The comparison uses \(0<q<1\), scale \(q^{-d/2}(1-q)^N\), and transfer coefficient \(q^{-1/2}-q^{1/2}\). [eq:state](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L243), [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275).

**Lean (primary):** The comparison uses \(0<t<1\) and substitutes \(q=t^2\). Its scale is \(t^{-d}(1-t^2)^N\) and its transfer coefficient is \(t^{-1}-t\). [Dihedral:730](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L730), [PositiveTransfer:591](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L591), [PositiveTransfer:621](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L621).

**Role in the proof:** The substitution \(q=t^2\) identifies the two normalizations. Linear root labels have degree one throughout the calculation.
<!-- source-comparison:end -->

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization



`OAI.KLInvariance.BruhatGraph.remainingConditions`: [PositiveTransfer.lean:1089](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1089).

`OAI.KLInvariance.BruhatGraph.scheduleState`: [PositiveTransfer.lean:1114](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1114).
