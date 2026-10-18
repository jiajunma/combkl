---
id: kl.paths.plane_degree
title: The sum of root-plane weights and the edge-factor degree
kind: theorem
status: proved
primary_topic: kl.06_reflection_orders
topics:
- kl.06_reflection_orders
uses:
- kl.realization.reflection_plane
- kl.foundations.bruhat_step
- kl.detail.edge_factor
- kl.detail.root_inversion_count
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.TitsSpace.sum_planeWeight
  - OAI.KLInvariance.TitsSpace.edgeFactor_degree_formula
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:621
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.sum_planeWeight
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:993
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.edgeFactor_degree_formula
  - artifact: openai-kl-paper
    locator: 3. Dihedral intervals and transported reflection orders; sec:dihedral
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
- dihedral
---

# The sum of root-plane weights and the edge-factor degree

For an upward reflection edge \(x\to r_\alpha x\), group the change in inversion roots by planes containing \(\alpha\). The resulting nonnegative integral weights \(k_\Pi\) have finite support and satisfy
\[
2\sum_\Pi k_\Pi=\ell(r_\alpha x)-\ell(x)-1.
\]
The edge factor \(f_e\), formed from the corresponding reduced root factors, therefore has degree
\[
\deg f_e=\frac{\ell(r_\alpha x)-\ell(x)-1}{2}.
\]

*Proof.*

### Step 1. Sum the change in inversion indicators

Let \(y=r_\alpha x>x\). For each positive root \(\beta\), let \(n_x(\beta)\) be one if it is inverted by \(x\), and zero otherwise. Only finitely many indicators are nonzero, and
\(\sum_\beta n_x(\beta)=\ell(x)\).
Thus the total change is
\(\sum_\beta(n_y(\beta)-n_x(\beta))=\ell(y)-\ell(x)\).

The distinguished root \(\alpha\) changes from noninverted to inverted, contributing one. Remove it. The remaining total is therefore \(\ell(y)-\ell(x)-1\).

### Step 2. Pair roots before grouping them into planes

Reflection in \(\alpha\), followed by choosing the positive representative of a root line, gives an involution \(\beta\mapsto\beta^*\). It preserves the plane spanned with \(\alpha\).

The root-sign calculation for an upward \(\alpha\)-edge gives
\[
(n_y-n_x)(\beta)+(n_y-n_x)(\beta^*)=
\begin{cases}
2,&\text{a contributing negative pair},\\
0,&\text{otherwise}.
\end{cases}
\]
In the contributing case, both roots were noninverted before the move and reflection in \(\alpha\) interchanges their lines with a negative sign. The other sign cases either leave both indicators unchanged or contribute one positive and one negative change, which cancel. The distinguished root has already been removed.

### Step 3. Define and count the half-pairs

For each contributing pair choose the member with smaller geometric slope. The two slopes are distinct, and the involution exchanges the members, so exactly one is chosen. Let \(k_P\) count the chosen members in plane \(P\). These are nonnegative integers, with finite support.

Grouping Step 2 by planes gives a total contribution \(2k_P\) in each plane. Summing and using Step 1 proves
\[
2\sum_Pk_P=\ell(y)-\ell(x)-1.
\]

### Step 4. Compute the polynomial degree

The actual edge factor is
\(f_e=\prod_P\overline\beta_P^{\,k_P}\)
in the coefficient ring modulo \(\alpha\). Every reduced root \(\overline\beta_P\) is nonzero and homogeneous of degree one. That quotient ring is a polynomial domain, so the product is nonzero and homogeneous of degree \(\sum_Pk_P\).

A nonzero homogeneous polynomial has total degree equal to its homogeneous degree. Hence
\(\deg f_e=\sum_Pk_P=(\ell(y)-\ell(x)-1)/2\).
This explains both the integrality of the half-length expression and its use in the normalized transfer coefficient.

## References

[3. Dihedral intervals and transported reflection orders](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L2).

## Lean formalization

`OAI.KLInvariance.TitsSpace.sum_planeWeight`: [ReflectionSchedules.lean:621](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L621).

`OAI.KLInvariance.TitsSpace.edgeFactor_degree_formula`: [ReflectionSchedules.lean:993](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L993).
