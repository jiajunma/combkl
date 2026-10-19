---
id: kl.hecke.bar_interchange
title: Parameter interchange and inverse bar transforms
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.definitions.bar_involution
- kl.hecke.word_independence
- kl.detail.hecke_quadratic_identity
lean:
  repository: openai-kl
  modules:
  - Hecke
  declarations:
  - OAI.KLInvariance.Hecke.barBasis_simple_mul_ascent
  - OAI.KLInvariance.Hecke.leftInv_barBasis
  - OAI.KLInvariance.Hecke.barLinear_left
  - OAI.KLInvariance.Hecke.barLinear_leftInv
  - OAI.KLInvariance.Hecke.barLinear_barBasis
  - OAI.KLInvariance.Hecke.barLinear_inverse
  - OAI.KLInvariance.HeckeQ.barBasis_simple_mul_ascent
  - OAI.KLInvariance.HeckeQ.leftInv_barBasis
  - OAI.KLInvariance.HeckeQ.barLinear_left
  - OAI.KLInvariance.HeckeQ.barLinear_leftInv
  - OAI.KLInvariance.HeckeQ.barLinear_barBasis
  - OAI.KLInvariance.HeckeQ.barLinear_inverse
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:309
    format: lean-location
    note: OAI.KLInvariance.Hecke.barBasis_simple_mul_ascent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:322
    format: lean-location
    note: OAI.KLInvariance.Hecke.leftInv_barBasis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:348
    format: lean-location
    note: OAI.KLInvariance.Hecke.barLinear_left
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:358
    format: lean-location
    note: OAI.KLInvariance.Hecke.barLinear_leftInv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:367
    format: lean-location
    note: OAI.KLInvariance.Hecke.barLinear_barBasis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:381
    format: lean-location
    note: OAI.KLInvariance.Hecke.barLinear_inverse
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:796
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.barBasis_simple_mul_ascent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:810
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.leftInv_barBasis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:841
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.barLinear_left
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:848
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.barLinear_leftInv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:862
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.barLinear_barBasis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:876
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.barLinear_inverse
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual coefficient hypotheses, conventions and source proof retained?
  verdict: Read both bar ascent, intertwining and inverse proofs; explained unit multiplication
    order, both descent calculations, inverse-generator intertwining and the reduced-word
    induction.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Parameter interchange and inverse bar transforms

For normalized Hecke operators over \(C\),
\[
B_aL_s(-a)=L_s(a)^{-1}B_a,\qquad B_aB_{-a}=I.
\]
For the unnormalized operators and a unit \(q\),
\[
B_qL_s(q^{-1})=L_s(q)^{-1}B_q,\qquad B_qB_{q^{-1}}=I.
\]

*Proof.*

### Step 1. Compute an ascent of an inverse-basis vector

Suppose \(\ell(sw)=\ell(w)+1\). Inversion preserves length, so appending \(s\) to \(w^{-1}\) is a right ascent. The standard-action identity gives
\[
U_{(sw)^{-1}}=U_{w^{-1}s}=U_{w^{-1}}L_s.
\]
Take inverses and apply to \(e_1\):
\[
b_{sw}=L_s^{-1}U_{w^{-1}}^{-1}e_1=L_s^{-1}b_w.
\]
This applies in either convention.

### Step 2. Compute the normalized descent case

Now suppose \(sw<w\). Step 1 at \(sw\) gives \(b_w(a)=L_s(a)^{-1}b_{sw}(a)\), hence
\(L_s(a)b_w(a)=b_{sw}(a)\).
The inverse formula therefore yields
\[
L_s(a)^{-1}b_w(a)=b_{sw}(a)-ab_w(a).
\]
Combining the ascent and descent cases,
\[
L_s(a)^{-1}b_w(a)
=b_{sw}(a)-a\mathbf1_{sw<w}b_w(a).
\]
This is exactly \(B_a(L_s(-a)e_w)\), by the normalized basis formula and linearity of \(B_a\). Equality on basis vectors proves the first normalized operator identity.

### Step 3. Compute the unnormalized descent case

For \(sw<w\), the same ascent argument gives \(L_s(q)b_w(q)=b_{sw}(q)\). Thus
\[
\begin{aligned}
L_s(q)^{-1}b_w(q)
&=q^{-1}\bigl(b_{sw}(q)-(q-1)b_w(q)\bigr)\\
&=q^{-1}b_{sw}(q)+(q^{-1}-1)b_w(q).
\end{aligned}
\]
This is \(B_q(L_s(q^{-1})e_w)\) in the descent branch. In the ascent branch both expressions equal \(b_{sw}(q)\), by Step 1. This proves the unnormalized intertwining identity.

### Step 4. Intertwine the inverse generators

The normalized identity \(B_aL_s(-a)=L_s(a)^{-1}B_a\) can be multiplied on the left by \(L_s(a)\) and on the right by \(L_s(-a)^{-1}\). It becomes
\[
B_aL_s(-a)^{-1}=L_s(a)B_a.
\]
The same calculation with the unnormalized identity gives
\[
B_qL_s(q^{-1})^{-1}=L_s(q)B_q.
\]
Both multiplications use the two-sided inverses proved by the [[node:kl.detail.hecke_quadratic_identity|quadratic identity]].

### Step 5. Prove inverse composition by reduced-word induction

For normalized parameters, prove \(B_ab_w(-a)=e_w\) by induction on a reduced word for \(w\). At the empty word, \(b_1=e_1\) and \(B_ae_1=e_1\).

Write a nonempty reduced word as \(s\omega\), with tail product \(u\). Then \(su\) is an ascent. By Steps 1 and 4 and the induction hypothesis,
\[
B_ab_{su}(-a)
=B_aL_s(-a)^{-1}b_u(-a)
=L_s(a)B_ab_u(-a)
=L_s(a)e_u=e_{su}.
\]
The last equality is the ascent formula.

For the unnormalized case, replace \(-a\) by \(q^{-1}\) and use the second identity in Step 4. The identical induction gives \(B_qb_w(q^{-1})=e_w\).

### Step 6. Conclude both-sided invertibility

Since \(B_{-a}e_w=b_w(-a)\), Step 5 proves \(B_aB_{-a}=I\). Replacing \(a\) by \(-a\) proves the reverse composite.

Likewise \(B_qB_{q^{-1}}=I\), and replacing \(q\) by \(q^{-1}\) proves \(B_{q^{-1}}B_q=I\). Thus the two parameter transforms are mutually inverse.

On \(T_s\), the calculation is
\[
B_{q^{-1}}T_s=qT_s+(q-1)T_1,
\]
\[
B_q\bigl(qT_s+(q-1)T_1\bigr)
=T_s+(1-q)T_1+(q-1)T_1=T_s.
\]

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Hecke.barBasis_simple_mul_ascent`: [Hecke.lean:309](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L309).

`OAI.KLInvariance.Hecke.leftInv_barBasis`: [Hecke.lean:322](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L322).

`OAI.KLInvariance.Hecke.barLinear_left`: [Hecke.lean:348](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L348).

`OAI.KLInvariance.Hecke.barLinear_leftInv`: [Hecke.lean:358](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L358).

`OAI.KLInvariance.Hecke.barLinear_barBasis`: [Hecke.lean:367](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L367).

`OAI.KLInvariance.Hecke.barLinear_inverse`: [Hecke.lean:381](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L381).

`OAI.KLInvariance.HeckeQ.barBasis_simple_mul_ascent`: [Hecke.lean:796](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L796).

`OAI.KLInvariance.HeckeQ.leftInv_barBasis`: [Hecke.lean:810](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L810).

`OAI.KLInvariance.HeckeQ.barLinear_left`: [Hecke.lean:841](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L841).

`OAI.KLInvariance.HeckeQ.barLinear_leftInv`: [Hecke.lean:848](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L848).

`OAI.KLInvariance.HeckeQ.barLinear_barBasis`: [Hecke.lean:862](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L862).

`OAI.KLInvariance.HeckeQ.barLinear_inverse`: [Hecke.lean:876](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L876).
