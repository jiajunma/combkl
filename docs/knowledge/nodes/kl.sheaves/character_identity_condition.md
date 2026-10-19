---
id: kl.duality.character_identity_condition
title: The stalk-character identification condition
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.duality.stalk_character
- kl.foundations.canonical_kl
- kl.sheaves.boundary_sheaf
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.BruhatGraph.StalkCharacterObligation
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:219
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.StalkCharacterObligation
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the complete quantified Prop definition and its chosen boundarySheaf/stalkCharacter
    parameters. Explained polynomial rather than single-evaluation equality, basis
    and boundary-model independence, top normalization and its exact endpoint-substitution
    role.
tags:
- Kazhdan-Lusztig
- graded-duality
---

# The stalk-character identification condition

Fix a finite-generator Coxeter system, \(u\le b\), and a finite real basis of its extended realization. Use the resulting degree-one polynomial coefficient algebra \(A\), and let \(B_{u,b}\) be the chosen normalized boundary sheaf on \([u,b]\).

For \(x\in[u,b]\), its actual stalk character is
\[
C_x^{[u,b]}(q)=\operatorname{ch}(B_{u,b}^x;q)\in\mathbb Z[q].
\]
If a homogeneous free basis of the stalk has degrees \(d_i\), this character is \(\sum_iq^{d_i}\). Let \(P_{x,b}(q)\) denote the canonical KL polynomial defined by the R-recurrence and strict degree normalization.

The **stalk-character identification condition** is the proposition
\[
\forall x\in[u,b],\qquad C_x^{[u,b]}(q)=P_{x,b}(q)
\quad\text{in }\mathbb Z[q].
\]
This is the complete content of the Lean definition StalkCharacterObligation.

## Polynomial equality and basis degrees

The equality says, coefficient by coefficient, that the number of stalk basis generators in degree \(n\) is the coefficient of \(q^n\) in \(P_{x,b}\). Basis independence makes the count independent of the homogeneous basis used to compute it.

The equality is an identity of integer polynomials. Applying a ring homomorphism to the coefficients and evaluating at a parameter preserves it. In particular it gives equality of the scaled actual-stalk character and scaled KL polynomial at a nonzero square parameter.

At the top vertex, both sides equal \(1\): the boundary top is \(A\) with generator degree zero, and the canonical family has diagonal polynomial \(P_{b,b}=1\).

## Independence of the chosen boundary model

Two normalized boundary sheaves on the same interval are graded-isomorphic. Their stalk isomorphisms preserve the generator degrees, so they have the same character. Consequently the condition can be used with any normalized boundary model on \([u,b]\).

The [[node:kl.sheaves.upper_interval_kernels|upper-interval kernel theorem]] also identifies \(C_x^{[u,b]}\) with the character of the original \(B(b)^x\) on \([1,b]\). This is the identification behind the shorter notation \(C_{x,b}\).

## Use in endpoint formulas

The [[node:kl.duality.character_endpoint_substitution|KL endpoint substitution theorem]] takes this equality at a vertex as an explicit hypothesis. It replaces \(C_{x,b}(t^2)\) by \(P_{x,b}(t^2)\) in the empty-condition state, and \(C_{x,b}(t^{-2})\) by \(P_{x,b}(t^{-2})\) in the full-kernel state.

The [[node:kl.duality.actual_character_reciprocity|actual-character reciprocity theorem]] supplies the identity for \(C\) used in the simultaneous comparison proof. The canonical family \(P\) enters the later polynomial-rigidity argument through its own recurrence and degree bound.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate statement.**

**OpenAI notes:** The grading-normalization proposition identifies the stalk graded rank with the canonical KL polynomial and uses the Elias–Williamson character theorem through the cited moment-graph bridges. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The development defines the equality of actual stalk characters and canonical KL polynomials as StalkCharacterObligation. The unconditional theorem used in the main route is R-reciprocity for the actual character. The local strict half-degree implication retains an explicit nonzero-diagonal hypothesis. [SheafMorphisms:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219), [DyerPaths:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L62), [PositiveTransfer:186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L186), [CharacterReciprocity:1807](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1807), [TerminalKernels:1273](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1273), [TerminalKernels:1284](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1284).

**Role in the proof:** The comparison uses the actual character C and its proved R-reciprocity. Canonical P is handled by the later polynomial-rigidity induction. The local degree result applies to a diagonal coefficient satisfying its stated nonvanishing hypothesis.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.StalkCharacterObligation`: [SheafMorphisms.lean:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219).
