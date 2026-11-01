---
id: kl.algebra.saturated_image_hilbert
title: The Hilbert value of an actual saturated image
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.component_transport
- kl.algebra.hilbert_scalar_quotient
- kl.detail.hilbert_exactness
- kl.algebra.hilbert_image_exactness
- kl.algebra.scalar_quotient
- kl.detail.hilbert_values
lean:
  repository: openai-kl
  modules:
  - Support
  declarations:
  - OAI.KLInvariance.Hilbert.imageMap
  - OAI.KLInvariance.Hilbert.imageMap_surjective
  - OAI.KLInvariance.Hilbert.imageMap_ker
  - OAI.KLInvariance.Hilbert.map_homogeneous
  - OAI.KLInvariance.Hilbert.saturated_image_value
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1216
    format: lean-location
    note: OAI.KLInvariance.Hilbert.imageMap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1221
    format: lean-location
    note: OAI.KLInvariance.Hilbert.imageMap_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1227
    format: lean-location
    note: OAI.KLInvariance.Hilbert.imageMap_ker
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1243
    format: lean-location
    note: OAI.KLInvariance.Hilbert.map_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1256
    format: lean-location
    note: OAI.KLInvariance.Hilbert.saturated_image_value
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the integer degree, scalar regularity, image inclusion, convergence
    and parameter assumptions explicit, and are source hypotheses separated from derived
    applications?
  verdict: Checked generic coefficient and decomposition hypotheses, finite pieces
    of the domain, homogeneous saturated S, exact scalar kernel and scalar injectivity.
    Expanded the actual-image map, both kernel directions, graded exactness and the
    scalar shift; preserved q>0 with explicit summability.
tags:
- Kazhdan-Lusztig
- Hilbert-comparison
---

# The Hilbert value of an actual saturated image

Let \(k\) be a field and \(A\) a commutative \(k\)-algebra. Let \(M,N\) have compatible \(A\)- and \(k\)-actions and integer-indexed direct-sum decompositions. Suppose every \(M_n\) is finite-dimensional over \(k\).

Let \((A_r)_{r\in\mathbb Z}\) be homogeneous scalar subspaces acting compatibly on \(M\), so \(A_rM_s\subseteq M_{r+s}\). Choose \(d\in\mathbb Z\) and \(a\in A_d\). Let \(f:M\to N\) be \(A\)-linear of degree zero, with
\[
\ker f=aM.
\]
Let \(S\subseteq M\) be a homogeneous \(A\)-submodule, saturated with respect to \(a\):
\[
av\in S\quad\Longrightarrow\quad v\in S.
\]
Assume multiplication by \(a\) is injective on \(M\).

For \(q>0\), suppose the series
\[
H_S(q)=\sum_{n\in\mathbb Z}\dim_k(S\cap M_n)q^n
\]
converges. Then the actual image has Hilbert value
\[
H_{f(S)}(q)=(1-q^d)H_S(q).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Actual image pieces and exact scalar-image values.**

**OpenAI notes:** The comparison proof multiplies the upper-kernel Hilbert series by the linear-quotient factor and the correction degree shift. [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275), [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The general image-shift theorem constructs an actual isomorphism of homogeneous intersection pieces and reindexes a summable integer-indexed series. The saturated-image theorem separately identifies the restricted map’s kernel with the scalar image, applies degreewise exactness and subtracts its Hilbert value. [PositiveTransfer:273](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L273), [PositiveTransfer:300](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L300), [PositiveTransfer:316](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L316), [Support:1227](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1227), [Support:1256](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1256).

**Role in the proof:** The Blueprint explains both constructions and retains their distinct generic parameter hypotheses: nonzero q for the shift and positive q for saturated-image exactness, each with explicit summability.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Restrict to the actual image

Define
\[
f_S:S\longrightarrow f(S),\qquad v\longmapsto f(v).
\]
The map is surjective by the definition of the image. Write \(\pi_n^M,\pi_n^N\) for the component projections. Since \(S\) is homogeneous and \(f\) has degree zero, the [[node:kl.algebra.component_transport|component-transport theorem]] gives
\[
\pi_n^N(f(v))=f(\pi_n^M(v))\in f(S).
\]
Thus the image is homogeneous, and \(f_S\) preserves degrees. These are the source's `imageMap` and `map_homogeneous` constructions.

### Step 2. Identify the restricted kernel using saturation

If \(v\in S\) and \(f(v)=0\), the ambient kernel equality gives \(v=aw\) for some \(w\in M\). Since \(aw=v\in S\), saturation implies \(w\in S\). Therefore \(v\in aS\).

Conversely, for \(w\in S\), the vector \(aw\) lies in \(aM=\ker f\) and in \(S\), so it belongs to the kernel of \(f_S\). Hence
\[
\ker f_S=aS.
\]

### Step 3. Apply graded exactness to the image presentation

The scalar image \(aS\) is homogeneous, because multiplication by \(a\in A_d\) is homogeneous and \(S\) is homogeneous. Steps 1–2 give the degree-zero exact sequence
\[
0\longrightarrow aS\longrightarrow S
\xrightarrow{f_S}f(S)\longrightarrow0.
\]
Each \(S_n\) is finite-dimensional as a subspace of \(M_n\). Homogeneous preimages make the sequence exact in every degree, so the image pieces are finite-dimensional as well.

For \(q>0\), the [[node:kl.detail.hilbert_exactness|Hilbert exactness theorem]] applies to this surjection and the assumed summable domain series. It gives
\[
H_S(q)=H_{aS}(q)+H_{f(S)}(q).
\]

### Step 4. Compute the scalar image and subtract

Multiplication by \(a\) is injective on \(M\), hence on \(S\), and has degree \(d\). The [[node:kl.algebra.hilbert_scalar_quotient|scalar-image Hilbert theorem]] gives
\[
H_{aS}(q)=q^dH_S(q).
\]
Its nonzero-parameter hypothesis follows from \(q>0\), and it uses the same summable series of \(S\).

Substitute this equality into Step 3 and rearrange:
\[
H_{f(S)}(q)=H_S(q)-q^dH_S(q)
=(1-q^d)H_S(q).
\]

For a degree-one scalar, the factor is \(1-q\). For example, with \(A=k[X]\), \(M=S=A\), \(a=X\), and \(f:A\to A/(X)=k\), one obtains \(H_{f(S)}(q)=(1-q)/(1-q)=1\) for \(0<q<1\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Hilbert.imageMap`: [Support.lean:1216](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1216).

`OAI.KLInvariance.Hilbert.imageMap_surjective`: [Support.lean:1221](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1221).

`OAI.KLInvariance.Hilbert.imageMap_ker`: [Support.lean:1227](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1227).

`OAI.KLInvariance.Hilbert.map_homogeneous`: [Support.lean:1243](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1243).

`OAI.KLInvariance.Hilbert.saturated_image_value`: [Support.lean:1256](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1256).
