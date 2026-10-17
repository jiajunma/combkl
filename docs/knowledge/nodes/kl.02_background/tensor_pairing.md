---
id: kl.notes.tensor_pairing
title: Transporting a perfect pairing through tensor induction
kind: theorem
status: proved
primary_topic: kl.02_background
topics:
- kl.02_background
uses:
- kl.notes.perfect_pairings
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.FrobeniusDuality.inducedModule
  - OAI.KLInvariance.FrobeniusDuality.inducedModule_pairing_tmul
  - OAI.KLInvariance.FrobeniusDuality.inducedPairing_balanced
  - OAI.KLInvariance.FrobeniusDuality.inducedPairing_symmetric
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:270
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedModule
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:276
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedModule_pairing_tmul
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:336
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedPairing_balanced
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:355
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedPairing_symmetric
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; bg:normalization
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

# Transporting a perfect pairing through tensor induction

Let \(R\subseteq A\) be a finite free Frobenius extension with trace \(\operatorname{tr}:A\to R\). If \(N\) is a finite free paired \(A\)-module, tensor induction produces a paired \(A\)-module \(A\otimes_R N\). Its pairing on pure tensors is
\[
\langle a\otimes m,b\otimes n\rangle
=ab\,\operatorname{tr}(\langle m,n\rangle),
\]
with the trace value included back into \(A\).

*Proof.*

First restrict scalars from \(A\) to \(R\), composing the pairing with the trace. Frobenius duality identifies the restricted module with its \(R\)-dual: this is the step that preserves perfectness, not merely bilinearity. Extend scalars back to \(A\); finite freeness makes the extended pairing perfect.

The displayed formula follows on pure tensors. Equality of bilinear maps can be checked on pure tensors, so symmetry follows from symmetry on \(N\). If \(N\) has a balanced right action, let it act on the second tensor factor. On pure tensors, balance reduces to the corresponding identity on \(N\); tensor induction extends the equality to arbitrary sums.

Iterating this construction makes the perfect pairing part of the word object itself. No denominators are introduced at any stage.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization

`OAI.KLInvariance.FrobeniusDuality.inducedModule`: [Frobenius.lean:270](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L270).

`OAI.KLInvariance.FrobeniusDuality.inducedModule_pairing_tmul`: [Frobenius.lean:276](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L276).

`OAI.KLInvariance.FrobeniusDuality.inducedPairing_balanced`: [Frobenius.lean:336](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L336).

`OAI.KLInvariance.FrobeniusDuality.inducedPairing_symmetric`: [Frobenius.lean:355](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L355).
