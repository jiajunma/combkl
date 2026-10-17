---
id: kl.foundations.finite_intervals
title: Finiteness of Bruhat intervals
kind: theorem
status: proved
primary_topic: kl.01_bruhat_order
topics:
- kl.01_bruhat_order
uses:
- kl.foundations.interval
- kl.detail.strong_exchange
lean:
  repository: openai-kl
  modules:
  - Bruhat
  declarations:
  - OAI.KLInvariance.interval_finite
  - OAI.KLInvariance.finite_bruhat_lower
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:106
    format: lean-location
    note: OAI.KLInvariance.interval_finite
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:86
    format: lean-location
    note: OAI.KLInvariance.finite_bruhat_lower
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

# Finiteness of Bruhat intervals

Every interval \([u,b]\) in an arbitrary Coxeter system is finite. The set of simple generators need not be finite.

*Proof.*

### Step 1. Bound the immediate reflection predecessors

Choose a reduced word \(\omega\) for \(b\). If \(x\to b\) is a reflection edge, write \(b=tx\), so \(x=tb\) and \(\ell(tb)<\ell(b)\). Strong exchange places \(t\) in the finite inversion list of \(\omega\). Thus every such \(x\) belongs to
\(\{tb:t\text{ occurs in that finite list}\}\).
There are therefore finitely many immediate reflection predecessors, even if the ambient generating set is infinite.

### Step 2. Decompose the entire lower ideal

Let \(L(b)=\{x:x\le b\}\). By the definition of Bruhat order as the reflexive transitive closure of upward reflection steps, a comparison \(x\le b\) is either \(x=b\), or has a last step \(z\to b\), preceded by \(x\le z\). Consequently
\[
L(b)\subseteq\{b\}\cup\bigcup_{z\to b}L(z).
\]

### Step 3. Induct on the top length

Use strong induction on \(\ell(b)\). Each predecessor \(z\to b\) has \(\ell(z)<\ell(b)\), so its lower ideal \(L(z)\) is finite by the induction hypothesis. Step 1 gives only finitely many such \(z\). A finite union of finite sets, together with the singleton \(\{b\}\), is finite. Step 2 shows that \(L(b)\) is a subset of this finite set.

At length zero, there are no predecessors, and the same argument leaves only the identity element.

### Step 4. Pass to an interval

The interval \([u,b]\) is the subset of \(L(b)\) consisting of elements also above \(u\). A subset of a finite set is finite. This proves interval finiteness without any finite-rank hypothesis.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.interval_finite`: [Bruhat.lean:106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L106).

`OAI.KLInvariance.finite_bruhat_lower`: [Bruhat.lean:86](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L86).
