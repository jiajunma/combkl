---
id: kl.realization.linear_reflection
title: Linear reflections from a root and a normal
kind: definition
status: formalized
primary_topic: kl.realizations
topics:
- kl.realizations
uses: []
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.Realization.geometricSimple
  - OAI.KLInvariance.Realization.simple_normal_value
  - OAI.KLInvariance.Realization.geometricSimple_preserves
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:311
    format: lean-location
    note: OAI.KLInvariance.Realization.geometricSimple
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:307
    format: lean-location
    note: OAI.KLInvariance.Realization.simple_normal_value
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:339
    format: lean-location
    note: OAI.KLInvariance.Realization.geometricSimple_preserves
  - artifact: openai-kl-paper
    locator: Real realizations; bg:realization
    format: section
    note: Construction and normalization of the realization.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition retain the local source hypotheses and construction?
  verdict: Source statements and construction read directly; dimensions, normalization,
    and orthogonality direction stated explicitly.
tags:
- Kazhdan-Lusztig
- realization
---

# Linear reflections from a root and a normal

Let \(V\) be a real vector space, let \(\alpha\in V\), and let \(f:V\to\mathbb R\) be linear with \(f(\alpha)=2\). Define
\[
r_{\alpha,f}(v)=v-f(v)\alpha.
\]
The equation \(f(\alpha)=2\) implies that both \(\alpha\) and \(f\) are nonzero.

## Fixed and moving directions

For \(v\in\ker f\), the formula gives \(r_{\alpha,f}(v)=v\). It also gives \(r_{\alpha,f}(\alpha)=-\alpha\). Every vector decomposes as
\[
v=\left(v-\frac{f(v)}2\alpha\right)+\frac{f(v)}2\alpha.
\]
The first term lies in \(\ker f\). If \(c\alpha\in\ker f\), then \(0=f(c\alpha)=2c\), so the intersection of the two summands is zero. Thus
\[
V=\ker f\oplus\mathbb R\alpha.
\]
The reflection acts by \(+1\) on the first summand and by \(-1\) on the second.

For a direct check, linearity gives \(f(r_{\alpha,f}(v))=-f(v)\). Therefore
\[
r_{\alpha,f}(r_{\alpha,f}(v))
=v-f(v)\alpha-(-f(v))\alpha=v.
\]
The reflection is an invertible linear map and is its own inverse.

The image of \(r_{\alpha,f}-1\) is \(\mathbb R\alpha\): every value is a multiple of \(\alpha\), and its value at \(\alpha\) is \(-2\alpha\). Its fixed space is \(\ker f\), of codimension one.

## Reflection defined by a bilinear form

Let \(B\) be symmetric and satisfy \(B(\alpha,\alpha)=2\). Taking \(f=B(\alpha,-)\) gives
\[
r_\alpha(v)=v-B(\alpha,v)\alpha.
\]
Put \(a=B(\alpha,v)\) and \(b=B(\alpha,w)\). Bilinearity gives
\[
\begin{aligned}
B(r_\alpha(v),r_\alpha(w))
 &=B(v,w)-bB(v,\alpha)-aB(\alpha,w)+abB(\alpha,\alpha)\\
 &=B(v,w)-ab-ab+2ab\\
 &=B(v,w).
\end{aligned}
\]
Hence \(r_\alpha\) preserves \(B\). This uses symmetry and the normalization \(B(\alpha,\alpha)=2\).

For the Tits form, take \(\alpha=\alpha_i\) and \(f=\nu_i\). These are the simple operators used to construct the geometric action.

## References

[Realizations in the OpenAI notes](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L34).

## Lean formalization

`OAI.KLInvariance.Realization.geometricSimple`: [Tits.lean:311](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L311).

`OAI.KLInvariance.Realization.simple_normal_value`: [Tits.lean:307](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L307).

`OAI.KLInvariance.Realization.geometricSimple_preserves`: [Tits.lean:339](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L339).
