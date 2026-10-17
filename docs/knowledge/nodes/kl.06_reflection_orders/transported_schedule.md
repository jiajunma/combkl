---
id: kl.detail.transported_schedule
title: Transported reflection schedules and chronological order
kind: definition
status: formalized
primary_topic: kl.06_reflection_orders
topics:
- kl.06_reflection_orders
uses:
- kl.paths.graph_invariance
- kl.notes.reflection_order
lean:
  repository: openai-kl
  modules:
  - EdgeLocalization
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.BruhatGraph.transportedSchedule
  - OAI.KLInvariance.BruhatGraph.chronologicalSchedule
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:40
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.transportedSchedule
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1225
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.chronologicalSchedule
  - artifact: openai-kl-paper
    locator: Related paper context; sec:dihedral
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
- reflection_orders
---

# Transported reflection schedules and chronological order

Let \(\phi:[u,b]\simeq[u',b']\) be an interval order isomorphism. The reconstruction theorem transports each reflection edge \(e:x\to y\) to an edge \(\phi(e)\). Give \(e\) the geometric reflection score of \(\phi(e)\) in the target Coxeter system.

The transported schedule is a list of all source-interval edges, with no repetition, in decreasing score order. Its reversal is the chronological schedule, whose scores are nondecreasing. Edges with equal score may occur in an arbitrary tie order; no invariance claim should depend on a particular such choice.

This distinction between the two lists comes from function composition. In an ordered transfer product, the leftmost operator acts last. The decreasing list therefore describes the outermost-first product, while its reversal describes the order in which edge conditions are removed.

For a suffix \(p\) of the chronological list, the outgoing edges of a vertex that still belong to \(p\) are exactly its remaining kernel conditions. This connects reflection order to the later filtration of stalk modules.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L2).

## Lean formalization



`OAI.KLInvariance.BruhatGraph.transportedSchedule`: [EdgeLocalization.lean:40](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L40).

`OAI.KLInvariance.BruhatGraph.chronologicalSchedule`: [PositiveTransfer.lean:1225](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1225).
