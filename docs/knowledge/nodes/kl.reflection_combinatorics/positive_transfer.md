---
id: kl.comparison.positive_transfer
title: Elementary edge transfers and ordered products
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses: []
lean:
  repository: openai-kl
  modules:
  - Comparison
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.Comparison.transfer
  - OAI.KLInvariance.Comparison.idealState
  - OAI.KLInvariance.SchedulePaths.step
  - OAI.KLInvariance.SchedulePaths.dispatch
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Comparison:74
    format: lean-location
    note: OAI.KLInvariance.Comparison.transfer
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Comparison:98
    format: lean-location
    note: OAI.KLInvariance.Comparison.idealState
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1172
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.step
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1177
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.dispatch
  - artifact: openai-kl-paper
    locator: 6. Reciprocity and simultaneous induction; sec:induction
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the state, list order, suffix hypotheses, parameter range and exact
    source conclusion stated explicitly?
  verdict: Read the semiring-valued step/dispatch definitions and the real transfer/idealState
    interface. Stated sources and targets, column action, recursive product order,
    chronological reversal and both two-edge computations.
tags:
- Kazhdan-Lusztig
- induction
---

# Elementary edge transfers and ordered products

Let \(V\) be a set of vertices, \(E\) a set of directed edges, and \(s,t:E\to V\) their source and target maps. A vector over a semiring \(R\) is a function \(v:V\to R\); its coordinate at \(z\) is \(v_z\). The semiring can, for example, be \(\mathbb R\) or a polynomial ring. Fix a coefficient \(T\in R\).

## One elementary transfer

For \(e\in E\), define
\[
(U_e(T)v)_z=
\begin{cases}
v_z+T v_{t(e)},&z=s(e),\\
v_z,&z\ne s(e).
\end{cases}
\]
This is `SchedulePaths.step`. It adds a multiple of the upper coordinate to the lower coordinate. The two summands use the input vector. If \(s(e)\ne t(e)\), the target coordinate stays unchanged.

With a finite vertex set and column-vector notation, define \(E_{xy}\) by
\[
(E_{xy}v)_z=\begin{cases}v_y,&z=x,\\0,&z\ne x.\end{cases}
\]
Then \(U_e(T)=1+T E_{s(e),t(e)}\), where \(1\) is the identity operator. For real scalars, `Comparison.transfer T x y` gives the same formula with the two endpoints supplied directly. The [[node:kl.detail.transfer_properties|transfer properties]] prove monotonicity for \(T\ge0\) and injectivity when the endpoints are distinct.

## The product associated with a list

Write \(\mathcal D_p(T)v\) for `SchedulePaths.dispatch`. Its recursion is
\[
\mathcal D_{[]}(T)v=v,\qquad
\mathcal D_{e::p}(T)v=U_e(T)\bigl(\mathcal D_p(T)v\bigr).
\]
Here \(e::p\) means the list with first entry \(e\) and tail \(p\). Thus
\[
\mathcal D_{[e_1,e_2,e_3]}(T)v
=U_{e_1}(T)\bigl(U_{e_2}(T)(U_{e_3}(T)v)\bigr).
\]
The first edge in this list supplies the outermost operator.

A chronological list \(p=[e_1,\ldots,e_r]\) processes \(e_1\) first and \(e_r\) last. Its composite is consequently
\[
U_{e_r}(T)\cdots U_{e_1}(T)
=\mathcal D_{p^{\mathrm{rev}}}(T),
\]
where \(p^{\mathrm{rev}}=[e_r,\ldots,e_1]\). Reversal converts chronological order to the source's product convention.

The alternative `Comparison.idealState` uses an edge sequence \((x_j,y_j)\), an initial vector \(v\), and a natural-number index:
\[
E_0=v,\qquad E_{j+1}=\tau_{x_j,y_j,T}E_j.
\]
For the first \(r\) edges of a chronological list, this gives \(E_r=\mathcal D_{p^{\mathrm{rev}}}(T)v\).

## A two-edge calculation

Take distinct vertices \(x,y,z\), edges \(e:x\to y\), \(f:y\to z\), and a vector with coordinates \((a,b,c)\).
Processing \(f\) and then \(e\) gives
\[
(a,b,c)\xmapsto{U_f}(a,b+Tc,c)
\xmapsto{U_e}(a+Tb+T^2c,b+Tc,c).
\]
The chronological list is \([f,e]\), and the resulting operator is \(\mathcal D_{[e,f]}=U_eU_f\). The term \(T^2c\) reaches \(x\) through the path \(x\to y\to z\).

Processing \(e\) first gives
\[
(a,b,c)\xmapsto{U_e}(a+Tb,b,c)
\xmapsto{U_f}(a+Tb,b+Tc,c).
\]
For the illustrative values \(T=2\), \((a,b,c)=(1,2,3)\), the two final vectors are \((17,8,3)\) and \((5,8,3)\), respectively. The first calculation explains how the later path expansion records the order in which contributions reach a coordinate.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Coordinate operators and ordered products.**

**OpenAI notes:** The notes attach a matrix 1+T E_xy to each edge and apply these matrices in chronological order. Their product is subsequently expanded into decreasing-label paths. [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275), [eq:comparison](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L298).

**Lean (primary):** The operator is defined on functions from the vertex type, over any semiring. Dispatch puts the head edge outside the recursively computed tail, so a chronological list must be reversed. Real monotonicity uses T >= 0; injectivity uses distinct endpoints. Concatenation is an explicit recursive identity. [ReflectionSchedules:1172](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1172), [ReflectionSchedules:1177](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1177), [PositiveTransfer:822](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L822), [PositiveTransfer:830](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L830), [PositiveTransfer:843](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L843), [PositiveTransfer:849](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L849), [PositiveTransfer:858](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L858).

**Role in the proof:** The coordinate calculation explains the matrix action and the list reversal. The two-edge example records the degree-two contribution when an upper-edge transfer precedes the lower-edge transfer.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Comparison.transfer`: [Comparison.lean:74](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L74).

`OAI.KLInvariance.Comparison.idealState`: [Comparison.lean:98](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L98).

`OAI.KLInvariance.SchedulePaths.step`: [ReflectionSchedules.lean:1172](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1172).

`OAI.KLInvariance.SchedulePaths.dispatch`: [ReflectionSchedules.lean:1177](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1177).
