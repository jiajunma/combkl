---
id: kl.detail.local_models
title: Local boundary models over a local coefficient ring
kind: definition
status: formalized
primary_topic: kl.07_localization
topics:
- kl.07_localization
uses:
- kl.detail.structure_sheaves
- kl.detail.sheaf_isomorphisms
- kl.detail.localization_rings
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.LocalModels
  - OAI.KLInvariance.MomentGraph.Sheaf.ModelSum
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:352
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.LocalModels
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:364
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.ModelSum
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

# Local boundary models over a local coefficient ring

Let \(R\) be a commutative local ring with maximal ideal \(\mathfrak m\), and let the graph have edge labels \(\alpha_e\in R\). A family of local models assigns a sheaf \(O_c\) to every vertex \(c\), with the following conditions:

- Each stalk \(O_c^x\) is finite free over \(R\).
- Every upper edge map is surjective with kernel \(\alpha_e O_c^{t(e)}\).
- Each \(O_c\) is globally generated and flabby.
- The stalk is zero unless \(x\le c\).
- A chosen linear isomorphism identifies \(O_c^c\) with \(R\).
- For \(x\ne c\), the kernel of the full outgoing stalk map is contained in \(\mathfrak m O_c^x\).

The final condition is local minimality. It is stated using the maximal ideal of this coefficient ring, rather than the positive-degree ideal of a graded polynomial algebra. No grading is part of this local-model datum.

An ungraded model sum with centers in \(U\) is a finite iterated direct sum of finite numbers of copies of \(O_c\), with \(c\in U\). Its construction starts from zero and repeatedly adds such a block. Unlike a graded model sum, it carries no degree shifts. The local decomposition theorem gives an actual sheaf isomorphism to this sum. In the root-plane application, the coefficient ring is the prime localization and the models come from induced dihedral structure sheaves.

## References

The precise Lean sources are listed below.

## Lean formalization

The fields `sheaf`, `free`, `finite`, `quotient`, `generated`, `flabby`, `support`, `top`, and `minimal` record the family and the listed conditions. The ungraded model-sum constructors are `zero` and `add`.

`OAI.KLInvariance.MomentGraph.Sheaf.LocalModels`: [CharacterReciprocity.lean:352](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L352).

`OAI.KLInvariance.MomentGraph.Sheaf.ModelSum`: [CharacterReciprocity.lean:364](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L364).
