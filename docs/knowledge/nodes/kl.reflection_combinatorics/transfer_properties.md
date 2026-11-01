---
id: kl.detail.transfer_properties
title: Order preservation, injectivity and composition of transfers
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.comparison.positive_transfer
lean:
  repository: openai-kl
  modules:
  - Comparison
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.Comparison.transfer_monotone
  - OAI.KLInvariance.Comparison.transfer_injective
  - OAI.KLInvariance.SchedulePaths.step_monotone
  - OAI.KLInvariance.SchedulePaths.step_injective
  - OAI.KLInvariance.SchedulePaths.dispatch_monotone
  - OAI.KLInvariance.SchedulePaths.dispatch_injective
  - OAI.KLInvariance.SchedulePaths.dispatch_append'
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Comparison:77
    format: lean-location
    note: OAI.KLInvariance.Comparison.transfer_monotone
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Comparison:85
    format: lean-location
    note: OAI.KLInvariance.Comparison.transfer_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:822
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.step_monotone
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:830
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.step_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:843
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.dispatch_monotone
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:849
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.dispatch_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:858
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.dispatch_append'
  - artifact: openai-kl-paper
    locator: Related paper context; sec:induction
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the state, list order, suffix hypotheses, parameter range and exact
    source conclusion stated explicitly?
  verdict: Checked the separate hypotheses for monotonicity and injectivity, arbitrary
    vertex sets and real vectors, nil/cons inductions and the exact concatenation
    order.
tags:
- Kazhdan-Lusztig
- comparison_and_freeness
---

# Order preservation, injectivity and composition of transfers

Let \(V,E\) be sets with source and target maps \(s,t:E\to V\). For a real coefficient \(T\), let \(U_e(T)\) and \(\mathcal D_p(T)\) be the [[node:kl.comparison.positive_transfer|elementary edge transfers]] and their ordered products. For vectors \(v,w:V\to\mathbb R\), write \(v\le w\) when \(v_z\le w_z\) for every \(z\in V\).

The following properties hold.

1. If \(T\ge0\), each \(U_e(T)\), and every finite product \(\mathcal D_p(T)\), preserves this coordinatewise order.
2. If \(s(e)\ne t(e)\), then \(U_e(T)\) is injective for every real \(T\). If every edge occurring in \(p\) has distinct endpoints, then \(\mathcal D_p(T)\) is injective.
3. For any finite lists \(p,q\), their concatenation satisfies
\[
\mathcal D_{p+\!\!+q}(T)v
=\mathcal D_p(T)\bigl(\mathcal D_q(T)v\bigr).
\]
No sign condition is needed for the third identity.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Coordinate operators and ordered products.**

**OpenAI notes:** The notes attach a matrix 1+T E_xy to each edge and apply these matrices in chronological order. Their product is subsequently expanded into decreasing-label paths. [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275), [eq:comparison](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L298).

**Lean (primary):** The operator is defined on functions from the vertex type, over any semiring. Dispatch puts the head edge outside the recursively computed tail, so a chronological list must be reversed. Real monotonicity uses T >= 0; injectivity uses distinct endpoints. Concatenation is an explicit recursive identity. [ReflectionSchedules:1172](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1172), [ReflectionSchedules:1177](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1177), [PositiveTransfer:822](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L822), [PositiveTransfer:830](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L830), [PositiveTransfer:843](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L843), [PositiveTransfer:849](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L849), [PositiveTransfer:858](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L858).

**Role in the proof:** The coordinate calculation explains the matrix action and the list reversal. The two-edge example records the degree-two contribution when an upper-edge transfer precedes the lower-edge transfer.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Order preservation in each coordinate

Assume \(T\ge0\) and \(v\le w\). At a coordinate \(z\ne s(e)\), the output coordinates are \(v_z\) and \(w_z\), so their inequality is one of the assumptions. At \(z=s(e)\),
\[
v_{s(e)}+T v_{t(e)}
\le w_{s(e)}+T w_{t(e)}.
\]
This follows by multiplying \(v_{t(e)}\le w_{t(e)}\) by \(T\ge0\), and adding \(v_{s(e)}\le w_{s(e)}\). It also holds when the source and target coincide. Thus \(U_e(T)v\le U_e(T)w\).

### Step 2. Recovery of the input at distinct endpoints

Suppose \(s(e)\ne t(e)\) and \(U_e(T)v=U_e(T)w\). At the target coordinate, the transfer changes neither input, so \(v_{t(e)}=w_{t(e)}\). At the source coordinate the equality reads
\[
v_{s(e)}+T v_{t(e)}
=w_{s(e)}+T w_{t(e)}.
\]
Substitute the target-coordinate equality and subtract the common summand to get \(v_{s(e)}=w_{s(e)}\). Every other output coordinate equals its input coordinate, giving equality there as well. Hence \(v=w\).

The inverse can be written explicitly:
\[
U_e(-T)\,U_e(T)v=v,\qquad U_e(T)\,U_e(-T)v=v.
\]
Indeed, the target coordinate remains fixed through each composition, and the changes \(+T v_{t(e)}\) and \(-T v_{t(e)}\) cancel at the source.

### Step 3. Monotonicity of an ordered product

For \(p=[]\), the operator is the identity. Suppose the assertion holds for \(p\). If \(v\le w\), first apply the induction hypothesis and then Step 1:
\[
\mathcal D_p(T)v\le\mathcal D_p(T)w
\quad\Longrightarrow\quad
U_e(T)\mathcal D_p(T)v\le U_e(T)\mathcal D_p(T)w.
\]
The two outside expressions are \(\mathcal D_{e::p}(T)v\) and \(\mathcal D_{e::p}(T)w\). This proves the assertion for the longer list. In particular the argument uses the order relation on the input vectors without imposing a sign condition on their individual coordinates.

### Step 4. Injectivity of an ordered product

The empty product is injective. Assume every edge of \(e::p\) has distinct endpoints and
\(\mathcal D_{e::p}(T)v=\mathcal D_{e::p}(T)w\).
By the product recursion, this is equality after applying \(U_e(T)\) to the two tail-product values. Step 2 cancels \(U_e(T)\), leaving
\(\mathcal D_p(T)v=\mathcal D_p(T)w\).
The endpoint condition restricts to every member of \(p\), so the induction hypothesis cancels the tail product and gives \(v=w\).

### Step 5. The concatenation formula

For \(p=[]\), both sides are \(\mathcal D_q(T)v\). For \(p=e::r\), list concatenation gives
\((e::r)+\!\!+q=e::(r+\!\!+q)\).
Using the product recursion and the induction hypothesis,
\[
\begin{aligned}
\mathcal D_{(e::r)+\!\!+q}(T)v
&=U_e(T)\bigl(\mathcal D_{r+\!\!+q}(T)v\bigr)\\
&=U_e(T)\bigl(\mathcal D_r(T)(\mathcal D_q(T)v)\bigr)\\
&=\mathcal D_{e::r}(T)(\mathcal D_q(T)v).
\end{aligned}
\]
The induction covers all finite lists. These three properties supply the order propagation and cancellations used in the [[node:kl.detail.schedule_comparison|full transfer inequality]] and the [[node:kl.comparison.no_deficit|exact-step theorem]].

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Comparison.transfer_monotone`: [Comparison.lean:77](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L77).

`OAI.KLInvariance.Comparison.transfer_injective`: [Comparison.lean:85](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L85).

`OAI.KLInvariance.SchedulePaths.step_monotone`: [PositiveTransfer.lean:822](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L822).

`OAI.KLInvariance.SchedulePaths.step_injective`: [PositiveTransfer.lean:830](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L830).

`OAI.KLInvariance.SchedulePaths.dispatch_monotone`: [PositiveTransfer.lean:843](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L843).

`OAI.KLInvariance.SchedulePaths.dispatch_injective`: [PositiveTransfer.lean:849](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L849).

`OAI.KLInvariance.SchedulePaths.dispatch_append'`: [PositiveTransfer.lean:858](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L858).
