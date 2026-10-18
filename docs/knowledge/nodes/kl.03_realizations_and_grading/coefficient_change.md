---
id: kl.detail.coefficient_change
title: Transport of coefficients along an algebra isomorphism
kind: definition
status: formalized
primary_topic: kl.03_realizations_and_grading
topics:
- kl.03_realizations_and_grading
uses:
- kl.sheaves.graded_module
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  declarations:
  - OAI.KLInvariance.CoefficientChange
  - OAI.KLInvariance.CoefficientChange.equiv
  - OAI.KLInvariance.CoefficientChange.kEquiv
  - OAI.KLInvariance.Graded.ModuleData.change
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1777
    format: lean-location
    note: OAI.KLInvariance.CoefficientChange
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1805
    format: lean-location
    note: OAI.KLInvariance.CoefficientChange.equiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1815
    format: lean-location
    note: OAI.KLInvariance.CoefficientChange.kEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1873
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.change
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# Transport of coefficients along an algebra isomorphism

Let \(e:A\xrightarrow{\sim}B\) be an isomorphism of \(k\)-algebras and let \(M\) be an \(A\)-module. Its transported \(B\)-module has the same additive group, with action
\[
b\cdot_B m=e^{-1}(b)\cdot_A m.
\]
The identification of underlying elements is \(e\)-semilinear: the old vector \(am\) corresponds to \(e(a)m\) in the new scalar action. It is \(k\)-linear because \(e\) fixes the base-field scalars. In particular, it preserves dimensions over \(k\).

For compatible gradings on \(A\) and \(B\), assume that \(e\) preserves every homogeneous component in both directions. Transport \(M_n\) by the underlying \(k\)-linear identification to define the degree-\(n\) piece over \(B\). Direct-sum decomposition, nonnegative support, and finite generation are retained.

This construction passes from the symmetric algebra of the extended realization to a polynomial ring after a basis is chosen. It changes the description of the coefficient algebra. General base change instead replaces a module by a tensor product and does not require an algebra isomorphism.

## References

The precise Lean sources are listed below.

## Lean formalization

The wrapper field `val` stores the underlying element. The new scalar action is defined through the inverse algebra equivalence.

`OAI.KLInvariance.CoefficientChange`: [BottSamelson.lean:1777](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1777).

`OAI.KLInvariance.CoefficientChange.equiv`: [BottSamelson.lean:1805](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1805).

`OAI.KLInvariance.CoefficientChange.kEquiv`: [BottSamelson.lean:1815](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1815).

`OAI.KLInvariance.Graded.ModuleData.change`: [BottSamelson.lean:1873](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1873).
