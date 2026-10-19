---
id: kl.hecke.r_parameter_reciprocity
title: Signed parameter reciprocity and the inverse-parameter bar coefficient
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.hecke.r_values
- kl.hecke.r_value_recursion
lean:
  repository: openai-kl
  modules:
  - Dihedral
  declarations:
  - OAI.KLInvariance.HeckeQ.dualR
  - OAI.KLInvariance.HeckeQ.dualR_diagonal
  - OAI.KLInvariance.HeckeQ.dualR_zero
  - OAI.KLInvariance.HeckeQ.dualR_recursion
  - OAI.KLInvariance.HeckeQ.rValue_eq_dualR
  - OAI.KLInvariance.HeckeQ.rValue_inverse_eq_barBasis
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:387
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.dualR
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:390
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.dualR_diagonal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:395
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.dualR_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:399
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.dualR_recursion
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:440
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.rValue_eq_dualR
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:467
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.rValue_inverse_eq_barBasis
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual coefficient hypotheses, conventions and source proof retained?
  verdict: Read dualR and all four reciprocity lemmas in Dihedral. Expanded the matching
    recurrences, strong-induction base, and cancellation of all sign and unit powers
    in the bar coefficient identity.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Signed parameter reciprocity and the inverse-parameter bar coefficient

Let \(q\) be a unit in a commutative ring. The actual R-values satisfy
\[
r_q(x,y)=(-q)^{\ell(y)}(-q^{-1})^{\ell(x)}r_{q^{-1}}(x,y).
\]
Consequently
\[
r_{q^{-1}}(x,y)=q^{\ell(x)}b_y(q)(x).
\]
For comparable endpoints the first equality can also be written
\(r_q(x,y)=(-1)^{\ell(y)-\ell(x)}q^{\ell(y)-\ell(x)}r_{q^{-1}}(x,y)\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Algebraic construction behind the polynomial conventions.**

**OpenAI notes:** The conventions specify the ordinary R descent recurrence. The reflection-order path theorem introduces the normalized family through path counting and states its square-parameter relation to ordinary R. [sec:introduction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1), [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185).

**Lean (primary):** The regular operators are built from Coxeter length. Left/right commutation and the cyclic identity vector prove reduced-word independence. Inverse operators define R-values; their recurrence proves polynomiality, and a second matching-recurrence argument proves signed parameter reciprocity. [Hecke:705](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L705), [Hecke:1000](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L1000), [OrdinaryR:31](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L31), [Dihedral:440](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L440).

**Role in the proof:** The KB develops these algebraic constructions before the geometric path formula. The recurrence and inverse-parameter coefficient identities used by the character argument follow from the constructed operators.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Define the comparison family

Set
\[
D_q(x,y)=(-q)^{\ell(y)}(-q^{-1})^{\ell(x)}r_{q^{-1}}(x,y).
\]
On the diagonal, the two scalar powers multiply to one, so \(D_q(x,x)=1\). Outside Bruhat order, the last factor is zero.

We prove that \(D_q\) satisfies the same recurrence as \(r_q\).

### Step 2. Compute simultaneous descents

Let \(sy<y\), and suppose \(sx<x\). Put \(m=\ell(sx)\), \(n=\ell(sy)\). The inverse-parameter recurrence is
\(r_{q^{-1}}(x,y)=r_{q^{-1}}(sx,sy)\).
Therefore
\[
D_q(x,y)
=(-q)^{n+1}(-q^{-1})^{m+1}r_{q^{-1}}(sx,sy)
=D_q(sx,sy),
\]
because the additional product \((-q)(-q^{-1})\) is one.

### Step 3. Compute the ascent branch

Suppose \(sx>x\), put \(v=sy\), and let
\(A=(-q)^{\ell(v)}(-q^{-1})^{\ell(x)}\).
The inverse-parameter recurrence gives
\[
\begin{aligned}
D_q(x,y)
&=(-q)A\bigl((q^{-1}-1)r_{q^{-1}}(x,v)
             +q^{-1}r_{q^{-1}}(sx,v)\bigr)\\
&=(q-1)A r_{q^{-1}}(x,v)-A r_{q^{-1}}(sx,v).
\end{aligned}
\]
The first term is \((q-1)D_q(x,v)\). Since \(\ell(sx)=\ell(x)+1\),
\[
qD_q(sx,v)=q(-q^{-1})A r_{q^{-1}}(sx,v)
=-A r_{q^{-1}}(sx,v).
\]
This proves the required recurrence in the second case.

### Step 4. Identify the two families by induction

Induct strongly on \(\ell(y)\), for all \(x\). At \(y=1\), the diagonal is one and every other bottom label gives zero, for both families.

For \(y\ne1\), choose a left descent. Both recurrences have identical coefficients and use only the shorter upper endpoint \(sy\). Induction identifies their values at \((x,sy)\) and \((sx,sy)\), hence at \((x,y)\). Thus \(r_q=D_q\).

### Step 5. Extract the inverse-parameter coefficient

Apply Step 4 with parameter \(q^{-1}\) and expand the definition of \(r_q\):
\[
\begin{aligned}
r_{q^{-1}}(x,y)
&=(-q^{-1})^{\ell(y)}(-q)^{\ell(x)}r_q(x,y)\\
&=(-q^{-1})^{\ell(y)}(-q)^{\ell(x)}
  (-1)^{\ell(x)}(-q)^{\ell(y)}b_y(q)(x)\\
&=q^{\ell(x)}b_y(q)(x).
\end{aligned}
\]
The top powers cancel because \((-q^{-1})(-q)=1\); the bottom factors satisfy \((-q)(-1)=q\). This is the coefficient identity used in positive-word convolution.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.HeckeQ.dualR`: [Dihedral.lean:387](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L387).

`OAI.KLInvariance.HeckeQ.dualR_diagonal`: [Dihedral.lean:390](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L390).

`OAI.KLInvariance.HeckeQ.dualR_zero`: [Dihedral.lean:395](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L395).

`OAI.KLInvariance.HeckeQ.dualR_recursion`: [Dihedral.lean:399](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L399).

`OAI.KLInvariance.HeckeQ.rValue_eq_dualR`: [Dihedral.lean:440](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L440).

`OAI.KLInvariance.HeckeQ.rValue_inverse_eq_barBasis`: [Dihedral.lean:467](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L467).
