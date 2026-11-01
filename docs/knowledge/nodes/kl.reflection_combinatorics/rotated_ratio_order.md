---
id: kl.order.rotated_ratio_order
title: Rotation of a ratio order through a simple reflection
kind: definition
status: formalized
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.notes.reflection_order
- kl.realization.positive_root_action
- kl.realization.signed_root_action
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.TitsSpace.positiveAction_simplePositive
  - OAI.KLInvariance.TitsSpace.simple_action_nonneg
  - OAI.KLInvariance.TitsSpace.simple_positiveAction_val
  - OAI.KLInvariance.TitsSpace.simple_positiveAction_ne
  - OAI.KLInvariance.TitsSpace.RatioOrder.turnNumerator
  - OAI.KLInvariance.TitsSpace.RatioOrder.turnDenominator
  - OAI.KLInvariance.TitsSpace.RatioOrder.turn_ratio_injective
  - OAI.KLInvariance.TitsSpace.RatioOrder.turn
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1327
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.positiveAction_simplePositive
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1334
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simple_action_nonneg
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1340
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simple_positiveAction_val
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1345
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simple_positiveAction_ne
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1369
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.RatioOrder.turnNumerator
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1372
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.RatioOrder.turnDenominator
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1413
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.RatioOrder.turn_ratio_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1454
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.RatioOrder.turn
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the chamber, positivity, simple-label exclusions, two orders and exact
    induction hypotheses retained?
  verdict: Read simple-root positiveAction facts and the turn construction. Preserved
    generic k!=0 and denominator positivity; proved injectivity by the exact cross
    multiplication and positive-root permutation. Checked the fractional-linear formula
    and A2 values by substitution.
tags:
- Kazhdan-Lusztig
- reflection_orders
---

# Rotation of a ratio order through a simple reflection

Fix a finite-generator Coxeter system \(W\), original real root space \(V_0\), and ratio order \(O=(h,f)\). Choose a simple generator \(s=s_i\), with simple root \(\alpha_i\), and write \(S=\rho(s)\) for its linear action.

For \(k\in\mathbb R\), define the turned numerator and denominator by
\[
f'=f\circ S,\qquad h'_k=(f-kh)\circ S.
\]
These are `turnNumerator` and `turnDenominator`. If
\[
k\ne0,\qquad h'_k(\alpha_j)>0\quad\text{for every simple root }\alpha_j,
\tag{1}
\]
they define the rotated ratio order
\[
O'=\operatorname{turn}(O,i,k)=(h'_k,f').
\]
Its slope is
\[
\sigma_{O'}(a)=\frac{f(Sa)}{f(Sa)-k h(Sa)}.
\tag{2}
\]

## The positive representative under a simple reflection

Write \(s\star a\) for the [[node:kl.realization.positive_root_action|positive-root action]]: it is the positive representative of the root line of \(Sa\). The [[node:kl.realization.signed_root_action|simple-root sign theorem]] says that the only positive root made negative by \(s_i\) is \(\alpha_i\). Consequently
\[
s\star\alpha_i=\alpha_i,\qquad
s\star a=Sa\quad(a\ne\alpha_i).
\]
The map \(s\star-\) is an involution on positive roots. Since it fixes \(\alpha_i\), it carries every other positive root to another root different from \(\alpha_i\).

## Genericity of the new ratio

The positivity condition in (1) makes \(h'_k\) positive on every positive root. Thus every denominator in (2) is nonzero.
For positive roots \(a,b\), put
\[
A_a=f(Sa),\quad B_a=h(Sa),\qquad
A_b=f(Sb),\quad B_b=h(Sb).
\]
The numbers \(B_a,B_b\) are also nonzero: \(Sa\) and \(Sb\) are positive or negative roots, and \(h\) has a strict sign on each of those two alternatives.

If the new slopes agree, cross multiplication gives
\[
A_a(A_b-kB_b)=A_b(A_a-kB_a).
\]
Cancel \(A_aA_b\) and use \(k\ne0\). The result is
\[
A_aB_b=A_bB_a,\qquad
\frac{A_a}{B_a}=\frac{A_b}{B_b}.
\]
Replacing a root by its negative changes both numerator and denominator signs, so these two ratios are \(\sigma_O(s\star a)\) and \(\sigma_O(s\star b)\).
The original slope is injective, and \(s\star-\) is a bijection. Hence \(s\star a=s\star b\), then \(a=b\).

This proves the genericity field `turn_ratio_injective`. Together with (1), it supplies all fields of the new ratio order.

## The fractional-linear slope formula

For \(a\ne\alpha_i\), one has \(S(s\star a)=a\). Put \(u=\sigma_O(a)\). Evaluating (2) at \(s\star a\) gives
\[
\sigma_{O'}(s\star a)
=\frac{f(a)}{f(a)-k h(a)}
=\frac{u}{u-k}.
\tag{3}
\]
The denominator \(u-k\) is positive, because \(h'_k(s\star a)=h(a)(u-k)>0\).
For the simple root, with \(c=\sigma_O(\alpha_i)\), the formula is
\[
\sigma_{O'}(\alpha_i)=\frac{c}{c-k}.
\tag{4}
\]
The [[node:kl.order.rotation_exists|order-rotation theorem]] chooses a negative \(k\) satisfying (1), makes (4) the greatest slope, and uses (3) to preserve the comparisons among all other reflected roots.

## The existing A2 order after rotation

Take simple roots \(a,b\), height denominator \(h\), and numerator \(f(a)=-1\), \(f(b)=3\).
The original slopes of \(a,a+b,b\) are \(-1,1,3\).
Reflect in \(a\), so
\[
Sa=-a,\qquad Sb=a+b,\qquad S(a+b)=b,
\]
and choose \(k=-1/2\). Direct substitution gives
\[
\begin{aligned}
f'(a)&=1,& h'_k(a)&=1/2,\\
f'(b)&=2,& h'_k(b)&=3,\\
f'(a+b)&=3,& h'_k(a+b)&=7/2.
\end{aligned}
\]
Thus
\[
\sigma_{O'}(b)=2/3,\qquad
\sigma_{O'}(a+b)=6/7,\qquad
\sigma_{O'}(a)=2.
\]
The simple root \(a\) moves from least to greatest. The old slope comparison \(\sigma_O(a+b)=1<3=\sigma_O(b)\) becomes \(\sigma_{O'}(b)=2/3<6/7=\sigma_{O'}(a+b)\) after applying the positive-root reflection to both roots. This is an illustrative calculation of the source construction.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**A fractional-linear change of slopes at a simple descent.**

**OpenAI notes:** The background path formula is cited for reflection orders, with the decreasing version obtained by reversing an order. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185).

**Lean (primary):** The adapted proof explicitly constructs a second ratio order: compose the numerator with a simple reflection and compose numerator minus k times denominator with the same reflection. A finite positive-gap choice gives negative k and a positive new denominator. The new chamber is indexed by the shorter element; the chosen simple root becomes greatest and other reflected comparisons are preserved. [DyerPaths:1369](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1369), [DyerPaths:1372](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1372), [DyerPaths:1413](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1413), [DyerPaths:1375](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1375), [DyerPaths:1459](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1459), [DyerPaths:1468](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1468), [DyerPaths:1489](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1489), [DyerPaths:1527](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1527).

**Role in the proof:** The construction retains its generic k!=0 and positivity hypotheses, while the rotation theorem states its negative-parameter conditions. The A2 example computes the old and new slopes through the same formulas.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.positiveAction_simplePositive`: [DyerPaths.lean:1327](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1327).

`OAI.KLInvariance.TitsSpace.simple_action_nonneg`: [DyerPaths.lean:1334](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1334).

`OAI.KLInvariance.TitsSpace.simple_positiveAction_val`: [DyerPaths.lean:1340](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1340).

`OAI.KLInvariance.TitsSpace.simple_positiveAction_ne`: [DyerPaths.lean:1345](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1345).

`OAI.KLInvariance.TitsSpace.RatioOrder.turnNumerator`: [DyerPaths.lean:1369](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1369).

`OAI.KLInvariance.TitsSpace.RatioOrder.turnDenominator`: [DyerPaths.lean:1372](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1372).

`OAI.KLInvariance.TitsSpace.RatioOrder.turn_ratio_injective`: [DyerPaths.lean:1413](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1413).

`OAI.KLInvariance.TitsSpace.RatioOrder.turn`: [DyerPaths.lean:1454](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1454).
