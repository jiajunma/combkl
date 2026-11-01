---
id: kl.paths.adapted_path_identification
title: The path polynomial of a chamber order equals the normalized R-polynomial
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.order.rotation_exists
- kl.order.chamber_existence
- kl.paths.path_polynomial_recursion
- kl.paths.bruhat_path_selection
- kl.detail.rtilde_recursion
- kl.foundations.rtilde
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.AdaptedDyer.polynomial_eq_rTilde
  - OAI.KLInvariance.AdaptedDyer.exists_dyer_schedule
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2462
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.polynomial_eq_rTilde
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:2488
    format: lean-location
    note: OAI.KLInvariance.AdaptedDyer.exists_dyer_schedule
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the chamber, positivity, simple-label exclusions, two orders and exact
    induction hypotheses retained?
  verdict: Read polynomial_eq_rTilde and exists_dyer_schedule. Made the strong induction
    quantify over the order and both endpoints, handled both x cases at y=1, checked
    the two smaller O-prime instances and matched the exact Hecke recursion. The statement
    retains Chamber(y).
tags:
- Kazhdan-Lusztig
- reflection_orders
---

# The path polynomial of a chamber order equals the normalized R-polynomial

Fix a finite-generator Coxeter system \(W\).
For every ratio order \(O\) and all \(x,y\in W\), the chamber condition at the upper endpoint implies
\[
O.\mathrm{Chamber}(y)
\quad\Longrightarrow\quad
F_O(x,y;X)=\widetilde R_{x,y}(X),
\]
where the polynomial on the right is the Hecke-defined normalized R-family.

In particular, for every \(y\) there is one ratio order \(O\) in its chamber such that this equality holds for every \(x\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Two orders in the recursion and strong induction on the top length.**

**OpenAI notes:** The normalized R-polynomial is introduced in the path-formula theorem through the weighted sum of increasing reflection paths. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [eq:bg-path-formula](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L191).

**Lean (primary):** The path polynomial and Hecke R-family are defined separately. The geometric rotation gives a recursion with the second order on every smaller polynomial. Strong induction quantifies over the order and both endpoints, applies twice at the shorter upper endpoint and matches the already proved Hecke recursion. The hypothesis of this identification is Chamber(y). [DyerPaths:2402](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2402), [DyerPaths:2462](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2462), [DyerPaths:2488](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2488), [Hecke:491](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L491).

**Role in the proof:** The exact chamber hypothesis, both smaller induction instances, the identity-top cases and the two-order recurrence are stated explicitly. The later geometric-order comparison uses this adapted identification as an input.
<!-- source-comparison:end -->

*Proof.*

### Step 1. The strong induction statement

For each natural number \(n\), prove:
for every ratio order \(O\), every \(x\in W\), and every \(y\in W\) with \(\ell(y)=n\) and \(O.\mathrm{Chamber}(y)\),
\[
F_O(x,y;X)=\widetilde R_{x,y}(X).
\]
The order and both endpoints are quantified in this statement, so the induction hypothesis can be used after rotating the order and changing the endpoints.

### Step 2. The identity upper endpoint

When \(y=1\) and \(x=1\), the diagonal identities give \(F_O(1,1;X)=1=\widetilde R_{1,1}(X)\).

If \(x\ne1\), then \(x\not\le_W1\): a contrary comparison would imply \(\ell(x)\le\ell(1)=0\), hence \(\ell(x)=0\) and \(x=1\).
The [[node:kl.paths.bruhat_path_selection|Bruhat path-selection theorem]] gives \(F_O(x,1;X)=0\), and the normalized R-family vanishes outside Bruhat order, giving the same value. This handles every \(x\) when \(y=1\), in particular the induction base \(n=0\).

### Step 3. Rotation to a strictly shorter upper endpoint

For \(y\ne1\), apply the [[node:kl.order.rotation_exists|order-rotation theorem]] to \(O.\mathrm{Chamber}(y)\). It supplies a simple generator \(s=s_i\) and a ratio order \(O'\) with
\[
\ell(sy)<\ell(y)=n,\qquad O'.\mathrm{Chamber}(sy),
\]
the chosen simple root least for \(O\) and greatest for \(O'\), and the exact comparison of all other reflected roots.
These are precisely the hypotheses of the [[node:kl.paths.path_polynomial_recursion|path-polynomial recursion]].

### Step 4. The two induction substitutions

The new upper endpoint has smaller length. The strong induction hypothesis therefore applies with the new order \(O'\) and each of the two lower endpoints:
\[
F_{O'}(sx,sy;X)=\widetilde R_{sx,sy}(X),
\]
\[
F_{O'}(x,sy;X)=\widetilde R_{x,sy}(X).
\]
Both applications use the same chamber condition \(O'.\mathrm{Chamber}(sy)\).

### Step 5. Agreement of the two recursions

The [[node:kl.paths.path_polynomial_recursion|path-polynomial recursion]] gives
\[
F_O(x,y;X)=
\begin{cases}
F_{O'}(sx,sy;X),&\ell(sx)<\ell(x),\\
F_{O'}(sx,sy;X)+X F_{O'}(x,sy;X),&\ell(x)<\ell(sx).
\end{cases}
\]
Substitute the two identities from Step 4. The result is
\[
\begin{cases}
\widetilde R_{sx,sy}(X),&\ell(sx)<\ell(x),\\
\widetilde R_{sx,sy}(X)+X\widetilde R_{x,sy}(X),&\ell(x)<\ell(sx).
\end{cases}
\]
The [[node:kl.detail.rtilde_recursion|normalized R-recursion]], whose upper-descent hypothesis is \(\ell(sy)<\ell(y)\), identifies this expression with \(\widetilde R_{x,y}(X)\). This proves the induction step and the first assertion for all \(n\).

### Step 6. A single order for every lower endpoint

For a fixed \(y\), the [[node:kl.order.chamber_existence|prescribed-chamber existence theorem]] chooses an order \(O\) in that chamber. Apply the first assertion to this same \(O,y\) and every \(x\).
This gives the stated simultaneous conclusion in \(x\), which is `exists_dyer_schedule`.

The later geometric-order argument compares the fixed decreasing geometric schedule with the negative numerator of such a height-denominator chamber order. This theorem supplies the R-value at that adapted endpoint of the comparison.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.AdaptedDyer.polynomial_eq_rTilde`: [DyerPaths.lean:2462](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2462).

`OAI.KLInvariance.AdaptedDyer.exists_dyer_schedule`: [DyerPaths.lean:2488](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L2488).
