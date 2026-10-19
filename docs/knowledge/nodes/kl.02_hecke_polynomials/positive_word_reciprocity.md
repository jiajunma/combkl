---
id: kl.hecke.positive_word_reciprocity
title: Bruhat support and bar reciprocity for positive Hecke words
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.hecke.positive_words
- kl.hecke.bar_interchange
- kl.hecke.r_parameter_reciprocity
- kl.detail.bruhat_lifting
- kl.foundations.finite_intervals
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  declarations:
  - OAI.KLInvariance.HeckeQ.one_add_leftInv
  - OAI.KLInvariance.HeckeQ.barLinear_positiveWord
  - OAI.KLInvariance.HeckeQ.positiveWord_support
  - OAI.KLInvariance.HeckeQ.positiveWord_rValue
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:944
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.one_add_leftInv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:951
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.barLinear_positiveWord
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:963
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.positiveWord_support
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:997
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.positiveWord_rValue
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual coefficient hypotheses, conventions and source proof retained?
  verdict: Read positiveWord support, barLinear_positiveWord and positiveWord_rValue.
    Kept the arbitrary-word bar identity separate from the reduced-word support hypothesis
    and displayed the coefficient extraction and bottom power.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Bruhat support and bar reciprocity for positive Hecke words

For a unit \(q\) and any word \(\omega\) of length \(m\),
\[
B_qH_\omega(q^{-1})=q^{-m}H_\omega(q).
\]
If \(\omega\) is reduced with product \(b\), then
\[
\operatorname{supp}H_\omega(q)\subseteq\{z:z\le b\},
\]
and, for every \(x\),
\[
\sum_{z\le b}r_q(x,z)h_\omega(z;q)
=q^{-\ell(x)}q^m h_\omega(x;q^{-1}).
\]

*Proof.*

### Step 1. Transform one positive generator

The inverse formula gives
\[
\begin{aligned}
I+L_s(q)^{-1}
&=I+q^{-1}\bigl(L_s(q)-(q-1)I\bigr)\\
&=q^{-1}I+q^{-1}L_s(q)
=q^{-1}(I+L_s(q)).
\end{aligned}
\]
The scalar simplification is \(1-q^{-1}(q-1)=q^{-1}\).

### Step 2. Induct over the word for the bar identity

For the empty word, \(H_{\varnothing}=T_1\), which \(B_q\) fixes. Suppose the identity holds for a tail \(\omega\) of length \(m\).

By linearity and [[node:kl.hecke.bar_interchange|bar intertwining]],
\[
B_qH_{s\omega}(q^{-1})
=(I+L_s(q)^{-1})B_qH_\omega(q^{-1}).
\]
Apply induction and Step 1:
\[
(I+L_s(q)^{-1})q^{-m}H_\omega(q)
=q^{-(m+1)}(I+L_s(q))H_\omega(q)
=q^{-(m+1)}H_{s\omega}(q).
\]
This proves the identity for every word.

### Step 3. Establish support for a reduced word

Induct on the reduced word. The empty-word vector has support contained in \(\{1\}\).

Write the word as \(s\omega\), with reduced tail product \(v\), so \(sv\) is an ascent. If \(h_{s\omega}(x;q)\ne0\), the coefficient recurrence implies that at least one of
\(h_\omega(x;q)\), \(h_\omega(sx;q)\) is nonzero. If both were zero, the displayed recurrence would give zero.

If the first is nonzero, induction gives \(x\le v\le sv\).

If the second is nonzero, induction gives \(sx\le v\). Monotonicity of \(U_s\), together with \(U_s(sx)=U_s(x)\), gives
\[
x\le U_s(x)=U_s(sx)\le U_s(v)=sv.
\]
Thus every nonzero coefficient lies below the new product.

### Step 4. Take a coefficient after replacing q by its inverse

Apply Step 2 with \(q^{-1}\):
\[
B_{q^{-1}}H_\omega(q)=q^mH_\omega(q^{-1}).
\]
For a reduced word, Step 3 lets us expand the left side over the finite set \(z\le b\). Its \(x\)-coefficient is
\[
\sum_{z\le b} b_z(q^{-1})(x)h_\omega(z;q)
=q^m h_\omega(x;q^{-1}).
\]

### Step 5. Substitute the proved R coefficient identity

[[node:kl.hecke.r_parameter_reciprocity|Parameter reciprocity]] gives
\[
r_q(x,z)=q^{-\ell(x)}b_z(q^{-1})(x).
\]
Multiply the equality in Step 4 by \(q^{-\ell(x)}\) and bring that common scalar into the finite sum. This is the required convolution formula.

For the one-letter word and \(x=1\), the left side is
\(r_q(1,1)+r_q(1,s)=1+(q-1)=q\);
the right side is \(q h_s(1;q^{-1})=q\). At \(x=s\), both sides are one.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.HeckeQ.one_add_leftInv`: [CharacterReciprocity.lean:944](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L944).

`OAI.KLInvariance.HeckeQ.barLinear_positiveWord`: [CharacterReciprocity.lean:951](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L951).

`OAI.KLInvariance.HeckeQ.positiveWord_support`: [CharacterReciprocity.lean:963](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L963).

`OAI.KLInvariance.HeckeQ.positiveWord_rValue`: [CharacterReciprocity.lean:997](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L997).
