---
id: kl.realization.radical_extension
title: The radical and its dual extension
kind: definition
status: formalized
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.realization.tits_form
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.Realization.Extension
  - OAI.KLInvariance.Realization.extensionForm
  - OAI.KLInvariance.Realization.extensionForm_inl
  - OAI.KLInvariance.TitsSpace.Extended
  - OAI.KLInvariance.TitsSpace.extendedForm
  - OAI.KLInvariance.TitsSpace.extendedRoot
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:439
    format: lean-location
    note: OAI.KLInvariance.Realization.Extension
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:441
    format: lean-location
    note: OAI.KLInvariance.Realization.extensionForm
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:466
    format: lean-location
    note: OAI.KLInvariance.Realization.extensionForm_inl
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:553
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.Extended
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:555
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.extendedForm
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:562
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.extendedRoot
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

# The radical and its dual extension

Let \(V_0\) be a real vector space with symmetric bilinear form \(B\). Its radical is
\[
K=\{v\in V_0:B(v,w)=0\text{ for every }w\in V_0\}=\ker B^\flat.
\]
Symmetry also gives \(B(w,k)=0\) for \(k\in K\). The form is nondegenerate when \(K=0\). Positive definiteness is the stronger condition \(B(v,v)>0\) for every nonzero \(v\).

The dual space \(K^*\) consists of linear maps \(K\to\mathbb R\), with pointwise addition and scalar multiplication. These functionals detect vectors: for nonzero \(k\), include \(k\) in a basis and assign value one to \(k\) and zero to the other basis vectors.

## A projection onto the radical

Choose a complementary subspace \(U\) with \(V_0=U\oplus K\). Every vector has a unique expression \(v=u+k\). The map
\[
p:V_0\longrightarrow K,\qquad p(u+k)=k
\]
is linear and satisfies \(p(k)=k\) for \(k\in K\).

Form \(E=V_0\oplus K^*\), with embedding \(\iota(v)=(v,0)\). Define
\[
B_p((v,\phi),(w,\psi))
=B(v,w)+\phi(pw)+\psi(pv).
\]
Every term is bilinear in the two pairs. The added directions pair with the radical by
\[
B_p((k,0),(0,\psi))=\psi(k).
\]
They pair to zero with \(U\) and with one another. The original form is preserved:
\[
B_p(\iota(v),\iota(w))=B(v,w).
\]
The choice of complement enters through \(p\); the displayed formula then determines the extension.

## The infinite dihedral example

For the infinite dihedral Tits form, \(K=\mathbb Rk\), where \(k=\alpha_s+\alpha_t\). Choose
\[
p(x\alpha_s+y\alpha_t)=\frac{x+y}{2}k.
\]
This fixes \(k\) and has kernel \(\mathbb R(\alpha_s-\alpha_t)\). Choose \(\phi\in K^*\) with \(\phi(k)=2\). In the basis \(\alpha_s,\alpha_t,\phi\), the extended Gram matrix is
\[
\begin{pmatrix}2&-2&1\\-2&2&1\\1&1&0\end{pmatrix}.
\]
Its determinant is \(-8\). The simple normals now have rows \((2,-2,1)\) and \((-2,2,1)\). If their linear combination with coefficients \(a,b\) vanishes, the first coordinate gives \(a=b\), and the third gives \(a+b=0\); hence both coefficients vanish.

The extra coordinate supplies values that separate the two normals while retaining the original independent roots. This illustrates [[node:kl.notes.extended_realization]].

## The extended Tits space

Apply the construction to the Tits form on \(\mathbb R^I\). The extended root is \(\widetilde\alpha_i=(\alpha_i,0)\). The development chooses a symmetric nondegenerate form supplied by the extension theorem. Its root pairings remain \(g_{ij}\).

These roots and the chosen form define reflections on all of \(E\). Their restriction to \(\iota(V_0)\) gives the original geometric action. The symmetric algebra of \(E\) will be the coefficient algebra.

## References

[Realizations in the OpenAI notes](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L34).

## Lean formalization

`OAI.KLInvariance.Realization.Extension`: [Tits.lean:439](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L439).

`OAI.KLInvariance.Realization.extensionForm`: [Tits.lean:441](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L441).

`OAI.KLInvariance.Realization.extensionForm_inl`: [Tits.lean:466](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L466).

`OAI.KLInvariance.TitsSpace.Extended`: [Tits.lean:553](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L553).

`OAI.KLInvariance.TitsSpace.extendedForm`: [Tits.lean:555](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L555).

`OAI.KLInvariance.TitsSpace.extendedRoot`: [Tits.lean:562](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L562).

`extensionForm` takes the projection explicitly. `extendedForm` chooses a form from the existence theorem and uses its symmetry, nondegeneracy, and restriction properties.
