---
id: kl.detail.base_change
title: Tensor base change of a graph sheaf
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.compatible_sections
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChange
  - OAI.KLInvariance.MomentGraph.Sheaf.tensorSections
  - OAI.KLInvariance.MomentGraph.Sheaf.constraint
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:989
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChange
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1007
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.tensorSections
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1031
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.constraint
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# Tensor base change of a graph sheaf

For a homomorphism of commutative rings \(R\to S\) and an \(R\)-linear graph sheaf \(B\), define its scalar extension by
\[
(S\otimes_R B)^x=S\otimes_R B^x,\qquad
(S\otimes_R B)^e=S\otimes_R B^e.
\]
The restrictions are \(1\otimes\rho_{e,s}\) and \(1\otimes\rho_{e,t}\). A tensor \(s\otimes m\) of a compatible section gives the compatible assignment \((s\otimes m_x)_x\); by linearity this defines the natural map from the tensor product of the section module to the section module after base change.

For a vertex set \(\Omega\), collect all compatibility equations into
\[
\delta_\Omega:\prod_xB^x\longrightarrow
\prod_{e:\,s(e),t(e)\in\Omega}B^e,\qquad
(\delta_\Omega m)_e=\rho_{e,s}(m_{s(e)})-\rho_{e,t}(m_{t(e)}).
\]
Then \(\Gamma(\Omega,B)=\ker\delta_\Omega\), using the convention that assignments still have a coordinate at every vertex.

When the products are finite and \(S\) is flat over \(R\), tensoring preserves this kernel and commutes with these products. Consequently the natural section map is an isomorphism. Localization has these flatness properties. General scalar extension need not preserve kernels, so the hypotheses in the localization theorem cannot be omitted.

## References

The precise Lean sources are listed below.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.baseChange`: [MinimalExtensions.lean:989](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L989).

`OAI.KLInvariance.MomentGraph.Sheaf.tensorSections`: [MinimalExtensions.lean:1007](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1007).

`OAI.KLInvariance.MomentGraph.Sheaf.constraint`: [MinimalExtensions.lean:1031](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1031).
