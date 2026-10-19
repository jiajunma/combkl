---
id: kl.hecke.dihedral_sum_product
title: The product recurrence for dihedral lower-interval sums
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.hecke.lower_interval_sums
- kl.hecke.dihedral_strings
- kl.detail.hecke_quadratic_identity
- kl.definitions.hecke_operators
lean:
  repository: openai-kl
  modules:
  - Dihedral
  declarations:
  - OAI.KLInvariance.Dihedral.left_plus_coeff
  - OAI.KLInvariance.Dihedral.lowerSum_product
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:287
    format: lean-location
    note: OAI.KLInvariance.Dihedral.left_plus_coeff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:336
    format: lean-location
    note: OAI.KLInvariance.Dihedral.lowerSum_product
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the reduced-word, coefficient and interval
    hypotheses?
  verdict: Read lowerSum_product and its coefficient cases. Presented the same finite
    membership calculation as a string partition with explicit operator values, union
    and double-membership inputs.
tags:
- Kazhdan-Lusztig
- dihedral
---

# The product recurrence for dihedral lower-interval sums

Let \(q\) be a unit in a commutative ring. Use a reduced alternating word \(\omega_i(n+2)\) and its data \(w,v,p,C_{i,n}\). For \(s=s_i\),
\[
(I+L_s(q))S_v=S_w+qC_{i,n}.
\]
Equivalently,
\[
(I+L_s(q))S_v=
\begin{cases}
S_w,&n=0,\\
S_w+qS_p,&n>0.
\end{cases}
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The same string calculation in two normalizations.**

**OpenAI notes:** The notes use \(C_w^\circ=q^{-\ell(w)/2}S_w\). Their product has a zero correction at length two and the shorter-prefix vector at longer lengths; induction proves semilinear bar invariance. [loc:dihedral-product](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L49), [loc:dihedral-kl](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L29).

**Lean (primary):** The finite sum S_w has coefficient one below w. The product is S_w plus q times the correction vector. Lean applies the coefficient-linear bar map to the product formula at the inverse unit parameter and cancels the common correction term. [Dihedral:217](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L217), [Dihedral:336](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L336), [Dihedral:517](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L517).

**Role in the proof:** Writing \(q=v^2\) and \(C_w^\circ=v^{-\ell(w)}S_w\) converts the two product formulas and bar statements directly. The explicit double-string theorem includes the finite longest-element case.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Partition the basis labels into strings

The map \(r\mapsto sr\) is an involution with no fixed point, since simple multiplication changes length by one. It partitions the group into pairs \(\{r,sr\}\).

In each pair, choose \(r\) to be the shorter member. Then \(r<sr\). Since \([1,v]\) is a lower ideal, it can meet this pair in exactly one of three ways: neither member, just \(r\), or both members.

Only finitely many pairs meet the finite lower ideal, so the following contributions form a finite sum.

### Step 2. Compute a singly included string

If only \(r\) lies below \(v\), the input contribution is \(T_r\). It is an ascent for left multiplication, so
\[
(I+L_s(q))T_r=T_r+T_{sr}.
\]
Both members occur with coefficient one.

### Step 3. Compute a doubly included string

If both members lie below \(v\), the input contribution is \(T_r+T_{sr}\). The two operator values are
\[
L_s(q)T_r=T_{sr},\qquad
L_s(q)T_{sr}=qT_r+(q-1)T_{sr}.
\]
Adding the original vector gives
\[
\begin{aligned}
(I+L_s(q))(T_r+T_{sr})
&=T_r+T_{sr}+T_{sr}+qT_r+(q-1)T_{sr}\\
&=(1+q)(T_r+T_{sr}).
\end{aligned}
\]
Thus every member contributes its coefficient one plus an additional \(q\).

A pair with neither member present contributes zero.

### Step 4. Identify the coefficient-one contribution

The union of all strings meeting \([1,v]\) consists of the \(x\) such that \(x\le v\) or \(sx\le v\). The [[node:kl.hecke.dihedral_strings|string-union theorem]] identifies this set with \([1,w]\).

Therefore the coefficient-one contributions from Steps 2–3 sum to \(S_w\).

### Step 5. Identify the additional q contribution

A basis label receives an extra \(q\) exactly when both \(x\le v\) and \(sx\le v\). The [[node:kl.hecke.dihedral_strings|double-membership theorem]] identifies this set with the empty set for \(n=0\), and with \([1,p]\) for \(n>0\).

Its indicator vector is precisely \(C_{i,n}\). The additional contribution is \(qC_{i,n}\), proving the recurrence.

For a reduced word \(sts\), the only doubled string is \(\{1,s\}\), so
\[
(I+L_s(q))S_{ts}=S_{sts}+q(T_1+T_s).
\]

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.left_plus_coeff`: [Dihedral.lean:287](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L287).

`OAI.KLInvariance.Dihedral.lowerSum_product`: [Dihedral.lean:336](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L336).
