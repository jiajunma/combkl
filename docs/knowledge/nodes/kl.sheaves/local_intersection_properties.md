---
id: kl.duality.local_intersection_properties
title: Image, symmetry, and grading of the local intersection map
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.local_intersection
- kl.sheaves.costalk_pairing_symmetry
- kl.sheaves.costalk_duality_degree
- kl.sheaves.boundary_sheaf
- kl.algebra.dual_basis_degrees
- kl.algebra.positive_ideal
- kl.detail.costalk_reciprocity
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.BruhatGraph.localIntersection_injective
  - OAI.KLInvariance.BruhatGraph.localIntersection_range
  - OAI.KLInvariance.BruhatGraph.localIntersection_minimal
  - OAI.KLInvariance.BruhatGraph.localIntersection_homogeneous
  - OAI.KLInvariance.BruhatGraph.localIntersection_symmetric
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:140
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.localIntersection_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:146
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.localIntersection_range
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:160
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.localIntersection_minimal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:167
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.localIntersection_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:180
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.localIntersection_symmetric
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read all five actual localIntersection properties and kernelMinimal_iff.
    Expanded both image containments, the assignment-to-kernel conversion, the incoming-edge
    shift, inverse symmetry and the matrix-coordinate calculation.
tags:
- Kazhdan-Lusztig
- graded-duality
---

# Image, symmetry, and grading of the local intersection map

Fix a finite-generator Coxeter system, its polynomial coefficient algebra \(A\), and the actual normalized boundary sheaf \(B(b)\) on \([1,b]\). At \(x\in[1,b]\), let \(M=B(b)^x\), let \(K_x\) be the full outgoing kernel, and let
\[
I_x:M^*\to M,\qquad I_x=\iota_x\kappa_x^{-1}
\]
be the local intersection map from the constructed symmetric section duality. Put \(d=\ell(b)-\ell(x)\).

The map is injective and \(\operatorname{im}I_x=K_x\). It satisfies
\[
\lambda(I_x\mu)=\mu(I_x\lambda).
\]
If \(\lambda(M_j)\subseteq A_{j+r}\) for every \(j\), then
\[
I_x\lambda\in M_{r+d}.
\]
At every proper vertex \(x<b\),
\[
\operatorname{im}I_x\subseteq A_+M.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate degree statement.**

**OpenAI notes:** The normalization proposition identifies stalk graded ranks with canonical KL polynomials using the cited character theorem and a conversion from degree-two to degree-one labels. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253), [eq:bg-ranks](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L257).

**Lean (primary):** The actual local intersection map is constructed from integral stalk–costalk duality. Boundary minimality puts its image in the positive ideal, and the strict degree theorem assumes that the specified diagonal coefficient is nonzero. [PositiveTransfer:132](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L132), [PositiveTransfer:160](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L160), [PositiveTransfer:186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L186).

**Role in the proof:** The local calculation gives \(2d_i<\ell(b)-\ell(x)\) for the basis generator named in that nonzero-diagonal hypothesis. Actual-character reciprocity supplies the endpoint identity in the comparison route.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Prove injectivity and identify the image

The inverse duality \(\kappa_x^{-1}:M^*\to K_x\) is injective, as is the submodule inclusion \(\iota_x\). Their composite is therefore injective.

Every value \(I_x\lambda\) lies in \(K_x\) by construction, proving \(\operatorname{im}I_x\subseteq K_x\).

Conversely, take \(v\in K_x\). Take \(\lambda=\kappa_x(v)\). Then
\[
I_x\lambda=\iota_x\bigl(\kappa_x^{-1}(\kappa_x(v))\bigr)=v.
\]
This proves the other containment and the image equality.

### Step 2. Apply boundary-cover minimality

For \(x<b\), the boundary sheaf's minimality field states that an assignment \(f\) whose outgoing restrictions vanish at \(x\) satisfies \(f_x\in A_+M\).

Given \(v\in K_x\), define \(f_x=v\) and \(f_y=0\) for every \(y\ne x\). Each outgoing restriction at \(x\) vanishes because \(v\in K_x\). The minimality field therefore gives \(v\in A_+M\).

Conversely, a containment \(K_x\subseteq A_+M\) immediately applies to the \(x\)-coordinate of any such assignment. This explains the source's kernelMinimal_iff conversion.

Step 1 now gives
\[
\operatorname{im}I_x=K_x\subseteq A_+M.
\]

### Step 3. Transport the homogeneous functional

The actual section pairing has shift \(L=\ell(b)\). The [[node:kl.sheaves.costalk_duality_degree|inverse stalk–costalk degree theorem]] sends a functional of degree \(r\) to kernel degree
\[
r+L-n_x,
\]
where \(n_x\) counts incoming edges.

On the lower Bruhat interval \([1,b]\), incoming edges correspond to the reflection inversions of \(x\), so \(n_x=\ell(x)\). Hence
\[
I_x\lambda\in M_{r+\ell(b)-\ell(x)}=M_{r+d}.
\]
Inclusion of the kernel preserves the induced grading.

### Step 4. Apply inverse-duality symmetry

The chosen actual section pairing is symmetric. The [[node:kl.sheaves.costalk_pairing_symmetry|stalk–costalk symmetry theorem]] therefore gives
\[
\lambda\bigl(\kappa_x^{-1}(\mu)\bigr)
=\mu\bigl(\kappa_x^{-1}(\lambda)\bigr).
\]
Evaluation uses the underlying stalk vector, so inserting the inclusions gives the claimed formula for \(I_x\).

### Step 5. Read the matrix entries

For a homogeneous basis \((m_i)\) with degrees \(d_i\), the dual functional \(\lambda_j\) has degree \(-d_j\). Step 3 gives
\(I_x\lambda_j\in M_{d-d_j}\).
Applying \(\lambda_i\), whose degree is \(-d_i\), gives
\[
a_{ij}=\lambda_i(I_x\lambda_j)\in A_{d-d_j-d_i}.
\]
Step 4 gives \(a_{ij}=a_{ji}\).

At \(x<b\), write \(I_x\lambda_j=\sum_s c_sv_s\) with \(c_s\in A_+\), using Step 2. Then
\[
a_{ij}=\sum_s c_s\lambda_i(v_s)\in A_+.
\]
Thus every coordinate has both the specified homogeneous degree and positive-ideal membership.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.localIntersection_injective`: [PositiveTransfer.lean:140](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L140).

`OAI.KLInvariance.BruhatGraph.localIntersection_range`: [PositiveTransfer.lean:146](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L146).

`OAI.KLInvariance.BruhatGraph.localIntersection_minimal`: [PositiveTransfer.lean:160](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L160).

`OAI.KLInvariance.BruhatGraph.localIntersection_homogeneous`: [PositiveTransfer.lean:167](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L167).

`OAI.KLInvariance.BruhatGraph.localIntersection_symmetric`: [PositiveTransfer.lean:180](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L180).
