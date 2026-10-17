---
id: kl.comparison.no_deficit
title: Endpoint equality forces equality at every transfer step
kind: theorem
status: proved
primary_topic: kl.08_comparison_and_freeness
topics:
- kl.08_comparison_and_freeness
uses:
- kl.comparison.positive_transfer
- kl.detail.transfer_properties
- kl.sheaves.hilbert_detection
lean:
  repository: openai-kl
  modules:
  - Comparison
  declarations:
  - OAI.KLInvariance.Comparison.every_step_eq_of_endpoint_eq
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Comparison:119
    format: lean-location
    note: OAI.KLInvariance.Comparison.every_step_eq_of_endpoint_eq
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
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- induction
---

# Endpoint equality forces equality at every transfer step

Suppose \(T\ge0\), the endpoints satisfy \(x_k\ne y_k\), and
\[
D_{k+1}\le\tau_{x_k,y_k,T}(D_k).
\]
If the final state equals the exact composite of these transfers applied to \(D_0\), every step is an equality.

*Proof.*

### Step 1. Construct the ideal states

Let \(M_k=\tau_{x_k,y_k,T}\), where \(T\ge0\) and \(x_k\ne y_k\). Use indices \(k=0,\ldots,n-1\), and define
\[
E_0=D_0,\qquad E_{k+1}=M_kE_k.
\]
The hypotheses are \(D_{k+1}\le M_kD_k\) and \(D_n=E_n\).

We first prove \(D_k\le E_k\). At \(k=0\) it is equality. If it holds at \(k\), monotonicity gives \(M_kD_k\le M_kE_k=E_{k+1}\); combining with the given inequality proves it at \(k+1\).

### Step 2. Recover exactness of the final transfer

For \(n>0\), apply Step 1 at \(n-1\):
\[
D_n\le M_{n-1}D_{n-1}\le M_{n-1}E_{n-1}=E_n=D_n.
\]
The first inequality is the actual last-step bound; the second is monotonicity; the next equality defines \(E_n\); the final equality is the endpoint hypothesis.

For each coordinate, a real number trapped between equal bounds must equal them. Hence
\(D_n=M_{n-1}D_{n-1}=M_{n-1}E_{n-1}\).

### Step 3. Recover the preceding endpoint

The last equality and injectivity of \(M_{n-1}\), proved in [[node:kl.detail.transfer_properties]], imply
\(D_{n-1}=E_{n-1}\).
Injectivity is legitimate because the edge endpoints are distinct. We have therefore recovered the endpoint hypothesis for the shorter list.

### Step 4. Complete induction on the number of steps

For \(n=0\), there are no steps to prove exact. For \(n>0\), Step 2 proves the last step exact; Step 3 gives the endpoint equality needed for the induction hypothesis on the first \(n-1\) steps. All their monotonicity and distinct-endpoint hypotheses are restrictions of the original ones. Induction proves every step exact.

### Step 5. Interpret an exact state step as image equality

In the sheaf application, each state deficit equals a positive scale times
\[
H_{f_eJ_e}(q)-H_{I_e}(q),\qquad I_e\subseteq f_eJ_e,\quad0<q<1.
\]
The scale is positive, so an exact state step gives equality of these Hilbert values. The upper scaled image is homogeneous. [[node:kl.sheaves.hilbert_detection]] therefore gives \(I_e=f_eJ_e\).

This last deduction uses containment and graded dimensions, not just a statement about ranks. It consequently also detects a difference supported in higher codimension.

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.Comparison.every_step_eq_of_endpoint_eq`: [Comparison.lean:119](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L119).
