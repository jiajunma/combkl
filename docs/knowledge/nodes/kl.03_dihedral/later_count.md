---
id: kl.paths.later_count
title: Later-edge counts in transported dihedral intervals
kind: theorem
status: proved
primary_topic: kl.03_dihedral
topics:
- kl.03_dihedral
uses:
- kl.paths.graph_invariance
- kl.foundations.rank_preservation
- kl.notes.relative_dihedral_transport
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.transported_count_difference_all
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:2200
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.transported_count_difference_all
  - artifact: openai-kl-paper
    locator: 3. Dihedral intervals and transported reflection orders; sec:dihedral
    format: section
    note: Chapter organization follows the paper; Lean references identify the precise
      formal statements.
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
- dihedral
---

# Later-edge counts in transported dihedral intervals

Fix a root plane in a real realization, a minimal representative of its dihedral coset, and a relative interval lying in the ambient interval being compared. For an edge \(x\to y\), compare its labels through the target system's reflection order. If \(h_x,h_y\) count the relative upward edges strictly later than this edge at the two endpoints, then
\[
h_x-h_y=\frac{\ell_D(y)-\ell_D(x)-1}{2},
\]
where \(\ell_D\) is the relative dihedral length.

*Proof.*

Use [[node:kl.paths.graph_invariance]] to transport the relative interval to a root plane in the target system while preserving relative rank differences. Express the ambient later-edge indicators as counts in that target interval. The signed-integer dihedral calculation gives the difference of these counts; the coordinate equalities transport it back. The small-rank cases are included separately, removing the intermediate restriction that the relative interval have rank at least two.

## A long edge in type \(A_2\)

Use the reflection order
\[
\alpha_1<\alpha_1+\alpha_2<\alpha_2
\]
in the rank-two system \(S_3\). The edge \(1\to w_0\) is labelled by \(\alpha_1+\alpha_2\). At the identity, exactly one supported upward edge has a later label, namely the edge labelled by \(\alpha_2\). At \(w_0\), there are no upward edges. Hence
\[
h_1-h_{w_0}=1=\frac{3-0-1}{2}.
\]

The quantity is not the length of the edge itself. It measures the excess of later conditions at its lower endpoint. After localization, each such condition contributes one uniformizer, so the count becomes the exponent of the scalar correction in the edge-image comparison.

## References

[3. Dihedral intervals and transported reflection orders](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L2).

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.transported_count_difference_all`: [DihedralIntervals.lean:2200](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2200).
