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
- kl.paths.sorted_path_selection
- kl.paths.bruhat_path_polynomial
- kl.dihedral.plane_path_reversal
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
  verdict: Stated finite-generator and both lower-region endpoint hypotheses for the
    polynomial entry theorem. Expanded the intrinsic plane-block step using the actual
    interval flip, middle-descent test and path involution. The adapted rotation,
    ambient block transfer and generic-pencil exposition remain in the topic review
    plan.
tags:
- Kazhdan-Lusztig
- background
---

# The decreasing-path formula for a geometric reflection order

Fix a Coxeter system \(W\) with finitely many simple generators, and let \(b,x,y\in W\) satisfy \(x\le_Wb\) and \(y\le_Wb\). Use the fixed geometric functional on the original real root space. Let \(p_b\) be its decreasing schedule of all directed reflection edges below \(b\), and use the formal coefficient \(X\) over \(\mathbb Z[X]\).

Then the ordered transfer product has entry
\[
\bigl(\mathcal D_{p_b}(X)\delta_y\bigr)_x
=\widetilde R_{x,y}(X).
\]
The [[node:kl.notes.path_product|path-sum expansion]] expresses the left side as the sum of \(X^{|q|}\) over the selected directed paths from \(x\) to \(y\). Their geometric labels are strictly decreasing.

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

### Step 1. Ordered path-polynomial entries

On the finite lower region below \(b\), expand the transfer product using [[node:kl.notes.path_product]]. Its \((x,y)\)-entry is the sum of \(X^{|p|}\) over directed paths whose edges occur in the schedule order. The [[node:kl.paths.sorted_path_selection|sorted-path selection theorem]] makes the weak schedule order strict along every contributing path, because equal root labels cannot be composable.

### Step 2. The adapted-order recursion

Choose a geometric ratio order whose numerator lies in the chamber adapted to \(y\). If \(y\ne1\), its chamber-rotation construction chooses a simple descent \(s\) and a second ratio order for \(sy\). In the original order the simple root is least; in the rotated order it is greatest. Reflection by \(s\) identifies the orderings of all other roots.

Split increasing paths according to whether they use that least simple edge. If \(sx<x\), such an edge cannot start a directed path from \(x\), and reflection transports all paths to paths from \(sx\) to \(sy\). If \(sx>x\), paths omitting the simple edge transport to paths from \(sx\) to \(sy\); paths using it must use it first and transport, after removing it, to paths from \(x\) to \(sy\). Removing that first edge removes one factor of \(X\).

Thus the path polynomials obey exactly
\[
F_{x,y}=\begin{cases}
F_{sx,sy},&sx<x,\\
F_{sx,sy}+TF_{x,sy},&sx>x.
\end{cases}
\]
The empty path gives \(F_{x,x}=1\), and there are no paths outside Bruhat order. Induction on \(\ell(y)\), using the rotated order at each step, identifies this adapted path polynomial with the Hecke-defined \(\widetilde R_{x,y}\).

### Step 3. The full intrinsic root-plane block

Fix an induced root-plane system \(D\) with its actual ambient root slopes, and a full intrinsic interval \([\mathrm{lo},\mathrm{hi}]_D\). The [[node:kl.dihedral.interval_flip|interval-flip construction]] fixes both endpoints and exchanges the two vertices in each strictly internal rank. Its edge map preserves source and target through that vertex map and is an involution.

For a composable pair \(e:x\to y\), \(h:y\to z\), the middle vertex has length strictly between the endpoint lengths. It has exactly one simple left descent, and the flip exchanges that descent. The [[node:kl.dihedral.middle_vertex_order|middle-vertex slope test]] therefore gives
\[
\lambda(e)<\lambda(h)
\Longleftrightarrow
\lambda(g(h))<\lambda(g(e)).
\]
The [[node:kl.dihedral.plane_path_reversal|plane-path reversal theorem]] verifies this equivalence and uses it in both directions of [[node:kl.paths.path_transport|sorted path transport]]. A decreasing path in a full schedule maps to a path in the reverse schedule, with the same fixed endpoints and the same number of edges. The involution gives the inverse correspondence.

The [[node:kl.notes.path_product|path-sum expansion]] now gives equality of the two endpoint entries on the intrinsic interval. To pass to the ambient lower region, paths whose labels all lie in this plane stay in one plane-subgroup coset. The coset graph identification lifts them to the full relative interval between their endpoints. Applying the intrinsic identity there gives the corresponding ambient plane-block entry equality; if the endpoints have no such path, both entries are zero.

### Step 4. Generic pencils and order independence

Choose a common transverse functional \(g\) for the given functional \(f\) and an adapted one \(h\), as follows. For three normalized roots \(a,b,c\) with \(c\) outside the plane of \(a,b\), put
\[
v_f=f(a-b)(c-b)-f(c-b)(a-b).
\]
The two difference vectors are independent and \(f(a-b)\ne0\), so \(v_f\ne0\). Require \(g(v_f)\ne0\), impose the analogous conditions for \(h\), and also require \(g(a-b)\ne0\) for distinct normalized roots. There are only countably many nonzero vectors to avoid; the polynomial-family argument in the generic-functional proof chooses such a \(g\).

If a pencil \((1-t)f+tg\) ties \(a,b,c\), eliminating \(t\) from the two equalities would give \(g(v_f)=0\). Thus no root outside the plane can join a tie of \(a,b\). Conversely, the normalized roots in that plane lie on the affine line through \(a,b\), so every one ties when \(a,b\) do. This proves the complete-plane-block condition. Along the linear pencils from \(f\) to \(g\) and from \(h\) to \(g\), a tie involving distinct roots is, by the transverse choice, a complete actual root-plane block.

Near any pencil parameter, the strict comparisons between different tied blocks remain fixed: only finitely many edges occur in the lower region, so finitely many strict inequalities need to be preserved. Inside each block, a linear functional orders the normalized roots either angularly or in reverse angular order. Step 3 identifies these two products. A block with only one reflection label consists of noninteracting edges, whose transfers commute.

Hence every block product, and therefore the whole entry, is locally constant along the pencil, including at crossing parameters. A locally constant function on the connected real parameter interval is constant. Comparing both pencils identifies the entry for \(f\) with that for \(h\).

### Step 5. The sign convention and fixed geometric functional

The adapted calculation in Step 2 counts increasing labels. Negating its numerator makes the decreasing schedule count exactly those paths. Step 4 permits replacing that negative numerator by the fixed geometric functional used for the full matrix. The constructed functional separates all positive-root slopes, so it satisfies the required genericity hypothesis. Its entry is therefore \(\widetilde R_{x,y}(X)\).

The Lean result used here is for these geometric orders; the preprint cites Dyer's broader reflection-order theorem. The blueprint follows the proved geometric-order statement.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.WallDyer.geometric_entry_eq_rTilde`: [ReflectionOrders.lean:1229](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionOrders.lean#L1229).
