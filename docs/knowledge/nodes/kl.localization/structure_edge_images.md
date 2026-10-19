---
id: kl.local.structure_edge_images
title: Edge images of selected structure-model kernels
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.structure_kernel_products
- kl.detail.structure_sheaves
- kl.local.structure_sheaf_properties
- kl.detail.upper_quotient
- kl.detail.compatible_sections
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.lower_surjective_of_generated
  - OAI.KLInvariance.MomentGraph.Sheaf.structure_lower_image
  - OAI.KLInvariance.MomentGraph.Sheaf.structure_upper_image
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:857
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.lower_surjective_of_generated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:867
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.structure_lower_image
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:878
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.structure_upper_image
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read lower_surjective_of_generated and both structure edge-image theorems.
    Expanded the global-section preimage, both containments for mapping a scalar-multiple
    submodule, and the two endpoint substitutions; illustrated the quotient action
    in a one-edge example.
tags:
- Kazhdan-Lusztig
- local-model-transport
---

# Edge images of selected structure-model kernels

Let \(R\) be a commutative ring with the DecompositionMonoid product-divisibility property, \(G\) an ordered graph with finitely many edges and labels \(\alpha_e\in R\), and \(\mathcal O_c\) its structure model below \(c\). The product-divisibility property combines pairwise relatively prime individual divisors into a divisor equal to their product, as in the [[node:kl.local.structure_kernel_products|structure-kernel product theorem]]. Fix an edge \(e:x\to y\).

For \(F\subseteq\operatorname{Out}(x)\) whose supported selected labels are pairwise relatively prime,
\[
\rho^-_e\bigl(K_x^{\mathcal O_c}(F)\bigr)
=p_{c,x}(F)\,\mathcal O_c^e.
\]
For \(H\subseteq\operatorname{Out}(y)\) with the corresponding relative-primality condition,
\[
\rho^+_e\bigl(K_y^{\mathcal O_c}(H)\bigr)
=p_{c,y}(H)\,\mathcal O_c^e.
\]
Both are equalities of submodules of the actual edge module. The scalars act through its \(R\)-module structure.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Selected products and actual edge-image maps.**

**OpenAI notes:** The notes express the outgoing kernel as the product of the supported labels in the local unique factorization domain, and extend this formula to arbitrary subsets of outgoing edges. Unsupported edges impose no condition. [loc:boundary-product](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L346), [loc:arbitrary-edge-subsets](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L404).

**Lean (primary):** The general kernel theorem assumes the DecompositionMonoid product-divisibility structure and pairwise relative primality only for the supported selected labels. Separate lower- and upper-image theorems use restriction surjectivity to identify the scalar-image submodules. Prime-label relative primality is proved after localization before specialization to the actual coset graph. [PlaneLocalization:791](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L791), [PlaneLocalization:795](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L795), [PlaneLocalization:823](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L823), [PlaneLocalization:867](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L867), [PlaneLocalization:878](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L878), [PlaneLocalization:918](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L918), [PlaneLocalization:973](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L973).

**Role in the proof:** The Blueprint retains the selected-set indexing and writes both image equalities inside the same model edge module. The polynomial-domain specialization supplies every relative-primality and product-divisibility hypothesis.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Prove surjectivity of a lower restriction from generation

For any globally generated sheaf \(B\) with surjective upper restrictions, take \(u\in B^e\). Choose \(v\in B^{t(e)}\) with \(\rho^+_e(v)=u\).

Generation supplies a global section \(s\) with \(s_{t(e)}=v\). Its compatibility at \(e\) gives
\[
\rho^-_e(s_{s(e)})
=\rho^+_e(s_{t(e)})
=\rho^+_e(v)=u.
\]
Thus \(\rho^-_e\) is surjective. This proves lower_surjective_of_generated.

For a structure model, generation and surjective upper restrictions hold by the [[node:kl.local.structure_sheaf_properties|basic structure-sheaf properties theorem]]. Hence both endpoint restrictions onto every edge module are surjective.

### Step 2. Map a scalar-multiple submodule

For an \(R\)-linear map \(f:M\to N\) and scalar \(p\in R\),
\[
f(pM)=p\,f(M).
\]
Indeed \(f(pm)=pf(m)\) gives one containment; every vector \(pf(m)\) on the right is the image of \(pm\), giving the other.

If \(f\) is surjective, \(f(M)=N\), so the formula becomes \(f(pM)=pN\).

### Step 3. Apply the stalk-kernel product formula at the lower endpoint

The [[node:kl.local.structure_kernel_products|structure-kernel product theorem]] gives
\[
K_x^{\mathcal O_c}(F)=p_{c,x}(F)\mathcal O_c^x.
\]
Map this equality by \(\rho^-_e\). Step 2 and lower surjectivity from Step 1 give
\[
\rho^-_e\bigl(K_x^{\mathcal O_c}(F)\bigr)
=p_{c,x}(F)\rho^-_e(\mathcal O_c^x)
=p_{c,x}(F)\mathcal O_c^e.
\]

### Step 4. Apply the same calculation at the upper endpoint

At \(y=t(e)\), the kernel formula gives
\(K_y^{\mathcal O_c}(H)=p_{c,y}(H)\mathcal O_c^y\).
Map by the surjective upper quotient:
\[
\rho^+_e\bigl(K_y^{\mathcal O_c}(H)\bigr)
=p_{c,y}(H)\rho^+_e(\mathcal O_c^y)
=p_{c,y}(H)\mathcal O_c^e.
\]
If the edge module is zero, both displayed image formulas are zero equalities.

### Step 5. Calculate a one-edge example

For a single supported edge \(e:x\to c\) labelled by \(\alpha\), choose \(F=\{e\}\). Then
\[
K_x^{\mathcal O_c}(F)=\alpha R,
\qquad
\rho^-_e(K_x^{\mathcal O_c}(F))
=\alpha\bigl(R/(\alpha)\bigr)=0.
\]
At \(c\), the outgoing selection is empty, its product is \(1\), and the upper image is all of \(R/(\alpha)\).

This calculation records both the stalk product and its image under the actual quotient map, the distinction needed in the later comparison of the two endpoint images.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.lower_surjective_of_generated`: [PlaneLocalization.lean:857](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L857).

`OAI.KLInvariance.MomentGraph.Sheaf.structure_lower_image`: [PlaneLocalization.lean:867](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L867).

`OAI.KLInvariance.MomentGraph.Sheaf.structure_upper_image`: [PlaneLocalization.lean:878](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L878).
