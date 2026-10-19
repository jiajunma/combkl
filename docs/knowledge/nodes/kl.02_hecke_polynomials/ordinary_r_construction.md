---
id: kl.hecke.ordinary_r_construction
title: Polynomiality, specialization and descent of ordinary R-values
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.detail.ordinary_r
- kl.hecke.r_value_recursion
- kl.hecke.r_values
- kl.coxeter.word_data
lean:
  repository: openai-kl
  modules:
  - OrdinaryR
  declarations:
  - OAI.KLInvariance.OrdinaryR.rValue_polynomial
  - OAI.KLInvariance.OrdinaryR.toLaurent_polynomial
  - OAI.KLInvariance.OrdinaryR.polynomial_diagonal
  - OAI.KLInvariance.OrdinaryR.polynomial_zero
  - OAI.KLInvariance.OrdinaryR.polynomial_recursion
  - OAI.KLInvariance.OrdinaryR.polynomial_eval
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.OrdinaryR:31
    format: lean-location
    note: OAI.KLInvariance.OrdinaryR.rValue_polynomial
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.OrdinaryR:65
    format: lean-location
    note: OAI.KLInvariance.OrdinaryR.toLaurent_polynomial
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.OrdinaryR:70
    format: lean-location
    note: OAI.KLInvariance.OrdinaryR.polynomial_diagonal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.OrdinaryR:75
    format: lean-location
    note: OAI.KLInvariance.OrdinaryR.polynomial_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.OrdinaryR:80
    format: lean-location
    note: OAI.KLInvariance.OrdinaryR.polynomial_recursion
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.OrdinaryR:93
    format: lean-location
    note: OAI.KLInvariance.OrdinaryR.polynomial_eval
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual coefficient hypotheses, conventions and source proof retained?
  verdict: Read polynomiality, Laurent truncation, every-descent recurrence and polynomial_eval.
    Both inductions include all lower labels, diagonal/support base cases and the
    smaller upper endpoint.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Polynomiality, specialization and descent of ordinary R-values

The Laurent R-value \(r_Q(x,y)\) is the image of an integral polynomial. Its polynomial representative \(R_{x,y}\) has diagonal one, vanishes outside Bruhat order, and satisfies the ordinary descent recurrence for every left descent of \(y\).

For every unit \(q_0\) in any commutative ring,
\[
R_{x,y}(q_0)=r_{q_0}(x,y).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Algebraic construction behind the polynomial conventions.**

**OpenAI notes:** The conventions specify the ordinary R descent recurrence. The reflection-order path theorem introduces the normalized family through path counting and states its square-parameter relation to ordinary R. [sec:introduction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1), [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185).

**Lean (primary):** The regular operators are built from Coxeter length. Left/right commutation and the cyclic identity vector prove reduced-word independence. Inverse operators define R-values; their recurrence proves polynomiality, and a second matching-recurrence argument proves signed parameter reciprocity. [Hecke:705](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L705), [Hecke:1000](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L1000), [OrdinaryR:31](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L31), [Dihedral:440](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L440).

**Role in the proof:** The KB develops these algebraic constructions before the geometric path formula. The recurrence and inverse-parameter coefficient identities used by the character argument follow from the constructed operators.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Set the polynomiality induction

Induct strongly on \(\ell(y)\), with the statement for every lower label \(x\). We seek a polynomial \(p\) whose Laurent image is \(r_Q(x,y)\).

When \(y=1\), use \(p=1\) if \(x=1\). If \(x\ne1\), then \(x\not\le1\): Bruhat comparison would imply \(\ell(x)\le0\), hence \(x=1\). The support theorem gives \(r_Q(x,1)=0\), so use \(p=0\).

### Step 2. Construct the polynomial in a descent step

For \(y\ne1\), a reduced word supplies a left descent \(s\). Put \(v=sy\), so \(\ell(v)<\ell(y)\).

Induction supplies polynomials \(p,r\) whose Laurent images are \(r_Q(x,v)\) and \(r_Q(sx,v)\). If \(sx<x\), the [[node:kl.hecke.r_value_recursion|R-value recurrence]] identifies \(r_Q(x,y)\) with the image of \(r\).

If \(sx>x\), the recurrence identifies it with the image of
\[
(q-1)p(q)+q\,r(q).
\]
This expression uses only nonnegative powers. Thus both branches provide the required polynomial and complete the induction.

### Step 3. Identify the source's truncation definition

If \(r_Q(x,y)=p(Q)\), truncating its Laurent series to nonnegative exponents returns \(p\), coefficient by coefficient. Therefore the source's definition has
\[
R_{x,y}(Q)=r_Q(x,y).
\]
This equality also shows that the representative is unique.

### Step 4. Transfer initial values and every descent recurrence

The Laurent image of \(R_{x,x}\) is one, so injectivity of the polynomial inclusion gives \(R_{x,x}=1\). The support case similarly gives \(R_{x,y}=0\).

For any left descent \(s\), apply the [[node:kl.hecke.r_value_recursion|R-value recurrence]] at \(Q\). Replace every R-value by its polynomial image. Inclusion preserves addition and multiplication, so injectivity gives exactly the displayed polynomial recurrence.

### Step 5. Prove specialization by a second induction

Fix \(q_0\in C^\times\). Induct on \(\ell(y)\), again for all \(x\). At \(y=1\), the diagonal/support cases give the same value on both sides.

For \(y\ne1\), choose \(s\) with \(sy<y\). The polynomial recurrence evaluates to
\[
R_{x,y}(q_0)=
\begin{cases}
R_{sx,sy}(q_0),&sx<x,\\
(q_0-1)R_{x,sy}(q_0)+q_0R_{sx,sy}(q_0),&sx>x.
\end{cases}
\]
Use induction at \((sx,sy)\) and \((x,sy)\). The right-hand side becomes the [[node:kl.hecke.r_value_recursion|R-value recurrence]] at \(q_0\), which equals \(r_{q_0}(x,y)\). This proves specialization.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.OrdinaryR.rValue_polynomial`: [OrdinaryR.lean:31](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L31).

`OAI.KLInvariance.OrdinaryR.toLaurent_polynomial`: [OrdinaryR.lean:65](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L65).

`OAI.KLInvariance.OrdinaryR.polynomial_diagonal`: [OrdinaryR.lean:70](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L70).

`OAI.KLInvariance.OrdinaryR.polynomial_zero`: [OrdinaryR.lean:75](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L75).

`OAI.KLInvariance.OrdinaryR.polynomial_recursion`: [OrdinaryR.lean:80](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L80).

`OAI.KLInvariance.OrdinaryR.polynomial_eval`: [OrdinaryR.lean:93](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L93).
