---
id: kl.notes.tensor_pairing
title: Transporting a perfect pairing through tensor induction
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.notes.perfect_pairings
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.FrobeniusDuality.inducedModule
  - OAI.KLInvariance.FrobeniusDuality.inducedModule_pairing_tmul
  - OAI.KLInvariance.FrobeniusDuality.inducedPairing_balanced
  - OAI.KLInvariance.FrobeniusDuality.inducedPairing_symmetric
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:270
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedModule
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:276
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedModule_pairing_tmul
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:336
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedPairing_balanced
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:355
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedPairing_symmetric
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

# Transporting a perfect pairing through tensor induction

Let \(R\subseteq A\) be a finite free Frobenius extension with trace \(\operatorname{tr}:A\to R\). If \(N\) is a finite free paired \(A\)-module, tensor induction produces a paired \(A\)-module \(A\otimes_R N\). Its pairing on pure tensors is
\[
\langle a\otimes m,b\otimes n\rangle
=ab\,\operatorname{tr}(\langle m,n\rangle),
\]
with the trace value included back into \(A\).

*Proof.*

### Step 1. Restrict the original pairing through the Frobenius trace

Let \(B_N:N\times N\to A\) be the perfect pairing, and define the \(R\)-valued pairing
\(b(m,n)=\operatorname{tr}(B_N(m,n))\).
The trace is \(R\)-linear, so \(b\) is \(R\)-bilinear.

Choose an \(R\)-basis \(a_i\) of the finite free Frobenius extension and its trace-dual basis \(a_i^\vee\):
\(\operatorname{tr}(a_ia_j^\vee)=\delta_{ij}\).
Choose an \(A\)-basis \(n_j\) of \(N\) and its pairing-dual basis \(n_j^\vee\). Then
\[
b(a_in_j,a_h^\vee n_k^\vee)
=\operatorname{tr}(a_ia_h^\vee\delta_{jk})
=\delta_{ih}\delta_{jk}.
\]
Thus the restricted pairing is perfect; its two dual bases have been exhibited.

### Step 2. Extend scalars and derive the formula

On \(A\otimes_RN\), define
\[
B(a\otimes m,b\otimes n)=ab\,\operatorname{tr}(B_N(m,n)).
\]
This respects the tensor relation: for \(r\in R\), moving \(r\) from the first scalar factor to \(m\) gives the same value by \(R\)-linearity of the trace. The same verification works in the second argument. Bilinearity therefore extends the formula to arbitrary tensors.

The bases from Step 1 extend to the \(A\)-bases \(1\otimes a_in_j\) and \(1\otimes a_i^\vee n_j^\vee\), with the same identity pairing matrix. Hence the induced pairing is perfect.

### Step 3. Check symmetry

If \(B_N(m,n)=B_N(n,m)\), then on pure tensors
\[
ab\,\operatorname{tr}(B_N(m,n))
=ba\,\operatorname{tr}(B_N(n,m)).
\]
The coefficient algebra is commutative. Every tensor is a finite sum of pure tensors, so bilinearity proves symmetry for arbitrary arguments.

### Step 4. Check balance of the induced right action

Let the original right action satisfy
\(B_N(mr,n)=B_N(m,nr)\).
The induced action changes only the second tensor factor:
\((a\otimes m)r=a\otimes(mr)\).
Consequently
\[
B((a\otimes m)r,b\otimes n)
=ab\,\operatorname{tr}(B_N(mr,n))
=ab\,\operatorname{tr}(B_N(m,nr))
=B(a\otimes m,(b\otimes n)r).
\]
Again finite bilinear expansion gives the statement for arbitrary tensors. These calculations establish the properties preserved at each Bott–Samelson induction step.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization

`OAI.KLInvariance.FrobeniusDuality.inducedModule`: [Frobenius.lean:270](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L270).

`OAI.KLInvariance.FrobeniusDuality.inducedModule_pairing_tmul`: [Frobenius.lean:276](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L276).

`OAI.KLInvariance.FrobeniusDuality.inducedPairing_balanced`: [Frobenius.lean:336](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L336).

`OAI.KLInvariance.FrobeniusDuality.inducedPairing_symmetric`: [Frobenius.lean:355](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L355).
