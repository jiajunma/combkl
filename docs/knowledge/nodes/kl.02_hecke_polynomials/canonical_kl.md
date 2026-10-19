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
- kl.hecke.normalization_unique
- kl.hecke.selected_families
- kl.hecke.ordinary_r_construction
- kl.hecke.recursive_p_degree
- kl.detail.kl_recursion
lean:
  repository: openai-kl
  modules:
  - CanonicalKL
  declarations:
  - OAI.KLInvariance.normalized_interval_sum
  - OAI.KLInvariance.constructed_normalizedKL
  - OAI.KLInvariance.normalizedKL_existsUnique
  - OAI.KLInvariance.klFamilies_spec
  - OAI.KLInvariance.klFamilies_eq_constructed
  - OAI.KLInvariance.klPolynomial_eq_constructed
  - OAI.KLInvariance.rPolynomial_eq_constructed
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:239
    format: lean-location
    note: OAI.KLInvariance.normalized_interval_sum
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:260
    format: lean-location
    note: OAI.KLInvariance.constructed_normalizedKL
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:273
    format: lean-location
    note: OAI.KLInvariance.normalizedKL_existsUnique
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:279
    format: lean-location
    note: OAI.KLInvariance.klFamilies_spec
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:282
    format: lean-location
    note: OAI.KLInvariance.klFamilies_eq_constructed
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:286
    format: lean-location
    note: OAI.KLInvariance.klPolynomial_eq_constructed
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:290
    format: lean-location
    note: OAI.KLInvariance.rPolynomial_eq_constructed
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
  prompt: Does the exposition preserve the exact domain, degree conventions and source
    argument?
  verdict: Read normalized_interval_sum, the seven-field construction, unique existence
    and all selected-family equalities. Every field is supplied by an explicit prior
    theorem and the lower-ideal/interval sum conversion is explained.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Existence and uniqueness of the canonical KL families

For every Coxeter system, exactly one pair \((R,P)\) satisfies the normalization data. It is the pair consisting of the ordinary R construction and the recursive lower-half P construction.

The selected interfaces agree with these constructions:
\[
\mathrm{klFamilies}=(R,P),\qquad
\mathrm{rPolynomial}(x,y)=R_{x,y},\qquad
\mathrm{klPolynomial}(x,y)=P_{x,y}.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit construction of the normalized family.**

**OpenAI notes:** The conventions specify the ordinary R recurrence, the strict P degree bound and reciprocity, referring to the classical Kazhdan–Lusztig normalization. [sec:introduction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1), [eq:reciprocity](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L235).

**Lean (primary):** After constructing R, the development defines P by the negative lower half of the proper-upper defect. The reversed R-kernel proves that defect anti-reciprocal, yielding reciprocity. Separate uniqueness inductions identify the selected family with the construction. [CanonicalKL:70](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L70), [CanonicalKL:162](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L162), [Bruhat:204](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L204), [CanonicalKL:260](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L260), [CanonicalKL:282](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L282).

**Role in the proof:** The KB presents the coefficient solution, defect identity, rank induction and seven normalization fields as a continuous construction. The classical selection interfaces are then identified with the explicit formulas.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Supply the three R conditions

Take \(R=\mathrm{OrdinaryR.polynomial}\). Its [[node:kl.hecke.ordinary_r_construction|construction theorem]] proves:

- \(R_{x,x}=1\);
- \(R_{x,y}=0\) when \(x\not\le y\);
- the ordinary recurrence for every left descent of \(y\).

These are precisely the R_diagonal, R_zero and R_recursion fields.

### Step 2. Supply the P values and degree condition

Take \(P=\mathrm{CanonicalP.polynomial}\). The [[node:kl.hecke.recursive_p_degree|recursive degree theorem]] gives the diagonal value one, the value zero when \(x\not\le y\), and
\(2\,\operatorname{natDegree}(P_{x,y})<d(x,y)\) for \(x<y\).

These provide P_diagonal, P_zero and P_degree.

### Step 3. Match the reciprocity sum to the normalization interface

The [[node:kl.detail.kl_recursion|recursion theorem]] proves
\[
\operatorname{reflect}_{d(x,y)}P_{x,y}
=\sum_{z\le y}R_{x,z}P_{z,y}.
\]
If \(x\not\le z\), its R-factor vanishes, so this is the sum over \([x,y]\).

The interval type in the normalization predicate consists exactly of those elements, carrying the two endpoint inequalities. Its finite instance identifies its finitely supported sum with the same finite sum of values. Therefore the displayed equality supplies the reciprocity field.

All seven fields have now been constructed, proving existence.

### Step 4. Apply uniqueness to any normalized pair

Let \((R',P')\) satisfy the same normalization data. The [[node:kl.hecke.normalization_unique|normalized-pair uniqueness theorem]] applies to it and the pair built in Steps 1–3. It gives \(R'=R\) and \(P'=P\).

Thus the normalization predicate has exactly one satisfying pair.

### Step 5. Identify classical selection with the construction

Classical selection of a witness to an inhabited predicate satisfies that predicate. Existence from Step 3 therefore gives NormalizedKL for klFamilies.

Uniqueness identifies klFamilies with \((R,P)\). Taking first components gives equality for rPolynomial; taking second components gives equality for klPolynomial. Evaluating those function equalities at \((x,y)\) yields the stated interfaces.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.normalized_interval_sum`: [CanonicalKL.lean:239](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L239).

`OAI.KLInvariance.constructed_normalizedKL`: [CanonicalKL.lean:260](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L260).

`OAI.KLInvariance.normalizedKL_existsUnique`: [CanonicalKL.lean:273](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L273).

`OAI.KLInvariance.klFamilies_spec`: [CanonicalKL.lean:279](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L279).

`OAI.KLInvariance.klFamilies_eq_constructed`: [CanonicalKL.lean:282](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L282).

`OAI.KLInvariance.klPolynomial_eq_constructed`: [CanonicalKL.lean:286](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L286).

`OAI.KLInvariance.rPolynomial_eq_constructed`: [CanonicalKL.lean:290](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L290).
