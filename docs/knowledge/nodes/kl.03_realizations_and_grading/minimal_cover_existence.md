---
id: kl.notes.minimal_cover_existence
title: Constructing a minimal graded free cover
kind: theorem
status: proved
primary_topic: kl.03_realizations_and_grading
topics:
- kl.03_realizations_and_grading
uses:
- kl.sheaves.minimal_cover
- kl.notes.graded_nakayama
lean:
  repository: openai-kl
  modules:
  - GradedModules
  declarations:
  - OAI.KLInvariance.Graded.ModuleData.exists_minimalCover
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1182
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.exists_minimalCover
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; bg:bmp
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
- background
---

# Constructing a minimal graded free cover

Assume \(A\) is nonnegatively graded over a field \(k\), and every element of \(A\) is congruent to a scalar modulo \(A_{>0}\). Every finite nonnegatively graded module \(M\) has a minimal graded free cover.

*Proof.*

Consider the finite-dimensional quotient \(M/A_{>0}M\). Choose a homogeneous basis and lift it to homogeneous elements \(m_i\in M\), of degrees \(d_i\). Let \(F\) be the finite free module with a basis element of degree \(d_i\) for each lift, and send that basis element to \(m_i\).

The image and \(A_{>0}M\) together generate \(M\), so graded Nakayama makes the map \(F\to M\) surjective. Modulo \(A_{>0}\), it is the chosen basis isomorphism. Therefore its kernel lies in \(A_{>0}F\), exactly the minimality condition.

The construction records the degrees as well as the number of generators. For example, \(A/(x)\) is covered by a degree-zero copy of \(A\); its kernel \((x)\) is contained in \(A_{>0}A\). In the graph construction the same operation is applied to a boundary image, whose generators encode relations among outgoing edges.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization

`OAI.KLInvariance.Graded.ModuleData.exists_minimalCover`: [GradedModules.lean:1182](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1182).
