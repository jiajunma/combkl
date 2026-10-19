---
id: kl.local.coset_kernel_products
title: Kernel products and edge images for the actual coset models
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.coset_structure_models
- kl.local.localized_relative_primality
- kl.local.structure_kernel_products
- kl.local.structure_edge_images
- kl.algebra.linear_primes
- kl.detail.root_reflection_correspondence
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetEdgeAmbient_injective
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetLabel_relPrime
  - OAI.KLInvariance.TitsSpace.PlaneBasis.coset_supported_pairwise
  - OAI.KLInvariance.TitsSpace.PlaneBasis.coset_kernel_product
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:945
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetEdgeAmbient_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:952
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetLabel_relPrime
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:963
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.coset_supported_pairwise
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:973
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.coset_kernel_product
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read injectivity of the ambient coset-edge map, the distinct same-source
    label argument, coset_supported_pairwise and coset_kernel_product. Traced primality
    and nondivisibility before localization, verified the local product-divisibility
    hypotheses, and derived both edge-image formulas through the previously proved
    generic theorem.
tags:
- Kazhdan-Lusztig
- local-model-transport
---

# Kernel products and edge images for the actual coset models

Fix a finite-generator Coxeter system \(W\), a root subspace \(P\) with a plane basis, and its induced dihedral subgroup \(D\). Choose \(a_0\in W\) with \(\ell(a_0)\le\ell(da_0)\) for every \(d\in D\), and an ambient top \(b\). Let \(K=\{d\in D:da_0\le_W b\}\) have its intrinsic Bruhat order and reflection edges. Use the plane ring \(R_P=A_{\mathfrak p_P}\) and the labels \(\gamma_e\) obtained by localizing the ambient positive-root polynomials. These are the models of the [[node:kl.local.coset_structure_models|coset structure-model theorem]]. Distinct edges with the same source have relatively prime labels in \(R_P\).

Consequently, for every model center \(c\in K\), vertex \(x\in K\), and arbitrary outgoing selection \(F\),
\[
K_x^{\mathcal O_c}(F)
=\left(\prod_{\substack{e\in F\\ t(e)\le_D c}}\gamma_e\right)\mathcal O_c^x.
\]
Applying either endpoint restriction gives the corresponding scalar-multiple submodule in the actual model edge module.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Selected products and actual edge-image maps.**

**OpenAI notes:** The notes express the outgoing kernel as the product of the supported labels in the local unique factorization domain, and extend this formula to arbitrary subsets of outgoing edges. Unsupported edges impose no condition. [loc:boundary-product](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L346), [loc:arbitrary-edge-subsets](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L404).

**Lean (primary):** The general kernel theorem assumes the DecompositionMonoid product-divisibility structure and pairwise relative primality only for the supported selected labels. Separate lower- and upper-image theorems use restriction surjectivity to identify the scalar-image submodules. Prime-label relative primality is proved after localization before specialization to the actual coset graph. [PlaneLocalization:791](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L791), [PlaneLocalization:795](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L795), [PlaneLocalization:823](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L823), [PlaneLocalization:867](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L867), [PlaneLocalization:878](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L878), [PlaneLocalization:918](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L918), [PlaneLocalization:973](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L973).

**Role in the proof:** The Blueprint retains the selected-set indexing and writes both image equalities inside the same model edge module. The polynomial-domain specialization supplies every relative-primality and product-divisibility hypothesis.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Keep distinct relative edges distinct in the ambient graph

The ambient vertex map is \(x\mapsto xa_0\), which is injective by right cancellation. If two relative edges have equal ambient images, their lower endpoints have equal images and so do their upper endpoints.

Both endpoint pairs therefore agree. Edges are reflection-step endpoint pairs, so the relative edges are equal. This proves cosetEdgeAmbient_injective.

### Step 2. Exclude divisibility of distinct incident polynomial labels

Let \(e\ne f\) have the same relative source. Their ambient images also have the same source. Write \(\alpha_e,\alpha_f\in A\) for their ambient polynomial labels before localization.

Each is prime by the [[node:kl.algebra.linear_primes|linear-prime theorem]]. If \(\alpha_e\mid\alpha_f\), divisibility of the degree-one polynomials forces dependence of the two embedded positive roots. Distinct positive roots are independent, so the roots are equal.

The positive-root/reflection correspondence then identifies the two left reflection labels. An edge with source \(x\) and reflection \(\tau\) has target \(\tau x\); equal reflection and source therefore identify the two ambient edges. Step 1 would imply \(e=f\), a contradiction.

Hence \(\alpha_e\nmid\alpha_f\).

### Step 3. Localize the relative-primality assertion

The coefficient algebra \(A\) is a polynomial domain, and the plane ideal is prime. Apply the [[node:kl.local.localized_relative_primality|localized relative-primality theorem]] to \(\alpha_e,\alpha_f\).

Their images are exactly \(\gamma_e,\gamma_f\). Thus distinct same-source relative edges have relatively prime localized labels. Restricting to any supported selected edge set preserves this pairwise property.

### Step 4. Apply the general product-kernel theorem

The graph has finitely many edges. The plane ring is a localization of a polynomial unique factorization domain, so it has the product-divisibility property used by the [[node:kl.local.structure_kernel_products|structure-kernel product theorem]].

Step 3 supplies relative primality for every supported selected set. That theorem gives the stated kernel equality, including empty selections and unsupported stalks. This is coset_kernel_product.

### Step 5. Retain both edge-image embeddings

For an edge \(e:x\to y\), apply the [[node:kl.local.structure_edge_images|structure edge-image theorem]] to the selected kernels at \(x\) and \(y\). With their respective products \(p_x,p_y\), it gives
\[
\rho^-_e(K_x(F))=p_x\mathcal O_c^e,\qquad
\rho^+_e(K_y(H))=p_y\mathcal O_c^e.
\]
When the edge is supported, both submodules lie in
\[
\mathcal O_c^e=R_P/(\gamma_e).
\]
When it is unsupported, both lie in the zero edge module.

These are the precise product expressions used after local decomposition to compare the two embedded edge images.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetEdgeAmbient_injective`: [PlaneLocalization.lean:945](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L945).

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetLabel_relPrime`: [PlaneLocalization.lean:952](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L952).

`OAI.KLInvariance.TitsSpace.PlaneBasis.coset_supported_pairwise`: [PlaneLocalization.lean:963](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L963).

`OAI.KLInvariance.TitsSpace.PlaneBasis.coset_kernel_product`: [PlaneLocalization.lean:973](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L973).
