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
- kl.detail.morphism_extension
- kl.detail.top_splitting
- kl.notes.minimal_cover_existence
- kl.notes.graded_projective_free
- kl.detail.model_sums
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

# Decomposing a free flabby sheaf into shifted boundary models

Let \(A\) be a connected nonnegatively graded Noetherian domain and let the labelled ordered graph be finite. Fix a boundary-model family \(O_c\). Every graded sheaf \(B\) with free stalks, the upper quotient rule, flabbiness, and global generation admits a graded isomorphism
\[
B\simeq\bigoplus_{c,i}O_c(d_{c,i}),\qquad d_{c,i}\in\mathbb N,
\]
with finitely many summands.

*Proof.*

### Step 1. State the downward-induction invariant

Maintain an upper set \(U\), a finite sum \(C\) of nonnegatively shifted models \(O_c\) with \(c\in U\), and a graded isomorphism \(B|_U\simeq C|_U\). Initially \(U=\varnothing\) and \(C=0\); the assertion on the empty set is vacuous.

Choose a maximal vertex \(x\notin U\). All its strict upper neighbors lie in \(U\), so the existing isomorphism identifies the two boundary images at \(x\); denote the identified module by \(D\).

### Step 2. Compare the two stalk covers

The map \(f:B^x\twoheadrightarrow D\) is surjective by flabbiness and generation. The map \(p:C^x\twoheadrightarrow D\) is a minimal free cover: every model already in \(C\) has top in \(U\), different from \(x\), so its minimality condition holds at \(x\), and finite sums and grading shifts preserve that kernel containment.

Lift \(f\) through \(p\) to a graded map \(g:B^x\to C^x\), using freeness of \(B^x\). Lift \(p\) through \(f\) to \(h_0:C^x\to B^x\), using freeness of \(C^x\). The composite \(gh_0\) lies over the identity of \(D\); minimality of \(p\) makes it invertible by the minimal-cover argument. Replace \(h_0\) with \(h=h_0(gh_0)^{-1}\). Then \(gh=1\).

### Step 3. Separate the residual free generators

Let \(K=\ker g\). The splitting gives
\[
B^x\simeq C^x\oplus K,\qquad
v\longmapsto(gv,\ v-hgv).
\]
Its inverse sends \((c,k)\) to \(hc+k\). These formulas verify both inverse identities and preserve grading.

The kernel is a finite graded projective module, as a direct summand of the free stalk \(B^x\). The homogeneous-basis theorem makes it free, with homogeneous basis degrees \(d_1,\ldots,d_m\ge0\), since its grading is inherited from a nonnegative stalk.

### Step 4. Realize those generators by model summands

Put \(S=\bigoplus_{i=1}^mO_x(d_i)\) and replace \(C\) by \(C\oplus S\). At \(x\), the normalized top stalk of \(O_x\) identifies \(S^x\) with \(K\), giving the isomorphism in Step 3.

At any \(y\in U\), the relation \(y\le x\) is impossible: because \(U\) is upper, it would imply \(x\in U\). The model support therefore gives \(S^y=0\). An edge with target in \(U\) likewise has zero \(S\)-edge module by the quotient rule. Hence the old isomorphism on \(U\) remains unchanged.

### Step 5. Check compatibility and finish

At a new outgoing edge from \(x\), the \(C\)-component commutes with restriction because \(pg=f\). The \(S\)-component has zero edge target, so its square commutes automatically. Incoming edge maps are induced from the new upper-stalk isomorphism through the common quotient rule.

We have extended the isomorphism to \(U\cup\{x\}\) while retaining the invariant. The complement decreases by one; finiteness finishes the induction. The final sum is an isomorphism of sheaves, so the same summands control stalks and their outgoing kernels.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization



`OAI.KLInvariance.MomentGraph.GradedSheaf.exists_modelSumIso`: [SheafMorphisms.lean:1642](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1642).
