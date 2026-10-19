---
id: kl.dihedral.plane_length
title: The ambient inversion count inside a root subspace
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.detail.root_inversions
- kl.detail.root_inversion_count
- kl.realization.root_planes
lean:
  repository: openai-kl
  modules:
  - Decomposition
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.TitsSpace.planeLength
  - OAI.KLInvariance.TitsSpace.planeLength_nonneg
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:705
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.planeLength
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:771
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.planeLength_nonneg
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

# The ambient inversion count inside a root subspace

Let \(P\subseteq V_0\) be a root-space subspace, and let \(w\in W\). Define
\[
L_P(w)=\#\{a\in\Phi^+\cap P:w^{-1}a\text{ is negative}\}.
\]
This is the number of ambient root inversions lying in \(P\).

The ambient inversion set is finite, of cardinality \(\ell_W(w)\). Therefore the count is finite and satisfies
\[
0\le L_P(w)\le\ell_W(w),\qquad L_P(1)=0.
\]
Lean records the count as an integer sum of the finitely supported inversion indicator:
\[
L_P(w)=\sum_{a\in\Phi^+}n_w(a)\,1_{a\in P}.
\]

## Relation to the induced length

When \(P\) is a root plane, this count is used during the construction of the subgroup \(D_P\). Plane-simple reflections change it by one, and conjugation by a suitable plane-simple reflection reduces the count of a nonsimple reflection by two.

After the induced Coxeter system is constructed, the inversion-sign theorem identifies
\[
L_P(w)=\ell_{D_P}(w)\qquad(w\in D_P).
\]
Thus the construction begins with an explicit finite ambient-root count and later proves that it equals the intrinsic Coxeter length.

## A plane in type A3

In the standard \(A_3\) root system, take
\[
a=\alpha_1+\alpha_2,\qquad b=\alpha_3.
\]
The positive roots in \(P(a,b)\) are \(a,b,a+b\). The reflection \(r_a\), corresponding to the permutation \((1\,3)\), has ambient length three. Its ambient positive inversions are
\(\alpha_1,\alpha_2,\alpha_1+\alpha_2\), of which only \(a\) lies in the plane. Hence \(L_P(r_a)=1\).

This is the induced simple-reflection length supplied by the plane's endpoint structure.

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.TitsSpace.planeLength`: [ReflectionSchedules.lean:705](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L705).

`OAI.KLInvariance.TitsSpace.planeLength_nonneg`: [Decomposition.lean:771](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L771).
