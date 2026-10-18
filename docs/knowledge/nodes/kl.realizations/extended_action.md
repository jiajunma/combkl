---
id: kl.realization.extended_action
title: The action on the extended root space
kind: definition
status: formalized
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.realization.geometric_action
- kl.realization.radical_extension
- kl.notes.extended_realization
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.extendedAction
  - OAI.KLInvariance.TitsSpace.extendedAction_simple
  - OAI.KLInvariance.TitsSpace.extendedAction_preserves
  - OAI.KLInvariance.TitsSpace.extendedAction_restrict
  - OAI.KLInvariance.TitsSpace.dominant
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:579
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.extendedAction
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:589
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.extendedAction_simple
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:583
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.extendedAction_preserves
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:599
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.extendedAction_restrict
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:618
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.dominant
  - artifact: openai-kl-paper
    locator: Real realizations; bg:realization
    format: section
    note: Construction and normalization of the realization.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition retain the local source hypotheses and construction?
  verdict: Source statements and construction read directly; dimensions, normalization,
    and orthogonality direction stated explicitly.
tags:
- Kazhdan-Lusztig
- realization
---

# The action on the extended root space

Let \(E=V_0\oplus K^*\) carry the chosen nondegenerate extension \(\widetilde B\) of the Tits form. Write \(\iota(v)=(v,0)\) and \(\widetilde\alpha_i=\iota(\alpha_i)\).

The extended action is the homomorphism \(\rho:W\to\operatorname{GL}(E)\) whose generators act by
\[
\rho(s_i)x=x-\widetilde B(\widetilde\alpha_i,x)\widetilde\alpha_i.
\]
The simple-root pairings are preserved by the extension, so the same reflection-relation theorem constructs this action. Each simple operator, and hence every product, preserves \(\widetilde B\).

## Restriction to the original root space

For \(v\in V_0\),
\[
\begin{aligned}
\rho(s_i)\iota(v)
 &=\iota(v)-\widetilde B(\iota(\alpha_i),\iota(v))\iota(\alpha_i)\\
 &=\iota\bigl(v-B(\alpha_i,v)\alpha_i\bigr)\\
 &=\iota(\rho_0(s_i)v).
\end{aligned}
\]
The identity element satisfies the same compatibility. If it holds for \(w\), then
\[
\rho(s_iw)\iota(v)
=\rho(s_i)\iota(\rho_0(w)v)
=\iota(\rho_0(s_i)\rho_0(w)v).
\]
Induction on a word proves
\[
\rho(w)\iota(v)=\iota(\rho_0(w)v)
\]
for every \(w\). The original roots and all their translates remain in the original embedded space.

## The extra coordinates

For an extension defined by a projection \(p:V_0\to K\), the formula is
\[
\rho(s_i)(v,\phi)
 =\bigl(v-[B(\alpha_i,v)+\phi(p\alpha_i)]\alpha_i,\ \phi\bigr).
\]
The dual coordinate stays fixed, while its value on \(p\alpha_i\) contributes to the first coordinate.

In the infinite dihedral example, choose \(\phi(k)=2\). Since \(p\alpha_s=p\alpha_t=k/2\),
\[
\rho(s)(0,\phi)=(-\alpha_s,\phi),\qquad
\rho(t)(0,\phi)=(-\alpha_t,\phi).
\]
These equations display how the new direction interacts with the original roots.

## A positive functional on the simple roots

For \(v=\sum_i v_i\alpha_i\), set \(\lambda(v,\phi)=\sum_i v_i\). Then \(\lambda(\widetilde\alpha_i)=1\) for every \(i\). The root-sign theorem later turns these positive values into descent tests.

Faithfulness and the rank-one characterization of this action are proved in [[node:kl.notes.reflection_faithfulness]].

## References

[Realizations in the OpenAI notes](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L34).

## Lean formalization

`OAI.KLInvariance.TitsSpace.extendedAction`: [Tits.lean:579](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L579).

`OAI.KLInvariance.TitsSpace.extendedAction_simple`: [Tits.lean:589](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L589).

`OAI.KLInvariance.TitsSpace.extendedAction_preserves`: [Tits.lean:583](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L583).

`OAI.KLInvariance.TitsSpace.extendedAction_restrict`: [Tits.lean:599](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L599).

`OAI.KLInvariance.TitsSpace.dominant`: [Tits.lean:618](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L618).
