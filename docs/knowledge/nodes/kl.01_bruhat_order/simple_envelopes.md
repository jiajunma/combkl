---
id: kl.detail.simple_envelopes
title: Lower and upper simple-reflection envelopes
kind: definition
status: formalized
primary_topic: kl.01_bruhat_order
topics:
- kl.01_bruhat_order
uses:
- kl.foundations.bruhat_order
lean:
  repository: openai-kl
  modules:
  - Bruhat
  declarations:
  - OAI.KLInvariance.lowerSimple
  - OAI.KLInvariance.upperSimple
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:299
    format: lean-location
    note: OAI.KLInvariance.lowerSimple
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:303
    format: lean-location
    note: OAI.KLInvariance.upperSimple
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# Lower and upper simple-reflection envelopes

Fix a simple reflection \(s\). Multiplication by \(s\) changes length by exactly one, so \(x\) and \(sx\) are comparable in Bruhat order. Define
\[
L_s(x)=\begin{cases}sx&\ell(sx)<\ell(x),\\ x&\ell(x)<\ell(sx),\end{cases}
\qquad
U_s(x)=\begin{cases}x&\ell(sx)<\ell(x),\\ sx&\ell(x)<\ell(sx).\end{cases}
\]
Thus \(L_s(x)\le x\le U_s(x)\), and both envelopes are constant on the pair \(\{x,sx\}\). These definitions use left multiplication. They are the two maps whose monotonicity gives the Bruhat lifting property. They also control the unions and intersections of upper sets used in the word-sheaf induction.

## References

The precise Lean sources are listed below.

## Lean formalization

`OAI.KLInvariance.lowerSimple`: [Bruhat.lean:299](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L299).

`OAI.KLInvariance.upperSimple`: [Bruhat.lean:303](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L303).
