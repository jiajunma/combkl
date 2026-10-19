---
id: kl.sheaves.boundary_existence
title: Existence of normalized boundary sheaves on finite ordered graphs
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.boundary_sheaf
- kl.detail.boundary_extension
- kl.notes.minimal_cover_existence
- kl.detail.graph_transport
- kl.foundations.finite_intervals
- kl.detail.polynomial_labels
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.MomentGraph.exists_boundarySheaf_card
  - OAI.KLInvariance.MomentGraph.exists_boundarySheaf
  - OAI.KLInvariance.BruhatGraph.exists_boundarySheaf
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:1177
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.exists_boundarySheaf_card
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:1238
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.exists_boundarySheaf
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:172
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.exists_boundarySheaf
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

# Existence of normalized boundary sheaves on finite ordered graphs

Let \(A\) be a nonnegatively graded Noetherian \(k\)-algebra such that every coefficient is congruent to a scalar modulo \(A_{>0}\). Let \(G\) be a finite ordered graph with greatest vertex \(b\), and suppose every edge label is homogeneous of degree one.

Then \(G\) admits a normalized minimal-boundary sheaf with distinguished stalk \(A\) at \(b\).

In particular, this applies to every Bruhat interval \([u,b]\) in a finite-generator Coxeter system, with polynomial coefficients from a basis of the real extended realization and its degree-one root labels.

*Proof.*

### Step 1. Establish the one-vertex case

If \(b\) is the only vertex, there are no edges, since every edge must strictly increase the order. Set \(B^b=A\) with its coefficient grading, whose unit generator has degree zero.

The stalk is free; its values are global sections; every compatible assignment extends; and there are no non-top minimality conditions. This supplies the boundary-sheaf data.

### Step 2. Remove a minimal vertex in the general case

Proceed by strong induction on the number of vertices. If there is more than one vertex, choose a minimal vertex \(x\).

It differs from \(b\): if \(x=b\), every vertex would be at most \(x\), and minimality would force equality. No edge ends at \(x\), because its source would be strictly smaller.

Remove \(x\) and all edges starting at it. The remaining finite graph still has greatest vertex \(b\), has fewer vertices, and retains its homogeneous labels.

### Step 3. Apply induction and reconstruct the removed data

Induction gives a boundary sheaf on the remaining graph. Regard the removed edges as attachments from a newly adjoined bottom vertex to their old targets.

The [[node:kl.detail.boundary_extension|bottom-attachment theorem]] constructs the new free stalk, edge quotients, and restrictions through a minimal cover of the attachment boundary image. It preserves generation and edge flabbiness, preserves old minimality, and supplies minimality at the new vertex.

### Step 4. Return to the original graph

Identify the adjoined vertex with \(x\), the retained vertices with their original vertices, and the old and attachment edge sets with the original edge set. These are bijections preserving sources, targets, and labels.

Reindex the constructed sheaf along those bijections. Free stalks, quotient maps, and outgoing kernels are transported componentwise. Edge-closed subsets correspond under the incidence bijection, so edge flabbiness transports as well; global generation is transported by reindexing sections.

The distinguished vertex is still \(b\), whose stalk retains its normalization. All the fields of a minimal-boundary sheaf are now verified on the original graph.

### Step 5. Check the Bruhat specialization

A Bruhat interval is finite, and its reflection edges form a finite set of vertex pairs. Its greatest vertex is \(b\).

The real polynomial coefficient algebra is Noetherian and nonnegatively graded, and reduction modulo its positive ideal is the base field. The polynomial root labels have degree one. Hence all hypotheses of the general construction hold, proving the stated specialization.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.exists_boundarySheaf_card`: [GradedSheaves.lean:1177](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L1177).

`OAI.KLInvariance.MomentGraph.exists_boundarySheaf`: [GradedSheaves.lean:1238](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L1238).

`OAI.KLInvariance.BruhatGraph.exists_boundarySheaf`: [SheafMorphisms.lean:172](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L172).
