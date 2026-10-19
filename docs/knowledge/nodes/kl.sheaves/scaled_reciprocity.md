---
id: kl.duality.scaled_reciprocity
title: Scaled reciprocity and its restriction to an upper interval
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.duality.scaled_stalk
- kl.duality.actual_character_reciprocity
- kl.duality.boundary_kernel_character
- kl.foundations.rtilde
- kl.hecke.polynomial_reflection
lean:
  repository: openai-kl
  modules:
  - EdgeLocalization
  declarations:
  - OAI.KLInvariance.BruhatGraph.scaledStalk_reciprocity_inverse
  - OAI.KLInvariance.BruhatGraph.scaledStalk_reciprocity
  - OAI.KLInvariance.BruhatGraph.scaledStalk_reciprocity_upper
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:381
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.scaledStalk_reciprocity_inverse
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:423
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.scaledStalk_reciprocity
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:430
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.scaledStalk_reciprocity_upper
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read both reciprocal-parameter formulas and the filtered-subtype reindexing
    for the upper interval. Expanded the integer exponent cancellation and retained
    the arbitrary scalar field and original boundary-character vector.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Scaled reciprocity and its restriction to an upper interval

Fix the actual boundary character on \([1,b]\) in a finite-generator Coxeter system. Write \(c_x^b(t)=t^{\ell(x)-\ell(b)}C_{x,b}(t^2)\) for its scaled actual-stalk character, and let \(\widetilde R_{x,z}\) be the normalized R-polynomial family. Integer coefficients are evaluated in the indicated field.

For \(x\in[1,b]\) and a nonzero parameter \(v\) in any field,
\[
c_x^b(v^{-1})
=\sum_{z\in[1,b]}\widetilde R_{x,z}(v-v^{-1})\,c_z^b(v).
\]
Equivalently, for \(t\ne0\),
\[
c_x^b(t)
=\sum_{z\in[1,b]}\widetilde R_{x,z}(t^{-1}-t)\,c_z^b(t^{-1}).
\]
For \(x\in[a,b]\), the second sum can be restricted to \(z\in[a,b]\), using the same characters from the boundary sheaf on \([1,b]\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Equivalent parameter conventions.**

**OpenAI notes:** The comparison uses \(0<q<1\), scale \(q^{-d/2}(1-q)^N\), and transfer coefficient \(q^{-1/2}-q^{1/2}\). [eq:state](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L243), [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275).

**Lean (primary):** The comparison uses \(0<t<1\) and substitutes \(q=t^2\). Its scale is \(t^{-d}(1-t^2)^N\) and its transfer coefficient is \(t^{-1}-t\). [Dihedral:730](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L730), [PositiveTransfer:591](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L591), [PositiveTransfer:621](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L621), [EdgeLocalization:377](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L377), [EdgeLocalization:423](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L423).

**Role in the proof:** The substitution \(q=t^2\) identifies the two normalizations. Linear root labels have degree one throughout the calculation.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Evaluate actual-character reciprocity at the square parameter

Put \(d_x=\ell(b)-\ell(x)\). Evaluate the integer polynomial reciprocity identity at \(q=v^2\). The degree bound permits reciprocal evaluation of reflection, giving
\[
(v^2)^{d_x}C_{x,b}(v^{-2})
=\sum_{z\in[1,b]}R_{x,z}(v^2)C_{z,b}(v^2).
\]

### Step 2. Normalize the left side

Multiply by \(v^{-d_x}\). Since \(v\ne0\), integer powers obey the exponent laws:
\[
v^{-d_x}(v^2)^{d_x}=v^{d_x}=(v^{-1})^{-d_x}.
\]
The left side is therefore \(c_x^b(v^{-1})\).

### Step 3. Normalize each R-polynomial term

The square-parameter normalization gives
\[
R_{x,z}(v^2)
=v^{\ell(z)-\ell(x)}
 \widetilde R_{x,z}(v-v^{-1}).
\]
For \(d_z=\ell(b)-\ell(z)\), the scalar exponents satisfy
\[
-d_x+\ell(z)-\ell(x)
=\ell(z)-\ell(b)=-d_z.
\]
Thus each right-hand term becomes
\[
\widetilde R_{x,z}(v-v^{-1})
\,v^{-d_z}C_{z,b}(v^2)
=\widetilde R_{x,z}(v-v^{-1})c_z^b(v).
\]
This proves the first identity.

### Step 4. Invert the parameter

Apply the first identity with \(v=t^{-1}\). Then \(v^{-1}=t\), and the normalized R argument becomes \(t^{-1}-t\). This gives the second identity.

### Step 5. Restrict the sum to an upper interval

Let \(a\le x\le b\). If a vertex \(z\le b\) does not satisfy \(a\le z\), then \(x\le z\) is impossible: it would imply \(a\le x\le z\).

The support of \(\widetilde R\) therefore makes its coefficient at this \(z\) zero. Remove all such terms. The remaining vertices are exactly \([a,b]\), with the same underlying group elements and the same actual-stalk values \(c_z^b(t^{-1})\).

This is the source's upper-interval formula. The character vector is the restriction of the original \([1,b]\) vector, which is the vector used in the later schedule comparison.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.scaledStalk_reciprocity_inverse`: [EdgeLocalization.lean:381](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L381).

`OAI.KLInvariance.BruhatGraph.scaledStalk_reciprocity`: [EdgeLocalization.lean:423](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L423).

`OAI.KLInvariance.BruhatGraph.scaledStalk_reciprocity_upper`: [EdgeLocalization.lean:430](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L430).
