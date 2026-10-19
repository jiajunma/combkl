---
id: kl.algebra.eigenvalue_difference
title: A scalar difference annihilates a pair-projection quotient
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.pair_projection
lean:
  repository: openai-kl
  modules:
  - Decomposition
  declarations:
  - OAI.KLInvariance.PairProjection.difference_annihilates
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:213
    format: lean-location
    note: OAI.KLInvariance.PairProjection.difference_annihilates
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read difference_annihilates and the endpoint-surjectivity/kernel identities
    it uses. Expanded the actual witness Tn-bn and all quotient signs.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# A scalar difference annihilates a pair-projection quotient

Let \(R\) be a commutative ring, and let \(f:N\to X\) and \(g:N\to Y\) be surjective \(R\)-linear maps. Form the pair-projection quotient
\[
Q=(X\oplus Y)/\{(f(n),g(n)):n\in N\},
\]
with maps \(\ell(x)=[(x,0)]\) and \(u(y)=-[(0,y)]\).

Suppose \(T:N\to N\) is \(R\)-linear and \(a,b\in R\) satisfy
\[
f(Tn)=a f(n),\qquad g(Tn)=b g(n)\qquad(n\in N).
\]
Then \((a-b)q=0\) for every \(q\in Q\).

*Proof.*

### Step 1. Represent the quotient class by one endpoint

The map \(\ell\) is surjective because \(g\) is. To see this directly, write a quotient element as \([(x,y)]\), choose \(n_0\) with \(g(n_0)=y\), and subtract its pair relation:
\[
[(x,y)]=[(x-f(n_0),0)].
\]
Thus write \(q=\ell(x_0)\).

### Step 2. Lift the endpoint and cancel the second projection

Surjectivity of \(f\) supplies \(n\) with \(f(n)=x_0\). Put
\[
h=Tn-bn.
\]
The two given action identities imply
\[
f(h)=a f(n)-b f(n)=(a-b)x_0,\qquad
g(h)=b g(n)-b g(n)=0.
\]
Therefore \(((a-b)x_0,0)\) belongs to the pair relation.

### Step 3. Take its quotient class

The pair from Step 2 has zero quotient class. By linearity of \(\ell\),
\[
(a-b)q=(a-b)\ell(x_0)=\ell((a-b)x_0)=0.
\]
This proves the claim. In the word-module application, \(T\) is right multiplication by one coefficient, while \(a,b\) are its coefficient characters at two weights.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.PairProjection.difference_annihilates`: [Decomposition.lean:213](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L213).
