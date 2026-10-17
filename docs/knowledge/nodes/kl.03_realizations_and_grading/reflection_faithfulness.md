---
id: kl.notes.reflection_faithfulness
title: Faithfulness and the rank-one characterization of reflections
kind: theorem
status: proved
primary_topic: kl.03_realizations_and_grading
topics:
- kl.03_realizations_and_grading
uses:
- kl.notes.extended_realization
- kl.realization.reflection_plane
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.extendedAction_injective
  - OAI.KLInvariance.TitsSpace.reflectionFaithful
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1117
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.extendedAction_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1255
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.reflectionFaithful
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; bg:realization
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

# Faithfulness and the rank-one characterization of reflections

The action on the extended real realization is faithful, and
\[
\operatorname{rank}(w-1)=1
\quad\Longleftrightarrow\quad
w\text{ is a reflection}.
\]
Thus the root labels detect exactly the group elements having a codimension-one fixed space.

*Proof.*

The extended action restricts to the ordinary geometric action. The latter is injective by the root-sign and length argument, so an element acting trivially on the extension must already be the identity.

Every reflection is conjugate to a simple reflection. A simple reflection has the formula
\[
v\longmapsto v-\widetilde B(\alpha_i,v)\alpha_i,
\]
and its difference from the identity has one-dimensional image. Conjugation preserves this rank.

For the converse, the nondegenerate form and orthogonality put an orthogonal transformation with rank-one change into reflection normal form. The Coxeter argument then identifies a root direction negated by the element and reduces along its length, showing that the element is a group reflection. This last identification uses the root and descent structure; rank one in an arbitrary representation would not by itself identify a Coxeter reflection.

Together with the two-reflection image calculation, this lets the proof recover root planes from products of actual group reflections.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L34).

## Lean formalization

`OAI.KLInvariance.TitsSpace.extendedAction_injective`: [Tits.lean:1117](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1117).

`OAI.KLInvariance.TitsSpace.reflectionFaithful`: [Tits.lean:1255](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1255).
