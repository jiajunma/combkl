---
id: kl.sheaves.stalk_remainder
title: Decomposing a stalk over an identified upper boundary
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.boundary_image_identity
- kl.algebra.minimal_cover_remainder
- kl.detail.sheaf_isomorphisms
- kl.sheaves.minimal_cover
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.split_stalk_graded
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1496
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.split_stalk_graded
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

# Decomposing a stalk over an identified upper boundary

Work over a connected nonnegatively graded Noetherian domain. Let \(B,C\) be graded sheaves on an ordered graph with finitely many edges. Fix a vertex \(x\).

Assume both sheaves are flabby and globally generated, both stalks \(B^x,C^x\) are free, and \(C\) is kernel-minimal at \(x\). Suppose an isomorphism above \(x\) is given, with degree-preserving edge components. Let
\[
T_x:\partial_xB\xrightarrow{\sim}\partial_xC
\]
be its induced boundary-product isomorphism.

Then there are a degree-zero map \(g:B^x\to C^x\), a finite graded free module \(K=\ker g\), and a graded isomorphism
\[
E:B^x\xrightarrow{\sim}C^x\oplus K
\]
such that
\[
T_xr_x^B(v)=r_x^C\bigl(\operatorname{pr}_1E(v)\bigr).
\]

*Proof.*

### Step 1. Identify the target boundary image

The above-\(x\) isomorphism identifies compatible tuples on the strict upper set. Applying its edge maps to their quotient values identifies the boundary images:
\[
T_x(B^{\delta x})=C^{\delta x}.
\]
Use \(T=\operatorname{im}r_x^C=C^{\delta x}\) as a common target. Its grading is the range grading of the degree-zero stalk map \(r_x^C\). The boundary product is finite because the edge set is finite. This supplies the graded target directly from the finite stalk and edge modules.

### Step 2. Form the two free covers

Global generation and flabbiness give the [[node:kl.sheaves.boundary_image_identity|boundary-image equality]] for both sheaves. Therefore
\[
f=T_xr_x^B:B^x\twoheadrightarrow T,\qquad
\pi=r_x^C:C^x\twoheadrightarrow T
\]
are surjections with codomains restricted to that image. They preserve degree because the stalk restrictions and the edge components of \(T_x\) preserve degree.

The source stalks are finite free. Kernel minimality of \(C\) says
\(\ker\pi\subseteq JC^x\).
Thus \(\pi\) is a minimal graded free cover of \(T\).

### Step 3. Apply the free-cover remainder theorem

[[node:kl.algebra.minimal_cover_remainder|That theorem supplies]] degree-zero maps \(g:B^x\to C^x\) and \(h:C^x\to B^x\) with
\[
\pi g=f,\qquad gh=1.
\]
For the finite graded free remainder \(K=\ker g\), it gives
\[
E(v)=(gv,v-hgv).
\]
The inverse is \((c,k)\mapsto hc+k\), with both maps preserving degree.

### Step 4. Check the boundary equation

The first component of \(E(v)\) is \(gv\). Hence
\[
r_x^C(\operatorname{pr}_1E(v))
=\pi(gv)=f(v)=T_xr_x^B(v).
\]
The remainder contributes zero to this boundary value. It is the part represented by new model summands centered at \(x\) in the global decomposition.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.split_stalk_graded`: [SheafMorphisms.lean:1496](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1496).
