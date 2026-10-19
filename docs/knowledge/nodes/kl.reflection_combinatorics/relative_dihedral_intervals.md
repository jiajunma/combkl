---
id: kl.notes.relative_dihedral_intervals
title: Relative length and Bruhat intervals in a plane-subgroup coset
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.induced_system
- kl.dihedral.plane_coset_graph
- kl.foundations.interval
lean:
  repository: openai-kl
  modules:
  - Decomposition
  - ReflectionOrders
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.system
  - OAI.KLInvariance.TitsSpace.planeCoset_exists_minimal
  - OAI.KLInvariance.TitsSpace.PlaneBasis.intervalToAmbient
  - OAI.KLInvariance.TitsSpace.PlaneBasis.coset_length_eq
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:906
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.system
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:2166
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.planeCoset_exists_minimal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionOrders:410
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.intervalToAmbient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1196
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.coset_length_eq
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
- dihedral
---

# Relative length and Bruhat intervals in a plane-subgroup coset

Let \(P\) be a root plane and let \(D_P\) carry its induced dihedral Coxeter system. For a coset \(D_Pa\), let \(a_0\) be its unique element of least ambient length.

Every coset element has a unique expression \(wa_0\), \(w\in D_P\). Define its relative length and order by
\[
\ell_{\mathrm{rel}}(wa_0)=\ell_P(w),
\]
\[
ga_0\le_{\mathrm{rel}}ha_0
\quad\Longleftrightarrow\quad g\le_P h.
\]
Thus the relative order is the induced Coxeter order transported through the coset bijection.

## Relative intervals

For \(g\le_P h\), the corresponding relative interval is
\[
[ga_0,ha_0]_{\mathrm{rel}}
=\{za_0:g\le_P z\le_P h\}.
\]
Its rank difference is \(\ell_P(h)-\ell_P(g)\).

The [[node:kl.dihedral.plane_coset_graph|coset graph theorem]] identifies its directed reflection edges with the ambient reflection edges between the same coset vertices. Relative paths use these edges while staying in the coset, so they are ambient Bruhat paths. The map from the relative interval into the ambient interval is an order-preserving injection.

The relative length also has the ambient-root description
\[
\ell_{\mathrm{rel}}(wa_0)
=\#\{r\in\Phi^+\cap P:(wa_0)^{-1}r\text{ is negative}\}.
\]

## A relative edge with ambient length difference three

In type \(A_3\), take
\(a=\alpha_1+\alpha_2\), \(b=\alpha_3\), and \(P=P(a,b)\).
The induced simple reflection \(r_a=(1\,3)\) has relative length one and ambient length three.

Thus the relative interval from \(1\) to \(r_a\) has two vertices. In the ambient group,
\[
r_a=s_1s_2s_1,
\]
so the subword criterion gives
\(1<s_1<r_a\).
The element \(s_1=(1\,2)\) is outside \(D_P=\langle(1\,3),(3\,4)\rangle\), whose elements fix \(2\).

This example shows the roles of the two ranks explicitly: the relative interval has one reflection step, while the ambient interval contains intermediate vertices outside the plane-subgroup coset.

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.system`: [Decomposition.lean:906](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L906).

`OAI.KLInvariance.TitsSpace.planeCoset_exists_minimal`: [Tits.lean:2166](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L2166).

`OAI.KLInvariance.TitsSpace.PlaneBasis.intervalToAmbient`: [ReflectionOrders.lean:410](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionOrders.lean#L410).

`OAI.KLInvariance.TitsSpace.PlaneBasis.coset_length_eq`: [Decomposition.lean:1196](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1196).
