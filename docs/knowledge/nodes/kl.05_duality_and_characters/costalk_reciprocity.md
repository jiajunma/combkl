---
id: kl.detail.costalk_reciprocity
title: The grading shift in stalk–costalk reciprocity
kind: theorem
status: proved
primary_topic: kl.05_duality_and_characters
topics:
- kl.05_duality_and_characters
uses:
- kl.detail.costalk_duality
- kl.detail.graded_character
- kl.sheaves.hilbert_free
lean:
  repository: openai-kl
  modules:
  - Support
  declarations:
  - OAI.KLInvariance.BruhatGraph.costalk_hilbert_of_duality
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1712
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.costalk_hilbert_of_duality
  - artifact: openai-kl-paper
    locator: Related paper context; bg:normalization
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
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

# The grading shift in stalk–costalk reciprocity

Let a section duality have degree shift \(L\): its pairing sends degrees \(i,j\) to degree \(i+j-L\). Let \(n_x\) be the number of incoming edges at \(x\), and let the stalk have homogeneous generator degrees \(d_i\). The induced basis of its full outgoing kernel has degrees
\[
L-n_x-d_i.
\]
Consequently, for \(0<q<1\) and \(N\) polynomial variables,
\[
H_{K_x}(q)
=q^{L-n_x}\operatorname{ch}(B^x;q^{-1})(1-q)^{-N}.
\]

*Proof.*

The dual basis has degrees \(-d_i\). The inverse stalk–costalk equivalence introduces the pairing shift \(L\), then removes the degree \(n_x\) of the incoming-label product. This gives the displayed kernel basis degrees. Apply the homogeneous-basis Hilbert formula and factor \(q^{L-n_x}\) out of the finite sum.

For the boundary sheaf on \([1,b]\), one has \(L=\ell(b)\) and \(n_x=\ell(x)\). Its kernel-character numerator is therefore
\(q^{d(x,b)}\operatorname{ch}(B^x;q^{-1})\).
This concerns the actual stalk character; identifying it with a KL polynomial is not required for this reciprocal identity.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization



`OAI.KLInvariance.BruhatGraph.costalk_hilbert_of_duality`: [Support.lean:1712](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1712).
