---
id: kl.notes.supported_pairings
title: Perfect graded pairings and supported sections
kind: definition
status: formalized
primary_topic: kl.02_background
topics:
- kl.02_background
uses:
- kl.notes.perfect_pairings
- kl.sheaves.graph_sheaf
lean:
  repository: openai-kl
  modules:
  - Support
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.PerfectPairing
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1850
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.PerfectPairing
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; bg:normalization
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the mathematical hypotheses and scope retained from the referenced declarations?
  verdict: The exposition follows the fixed Lean source; worked calculations explain
    the constructions.
tags:
- Kazhdan-Lusztig
- background
---

# Perfect graded pairings and supported sections

Let \(\Gamma(B)\) be the module of global sections of a graded graph sheaf. A perfect pairing of degree \(d\) is a duality
\[
\Gamma(B)\simeq\operatorname{Hom}_A(\Gamma(B),A)
\]
such that pairing a degree-\(i\) section with a degree-\(j\) section gives an element of \(A_{i+j-d}\).

It also satisfies two support conditions. If a section \(m\) is supported only at \(x\) and \(n_x=0\), then \(\langle m,n\rangle=0\). Conversely, if \(m_x=0\) and \(n\) is supported only at \(x\), then \(\langle m,n\rangle=0\).

Both conditions are needed when the pairing is used before symmetry has been transported to every quotient or summand. They allow the pairing to descend between stalk quotients and supported-section modules.

Over the coefficient ring, isolating a single vertex may require multiplication by a product of labels. The construction keeps this scalar in the support-cutting map instead of dividing by it. Balance is then proved integrally by orthogonality and cancellation of a nonzero scalar. The resulting dualities are therefore strong enough to control modules supported in higher codimension.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization

The fields `pairing`, `homogeneous`, `left_orthogonal`, and `right_orthogonal` record the duality, its degree, and the two support conditions.

`OAI.KLInvariance.MomentGraph.GradedSheaf.PerfectPairing`: [Support.lean:1850](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1850).
