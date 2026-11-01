---
id: kl.paths.path_polynomial_recursion
title: The two-order descent recursion for increasing path polynomials
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.paths.rotated_path_sum
- kl.paths.simple_prefix_split
- kl.paths.extremal_label_paths
- kl.paths.bruhat_path_polynomial
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.AdaptedDyer.polynomial_recursion
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2402
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.polynomial_recursion
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the chamber, positivity, simple-label exclusions, two orders and exact
    induction hypotheses retained?
  verdict: Read polynomial_recursion and both branches. Verified that only the path
    splitting uses the least-label assumption, that both partial sums use the greatest-label
    rotation theorem, and that every smaller polynomial uses O-prime. Checked the
    A2 paths by their left-reflection labels.
tags:
- Kazhdan-Lusztig
- reflection_orders
---

# The two-order descent recursion for increasing path polynomials

Fix a finite-generator Coxeter system \(W\), a simple generator \(s=s_i\), and two ratio orders \(O,O'\).
Assume:

- \(\alpha_i\) is strictly least for \(O\);
- \(\alpha_i\) is strictly greatest for \(O'\);
- for all positive roots \(a,b\ne\alpha_i\),
\[
\sigma_{O'}(s\star a)<\sigma_{O'}(s\star b)
\Longleftrightarrow
\sigma_O(a)<\sigma_O(b).
\]

For all \(x,y\in W\) with \(\ell(sy)<\ell(y)\), the path polynomials satisfy
\[
F_O(x,y;X)=
\begin{cases}
F_{O'}(sx,sy;X),&\ell(sx)<\ell(x),\\
F_{O'}(sx,sy;X)+X F_{O'}(x,sy;X),&\ell(x)<\ell(sx).
\end{cases}
\tag{1}
\]
Both smaller path polynomials use the second order \(O'\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Two orders in the recursion and strong induction on the top length.**

**OpenAI notes:** The normalized R-polynomial is introduced in the path-formula theorem through the weighted sum of increasing reflection paths. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [eq:bg-path-formula](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L191).

**Lean (primary):** The path polynomial and Hecke R-family are defined separately. The geometric rotation gives a recursion with the second order on every smaller polynomial. Strong induction quantifies over the order and both endpoints, applies twice at the shorter upper endpoint and matches the already proved Hecke recursion. The hypothesis of this identification is Chamber(y). [DyerPaths:2402](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2402), [DyerPaths:2462](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2462), [DyerPaths:2488](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2488), [Hecke:491](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L491).

**Role in the proof:** The exact chamber hypothesis, both smaller induction instances, the identity-top cases and the two-order recurrence are stated explicitly. The later geometric-order comparison uses this adapted identification as an input.
<!-- source-comparison:end -->

*Proof.*

### Step 1. The two possible initial length changes

Multiplication by a simple generator changes Coxeter length by exactly one. Thus either \(s\) is a descent at \(x\), or it is an ascent there. These are exactly the two cases in (1).

### Step 2. The initial-descent case

Assume \(\ell(sx)<\ell(x)\).
The label \(\alpha_i\) is least for \(O\), so the [[node:kl.paths.extremal_label_paths|extremal-label theorem]] makes every increasing path from \(x\) to \(y\) avoid it. Consequently
\[
\operatorname{Paths}_O(x,y)=\mathcal N_{O,i}(x,y).
\]
The greatest-label hypothesis for \(O'\), the comparison of the other roots, and the descent at \(y\) are exactly the hypotheses of the [[node:kl.paths.rotated_path_sum|rotated path-sum theorem]]. Apply it to obtain
\[
F_O(x,y;X)
=\sum_{q\in\mathcal N_{O,i}(x,y)}X^{|q|}
=F_{O'}(sx,sy;X).
\]

### Step 3. The initial-ascent case

Assume \(\ell(x)<\ell(sx)\).
The [[node:kl.paths.simple_prefix_split|simple-prefix decomposition]] applies to \(O,i,x,y\), since the chosen label is least. It gives
\[
F_O(x,y;X)=A(x,y)+X A(sx,y),
\]
where \(A(z,y)=\sum_{q\in\mathcal N_{O,i}(z,y)}X^{|q|}\).

Apply the [[node:kl.paths.rotated_path_sum|rotated path-sum theorem]] twice, using the same orders and the same descent at \(y\):
\[
A(x,y)=F_{O'}(sx,sy;X),
\]
\[
A(sx,y)=F_{O'}(s(sx),sy;X)=F_{O'}(x,sy;X).
\]
The last equality uses \(s^2=1\). Substitution gives the second branch of (1).

### Step 4. The common A2 example

Take \(s=s_a\), \(y=w_0=s_as_bs_a\), \(x=1\), and the original and rotated orders with slopes
\[
O:\ a<a+b<b,\qquad O':\ b<a+b<a.
\]
The orders are those calculated in the [[node:kl.order.rotated_ratio_order|rotated ratio-order construction]]; these inequalities denote their slope orders.
Now \(sy=s_bs_a\). The \(O'\)-increasing paths from \(s_a\) to \(s_bs_a\) consist of the single edge labelled \(b\), so their polynomial is \(X\).
From \(1\) to \(s_bs_a\), the increasing path is
\[
1\longrightarrow s_b\longrightarrow s_bs_a,
\]
with labels \(b,a+b\), giving \(X^2\). The other middle vertex gives the decreasing label pair \(a,b\).
Formula (1) therefore yields
\[
F_O(1,w_0;X)=X+X\cdot X^2=X+X^3.
\]
The two original increasing paths are the single edge labelled \(a+b\) and
\[
1\longrightarrow s_a\longrightarrow s_as_b\longrightarrow w_0
\]
with labels \(a,a+b,b\). This calculation exhibits the avoiding and simple-prefix parts of the recurrence.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.AdaptedDyer.polynomial_recursion`: [DyerPaths.lean:2402](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2402).
