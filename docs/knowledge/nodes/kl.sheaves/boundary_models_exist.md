---
id: kl.sheaves.boundary_models_exist
title: Construction of normalized models at every vertex
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.boundary_models
- kl.sheaves.boundary_existence
- kl.sheaves.lower_extension_properties
- kl.detail.graph_transport
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.MomentGraph.lowerBoundary
  - OAI.KLInvariance.MomentGraph.actualBoundaryModels
  - OAI.KLInvariance.BruhatGraph.lowerIntervalMap
  - OAI.KLInvariance.BruhatGraph.lowerIntervalBoundary
  - OAI.KLInvariance.BruhatGraph.boundaryModels
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:757
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.lowerBoundary
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:762
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.actualBoundaryModels
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:348
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.lowerIntervalMap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:378
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.lowerIntervalBoundary
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:385
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.boundaryModels
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

# Construction of normalized models at every vertex

Let \(A\) be a nonnegatively graded Noetherian algebra over a field \(k\). Assume that every \(a\in A\) is congruent to a scalar from \(k\) modulo the positive ideal \(J\). Let the ordered graph have finite vertex and edge sets, and let every label be homogeneous of degree one.

Then a boundary-model family exists on the graph.

For the Bruhat graph of \([1,b]\), the model centered at \(c\le b\) is the actual normalized boundary sheaf on \([1,c]\), reindexed onto the corresponding lower graph and extended by zero.

*Proof.*

### Step 1. Restrict the graph to a principal lower ideal

For each \(c\), let \(K_c=\{x:x\le c\}\). This is a lower ideal and has greatest vertex \(c\). Its lower graph has finite vertices and edges, and the inherited labels remain homogeneous of degree one.

### Step 2. Construct its normalized boundary sheaf

The finite [[node:kl.sheaves.boundary_existence|boundary-existence theorem]] applies to this lower graph and the coefficient hypotheses. It gives a sheaf \(B_c\) with free stalks, upper quotients, edge flabbiness, global generation, normalization at \(c\), and minimality away from \(c\).

Extend \(B_c\) by zero and call the resulting sheaf \(O_c\).

### Step 3. Verify the model-family fields

The [[node:kl.sheaves.lower_extension_properties|lower-extension theorem]] preserves free stalks, upper quotients, flabbiness, and generation. It makes \(O_c^x=0\) whenever \(x\not\le c\).

At \(c\), the inside-stalk identification followed by the boundary normalization gives
\[
O_c^c\simeq B_c^c\simeq A.
\]
Both maps preserve degree.

For \(x\ne c\) inside the ideal, boundary minimality passes through lower extension. For \(x\) outside it, the stalk and outgoing kernel are zero. Thus the model is minimal away from its center. Choosing these constructions for all \(c\) supplies the boundary-model family.

### Step 4. Identify the Bruhat lower graph

Inside \([1,b]\), the lower ideal below \(c\) consists of the elements \(x\) with \(1\le x\le c\). Its vertices therefore identify with \([1,c]\).

An edge in the lower graph has target at most \(c\), and its source is below that target. It is exactly the same reflection edge in \([1,c]\). The vertex and edge identifications preserve the reflection labels, hence the polynomial root labels.

Pull back the chosen boundary sheaf on \([1,c]\) along this graph identification and extend it by zero. This is the concrete Bruhat model family used in the character decomposition.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.lowerBoundary`: [MinimalExtensions.lean:757](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L757).

`OAI.KLInvariance.MomentGraph.actualBoundaryModels`: [MinimalExtensions.lean:762](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L762).

`OAI.KLInvariance.BruhatGraph.lowerIntervalMap`: [SheafMorphisms.lean:348](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L348).

`OAI.KLInvariance.BruhatGraph.lowerIntervalBoundary`: [SheafMorphisms.lean:378](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L378).

`OAI.KLInvariance.BruhatGraph.boundaryModels`: [SheafMorphisms.lean:385](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L385).
