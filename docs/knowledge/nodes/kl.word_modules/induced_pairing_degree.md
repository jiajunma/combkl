---
id: kl.word.induced_pairing_degree
title: The basis and pairing degree of one reflection tensor step
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.reflection_coordinates
- kl.word.reflection_trace_degree
- kl.notes.tensor_pairing
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.FrobeniusDuality.inducedBasis
  - OAI.KLInvariance.FrobeniusDuality.inducedBasis_apply
  - OAI.KLInvariance.FrobeniusDuality.inducedPairing_basis
  - OAI.KLInvariance.FrobeniusDuality.inducedPairing_basis_homogeneous
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:569
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedBasis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:574
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedBasis_apply
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:580
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedPairing_basis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:602
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedPairing_basis_homogeneous
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read inducedBasis, its pure-tensor formula, basis pairing and homogeneous
    degree statement. Preserved the generic basis-degree hypothesis and separated
    it from a pre-existing grading on N.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# The basis and pairing degree of one reflection tensor step

Let \(A\) be a commutative domain over a characteristic-zero field \(k\), equipped with an integer grading by \(k\)-subspaces, with \(1\in A_0\) and \(A_iA_j\subseteq A_{i+j}\). Let \((\tau,\alpha)\) be reflection data such that \(\alpha\in A_1\) and \(\tau\) preserves the grading. Put \(R=A^\tau\), and let \(t\) be the reflection trace.

Let \(N\) be a finite free paired \(A\)-module with basis \((b_j)_{j\in J}\). Assign integers \(d_j\) to its basis vectors. Suppose that for some integer \(L\),
\[
B_N(b_j,b_k)\in A_{d_j+d_k-L}
\qquad(j,k\in J).
\]
Then the induced module \(N'=A\otimes_R N\) has basis
\[
e_{\varepsilon,j}=1\otimes r_\varepsilon b_j,
\qquad r_0=1,\quad r_1=\alpha,\quad \varepsilon\in\{0,1\},
\]
and its pairing satisfies
\[
B'(e_{\varepsilon,j},e_{\delta,k})
\in A_{(\varepsilon+d_j)+(\delta+d_k)-(L+1)}.
\]
Here \(d_j\) is a basis-degree assignment; the displayed hypothesis is the precise condition on the old pairing entries.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit tensor construction underlying the duality.**

**OpenAI notes:** The grading-normalization proof starts from a normalized self-dual projective, uses the cited moment-graph/Soergel equivalence and character theorem, and translates doubled degrees back to the degree-one convention. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The local construction begins with the simple reflection fixed algebra and the trace extracting the root coefficient, normalized by t(alpha)=1. It recovers linear functionals through the trace, extends the resulting duality by tensor product, and proves a one-degree pairing shift for each letter. [Decomposition:1588](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1588), [Frobenius:168](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L168), [Frobenius:270](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L270), [Frobenius:602](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L602).

**Role in the proof:** These nodes supply the actual word-module pairing and its homogeneous basis calculation. The boundary-pairing construction subsequently transports this pairing to a boundary summand. The source uses roots of degree one throughout this tensor calculation.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Construct the new basis

The [[node:kl.word.reflection_coordinates|reflection coordinate theorem]] makes \((r_0,r_1)\) an \(R\)-basis of \(A\). The product-basis construction makes
\((r_\varepsilon b_j)\) an \(R\)-basis of \(N\). Extending scalars gives the claimed \(A\)-basis \(e_{\varepsilon,j}\) of \(N'\).

The source constructs inducedBasis by exactly these two operations: the scalar-tower basis followed by base change. Its inducedBasis_apply formula identifies each vector with the displayed pure tensor.

### Step 2. Evaluate its pairing

The tensor-pairing formula at outer coefficients \(1,1\) gives
\[
B'(e_{\varepsilon,j},e_{\delta,k})
=t\bigl(B_N(r_\varepsilon b_j,r_\delta b_k)\bigr),
\]
viewing the trace value in \(A\) through the inclusion \(R\to A\). Bilinearity of the old pairing yields
\[
B'(e_{\varepsilon,j},e_{\delta,k})
=t\bigl(r_\varepsilon r_\delta B_N(b_j,b_k)\bigr).
\]

### Step 3. Compute the degree inside the trace

The reflection basis elements satisfy
\(r_\varepsilon\in A_\varepsilon\) and \(r_\delta\in A_\delta\). Multiplying these two homogeneous elements with the assumed pairing entry gives
\[
r_\varepsilon r_\delta B_N(b_j,b_k)
\in A_{\varepsilon+\delta+d_j+d_k-L}.
\]

### Step 4. Apply the one-degree trace shift

The reflection trace lowers the degree by one, so the expression from Step 2 lies in
\[
A_{\varepsilon+\delta+d_j+d_k-L-1}.
\]
Rearranging the index gives
\[
\varepsilon+\delta+d_j+d_k-L-1
=(\varepsilon+d_j)+(\delta+d_k)-(L+1),
\]
as required. Thus assigning degree \(\varepsilon+d_j\) to the new basis increases the pairing shift from \(L\) to \(L+1\).

Starting from \(N=A\), basis \(1\), assigned degree \(0\), and \(L=0\), one step gives basis degrees \(0,1\) and pairing shift \(1\). Iterating this result is the basis-level induction in the word-pairing degree theorem.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.FrobeniusDuality.inducedBasis`: [Frobenius.lean:569](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L569).

`OAI.KLInvariance.FrobeniusDuality.inducedBasis_apply`: [Frobenius.lean:574](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L574).

`OAI.KLInvariance.FrobeniusDuality.inducedPairing_basis`: [Frobenius.lean:580](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L580).

`OAI.KLInvariance.FrobeniusDuality.inducedPairing_basis_homogeneous`: [Frobenius.lean:602](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L602).
