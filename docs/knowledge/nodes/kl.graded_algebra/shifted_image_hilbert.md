---
id: kl.algebra.shifted_image_hilbert
title: Homogeneous image pieces and their Hilbert degree shift
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.component_transport
- kl.algebra.homogeneous_subquotients
- kl.detail.hilbert_values
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.Hilbert.shifted_map_homogeneous
  - OAI.KLInvariance.Hilbert.shiftedImagePieceMap
  - OAI.KLInvariance.Hilbert.shiftedImagePieceMap_surjective
  - OAI.KLInvariance.Hilbert.shiftedImagePieceEquiv
  - OAI.KLInvariance.Hilbert.shifted_image_value
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:262
    format: lean-location
    note: OAI.KLInvariance.Hilbert.shifted_map_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:273
    format: lean-location
    note: OAI.KLInvariance.Hilbert.shiftedImagePieceMap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:284
    format: lean-location
    note: OAI.KLInvariance.Hilbert.shiftedImagePieceMap_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:300
    format: lean-location
    note: OAI.KLInvariance.Hilbert.shiftedImagePieceEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:316
    format: lean-location
    note: OAI.KLInvariance.Hilbert.shifted_image_value
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the integer degree, scalar regularity, image inclusion, convergence
    and parameter assumptions explicit, and are source hypotheses separated from derived
    applications?
  verdict: Read all shifted-image maps and the value proof; preserved generic compatible
    scalar actions, integer degree, q!=0 and summability. Explained image homogeneity,
    the component preimage, piece equivalence, finrank coefficients and the translation
    of the bilateral series.
tags:
- Kazhdan-Lusztig
- Hilbert-comparison
---

# Homogeneous image pieces and their Hilbert degree shift

Let \(k\) be a field, \(A\) a commutative \(k\)-algebra, and \(M,N\) be \(A\)-modules with compatible \(k\)-actions and direct-sum decompositions
\[
M=\bigoplus_{n\in\mathbb Z}M_n,\qquad N=\bigoplus_{n\in\mathbb Z}N_n.
\]
Write \(\pi_n^M,\pi_n^N\) for their degree-\(n\) component projections. Let \(S\subseteq M\) be an \(A\)-submodule closed under all homogeneous component maps, and let \(f:M\to N\) be \(A\)-linear of integer degree \(d\):
\[
f(M_n)\subseteq N_{n+d}.
\]
Then the image \(f(S)\) is homogeneous, and for every \(n\) the map
\[
S\cap M_{n-d}\longrightarrow f(S)\cap N_n,\qquad v\longmapsto f(v)
\]
is surjective. If \(f\) is injective, this map is a \(k\)-linear isomorphism.

Write
\[
h_S(n)=\operatorname{finrank}_k(S\cap M_n),\qquad
H_S(q)=\sum_{n\in\mathbb Z}h_S(n)q^n.
\]
Here `finrank` is the source's natural-number rank: it is the usual dimension for finite-dimensional pieces and zero for infinite-dimensional pieces. In the graded polynomial-module applications, the pieces are finite-dimensional.

If \(f\) is injective, \(q\in\mathbb R\setminus\{0\}\), and the series defining \(H_S(q)\) is absolutely summable, then
\[
H_{f(S)}(q)=q^dH_S(q).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Actual image pieces and exact scalar-image values.**

**OpenAI notes:** The comparison proof multiplies the upper-kernel Hilbert series by the linear-quotient factor and the correction degree shift. [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275), [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The general image-shift theorem constructs an actual isomorphism of homogeneous intersection pieces and reindexes a summable integer-indexed series. The saturated-image theorem separately identifies the restricted map’s kernel with the scalar image, applies degreewise exactness and subtracts its Hilbert value. [PositiveTransfer:273](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L273), [PositiveTransfer:300](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L300), [PositiveTransfer:316](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L316), [Support:1227](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1227), [Support:1256](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1256).

**Role in the proof:** The Blueprint explains both constructions and retains their distinct generic parameter hypotheses: nonzero q for the shift and positive q for saturated-image exactness, each with explicit summability.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Compute a component of an image vector

The [[node:kl.algebra.component_transport|component-transport theorem]] gives, for every \(v\in M\),
\[
\pi_n^N(f(v))=f(\pi_{n-d}^M(v)).
\]
If \(v\in S\), homogeneity of \(S\) puts \(\pi_{n-d}^M(v)\) in \(S\). Hence every component of \(f(v)\) belongs to \(f(S)\). This proves homogeneity of the image.

### Step 2. Construct the map on the actual homogeneous pieces

If \(v\in S\cap M_{n-d}\), the degree hypothesis gives
\(f(v)\in N_{(n-d)+d}=N_n\), and its image membership is witnessed by \(v\in S\). Thus the displayed piece map is well-defined and \(k\)-linear. This is `shiftedImagePieceMap`.

Take \(w\in f(S)\cap N_n\). Choose \(v\in S\) with \(f(v)=w\). Then
\[
f(\pi_{n-d}^M(v))
=\pi_n^N(f(v))
=\pi_n^N(w)
=w.
\]
The chosen component belongs to \(S\cap M_{n-d}\), proving surjectivity.

### Step 3. Use injectivity to identify the piece ranks

If \(f\) is injective, equal values of the piece map imply equal vectors in \(M\). The surjective piece map is therefore an isomorphism, giving
\[
h_{f(S)}(n)=h_S(n-d).
\]
This is the rank equality supplied by `shiftedImagePieceEquiv`.

### Step 4. Translate the summable integer-indexed series

The translation \(m\mapsto m+d\) is a bijection of \(\mathbb Z\). Using Step 3 and that bijection,
\[
\begin{aligned}
H_{f(S)}(q)
&=\sum_{n\in\mathbb Z}h_S(n-d)q^n\\
&=\sum_{m\in\mathbb Z}h_S(m)q^{m+d}\\
&=q^d\sum_{m\in\mathbb Z}h_S(m)q^m
=q^dH_S(q).
\end{aligned}
\]
The identity \(q^{m+d}=q^mq^d\) uses \(q\ne0\). The assumed summability is preserved by translation and multiplication by the fixed scalar \(q^d\); this also proves summability of the image series.

As an illustrative calculation, let \(A=k[X]\) and \(M=Ae\), with \(\deg(e)=-1\). Multiplication by \(X\) is an injective degree-one map. For \(0<q<1\),
\[
H_M(q)=\frac{q^{-1}}{1-q},\qquad
H_{XM}(q)=\frac1{1-q}=qH_M(q).
\]
The negative generator degree appears in the integer-indexed series exactly as the shift formula predicts.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Hilbert.shifted_map_homogeneous`: [PositiveTransfer.lean:262](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L262).

`OAI.KLInvariance.Hilbert.shiftedImagePieceMap`: [PositiveTransfer.lean:273](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L273).

`OAI.KLInvariance.Hilbert.shiftedImagePieceMap_surjective`: [PositiveTransfer.lean:284](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L284).

`OAI.KLInvariance.Hilbert.shiftedImagePieceEquiv`: [PositiveTransfer.lean:300](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L300).

`OAI.KLInvariance.Hilbert.shifted_image_value`: [PositiveTransfer.lean:316](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L316).
