---
id: kl.paths.dyer_paths
title: The decreasing-path formula for a geometric reflection order
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.foundations.rtilde
- kl.foundations.bruhat_step
- kl.notes.reflection_order
- kl.notes.path_product
lean:
  repository: openai-kl
  modules:
  - ReflectionOrders
  declarations:
  - OAI.KLInvariance.WallDyer.geometric_entry_eq_rTilde
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionOrders:1229
    format: lean-location
    note: OAI.KLInvariance.WallDyer.geometric_entry_eq_rTilde
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- background
---

# The decreasing-path formula for a geometric reflection order

Fix a finite lower Bruhat region and the constructed geometric reflection order. The \(x,y\) entry of the ordered edge-transfer product is
\[
\widetilde R_{x,y}(T).
\]
Expanding the product assigns \(T\) to each edge, so a composable decreasing reflection path contributes \(T\) raised to its length.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same polynomial, different construction order.**

**OpenAI notes:** The path-formula theorem introduces the normalized R-polynomial through increasing reflection paths and relates it to the ordinary R-polynomial; decreasing paths follow by reversing the reflection order. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [eq:bg-path-formula](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L191).

**Lean (primary):** The normalized R-family is defined first as a coefficient of the Hecke bar transform. Its recursion is proved algebraically, and the geometric path product is later proved equal to that independently constructed family. [Hecke:482](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L482), [Hecke:491](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L491), [ReflectionOrders:1229](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionOrders.lean#L1229).

**Role in the proof:** The bar construction supplies the R-family and its recursion. The path theorem then identifies that family with the ordered path polynomial.

**Different stated generality.**

**OpenAI notes:** The cited Dyer theorem is stated for a reflection order in general; the subsequent comparison chooses geometric reflection orders. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185).

**Lean (primary):** The referenced formal entry theorem establishes the required path formula for the constructed geometric functional on a finite lower region of a finite-generator system. Generic pencils and complete root-plane blocks provide its order-independence argument. [ReflectionSchedules:126](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L126), [ReflectionOrders:1229](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionOrders.lean#L1229).

**Role in the proof:** The geometric-order hypotheses specify the path theorem used here. The generic-functional construction orders all positive roots; the transfer calculation takes place on the finite region in the theorem.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Identify matrix entries with ordered path polynomials

On the finite lower region below \(b\), expand the transfer product using [[node:kl.notes.path_product]]. Its \((x,y)\)-entry is the sum of \(T^{|p|}\) over directed paths whose edges occur in the schedule order. Equal root labels cannot be consecutive in a directed path, so the ordering is strict along every contributing path.

### Step 2. Prove the formula for an order adapted to y

Choose a geometric ratio order whose numerator lies in the chamber adapted to \(y\). If \(y\ne1\), its chamber-rotation construction chooses a simple descent \(s\) and a second ratio order for \(sy\). In the original order the simple root is least; in the rotated order it is greatest. Reflection by \(s\) identifies the orderings of all other roots.

Split increasing paths according to whether they use that least simple edge. If \(sx<x\), such an edge cannot start a directed path from \(x\), and reflection transports all paths to paths from \(sx\) to \(sy\). If \(sx>x\), paths omitting the simple edge transport to paths from \(sx\) to \(sy\); paths using it must use it first and transport, after removing it, to paths from \(x\) to \(sy\). Removing that first edge removes one factor of \(T\).

Thus the path polynomials obey exactly
\[
F_{x,y}=\begin{cases}
F_{sx,sy},&sx<x,\\
F_{sx,sy}+TF_{x,sy},&sx>x.
\end{cases}
\]
The empty path gives \(F_{x,x}=1\), and there are no paths outside Bruhat order. Induction on \(\ell(y)\), using the rotated order at each step, identifies this adapted path polynomial with the Hecke-defined \(\widetilde R_{x,y}\).

### Step 3. Verify invariance of a complete root-plane block

A finite relative dihedral interval has an involution fixing its endpoints and swapping the two vertices in each internal rank. It preserves relative lengths and hence the odd-gap edge criterion. Map each edge through this involution.

For a two-edge path with indices \(i,j,k\), we have \(|i|<|j|<|k|\), and its labels are \(i+j\), \(j+k\). Their signs are the signs of \(j\), \(k\), respectively. In the signed angular order, \(i+j\prec j+k\) holds exactly when \(j>0\): if both labels are positive, their ordinary difference is \(k-i>0\); if the first is positive and the second negative, it is also earlier. If \(j<0\), a negative first label follows a positive second label, and when both are negative their ordinary difference is negative, so the comparison reverses. Swapping the middle-rank vertex replaces \(j\) by \(-j\), reversing this comparison. The conclusion also holds if the entire induced angular order is reversed. Consequently the involution sends a decreasing path between the endpoints to an increasing one of the same number of edges. Applying it twice restores the path. This is a weight-preserving bijection, so the entry of a complete plane block is unchanged by reversing its angular order.

Every path using only labels in that plane stays in one plane-subgroup coset and lifts to its relative interval. Thus the same equality holds for the full plane block inside the ambient lower region. If no such path joins the selected endpoints, both entries are zero.

### Step 4. Move between generic functionals without changing the entry

Choose a common transverse functional \(g\) for the given functional \(f\) and an adapted one \(h\), as follows. For three normalized roots \(a,b,c\) with \(c\) outside the plane of \(a,b\), put
\[
v_f=f(a-b)(c-b)-f(c-b)(a-b).
\]
The two difference vectors are independent and \(f(a-b)\ne0\), so \(v_f\ne0\). Require \(g(v_f)\ne0\), impose the analogous conditions for \(h\), and also require \(g(a-b)\ne0\) for distinct normalized roots. There are only countably many nonzero vectors to avoid; the polynomial-family argument in the generic-functional proof chooses such a \(g\).

If a pencil \((1-t)f+tg\) ties \(a,b,c\), eliminating \(t\) from the two equalities would give \(g(v_f)=0\). Thus no root outside the plane can join a tie of \(a,b\). Conversely, the normalized roots in that plane lie on the affine line through \(a,b\), so every one ties when \(a,b\) do. This proves the complete-plane-block condition. Along the linear pencils from \(f\) to \(g\) and from \(h\) to \(g\), a tie involving distinct roots is, by the transverse choice, a complete actual root-plane block.

Near any pencil parameter, the strict comparisons between different tied blocks remain fixed: only finitely many edges occur in the lower region, so finitely many strict inequalities need to be preserved. Inside each block, a linear functional orders the normalized roots either angularly or in reverse angular order. Step 3 identifies these two products. A block with only one reflection label consists of noninteracting edges, whose transfers commute.

Hence every block product, and therefore the whole entry, is locally constant along the pencil, including at crossing parameters. A locally constant function on the connected real parameter interval is constant. Comparing both pencils identifies the entry for \(f\) with that for \(h\).

### Step 5. Fix the sign and apply the constructed functional

The adapted calculation in Step 2 counts increasing labels. Negating its numerator makes the decreasing schedule count exactly those paths. Step 4 permits replacing that negative numerator by the fixed geometric functional used for the full matrix. The constructed functional separates all positive-root slopes, so it satisfies the required genericity hypothesis. Its entry is therefore \(\widetilde R_{x,y}(T)\).

The Lean result used here is for these geometric orders; the preprint cites Dyer's broader reflection-order theorem. The blueprint follows the proved geometric-order statement.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.WallDyer.geometric_entry_eq_rTilde`: [ReflectionOrders.lean:1229](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionOrders.lean#L1229).
