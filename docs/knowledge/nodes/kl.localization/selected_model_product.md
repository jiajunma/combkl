---
id: kl.local.selected_model_product
title: Supported selected edges and their label product
kind: definition
status: formalized
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.detail.structure_sheaves
- kl.sheaves.upward_kernel
- kl.local.flow_down
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.supportedOutgoing
  - OAI.KLInvariance.MomentGraph.Sheaf.kernelProduct
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:791
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.supportedOutgoing
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:795
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.kernelProduct
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read supportedOutgoing as a finite set of outgoing subtype edges, and kernelProduct
    as its exact label product. Explained the selected-set and support conditions,
    the empty product, its relation to modelProduct, and arbitrary selections independent
    of an edge order.
tags:
- Kazhdan-Lusztig
- local-model-transport
---

# Supported selected edges and their label product

Let \(G\) be an ordered graph with finitely many edges, labelled by \(\alpha_e\) in a commutative ring \(R\). Fix a structure-model center \(c\) and a vertex \(x\). Write
\[
\operatorname{Out}(x)=\{e:s(e)=x\},
\]
and choose any subset \(F\subseteq\operatorname{Out}(x)\).

The **supported selected edge set** is
\[
F_c(x)=\{e\in F:t(e)\le c\}.
\]
The source calls it supportedOutgoing. Its **selected model product** is
\[
p_{c,x}(F)=\prod_{e\in F_c(x)}\alpha_e,
\]
called kernelProduct. The product over an empty set is \(1\).

The selection \(F\) is arbitrary. A suffix of an edge order is one possible choice, but the definition itself uses only the selected set and the model support.

## The equations indexed by this set

For \(x\le c\), identify the stalk \(\mathcal O_c^x\) with \(R\). A selected edge with target below \(c\) imposes the quotient equation
\[
[v]=0\text{ in }R/(\alpha_e),
\]
or equivalently \(\alpha_e\mid v\).

A selected edge with target outside the support has zero edge module, so its restriction is zero for every stalk vector. Consequently the selected upward kernel is the intersection of the scalar conditions indexed by \(F_c(x)\).

For \(F=\operatorname{Out}(x)\), this selected model product is the supported outgoing product \(P_c(x)\) used in the flow-down construction. For a smaller selection it contains exactly the remaining selected supported factors.

## A two-label calculation

Suppose two selected supported edges have labels \(a,b\). The two equations are \(a\mid v\) and \(b\mid v\). If \(a,b\) are relatively prime and the ring has the finite product-divisibility property, these are equivalent to \(ab\mid v\).

Selecting only the first edge gives product \(a\). Selecting no supported edges gives product \(1\) and imposes no scalar restriction.

The [[node:kl.local.structure_kernel_products|structure-kernel product theorem]] proves this calculation for every finite selected set and also treats the zero stalks outside the support.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Selected products and actual edge-image maps.**

**OpenAI notes:** The notes express the outgoing kernel as the product of the supported labels in the local unique factorization domain, and extend this formula to arbitrary subsets of outgoing edges. Unsupported edges impose no condition. [loc:boundary-product](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L346), [loc:arbitrary-edge-subsets](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L404).

**Lean (primary):** The general kernel theorem assumes the DecompositionMonoid product-divisibility structure and pairwise relative primality only for the supported selected labels. Separate lower- and upper-image theorems use restriction surjectivity to identify the scalar-image submodules. Prime-label relative primality is proved after localization before specialization to the actual coset graph. [PlaneLocalization:791](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L791), [PlaneLocalization:795](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L795), [PlaneLocalization:823](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L823), [PlaneLocalization:867](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L867), [PlaneLocalization:878](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L878), [PlaneLocalization:918](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L918), [PlaneLocalization:973](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L973).

**Role in the proof:** The Blueprint retains the selected-set indexing and writes both image equalities inside the same model edge module. The polynomial-domain specialization supplies every relative-primality and product-divisibility hypothesis.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.supportedOutgoing`: [PlaneLocalization.lean:791](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L791).

`OAI.KLInvariance.MomentGraph.Sheaf.kernelProduct`: [PlaneLocalization.lean:795](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L795).
