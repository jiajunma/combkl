---
id: kl.coxeter.lower_interval_parity
title: Parity balance in lower Bruhat intervals
kind: theorem
status: proved
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.coxeter.external_vertices
- kl.detail.simple_envelopes
- kl.detail.bruhat_lifting
- kl.coxeter.word_data
- kl.foundations.interval
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.simple_mul_bruhat_of_descent
  - OAI.KLInvariance.lower_parity_balance
  - OAI.KLInvariance.external_parity_card_le
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:243
    format: lean-location
    note: OAI.KLInvariance.simple_mul_bruhat_of_descent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:252
    format: lean-location
    note: OAI.KLInvariance.lower_parity_balance
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:288
    format: lean-location
    note: OAI.KLInvariance.external_parity_card_le
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the simple-envelope proof of lower-ideal stability, the simple-reflection
    parity bijection and the finite set-difference calculation. Preserved the arbitrary-rank
    Coxeter scope and all c=1, x=1 and nonidentity cases.
tags:
- Kazhdan-Lusztig
- interpolation
---

# Parity balance in lower Bruhat intervals

Let \(W\) be any Coxeter system. If \(c\ne1\), its finite lower Bruhat interval has equally many vertices of each length parity. More precisely, for \(p\in\{0,1\}\),
\[
\#\{z\le c:\ell(z)\bmod2=p\}
=\#\{z\le c:\ell(z)\bmod2\ne p\}.
\]

For \(x\le c\), the external parity classes satisfy
\[
|Z(x,c)|\le |Y(x,c)|.
\]
Consequently there exists an injection \(Z(x,c)\hookrightarrow Y(x,c)\).

*Proof.*

### Step 1. Keep a lower interval invariant under a simple reflection

Choose a left descent \(s\) of \(c\), so \(\ell(sc)<\ell(c)\). Such a descent exists because \(c\ne1\).

Let \(U_s(z)=\max\{z,sz\}\) be the upper simple envelope. Its pair-constancy and monotonicity give, for \(z\le c\),
\[
sz\le U_s(sz)=U_s(z)\le U_s(c)=c.
\]
The last equality uses the descent at \(c\). Thus left multiplication by \(s\) preserves the lower interval.

### Step 2. Pair the two length parities

Multiplication by a simple reflection changes length by one, so \(z\mapsto sz\) exchanges the two parity classes.

It is its own inverse because \(s^2=1\). Hence it is a bijection from the class with parity \(p\) to the other class, proving equality of their finite cardinalities.

### Step 3. Express external cardinalities as differences

Assume \(x\le c\), and put \(p=\ell(x)\bmod2\). Transitivity gives \([1,x]\subseteq[1,c]\). Filtering by either parity preserves this containment.

Write \(C_p,C_{\ne p}\) for the two parity counts below \(c\), and \(X_p,X_{\ne p}\) for those below \(x\). Removing the smaller lower interval gives
\[
|Z(x,c)|=C_p-X_p,\qquad
|Y(x,c)|=C_{\ne p}-X_{\ne p}.
\]
These are natural-number differences of counts of nested finite sets.

### Step 4. Check the identity cases and the balanced case

If \(c=1\), the inequalities \(1\le x\le1\) force \(x=1\), and both external classes are empty.

Suppose \(c\ne1\). Step 2 gives \(C_p=C_{\ne p}\).

If \(x\ne1\), Step 2 also gives \(X_p=X_{\ne p}\), so the external counts are equal.

If \(x=1\), then \(p=0\) and \([1,x]=\{1\}\). Thus \(X_p=1\) and \(X_{\ne p}=0\), giving
\[
|Z(1,c)|=C_0-1\le C_0=|Y(1,c)|.
\]
This proves the inequality in every case.

### Step 5. Choose the matching used in interpolation

The two external classes are finite. Since the same-parity class has no more elements, enumerate it and assign its elements to distinct members of the opposite-parity class. This yields an injection
\[
j:Z(x,c)\hookrightarrow Y(x,c).
\]
Each opposite-parity vertex therefore receives at most one matched same-parity vertex.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.simple_mul_bruhat_of_descent`: [SheafMorphisms.lean:243](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L243).

`OAI.KLInvariance.lower_parity_balance`: [SheafMorphisms.lean:252](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L252).

`OAI.KLInvariance.external_parity_card_le`: [SheafMorphisms.lean:288](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L288).
