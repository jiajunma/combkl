---
id: kl.detail.r_kernel
title: The reciprocal convolution identity for R-polynomials
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.detail.ordinary_r
- kl.definitions.bar_involution
- kl.foundations.finite_intervals
lean:
  repository: openai-kl
  modules:
  - OrdinaryR
  declarations:
  - OAI.KLInvariance.OrdinaryR.polynomial_kernel_reverse
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.OrdinaryR:245
    format: lean-location
    note: OAI.KLInvariance.OrdinaryR.polynomial_kernel_reverse
  - artifact: openai-kl-paper
    locator: Related paper context; sec:introduction
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- hecke_polynomials
---

# The reciprocal convolution identity for R-polynomials

Write \(d(x,z)=\ell(z)-\ell(x)\) for comparable endpoints and
\[
\overline R_{x,z}(q)=q^{d(x,z)}R_{x,z}(q^{-1}).
\]
For every finite Bruhat interval,
\[
\sum_{x\leq z\leq y}\overline R_{x,z}(q)R_{z,y}(q)=\delta_{x,y}.
\]
Terms with noncomparable endpoints vanish. The degree bound on \(R\) ensures that the displayed reflection is a polynomial.

*Proof.*

### Step 1. Work with an invertible formal parameter

Let \(Q\) be the Laurent indeterminate, so \(Q\) is a unit in \(\mathbb Z[Q,Q^{-1}]\). The constructed ordinary R-polynomial evaluated at \(Q\) equals the coefficient R-value of the unnormalized Hecke bar transform.

The coefficient identity for the two inverse bar transforms is
\[
\sum_{x\le z\le y}
R_{x,z}(Q)\,Q^{\ell(y)}Q^{-\ell(z)}
R_{z,y}(Q^{-1})=\delta_{x,y}.
\]
This is the \((x,y)\)-entry of the identity operator obtained by composing the bar transforms at \(Q\) and \(Q^{-1}\). Triangularity removes terms outside \([x,y]\), so the coefficient sum is finite.

### Step 2. Return to polynomial coefficients

Since \(z\le y\),
\(Q^{\ell(y)}Q^{-\ell(z)}=Q^{d(z,y)}\).
The ordinary R-degree bound gives
\(\deg R_{z,y}\le d(z,y)\).
Consequently \(Q^{d(z,y)}R_{z,y}(Q^{-1})\) is the Laurent image of the polynomial \(\operatorname{reflect}_{d(z,y)}R_{z,y}\).

Every term of Step 1 is therefore the image of a polynomial. The embedding \(\mathbb Z[q]\to\mathbb Z[Q,Q^{-1}]\) is injective, so
\[
\sum_{x\le z\le y}R_{x,z}\operatorname{reflect}_{d(z,y)}R_{z,y}
=\delta_{x,y}
\]
holds in the polynomial ring.

### Step 3. Reverse the order of the reflected factor

Reflect this identity in total degree \(d(x,y)\). For each comparable \(z\),
\(d(x,z)+d(z,y)=d(x,y)\).
Using the degree bounds, reflection of the product splits as
\[
\operatorname{reflect}_{d(x,y)}
\bigl(R_{x,z}\operatorname{reflect}_{d(z,y)}R_{z,y}\bigr)
=\operatorname{reflect}_{d(x,z)}R_{x,z}\,R_{z,y}.
\]
Here reflecting the second polynomial twice returns it; this follows term by term from \(q^i\mapsto q^{d(z,y)-i}\).

Reflection distributes over the finite sum. If \(x\ne y\), the right-hand side is zero and stays zero. If \(x=y\), the rank is zero and reflection fixes one. This gives the stated reversed convolution.

For noncomparable \(x,y\), each potential term vanishes by triangularity, and the right-hand side is zero as well.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization



`OAI.KLInvariance.OrdinaryR.polynomial_kernel_reverse`: [OrdinaryR.lean:245](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L245).
