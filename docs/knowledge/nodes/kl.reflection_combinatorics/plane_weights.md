---
id: kl.geometry.plane_weights
title: Root partners and geometric plane weights
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.detail.positive_roots
- kl.detail.root_inversions
- kl.notes.reflection_order
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the source root-sign and finiteness hypotheses retained?
  verdict: The definitions apply to any x and positive alpha in finite generator rank;
    the theorem states the noninversion hypothesis used in the sign argument.
tags:
- Kazhdan-Lusztig
- root-geometry
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.TitsSpace.partner
  - OAI.KLInvariance.TitsSpace.goodPairRoot
  - OAI.KLInvariance.TitsSpace.extraRoot
  - OAI.KLInvariance.TitsSpace.halfRoot
  - OAI.KLInvariance.TitsSpace.planeDefect
  - OAI.KLInvariance.TitsSpace.planeWeight
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:376
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.partner
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:460
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.goodPairRoot
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:525
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.extraRoot
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:536
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.halfRoot
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:340
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.planeDefect
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:592
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.planeWeight
---

# Root partners and geometric plane weights

Let \((W,S)\) have finitely many simple generators, let \(\Phi^+\) be its positive roots, and fix \(x\in W\), \(\alpha\in\Phi^+\). Let \(r_\alpha\) be the reflection represented by \(\alpha\).

For \(\beta\in\Phi^+\), define the inversion indicator
\[
n_x(\beta)=
\begin{cases}1,&x^{-1}\beta\text{ is negative},\\0,&x^{-1}\beta\text{ is positive}.\end{cases}
\]
It has finite support, of size \(\ell(x)\).

## The partner of a positive root

The partner \(\beta^*\) is the positive root representing the line of \(r_\alpha\beta\):
\[
\beta^*=
\begin{cases}
r_\alpha\beta,&r_\alpha\beta\text{ is positive},\\
-r_\alpha\beta,&r_\alpha\beta\text{ is negative}.
\end{cases}
\]
Since \(r_\alpha^2=1\), taking partners twice returns \(\beta\). Also \(\alpha^*=\alpha\). The reflection formula shows
\[
\operatorname{span}\{\alpha,\beta^*\}
=\operatorname{span}\{\alpha,\beta\}.
\]
Thus the partner operation preserves the root plane containing \(\alpha\).

Call \(\beta\) flipped when \(r_\alpha\beta\) is negative. In that case
\[
\beta+\beta^*=B(\alpha,\beta)\alpha.
\]
Both roots on the left are positive, so applying the positive height functional shows \(B(\alpha,\beta)>0\).

## The contributing pairs and their representatives

A contributing root satisfies all three conditions
\[
r_\alpha\beta\text{ is negative},\qquad
n_x(\beta)=0,\qquad n_x(\beta^*)=0.
\]
For plane counting, also require \(\beta\ne\alpha\). The resulting set is closed under taking partners.

Choose the fixed injective geometric slope \(s\) on \(\Phi^+\). A half-root is a contributing root different from \(\alpha\) satisfying
\[
s(\beta)<s(\beta^*).
\]
The slope chooses exactly one member of each two-element contributing pair. The plane-weight theorem proves the needed absence of a fixed partner among these roots.

Only finitely many contributing roots occur. Indeed, for \(y=r_\alpha x\) and a flipped root,
\[
n_y(\beta)=1-n_x(\beta^*).
\]
Every contributing root therefore belongs to the finite inversion set of \(y\).

## Grouping by planes

For a root plane \(P\), define
\[
k_P(x,\alpha)=
\#\{\beta:\beta\text{ is a half-root and }
\operatorname{span}\{\alpha,\beta\}=P\}.
\]
These are nonnegative integers, and only finitely many are nonzero. They are the geometric plane weights.

The plane defect records all changes of inversion indicators except the distinguished root:
\[
D_P(x,y;\alpha)=
\sum_{\substack{\beta\in\Phi^+,\ \beta\ne\alpha\\
\operatorname{span}\{\alpha,\beta\}=P}}
\bigl(n_y(\beta)-n_x(\beta)\bigr).
\]
This sum is finite because both inversion sets are finite.

When \(\alpha\) is an ascent root for \(x\), the weight-sum theorem proves \(D_P=2k_P\) for each plane. Summing gives the length change after the distinguished root's contribution has been removed.

## References

The local root-sign and plane-weight calculations are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.partner`: [ReflectionSchedules.lean:376](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L376).

`OAI.KLInvariance.TitsSpace.goodPairRoot`: [ReflectionSchedules.lean:460](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L460).

`OAI.KLInvariance.TitsSpace.extraRoot`: [ReflectionSchedules.lean:525](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L525).

`OAI.KLInvariance.TitsSpace.halfRoot`: [ReflectionSchedules.lean:536](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L536).

`OAI.KLInvariance.TitsSpace.planeDefect`: [ReflectionSchedules.lean:340](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L340).

`OAI.KLInvariance.TitsSpace.planeWeight`: [ReflectionSchedules.lean:592](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L592).
