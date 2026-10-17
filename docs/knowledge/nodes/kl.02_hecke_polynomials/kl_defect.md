---
id: kl.detail.kl_defect
title: The defect in the lower-half KL recursion
kind: definition
status: formalized
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.detail.ordinary_r
- kl.foundations.low_half
- kl.foundations.interval
lean:
  repository: openai-kl
  modules:
  - CanonicalKL
  declarations:
  - OAI.KLInvariance.CanonicalP.defect
  - OAI.KLInvariance.CanonicalP.polynomial
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:95
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.defect
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:70
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.polynomial
  - artifact: openai-kl-paper
    locator: Related paper context; sec:introduction
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  definition: accepted
  proof: not_applicable
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

# The defect in the lower-half KL recursion

For \(x<y\), suppose the polynomials \(P_{z,y}\) have already been constructed for \(x<z\leq y\). Define the defect
\[
D_{x,y}(q)=\sum_{x<z\leq y}R_{x,z}(q)P_{z,y}(q).
\]
The interval is finite, and every \(P_{z,y}\) on the right has smaller rank difference. Thus this is legitimate descending recursion in the lower endpoint.

The desired reciprocity equation is
\[
q^{d(x,y)}P_{x,y}(q^{-1})=P_{x,y}(q)+D_{x,y}(q).
\]
It remains to solve for a polynomial strictly below the middle degree. Let
\(\operatorname{low}_d\) retain coefficients \(q^i\) with \(2i<d\). The construction sets
\[
P_{x,y}=-\operatorname{low}_{d(x,y)}D_{x,y},\qquad P_{x,x}=1,
\]
and sets \(P_{x,y}=0\) when \(x\not\leq y\).

For a cover \(x<y\), the defect is \(q-1\); its strict lower part is \(-1\), so the construction gives \(P_{x,y}=1\). Reciprocity of this construction is a theorem, explained in the next entry.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization



`OAI.KLInvariance.CanonicalP.defect`: [CanonicalKL.lean:95](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L95).

`OAI.KLInvariance.CanonicalP.polynomial`: [CanonicalKL.lean:70](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L70).
