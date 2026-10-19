---
id: kl.algebra.perfect_inverse_degree
title: Homogeneous functionals have homogeneous pairing representatives
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.grading_components
- kl.detail.graded_maps_shifts
- kl.notes.perfect_pairings
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.Graded.perfect_inverse_of_homogeneous_functional
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2285
    format: lean-location
    note: OAI.KLInvariance.Graded.perfect_inverse_of_homogeneous_functional
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
- duality_and_characters
---

# Homogeneous functionals have homogeneous pairing representatives

Let \(A\) be a commutative algebra over a field \(k\), and let \(M\) be an \(A\)-module. Equip the underlying \(k\)-vector spaces \(A\) and \(M\) with integer gradings
\[
A=\bigoplus_j A_j,\qquad M=\bigoplus_i M_i.
\]
Suppose an \(A\)-linear isomorphism \(D:M\xrightarrow{\sim}M^*\) gives a perfect pairing with
\[
\langle M_i,M_j\rangle\subseteq A_{i+j-L},
\qquad \langle m,n\rangle=D(m)(n),
\]
for a fixed integer \(L\).

Let \(\lambda:M\to A\) be an \(A\)-linear functional homogeneous of degree \(r\), meaning \(\lambda(M_j)\subseteq A_{j+r}\) for every \(j\). Then
\[
D^{-1}(\lambda)\in M_{r+L}.
\]

*Proof.*

### Step 1. Isolate the proposed homogeneous component

Put \(m=D^{-1}(\lambda)\), and write \(m=\sum_i m_i\) in its finite homogeneous decomposition. We will prove \(D(m_{r+L})=\lambda\); injectivity of \(D\) will then give \(m=m_{r+L}\).

### Step 2. Test the pairing on a homogeneous vector

Fix \(n\in M_j\). Bilinearity gives
\[
\lambda(n)=\langle m,n\rangle=\sum_i\langle m_i,n\rangle.
\]
The term indexed by \(i\) lies in \(A_{i+j-L}\). These degrees are distinct as \(i\) varies. The left side lies in \(A_{j+r}\).

Take the degree-\((j+r)\) component of both sides. The left side remains \(\lambda(n)\). On the right, the unique index with
\(i+j-L=j+r\) is \(i=r+L\). Thus
\[
\lambda(n)=\langle m_{r+L},n\rangle.
\]
If that component of \(m\) is zero, the same equality follows with a zero right side.

### Step 3. Extend the equality to all vectors

Every \(n\in M\) is a finite sum of homogeneous vectors. Both \(\lambda\) and \(D(m_{r+L})\) are additive, so the equality in Step 2 holds on their sum. They are therefore equal as functionals:
\[
D(m_{r+L})=\lambda=D(m).
\]
Injectivity gives \(m=m_{r+L}\in M_{r+L}\).

### Step 4. Evaluate the shift on the one-edge section module

In the basis \(e_0=(1,1)\), \(e_1=(\alpha,-\alpha)\), the one-edge section pairing has matrix
\(\begin{pmatrix}0&1\\ 1&0\end{pmatrix}\) and shift \(L=1\).
The coordinate functionals have degrees \(0,-1\). The pairing representatives are
\[
D^{-1}(e_0^*)=e_1,\qquad D^{-1}(e_1^*)=e_0,
\]
of degrees \(0+1=1\) and \(-1+1=0\), respectively.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.Graded.perfect_inverse_of_homogeneous_functional`: [IntegralPairings.lean:2285](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2285).
