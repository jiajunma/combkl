---
id: kl.word.uniform_diagonal_projector
title: A diagonal operator with one scalar on a chosen block
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.diagonal_stabilizer
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.FiniteCharacterLocalization.uniform_projector
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1700
    format: lean-location
    note: OAI.KLInvariance.FiniteCharacterLocalization.uniform_projector
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the bilinear form, coefficient ring, finite coordinate presentation
    and lifting hypotheses explicit?
  verdict: Read uniform_projector and its two product evaluations. Preserved arbitrary
    X with finite C and the common scalar multiplier; explained the scaled projection
    identity rather than asserting unnormalized idempotence.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# A diagonal operator with one scalar on a chosen block

Let \(R\) be a commutative ring, \(L\subseteq\prod_{x\in X}E_x\) a submodule, and \(C\subseteq X\) a finite subset. Suppose \(f\in\operatorname{Stab}(L)\) and \(f(x)=0\) for \(x\notin C\).

Put
\[
d=\prod_{c\in C}f(c).
\]
There is a stable weight \(g\) with
\[
g(x)=d\quad(x\in C),\qquad g(x)=0\quad(x\notin C).
\]
Explicitly,
\[
g=d-\prod_{c\in C}(f(c)-f),
\]
where each \(f(c)\) is regarded as a constant function on \(X\).

*Proof.*

### Step 1. Construct the weight in the stabilizer algebra

For each \(c\), the constant function \(f(c)\) is stable. Subtracting the stable function \(f\) gives another stable function \(f(c)-f\). Their finite product is stable, and so is its difference from the constant function \(d\). Hence the displayed \(g\) lies in \(\operatorname{Stab}(L)\).

### Step 2. Evaluate on the selected block

If \(x\in C\), the factor with \(c=x\) in the product has value
\(f(x)-f(x)=0\). Thus the product is zero at \(x\), and \(g(x)=d\).

### Step 3. Evaluate outside the block

If \(x\notin C\), then \(f(x)=0\). The product at \(x\) is
\[
\prod_{c\in C}(f(c)-0)=d.
\]
Thus \(g(x)=d-d=0\).

### Step 4. Describe its action on a vector

For \(m\in L\), stability gives \(D_gm\in L\). Its coordinates are
\[
(D_gm)_x=
\begin{cases}
d\,m_x,&x\in C,\\
0,&x\notin C.
\end{cases}
\]
Thus this operator selects the block with a common scalar multiplier. Coordinatewise, it satisfies \(D_g^2=dD_g\). If \(d\) is invertible in a coefficient localization, \(d^{-1}D_g\) is an idempotent projection there.

The formulas use the empty-product convention \(1\); when \(C\) is empty, the constructed weight is the zero function.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.FiniteCharacterLocalization.uniform_projector`: [IntegralPairings.lean:1700](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1700).
