---
id: kl.sheaves.boundary_recognition
title: Recognition of a boundary sheaf by a primitive top splitting
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.top_splitting
- kl.detail.primitive_summand
- kl.sheaves.boundary_sheaf
- kl.detail.primitive_projectors
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  declarations:
  - OAI.KLInvariance.MomentGraph.BoundarySheaf.top_nontrivial
  - OAI.KLInvariance.MomentGraph.BoundarySheaf.iso_of_primitive_top_split
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1166
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.BoundarySheaf.top_nontrivial
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1176
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.BoundarySheaf.iso_of_primitive_top_split
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
- duality_and_characters
---

# Recognition of a boundary sheaf by a primitive top splitting

Let \(A\) be a connected nonnegatively graded Noetherian domain, and let \(G\) be a finite labelled ordered graph with greatest vertex \(b\). Let \(B\) be its normalized minimal-boundary sheaf.

Suppose a graded sheaf \(C\) has free stalks, the same upper-quotient rule, flabbiness, and global generation. Suppose its identity is primitive, and there are degree-zero maps
\[
i_b:B^b\to C^b,\qquad p_b:C^b\to B^b,\qquad p_bi_b=1.
\]
Then \(C\) is graded isomorphic to \(B\).

*Proof.*

### Step 1. Extend the top splitting

The [[node:kl.detail.top_splitting|top-splitting theorem]] applies because the graph is finite with greatest vertex \(b\), the coefficient algebra has the stated grading properties, and \(C\) has precisely the free-stalk, quotient, flabbiness, and generation hypotheses required there.

It produces graded sheaf morphisms
\[
i:B\to C,\qquad p:C\to B,\qquad pi=1_B.
\]
Their composite \(q=ip\) is a projector on \(C\).

### Step 2. Use primitivity and a nonzero normalized vector

Primitivity of \(1_C\) gives \(q=0\) or \(q=1_C\). The top module \(B^b\) is the graded unit module \(A\), so it contains the nonzero vector \(1\); the domain hypothesis gives \(1\ne0\).

If \(q=0\), then at the top
\[
p_bq_bi_b(1)=0.
\]
But \(q=ip\) and \(pi=1_B\) make the same expression equal to \(1\). Thus \(q\ne0\), and \(q=1_C\).

Here \(i_b,p_b\) denote the top components of the extended split maps; their splitting identity alone supplies the calculation.

### Step 3. Read off the isomorphism

The equations \(pi=1_B\) and \(ip=1_C\) hold on every vertex and edge component. Hence \(i,p\) are inverse linear isomorphisms at all components. They preserve grading and commute with restrictions because they are graded sheaf morphisms. They therefore define the required graded sheaf isomorphism.

## References

The source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.BoundarySheaf.top_nontrivial`: [CharacterReciprocity.lean:1166](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1166).

`OAI.KLInvariance.MomentGraph.BoundarySheaf.iso_of_primitive_top_split`: [CharacterReciprocity.lean:1176](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1176).
