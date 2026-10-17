---
id: kl.notes.graded_projective_free
title: From graded projectivity to a homogeneous free basis
kind: theorem
status: proved
primary_topic: kl.06_induction
topics:
- kl.06_induction
uses:
- kl.notes.graded_nakayama
- kl.sheaves.minimal_cover
lean:
  repository: openai-kl
  modules:
  - GradedModules
  declarations:
  - OAI.KLInvariance.Graded.exists_homogeneous_basis_polynomial
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:472
    format: lean-location
    note: OAI.KLInvariance.Graded.exists_homogeneous_basis_polynomial
  - artifact: openai-kl-paper
    locator: 6. Reciprocity and simultaneous induction; sec:induction
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the mathematical hypotheses and scope retained from the referenced declarations?
  verdict: The exposition follows the fixed Lean source; worked calculations explain
    the constructions.
tags:
- Kazhdan-Lusztig
- induction
---

# From graded projectivity to a homogeneous free basis

Let \(A=k[x_1,\ldots,x_N]\), with each variable in degree one. A finite projective \(A\)-module equipped with a compatible grading bounded below admits a finite homogeneous basis.

*Proof.*

Shift the lower degree bound to zero. Lift a homogeneous basis modulo the positive-degree ideal to obtain a minimal graded free surjection \(F\to M\). Projectivity supplies a splitting. Taking the degree-zero homogeneous component of a splitting yields a graded splitting, so
\[
F\simeq M\oplus K
\]
as graded modules.

The cover was minimal: reduction modulo the positive-degree ideal is already an isomorphism onto \(M/A_{>0}M\). Consequently \(K/A_{>0}K=0\). The kernel inherits a lower bound on degrees, so graded Nakayama gives \(K=0\). The chosen homogeneous generators are therefore a basis.

This is the final algebraic step in the reverse traversal of edge conditions: the exact-sequence argument first gives projectivity of the new kernel, and its grading supplies freeness.

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.Graded.exists_homogeneous_basis_polynomial`: [GradedModules.lean:472](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L472).
