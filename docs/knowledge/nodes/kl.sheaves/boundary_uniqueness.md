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
- kl.detail.boundary_extension
- kl.notes.graded_nakayama
- kl.detail.sheaf_isomorphisms
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.BoundarySheaf.exists_gradedIso
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:829
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.BoundarySheaf.exists_gradedIso
  - artifact: openai-kl-paper
    locator: Related paper context; bg:bmp
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
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

Let \(A\) be a connected nonnegatively graded Noetherian domain over a field, and let a finite labelled ordered graph have a greatest vertex \(b\). Two minimal-boundary sheaves with the same labels and top normalization are graded-isomorphic.

The assertion is existence of an isomorphism, not uniqueness of that isomorphism.

*Proof.*

### Step 1. Prove the local minimal-cover comparison

Let \(p:F\twoheadrightarrow D\) and \(q:G\twoheadrightarrow D\) be minimal graded free covers. Freeness of \(F\) allows a graded lift \(h:F\to G\) with \(qh=p\), by lifting a homogeneous basis degree by degree.

Both covers induce isomorphisms modulo the positive ideal \(J\). For example, if \(p(v)\in JD\), lift an expression for \(p(v)\) from \(JF\); subtracting that lift puts \(v\) in \(\ker p\subseteq JF\). Thus \(p^{-1}(JD)=JF\), proving injectivity of the induced quotient map. Surjectivity is inherited from \(p\). The same applies to \(q\). Hence \(h\) is an isomorphism modulo \(J\).

### Step 2. Upgrade the lift to an isomorphism

The cokernel of \(h\) is graded and bounded below; its quotient by \(J\) is zero. Graded Nakayama makes it zero, so \(h\) is surjective. Since \(G\) is free, \(h\) has a linear section, giving \(F\simeq G\oplus K\), where \(K=\ker h\).

Injectivity modulo \(J\) gives \(K\subseteq JF\). Projecting this containment onto the summand \(K\) gives \(K=JK\). The kernel is homogeneous and bounded below, so graded Nakayama gives \(K=0\). Thus \(h\) is bijective. Its inverse preserves degree because a bijective graded map has a unique homogeneous preimage of each homogeneous element.

### Step 3. Start the sheaf comparison at the top

Both top stalks are the normalized module \(A\). Identify them by their prescribed graded normalization. There are no edges above the greatest vertex, so this is compatible initial data.

Suppose a graded isomorphism is already defined on an upper set. Choose a maximal missing vertex \(x\). The existing isomorphism identifies sections above \(x\), hence their boundary images. The two stalk boundary maps are minimal covers of that common image: surjectivity onto it follows from flabbiness and global generation, and kernel minimality is a boundary-sheaf condition.

### Step 4. Extend over x and its incident edges

Apply Steps 1–2 to obtain the stalk isomorphism at \(x\), commuting with the boundary maps. Outgoing lower squares therefore commute. Incoming edge modules are quotients by the same labels; the stalk isomorphism induces their edge isomorphisms, commuting with upper restrictions. All old maps are retained.

The enlarged vertex set is upper and has smaller complement. Finite downward induction yields a graded isomorphism of the whole sheaves. The choices of lifts show why existence is asserted; the resulting isomorphism is not claimed to be unique.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization



`OAI.KLInvariance.MomentGraph.BoundarySheaf.exists_gradedIso`: [MinimalExtensions.lean:829](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L829).
