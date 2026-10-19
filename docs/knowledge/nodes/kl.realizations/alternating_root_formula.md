---
id: kl.realization.alternating_root_formula
title: Root coordinates along an alternating word
kind: theorem
status: proved
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.coxeter.alternating_words
- kl.coxeter.reduced_alternating_tail
- kl.realization.rank_two_coefficients
- kl.realization.geometric_action
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.alternating_root
  - OAI.KLInvariance.TitsSpace.pair_image_nonneg
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:838
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.alternating_root
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:919
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.pair_image_nonneg
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are all action, sign, and length conventions retained?
  verdict: Read the finite-rank Tits proofs, the exact two-generator tail convention,
    and both group-action directions; the chosen smaller induction instance is explicit.
tags:
- Kazhdan-Lusztig
- root-geometry
---

# Root coordinates along an alternating word

Let \(\rho_0\) be the geometric action of a finite-generator Coxeter system. For indices \(i,j\), let \(a_n(i,j)\) be the alternating word of length \(n\) ending in \(j\), and put
\[
c_n=S_n(2\cos(\pi/m_{ij})).
\]
Then
\[
\rho_0(\operatorname{prod}a_n(i,j))\alpha_i=
\begin{cases}
c_n\alpha_i+c_{n-1}\alpha_j,&n\text{ even},\\
c_{n-1}\alpha_i+c_n\alpha_j,&n\text{ odd}.
\end{cases}
\]

Suppose in addition \(i\ne j\), both \(\rho_0(u)\alpha_i\) and \(\rho_0(u)\alpha_j\) are coordinatewise nonnegative, and \(\omega\) uses only \(i,j\) with \(\omega[i]\) reduced. Then
\[
\rho_0(u\,\operatorname{prod}\omega)\alpha_i
\]
is coordinatewise nonnegative.

*Proof.*

### Step 1. The initial coefficients and simple actions

Write \(c=2\cos(\pi/m_{ij})\), with \(c=2\) for an infinite exponent. The coefficient recurrence is
\[
c_{-1}=0,\quad c_0=1,\quad c_{n+1}=cc_n-c_{n-1}.
\]
The simple-action formula gives
\[
s_j\alpha_i=\alpha_i+c\alpha_j,\qquad s_j\alpha_j=-\alpha_j,
\]
and the analogous formulas with \(i,j\) interchanged.

For \(n=0\), the word is empty, so its action gives \(\alpha_i=c_0\alpha_i+c_{-1}\alpha_j\).

### Step 2. The even-to-odd induction step

When \(n\) is even, the next alternating word is obtained by prepending \(j\). Apply \(s_j\) to the induction formula:
\[
s_j(c_n\alpha_i+c_{n-1}\alpha_j)
=c_n\alpha_i+(cc_n-c_{n-1})\alpha_j
=c_n\alpha_i+c_{n+1}\alpha_j.
\]
This is the formula for the odd length \(n+1\).

### Step 3. The odd-to-even induction step

When \(n\) is odd, prepend \(i\). Then
\[
s_i(c_{n-1}\alpha_i+c_n\alpha_j)
=(cc_n-c_{n-1})\alpha_i+c_n\alpha_j
=c_{n+1}\alpha_i+c_n\alpha_j.
\]
This is the formula for even length \(n+1\). The two cases complete induction.

### Step 4. Place a reduced tail in the nonnegative range

Put \(n=|\omega|\). The reduced-tail theorem identifies \(\omega=a_n(i,j)\). If \(m=m_{ij}\) is finite, it gives \(n+1\le m\). The coefficient nonnegativity calculation therefore applies to both \(c_n\) and \(c_{n-1}\).

For an infinite exponent, these coefficients are \(n+1\) and \(n\), again nonnegative.

### Step 5. Apply the positive prefix

Apply \(\rho_0(u)\) to the appropriate formula. The result is a nonnegative linear combination of \(\rho_0(u)\alpha_i\) and \(\rho_0(u)\alpha_j\). Both have nonnegative coordinates by hypothesis, so every coordinate of the combination is nonnegative.

## References

The local action and sign calculations are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.alternating_root`: [Tits.lean:838](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L838).

`OAI.KLInvariance.TitsSpace.pair_image_nonneg`: [Tits.lean:919](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L919).
