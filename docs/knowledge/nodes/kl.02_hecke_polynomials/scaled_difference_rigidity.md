---
id: kl.hecke.scaled_difference_rigidity
title: Rigidity of a reciprocal scaled difference
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.hecke.scaled_polynomials
- kl.comparison.reciprocal_rigidity
lean:
  repository: openai-kl
  modules:
  - SimultaneousInvariance
  declarations:
  - OAI.KLInvariance.Comparison.eq_of_scaled_difference_reciprocal
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SimultaneousInvariance:328
    format: lean-location
    note: OAI.KLInvariance.Comparison.eq_of_scaled_difference_reciprocal
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the exact domain, degree conventions and source
    argument?
  verdict: Read eq_of_scaled_difference_reciprocal in SimultaneousInvariance. Preserved
    quantification over all t in (0,1), the square-root substitution and the multiplication
    that converts scaled symmetry to ordinary reciprocal evaluation.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Rigidity of a reciprocal scaled difference

Let \(P,P'\in\mathbb Z[q]\) satisfy
\[
2\,\operatorname{natDegree}(P)<d,\qquad
2\,\operatorname{natDegree}(P')<d.
\]
Assume that, for every real \(0<t<1\),
\[
S_d(P;t)-S_d(P';t)
=S_d(P;t^{-1})-S_d(P';t^{-1}).
\]
Then \(P=P'\).

*Proof.*

### Step 1. Choose a square root for each polynomial parameter

Fix any real \(q\) with \(0<q<1\). Put \(t=\sqrt q\). Then \(t>0\), \(t^2=q\), and \(t<1\): otherwise \(t^2\ge1\), contradicting \(q<1\).

Also \((t^{-1})^2=(t^2)^{-1}=q^{-1}\). The assumed scaled identity therefore applies to this \(t\).

### Step 2. Expand the two scaled differences

Write \(\Delta(q)=P(q)-P'(q)\). Linearity of the scaling gives
\[
S_d(P;t)-S_d(P';t)=t^{-d}\Delta(q),
\]
\[
S_d(P;t^{-1})-S_d(P';t^{-1})
=(t^{-1})^{-d}\Delta(q^{-1})
=t^d\Delta(q^{-1}).
\]
Thus the hypothesis becomes
\[
t^{-d}\Delta(q)=t^d\Delta(q^{-1}).
\]

### Step 3. Cancel the scale

Since \(t>0\), the number \(t^d\) is nonzero. Multiply by it:
\[
\Delta(q)=t^{2d}\Delta(q^{-1}).
\]
Now \(t^{2d}=(t^2)^d=q^d\). Therefore
\[
\Delta(q)=q^d\Delta(q^{-1})
\]
for every \(0<q<1\).

### Step 4. Apply reciprocal-difference rigidity

The two original strict midpoint bounds are precisely the hypotheses of the [[node:kl.comparison.reciprocal_rigidity|integral reciprocal-difference theorem]]. The identity from Step 3 supplies its evaluation condition, so it gives \(P=P'\).

For constant polynomials and \(d=1\), the scaled difference is \((P-P')t^{-1}\), and its inverted value is \((P-P')t\). Their equality at \(t=1/2\) forces the constant difference to vanish.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Comparison.eq_of_scaled_difference_reciprocal`: [SimultaneousInvariance.lean:328](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SimultaneousInvariance.lean#L328).
