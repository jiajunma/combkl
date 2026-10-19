---
id: kl.hecke.lower_interval_sums
title: Lower-interval Hecke sums and their correction vectors
kind: definition
status: formalized
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.definitions.hecke_operators
- kl.foundations.finite_intervals
- kl.coxeter.alternating_words
lean:
  repository: openai-kl
  modules:
  - Dihedral
  declarations:
  - OAI.KLInvariance.Dihedral.lowerSum
  - OAI.KLInvariance.Dihedral.lowerSum_coeff
  - OAI.KLInvariance.Dihedral.lowerSum_one
  - OAI.KLInvariance.Dihedral.lowerSum_simple
  - OAI.KLInvariance.Dihedral.correction
  - OAI.KLInvariance.Dihedral.correction_coeff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:197
    format: lean-location
    note: OAI.KLInvariance.Dihedral.lowerSum
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:200
    format: lean-location
    note: OAI.KLInvariance.Dihedral.lowerSum_coeff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:205
    format: lean-location
    note: OAI.KLInvariance.Dihedral.lowerSum_one
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:490
    format: lean-location
    note: OAI.KLInvariance.Dihedral.lowerSum_simple
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:322
    format: lean-location
    note: OAI.KLInvariance.Dihedral.correction
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:325
    format: lean-location
    note: OAI.KLInvariance.Dihedral.correction_coeff
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the reduced-word, coefficient and interval
    hypotheses?
  verdict: Read lowerSum and correction, including correction at n=0. Defined the
    parameter-independent coefficient vector and its exact reduced prefix/tail inputs.
tags:
- Kazhdan-Lusztig
- dihedral
---

# Lower-interval Hecke sums and their correction vectors

Fix a rank-two Coxeter system and a commutative coefficient ring \(C\). In the unnormalized standard Hecke module, define
\[
S_w=\sum_{z\le w}T_z.
\]
The lower ideal is finite. Its coefficient function is the indicator of that ideal:
\[
S_w(x)=
\begin{cases}
1,&x\le w,\\
0,&x\not\le w.
\end{cases}
\]
Thus every included basis vector occurs with coefficient one.

The first sums are
\[
S_1=T_1,\qquad S_s=T_1+T_s.
\]
The vector \(S_w\) depends on the basis and order, while the parameter \(q\) enters when a Hecke operator acts on it.

## Simple-reflection strings

For a fixed simple reflection \(s\), a simple-reflection string is the pair
\(\{r,sr\}\). Multiplication by \(s\) exchanges the two members, since \(s^2=1\). The members are distinct, and their lengths differ by one.

Choose \(r\) to be the shorter member. Then \(r<sr\) in Bruhat order. Distinct strings are disjoint: sharing either member determines the other by multiplying by \(s\). Thus these pairs partition the group.

The lower ideal of \(v\) can contain neither member, just the shorter member, or both members. If it contains the longer member, downward closure also includes the shorter one.

## Prefix and tail data

Suppose \(\omega_i(n+2)\) is reduced, and write
\[
w=\operatorname{prod}\omega_i(n+2),\quad
v=\operatorname{prod}\omega_{\bar i}(n+1),\quad
p=\operatorname{prod}\omega_i(n).
\]
With \(s=s_i\), we have \(w=sv\), and their lengths are \(n+2,n+1,n\). The tail and prefix are reduced because the original word is reduced.

Define the correction vector
\[
C_{i,n}=
\begin{cases}
0,&n=0,\\
S_p,&n>0.
\end{cases}
\]
Its coefficient is one exactly when \(n>0\) and \(x\le p\), and zero otherwise.

## The first two corrections

For \(w=st\), the tail is \(v=t\), and \(n=0\). The correction is the zero vector.

For a reduced \(w=sts\), the tail is \(v=ts\), the prefix two letters shorter is \(p=s\), and
\[
C_{s,1}=S_s=T_1+T_s.
\]
The [[node:kl.hecke.dihedral_sum_product|Hecke-sum product theorem]] explains these vectors by identifying the simple-reflection pairs whose two members already lie below \(v\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.lowerSum`: [Dihedral.lean:197](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L197).

`OAI.KLInvariance.Dihedral.lowerSum_coeff`: [Dihedral.lean:200](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L200).

`OAI.KLInvariance.Dihedral.lowerSum_one`: [Dihedral.lean:205](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L205).

`OAI.KLInvariance.Dihedral.lowerSum_simple`: [Dihedral.lean:490](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L490).

`OAI.KLInvariance.Dihedral.correction`: [Dihedral.lean:322](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L322).

`OAI.KLInvariance.Dihedral.correction_coeff`: [Dihedral.lean:325](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L325).
