---
id: kl.detail.quotient_image_free
title: Freeness of a saturated image over the edge quotient ring
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.detail.upper_quotient
- kl.sheaves.upward_kernel
- kl.algebra.kernel_saturation
- kl.algebra.scalar_quotient
- kl.algebra.scalar_quotient_basis
lean:
  repository: openai-kl
  modules:
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.ScalarQuotient.saturated_image_free
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:624
    format: lean-location
    note: OAI.KLInvariance.ScalarQuotient.saturated_image_free
  - artifact: openai-kl-paper
    locator: 5. Edge-image bound; edge:bound
    format: section
    note: The saturated upper-kernel quotient argument in the edge-image proof.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, finiteness and freeness hypotheses, original embedded
    submodules, localization multipliers and schedule assumptions explicit?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- global-inclusion
---

# Freeness of a saturated image over the edge quotient ring

Let \(R\) be a commutative ring, \(a\in R\), and \(M,N\) be \(R\)-modules. Suppose \(N\) also has a compatible \(R/(a)\)-action, so \(rv=\overline r\,v\). Let \(q:M\to N\) be \(R\)-linear, with
\[
\ker q=aM.
\]
Let \(L\subseteq M\) be finite free and saturated with respect to \(a\):
\[
av\in L\quad\Longrightarrow\quad v\in L.
\]
Then \(q(L)\), regarded as a module over \(R/(a)\), is free.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Compatible quotient actions and the actual free upper image.**

**OpenAI notes:** The notes identify the upper image with the selected upper kernel modulo the current root label. Saturation gives this quotient, and freeness of the upper kernel gives freeness over the edge coefficient ring. Multiplication by the nonzero correction then gives the free target. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The quotient action and its scalar tower are explicit. A finite free scalar presentation gives the edge-module basis. Regularity of the incoming label on every outgoing edge module gives saturation; Noetherian finiteness permits the finite quotient presentation. A separate same-carrier quotient-submodule construction and injective scalar-image map give freeness of the corrected target. [TerminalKernels:613](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L613), [TerminalKernels:624](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L624), [TerminalKernels:681](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L681), [TerminalKernels:691](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L691), [TerminalKernels:880](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L880).

**Role in the proof:** The Blueprint retains the precise coefficient ring of each freeness statement, all action compatibilities, the arbitrary outgoing selection and the finite-basis hypothesis used for finiteness.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Restrict the map to the chosen submodule

Let \(I=q(L)\). Restriction gives a surjection \(q_L:L\twoheadrightarrow I\). An element of its kernel is a vector \(v\in L\) with \(q(v)=0\).

The ambient kernel condition gives \(v=aw\) for some \(w\in M\). Since \(aw=v\in L\), saturation gives \(w\in L\). Thus every kernel element belongs to \(aL\). Conversely \(q(aw)=0\) for every \(w\in L\), so \(\ker q_L=aL\).

### Step 2. Write the quotient isomorphism explicitly

Define
\[
\theta:L/aL\longrightarrow I,\qquad [v]\longmapsto q(v).
\]
If \(v-v'=aw\), their images agree, so the map is well-defined. It is surjective because \(I=q(L)\). If \(\theta([v])=0\), Step 1 gives \(v\in aL\), so \([v]=0\). Thus it is injective.

The action of \(R/(a)\) is compatible with this map: replacing a scalar by another representative changes its product by an \(a\)-multiple, which is zero in both modules. Hence \(\theta\) is an \(R/(a)\)-linear isomorphism.

### Step 3. Reduce a basis and prove it remains a basis

Choose a finite \(R\)-basis \(e_1,\ldots,e_r\) of \(L\). Every vector in \(L/aL\) is a combination of their residue classes, so they span.

If \(\sum_i\overline c_i[e_i]=0\), lift the coefficients to \(c_i\in R\). The vector \(\sum_ic_ie_i\) belongs to \(aL\), so it equals \(a\sum_id_ie_i\). Uniqueness of basis coordinates gives \(c_i=ad_i\), hence every \(\overline c_i=0\). Thus the residue classes are independent.

They form a free \(R/(a)\)-basis, and the isomorphism in Step 2 transfers it to \(I\). This is the [[node:kl.algebra.scalar_quotient_basis|coordinate-reduction presentation theorem]] applied to the restricted map \(q_L\).

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L26).

## Lean formalization



`OAI.KLInvariance.ScalarQuotient.saturated_image_free`: [TerminalKernels.lean:624](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L624).
