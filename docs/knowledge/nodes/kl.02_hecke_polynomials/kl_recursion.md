---
id: kl.detail.kl_recursion
title: Reciprocity of the lower-half construction
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.detail.kl_defect
- kl.detail.r_kernel
- kl.foundations.low_half
lean:
  repository: openai-kl
  modules:
  - CanonicalKL
  declarations:
  - OAI.KLInvariance.CanonicalP.lowPart_solution
  - OAI.KLInvariance.CanonicalP.polynomial_reciprocity
  - OAI.KLInvariance.CanonicalP.polynomial_strict_degree
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:43
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.lowPart_solution
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:162
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.polynomial_reciprocity
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:104
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.polynomial_strict_degree
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

# Reciprocity of the lower-half construction

The recursively constructed family satisfies
\[
q^{d(x,y)}P_{x,y}(q^{-1})
=\sum_{x\leq z\leq y}R_{x,z}(q)P_{z,y}(q),
\qquad
2\deg P_{x,y}<d(x,y)\quad(x<y).
\]

*Proof.*

### Step 1. Make the induction data explicit

For \(x<y\), put \(d=d(x,y)\) and
\[
D_{x,y}=\sum_{x<z\le y}R_{x,z}P_{z,y},
\qquad P_{x,y}=-\operatorname{low}_dD_{x,y}.
\]
Every term \(P_{z,y}\) has smaller rank because \(z>x\). Induct on \(d\). The diagonal case has \(P_{x,x}=R_{x,x}=1\), so reciprocity holds.

The construction itself gives \(\deg P_{x,y}<d/2\): the truncation retains exactly the exponents \(i\) with \(2i<d\), and changing a sign creates no new exponent.

### Step 2. Reflect the defect and substitute the smaller reciprocity equations

Let a bar on an entry with endpoints \(u,v\) mean reflection in degree \(d(u,v)\). Rank additivity and the degree bounds give
\[
\overline{D}_{x,y}
=\sum_{x<z\le y}\overline R_{x,z}\,\overline P_{z,y}.
\]
The induction hypothesis says
\(\overline P_{z,y}=\sum_{z\le w\le y}R_{z,w}P_{w,y}\).
Substitute it and interchange the two finite sums:
\[
\overline D_{x,y}
=\sum_{x<w\le y}
\left(\sum_{x<z\le w}\overline R_{x,z}R_{z,w}\right)P_{w,y}.
\]

### Step 3. Evaluate the inner sum

For \(w>x\), the R-kernel identity gives
\(\sum_{x\le z\le w}\overline R_{x,z}R_{z,w}=0\).
Its \(z=x\) term is \(R_{x,w}\), because \(R_{x,x}=1\). Removing that term gives
\[
\sum_{x<z\le w}\overline R_{x,z}R_{z,w}=-R_{x,w}.
\]
Thus Step 2 becomes
\(\overline D_{x,y}=-\sum_{x<w\le y}R_{x,w}P_{w,y}=-D_{x,y}\).
This proves the anti-reciprocity required by the lower-half construction.

### Step 4. Solve the anti-reciprocal equation coefficient by coefficient

Write \(D=\sum_i a_iq^i\), and set \(P=-\sum_{2i<d}a_iq^i\). Anti-reciprocity says \(a_{d-i}=-a_i\). If \(d\) is even, its middle coefficient satisfies \(a_{d/2}=-a_{d/2}\), hence is zero over \(\mathbb Z\).

For \(2i<d\), the coefficient of \(q^i\) in \(\overline P\) is zero, and that in \(P+D\) is \(-a_i+a_i=0\).
For \(2i>d\), the coefficient in \(\overline P\) is \(-a_{d-i}=a_i\), and that in \(P+D\) is \(a_i\).
At the middle, both are zero. Outside degrees \(0,\ldots,d\), the bounds give zero. Hence \(\overline P=P+D\).

### Step 5. Restore the omitted diagonal summand

Since \(R_{x,x}=1\), \(P_{x,y}+D_{x,y}\) is exactly
\(\sum_{x\le z\le y}R_{x,z}P_{z,y}\).
Step 4 is the desired reciprocity equation. Together with the degree observation in Step 1, this completes the induction.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization



`OAI.KLInvariance.CanonicalP.lowPart_solution`: [CanonicalKL.lean:43](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L43).

`OAI.KLInvariance.CanonicalP.polynomial_reciprocity`: [CanonicalKL.lean:162](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L162).

`OAI.KLInvariance.CanonicalP.polynomial_strict_degree`: [CanonicalKL.lean:104](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L104).
