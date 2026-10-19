---
id: kl.hecke.r_value_recursion
title: The ordinary descent recurrence at every unit parameter
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.hecke.r_values
- kl.hecke.bar_interchange
- kl.hecke.bar_triangularity
lean:
  repository: openai-kl
  modules:
  - Hecke
  declarations:
  - OAI.KLInvariance.HeckeQ.rValue_recursion
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:1000
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.rValue_recursion
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual coefficient hypotheses, conventions and source proof retained?
  verdict: Read rValue_recursion and its coefficient input. Displayed both scalar
    normalizations with exact length shifts and explained why every left descent is
    valid.
tags:
- Kazhdan-Lusztig
- Hecke
---

# The ordinary descent recurrence at every unit parameter

Let \(q\) be a unit in a commutative ring. If \(s\) is a simple reflection with \(sy<y\), then for every \(x\),
\[
r_q(x,y)=
\begin{cases}
r_q(sx,sy),&sx<x,\\
(q-1)r_q(x,sy)+q\,r_q(sx,sy),&sx>x.
\end{cases}
\]
Every left descent of \(y\) satisfies this identity.

*Proof.*

### Step 1. Express the longer bar vector through the shorter one

Put \(v=sy\), so \(sv=y\) is an ascent and \(\ell(v)=\ell(y)-1\). The [[node:kl.hecke.bar_interchange|bar ascent formula]] gives
\(b_y(q)=L_s(q)^{-1}b_v(q)\).

Write \(c_x=b_v(q)(x)\) and \(c_{sx}=b_v(q)(sx)\). The [[node:kl.hecke.bar_triangularity|inverse-coefficient formula]] gives
\[
b_y(q)(x)=
\begin{cases}
q^{-1}c_{sx},&sx<x,\\
c_{sx}+(q^{-1}-1)c_x,&sx>x.
\end{cases}
\]

### Step 2. Normalize the simultaneous descent case

Suppose \(sx<x\). Put \(m=\ell(sx)\) and \(n=\ell(v)\). Then \(\ell(x)=m+1\) and \(\ell(y)=n+1\). Therefore
\[
\begin{aligned}
r_q(x,y)
&=(-1)^{m+1}(-q)^{n+1}q^{-1}c_{sx}\\
&=(-1)^m(-q)^n\bigl((-1)(-q)q^{-1}\bigr)c_{sx}\\
&=(-1)^m(-q)^nc_{sx}=r_q(sx,v).
\end{aligned}
\]
The scalar in parentheses is one.

### Step 3. Normalize the ascent case at the lower endpoint

Suppose \(sx>x\). Put \(m=\ell(x)\) and \(n=\ell(v)\), so \(\ell(sx)=m+1\) and \(\ell(y)=n+1\). Let
\(A=(-1)^m(-q)^n\).
Then
\[
r_q(x,y)=(-q)A\bigl(c_{sx}+(q^{-1}-1)c_x\bigr).
\]
The \(c_x\)-term is
\[
(-q)(q^{-1}-1)A c_x=(q-1)r_q(x,v).
\]
For the other term, \(r_q(sx,v)=-A c_{sx}\), hence
\[
(-q)A c_{sx}=q\,r_q(sx,v).
\]
Adding gives the second branch.

### Step 4. Identify the smaller instances

Every entry on the right has upper endpoint \(sy\), whose length is one less than that of \(y\). The calculation uses any chosen left descent and the already defined bar vector. It consequently proves the recurrence simultaneously for every such descent.

For \(x=1,y=s\), the second branch reads
\[
r_q(1,s)=(q-1)r_q(1,1)+q\,r_q(s,1)=q-1,
\]
using the diagonal and support values.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.HeckeQ.rValue_recursion`: [Hecke.lean:1000](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L1000).
