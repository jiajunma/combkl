---
id: kl.definitions.bar_involution
title: Inverse-basis transforms and the Hecke bar involution
kind: definition
status: formalized
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.hecke.word_actions
- kl.hecke.word_independence
lean:
  repository: openai-kl
  modules:
  - Hecke
  declarations:
  - OAI.KLInvariance.Hecke.barBasis
  - OAI.KLInvariance.Hecke.barLinear
  - OAI.KLInvariance.HeckeQ.barBasis
  - OAI.KLInvariance.HeckeQ.barLinear
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:303
    format: lean-location
    note: OAI.KLInvariance.Hecke.barBasis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:339
    format: lean-location
    note: OAI.KLInvariance.Hecke.barLinear
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:790
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.barBasis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:833
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.barLinear
  - artifact: openai-kl-paper
    locator: 1. Introduction and conventions; sec:introduction
    format: section
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual coefficient hypotheses, conventions and source proof retained?
  verdict: Read both barBasis/barLinear definitions. Put inverse standard operators
    first, state the exact coefficient-linear maps, and derive the Laurent semilinear
    description by coefficient substitution.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Inverse-basis transforms and the Hecke bar involution

Let \(U_w\) be the standard invertible action on the Hecke module. The inverse-basis vector attached to \(w\) is
\[
b_w=U_{w^{-1}}^{-1}e_1.
\]
The linear bar transform is the \(C\)-linear operator \(B\) defined by \(B(e_w)=b_w\). Thus for any finitely supported vector,
\[
B\left(\sum_w c_we_w\right)=\sum_w c_wb_w.
\]
The standard action is independent of the chosen reduced word, so this definition is independent of that choice as well.

Write \(b_w(a),B_a\) in the normalized convention, and \(b_w(q),B_q\) in the unnormalized convention. The latter uses a unit \(q\).

## A reduced-word formula

If \(w=s_1\cdots s_m\) is reduced, then the reverse word is reduced for \(w^{-1}\). Reversing the product when taking its inverse gives
\[
b_w=L_{s_1}^{-1}\cdots L_{s_m}^{-1}e_1.
\]
In particular \(b_1=e_1\). For a simple reflection,
\[
b_s(a)=H_s-aH_1,\qquad
b_s(q)=q^{-1}T_s+(q^{-1}-1)T_1.
\]

These expressions are the vectors denoted conventionally by \(H_{w^{-1}}^{-1}\) and \(T_{w^{-1}}^{-1}\). The source defines them by inverse operators.

## Parameter interchange

The parameter-interchange theorem proves
\[
B_aL_s(-a)=L_s(a)^{-1}B_a,\qquad B_aB_{-a}=I,
\]
and
\[
B_qL_s(q^{-1})=L_s(q)^{-1}B_q,\qquad B_qB_{q^{-1}}=I.
\]
The maps \(B_a,B_q\) themselves are coefficient-linear.

## Semilinearity over Laurent coefficients

In the normalized Laurent convention, \(C=\mathbb Z[v,v^{-1}]\) and \(a=v-v^{-1}\). Let \(\sigma\) replace \(v\) by \(v^{-1}\) in every coefficient and leave the basis labels fixed. Then \(\sigma(a)=-a\).

The semilinear bar is
\[
\overline f=B_a(\sigma f).
\]
Consequently \(\overline{cf}=\sigma(c)\overline f\), and \(\overline{H_w}=b_w(a)\). Applying coefficient inversion to the defining operator formulas changes \(B_a\) to \(B_{-a}\). Hence
\[
\overline{\overline f}=B_aB_{-a}f=f.
\]

For \(H_s\), this can be read directly:
\[
\overline{H_s}=H_s-aH_1,\qquad
\overline{H_s-aH_1}=(H_s-aH_1)+aH_1=H_s.
\]
The unnormalized Laurent convention similarly uses coefficient inversion \(q\mapsto q^{-1}\) before \(B_q\).

A bar-invariant vector satisfies \(\overline f=f\). The linear transforms are the objects used by the coefficient proofs in Lean; the semilinear formulas express them in the usual Laurent notation.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Hecke.barBasis`: [Hecke.lean:303](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L303).

`OAI.KLInvariance.Hecke.barLinear`: [Hecke.lean:339](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L339).

`OAI.KLInvariance.HeckeQ.barBasis`: [Hecke.lean:790](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L790).

`OAI.KLInvariance.HeckeQ.barLinear`: [Hecke.lean:833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L833).
