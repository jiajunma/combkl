---
id: kl.detail.kl_defect
title: The reciprocity defect on a proper upper interval
kind: definition
status: formalized
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.hecke.recursive_p
- kl.detail.ordinary_r
- kl.foundations.finite_intervals
lean:
  repository: openai-kl
  modules:
  - CanonicalKL
  - OrdinaryR
  declarations:
  - OAI.KLInvariance.properIntervalFinset
  - OAI.KLInvariance.mem_properIntervalFinset
  - OAI.KLInvariance.CanonicalP.defect
  - OAI.KLInvariance.CanonicalP.defect_full_sum
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.OrdinaryR:219
    format: lean-location
    note: OAI.KLInvariance.properIntervalFinset
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.OrdinaryR:223
    format: lean-location
    note: OAI.KLInvariance.mem_properIntervalFinset
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:95
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.defect
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:124
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.defect_full_sum
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
  prompt: Does the exposition preserve the exact domain, degree conventions and source
    argument?
  verdict: Read properIntervalFinset, defect and defect_full_sum. Specified the excluded
    bottom, support-zero terms, diagonal removal and all-pair definition.
tags:
- Kazhdan-Lusztig
- Hecke
---

# The reciprocity defect on a proper upper interval

Let \(P\) be the recursive family. For every \(x,y\), define
\[
D_{x,y}=\sum_{x<z\le y}R_{x,z}P_{z,y}.
\]
The index set is the proper upper part of the interval: it excludes \(x\) and includes \(y\) when \(x<y\). In the source, properIntervalFinset filters the finite lower ideal of \(y\) by \(x\le z\) and \(x\ne z\).

For \(x=y\) or \(x\not\le y\), this index set is empty, so \(D_{x,y}=0\).

## The part of reciprocity already supplied by smaller intervals

When \(x<y\), every \(P_{z,y}\) in the defect has smaller rank difference. The defect is therefore determined before the new \(P_{x,y}\) is defined. The recursion is
\[
P_{x,y}=-\operatorname{low}_{d(x,y)}D_{x,y}.
\]

Write \(L(y)=\{z:z\le y\}\). For \(x\le y\),
\[
D_{x,y}
=\sum_{z\in L(y)}R_{x,z}P_{z,y}-P_{x,y}.
\]
To check this, discard the terms with \(x\not\le z\), since their R-factor is zero. Among the remaining terms, \(z=x\) contributes \(R_{x,x}P_{x,y}=P_{x,y}\). Removing it leaves precisely the defining defect.

Thus reciprocity is equivalent to
\[
\operatorname{reflect}_{d(x,y)}P_{x,y}=P_{x,y}+D_{x,y}.
\]
The defect records the contribution of the proper upper intervals. Its anti-reciprocity is the compatibility identity that makes the lower-half choice solve the whole equation.

For the first two examples,
\[
D_{1,s}=q-1,\qquad D_{1,st}=q^2-1.
\]
Reflection in degrees one and two, respectively, negates these defects.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.properIntervalFinset`: [OrdinaryR.lean:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L219).

`OAI.KLInvariance.mem_properIntervalFinset`: [OrdinaryR.lean:223](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L223).

`OAI.KLInvariance.CanonicalP.defect`: [CanonicalKL.lean:95](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L95).

`OAI.KLInvariance.CanonicalP.defect_full_sum`: [CanonicalKL.lean:124](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L124).
