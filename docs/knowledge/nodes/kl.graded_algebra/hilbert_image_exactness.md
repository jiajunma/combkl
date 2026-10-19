---
id: kl.algebra.hilbert_image_exactness
title: Hilbert additivity for the image of a homogeneous submodule
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.detail.hilbert_values
- kl.algebra.component_transport
- kl.algebra.homogeneous_subquotients
lean:
  repository: openai-kl
  modules:
  - HilbertSeries
  declarations:
  - OAI.KLInvariance.Hilbert.imagePieceMap
  - OAI.KLInvariance.Hilbert.imagePieceMap_surjective
  - OAI.KLInvariance.Hilbert.imageKernelEquiv
  - OAI.KLInvariance.Hilbert.finrank_image_exact
  - OAI.KLInvariance.Hilbert.value_image_exact
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:451
    format: lean-location
    note: OAI.KLInvariance.Hilbert.imagePieceMap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:459
    format: lean-location
    note: OAI.KLInvariance.Hilbert.imagePieceMap_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:476
    format: lean-location
    note: OAI.KLInvariance.Hilbert.imageKernelEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:492
    format: lean-location
    note: OAI.KLInvariance.Hilbert.finrank_image_exact
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:513
    format: lean-location
    note: OAI.KLInvariance.Hilbert.value_image_exact
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the grading, scalar, finiteness and convergence hypotheses retained?
  verdict: Read imagePieceMap, its homogeneous lifting proof, the kernel equivalence
    and value_image_exact. Kept finiteness on the source pieces and derived image
    finiteness from the surjection.
tags:
- Kazhdan-Lusztig
- graded-algebra
---

# Hilbert additivity for the image of a homogeneous submodule

Let \(k\) be a field and \(A\) a commutative \(k\)-algebra. Let \(f:M\to N\) be degree zero between compatibly graded \(A\)-modules, and let \(S\subseteq M\) be a homogeneous \(A\)-submodule. Assume every \(M_n\) is finite-dimensional.

For \(q>0\), if the intersection series of \(S\) converges, then
\[
H_S(q)=H_{S\cap\ker f}(q)+H_{f(S)}(q).
\]
Both series on the right converge.

*Proof.*

### Step 1. Define the map on the degree-n intersections

Restriction gives a \(k\)-linear map
\[
f_n:S\cap M_n\longrightarrow f(S)\cap N_n,\qquad m\longmapsto f(m).
\]
The image lies in \(f(S)\) by definition and in \(N_n\) because \(f\) preserves degree.

### Step 2. Lift a homogeneous image vector inside S

Take \(y=f(s)\in f(S)\cap N_n\), with \(s\in S\). Homogeneity of \(S\) gives \(\pi_n(s)\in S\cap M_n\), and component transport gives
\[
f(\pi_n(s))=\pi_n(f(s))=\pi_n(y)=y.
\]
Thus \(f_n\) is surjective.

Its kernel consists exactly of the vectors in \(S\cap\ker f\cap M_n\). The correspondence is the identity on the underlying vector.

### Step 3. Apply finite-dimensional rank–nullity

The domain \(S\cap M_n\) is finite-dimensional as a subspace of \(M_n\). Its image is therefore finite-dimensional, and rank–nullity gives
\[
\dim_k(S\cap M_n)
=\dim_k(S\cap\ker f\cap M_n)
+\dim_k(f(S)\cap N_n).
\]
This supplies finiteness of the image pieces directly.

### Step 4. Dominate both numerical series

Multiply by \(q^n>0\). Each right-hand term is nonnegative and at most the left-hand term. Since the series for \(S\) converges, comparison proves convergence of the kernel-intersection and image series.

### Step 5. Sum the identities

Summing the degreewise equality is now valid and gives the stated Hilbert identity.

For an edge restriction \(\rho_e\), take \(S\) to be a partial outgoing kernel. Then \(S\cap\ker\rho_e\) is the kernel after adding that edge condition, and \(f(S)\) is its actual restriction image. The identity measures the change by that image's Hilbert value.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Hilbert.imagePieceMap`: [HilbertSeries.lean:451](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L451).

`OAI.KLInvariance.Hilbert.imagePieceMap_surjective`: [HilbertSeries.lean:459](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L459).

`OAI.KLInvariance.Hilbert.imageKernelEquiv`: [HilbertSeries.lean:476](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L476).

`OAI.KLInvariance.Hilbert.finrank_image_exact`: [HilbertSeries.lean:492](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L492).

`OAI.KLInvariance.Hilbert.value_image_exact`: [HilbertSeries.lean:513](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L513).
