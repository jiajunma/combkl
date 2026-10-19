---
id: kl.detail.root_inversions
title: Positive-root inversion sets
kind: definition
status: formalized
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.detail.positive_roots
- kl.realization.signed_root_action
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.RootInversions
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:2039
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.RootInversions
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

# Positive-root inversion sets

For \(w\in W\), its root-inversion set is
\[
\operatorname{Inv}_{\Phi}(w)
=\{a\in\Phi^+:\rho_0(w^{-1})a\text{ is coordinatewise nonpositive}\}.
\]
The inverse in this definition matches left multiplication by the represented reflection.

For the identity, the set is empty: a positive real root is nonzero and cannot also be nonpositive. For a simple reflection \(s_i\), the set is \(\{\alpha_i\}\), because \(s_i\) makes precisely its own positive root negative.

For each positive root \(a\), its root-inversion indicator is one when \(a\) belongs to this set and zero otherwise. The sign-and-count theorem [[node:kl.detail.root_inversion_count]] establishes
\[
a\in\operatorname{Inv}_{\Phi}(w)
\quad\Longleftrightarrow\quad
\ell(r_aw)<\ell(w),
\qquad
|\operatorname{Inv}_{\Phi}(w)|=\ell(w).
\]
It constructs the bijection to left-inversion reflections through the signed action and a reduced word.

The geometric plane weights use the change of these indicators when \(w\) is multiplied by a reflection. Their finite support follows from this inversion-count result.

## References

The local definitions are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.RootInversions`: [Tits.lean:2039](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L2039).
