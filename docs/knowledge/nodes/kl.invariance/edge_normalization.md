---
id: kl.comparison.edge_normalization
title: The edge degree gives a uniform positive transfer coefficient
kind: theorem
status: proved
primary_topic: kl.invariance
topics:
- kl.invariance
uses:
- kl.comparison.normalized_kernel
- kl.paths.plane_degree
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.Comparison.edge_scalar_identity
  - OAI.KLInvariance.Comparison.transferCoefficient_pos
  - OAI.KLInvariance.Comparison.stateScale_pos
  - OAI.KLInvariance.BruhatGraph.stateScale_positive
  - OAI.KLInvariance.BruhatGraph.edge_stateScale
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:535
    format: lean-location
    note: OAI.KLInvariance.Comparison.edge_scalar_identity
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:550
    format: lean-location
    note: OAI.KLInvariance.Comparison.transferCoefficient_pos
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:555
    format: lean-location
    note: OAI.KLInvariance.Comparison.stateScale_pos
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:595
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.stateScale_positive
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:603
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edge_stateScale
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the integer degree, scalar regularity, image inclusion, convergence
    and parameter assumptions explicit, and are source hypotheses separated from derived
    applications?
  verdict: Checked the integer-power identity under t!=0, strict positivity for 0<t<1,
    the actual length-degree substitution and the common polynomial-variable scale.
    Included cover and gap-three calculations with the same coefficient.
tags:
- Kazhdan-Lusztig
- Hilbert-comparison
---

# The edge degree gives a uniform positive transfer coefficient

Let \(m,n,k\in\mathbb Z\) satisfy
\[
m+2k=n-1.
\]
For every real \(t\ne0\),
\[
t^m(t^2)^k(1-t^2)=(t^{-1}-t)t^n.
\]

For the Coxeter-sheaf application, fix a finite-generator real Coxeter system \(W\), \(u\le_Wb\), and a finite real basis of its extended realization, giving \(N\) polynomial coordinates. For an edge \(e:x\to_Wy\) of \([u,b]_W\), with positive source root \(a_e\), take
\[
m=\ell_W(x)-\ell_W(b),\qquad
n=\ell_W(y)-\ell_W(b),\qquad
k=\deg(F_{x,a_e})
\]
The [[node:kl.paths.plane_degree|edge-degree theorem]] gives the required relation. Thus, with the state scales for a coefficient algebra in \(N\) variables,
\[
s_x(t)(t^2)^k(1-t^2)=T(t)s_y(t),
\qquad T(t)=t^{-1}-t.
\]
For \(0<t<1\), both every state scale \(s_x(t)\) and \(T(t)\) are strictly positive.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Equivalent parameter conventions.**

**OpenAI notes:** The comparison uses \(0<q<1\), scale \(q^{-d/2}(1-q)^N\), and transfer coefficient \(q^{-1/2}-q^{1/2}\). [eq:state](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L243), [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275).

**Lean (primary):** The comparison uses \(0<t<1\) and substitutes \(q=t^2\). Its scale is \(t^{-d}(1-t^2)^N\) and its transfer coefficient is \(t^{-1}-t\). [Dihedral:730](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L730), [PositiveTransfer:591](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L591), [PositiveTransfer:621](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L621), [EdgeLocalization:377](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L377), [EdgeLocalization:423](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L423), [PositiveTransfer:535](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L535), [PositiveTransfer:603](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L603).

**Role in the proof:** The substitution \(q=t^2\) identifies the two normalizations. Linear root labels have degree one throughout the calculation.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Combine the integer powers

Because \(t\ne0\), integer powers obey the product and exponent laws:
\[
(t^2)^k=t^{2k},\qquad
t^m(t^2)^k=t^{m+2k}=t^{n-1}.
\]
The last equality is the given relation among \(m,n,k\).

### Step 2. Extract the common transfer coefficient

Again using \(t\ne0\),
\[
t^{n-1}=t^nt^{-1}.
\]
Consequently
\[
\begin{aligned}
t^m(t^2)^k(1-t^2)
&=t^nt^{-1}(1-t^2)\\
&=t^n(t^{-1}-t)\\
&=(t^{-1}-t)t^n.
\end{aligned}
\]
This proves the elementary scalar identity, including negative integer exponents.

### Step 3. Verify positivity in the comparison range

If \(0<t<1\), then \(t^{-1}>1>t\), so \(T(t)>0\). Also \(1-t^2>0\), and \(t^r>0\) for every integer \(r\); for negative \(r\), it is a reciprocal of a positive power.

Thus
\[
(1-t^2)^N t^r>0
\]
for every natural \(N\) and integer \(r\). This gives positivity of every state scale.

### Step 4. Substitute the actual edge degrees

For an actual edge, the [[node:kl.paths.plane_degree|edge-degree theorem]] gives
\[
2k=\ell_W(y)-\ell_W(x)-1.
\]
Substitute the displayed \(m,n\) to get \(m+2k=n-1\). Multiply the scalar identity from Step 2 by the common factor \((1-t^2)^N\). The left and right sides become
\[
s_x(t)(t^2)^k(1-t^2)
\quad\text{and}\quad
T(t)s_y(t),
\]
respectively. This proves the state-scale identity.

For a cover, \(k=0\) and \(s_x/s_y=t^{-1}\), giving the coefficient \(t^{-1}(1-t^2)\). For a length gap of three, \(k=1\) and \(s_x/s_y=t^{-3}\), so the factor is \(t^{-3}t^2(1-t^2)\). Both equal \(T(t)\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Comparison.edge_scalar_identity`: [PositiveTransfer.lean:535](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L535).

`OAI.KLInvariance.Comparison.transferCoefficient_pos`: [PositiveTransfer.lean:550](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L550).

`OAI.KLInvariance.Comparison.stateScale_pos`: [PositiveTransfer.lean:555](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L555).

`OAI.KLInvariance.BruhatGraph.stateScale_positive`: [PositiveTransfer.lean:595](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L595).

`OAI.KLInvariance.BruhatGraph.edge_stateScale`: [PositiveTransfer.lean:603](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L603).
