---
id: kl.realization.tits_form
title: The Tits form, simple roots, and normal functionals
kind: definition
status: formalized
primary_topic: kl.03_realizations_and_grading
topics:
- kl.03_realizations_and_grading
uses: []
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.gram
  - OAI.KLInvariance.TitsSpace.root
  - OAI.KLInvariance.TitsSpace.normal
  - OAI.KLInvariance.TitsSpace.form
  - OAI.KLInvariance.TitsSpace.form_symm
  - OAI.KLInvariance.TitsSpace.form_roots
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:365
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.gram
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:367
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.root
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:371
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.normal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:374
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.form
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:391
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.form_symm
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:405
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.form_roots
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

# The Tits form, simple roots, and normal functionals

Let \(I\) be a finite set of simple generators for a Coxeter system \((W,S)\). Write \(m_{ij}\) for the order of \(s_is_j\). Thus \(m_{ii}=1\), and for distinct indices \(m_{ij}\) is an integer at least two or is infinite.

The geometric root space is \(V_0=\mathbb R^I\). For each \(i\), let \(\alpha_i\) be the vector whose \(i\)-th coordinate is one and whose other coordinates are zero. Every vector has a unique expression \(v=\sum_i v_i\alpha_i\).

## The defining matrix

Set
\[
g_{ij}=
\begin{cases}
-2\cos(\pi/m_{ij}),&m_{ij}<\infty,\\
-2,&m_{ij}=\infty.
\end{cases}
\]
The Tits form is the bilinear map
\[
B:V_0\times V_0\longrightarrow\mathbb R,\qquad
B(v,w)=\sum_{i,j\in I}v_i g_{ij}w_j.
\]
Consequently \(B(\alpha_i,\alpha_j)=g_{ij}\). Symmetry of the Coxeter matrix gives \(g_{ij}=g_{ji}\); interchanging the two summation indices proves \(B(v,w)=B(w,v)\).

The normalization gives \(g_{ii}=-2\cos\pi=2\). For distinct generators, exponent two gives \(g_{ij}=0\), exponent three gives \(g_{ij}=-1\), and an infinite exponent gives \(g_{ij}=-2\). Thus the relations between the generators determine every matrix entry.

## Root vectors and normal functionals

The simple normal associated with \(\alpha_i\) is
\[
\nu_i:V_0\longrightarrow\mathbb R,\qquad
\nu_i(v)=B(\alpha_i,v)=\sum_jg_{ij}v_j.
\]
A root vector belongs to \(V_0\); its normal belongs to the dual space \(V_0^*=\operatorname{Hom}_{\mathbb R}(V_0,\mathbb R)\). The form defines a linear map
\[
B^\flat:V_0\longrightarrow V_0^*,\qquad v\longmapsto B(v,-),
\]
sending \(\alpha_i\) to \(\nu_i\).

The simple reflection formula is \(s_i(v)=v-\nu_i(v)\alpha_i\). It changes only the \(i\)-th coordinate in the simple-root basis. Since \(\nu_i(\alpha_i)=2\), it sends \(\alpha_i\) to \(-\alpha_i\) and fixes every vector in \(\ker\nu_i\). The involution calculation is developed in [[node:kl.realization.linear_reflection]].

## Two rank-two calculations

For \(m_{st}=3\), the Gram matrix is
\[
\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
\]
Its determinant is three, so \(B^\flat\) is invertible. Both the roots and the normals are independent.

For \(m_{st}=\infty\), the matrix is
\[
\begin{pmatrix}2&-2\\-2&2\end{pmatrix}.
\]
Here \(\nu_s(x\alpha_s+y\alpha_t)=2x-2y\) and \(\nu_t(x\alpha_s+y\alpha_t)=-2x+2y\). The roots still form a basis, whereas \(\nu_t=-\nu_s\). The vector \(k=\alpha_s+\alpha_t\) satisfies \(B(k,v)=0\) for every \(v\). The kernel of \(B^\flat\) is called the radical.

The extension construction pairs radical directions with added dual directions. It retains the original roots and gives independent extended normals; see [[node:kl.realization.radical_extension]] and [[node:kl.notes.extended_realization]].

## References

[Realizations in the OpenAI notes](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L34).

## Lean formalization

`OAI.KLInvariance.TitsSpace.gram`: [Tits.lean:365](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L365).

`OAI.KLInvariance.TitsSpace.root`: [Tits.lean:367](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L367).

`OAI.KLInvariance.TitsSpace.normal`: [Tits.lean:371](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L371).

`OAI.KLInvariance.TitsSpace.form`: [Tits.lean:374](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L374).

`OAI.KLInvariance.TitsSpace.form_symm`: [Tits.lean:391](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L391).

`OAI.KLInvariance.TitsSpace.form_roots`: [Tits.lean:405](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L405).

The Coxeter matrix encodes infinity by zero. In the coefficient formula, real division by zero gives `Real.pi / 0 = 0`, so the entry is `-2 * Real.cos 0 = -2`. The diagonal entry is one and gives `-2 * Real.cos Real.pi = 2`.
