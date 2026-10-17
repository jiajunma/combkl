---
id: kl.foundations.subword
title: The reduced-subword criterion
kind: theorem
status: proved
primary_topic: kl.01_bruhat_order
topics:
- kl.01_bruhat_order
uses:
- kl.foundations.bruhat_order
- kl.detail.strong_exchange
lean:
  repository: openai-kl
  modules:
  - Bruhat
  declarations:
  - OAI.KLInvariance.bruhat_iff_reduced_subword
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:439
    format: lean-location
    note: OAI.KLInvariance.bruhat_iff_reduced_subword
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- background
---

# The reduced-subword criterion

Fix any reduced expression \(\omega\) for \(y\). Then \(x\le y\) if and only if \(\omega\) has a reduced subword, with the original order of letters retained, whose product is \(x\).

*Proof.*

### Step 1. Reduce an arbitrary word without adding letters

We first show that every word contains a reduced subword with the same product. Induct on its length. The empty word is reduced. For a word \(s\omega\), replace \(\omega\) by a reduced subword \(\nu\) with the same product, using induction.

If left multiplication by \(s\) raises length, \(s\nu\) is reduced. If it lowers length, strong exchange deletes one position from \(\nu\) to give the product \(s\,\operatorname{prod}(\nu)\). Its length is exactly one less than the reduced length of \(\nu\), so the deleted word is reduced. In both cases the result is a subword of the original word.

### Step 2. Prove the forward implication along a Bruhat chain

For one downward reflection step from \(y\) to \(x=ty\), apply strong exchange to the supplied reduced expression of \(y\). It deletes a position and produces a word for \(x\). Apply Step 1 if that word is not reduced.

For a chain \(x=x_0\to x_1\to\cdots\to x_r=y\), start with the fixed reduced word of \(y\), perform this operation for the last edge, and continue down the chain. A subword of a subword is a subword. At the end we have a reduced subword for \(x\) inside the originally fixed word.

### Step 3. Establish the simple-multiplication order property for the converse

Fix a simple reflection \(s\), and define
\(L_s(x)=\min\{x,sx\}\), \(U_s(x)=\max\{x,sx\}\), using their lengths to choose the smaller and larger elements.

For a reflection edge \(x\to y\), either \(y=sx\), in which case \(U_s(x)=U_s(y)\), or \(sx\to sy\) is also upward. To verify the latter orientation, if \(sy>y\), use
\(\ell(sx)\le\ell(x)+1\le\ell(y)<\ell(sy)\).
If \(sy<y\), write a reduced expression \(y=s\omega\). Strong exchange for \(x=ty\) cannot delete the first letter, because that would give \(x=sy\), excluded by \(y\ne sx\). It deletes a later letter, so \(sx\) has an expression shorter than the reduced word \(\omega\) for \(sy\). Thus again \(\ell(sx)<\ell(sy)\).

Now check the four descent cases. If \(s\) raises both endpoints, use \(sx\le sy\); if it lowers both, use \(x\le y\). If it lowers \(x\) and raises \(y\), use \(x\le y\le sy\). If it raises \(x\) and lowers \(y\), use \(sx\le sy\le y\). These prove \(U_s(x)\le U_s(y)\). Following a Bruhat chain proves monotonicity of \(U_s\) on all comparisons. The same four cases give monotonicity of \(L_s\).

### Step 4. Prove that every subword product lies below the top

Induct on the fixed reduced word \(s\omega\). Its tail \(\omega\) is reduced, and \(s\) raises its product \(w\), so \(U_s(w)=sw\).

If the subword omits the first letter, its product \(v\) is at most \(w\) by induction, hence at most \(sw\).
If it retains the first letter, write it \(s\mu\). Induction gives \(\operatorname{prod}(\mu)\le w\). Monotonicity gives
\(U_s(\operatorname{prod}(\mu))\le U_s(w)=sw\).
The element \(s\operatorname{prod}(\mu)\) is at most its own upper choice, which equals \(U_s(\operatorname{prod}(\mu))\). Thus its product is again at most \(sw\).

This proves the converse, and with Step 2 proves the stated equivalence.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.bruhat_iff_reduced_subword`: [Bruhat.lean:439](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L439).
