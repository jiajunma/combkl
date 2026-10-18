---
id: kl.realization.orthogonal_rank_one
title: Orthogonal operators with a one-dimensional moving space
kind: theorem
status: proved
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.realization.moving_spaces
- kl.realization.radical_extension
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.Realization.orthogonal_rank_one_form
  - OAI.KLInvariance.Realization.orthogonal_finrank_one
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:111
    format: lean-location
    note: OAI.KLInvariance.Realization.orthogonal_rank_one_form
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:153
    format: lean-location
    note: OAI.KLInvariance.Realization.orthogonal_finrank_one
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

# Orthogonal operators with a one-dimensional moving space

Let \(B\) be a symmetric nondegenerate bilinear form on a real vector space \(V\). Suppose \(g:V\to V\) is invertible and linear, preserves \(B\), and has one-dimensional moving space. Then there is \(u\in V\) with \(B(u,u)\ne0\) such that
\[
g(v)=v-\frac{2B(u,v)}{B(u,u)}u
\]
for every \(v\). In particular, \(g^2=1\).

*Proof.*

### Step 1. Write the rank-one change using a functional

Choose a nonzero basis vector \(u\) of \(\operatorname{Mov}(g)\). Each value of \(g-1\) is a unique scalar multiple of \(u\). Taking that coordinate defines a linear functional \(f\) such that
\[
g(v)=v+f(v)u.
\]
The functional is nonzero, since otherwise the moving space would be zero. Choose \(z\) with \(f(z)=1\), by rescaling any vector on which \(f\) is nonzero.

### Step 2. Identify the normal functional

For \(h\in\ker f\), one has \(g(h)=h\) and \(g(z)=z+u\). Preservation of the form gives
\[
B(z+u,h)=B(z,h),
\]
so \(B(u,h)=0\).

For arbitrary \(v\), the vector \(v-f(v)z\) lies in \(\ker f\). Thus
\[
B(u,v)=f(v)B(u,z).
\]
Put \(c=B(u,z)\). If \(c=0\), this equation would give \(B(u,v)=0\) for every \(v\); nondegeneracy would imply \(u=0\). Hence \(c\ne0\).

### Step 3. Determine the coefficient on the moving vector

Preservation of the norm of \(z\) gives
\[
B(z+u,z+u)=B(z,z).
\]
Expanding and using symmetry yields
\[
2c+B(u,u)=0.
\]
On the other hand, Step 2 with \(v=u\) gives \(B(u,u)=cf(u)\). Since \(c\ne0\),
\[
f(u)=-2,\qquad B(u,u)=-2c\ne0.
\]

### Step 4. Obtain the reflection formula and involutivity

Step 2 and \(B(u,u)=-2c\) give
\[
f(v)=\frac{B(u,v)}c=-\frac{2B(u,v)}{B(u,u)}.
\]
Substitution into \(g(v)=v+f(v)u\) proves the stated formula.

Also
\[
f(g(v))=f(v)+f(v)f(u)=-f(v).
\]
Applying \(g\) a second time therefore gives
\[
g^2(v)=v+f(v)u+f(g(v))u=v.
\]

## References

The local source statements and calculations are listed below.

## Lean formalization

`OAI.KLInvariance.Realization.orthogonal_rank_one_form`: [Tits.lean:111](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L111).

`OAI.KLInvariance.Realization.orthogonal_finrank_one`: [Tits.lean:153](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L153).
