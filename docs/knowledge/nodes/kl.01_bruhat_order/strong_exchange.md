---
id: kl.detail.strong_exchange
title: Strong exchange and deletion from a reduced word
kind: theorem
status: proved
primary_topic: kl.01_bruhat_order
topics:
- kl.01_bruhat_order
uses: []
lean:
  repository: openai-kl
  modules:
  - Coxeter
  declarations:
  - OAI.KLInvariance.CoxeterSupport.strong_exchange
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Coxeter:228
    format: lean-location
    note: OAI.KLInvariance.CoxeterSupport.strong_exchange
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
- bruhat_order
---

# Strong exchange and deletion from a reduced word

Let \(w=s_1\cdots s_n\) be a supplied reduced expression in an arbitrary Coxeter system. If a reflection \(t\) is a left inversion of \(w\), meaning \(\ell(tw)<\ell(w)\), then some position \(j\) satisfies
\[
tw=s_1\cdots\widehat{s_j}\cdots s_n.
\]
The deletion takes place in this particular reduced expression; the assertion is not merely that some shorter expression exists.

*Proof.*

Associate to the reduced word its left-inversion sequence
\[
t_j=s_1\cdots s_{j-1}s_j s_{j-1}\cdots s_1.
\]
The signed-reflection action establishes that every left inversion occurs in this sequence. Choose the position with \(t=t_j\). Multiplying \(t_j\) by \(w\), the inverse prefix cancels and then \(s_j^2=1\), giving exactly the displayed deletion.

This is the combinatorial mechanism behind the reduced-subword characterization of Bruhat order. The word after deletion need not itself be reduced: the theorem asserts the group-product identity, and a reflection can decrease length by more than one.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization



`OAI.KLInvariance.CoxeterSupport.strong_exchange`: [Coxeter.lean:228](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Coxeter.lean#L228).
