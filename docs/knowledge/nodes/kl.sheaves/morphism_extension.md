---
id: kl.detail.morphism_extension
title: Extending a sheaf morphism from an upper set
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.sheaf_morphism
- kl.sheaves.boundary_morphism_lift
- kl.sheaves.morphism_extension_step
- kl.detail.upper_quotient
- kl.sheaves.flabbiness
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.ofUniv
  - OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.exists_extension
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:607
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.ofUniv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:834
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.exists_extension
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
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the full finite-complement strong induction, empty case, maximal missing
    vertex, graded stalk lift, one-vertex extension and old-vertex transport. The
    final old-edge equality is derived explicitly from the source conclusion and upper-map
    surjectivity.
tags:
- Kazhdan-Lusztig
- sheaf-operations
---

# Extending a sheaf morphism from an upper set

Let \(k\) be a field and \(A\) a connected nonnegatively graded Noetherian domain over \(k\). Let the ordered graph have finite vertex set \(V\) and edge set \(E\), with labels \(\alpha_e\).

Suppose \(B,C\) are graded sheaves satisfying the upper-quotient rule for these labels. Assume both are flabby and globally generated, and every stalk of \(B\) is free.

For an upper set \(U\), every degree-zero partial morphism \(j\) on \(U\) extends to a degree-zero sheaf morphism \(f:B\to C\) with
\[
f_x=j_x\qquad(x\in U).
\]
The upper-quotient rule also makes its edge maps agree with \(j_e\) whenever \(t(e)\in U\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Graded extension preceding local decomposition.**

**OpenAI notes:** The local-ring decomposition descends through the coset vertices, lifting stalk maps over the common boundary image and retaining both endpoint restrictions. [loc:decomposition](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L285).

**Lean (primary):** The graded morphism-extension theorem works over a connected nonnegatively graded Noetherian domain. A homogeneous free-basis lift constructs the next stalk map, upper quotients construct the incoming edge maps, and finite-complement induction extends the partial morphism. [SheafMorphisms:675](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L675), [SheafMorphisms:723](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L723), [SheafMorphisms:834](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L834).

**Role in the proof:** This graded extension is used in boundary recognition and splitting. The ungraded local-ring decomposition is a later construction with its own local-ring and model hypotheses.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Set up induction on the missing vertices

Let \(T=V\setminus U\). Use strong induction on the finite set \(T\), proving extension for every partial morphism on its upper complement.

If \(T=\varnothing\), then \(U=V\). The partial morphism already supplies all vertex maps, all edge maps and both commuting squares. The source's ofUniv construction regards these as a full morphism.

### Step 2. Choose a maximal missing vertex

Assume \(T\ne\varnothing\), and choose a maximal element \(x\in T\). If \(x<y\), then \(y\notin T\): otherwise maximality would force \(y\le x\), contradicting \(x<y\). Hence every vertex strictly above \(x\) lies in \(U\).

Apply the [[node:kl.sheaves.boundary_morphism_lift|boundary-morphism lifting theorem]]. Its hypotheses hold because the edge set is finite, the source stalk \(B^x\) is free, and both sheaves are flabby and generated. It gives a degree-zero \(l_x:B^x\to C^x\) with
\[
r_C l_x=j_{\partial x}r_B.
\]
Evaluating this tuple equation at an outgoing edge gives
\(j_e\rho^{B,-}_e=\rho^{C,-}_e l_x\).

### Step 3. Extend across the chosen vertex

The [[node:kl.sheaves.morphism_extension_step|one-vertex morphism extension theorem]] applies to \(U,x,j,l_x\) and the upper-quotient rules. It gives a partial morphism \(j'\) on \(U'=U\cup\{x\}\) that agrees with all old vertex maps.

The new set is upper. If \(y\in U\) and \(y\le z\), then \(z\in U\). If \(y=x\), either \(z=x\), or \(x<z\) and the maximality argument places \(z\) in \(U\).

Its complement is \(T\setminus\{x\}\), a strict subset of \(T\).

### Step 4. Apply the strictly smaller induction instance

The induction hypothesis extends \(j'\) to a full morphism \(f\) agreeing on \(U'\). For each \(y\in U\),
\[
f_y=j'_y=j_y.
\]
The first equality is the smaller-set induction conclusion; the second is preservation in the one-vertex construction. This completes the induction and proves the vertex agreement claimed by exists_extension.

### Step 5. Recover agreement on the old edge maps

Let \(e\) have target \(y\in U\). Both morphisms have the upper commuting square, and \(f_y=j_y\), so
\[
f_e\rho^{B,+}_e
=\rho^{C,+}_e f_y
=\rho^{C,+}_e j_y
=j_e\rho^{B,+}_e.
\]
The upper restriction \(\rho^{B,+}_e\) is surjective. Every edge vector has an upper-stalk preimage, and evaluating the displayed equality on that preimage gives \(f_e=j_e\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.ofUniv`: [SheafMorphisms.lean:607](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L607).

`OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.exists_extension`: [SheafMorphisms.lean:834](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L834).
