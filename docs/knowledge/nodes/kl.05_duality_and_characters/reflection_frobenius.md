---
id: kl.notes.reflection_frobenius
title: The rank-two Frobenius extension associated with a reflection
kind: theorem
status: proved
primary_topic: kl.05_duality_and_characters
topics:
- kl.05_duality_and_characters
uses:
- kl.notes.perfect_pairings
lean:
  repository: openai-kl
  modules:
  - Decomposition
  declarations:
  - OAI.KLInvariance.ReflectionFrobenius.coordinates
  - OAI.KLInvariance.ReflectionFrobenius.trace
  - OAI.KLInvariance.ReflectionFrobenius.trace_mul
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1504
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.coordinates
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1517
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.trace
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1530
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.trace_mul
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; bg:normalization
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the mathematical hypotheses and scope retained from the referenced declarations?
  verdict: The exposition follows the fixed Lean source; worked calculations explain
    the constructions.
tags:
- Kazhdan-Lusztig
- background
---

# The rank-two Frobenius extension associated with a reflection

Let \(A\) be a domain over a characteristic-zero field, let \(\tau\) be an involutive algebra automorphism, and let \(0\ne\alpha\in A\) satisfy
\[
\tau(\alpha)=-\alpha,\qquad \alpha\mid a-\tau(a)\quad(a\in A).
\]
Write \(R=A^\tau\). Then
\[
A=R\oplus\alpha R.
\]
Define \(\operatorname{tr}(a_0+\alpha a_1)=a_1\). The pairing
\[
(a,b)\longmapsto\operatorname{tr}(ab)
\]
is perfect over \(R\).

*Proof.*

### Step 1. Construct the two invariant coordinates

For \(a\in A\), put \(a_0=(a+\tau(a))/2\). Involutivity gives \(\tau(a_0)=a_0\), so \(a_0\in R=A^\tau\).
By the divisibility hypothesis choose \(d\) with \(a-\tau(a)=\alpha d\). Apply \(\tau\):
\[
\tau(a)-a=-\alpha\tau(d).
\]
Negating the original equation also gives \(\tau(a)-a=-\alpha d\). Since \(\alpha\ne0\) and \(A\) is a domain, cancellation gives \(\tau(d)=d\). Thus \(a_1=d/2\in R\).

Adding the even and odd parts gives \(a=a_0+\alpha a_1\). Division by two is legitimate over the stated characteristic-zero coefficient field.

### Step 2. Prove uniqueness

Suppose \(a_0+\alpha a_1=b_0+\alpha b_1\), with all four coefficients in \(R\). Apply \(\tau\) to obtain \(a_0-\alpha a_1=b_0-\alpha b_1\). Subtracting gives
\(2\alpha(a_1-b_1)=0\).
The scalar \(2\alpha\) is nonzero in the domain, so \(a_1=b_1\), and substitution gives \(a_0=b_0\). Hence \(1,\alpha\) form an \(R\)-basis of \(A\).

### Step 3. Compute the trace pairing

Because \(\tau(\alpha^2)=\alpha^2\), the element \(\alpha^2\) belongs to \(R\). Multiplication gives
\[
(a_0+\alpha a_1)(b_0+\alpha b_1)
=(a_0b_0+\alpha^2a_1b_1)+\alpha(a_0b_1+a_1b_0).
\]
The trace is the second coordinate, so
\(\operatorname{tr}(ab)=a_0b_1+a_1b_0\).

### Step 4. Verify perfection by an explicit dual basis

The pairings of \(1,\alpha\) are
\[
\operatorname{tr}(1)=0,\quad
\operatorname{tr}(\alpha)=1,\quad
\operatorname{tr}(\alpha^2)=0.
\]
Thus \(\alpha,1\) are the dual basis to \(1,\alpha\). More explicitly, if an \(R\)-linear functional has values \(u\) on \(1\) and \(v\) on \(\alpha\), the element \(v+\alpha u\) pairs with them to give exactly \(u,v\). This proves the map to the dual is both surjective and injective over \(R\) itself.

The trace is \((a-\tau(a))/(2\alpha)\), with the quotient understood through the divisibility already proved, not through a fraction-field extension.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization

`OAI.KLInvariance.ReflectionFrobenius.coordinates`: [Decomposition.lean:1504](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1504).

`OAI.KLInvariance.ReflectionFrobenius.trace`: [Decomposition.lean:1517](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1517).

`OAI.KLInvariance.ReflectionFrobenius.trace_mul`: [Decomposition.lean:1530](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1530).
