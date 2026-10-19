---
id: kl.detail.local_models
title: Local boundary models over a local coefficient ring
kind: definition
status: formalized
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.sheaves.graph_sheaf
- kl.detail.upper_quotient
- kl.sheaves.flabbiness
- kl.sheaves.upward_kernel
- kl.detail.sheaf_isomorphisms
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.LocalModels
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:352
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.LocalModels
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Expanded every LocalModels field and the exact x!=c minimality condition.
    Derived the residue-field minimal-cover interpretation through the preimage equality
    and illustrated it on a single edge. Kept the chosen top isomorphism as data,
    not merely a rank assertion.
tags:
- Kazhdan-Lusztig
- local-model-transport
---

# Local boundary models over a local coefficient ring

Let \(R\) be a commutative local ring, with maximal ideal \(\mathfrak m\), and let \(G\) be an ordered graph with labels \(\alpha_e\in R\). A **family of local boundary models** consists of a sheaf \(O_c\) for every vertex \(c\), together with the following data and conditions.

| Lean field | Mathematical content |
|---|---|
| sheaf | The family \(c\mapsto O_c\), including both endpoint restrictions on every edge. |
| free | Every vertex stalk \(O_c^x\) is a free \(R\)-module. |
| finite | Every vertex stalk is finitely generated. Together with free, this makes it finite free. |
| quotient | Each upper map \(O_c^{t(e)}\to O_c^e\) is surjective and has kernel \(\alpha_eO_c^{t(e)}\). |
| generated | Evaluation of global sections onto each stalk is surjective. |
| flabby | Every compatible section on an upper vertex subset extends to a global section. |
| support | The stalk \(O_c^x\) is zero whenever \(x\not\le c\). |
| top | A chosen \(R\)-linear isomorphism \(O_c^c\simeq R\). |
| minimal | For \(x\ne c\), the full outgoing kernel is contained in \(\mathfrak mO_c^x\). |

The source packages these fields as LocalModels. The chosen top coordinate is part of the data. All the modules and maps here are ungraded.

## The outgoing map and local minimality

At a vertex \(x\), collect the lower restrictions into
\[
d_x:O_c^x\longrightarrow\prod_{e:s(e)=x}O_c^e,
\qquad v\longmapsto(\rho^-_e(v))_e.
\]
Its kernel consists of vectors whose restrictions vanish on every outgoing edge. The minimal field is the inclusion
\[
\ker d_x\subseteq\mathfrak mO_c^x\qquad(x\ne c).
\]

At a vertex \(x\ne c\), let \(N_x=\operatorname{im}d_x\). The induced surjection
\(\pi_x:O_c^x\to N_x\) becomes an isomorphism after reduction modulo \(\mathfrak m\). Indeed surjectivity persists, and
\[
\pi_x^{-1}(\mathfrak mN_x)
=\mathfrak mO_c^x+\ker\pi_x
=\mathfrak mO_c^x.
\]
For the first equality, write an element of \(\mathfrak mN_x\) as a finite sum of ideal scalars times images and lift each image; the difference from this lifted sum lies in the kernel. The second equality is the minimality condition.

Thus the residue classes of a stalk basis provide exactly the generators needed for its outgoing image. This is the local-ring minimal-cover condition used in the decomposition.

## A one-edge example

Let \(G\) consist of \(x<c\) with one edge labelled by \(\alpha\in\mathfrak m\). The structure model centered at \(c\) has stalks \(R,R\), edge module \(R/(\alpha)\), and quotient restrictions. At \(x\),
\[
\ker d_x=\alpha R\subseteq\mathfrak mR.
\]
Its outgoing image is \(R/(\alpha)\), and reducing either the stalk or this image modulo \(\mathfrak m\) gives the residue field \(R/\mathfrak m\).

At the center \(c\), there are no outgoing edges and the outgoing kernel is \(R\). The minimality condition is imposed only at \(x\ne c\); the top condition instead specifies the free rank-one stalk at \(c\).

For the actual localized coset graph, the [[node:kl.local.local_structure_models|local structure-model theorem]] constructs these fields from the structure sheaves, their flabbiness, the maximal-ideal labels and the existence of outgoing edges below every larger center. Finite ungraded model sums assemble copies of these sheaves for the later decomposition theorem.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.LocalModels`: [CharacterReciprocity.lean:352](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L352).
