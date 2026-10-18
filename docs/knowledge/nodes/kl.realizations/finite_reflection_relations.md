---
id: kl.realization.finite_reflection_relations
title: Finite Coxeter relations for linear reflections
kind: theorem
status: proved
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.realization.linear_reflection
- kl.realization.rank_two_coefficients
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.Realization.reflection_pow_even_eq_one
  - OAI.KLInvariance.Realization.reflection_pow_odd_eq_one
  - OAI.KLInvariance.Realization.geometric_reflection_relation
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:196
    format: lean-location
    note: OAI.KLInvariance.Realization.reflection_pow_even_eq_one
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:207
    format: lean-location
    note: OAI.KLInvariance.Realization.reflection_pow_odd_eq_one
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:225
    format: lean-location
    note: OAI.KLInvariance.Realization.geometric_reflection_relation
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the calculation preserve the local statement and proof route?
  verdict: Checked the general linear-functional hypotheses, even/odd Chebyshev vanishings,
    rank-one normal form, and arbitrary-rank coordinate action.
tags:
- Kazhdan-Lusztig
- realization
---

# Finite Coxeter relations for linear reflections

Let \(V\) be a real vector space, \(\alpha,\beta\in V\), and \(f,g\in V^*\) satisfy
\[
f(\alpha)=g(\beta)=2,\qquad
f(\beta)=g(\alpha)=c=-2\cos(\pi/m),
\]
where \(m\ge2\) is an integer. Define
\[
r(v)=v-f(v)\alpha,\qquad s(v)=v-g(v)\beta.
\]
Then \((rs)^m=1\) on \(V\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same relation, different calculation.**

**OpenAI notes:** The realization lemma verifies the finite Coxeter relation on a positive-definite root plane and its fixed orthogonal complement. [bg:realization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L34).

**Lean (primary):** The local theorem takes two vectors and two linear functionals with specified cross-evaluations. It proves the relation by an operator-power identity and separate even and odd Chebyshev evaluations. [Tits:225](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L225).

**Role in the proof:** The displayed matrix recurrence expands the power calculation. Its even and odd vanishings match the local helper lemmas, and the common fixed space gives the identity on the entire ambient vector space.
<!-- source-comparison:end -->

*Proof.*

### Step 1. The exponent-two case

If \(m=2\), then \(c=0\). Expanding gives
\[
rs(v)=v-g(v)\beta-f(v)\alpha=sr(v).
\]
Both \(r\) and \(s\) square to the identity, so \((rs)^2=r^2s^2=1\).

For the remaining steps assume \(m>2\), and put \(\theta=\pi/m\).

### Step 2. Split off the common fixed space

The determinant \(4-c^2=4\sin^2\theta\) is positive. Thus \(\alpha,\beta\) are independent: applying \(f\) and \(g\) to \(a\alpha+b\beta=0\) gives an invertible system with coefficient matrix
\[
\begin{pmatrix}2&c\\ c&2\end{pmatrix}.
\]
Let \(U=\operatorname{span}\{\alpha,\beta\}\) and \(K=\ker f\cap\ker g\).

For any \(v\in V\), set
\[
a=\frac{2f(v)-cg(v)}{4-c^2},\qquad
b=\frac{2g(v)-cf(v)}{4-c^2}.
\]
These formulas satisfy \(2a+cb=f(v)\) and \(ca+2b=g(v)\). Hence \(v-a\alpha-b\beta\in K\). The same invertible system gives \(U\cap K=0\), so \(V=U\oplus K\).

Both reflections fix \(K\) pointwise and preserve \(U\). It remains to compute their product on \(U\).

### Step 3. The matrix of the product

In the ordered basis \(\alpha,\beta\), the matrices are
\[
r=\begin{pmatrix}-1&-c\\0&1\end{pmatrix},
\qquad
s=\begin{pmatrix}1&0\\-c&-1\end{pmatrix}.
\]
Their product is
\[
Q=\begin{pmatrix}c^2-1&c\\-c&-1\end{pmatrix}.
\]
It has determinant one. Put
\[
z=c^2-2=2\cos(2\theta).
\]
Direct multiplication gives
\[
Q^2=
\begin{pmatrix}
c^4-3c^2+1&c(c^2-2)\\
-c(c^2-2)&1-c^2
\end{pmatrix}
=zQ-I.
\]
In particular \(Q^{-1}=zI-Q\).

### Step 4. The Chebyshev power formula

For \(n\ge1\),
\[
Q^n=S_{n-1}(z)Q-S_{n-2}(z)I.
\]
At \(n=1\) this is \(Q=S_0Q-S_{-1}I\). If it holds at \(n\), multiply by \(Q\), substitute \(Q^2=zQ-I\), and use the recurrence:
\[
\begin{aligned}
Q^{n+1}
 &=S_{n-1}(z)(zQ-I)-S_{n-2}(z)Q\\
 &=S_n(z)Q-S_{n-1}(z)I.
\end{aligned}
\]
The inverse \(Q^{-1}\) satisfies the same quadratic equation, so the same induction also computes \(Q^{-n}\).

Since \(0<2\theta<\pi\), the number \(\sin(2\theta)\) is positive. The trigonometric formula for \(S_n\) can therefore be used at \(z=2\cos(2\theta)\).

### Step 5. Even exponent

If \(m=2k\), then \(k(2\theta)=\pi\). Thus
\[
S_{k-1}(z)=0,\qquad S_{k-2}(z)=1,
\]
because the corresponding sine numerators are \(\sin\pi=0\) and \(\sin(\pi-2\theta)=\sin(2\theta)\). Step 4 gives \(Q^k=-I\), and hence \(Q^{2k}=I\).

This is the vanishing condition \(S_{k-1}(z)=0\) used in the source's even-power calculation.

### Step 6. Odd exponent

If \(m=2k+1\), then
\[
(k+1)2\theta=\pi+\theta,\qquad k\,2\theta=\pi-\theta.
\]
Their sine values are opposites, so
\[
S_k(z)+S_{k-1}(z)=0.
\]
Write \(u=S_{k-1}(z)\) and \(v=S_{k-2}(z)\). The recurrence and the last equality give \(S_k(z)=-u\) and \(v=(z+1)u\).

The power formula gives
\[
Q^{k+1}=-u(Q+I).
\]
Applying the same formula to the inverse, and using \(Q^{-1}=zI-Q\), gives
\[
Q^{-k}=uQ^{-1}-vI
      =u(zI-Q)-(z+1)uI
      =-u(Q+I).
\]
Therefore \(Q^{k+1}=Q^{-k}\). Multiplying by \(Q^k\) proves \(Q^{2k+1}=I\).

This is the vanishing condition \(S_k(z)+S_{k-1}(z)=0\) used in the source's odd-power calculation.

### Step 7. Recover the operator on the whole space

The product has \(m\)-th power equal to the identity on \(U\) by Steps 5–6 and on \(K\) because each reflection fixes \(K\). The direct-sum decomposition in Step 2 therefore gives \((rs)^m=1\) on all of \(V\).

## References

The local source statements and calculations are listed below.

## Lean formalization

`OAI.KLInvariance.Realization.reflection_pow_even_eq_one`: [Tits.lean:196](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L196).

`OAI.KLInvariance.Realization.reflection_pow_odd_eq_one`: [Tits.lean:207](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L207).

`OAI.KLInvariance.Realization.geometric_reflection_relation`: [Tits.lean:225](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L225).

The source invokes the library reflection-power identity in its even and odd helper lemmas. Steps 2–4 expand that identity using coordinates on the two-root span; Steps 5–6 use the same Chebyshev vanishing conditions as those helpers. The exponent-two case is expanded separately in both proofs.
