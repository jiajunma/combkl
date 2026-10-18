---
id: kl.coxeter.reflection_sign_flip
title: A reflection reverses the sign of its own label
kind: theorem
status: proved
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.coxeter.signed_reflection_action
lean:
  repository: openai-kl
  modules:
  - Coxeter
  declarations:
  - OAI.KLInvariance.CoxeterSupport.reflectionAction_reflection
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Coxeter:173
    format: lean-location
    note: OAI.KLInvariance.CoxeterSupport.reflectionAction_reflection
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry retain the local construction and its quantifiers?
  verdict: Checked arbitrary words, arbitrary labels, sign translation, and the precise
    Coxeter presentation relations directly in the local source.
tags:
- Kazhdan-Lusztig
- Coxeter
---

# A reflection reverses the sign of its own label

Let \(t\) be a reflection in a Coxeter group. For every \(\varepsilon\in\mathbb Z/2\mathbb Z\),
\[
A_t(t,\varepsilon)=(t,\varepsilon+1).
\]

*Proof.*

### Step 1. Choose a simple conjugate

Write \(t=us_iu^{-1}\). By the translation formula for the signed action, there are bits \(\delta,\eta\) such that
\[
A_{u^{-1}}(t,\varepsilon)=(s_i,\varepsilon+\delta),
\qquad
A_u(s_i,\varepsilon)=(t,\varepsilon+\eta).
\]
Each translation is independent of \(\varepsilon\).

### Step 2. Cancel the inverse translations

Apply \(A_uA_{u^{-1}}\) to \((t,0)\). The inverse law makes the result \((t,0)\). The two translation formulas instead give \((t,\delta+\eta)\). Thus \(\delta+\eta=0\).

### Step 3. Insert the simple reflection

The group-action law gives \(A_t=A_uA_iA_{u^{-1}}\). On \((t,\varepsilon)\), these three maps successively give
\[
(s_i,\varepsilon+\delta),\qquad
(s_i,\varepsilon+\delta+1),\qquad
(t,\varepsilon+\delta+1+\eta).
\]
Since \(\delta+\eta=0\), the final bit is \(\varepsilon+1\), as asserted.

## References

The local declarations below give the construction and its word calculations.

## Lean formalization

`OAI.KLInvariance.CoxeterSupport.reflectionAction_reflection`: [Coxeter.lean:173](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Coxeter.lean#L173).
