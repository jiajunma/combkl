---
id: kl.word.stalk_degree_exactness
title: Degreewise exact sequences and word-stalk dimensions
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.head_kernel_maps
- kl.word.head_kernel_degree
- kl.detail.hilbert_exactness
- kl.algebra.polynomial_hilbert
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.symmetricGrading_finite
  - OAI.KLInvariance.TitsSpace.bottCoordinatePiece_finite
  - OAI.KLInvariance.TitsSpace.bottStalkPiece_finite
  - OAI.KLInvariance.TitsSpace.bottStalk_finrank_ascent
  - OAI.KLInvariance.TitsSpace.bottStalk_finrank_descent
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1731
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.symmetricGrading_finite
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1735
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCoordinatePiece_finite
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1740
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkPiece_finite
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1744
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalk_finrank_ascent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:86
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalk_finrank_descent
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the gradings, scalar actions, coefficient variables and formal polynomial
    conclusions explicit?
  verdict: Read the finite homogeneous-piece instances and both finrank recurrences.
    Followed the source coefficient-product-subspace finiteness route, degreewise
    surjectivity and kernel-piece equivalences before rank-nullity.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Degreewise exact sequences and word-stalk dimensions

Fix a finite-generator Coxeter system and a finite basis of the extended realization, with linear coefficient generators in degree one. For a word \(\mathbf t\), define
\[
f_{\mathbf t,x}(n)=\dim_{\mathbb R}(M_{\mathbf t}^x)_n.
\]
These dimensions are finite.

For every integer \(n\), prepending a simple reflection \(s\) gives
\[
f_{s\mathbf t,x}(n)=
\begin{cases}
f_{\mathbf t,x}(n)+f_{\mathbf t,sx}(n-1),&\ell(x)<\ell(sx),\\
f_{\mathbf t,sx}(n)+f_{\mathbf t,x}(n-1),&\ell(sx)<\ell(x).
\end{cases}
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Degree-one kernels and shift conventions.**

**OpenAI notes:** The normalization proof temporarily assigns degree two to linear forms and uses \(M(k)^j=M^{j+k}\) for its shifted self-dual object. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The word construction keeps linear forms in degree one. Each kernel equivalence sends an old degree-\(n\) vector to degree \(n+1\). The local module-data convention is \(M(1)_n=M_{n-1}\). [GradedModules:1244](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1244), [BottSamelson:1618](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1618), [BottSamelson:2084](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L2084), [BottSamelson:1744](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1744).

**Role in the proof:** The old degree-\((n-1)\) piece contributes to the new degree-\(n\) kernel. Reindexing its Hilbert sum gives the factor \(q\) in the word-character recurrence.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Check finite-dimensionality of all pieces

A degree-\(n\) coefficient piece is zero for \(n<0\). For \(n\ge0\), it is spanned by monomials in finitely many variables whose exponents sum to \(n\). Each exponent is between \(0\) and \(n\), so there are finitely many such monomials.

A word has finitely many subexpressions. Its weight-coordinate module in a fixed degree is therefore a finite product of finite-dimensional coefficient pieces. The stalk piece is a real subspace of that product, and hence is finite-dimensional. This is the source's coefficient-piece, coordinate-piece and stalk-piece finiteness chain.

### Step 2. Restrict a head projection degree by degree

Let \(h:Z\to Q\) be either head projection, viewed as real-linear. It is surjective and preserves degree.

For \(q\in Q_n\), choose \(z\) with \(h(z)=q\), then take the degree-\(n\) component. Homogeneity gives
\[
h(\operatorname{pr}_n z)
=\operatorname{pr}_n(h(z))=q.
\]
Thus the restricted map \(Z_n\to Q_n\) is surjective.

Its kernel consists of the vectors in \(Z_n\) killed by \(h\), which is exactly the degree-\(n\) piece of \(\ker h\). Hence
\[
0\to(\ker h)_n\to Z_n\to Q_n\to0
\]
is an exact sequence of real vector spaces.

### Step 3. Substitute the ascent kernel

Suppose \(\ell(x)<\ell(sx)\). Use \(h_0:Z=M_{s\mathbf t}^x\to X=M_{\mathbf t}^x\). The [[node:kl.word.head_kernel_degree|degree-one kernel theorem]] identifies
\((K_0)_n\simeq(M_{\mathbf t}^{sx})_{n-1}\).
Thus Step 2 becomes
\[
0\to(M_{\mathbf t}^{sx})_{n-1}
\xrightarrow{\kappa_0}(M_{s\mathbf t}^{x})_n
\xrightarrow{h_0}(M_{\mathbf t}^{x})_n\to0.
\]
Rank-nullity in these finite-dimensional spaces gives the ascent formula.

### Step 4. Substitute the descent kernel

Suppose \(\ell(sx)<\ell(x)\). Use the real-linear map
\(h_1:Z\to Y=M_{\mathbf t}^{sx}\). Its kernel piece is
\((K_1)_n\simeq(M_{\mathbf t}^{x})_{n-1}\), giving
\[
0\to(M_{\mathbf t}^{x})_{n-1}
\xrightarrow{\kappa_1}(M_{s\mathbf t}^{x})_n
\xrightarrow{h_1}(M_{\mathbf t}^{sx})_n\to0.
\]
Rank-nullity gives the descent formula.

Simple multiplication changes length by one, so the two cases cover every \(x\). The shift \(n-1\) comes from the actual degree of the root in the kernel map.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.symmetricGrading_finite`: [BottSamelson.lean:1731](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1731).

`OAI.KLInvariance.TitsSpace.bottCoordinatePiece_finite`: [BottSamelson.lean:1735](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1735).

`OAI.KLInvariance.TitsSpace.bottStalkPiece_finite`: [BottSamelson.lean:1740](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1740).

`OAI.KLInvariance.TitsSpace.bottStalk_finrank_ascent`: [BottSamelson.lean:1744](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1744).

`OAI.KLInvariance.TitsSpace.bottStalk_finrank_descent`: [IntegralPairings.lean:86](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L86).
