---
id: kl.algebra.hilbert_scalar_quotient
title: Hilbert values of a regular homogeneous scalar image and quotient
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.scalar_quotient
- kl.algebra.component_transport
- kl.detail.hilbert_exactness
- kl.detail.hilbert_values
lean:
  repository: openai-kl
  modules:
  - Support
  declarations:
  - OAI.KLInvariance.Hilbert.scalarDegreeMap
  - OAI.KLInvariance.Hilbert.scalarDegreeMap_surjective
  - OAI.KLInvariance.Hilbert.scalarDegreeMap_injective
  - OAI.KLInvariance.Hilbert.scalarDegreeEquiv
  - OAI.KLInvariance.Hilbert.scalar_value
  - OAI.KLInvariance.Hilbert.scalarQuotient_value
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1124
    format: lean-location
    note: OAI.KLInvariance.Hilbert.scalarDegreeMap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1132
    format: lean-location
    note: OAI.KLInvariance.Hilbert.scalarDegreeMap_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1146
    format: lean-location
    note: OAI.KLInvariance.Hilbert.scalarDegreeMap_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1153
    format: lean-location
    note: OAI.KLInvariance.Hilbert.scalarDegreeEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1161
    format: lean-location
    note: OAI.KLInvariance.Hilbert.scalar_value
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1186
    format: lean-location
    note: OAI.KLInvariance.Hilbert.scalarQuotient_value
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the grading, scalar, finiteness and convergence hypotheses retained?
  verdict: Read scalarDegreeMap, its bijectivity, scalar_value and scalarQuotient_value.
    Preserved integer degree, injective scalar action, q nonzero for the image formula
    and positive q/finite pieces for the quotient.
tags:
- Kazhdan-Lusztig
- graded-algebra
---

# Hilbert values of a regular homogeneous scalar image and quotient

Let \(k\) be a field and \(A\) a commutative \(k\)-algebra. Use the source Hilbert values for a compatibly graded \(A\)-module \(M\), and let \(a\in A_d\) be homogeneous of integer degree \(d\). Assume multiplication by \(a\) on \(M\) is injective.

If \(q\ne0\) and the series for \(M\) converges, then
\[
H_{aM}(q)=q^dH_M(q).
\]
If also the pieces of \(M\) are finite-dimensional and \(q>0\), then
\[
H_{M/aM}(q)=(1-q^d)H_M(q).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit convergence and degreewise comparison.**

**OpenAI notes:** The graded-rank paragraph gives \(\operatorname{Hilb}(M;q)=\operatorname{grk}_A(M;q)/(1-q)^N\) for a homogeneous free basis. The comparison evaluates Hilbert series at \(0<q<1\), uses the factor \(1-q\) for a degree-one scalar quotient, and detects equality through a positive quotient deficit. [sec:background](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2), [eq:state](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L243), [eq:image-equality](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L370).

**Lean (primary):** The implementation defines real integer-indexed terms from the finite ranks of intersections with ambient pieces. Finite homogeneous covers prove piece finiteness and summability. Degreewise exactness proves the scalar-quotient factor, and inclusion plus homogeneity of the larger subspace turns one equal positive Hilbert value into equality. [ModuleAlgebra:506](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L506), [HilbertSeries:245](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L245), [Support:1186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1186), [ModuleAlgebra:549](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L549).

**Role in the proof:** The KB distinguishes the formal coefficient series, its convergent real value and the free-module basis-degree polynomial. The factor \((1-q)^N\) removes the coefficient-ring contribution; \(1-q\) records quotienting by a regular degree-one label.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Identify the pieces of the scalar image

Multiplication gives
\[
M_{n-d}\longrightarrow(aM)_n,\qquad m\longmapsto am.
\]
It is injective by the assumption on multiplication.

For surjectivity, take \(av\in M_n\). Component transport gives
\[
a\,\pi_{n-d}(v)=\pi_n(av)=av.
\]
Thus every homogeneous image vector comes from \(M_{n-d}\). This is a \(k\)-linear equivalence, so
\(\dim_k(aM)_n=\dim_kM_{n-d}\).

### Step 2. Shift the convergent series

Translate the integer index by \(d\):
\[
\begin{aligned}
H_{aM}(q)
&=\sum_n\dim_kM_{n-d}\,q^n\\
&=q^d\sum_m\dim_kM_m\,q^m
=q^dH_M(q).
\end{aligned}
\]
The identity \(q^{m+d}=q^mq^d\) uses \(q\ne0\). Translation and multiplication by the fixed scalar preserve convergence.

### Step 3. Apply homogeneous exactness to the quotient map

The image \(aM\) is homogeneous by the scalar component formula. The quotient map has degree zero, is surjective and has kernel \(aM\).

For finite-dimensional pieces and positive \(q\), [[node:kl.detail.hilbert_exactness|Hilbert exactness]] gives
\[
H_M(q)=H_{aM}(q)+H_{M/aM}(q).
\]
Substitute Step 2 and rearrange to obtain the quotient formula.

### Step 4. Specialize to a degree-one label

For \(d=1\),
\[
H_{M/aM}(q)=(1-q)H_M(q).
\]
For a nonzero linear label \(a\) and a graded free module over \(A=k[X_1,\ldots,X_N]\), multiplication is injective because the coefficient ring is a domain. Hence
\[
H_{M/aM}(q)
=(1-q)\frac{\operatorname{grk}_A(M;q)}{(1-q)^N}
=\frac{\operatorname{grk}_A(M;q)}{(1-q)^{N-1}}.
\]


For \(A=k[X]\), \(a=X\), and \(M=A\oplus A(2)\), the quotient has basis classes in degrees zero and two over \(k\). Its Hilbert value is \(1+q^2\), equal to
\[
(1-q)\frac{1+q^2}{1-q}.
\]
This is the factor used when the sheaf comparison passes from an upper kernel to its edge quotient.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Hilbert.scalarDegreeMap`: [Support.lean:1124](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1124).

`OAI.KLInvariance.Hilbert.scalarDegreeMap_surjective`: [Support.lean:1132](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1132).

`OAI.KLInvariance.Hilbert.scalarDegreeMap_injective`: [Support.lean:1146](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1146).

`OAI.KLInvariance.Hilbert.scalarDegreeEquiv`: [Support.lean:1153](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1153).

`OAI.KLInvariance.Hilbert.scalar_value`: [Support.lean:1161](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1161).

`OAI.KLInvariance.Hilbert.scalarQuotient_value`: [Support.lean:1186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1186).
