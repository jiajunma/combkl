---
id: kl.detail.top_splitting
title: Extending a split top stalk to a sheaf summand
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.morphism_extension
- kl.sheaves.boundary_sheaf
- kl.detail.split_summands
- kl.sheaves.boundary_top_detection
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

Let \(A\) be a connected nonnegatively graded Noetherian domain, and let \(B\) be a normalized minimal-boundary sheaf on a finite labelled ordered graph with greatest vertex \(b\).

Let \(C\) be a graded sheaf with free stalks, the same upper-quotient rule, flabbiness, and global generation. Suppose degree-zero maps
\[
i_b:B^b\to C^b,\qquad p_b:C^b\to B^b,\qquad p_bi_b=1
\]
split the top stalk. Then these maps extend to a split pair of graded sheaf morphisms, so \(B\) is a graded summand of \(C\).

*Proof.*

### Step 1. Extend the top maps in both directions

The set \(\{b\}\) is upper because \(b\) is greatest. Each of the two prescribed vertex maps determines the incoming edge maps through the upper quotients.

Apply the morphism-extension theorem to \(B\to C\). Its hypotheses hold: both sheaves have the same upper quotients, are flabby and globally generated, and the source stalks of \(B\) are free. Apply it again to \(C\to B\), now using freeness of the stalks of \(C\).

We obtain graded sheaf maps \(i:B\to C\) and \(p:C\to B\) with the prescribed top components.

### Step 2. Prove the composite is a sheaf automorphism

Let \(f=pi:B\to B\). At the top,
\[
f_b=p_bi_b=1_{B^b}.
\]
The top-detection theorem [[node:kl.sheaves.boundary_top_detection]] applies to the morphism \(f\) between \(B\) and itself. It compares minimal stalk covers downward from the top and yields bijectivity at every stalk and edge. Thus \(f\) is a graded sheaf automorphism.

### Step 3. Correct the inclusion

Define
\[
\widehat i=i f^{-1}:B\to C.
\]
Then
\[
p\widehat i=pi f^{-1}=ff^{-1}=1_B
\]
at every vertex and edge. The maps \(\widehat i,p\) therefore form a split pair.

Since \(f_b=1\), its inverse at the top is also the identity. Hence \(\widehat i_b=i_b\), and the correction retains the original top maps.

## References

The source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.BoundarySheaf.splitIn_of_top_split`: [SheafMorphisms.lean:1380](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1380).
