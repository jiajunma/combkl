---
id: kl.notes.bott_samelson
title: Word objects and Bott–Samelson tensor induction
kind: definition
status: formalized
primary_topic: kl.02_background
topics:
- kl.02_background
uses:
- kl.notes.tensor_pairing
- kl.notes.extended_realization
- kl.notes.reflection_frobenius
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.TitsSpace.bottSamelson
  - OAI.KLInvariance.TitsSpace.BottSamelsonModule
  - OAI.KLInvariance.TitsSpace.BottIndex
  - OAI.KLInvariance.TitsSpace.bottWeight
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:394
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSamelson
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:399
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BottSamelsonModule
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:947
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BottIndex
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1056
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottWeight
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

# Word objects and Bott–Samelson tensor induction

Let \(A\) be the symmetric coefficient ring of the extended realization. For a word \(\mathbf s=(s_1,\ldots,s_m)\), define its paired word object recursively:
\[
B_{\varnothing}=A,\qquad
B_{(s,\mathbf t)}=A\otimes_{A^s}B_{\mathbf t}.
\]
The right action, perfect pairing, and symmetry are transported by the Frobenius construction at each step.

Each rank-two extension introduces two basis choices. Thus the word object has a natural basis indexed by
\[
\varepsilon=(\varepsilon_1,\ldots,\varepsilon_m)\in\{0,1\}^m.
\]
Its degree is \(\sum_j\varepsilon_j\), and its weight is the subexpression product
\[
w(\varepsilon)=s_1^{\varepsilon_1}\cdots s_m^{\varepsilon_m}.
\]
The construction is defined for every word. Reducedness is required by later assertions identifying its top, support, and decomposition.

For the word \((s,t)\), the four indices have weights \(1,s,t,st\). The indices retain the word positions, so different indices may have the same group weight for longer words. Grouping evaluations by weight is what produces the stalks. This separates the tensor word, indexed by subexpressions, from the Bruhat graph, indexed by group elements.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottSamelson`: [Frobenius.lean:394](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L394).

`OAI.KLInvariance.TitsSpace.BottSamelsonModule`: [Frobenius.lean:399](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L399).

`OAI.KLInvariance.TitsSpace.BottIndex`: [Frobenius.lean:947](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L947).

`OAI.KLInvariance.TitsSpace.bottWeight`: [Frobenius.lean:1056](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1056).
