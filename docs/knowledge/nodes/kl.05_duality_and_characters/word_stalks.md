---
id: kl.notes.word_stalks
title: Stalks as images of weight evaluations
kind: definition
status: formalized
primary_topic: kl.05_duality_and_characters
topics:
- kl.05_duality_and_characters
uses:
- kl.notes.bott_samelson
- kl.sheaves.graph_sheaf
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.TitsSpace.bottWeightProjection
  - OAI.KLInvariance.TitsSpace.bottStalk
  - OAI.KLInvariance.TitsSpace.bottStalkProjection_surjective
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1497
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottWeightProjection
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1558
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalk
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1566
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkProjection_surjective
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; bg:normalization
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the mathematical hypotheses and scope retained from the referenced declarations?
  verdict: The exposition follows the fixed Lean source; worked calculations explain
    the constructions.
tags:
- Kazhdan-Lusztig
- background
---

# Stalks as images of weight evaluations

For a word \(\mathbf s\) and a group element \(x\), collect all evaluation coordinates whose subexpression weight is \(x\):
\[
\pi_x:B_{\mathbf s}\longrightarrow
\prod_{\varepsilon:\,w(\varepsilon)=x}A.
\]
The actual stalk is the image \(B_{\mathbf s}^x=\operatorname{im}\pi_x\), with the induced projection onto that image. It is not defined to be the entire coordinate product.

For a single reflection \(s\), the two evaluations of \(a\otimes b\) are \(ab\) and \(a\,s(b)\). Their difference is divisible by the root label \(\alpha_s\). Conversely, the rank-two invariant-ring decomposition reconstructs a tensor from any pair obeying this congruence. Thus already the first word records an integral relation between its two coordinates.

This image description has two consequences. First, surjectivity onto the stalk is immediate from the definition of image. Second, proving the stalk free is a separate structural argument about that image; it does not follow just because the surrounding coordinate product is free. The later reflection-pair and graded arguments establish the required freeness and compatibility with the graph restrictions.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottWeightProjection`: [Frobenius.lean:1497](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1497).

`OAI.KLInvariance.TitsSpace.bottStalk`: [Frobenius.lean:1558](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1558).

`OAI.KLInvariance.TitsSpace.bottStalkProjection_surjective`: [Frobenius.lean:1566](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1566).
