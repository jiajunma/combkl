---
id: kl.comparison.edge_increment
title: The normalized single-edge inequality and its equality criterion
kind: theorem
status: proved
primary_topic: kl.invariance
topics:
- kl.invariance
uses:
- kl.comparison.normalized_kernel
- kl.comparison.edge_normalization
- kl.comparison.raw_edge_increment
- kl.local.edge_factor_action_properties
- kl.local.edge_inclusion
- kl.detail.transported_schedule
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.BruhatGraph.normalized_edge_increment_le
  - OAI.KLInvariance.BruhatGraph.normalized_edge_increment_eq_iff
  - OAI.KLInvariance.Comparison.scaled_increment_eq_iff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:621
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.normalized_edge_increment_le
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:637
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.normalized_edge_increment_eq_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:562
    format: lean-location
    note: OAI.KLInvariance.Comparison.scaled_increment_eq_iff
  - artifact: openai-kl-paper
    locator: 6. Reciprocity and simultaneous induction; sec:induction
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the integer degree, scalar regularity, image inclusion, convergence
    and parameter assumptions explicit, and are source hypotheses separated from derived
    applications?
  verdict: Replaced the compressed parent with the exact one-system BoundarySheaf,
    arbitrary selections and conditional image-inclusion setup. Expanded both normalized
    inequality and iff criterion via positive scaling and cancellation; kept upper-kernel
    freeness only in the separate chronological application.
tags:
- Kazhdan-Lusztig
- Hilbert-comparison
---

# The normalized single-edge inequality and its equality criterion

Fix a finite-generator real Coxeter system \(W\), \(u\le_Wb\), a finite real basis of the extended realization and its polynomial coefficient algebra \(A\). Let \(\mathcal B\) be a boundary sheaf on \([u,b]_W\).

For an edge \(e:x\to y\) with positive source root \(a_e\), choose arbitrary outgoing selections \(F,H\) at \(x,y\). Let
\[
I=\rho_e^-(K_x(F)),\qquad J=\rho_e^+(K_y(H)),
\]
and let \(\mu_e\) be multiplication on the actual edge module by the correction lift \(F_{x,a_e}\). Assume the embedded image inclusion
\[
I\subseteq\mu_e(J).
\]
Write \(H_x(F;q)\) for the kernel Hilbert value. With \(N\) the cardinality of the chosen coefficient basis, the state scale and normalized kernel value are
\[
s_x(t)=(1-t^2)^N t^{\ell_W(x)-\ell_W(b)},
\qquad D_x(t,F)=s_x(t)H_x(F;t^2).
\]
For every \(0<t<1\), they satisfy
\[
D_x(t,F)\le
D_x(t,F\cup\{e\})+T(t)D_y(t,H),
\qquad T(t)=t^{-1}-t.
\]
Equality at the chosen \(t\) holds if and only if
\[
I=\mu_e(J).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Equivalent parameter conventions.**

**OpenAI notes:** The comparison uses \(0<q<1\), scale \(q^{-d/2}(1-q)^N\), and transfer coefficient \(q^{-1/2}-q^{1/2}\). [eq:state](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L243), [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275).

**Lean (primary):** The comparison uses \(0<t<1\) and substitutes \(q=t^2\). Its scale is \(t^{-d}(1-t^2)^N\) and its transfer coefficient is \(t^{-1}-t\). [Dihedral:730](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L730), [PositiveTransfer:591](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L591), [PositiveTransfer:621](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L621), [EdgeLocalization:377](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L377), [EdgeLocalization:423](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L423), [PositiveTransfer:535](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L535), [PositiveTransfer:603](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L603).

**Role in the proof:** The substitution \(q=t^2\) identifies the two normalizations. Linear root labels have degree one throughout the calculation.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Apply the raw Hilbert increment at q=t squared

Set \(q=t^2\). The assumptions \(0<t<1\) give \(0<q<1\). The actual correction map is homogeneous and injective, with degree
\[
k=\deg(F_{x,a_e})
=\frac{\ell_W(y)-\ell_W(x)-1}{2}.
\]
The [[node:kl.comparison.raw_edge_increment|raw edge-increment theorem]] applies to the actual boundary sheaf and the supplied inclusion:
\[
H_x(F;q)-H_x(F\cup\{e\};q)
\le q^k(1-q)H_y(H;q).
\]
It also states that equality in this raw formula is equivalent to \(I=\mu_e(J)\).

### Step 2. Multiply by the positive state scale

The [[node:kl.comparison.edge_normalization|edge-normalization theorem]] gives \(s_x(t)>0\). Multiplying the raw inequality by that positive number preserves its direction:
\[
s_x(t)H_x(F;t^2)-s_x(t)H_x(F\cup\{e\};t^2)
\le s_x(t)(t^2)^k(1-t^2)H_y(H;t^2).
\]
The same theorem identifies the factor on the right as \(T(t)s_y(t)\). By the definitions of the normalized kernel values, this becomes
\[
D_x(t,F)-D_x(t,F\cup\{e\})
\le T(t)D_y(t,H).
\]
Moving the subtracted term to the right proves the stated inequality.

### Step 3. Recover the raw equality by cancelling a nonzero scale

Suppose the normalized inequality is an equality. Substitute the definitions and the state-scale identity to obtain
\[
s_x(t)H_x(F;t^2)
=s_x(t)H_x(F\cup\{e\};t^2)
+s_x(t)\bigl((t^2)^k(1-t^2)\bigr)H_y(H;t^2).
\]
The factor \(s_x(t)\) is nonzero. Divide by it and move the second term to the left. This gives exactly the raw equality in Step 1.

Conversely, multiplying that raw equality by \(s_x(t)\) and applying the same factor identity gives the normalized equality. This is the source's `scaled_increment_eq_iff` cancellation.

### Step 4. Apply the actual image equality criterion

Step 1 identifies raw equality with \(I=\mu_e(J)\). Step 3 identifies normalized equality with raw equality. Combining the two equivalences proves the asserted criterion for the two actual embedded images.

## Application to a chronological step

Take the canonical boundary sheaf restricted from \([1,b]_W\), an interval order isomorphism to a second finite-generator system, and a chronological suffix consisting of \(e\) followed by \(p\). Set
\[
F=\mathcal R_p(x),\qquad H=\mathcal R_p(y).
\]
If the upper selected kernel \(K_y(H)\) is free over \(A\), the [[node:kl.local.edge_inclusion|schedule edge-inclusion theorem]] supplies the premise \(I\subseteq\mu_e(J)\).

The condition set before processing \(e\) is \(F\cup\{e\}\) at \(x\), and remains \(H\) at \(y\). At every other vertex it is unchanged as well. Thus the theorem gives the one-coordinate update bound used in the full schedule comparison, with the same positive coefficient \(T(t)\) at each edge.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.normalized_edge_increment_le`: [PositiveTransfer.lean:621](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L621).

`OAI.KLInvariance.BruhatGraph.normalized_edge_increment_eq_iff`: [PositiveTransfer.lean:637](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L637).

`OAI.KLInvariance.Comparison.scaled_increment_eq_iff`: [PositiveTransfer.lean:562](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L562).
