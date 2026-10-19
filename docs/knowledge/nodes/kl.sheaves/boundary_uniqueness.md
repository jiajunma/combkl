---
id: kl.detail.boundary_uniqueness
title: Uniqueness of the minimal-boundary sheaf up to graded isomorphism
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.boundary_sheaf
- kl.sheaves.boundary_image_identity
- kl.algebra.minimal_cover_maps
- kl.sheaves.partial_iso_extension
- kl.detail.sheaf_isomorphisms
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.extend_stalk_graded
  - OAI.KLInvariance.MomentGraph.BoundarySheaf.extend_iso
  - OAI.KLInvariance.MomentGraph.BoundarySheaf.exists_gradedIso
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:116
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.extend_stalk_graded
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:806
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.BoundarySheaf.extend_iso
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:829
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.BoundarySheaf.exists_gradedIso
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

# Uniqueness of the minimal-boundary sheaf up to graded isomorphism

Let \(A\) be a connected nonnegatively graded Noetherian domain, and let a finite labelled ordered graph have greatest vertex \(b\). Any two normalized minimal-boundary sheaves \(B,C\) with those labels admit a graded sheaf isomorphism.

*Proof.*

### Step 1. Start with an empty partial isomorphism

On \(U=\varnothing\), no vertex map or edge map is required. We construct a graded partial isomorphism on larger upper sets, by induction on the finite number of missing vertices.

Choose a maximal missing vertex \(x\). Every \(y>x\) already lies in \(U\).

### Step 2. Supply the normalized stalk when x is b

If \(x=b\), use the two prescribed top identifications with the graded unit module \(A\) to identify \(B^b\) and \(C^b\).

There are no outgoing edges from the greatest vertex, so the outgoing compatibility condition is empty. The [[node:kl.sheaves.partial_iso_extension|partial-isomorphism extension theorem]] adds this stalk map and the incoming edge maps induced by its upper quotients. Thus the partial data already include edges whose lower endpoints have not yet been added.

### Step 3. Identify the common boundary target at another vertex

Now assume \(x\ne b\). The existing partial isomorphism identifies the sheaves above \(x\), including the edge modules on all edges leaving \(x\). Its edge maps identify their boundary images.

By generation and flabbiness, each outgoing stalk map surjects onto its boundary image. Use the boundary-image identification to regard both maps as covers of one graded module \(T\):
\[
\pi:B^x\twoheadrightarrow T,\qquad
\rho:C^x\twoheadrightarrow T.
\]
Both stalks are finite free. Minimality at \(x\ne b\) gives
\[
\ker\pi\subseteq JB^x,\qquad
\ker\rho\subseteq JC^x.
\]
Thus both are minimal graded free covers.

### Step 4. Extend the stalk and edge isomorphisms

The [[node:kl.algebra.minimal_cover_maps|minimal-cover comparison theorem]] supplies a graded isomorphism
\(j_x:B^x\to C^x\) with \(\rho j_x=\pi\). In the original boundary products, this is exactly the lower commuting square on every outgoing edge from \(x\).

Apply the [[node:kl.sheaves.partial_iso_extension|partial-isomorphism extension theorem]]. It keeps the old components, uses \(j_x\) at \(x\), and defines each new incoming edge map by the common scalar quotient rule. This produces a graded partial isomorphism on \(U\cup\{x\}\).

### Step 5. Complete the finite induction

The new set is upper: elements above an old vertex stay in \(U\), and those strictly above \(x\) were already present. Its complement has one fewer vertex.

When the complement is empty, all vertex maps and all edge maps are present, with both restriction squares. They form a graded sheaf isomorphism \(B\simeq C\), proving uniqueness of the normalized object up to graded isomorphism.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.extend_stalk_graded`: [MinimalExtensions.lean:116](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L116).

`OAI.KLInvariance.MomentGraph.BoundarySheaf.extend_iso`: [MinimalExtensions.lean:806](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L806).

`OAI.KLInvariance.MomentGraph.BoundarySheaf.exists_gradedIso`: [MinimalExtensions.lean:829](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L829).
