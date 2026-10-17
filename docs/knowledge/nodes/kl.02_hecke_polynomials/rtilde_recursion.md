---
id: kl.detail.rtilde_recursion
title: The descent recursion for normalized R-polynomials
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.detail.rtilde_family
- kl.definitions.bar_involution
lean:
  repository: openai-kl
  modules:
  - Hecke
  declarations:
  - OAI.KLInvariance.Hecke.rTilde_recursion
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:491
    format: lean-location
    note: OAI.KLInvariance.Hecke.rTilde_recursion
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
- hecke_polynomials
---

# The descent recursion for normalized R-polynomials

If \(s\) is a simple reflection and \(sy<y\), then
\[
\widetilde R_{x,y}(a)=
\begin{cases}
\widetilde R_{sx,sy}(a),&sx<x,\\
\widetilde R_{sx,sy}(a)+a\widetilde R_{x,sy}(a),&sx>x.
\end{cases}
\]
Together with diagonal value \(1\) and vanishing outside Bruhat order, this computes the family by induction on the upper endpoint's length. The rank-one value is \(\widetilde R_{1,s}(a)=a\).

*Proof.*

The upper descent means \(y=s(sy)\) is a simple ascent from \(sy\). Apply the bar-basis ascent formula and read its coefficient at \(x\). The inverse Hecke operator has two cases according to whether \(s\) lowers \(x\). Substituting the defining parameter \(-a\) in the bar transform produces the positive coefficient \(a\) in the second case.

The direction of the descent and the sign of the parameter are essential: this recurrence comes from the constructed bar action.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization



`OAI.KLInvariance.Hecke.rTilde_recursion`: [Hecke.lean:491](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L491).
