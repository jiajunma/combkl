---
id: kl.sheaves.boundary_existence
title: Existence of the Bruhat minimal-boundary sheaf
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.boundary_sheaf
- kl.sheaves.minimal_cover
- kl.foundations.finite_intervals
- kl.notes.boundary_image
- kl.notes.minimal_cover_existence
- kl.detail.boundary_extension
- kl.detail.polynomial_labels
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.BruhatGraph.exists_boundarySheaf
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:172
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.exists_boundarySheaf
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- background
---

# Existence of the Bruhat minimal-boundary sheaf

For a finite-generator Coxeter system and \(u\le b\), choose a real basis of the extended Tits realization and express roots as degree-one coordinate polynomials. The Bruhat interval graph admits a minimal-boundary sheaf with top \(b\).

*Proof.*

### Step 1. Check the coefficient and graph hypotheses

For the Bruhat graph of \([u,b]\), interval finiteness gives finitely many vertices. Its edges are selected pairs of vertices, so there are finitely many edges too. The order has greatest vertex \(b\).

The coefficient ring is a real polynomial ring: it is Noetherian, nonnegatively graded, and its quotient by the positive-degree ideal is \(\mathbb R\). Every root label is homogeneous of degree one. These are exactly the hypotheses needed for the minimal-cover construction.

### Step 2. Induct on the number of vertices

For a one-vertex graph, take \(B^b=A\). There are no edges, every assignment is a global section, and every top-stalk value is realized. Freeness and the top normalization hold; the non-top minimality condition is vacuous.

For a graph with more than one vertex, choose a minimal vertex \(x\). It cannot equal the greatest vertex \(b\), because then every vertex would equal \(b\). No edge can end at \(x\): its source would be strictly smaller than \(x\).

### Step 3. Remove x and apply induction

Remove \(x\) and all edges whose source is \(x\). The remaining graph has fewer vertices, still has greatest vertex \(b\), and inherits the same homogeneous labels. Induction constructs its boundary sheaf.

The removed edges are now a finite list of attachments from a new bottom vertex to their old targets. Apply [[node:kl.detail.boundary_extension]]: form the boundary image, choose its minimal graded free cover, and attach that cover as the stalk at \(x\).

### Step 4. Verify the definition's conditions separately

Old stalks remain free and the new stalk is free. Old quotient maps remain unchanged and new ones were defined as quotients. Extension from edge-closed subsets and global generation hold by the two lifting arguments in the attachment theorem.

The top stalk remains the old stalk \(A\), because \(x\ne b\). Minimality at \(x\) is the kernel condition of its chosen cover; minimality at old vertices is unchanged. Thus all fields required for a minimal-boundary sheaf have been supplied.

### Step 5. Return to the original graph labels

The attachment construction uses a graph with a formally adjoined bottom vertex. Identify that bottom with the removed \(x\), the old vertices with their original vertices, and the two classes of edges with the original edge set. This graph isomorphism preserves sources, targets, and labels. Reindex the constructed sheaf along it to obtain the required sheaf on the original Bruhat graph.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.exists_boundarySheaf`: [SheafMorphisms.lean:172](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L172).
