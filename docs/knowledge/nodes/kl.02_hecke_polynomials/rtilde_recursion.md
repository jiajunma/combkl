---
id: kl.detail.rtilde_recursion
title: The descent recursion for normalized R-polynomials
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.detail.rtilde_family
- kl.definitions.bar_involution
- kl.detail.hecke_quadratic_identity
lean:
  repository: openai-kl
  modules:
  - Hecke
  declarations:
  - OAI.KLInvariance.Hecke.rTilde_recursion
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:491
    format: lean-location
    note: OAI.KLInvariance.Hecke.rTilde_recursion
  - artifact: openai-kl-paper
    locator: Related paper context; sec:introduction
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- hecke_polynomials
---

# The descent recursion for normalized R-polynomials

If \(s\) is a simple reflection and \(sy<y\), then
\[
\widetilde R_{x,y}(a)=
\begin{cases}
\widetilde R_{sx,sy}(a),&sx<x,\\
\widetilde R_{sx,sy}(a)+a\widetilde R_{x,sy}(a),&sx>x.
\end{cases}
\]
Together with diagonal value \(1\) and vanishing outside Bruhat order, this computes the family by induction on the upper endpoint's length. The rank-one value is \(\widetilde R_{1,s}(a)=a\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same polynomial, different construction order.**

**OpenAI notes:** The path-formula theorem introduces the normalized R-polynomial through increasing reflection paths and relates it to the ordinary R-polynomial; decreasing paths follow by reversing the reflection order. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [eq:bg-path-formula](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L191).

**Lean (primary):** The normalized R-family is defined first as a coefficient of the Hecke bar transform. Its recursion is proved algebraically, and the geometric path product is later proved equal to that independently constructed family. [Hecke:482](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L482), [Hecke:491](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L491), [ReflectionOrders:1229](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionOrders.lean#L1229).

**How to read this entry:** The bar construction supplies the R-family and its recursion. The path theorem then identifies that family with the ordered path polynomial.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Relate the two upper endpoints

Fix a simple reflection \(s\) with \(sy<y\), and put \(v=sy\). Then \(sv=y\) is an ascent from \(v\). Write \(B_v\) for the bar-basis vector at \(v\), with the parameter convention \(-a\) used to define \(\widetilde R\).

The bar-basis ascent formula gives \(B_y=L_s^{-1}B_v\). The quadratic identity says that the inverse operator is \(L_s-(-a)=L_s+a\) in this parameter convention.

### Step 2. Read the coefficient of a general vector

Write \(B_v=\sum_w b_we_w\). The basis formula with parameter \(-a\) is
\[
L_se_w=e_{sw}-a\mathbf1_{\ell(sw)<\ell(w)}e_w.
\]
The coefficient of \(e_x\) in \(L_sB_v\) is
\(b_{sx}-a\mathbf1_{\ell(sx)<\ell(x)}b_x\):
the first term comes from \(w=sx\), and the second from \(w=x\).

Adding \(aB_v\), the coefficient in \(L_s^{-1}B_v\) is therefore
\[
b_{sx}+a\bigl(1-\mathbf1_{\ell(sx)<\ell(x)}\bigr)b_x.
\]

### Step 3. Substitute the R-coefficients

By definition,
\(b_{sx}=\widetilde R_{sx,sy}(a)\) and
\(b_x=\widetilde R_{x,sy}(a)\).
If \(sx<x\), the indicator is one and the second term cancels. If \(sx>x\), it is zero and the second term is \(a\widetilde R_{x,sy}(a)\). These are exactly the two branches in the statement.

Since the upper endpoint \(sy\) is shorter than \(y\), this recurrence is suitable for induction. At \(x=y\) the diagonal coefficient is one; outside Bruhat order triangularity gives zero, so these cases are consistent with the same constructed family.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization



`OAI.KLInvariance.Hecke.rTilde_recursion`: [Hecke.lean:491](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L491).
