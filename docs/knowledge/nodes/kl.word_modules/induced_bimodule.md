---
id: kl.word.induced_bimodule
title: Right actions, balance and symmetry under tensor induction
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.notes.perfect_pairings
- kl.notes.tensor_pairing
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.FrobeniusDuality.restrictedRight
  - OAI.KLInvariance.FrobeniusDuality.inducedRight
  - OAI.KLInvariance.FrobeniusDuality.inducedRight_tmul
  - OAI.KLInvariance.FrobeniusDuality.inducedPairing_balanced
  - OAI.KLInvariance.FrobeniusDuality.inducedPairing_symmetric
  - OAI.KLInvariance.FrobeniusDuality.inducedBimodule
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:319
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.restrictedRight
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:330
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedRight
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:333
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedRight_tmul
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:336
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedPairing_balanced
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:355
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedPairing_symmetric
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:369
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedBimodule
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read restrictedRight/inducedRight and both tensor-induction proofs. Expanded
    well-definedness, ring-homomorphism laws and the finite bilinear extension, with
    symmetry and balance hypotheses explicit.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Right actions, balance and symmetry under tensor induction

Let \(\eta:R\to A\) be a finite free Frobenius extension with trace \(t\) and trace duality \(D\). Let \(N\) be a paired bimodule over \(A\), with symmetric perfect pairing \(B_N\) and commuting right action satisfying
\[
B_N(m\cdot r,n)=B_N(m,n\cdot r).
\]
The tensor-induced module \(N'=A\otimes_R N\) becomes a paired bimodule with
\[
(a\otimes m)\cdot r=a\otimes(m\cdot r).
\]
Its perfect pairing \(B'\) is symmetric and balanced for this action.

*Proof.*

### Step 1. Define the right action on the tensor product

Fix \(r\in A\). The old map \(\rho(r):m\mapsto m\cdot r\) is \(A\)-linear, hence \(R\)-linear. In particular, for \(s\in R\),
\[
(\eta(s)m)\cdot r=\eta(s)(m\cdot r).
\]
Therefore the images of the two sides of a tensor relation agree:
\[
a\eta(s)\otimes(m\cdot r)
=a\otimes\eta(s)(m\cdot r)
=a\otimes((\eta(s)m)\cdot r).
\]
Additivity in each tensor factor also holds. This defines an \(A\)-linear endomorphism \(\rho'(r)\) of \(N'\).

### Step 2. Verify the action laws

On a pure tensor,
\[
\rho'(1)(a\otimes m)=a\otimes m,
\]
and additivity of the old action gives
\(\rho'(r+s)=\rho'(r)+\rho'(s)\).
The multiplication identity follows from the old ring homomorphism:
\[
\rho'(rs)(a\otimes m)
=a\otimes\rho(rs)m
=a\otimes\rho(r)(\rho(s)m)
=\rho'(r)\rho'(s)(a\otimes m).
\]
The zero identity follows in the same way. Pure tensors generate \(N'\), so these are endomorphism identities. Thus \(\rho'\) is a unital ring homomorphism \(A\to\operatorname{End}_A(N')\).

Its \(A\)-linearity also gives commutation with the new left action:
\[
c((a\otimes m)\cdot r)
=(ca)\otimes(m\cdot r)
=(c(a\otimes m))\cdot r.
\]

### Step 3. Prove balance on pure tensors

Using the induced pairing formula,
\[
\begin{aligned}
B'((a\otimes m)\cdot r,b\otimes n)
&=ab\,\eta(t(B_N(m\cdot r,n)))\\
&=ab\,\eta(t(B_N(m,n\cdot r)))\\
&=B'(a\otimes m,(b\otimes n)\cdot r).
\end{aligned}
\]
The middle equality is precisely the old balance identity.

### Step 4. Prove symmetry on pure tensors

Old symmetry and commutativity of \(A\) give
\[
\begin{aligned}
B'(a\otimes m,b\otimes n)
&=ab\,\eta(t(B_N(m,n)))\\
&=ba\,\eta(t(B_N(n,m)))\\
&=B'(b\otimes n,a\otimes m).
\end{aligned}
\]

### Step 5. Extend both identities to arbitrary vectors

Write \(x=\sum_i a_i\otimes m_i\) and \(y=\sum_j b_j\otimes n_j\), with finite sums. Bilinearity gives
\[
B'(x,y)=\sum_{i,j}B'(a_i\otimes m_i,b_j\otimes n_j).
\]
The right action is additive, so the balance expression expands into the same double sum with \(\rho'\) applied termwise. Applying Step 3 to each pair proves balance for \(x,y\). Applying Step 4 to each pair and exchanging the two finite indices proves symmetry.

Finite freeness and perfection come from the [[node:kl.notes.tensor_pairing|tensor-pairing theorem]]. Together with the action just constructed and these two identities, they fill the fields of inducedBimodule.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.FrobeniusDuality.restrictedRight`: [Frobenius.lean:319](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L319).

`OAI.KLInvariance.FrobeniusDuality.inducedRight`: [Frobenius.lean:330](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L330).

`OAI.KLInvariance.FrobeniusDuality.inducedRight_tmul`: [Frobenius.lean:333](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L333).

`OAI.KLInvariance.FrobeniusDuality.inducedPairing_balanced`: [Frobenius.lean:336](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L336).

`OAI.KLInvariance.FrobeniusDuality.inducedPairing_symmetric`: [Frobenius.lean:355](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L355).

`OAI.KLInvariance.FrobeniusDuality.inducedBimodule`: [Frobenius.lean:369](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L369).
