---
id: kl.local.structure_kernel_products
title: Selected kernels of a structure model are product submodules
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.selected_model_product
- kl.detail.structure_sheaves
- kl.sheaves.upward_kernel
- kl.algebra.linear_ideals
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.structure_kernel_iff_dvd
  - OAI.KLInvariance.MomentGraph.Sheaf.structure_kernel_product
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:798
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.structure_kernel_iff_dvd
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:823
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.structure_kernel_product
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read both directions of structure_kernel_iff_dvd and both support branches
    of structure_kernel_product. Kept relative primality restricted to the selected
    supported labels and the general DecompositionMonoid ring hypothesis; explained
    the submodule equality through actual scalar coordinates.
tags:
- Kazhdan-Lusztig
- local-model-transport
---

# Selected kernels of a structure model are product submodules

Let \(R\) be a commutative ring with the DecompositionMonoid product-divisibility property: finitely many pairwise relatively prime scalars that each divide \(v\) have a product dividing \(v\). Let \(G\) be an ordered graph with finitely many edges and labels \(\alpha_e\in R\).

Fix a center \(c\), vertex \(x\), and selection \(F\subseteq\operatorname{Out}(x)\). Assume the labels indexed by the supported selected edge set \(F_c(x)\) are pairwise relatively prime. Then the selected upward kernel in the structure model is
\[
K_x^{\mathcal O_c}(F)
=p_{c,x}(F)\,\mathcal O_c^x.
\]
The right side is the image of multiplication by the scalar product on the full stalk.

If \(x\le c\), the equivalent scalar statement is
\[
v\in K_x^{\mathcal O_c}(F)
\quad\Longleftrightarrow\quad
p_{c,x}(F)\mid v.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Selected products and actual edge-image maps.**

**OpenAI notes:** The notes express the outgoing kernel as the product of the supported labels in the local unique factorization domain, and extend this formula to arbitrary subsets of outgoing edges. Unsupported edges impose no condition. [loc:boundary-product](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L346), [loc:arbitrary-edge-subsets](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L404).

**Lean (primary):** The general kernel theorem assumes the DecompositionMonoid product-divisibility structure and pairwise relative primality only for the supported selected labels. Separate lower- and upper-image theorems use restriction surjectivity to identify the scalar-image submodules. Prime-label relative primality is proved after localization before specialization to the actual coset graph. [PlaneLocalization:791](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L791), [PlaneLocalization:795](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L795), [PlaneLocalization:823](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L823), [PlaneLocalization:867](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L867), [PlaneLocalization:878](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L878), [PlaneLocalization:918](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L918), [PlaneLocalization:973](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L973).

**Role in the proof:** The Blueprint retains the selected-set indexing and writes both image equalities inside the same model edge module. The polynomial-domain specialization supplies every relative-primality and product-divisibility hypothesis.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Translate a supported quotient equation

Suppose \(x\le c\), and use its scalar coordinate \(v\in R\). For \(e\in F_c(x)\), the lower restriction is the quotient map. Thus
\[
\rho^-_e(v)=0
\quad\Longleftrightarrow\quad
v\in(\alpha_e)
\quad\Longleftrightarrow\quad
\alpha_e\mid v.
\]

For \(e\in F\) outside \(F_c(x)\), the edge module is zero and the equation holds automatically. Therefore membership in the selected kernel is equivalent to divisibility by every supported selected label.

### Step 2. Combine the individual divisibilities

If \(v\) belongs to the selected kernel, Step 1 gives \(\alpha_e\mid v\) for every \(e\in F_c(x)\). The labels are pairwise relatively prime by hypothesis. Applying the finite product-divisibility property yields
\[
p_{c,x}(F)\mid v.
\]

Conversely, if the product divides \(v\), every factor \(\alpha_e\) divides the product and therefore divides \(v\). Step 1 then makes every selected restriction vanish. This proves the scalar equivalence.

For an empty supported selection, the product is \(1\), which divides every \(v\), as required.

### Step 3. Identify the supported stalk submodule

A scalar \(v\) is divisible by \(p=p_{c,x}(F)\) exactly when \(v=pr\) for some \(r\in R\). Under the supported-stalk coordinate, \(r\) specifies a vector of \(\mathcal O_c^x\).

Thus the scalar equivalence says precisely
\[
v\in K_x^{\mathcal O_c}(F)
\quad\Longleftrightarrow\quad
v\in p\,\mathcal O_c^x.
\]
This is equality of the two submodules in the same stalk.

### Step 4. Treat an unsupported stalk

If \(x\not\le c\), then \(\mathcal O_c^x=0\). Its selected kernel and the image of scalar multiplication on it are both the zero submodule.

This establishes the formula for every vertex, including those outside the model support.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.structure_kernel_iff_dvd`: [PlaneLocalization.lean:798](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L798).

`OAI.KLInvariance.MomentGraph.Sheaf.structure_kernel_product`: [PlaneLocalization.lean:823](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L823).
