---
id: kl.coxeter.rank_embedding
title: Strictly monotone interval maps cannot decrease rank
kind: theorem
status: proved
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.foundations.interval
- kl.coxeter.bruhat_successor
lean:
  repository: openai-kl
  modules:
  - CanonicalKL
  declarations:
  - OAI.KLInvariance.rankDifference_le_of_strictMono
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:367
    format: lean-location
    note: OAI.KLInvariance.rankDifference_le_of_strictMono
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the exact interval, order-map and rank hypotheses retained?
  verdict: Read rankDifference_le_of_strictMono. Retained StrictMono rather than adding
    injectivity/order-reflection assumptions; the one-step successor, shorter remaining
    rank and target integer-length increase are explicit.
tags:
- Kazhdan-Lusztig
- Bruhat
- intervals
---

# Strictly monotone interval maps cannot decrease rank

Let \(f:[u,b]\to[u',b']\) be strictly monotone: \(a<c\) implies \(f(a)<f(c)\). For every \(x\le y\),
\[
d(x,y)\le d'(f(x),f(y)),
\]
where \(d,d'\) use the lengths in the respective Coxeter systems.

*Proof.*

### Step 1. Set the rank induction

Induct on \(n=d(x,y)\), allowing every comparable pair in the source interval.

If \(x=y\), both images are the same, so both rank differences are zero.

For \(x<y\), the [[node:kl.coxeter.bruhat_successor|length-one successor theorem]] gives \(z\) with
\[
x<z\le y,\qquad d(x,z)=1.
\]
Transitivity with \(u\le x\) and \(y\le b\) makes \(z\) a member of the original interval.

### Step 2. Apply induction to the shorter remaining pair

Rank additivity gives
\[
d(z,y)=d(x,y)-1=n-1<n.
\]
Thus the induction hypothesis supplies
\[
d(z,y)\le d'(f(z),f(y)).
\]

Strict monotonicity implies ordinary monotonicity: equality of source points gives equality of images, while a strict comparison gives a strict comparison. Hence \(f(z)\le f(y)\).

### Step 3. Count the first target step

Since \(x<z\), strict monotonicity gives \(f(x)<f(z)\). Strict Bruhat comparison raises integer length, so
\[
d'(f(x),f(z))\ge1.
\]

### Step 4. Add the target rank differences

Using target rank additivity, Steps 2–3 yield
\[
\begin{aligned}
d'(f(x),f(y))
&=d'(f(x),f(z))+d'(f(z),f(y))\\
&\ge1+d(z,y)\\
&=d(x,y).
\end{aligned}
\]
This completes the induction.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.rankDifference_le_of_strictMono`: [CanonicalKL.lean:367](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L367).
