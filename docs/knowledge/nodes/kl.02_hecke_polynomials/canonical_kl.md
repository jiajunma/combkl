---
id: kl.foundations.canonical_kl
title: Existence and uniqueness of the canonical KL families
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.foundations.normalized_kl
- kl.foundations.low_half
- kl.detail.kl_recursion
- kl.detail.ordinary_r
lean:
  repository: openai-kl
  modules:
  - CanonicalKL
  - Model
  declarations:
  - OAI.KLInvariance.normalizedKL_existsUnique
  - OAI.KLInvariance.klFamilies_spec
  - OAI.KLInvariance.klPolynomial_eq_constructed
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:273
    format: lean-location
    note: OAI.KLInvariance.normalizedKL_existsUnique
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:279
    format: lean-location
    note: OAI.KLInvariance.klFamilies_spec
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:286
    format: lean-location
    note: OAI.KLInvariance.klPolynomial_eq_constructed
  - artifact: openai-kl-paper
    locator: 1. Introduction and conventions; sec:introduction
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
- introduction
---

# Existence and uniqueness of the canonical KL families

For every Coxeter system, exactly one pair of polynomial families satisfies [[node:kl.foundations.normalized_kl]]. The polynomials selected by those conditions agree with the explicit lower-half construction.

*Proof.*

### Step 1. Exhibit a family rather than assume one exists

Take the constructed ordinary R-family and the lower-half P-family. Their diagonal values are one and their noncomparable values are zero by construction. The Hecke coefficient calculation proves the R-recursion. The lower-half construction proves the strict degree bound, and [[node:kl.detail.kl_recursion]] proves reciprocity. Thus every condition in the definition of a normalized pair is satisfied. This proves existence.

### Step 2. Prove uniqueness of the R-component

Let two normalized pairs be given. Induct on the length of the upper endpoint \(y\), allowing every \(x\). If \(y=1\), only \(x=1\) can lie below it; diagonal and zero conditions give equality.

If \(y\ne1\), choose a simple descent \(s\). Both normalized families satisfy the same R-recursion. Every term on its right has upper endpoint \(sy\), whose length is smaller. The induction hypothesis identifies those terms in both branches, so it identifies the R-values at \((x,y)\).

### Step 3. Prove uniqueness of the P-component

The R-components now agree. Induct on \(d(x,y)\). The diagonal and noncomparable cases are fixed. For \(x<y\), every term with \(z>x\) in the reciprocity sum is equal by induction. Subtract the two reciprocity equations. Their difference \(p=P_{x,y}-P'_{x,y}\) satisfies
\(\operatorname{reflect}_d p=p\), and both original degree bounds imply that \(p\) is supported strictly below \(d/2\).

If \(p\ne0\), let \(m\) be its highest nonzero degree. Reflection sends that coefficient to degree \(d-m>m\), contradicting equality with \(p\). Hence \(p=0\). This establishes uniqueness of P at the current pair and completes induction.

### Step 4. Identify the selected family

The selected KL family is chosen from the predicate specifying normalized pairs. Step 1 proves that this predicate has a witness, so the selected family satisfies it. Steps 2–3 show that it must equal the explicitly constructed family. Taking the P-component gives the claimed equality for the selected canonical KL polynomials.

## References

[1. Introduction and conventions](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization

`OAI.KLInvariance.normalizedKL_existsUnique`: [CanonicalKL.lean:273](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L273).

`OAI.KLInvariance.klFamilies_spec`: [CanonicalKL.lean:279](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L279).

`OAI.KLInvariance.klPolynomial_eq_constructed`: [CanonicalKL.lean:286](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L286).
