---
id: kl.hecke.dihedral_bar_sum
title: The bar eigenvalue of a dihedral lower-interval sum
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.hecke.dihedral_sum_product
- kl.hecke.lower_interval_sums
- kl.coxeter.dihedral_reduced_words
- kl.hecke.bar_interchange
- kl.detail.hecke_quadratic_identity
lean:
  repository: openai-kl
  modules:
  - Dihedral
  declarations:
  - OAI.KLInvariance.Dihedral.plus_leftInv
  - OAI.KLInvariance.Dihedral.bar_lowerSum_alt
  - OAI.KLInvariance.Dihedral.bar_lowerSum
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:509
    format: lean-location
    note: OAI.KLInvariance.Dihedral.plus_leftInv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:517
    format: lean-location
    note: OAI.KLInvariance.Dihedral.bar_lowerSum_alt
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:557
    format: lean-location
    note: OAI.KLInvariance.Dihedral.bar_lowerSum
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the reduced-word, coefficient and interval
    hypotheses?
  verdict: Read bar_lowerSum_alt and bar_lowerSum. Kept the coefficient-linear transform
    and the product recurrence at q inverse, including the zero correction at length
    two and both smaller induction instances.
tags:
- Kazhdan-Lusztig
- dihedral
---

# The bar eigenvalue of a dihedral lower-interval sum

For a rank-two Coxeter system and a unit \(q\) in a commutative ring,
\[
B_qS_w=q^{-\ell(w)}S_w.
\]
Here \(B_q\) is the coefficient-linear unnormalized bar transform.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The same string calculation in two normalizations.**

**OpenAI notes:** The notes use \(C_w^\circ=q^{-\ell(w)/2}S_w\). Their product has a zero correction at length two and the shorter-prefix vector at longer lengths; induction proves semilinear bar invariance. [loc:dihedral-product](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L49), [loc:dihedral-kl](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L29).

**Lean (primary):** The finite sum S_w has coefficient one below w. The product is S_w plus q times the correction vector. Lean applies the coefficient-linear bar map to the product formula at the inverse unit parameter and cancels the common correction term. [Dihedral:217](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L217), [Dihedral:336](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L336), [Dihedral:517](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L517).

**Role in the proof:** Writing \(q=v^2\) and \(C_w^\circ=v^{-\ell(w)}S_w\) converts the two product formulas and bar statements directly. The explicit double-string theorem includes the finite longest-element case.
<!-- source-comparison:end -->

*Proof.*

### Step 1. State the reduced-word induction

Prove the formula for the product of every reduced \(\omega_i(m)\), by strong induction on \(m\), allowing either first index.

At \(m=0\), the sum is \(S_1=T_1\), and \(B_qT_1=T_1\).

At \(m=1\), it is \(S_s=T_1+T_s\). The simple bar vector gives
\[
B_qS_s=T_1+q^{-1}T_s+(q^{-1}-1)T_1
=q^{-1}(T_1+T_s).
\]

### Step 2. Supply both smaller induction instances

For \(m=n+2\), use \(w,v,p,C=C_{i,n}\) from the [[node:kl.hecke.dihedral_sum_product|product recurrence]]. The tail \(v\) has reduced length \(n+1<m\), so induction gives
\[
B_qS_v=q^{-(n+1)}S_v.
\]

If \(n>0\), the prefix \(p\) is reduced with length \(n<m\), giving \(B_qC=q^{-n}C\). If \(n=0\), then \(C=0\), and this same equation holds because both sides are zero.

### Step 3. Apply the linear bar to the inverse-parameter recurrence

Use the [[node:kl.hecke.dihedral_sum_product|product recurrence]] at parameter \(q^{-1}\):
\[
(I+L_s(q^{-1}))S_v=S_w+q^{-1}C.
\]
Applying the linear map \(B_q\), and using its intertwining identity, gives
\[
(I+L_s(q)^{-1})B_qS_v
=B_qS_w+q^{-1}B_qC.
\]
The coefficient \(q^{-1}\) is retained by this linear map.

### Step 4. Simplify the left side with the original [[node:kl.hecke.dihedral_sum_product|product recurrence]]

The [[node:kl.detail.hecke_quadratic_identity|quadratic inverse formula]] gives
\[
\begin{aligned}
I+L_s(q)^{-1}
&=I+q^{-1}\bigl(L_s(q)-(q-1)I\bigr)\\
&=\bigl(1-q^{-1}(q-1)\bigr)I+q^{-1}L_s(q)\\
&=q^{-1}(I+L_s(q)).
\end{aligned}
\]
Here \(1-q^{-1}(q-1)=q^{-1}\), using \(q^{-1}q=1\).
Substitute it and Step 2 into the left side:
\[
\begin{aligned}
(I+L_s(q)^{-1})B_qS_v
&=q^{-(n+2)}(I+L_s(q))S_v\\
&=q^{-(n+2)}(S_w+qC)\\
&=q^{-(n+2)}S_w+q^{-(n+1)}C.
\end{aligned}
\]

The right side of Step 3 becomes
\[
B_qS_w+q^{-1}q^{-n}C
=B_qS_w+q^{-(n+1)}C.
\]
Subtract the identical correction term from the two sides. This yields
\(B_qS_w=q^{-(n+2)}S_w\), completing induction.

### Step 5. Pass from a reduced word to any element

Every element has a reduced alternating expression of length \(\ell(w)\). Apply the proven formula to that expression to obtain the statement for every \(w\).

### Step 6. Express the normalized bar-invariant vector

Over Laurent coefficients with \(q=v^2\), put
\[
C_w^\circ=v^{-\ell(w)}S_w.
\]
The coefficient involution sends \(v^{-\ell(w)}\) to \(v^{\ell(w)}\). Since the coefficients of \(S_w\) are integers, its semilinear bar equals \(B_qS_w\). Thus
\[
\overline{C_w^\circ}
=v^{\ell(w)}v^{-2\ell(w)}S_w
=v^{-\ell(w)}S_w=C_w^\circ.
\]
This is the normalization of the bar calculation used in the OpenAI notes.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.plus_leftInv`: [Dihedral.lean:509](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L509).

`OAI.KLInvariance.Dihedral.bar_lowerSum_alt`: [Dihedral.lean:517](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L517).

`OAI.KLInvariance.Dihedral.bar_lowerSum`: [Dihedral.lean:557](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L557).
