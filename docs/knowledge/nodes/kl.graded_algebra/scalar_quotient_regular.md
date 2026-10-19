---
id: kl.algebra.scalar_quotient_regular
title: Regular scalars on a quotient of a finite free module
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.scalar_quotient
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  declarations:
  - OAI.KLInvariance.FiniteFreeScalar.exists_smul_iff
  - OAI.KLInvariance.FiniteFreeScalar.scalar_quotient_regular
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:898
    format: lean-location
    note: OAI.KLInvariance.FiniteFreeScalar.exists_smul_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:924
    format: lean-location
    note: OAI.KLInvariance.FiniteFreeScalar.scalar_quotient_regular
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read the finite-basis scalar divisibility criterion and scalar_quotient_regular.
    Preserved the general commutative ring, prime-element and exact-kernel assumptions
    and reproduced the coordinate argument.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Regular scalars on a quotient of a finite free module

Let \(R\) be a commutative ring, \(M\) a finite free \(R\)-module with basis
\(b_1,\ldots,b_d\), and \(q:M\to N\) a surjective linear map. Let \(\alpha\in R\) be prime and suppose
\[
\ker q=\alpha M.
\]
If \(\alpha\nmid\beta\), then multiplication by \(\beta\) on \(N\) is injective.

Here primality means that \(\alpha\) is a nonzero nonunit and
\(\alpha\mid uv\) implies \(\alpha\mid u\) or \(\alpha\mid v\).
The kernel equality means exactly that \(q(m)=0\) if and only if \(m=\alpha n\) for some \(n\in M\).

*Proof.*

### Step 1. Detect scalar divisibility in basis coordinates

Write \(m=\sum_i m_i b_i\). If \(m=\alpha n\), linearity of coordinates gives
\(m_i=\alpha n_i\) for every \(i\).

Conversely, if every \(m_i\) is divisible by \(\alpha\), choose \(n_i\) with \(m_i=\alpha n_i\), and put \(n=\sum_i n_i b_i\). The sum is finite and has \(\alpha n=m\). Thus
\[
m\in\alpha M\quad\Longleftrightarrow\quad
\alpha\mid m_i\text{ for every }i.
\]
This is the source's exists_smul_iff criterion.

### Step 2. Lift a vector killed by the scalar

Suppose \(\beta v=0\) in \(N\). Surjectivity gives \(m\in M\) with \(q(m)=v\). Then
\[
q(\beta m)=\beta q(m)=\beta v=0.
\]
The kernel hypothesis supplies \(n\in M\) with \(\beta m=\alpha n\).

### Step 3. Divide each lifted coefficient

Taking the \(i\)-th basis coordinate gives
\[
\beta m_i=\alpha n_i.
\]
Hence \(\alpha\mid\beta m_i\). Primality and \(\alpha\nmid\beta\) imply \(\alpha\mid m_i\) for every \(i\). Step 1 gives \(m\in\alpha M=\ker q\), so \(v=q(m)=0\).

### Step 4. Recover injectivity

If \(\beta v=\beta w\), then \(\beta(v-w)=0\). Step 3 gives \(v-w=0\), hence \(v=w\).

For example, let \(R=k[X,Y]\), \(M=R^d\), and let \(q\) reduce each coordinate modulo \(X\). Its kernel is \(XM\). Since \(X\nmid Y\), multiplication by \(Y\) is injective on the quotient. The proof above performs this cancellation by lifting coordinates to \(R\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.FiniteFreeScalar.exists_smul_iff`: [BottSamelson.lean:898](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L898).

`OAI.KLInvariance.FiniteFreeScalar.scalar_quotient_regular`: [BottSamelson.lean:924](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L924).
