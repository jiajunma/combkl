---
id: kl.sheaves.word_adjoint_descent
title: The integral word adjoint descends to a graded sheaf map
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.word_sheaf
- kl.detail.word_flabbiness
- kl.detail.word_evaluation_injective
- kl.word.support_duality
- kl.sheaves.adjoint_properties
- kl.algebra.quotient_endomorphism_descent
lean:
  repository: openai-kl
  modules:
  - BalancedPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.bott_projection_zero_iff_annihilates_support
  - OAI.KLInvariance.TitsSpace.bottAdjoint_preserves_kernel
  - OAI.KLInvariance.TitsSpace.bottAdjoint_preserves_support
  - OAI.KLInvariance.TitsSpace.bottEndOfSheaf
  - OAI.KLInvariance.TitsSpace.bottEndOfSheaf_preserves_support
  - OAI.KLInvariance.TitsSpace.bottAdjointWordHom
  - OAI.KLInvariance.TitsSpace.bottAdjointSheaf
  - OAI.KLInvariance.TitsSpace.bottAdjointSheaf_vertex
  - OAI.KLInvariance.TitsSpace.bottEndOfAdjointSheaf
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:101
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bott_projection_zero_iff_annihilates_support
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:121
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottAdjoint_preserves_kernel
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:133
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottAdjoint_preserves_support
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:533
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEndOfSheaf
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:570
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEndOfSheaf_preserves_support
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:700
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottAdjointWordHom
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:717
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottAdjointSheaf
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:735
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottAdjointSheaf_vertex
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:743
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEndOfAdjointSheaf
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

# The integral word adjoint descends to a graded sheaf map

Fix a reduced word \(\mathbf s\) in a finite-generator Coxeter system and a basis of the extended realization. Let \(W_{\mathbf s}\) be its graded pair-projection sheaf on \([1,w(\mathbf s)]\), over the symmetric coefficient algebra \(A\). Let \(M=M_{\mathbf s}\), with perfect symmetric word pairing \(D\).

The section equivalence identifies \(M\) with all global sections of \(W_{\mathbf s}\). A graded sheaf endomorphism \(h\) therefore induces an \(A\)-linear word-module endomorphism \(F\). Its adjoint \(F^*\) descends to a graded sheaf endomorphism \(h^*\), characterized at every vertex by
\[
h_x^*(\pi_x(m))=\pi_x(F^*m).
\]
The word-module endomorphism induced by \(h^*\) is exactly \(F^*\).

*Proof.*

### Step 1. Transfer the sheaf map to the word module

Let \(J:M\xrightarrow{\sim}\Gamma(W_{\mathbf s})\) be the section equivalence. The induced word map is
\[
F=J^{-1}\circ\Gamma(h)\circ J.
\]
Its coordinates satisfy
\[
\pi_x(Fm)=h_x(\pi_x(m)),
\]
because \(\Gamma(h)\) applies \(h_x\) at each vertex.

Hence \(F\) preserves each projection kernel. It also preserves \(S_x\), the elements supported at weight \(x\): all stalk coordinates at other weights are zero, and a linear component map sends zero to zero. Every subexpression weight of a reduced word lies in the interval, so these stalk coordinates include all evaluation coordinates.

The maps \(J,J^{-1}\) preserve grading. For the inverse assertion, decompose a word element into homogeneous components. If all its stalk coordinates have degree \(n\), every component of another degree has zero evaluations. Injectivity of full evaluation makes each such component zero. Thus \(F\) preserves degrees.

### Step 2. Characterize the projection kernel by supported tests

We claim
\[
\pi_x(m)=0
\quad\Longleftrightarrow\quad
\langle s,m\rangle=0\text{ for every }s\in S_x.
\]
The forward implication is weight-support orthogonality.

For the converse, let \(\lambda\) be any coordinate functional on the image stalk \(M^x\subseteq A^{J_x}\). Weight-stalk duality supplies \(s_\lambda\in S_x\) with
\[
\langle s_\lambda,m\rangle=\lambda(\pi_x(m)).
\]
The assumed vanishing makes every coordinate of \(\pi_x(m)\) zero. Since the stalk is a submodule of that coordinate product, \(\pi_x(m)=0\).

### Step 3. Show the adjoint preserves every projection kernel

Suppose \(\pi_x(m)=0\), and take \(s\in S_x\). Symmetry and the adjoint equation give
\[
\langle s,F^*m\rangle=\langle Fs,m\rangle.
\]
Step 1 places \(Fs\) in \(S_x\); Step 2 therefore makes the right side zero. Applying the converse in Step 2 yields
\(\pi_x(F^*m)=0\).

There is a complementary support calculation. If \(m\in S_x\) and \(n\in\ker\pi_x\), then \(Fn\in\ker\pi_x\), so
\[
\langle F^*m,n\rangle=\langle m,Fn\rangle=0.
\]
The weight-support annihilator theorem gives \(F^*m\in S_x\).

### Step 4. Descend to vertex and edge maps

The stalk projection \(\pi_x\) is surjective by its image definition. Step 3 permits quotient descent, defining \(h_x^*\) by the stated formula.

At an edge \(x\to y\), its pair-projection quotient is built from \(\pi_x,\pi_y\). Both kernels are preserved by \(F^*\). The projection-and-edge descent theorem therefore supplies \(h_e^*\) with
\[
h_e^*\rho^-_e=\rho^-_e h_x^*,\qquad
h_e^*\rho^+_e=\rho^+_e h_y^*.
\]
These are exactly the two sheaf-morphism equations.

### Step 5. Preserve degrees and identify the section map

The word pairing is homogeneous, and \(F\) preserves degrees. The adjoint-grading theorem gives degree preservation for \(F^*\). Homogeneous lifts through each surjective stalk projection and lower edge map give degree preservation for every descended component. Thus \(h^*\) is a graded sheaf morphism.

The word map induced by \(h^*\) and \(F^*\) have the same projection at every vertex, by their defining equations. Together those projections give the full evaluation tuple. Injectivity of full evaluation therefore identifies the two word maps.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bott_projection_zero_iff_annihilates_support`: [BalancedPairings.lean:101](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L101).

`OAI.KLInvariance.TitsSpace.bottAdjoint_preserves_kernel`: [BalancedPairings.lean:121](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L121).

`OAI.KLInvariance.TitsSpace.bottAdjoint_preserves_support`: [BalancedPairings.lean:133](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L133).

`OAI.KLInvariance.TitsSpace.bottEndOfSheaf`: [BalancedPairings.lean:533](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L533).

`OAI.KLInvariance.TitsSpace.bottEndOfSheaf_preserves_support`: [BalancedPairings.lean:570](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L570).

`OAI.KLInvariance.TitsSpace.bottAdjointWordHom`: [BalancedPairings.lean:700](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L700).

`OAI.KLInvariance.TitsSpace.bottAdjointSheaf`: [BalancedPairings.lean:717](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L717).

`OAI.KLInvariance.TitsSpace.bottAdjointSheaf_vertex`: [BalancedPairings.lean:735](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L735).

`OAI.KLInvariance.TitsSpace.bottEndOfAdjointSheaf`: [BalancedPairings.lean:743](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L743).
