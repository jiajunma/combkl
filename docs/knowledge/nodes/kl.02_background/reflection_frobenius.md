---
id: kl.notes.reflection_frobenius
title: The rank-two Frobenius extension associated with a reflection
kind: theorem
status: proved
primary_topic: kl.02_background
topics:
- kl.02_background
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

For \(a\in A\), its even part \((a+\tau(a))/2\) is fixed by \(\tau\). Write \(a-\tau(a)=\alpha d\). Applying \(\tau\), using involutivity and the sign of \(\alpha\), and cancelling \(\alpha\) shows that \(d\) is fixed. Thus
\[
a=\frac{a+\tau(a)}2+\alpha\frac d2
\]
has the required form. Applying \(\tau\) to two such expressions and subtracting proves uniqueness.

Because \(\alpha^2\in R\), multiplication gives
\[
\operatorname{tr}\bigl((a_0+\alpha a_1)(b_0+\alpha b_1)\bigr)
=a_0b_1+a_1b_0.
\]
The pairing matrix in the basis \(1,\alpha\) is
\(\begin{pmatrix}0&1\\1&0\end{pmatrix}\), which is invertible over \(R\). This proves perfectness without passing to a fraction field.

For a simple reflection acting on the coefficient ring, this gives the extension \(A^s\subseteq A\) used in Bott–Samelson tensor induction. The trace normalization here selects the \(\alpha\)-coefficient; it is one half of \((a-s(a))/\alpha\).

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization

`OAI.KLInvariance.ReflectionFrobenius.coordinates`: [Decomposition.lean:1504](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1504).

`OAI.KLInvariance.ReflectionFrobenius.trace`: [Decomposition.lean:1517](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1517).

`OAI.KLInvariance.ReflectionFrobenius.trace_mul`: [Decomposition.lean:1530](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1530).
