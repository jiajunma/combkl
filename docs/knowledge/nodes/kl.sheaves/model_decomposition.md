---
id: kl.detail.model_decomposition
title: Decomposing a free flabby sheaf into shifted boundary models
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.boundary_models
- kl.detail.model_sums
- kl.sheaves.model_sum_step
- kl.detail.sheaf_isomorphisms
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.exists_modelSumIso
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1642
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.exists_modelSumIso
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- moment_graph_sheaves
---

# Decomposing a free flabby sheaf into shifted boundary models

Let \(A\) be a connected nonnegatively graded Noetherian domain, and let the labelled ordered graph have finite vertex and edge sets. Fix a boundary-model family \((O_c)\).

Every graded sheaf \(B\) with free stalks, the upper-quotient rule, flabbiness, and global generation has a graded sheaf isomorphism
\[
B\simeq\bigoplus_{c,j}O_c(d_{c,j}),
\qquad d_{c,j}\in\mathbb N,
\]
with finitely many summands.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Related descent in different coefficient settings.**

**OpenAI notes:** The plane-localization proposition descends through a finite coset graph over an ungraded local ring. Nakayama makes the lifted stalk map surjective, its free target gives a splitting, and projectivity over the local ring makes the remainder free. Multiplicities count copies of local structure models. [loc:decomposition](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L285).

**Lean (primary):** The graded construction lifts in both directions and corrects the composite using invertibility modulo the positive ideal. The remainder is graded projective over a connected Noetherian domain and has a homogeneous basis. Its degrees determine nonnegative shifts of boundary models. Partial isomorphisms already include every edge whose upper endpoint has been processed. [SheafMorphisms:1427](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1427), [SheafMorphisms:1567](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1567), [SheafMorphisms:1642](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1642).

**Role in the proof:** Both constructions split a stalk over the upper boundary image and add models centered at the new vertex. The graded construction records a polynomial of shifts at each center; the ungraded local construction records an integer number of copies.
<!-- source-comparison:end -->

*Proof.*

### Step 1. State the induction data

Maintain an upper set \(U\), a constructed model sum \(C\) centered in \(U\), and a graded partial isomorphism from \(B\) to \(C\) on \(U\).

The partial data include vertex maps at all \(y\in U\) and edge maps whenever the upper endpoint lies in \(U\). The lower square is imposed when both endpoints are in \(U\), and the upper square whenever the target is in \(U\).

We prove that these data extend to a decomposition on the whole graph, by induction on the number of missing vertices.

### Step 2. Start with the empty domain

Take \(U=\varnothing\) and \(C=0\), the zero constructor for a model sum. No vertex belongs to \(U\), and no edge has its target there, so the partial isomorphism has no components to choose. This provides the initial data.

### Step 3. Choose a maximal missing vertex

If the missing set is nonempty, its finiteness supplies a maximal element \(x\). Every \(y>x\) already lies in \(U\); otherwise it would be a larger missing vertex.

The [[node:kl.sheaves.model_sum_step|model-sum extension theorem]] applies because \(B^x\) is free and the other sheaf properties are the hypotheses of the present theorem. It produces a new model sum \(D\) centered in \(U'=U\cup\{x\}\), and a graded partial isomorphism on \(U'\).

The set \(U'\) is upper. An element above a vertex of \(U\) remains in \(U\); an element strictly above \(x\) belongs to \(U\) by maximality. Thus the induction data are preserved.

### Step 4. Continue on a strictly smaller complement

The new missing set is the old set with \(x\) removed, so its cardinality decreases by one. Apply the induction hypothesis to the new data.

When no vertex is missing, \(U=V\). Every vertex map and every edge map is then present, with both restriction squares. The partial isomorphism is a full graded sheaf isomorphism, and the target is a model sum centered in the whole vertex set.

### Step 5. Follow the one-edge construction

For \(B=O_y\oplus O_x(2)\) on \(x\to y\), the first vertex is \(y\). Its stalk has one degree-zero generator, so the first block is \(O_y\).

At \(x\), compare
\[
B^x=A\oplus A(2)\longrightarrow A/(\alpha)
\]
with the minimal cover \(O_y^x=A\to A/(\alpha)\). The remainder is \(A(2)\), so the next block is \(O_x(2)\).

The completed isomorphism records exactly the two summands and their restriction maps. The character formulas use this same construction at both stalks and outgoing kernels.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.exists_modelSumIso`: [SheafMorphisms.lean:1642](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1642).
