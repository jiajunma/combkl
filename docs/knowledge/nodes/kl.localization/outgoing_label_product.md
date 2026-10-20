---
id: kl.local.outgoing_label_product
title: The outgoing label product of a selected edge set
kind: definition
status: formalized
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.sheaves.upward_kernel
lean:
  repository: openai-kl
  modules:
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.outgoingLabelProduct
  - OAI.KLInvariance.MomentGraph.Sheaf.outgoingLabelProduct_dvd
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:781
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.outgoingLabelProduct
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:784
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.outgoingLabelProduct_dvd
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, finiteness and freeness hypotheses, original embedded
    submodules, localization multipliers and schedule assumptions explicit?
  verdict: Defined the finite selected-edge product with its empty case, exact edge
    indexing and factor-divisibility identity; separated the definition from its sheaf-image
    consequence.
tags:
- Kazhdan-Lusztig
- global-inclusion
---

# The outgoing label product of a selected edge set

Let \(R\) be a commutative ring, \(G\) an ordered graph with finitely many edges, and \(\alpha_f\in R\) its scalar label at each edge \(f\). For a vertex \(x\) and a selection \(F\subseteq\operatorname{Out}_G(x)\), define the outgoing label product
\[
g_{x,F}=\prod_{f\in F}\alpha_f\in R.
\]
This is `Sheaf.outgoingLabelProduct`. The selection is finite because the edge set is finite. Each selected edge occurs once in the product, and the empty product is \(1\).

For every \(f\in F\), the label divides the product. Indeed, separating that factor gives
\[
g_{x,F}=\alpha_f\prod_{h\in F\setminus\{f\}}\alpha_h.
\]
This is `outgoingLabelProduct_dvd`.

For example, a selection of two edges labeled \(X\) and \(Y\) gives \(g_{x,F}=XY\). Multiplication by this scalar supplies both label factors at once. In a sheaf whose label \(\alpha_f\) annihilates its edge module, the [[node:kl.local.outgoing_product_image|outgoing-product image theorem]] shows that \(g_{x,F}\) sends every stalk vector into the selected kernel.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The correction and outgoing products supply one global multiplier.**

**OpenAI notes:** The notes multiply the upper outgoing labels to obtain a nonzero reduced scalar whose multiples lie in the upper image. The correction factor gives a free target of full generic rank, and primes containing reduced roots are related to plane primes. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The outgoing product is defined for any finite graph and selection. Label annihilation and an upper lift prove its image containment. The actual reduced outgoing and correction products are nonzero, and every prime divisor of their product is associated to one reduced independent root. Quotient divisibility by that root is equivalent to membership in its plane ideal. [TerminalKernels:781](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L781), [TerminalKernels:798](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L798), [TerminalKernels:732](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L732), [TerminalKernels:752](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L752), [TerminalKernels:838](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L838).

**Role in the proof:** The Blueprint gives the explicit global multiplier and the complete factor classification used by the membership theorem.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.outgoingLabelProduct`: [TerminalKernels.lean:781](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L781).

`OAI.KLInvariance.MomentGraph.Sheaf.outgoingLabelProduct_dvd`: [TerminalKernels.lean:784](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L784).
