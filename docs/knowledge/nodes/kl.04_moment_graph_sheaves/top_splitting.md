---
id: kl.detail.top_splitting
title: Extending a split top stalk to a sheaf summand
kind: theorem
status: proved
primary_topic: kl.04_moment_graph_sheaves
topics:
- kl.04_moment_graph_sheaves
uses:
- kl.detail.morphism_extension
- kl.sheaves.boundary_sheaf
- kl.detail.split_summands
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.MomentGraph.BoundarySheaf.splitIn_of_top_split
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1380
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.BoundarySheaf.splitIn_of_top_split
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

# Extending a split top stalk to a sheaf summand

Let \(B\) be the normalized minimal-boundary sheaf on a finite labelled graph with greatest vertex \(b\), over a connected nonnegatively graded Noetherian domain. Let \(C\) be a graded sheaf with free stalks, the same upper quotient rule, flabbiness, and global generation. If graded maps
\[
i_b:B^b\to C^b,\qquad p_b:C^b\to B^b,\qquad p_bi_b=1
\]
split the top stalk, then \(B\) is a graded direct summand of \(C\).

*Proof.*

### Step 1. Extend both top maps with their hypotheses checked

The given maps \(i_b:B^b\to C^b\), \(p_b:C^b\to B^b\) satisfy \(p_bi_b=1\).
Apply the morphism-extension theorem once to \(B\to C\) and once to \(C\to B\). Both sheaves are flabby, globally generated, and obey the same upper quotient rule. Both have free stalks, so the required source-freeness condition holds in each direction. We obtain graded morphisms \(i,p\) agreeing with the given maps at \(b\).

Their composite \(f=pi\) is a sheaf endomorphism of \(B\) whose top component is the identity. It need not yet be the identity at other vertices.

### Step 2. Show that f is invertible below the top

Induct downward. Suppose its stalk maps are invertible above \(x\). Their quotient maps make its outgoing edge maps invertible, and hence identify the boundary image at \(x\) with itself by an automorphism \(a\).

The stalk map \(f_x\) lies over \(a\) on the minimal cover \(B^x\to D_x\). Lift \(a^{-1}\) through the cover, obtaining a graded map \(l\). Then both \(f_xl-1\) and \(lf_x-1\) have image in the cover kernel, hence in \(JB^x\).

A graded self-map congruent to the identity modulo \(J\) is bijective: its homogeneous cokernel has zero quotient modulo \(J\), so Nakayama makes it surjective; on a finite free module, a surjective self-map has invertible determinant and is injective. Therefore \(f_xl\) and \(lf_x\) are bijective. The former makes \(f_x\) surjective and the latter makes it injective. This completes the downward induction.

### Step 3. Construct the inverse as a sheaf morphism

Invert each bijective stalk and edge map. The equations expressing commutation with restrictions can be multiplied by these inverses, proving the same commutation equations for them. The inverses preserve degree, so they assemble into a graded sheaf inverse \(f^{-1}\).

### Step 4. Correct the splitting

Set \(\widehat i=i f^{-1}\). Then
\[
p\widehat i=pi f^{-1}=ff^{-1}=1
\]
at every stalk and edge. Thus \(B\) is a graded direct summand of \(C\). The correction is explicit; the argument never assumes that arbitrary extensions of the two top maps already split.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization



`OAI.KLInvariance.MomentGraph.BoundarySheaf.splitIn_of_top_split`: [SheafMorphisms.lean:1380](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1380).
