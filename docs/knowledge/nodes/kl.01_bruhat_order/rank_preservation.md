---
id: kl.foundations.rank_preservation
title: Interval isomorphisms preserve rank differences
kind: theorem
status: proved
primary_topic: kl.01_bruhat_order
topics:
- kl.01_bruhat_order
uses:
- kl.foundations.interval
- kl.foundations.subword
lean:
  repository: openai-kl
  modules:
  - CanonicalKL
  declarations:
  - OAI.KLInvariance.intervalIso_rankDifference
  - OAI.KLInvariance.intervalIso_full_rankDifference
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:415
    format: lean-location
    note: OAI.KLInvariance.intervalIso_rankDifference
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:458
    format: lean-location
    note: OAI.KLInvariance.intervalIso_full_rankDifference
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

# Interval isomorphisms preserve rank differences

If \(\phi:[u,b]\simeq[u',b']\) is an order isomorphism, then every comparable pair \(x\le y\) satisfies
\[
\ell(y)-\ell(x)=\ell(\phi(y))-\ell(\phi(x)).
\]

*Proof.*

First establish that a nontrivial Bruhat interval contains a next step increasing length by one. Compare rank differences with lengths of strictly increasing chains. An interval isomorphism sends strict chains to strict chains, giving one inequality; its inverse gives the other. Since the bottom and top are determined by the order, the full interval rank difference is preserved as well.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.intervalIso_rankDifference`: [CanonicalKL.lean:415](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L415).

`OAI.KLInvariance.intervalIso_full_rankDifference`: [CanonicalKL.lean:458](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L458).
