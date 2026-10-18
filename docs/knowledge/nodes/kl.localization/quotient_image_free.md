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
    locator: Related paper context; edge:lattice
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
- localization
---

# Freeness of a saturated image over the edge quotient ring

Let \(q:M\to N\) be \(R\)-linear, with \(N\) an \(R/(a)\)-module and
\[
\ker q=aM.
\]
Let \(L\subseteq M\) be finite free and saturated with respect to \(a\):
\[
av\in L\quad\Longrightarrow\quad v\in L.
\]
Then \(q(L)\), regarded as a module over \(R/(a)\), is free.

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

They form a free \(R/(a)\)-basis, and the isomorphism in Step 2 transfers it to \(I\).

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L26).

## Lean formalization



`OAI.KLInvariance.ScalarQuotient.saturated_image_free`: [TerminalKernels.lean:624](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L624).
