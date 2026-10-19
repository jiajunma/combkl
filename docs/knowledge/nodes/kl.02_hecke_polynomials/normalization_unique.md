---
id: kl.hecke.normalization_unique
title: Uniqueness of a normalized polynomial-family pair
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.foundations.normalized_kl
- kl.hecke.low_degree_rigidity
- kl.foundations.finite_intervals
- kl.coxeter.word_data
lean:
  repository: openai-kl
  modules:
  - Bruhat
  declarations:
  - OAI.KLInvariance.normalized_R_unique
  - OAI.KLInvariance.normalized_P_unique
  - OAI.KLInvariance.normalizedKL_unique
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:111
    format: lean-location
    note: OAI.KLInvariance.normalized_R_unique
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:151
    format: lean-location
    note: OAI.KLInvariance.normalized_P_unique
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:204
    format: lean-location
    note: OAI.KLInvariance.normalizedKL_unique
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the exact domain, degree conventions and source
    argument?
  verdict: Read normalized_R_unique, normalized_P_unique and normalizedKL_unique.
    Separated the upper-length and interval-rank inductions, all endpoint cases, the
    single surviving bottom term and the exact degree bound for the difference.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Uniqueness of a normalized polynomial-family pair

For a fixed Coxeter system, any two pairs satisfying the normalization data have identical R-components and identical P-components.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit construction of the normalized family.**

**OpenAI notes:** The conventions specify the ordinary R recurrence, the strict P degree bound and reciprocity, referring to the classical Kazhdan–Lusztig normalization. [sec:introduction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1), [eq:reciprocity](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L235).

**Lean (primary):** After constructing R, the development defines P by the negative lower half of the proper-upper defect. The reversed R-kernel proves that defect anti-reciprocal, yielding reciprocity. Separate uniqueness inductions identify the selected family with the construction. [CanonicalKL:70](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L70), [CanonicalKL:162](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L162), [Bruhat:204](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L204), [CanonicalKL:260](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L260), [CanonicalKL:282](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L282).

**Role in the proof:** The KB presents the coefficient solution, defect identity, rank induction and seven normalization fields as a continuous construction. The classical selection interfaces are then identified with the explicit formulas.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Induct on the upper length for the R-component

Let \((R,P)\) and \((R',P')\) be normalized pairs. Prove \(R_{x,y}=R'_{x,y}\) by strong induction on \(\ell(y)\), for all \(x\).

If \(y=1\), then \(x=1\) gives diagonal value one. If \(x\ne1\), it cannot lie below \(1\): length monotonicity would force \(\ell(x)=0\), hence \(x=1\). Both R-values are therefore zero.

For \(y\ne1\), choose a simple left descent \(s\), and put \(v=sy\), with \(\ell(v)<\ell(y)\). Both families satisfy the same recurrence. In the descent branch at \(x\), induction identifies \(R_{sx,v}\) with \(R'_{sx,v}\). In the ascent branch it identifies both \(R_{x,v}\) and \(R_{sx,v}\) with their primed counterparts. The scalar coefficients \(q-1,q\) are the same. Hence the R-values agree for every pair.

### Step 2. Set the independent rank induction for P

Now prove \(P_{x,y}=P'_{x,y}\) by strong induction on the natural rank difference, allowing every pair.

If \(x\not\le y\), both values are zero. If \(x=y\), both are one.

For \(x<y\), set \(d=d(x,y)\). If \(z\in[x,y]\) and \(z\ne x\), then
\[
d(z,y)=\ell(y)-\ell(z)<\ell(y)-\ell(x)=d.
\]
Thus induction gives \(P_{z,y}=P'_{z,y}\) at every index except possibly the bottom.

### Step 3. Subtract the two reciprocity equations

Set \(f=P_{x,y}-P'_{x,y}\). Linearity of reflection and Step 1 give
\[
\operatorname{reflect}_df
=\sum_{z\in[x,y]}R_{x,z}(P_{z,y}-P'_{z,y}).
\]
For \(z\ne x\), Step 2 makes the bracket zero. At \(z=x\), the R-factor is \(R_{x,x}=1\). Therefore
\[
\operatorname{reflect}_df=f.
\]

### Step 4. Apply low-degree rigidity

Both P-values have twice their natural degree strictly less than \(d\). The degree of their difference is at most the maximum of their degrees, so
\(2\,\operatorname{natDegree}(f)<d\).

The [[node:kl.hecke.low_degree_rigidity|integral low-degree rigidity theorem]] now gives \(f=0\), hence \(P_{x,y}=P'_{x,y}\). This completes the second induction.

### Step 5. Recover equality of pairs

Step 1 proves equality of the first component as a function of both endpoints. Steps 2–4 prove equality of the second. Equality of the two ordered pairs follows componentwise.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.normalized_R_unique`: [Bruhat.lean:111](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L111).

`OAI.KLInvariance.normalized_P_unique`: [Bruhat.lean:151](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L151).

`OAI.KLInvariance.normalizedKL_unique`: [Bruhat.lean:204](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L204).
