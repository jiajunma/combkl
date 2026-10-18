---
id: kl.detail.costalk_reciprocity
title: The grading shift in stalk–costalk reciprocity
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
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

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate statement.**

**OpenAI notes:** The grading-normalization proposition identifies the stalk graded rank with the canonical KL polynomial and uses the Elias–Williamson character theorem through the cited moment-graph bridges. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The development defines the equality of actual stalk characters and canonical KL polynomials as StalkCharacterObligation. The unconditional theorem used in the main route is R-reciprocity for the actual character. The local strict half-degree implication retains an explicit nonzero-diagonal hypothesis. [SheafMorphisms:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219), [DyerPaths:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L62), [PositiveTransfer:186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L186).

**Role in the proof:** The comparison uses the actual character C and its proved R-reciprocity. Canonical P is handled by the later polynomial-rigidity induction. The local degree result applies to a diagonal coefficient satisfying its stated nonvanishing hypothesis.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Record the stalk basis and its dual degrees

Choose homogeneous generators \(m_i\) of \(B^x\) of degrees \(d_i\). The dual basis functional \(\lambda_i\) has degree \(-d_i\): applied to an element of degree \(n\), it extracts a coefficient in \(A_{n-d_i}\).

Let the global pairing have degree \(-L\), so it sends section degrees \(r,s\) to scalar degree \(r+s-L\).

### Step 2. Compute the degree of the supported representative

The functional \(\lambda_i\circ\mathrm{ev}_x\) sends a homogeneous section of degree \(s\) to degree \(s-d_i\). If its perfect-pairing representative has degree \(r\), the pairing instead gives degree \(r+s-L\). Matching these degrees gives
\(r=L-d_i\).

The equivalence in [[node:kl.detail.costalk_duality]] identifies a kernel vector with a supported section by multiplication by \(\beta_x\), the incoming-label product. Every factor has degree one, so \(\deg\beta_x=n_x\). Therefore the kernel vector corresponding to \(\lambda_i\) has degree
\[
L-d_i-n_x.
\]
Homogeneity of the inverse duality is essential to this calculation.

### Step 3. Apply the homogeneous-basis Hilbert formula

The kernel vectors form a basis, because they are the inverse images of a dual basis under a linear equivalence. Hence
\[
H_{K_x}(q)=
\left(\sum_iq^{L-n_x-d_i}\right)(1-q)^{-N}
=q^{L-n_x}\left(\sum_iq^{-d_i}\right)(1-q)^{-N}.
\]
The sum in parentheses is exactly \(\operatorname{ch}(B^x;q^{-1})\). This proves the claimed identity for \(0<q<1\), where all Hilbert series converge.

### Step 4. Specialize the shift on the lower Bruhat ideal

For the actual sheaf on \([1,b]\), the pairing shift is \(L=\ell(b)\). Incoming edges at \(x\) correspond to the reflections lowering \(x\); the inversion count is \(\ell(x)\), so \(n_x=\ell(x)\). The numerator becomes
\[
q^{d(x,b)}C_{x,b}(q^{-1}).
\]
Each kernel basis vector has nonnegative degree, since it lies in a nonnegative stalk. Therefore \(d_i\le d(x,b)\). This also gives the weak degree bound that permits interpreting this reciprocal expression as a polynomial reflection. It does not give the strict KL half-degree bound.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization



`OAI.KLInvariance.BruhatGraph.costalk_hilbert_of_duality`: [Support.lean:1712](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1712).
