---
id: kl.local.structure_scaled_images
title: Scaled image equality from model products and their counts
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.detail.scaled_images
- kl.local.structure_edge_images
- kl.local.selected_model_product
- kl.local.product_image_scaling
- kl.detail.structure_sheaves
lean:
  repository: openai-kl
  modules:
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.structure_scaledImages
  - OAI.KLInvariance.MomentGraph.Sheaf.structure_scaledImages_of_count
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:62
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.structure_scaledImages
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:82
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.structure_scaledImages_of_count
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read both structure_scaledImages statements and proofs. Preserved finite
    edges, the product-divisibility ring structure and separate supported-selection
    coprimality hypotheses. Identified the actual quotient action, proved both unit-image
    containments and the cardinality-to-association calculation, and explained the
    direct zero-edge branch.
tags:
- Kazhdan-Lusztig
- embedded-images
---

# Scaled image equality from model products and their counts

Let \(R\) be a commutative ring with the DecompositionMonoid product-divisibility property: pairwise relatively prime individual divisors can be multiplied into a divisor. Let \(G\) be an ordered graph with finitely many edges and labels \(\alpha_f\in R\). Fix a model center \(c\), an edge \(e:x\to y\), outgoing selections \(F,H\) at \(x,y\), and a scalar \(r\in R\).

Write
\[
F_c=\{f\in F:t(f)\le c\},\qquad
H_c=\{h\in H:t(h)\le c\},
\]
\[
p_x=\prod_{f\in F_c}\alpha_f,\qquad
p_y=\prod_{h\in H_c}\alpha_h.
\]
Assume the labels in each of \(F_c,H_c\) are pairwise relatively prime. Let
\[
q_e:R\to S_e=R/(\alpha_e)
\]
be the quotient map. Write \(s\sim t\) when one is a unit multiple of the other in \(S_e\).

If
\[
q_e(p_x)\sim q_e(rp_y),
\]
then the structure model \(\mathcal O_c\) satisfies
\[
L_e^{\mathcal O_c}(F)=rU_e^{\mathcal O_c}(H).
\]

A sufficient condition for the association is the existence of \(p\in S_e\) and \(k\in\mathbb N\) with
\[
q_e(\alpha_f)\sim p\ (f\in F_c),\qquad
q_e(\alpha_h)\sim p\ (h\in H_c),\qquad
q_e(r)\sim p^k,
\]
and
\[
|F_c|=|H_c|+k.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Associated products in the actual model edge quotient.**

**OpenAI notes:** In each supported rank-one model, the two images are principal product ideals in the localized edge ring. Their reduced labels have the same uniformizer up to units, and the correction factor supplies the exponent difference. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The structure-model theorem uses the exact quotient R/(alpha_e) as the edge coefficient ring and derives equality from association of the two scalar products. The actual coset labels are identified with localized ambient root forms before the label and factor associations are imported. A zero edge module gives the equality directly. [TerminalKernels:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L62), [TerminalKernels:82](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L82), [PlaneLocalization:1640](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1640), [PlaneLocalization:1647](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1647), [PlaneLocalization:1651](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1651), [PlaneLocalization:1663](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1663).

**Role in the proof:** The Blueprint keeps the quotient action, root inequality and count hypotheses explicit. The actual supported case combines these algebraic inputs with the transported later-edge count.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Identify the two model images

The [[node:kl.local.structure_edge_images|structure edge-image theorem]] applies to the two supported selections and their relative-primality hypotheses. It gives
\[
L_e^{\mathcal O_c}(F)=p_x\mathcal O_c^e,\qquad
U_e^{\mathcal O_c}(H)=p_y\mathcal O_c^e.
\]

### Step 2. Use the actual quotient coefficient action

The model edge module is \(S_e\) if \(y\le c\), and zero otherwise. In either case it is an \(S_e\)-module with compatible \(R\)-action through \(q_e\).

If \(q_e(p_x)\sim q_e(rp_y)\), choose a unit \(u\in S_e^\times\) with
\[
q_e(p_x)=u\,q_e(rp_y).
\]
For any \(m\in\mathcal O_c^e\),
\[
p_xm=rp_y(um).
\]
This gives \(p_x\mathcal O_c^e\subseteq rp_y\mathcal O_c^e\). Applying the inverse unit gives the reverse containment.

Hence
\[
p_x\mathcal O_c^e
=r(p_y\mathcal O_c^e).
\]
Substitute Step 1 to obtain the scaled image equality. This proves structure_scaledImages.

### Step 3. Derive the association from the count hypotheses

Suppose the displayed conditions involving \(p,k\) hold. Multiplying the factor associations gives
\[
q_e(p_x)\sim p^{|F_c|},\qquad
q_e(p_y)\sim p^{|H_c|}.
\]
The count equation yields
\[
p^{|F_c|}=p^k p^{|H_c|}.
\]
Since \(q_e(r)\sim p^k\), it follows that
\[
q_e(p_x)\sim q_e(r)\,q_e(p_y)=q_e(rp_y).
\]
Step 2 now proves the equality. This is the count form of the associated-product image calculation.

### Step 4. Read the unsupported-edge case directly

If \(y\not\le c\), the current edge module is zero. Both selected images are then zero, and the two ScaledImages witness statements are realized by zero vectors.

Thus an unsupported model contributes the zero equality directly. In the actual coset comparison, the product and count hypotheses are checked in the supported-edge branch.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.structure_scaledImages`: [TerminalKernels.lean:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L62).

`OAI.KLInvariance.MomentGraph.Sheaf.structure_scaledImages_of_count`: [TerminalKernels.lean:82](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L82).
