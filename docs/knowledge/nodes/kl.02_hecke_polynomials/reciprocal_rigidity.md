---
id: kl.comparison.reciprocal_rigidity
title: Rigidity of a low-degree polynomial under reciprocal evaluation
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.hecke.polynomial_reflection
lean:
  repository: openai-kl
  modules:
  - Comparison
  declarations:
  - OAI.KLInvariance.Comparison.low_degree_zero_of_eval_reciprocal
  - OAI.KLInvariance.Comparison.eq_of_eval_difference_reciprocal
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Comparison:24
    format: lean-location
    note: OAI.KLInvariance.Comparison.low_degree_zero_of_eval_reciprocal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Comparison:50
    format: lean-location
    note: OAI.KLInvariance.Comparison.eq_of_eval_difference_reciprocal
  - artifact: openai-kl-paper
    locator: 6. Reciprocity and simultaneous induction; sec:induction
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
  verdict: Read both Comparison rigidity theorems. Explained the passage from all
    real parameters to polynomial equality, the finite-root argument, the decisive
    coefficient and the injective coefficient map.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Rigidity of a low-degree polynomial under reciprocal evaluation

Let \(f\in\mathbb R[q]\), \(d\in\mathbb N\), and
\(2\,\operatorname{natDegree}(f)<d\).
If
\[
f(q)=q^df(q^{-1})\qquad(0<q<1),
\]
then \(f=0\).

Consequently, integral polynomials \(P,P'\), each satisfying the strict midpoint bound, are equal if
\[
P(q)-P'(q)=q^d\bigl(P(q^{-1})-P'(q^{-1})\bigr)
\qquad(0<q<1).
\]

*Proof.*

### Step 1. Replace reciprocal evaluation by a polynomial

The degree bound implies \(\operatorname{natDegree}(f)\le d\). Its reflected polynomial
\(f^\vee=\operatorname{reflect}_df\)
therefore satisfies
\(f^\vee(q)=q^df(q^{-1})\) at every nonzero real \(q\).

The assumed identity says \(f(q)-f^\vee(q)=0\) on the interval \((0,1)\).

### Step 2. Obtain equality of polynomials

The interval contains infinitely many distinct real numbers, for example \(1/(n+2)\) for natural \(n\).

A nonzero polynomial of degree \(m\) has at most \(m\) distinct roots: at a root \(a\), the factor theorem divides out \(q-a\); at any different root the remaining factor still vanishes; each division lowers the degree by one. Therefore a polynomial with infinitely many roots must be zero.

Apply this to \(f-f^\vee\). We obtain the polynomial identity
\(\operatorname{reflect}_df=f\).

### Step 3. Compare the coefficient at the natural degree

Suppose \(f\ne0\), and put \(m=\operatorname{natDegree}(f)\). Its coefficient \(f_m\) is nonzero. Since \(2m<d\), we have \(d-m>m\), and hence \(f_{d-m}=0\).

The coefficient of the reflected polynomial at \(m\) is \(f_{d-m}=0\). The identity from Step 2 says it equals \(f_m\), a contradiction. Thus \(f=0\).

### Step 4. Apply the conclusion to an integral difference

Put \(g=(P-P')\) and map its integer coefficients into \(\mathbb R\). Subtraction creates no exponent beyond the maximum of the two original natural degrees; mapping coefficients creates no new exponent. Hence
\(2\,\operatorname{natDegree}(g)<d\).

The assumed reciprocal-difference identity is exactly the hypothesis of Steps 1–3 for this real polynomial. Thus its real coefficients all vanish. Injectivity of \(\mathbb Z\to\mathbb R\) makes every integer coefficient of \(P-P'\) zero, proving \(P=P'\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Comparison.low_degree_zero_of_eval_reciprocal`: [Comparison.lean:24](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L24).

`OAI.KLInvariance.Comparison.eq_of_eval_difference_reciprocal`: [Comparison.lean:50](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L50).
