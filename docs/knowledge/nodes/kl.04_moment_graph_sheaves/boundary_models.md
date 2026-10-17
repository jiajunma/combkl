---
id: kl.detail.boundary_models
title: Boundary models supported on principal lower ideals
kind: definition
status: formalized
primary_topic: kl.04_moment_graph_sheaves
topics:
- kl.04_moment_graph_sheaves
uses:
- kl.sheaves.boundary_sheaf
- kl.detail.graded_sheaf
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.BoundaryModels
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:661
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.BoundaryModels
  - artifact: openai-kl-paper
    locator: Related paper context; bg:bmp
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
- moment_graph_sheaves
---

# Boundary models supported on principal lower ideals

A boundary-model family assigns to every vertex \(c\) a graded sheaf \(O_c\) on the whole graph, supported on the principal lower ideal \(\{x:x\leq c\}\). Its data satisfy:

- Every stalk of \(O_c\) is free.
- Every upper edge restriction is the quotient by the prescribed label.
- \(O_c\) is flabby and globally generated.
- Its stalk is zero whenever \(x\not\leq c\).
- The stalk at \(c\) is graded-isomorphic to \(A\), with generator in degree zero.
- Away from \(c\), the full outgoing boundary map is minimal.

One obtains these models by constructing the normalized minimal-boundary sheaf on the lower ideal and extending it by zero. Edges leaving that ideal have zero upper stalk and zero edge quotient, consistent with the quotient rule.

A finite model sum is built from finitely many copies \(O_c(d)\), with nonnegative shifts \(d\). The model-decomposition theorem explains when a given sheaf is isomorphic to such a sum. The shifts are actual homogeneous generator degrees, rather than arbitrary Laurent powers.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization

The fields are `sheaf`, `free`, `quotient`, `generated`, `flabby`, `support`, `top`, `top_graded`, `minimal`. The separate top_graded field records compatibility of the top isomorphism with the grading.

`OAI.KLInvariance.MomentGraph.GradedSheaf.BoundaryModels`: [MinimalExtensions.lean:661](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L661).
