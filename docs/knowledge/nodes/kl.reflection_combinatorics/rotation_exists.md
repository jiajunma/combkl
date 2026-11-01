---
id: kl.order.rotation_exists
title: A chamber order rotates at a least simple descent
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.order.rotated_ratio_order
- kl.order.chamber_adaptation
- kl.notes.reflection_order
- kl.realization.positive_root_action
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.TitsSpace.exists_uniform_pos_lt
  - OAI.KLInvariance.TitsSpace.RatioOrder.exists_turn_parameter
  - OAI.KLInvariance.TitsSpace.RatioOrder.turn_chamber
  - OAI.KLInvariance.TitsSpace.RatioOrder.turn_simple_greatest
  - OAI.KLInvariance.TitsSpace.RatioOrder.turn_slope_lt_iff
  - OAI.KLInvariance.TitsSpace.RatioOrder.exists_rotation
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1351
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.exists_uniform_pos_lt
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1375
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.RatioOrder.exists_turn_parameter
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1459
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.RatioOrder.turn_chamber
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1468
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.RatioOrder.turn_simple_greatest
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1489
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.RatioOrder.turn_slope_lt_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1527
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.RatioOrder.exists_rotation
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the chamber, positivity, simple-label exclusions, two orders and exact
    induction hypotheses retained?
  verdict: Read the finite gap construction, positivity checks on each simple root,
    turn_chamber, comparison through one and the positive-denominator cross multiplication.
    Preserved the exact non-simple comparisons and both strict endpoint-order conditions
    of exists_rotation.
tags:
- Kazhdan-Lusztig
- reflection_orders
---

# A chamber order rotates at a least simple descent

Fix a finite-generator Coxeter system \(W\), a ratio order \(O=(h,f)\), and \(y\ne1\) satisfying \(O.\mathrm{Chamber}(y)\).
There are a simple generator \(s=s_i\) and a ratio order \(O'\) such that:

1. \(\ell(sy)<\ell(y)\) and \(O'.\mathrm{Chamber}(sy)\);
2. for every positive root \(a\ne\alpha_i\),
\[
\sigma_O(\alpha_i)<\sigma_O(a),\qquad
\sigma_{O'}(a)<\sigma_{O'}(\alpha_i);
\]
3. for \(a,b\ne\alpha_i\),
\[
\sigma_{O'}(s\star a)<\sigma_{O'}(s\star b)
\Longleftrightarrow
\sigma_O(a)<\sigma_O(b).
\]
Here \(s\star-\) is the [[node:kl.realization.positive_root_action|positive-root action]]. The order \(O'\) is the [[node:kl.order.rotated_ratio_order|rotated ratio-order construction]] for a suitable negative parameter.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**A fractional-linear change of slopes at a simple descent.**

**OpenAI notes:** The background path formula is cited for reflection orders, with the decreasing version obtained by reversing an order. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185).

**Lean (primary):** The adapted proof explicitly constructs a second ratio order: compose the numerator with a simple reflection and compose numerator minus k times denominator with the same reflection. A finite positive-gap choice gives negative k and a positive new denominator. The new chamber is indexed by the shorter element; the chosen simple root becomes greatest and other reflected comparisons are preserved. [DyerPaths:1369](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1369), [DyerPaths:1372](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1372), [DyerPaths:1413](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1413), [DyerPaths:1375](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1375), [DyerPaths:1459](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1459), [DyerPaths:1468](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1468), [DyerPaths:1489](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1489), [DyerPaths:1527](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1527).

**Role in the proof:** The construction retains its generic k!=0 and positivity hypotheses, while the rotation theorem states its negative-parameter conditions. The A2 example computes the old and new slopes through the same formulas.
<!-- source-comparison:end -->

*Proof.*

### Step 1. A least simple descent

The [[node:kl.order.chamber_adaptation|chamber and least-descent theorem]] gives \(i\) with
\[
\ell(s_i y)<\ell(y),\qquad
c:=\sigma_O(\alpha_i)<0,\qquad
c\le\sigma_O(a)\quad(a\in\Phi^+).
\]
The slope is injective, so the last inequality is strict when \(a\ne\alpha_i\). This establishes the required least-root property in \(O\).

### Step 2. A parameter from finitely many positive gaps

For each simple-root index \(j\), set
\[
v_j=
\begin{cases}
-c,&j=i,\\
\sigma_O(s_i\star\alpha_j)-c,&j\ne i.
\end{cases}
\]
The first value is positive because \(c<0\).
For \(j\ne i\), the [[node:kl.realization.positive_root_action|positive-root action]] sends \(\alpha_j\) to a positive root different from \(\alpha_i\). Step 1 and slope injectivity therefore make \(v_j>0\).

There are finitely many such numbers and at least one index \(i\). Choose
\[
0<\varepsilon<\min_j v_j,\qquad k=c+\varepsilon.
\]
For example, half the minimum works. Then \(c<k<0\), since \(\varepsilon<v_i=-c\).
This is the finite positive-gap choice implemented by `exists_uniform_pos_lt` and `exists_turn_parameter`.

### Step 3. Positivity of the turned denominator

Let \(S=\rho(s_i)\) and \(h'_k=(f-kh)\circ S\).
At \(\alpha_i\), use \(S\alpha_i=-\alpha_i\) and \(f(\alpha_i)=c h(\alpha_i)\):
\[
h'_k(\alpha_i)
=-f(\alpha_i)+k h(\alpha_i)
=(k-c)h(\alpha_i)
=\varepsilon h(\alpha_i)>0.
\]
For \(j\ne i\), put \(a_j=s_i\star\alpha_j=S\alpha_j\). Then
\[
h'_k(\alpha_j)
=h(a_j)\bigl(\sigma_O(a_j)-k\bigr)
=h(a_j)(v_j-\varepsilon)>0.
\]
Thus the turned denominator is positive on every simple root and hence every positive root.
Also \(k<0\) implies \(k\ne0\). The [[node:kl.order.rotated_ratio_order|rotated ratio-order construction]] therefore supplies \(O'=(h'_k,f\circ S)\), including injectivity of its slope.

### Step 4. The new chamber

For each simple root \(\alpha_j\),
\[
f'(\rho(s_i y)\alpha_j)
=f(\rho(s_i)\rho(s_i y)\alpha_j)
=f(\rho(y)\alpha_j)>0.
\]
The middle equality uses \(s_i^2=1\). This is exactly \(O'.\mathrm{Chamber}(s_i y)\).

### Step 5. The simple root becomes greatest

For a positive root \(a\ne\alpha_i\), its transform \(Sa\) is positive, so \(h(Sa)>0\).
Since \(k<0\),
\[
h'_k(a)-f'(a)=-k h(Sa)>0.
\]
Divide by \(h'_k(a)>0\) to get \(\sigma_{O'}(a)<1\).
For the simple root,
\[
f'(\alpha_i)-h'_k(\alpha_i)=-k h(\alpha_i)>0,
\]
so \(\sigma_{O'}(\alpha_i)>1\).
Combining the two strict inequalities proves that every other positive-root slope lies below the simple-root slope.

### Step 6. Preservation of the other comparisons

Take \(a,b\ne\alpha_i\), and put \(u=\sigma_O(a)\), \(v=\sigma_O(b)\).
The fractional-linear formula gives the new slopes at their positive reflected roots as
\[
\frac{u}{u-k},\qquad\frac{v}{v-k},
\]
with both denominators positive. Cross multiplication therefore yields
\[
\begin{aligned}
\frac{u}{u-k}<\frac{v}{v-k}
&\Longleftrightarrow u(v-k)<v(u-k)\\
&\Longleftrightarrow -ku<-kv\\
&\Longleftrightarrow u<v,
\end{aligned}
\]
where the last step uses \(-k>0\). This proves the required equivalence and completes every assertion.

The construction moves the least simple label to the opposite end of the order while replacing the top element \(y\) by the strictly shorter element \(s_i y\). These are the geometric inputs to the [[node:kl.paths.path_polynomial_recursion|path-polynomial recursion]].

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.exists_uniform_pos_lt`: [DyerPaths.lean:1351](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1351).

`OAI.KLInvariance.TitsSpace.RatioOrder.exists_turn_parameter`: [DyerPaths.lean:1375](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1375).

`OAI.KLInvariance.TitsSpace.RatioOrder.turn_chamber`: [DyerPaths.lean:1459](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1459).

`OAI.KLInvariance.TitsSpace.RatioOrder.turn_simple_greatest`: [DyerPaths.lean:1468](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1468).

`OAI.KLInvariance.TitsSpace.RatioOrder.turn_slope_lt_iff`: [DyerPaths.lean:1489](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1489).

`OAI.KLInvariance.TitsSpace.RatioOrder.exists_rotation`: [DyerPaths.lean:1527](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1527).
