---
id: kl.hecke.commutation
title: Left and right simple Hecke operators commute
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.definitions.hecke_operators
- kl.coxeter.simple_edge_transport
lean:
  repository: openai-kl
  modules:
  - Hecke
  declarations:
  - OAI.KLInvariance.Hecke.left_right_commute
  - OAI.KLInvariance.HeckeQ.left_right_commute
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:59
    format: lean-location
    note: OAI.KLInvariance.Hecke.left_right_commute
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:540
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.left_right_commute
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual coefficient hypotheses, conventions and source proof retained?
  verdict: Read both left_right_commute proofs. Expanded the noncollapsed orientation
    square in both parameter conventions and the identical two-dimensional action
    in the collapsed case.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Left and right simple Hecke operators commute

For simple reflections \(s,t\), left and right operators with the same parameter commute:
\[
L_sD_t=D_tL_s.
\]
This holds in both the normalized and unnormalized conventions over any commutative coefficient ring.

*Proof.*

### Step 1. Record the two length orientations

Fix a basis label \(w\). Put
\[
\varepsilon=\mathbf1_{\ell(sw)<\ell(w)},\qquad
\eta=\mathbf1_{\ell(wt)<\ell(w)}.
\]
If \(sw\ne wt\), [[node:kl.coxeter.simple_edge_transport|simple-edge transport]] gives
\[
\ell(swt)<\ell(wt)\ \Longleftrightarrow\ \ell(sw)<\ell(w),
\]
\[
\ell(swt)<\ell(sw)\ \Longleftrightarrow\ \ell(wt)<\ell(w).
\]
For the first equivalence, apply right multiplication by \(t\) to the edge between \(w\) and \(sw\). The hypothesis excludes its collapsed case. For the second, apply left multiplication by \(s\) to the edge between \(w\) and \(wt\). Thus the same two orientation flags apply at opposite sides of the square.

### Step 2. Expand the normalized square

In the case \(sw\ne wt\), the normalized formulas give
\[
L_sD_tH_w
=H_{swt}+a\varepsilon H_{wt}
+a\eta H_{sw}+a^2\varepsilon\eta H_w.
\]
Indeed, first \(D_tH_w=H_{wt}+a\eta H_w\), then apply \(L_s\) to both terms. The left-descent flag at \(wt\) is \(\varepsilon\) by Step 1.

In the reversed order,
\[
D_tL_sH_w
=H_{swt}+a\eta H_{sw}
+a\varepsilon H_{wt}+a^2\varepsilon\eta H_w.
\]
The two finite sums agree.

### Step 3. Expand the unnormalized square

For \(\epsilon\in\{0,1\}\), put
\[
c_\epsilon=\begin{cases}1,&\epsilon=0,\\ q,&\epsilon=1,\end{cases}
\qquad
d_\epsilon=\begin{cases}0,&\epsilon=0,\\ q-1,&\epsilon=1.\end{cases}
\]
Then \(L_sT_w=c_\varepsilon T_{sw}+d_\varepsilon T_w\), and the right formula has coefficients \(c_\eta,d_\eta\).

Using Step 1 at the opposite vertices gives
\[
L_sD_tT_w
=c_\eta c_\varepsilon T_{swt}
+c_\eta d_\varepsilon T_{wt}
+d_\eta c_\varepsilon T_{sw}
+d_\eta d_\varepsilon T_w.
\]
The reversed product gives these same four terms, with scalar factors in the opposite order. They agree because \(C\) is commutative.

### Step 4. Treat the collapsed square

Suppose \(u=sw=wt\). Then \(su=w=ut\). Both operators preserve the span of \(e_w,e_u\), and both act on it by the same two formulas: \(w\) and \(u\) have the same length comparison for the left and right operations.

Consequently \(L_s\) and \(D_t\) agree on this span, so their two composites agree on \(e_w\). This handles either orientation and both coefficient conventions.

Every basis label belongs to one of these cases. Equality on all basis vectors proves equality of the linear operators.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Hecke.left_right_commute`: [Hecke.lean:59](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L59).

`OAI.KLInvariance.HeckeQ.left_right_commute`: [Hecke.lean:540](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L540).
