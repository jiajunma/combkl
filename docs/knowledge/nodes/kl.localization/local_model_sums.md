---
id: kl.local.model_sums
title: Finite ungraded sums of local models
kind: definition
status: formalized
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.detail.local_models
- kl.sheaves.graph_sheaf
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  - GradedSheaves
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.ModelSum
  - OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.mono
  - OAI.KLInvariance.MomentGraph.Sheaf.zero
  - OAI.KLInvariance.MomentGraph.Sheaf.prod
  - OAI.KLInvariance.MomentGraph.Sheaf.pi
  - OAI.KLInvariance.MomentGraph.Sheaf.pi_compatible
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:364
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.ModelSum
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:375
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.mono
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:271
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:277
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.prod
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:819
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.pi
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:825
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.pi_compatible
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the ungraded ModelSum zero/add constructors and mono. Kept the definition
    general for a family over a commutative ring, explained finite products and both
    restrictions, distinguished the inductive construction from a later isomorphism,
    and used an explicit rank calculation on a one-edge graph.
tags:
- Kazhdan-Lusztig
- local-model-transport
---

# Finite ungraded sums of local models

Let \(R\) be a commutative ring, \(G\) an ordered graph, \(O_c\) a family of sheaves on \(G\), and \(U\) a set of allowed centers. An **ungraded model sum with centers in \(U\)** is a sheaf built by these finite rules:

1. The zero sheaf is a model sum.
2. If \(B\) is a model sum, \(c\in U\), and \(n\in\mathbb N\), then
   \[
   B\times O_c^{\,n}
   \]
   is a model sum.

This is the source's inductive proposition ModelSum. The second factor is the finite product indexed by \(\{0,\ldots,n-1\}\); for finitely many modules this is also their direct sum. Repeated use of the second rule gives a finite iterated direct sum of copies of the chosen models.

## Stalks, edge modules and restrictions

At a vertex \(x\), the new stalk is
\[
B^x\times(O_c^x)^n.
\]
At an edge \(e\), the new edge module is
\[
B^e\times(O_c^e)^n.
\]
The lower and upper restrictions act componentwise. Consequently a global section is exactly a global section of \(B\) together with \(n\) global sections of \(O_c\). The same description holds for sections on an upper subset.

The integer \(n\) records the number of copies. There are no grading shifts in this construction.

## Two centers on a one-edge graph

Take the one-edge graph \(x<c\) over a local ring \(R\), with edge label \(\alpha\in R\), and its structure models \(O_x,O_c\). The sum
\[
O_c^2\oplus O_x^3
\]
has stalk \(R^5\) at \(x\), stalk \(R^2\) at \(c\), and edge module \((R/(\alpha))^2\). The lower restriction reduces the two \(O_c\)-coordinates and kills the three \(O_x\)-coordinates. The upper restriction reduces both coordinates.

Thus adding models centered at \(x\) enlarges that stalk while leaving the already constructed data above \(x\) unchanged. This is the operation used in descending local decomposition.

## Allowed centers and isomorphisms

If \(U\subseteq T\), the same construction is a model sum with centers in \(T\): every center chosen by the construction still belongs to the larger set. Induction on the two construction rules proves this monotonicity.

ModelSum records the constructed sheaf itself. A decomposition of another sheaf \(C\) consists of a model sum \(D\) together with an actual sheaf isomorphism \(C\simeq D\), so both endpoint maps are part of the conclusion.

When \(O\) is a family of local boundary models, their finite sums retain the stalk, quotient, generation and flabbiness properties by these componentwise formulas. The local decomposition proof uses the corresponding source lemmas.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.ModelSum`: [CharacterReciprocity.lean:364](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L364).

`OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.mono`: [CharacterReciprocity.lean:375](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L375).

`OAI.KLInvariance.MomentGraph.Sheaf.zero`: [MinimalExtensions.lean:271](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L271).

`OAI.KLInvariance.MomentGraph.Sheaf.prod`: [MinimalExtensions.lean:277](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L277).

`OAI.KLInvariance.MomentGraph.Sheaf.pi`: [GradedSheaves.lean:819](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L819).

`OAI.KLInvariance.MomentGraph.Sheaf.pi_compatible`: [GradedSheaves.lean:825](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L825).
