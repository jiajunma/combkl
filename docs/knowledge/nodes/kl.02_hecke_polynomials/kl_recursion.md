---
id: kl.detail.kl_recursion
title: Reciprocity of the lower-half construction
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.hecke.recursive_p
- kl.detail.kl_defect
- kl.hecke.recursive_p_degree
- kl.hecke.defect_antireciprocity
- kl.hecke.low_part_solution
lean:
  repository: openai-kl
  modules:
  - CanonicalKL
  declarations:
  - OAI.KLInvariance.CanonicalP.polynomial_reciprocity
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:162
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.polynomial_reciprocity
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
  prompt: Does the exposition preserve the exact domain, degree conventions and source
    argument?
  verdict: Read polynomial_reciprocity. Made the all-comparable rank induction, diagonal
    lower-ideal sum, each proper upper interval and the two detailed supporting calculations
    explicit.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Reciprocity of the lower-half construction

For the recursively constructed family and every comparable \(x\le y\),
\[
\operatorname{reflect}_{d(x,y)}P_{x,y}
=\sum_{z\le y}R_{x,z}P_{z,y}
=\sum_{x\le z\le y}R_{x,z}P_{z,y}.
\]
Since \(\deg P_{x,y}\le d(x,y)\), the left side is also \(q^{d(x,y)}P_{x,y}(q^{-1})\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit construction of the normalized family.**

**OpenAI notes:** The conventions specify the ordinary R recurrence, the strict P degree bound and reciprocity, referring to the classical Kazhdan–Lusztig normalization. [sec:introduction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1), [eq:reciprocity](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L235).

**Lean (primary):** After constructing R, the development defines P by the negative lower half of the proper-upper defect. The reversed R-kernel proves that defect anti-reciprocal, yielding reciprocity. Separate uniqueness inductions identify the selected family with the construction. [CanonicalKL:70](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L70), [CanonicalKL:162](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L162), [Bruhat:204](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L204), [CanonicalKL:260](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L260), [CanonicalKL:282](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L282).

**Role in the proof:** The KB presents the coefficient solution, defect identity, rank induction and seven normalization fields as a continuous construction. The classical selection interfaces are then identified with the explicit formulas.
<!-- source-comparison:end -->

*Proof.*

### Step 1. State the rank induction

Use strong induction on the natural rank difference \(d(x,y)\), for every comparable pair. The weak and strict degree bounds are already available from the recursive definition.

When \(x=y\), \(P_{x,x}=1\) and reflection in degree zero fixes one. In the lower-ideal sum, the term \(z=x\) is \(R_{x,x}P_{x,x}=1\).

For any other \(z\le x\), the comparison \(x\le z\) would force \(z=x\) by antisymmetry. Hence \(R_{x,z}=0\), and every other term is zero. This proves the diagonal case.

### Step 2. Verify each smaller induction instance

Now take \(x<y\), and write \(d=d(x,y)>0\). For every \(z\) with \(x<z\le y\),
\[
d(z,y)=\ell(y)-\ell(z)<\ell(y)-\ell(x)=d.
\]
The induction hypothesis at \((z,y)\) therefore gives exactly
\[
\operatorname{reflect}_{d(z,y)}P_{z,y}
=\sum_{t\le y}R_{z,t}P_{t,y}.
\]

### Step 3. Obtain the current anti-reciprocal defect

The [[node:kl.hecke.defect_antireciprocity|defect anti-reciprocity theorem]] applies to the equations in Step 2. Its degree hypotheses hold by the already proved R and recursive-P bounds. It gives
\[
\operatorname{reflect}_dD_{x,y}=-D_{x,y}.
\]

### Step 4. Solve the defect equation

By the defining recursion,
\(P_{x,y}=-\operatorname{low}_dD_{x,y}\).
The [[node:kl.hecke.low_part_solution|lower-half solution theorem]], applied to Step 3, yields
\[
\operatorname{reflect}_dP_{x,y}=P_{x,y}+D_{x,y}.
\]
The full-sum identity for \(D_{x,y}\) identifies the right side with
\(\sum_{z\le y}R_{x,z}P_{z,y}\).
This proves the new induction case.

### Step 5. Restrict the sum to the interval

A term with \(z\le y\) but \(x\not\le z\) has \(R_{x,z}=0\). Removing those terms gives the sum over \([x,y]\).

The degree bound permits reciprocal evaluation of the reflected polynomial, giving the displayed power notation and completing the proof.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.CanonicalP.polynomial_reciprocity`: [CanonicalKL.lean:162](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L162).
