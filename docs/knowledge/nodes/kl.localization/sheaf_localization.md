---
id: kl.notes.sheaf_localization
title: Flat base change of selected kernels and edge images
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.detail.base_change
- kl.sheaves.section_constraints
- kl.algebra.flat_embedded_modules
- kl.sheaves.base_change_properties
- kl.sheaves.upward_kernel
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.kernelConstraint_tensor
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChange_upwardKernel
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChange_lowerImage
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChange_upperImage
  - OAI.KLInvariance.MomentGraph.Sheaf.edge_subsingleton_of_unit
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:330
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.kernelConstraint_tensor
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:347
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChange_upwardKernel
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:360
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChange_lowerImage
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:367
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChange_upperImage
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:534
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.edge_subsingleton_of_unit
  - artifact: openai-kl-paper
    locator: 4. Localization at a root plane; loc:decomposition
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the outgoing-constraint tensor identity, embedded kernel equality
    and both edge-image substitutions. Kept finite edges but no finite-vertex hypothesis,
    separated the extra upper-quotient/unit-label claim, and removed dihedral models
    as a prerequisite of this general flat-algebra theorem.
tags:
- Kazhdan-Lusztig
- sheaf-operations
---

# Flat base change of selected kernels and edge images

Let \(\varphi:R\to S\) be a flat homomorphism of commutative rings, and let \(B\) be an \(R\)-linear sheaf on an ordered graph with finitely many edges. For a vertex \(x\) and a set \(F\) of outgoing edges at \(x\),
\[
(K_x^B(F))_S=K_x^{B_S}(F)
\quad\text{inside }S\otimes_R B^x.
\]
Here \(P_S\) denotes the image of \(S\otimes_R P\) in the ambient tensor module.

For an edge \(e:x\to y\), let \(F\) be a set of outgoing conditions at \(x\), and \(H\) one at \(y\). Then
\[
\bigl(\rho^{B,-}_e(K_x^B(F))\bigr)_S
=\rho^{B_S,-}_e(K_x^{B_S}(F)),
\]
\[
\bigl(\rho^{B,+}_e(K_y^B(H))\bigr)_S
=\rho^{B_S,+}_e(K_y^{B_S}(H)).
\]
Both image equalities hold inside the same module \(S\otimes_R B^e\).

If \(B\) also satisfies the upper-quotient rule for labels \(\alpha_e\), an edge with invertible \(\varphi(\alpha_e)\) has zero module after base change, and its outgoing vanishing condition is automatic.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit finite-flat construction.**

**OpenAI notes:** The localization discussion uses flat extension of kernels and images and then decomposes the localized sheaf over the local ring on a dihedral coset. [loc:models](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L125), [loc:decomposition](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L285).

**Lean (primary):** The scalar-extension lemmas first treat general commutative rings and graph sheaves. Finite product maps identify tensor constraints; flat exactness gives section and selected-kernel identities. Image commutation is proved separately by tensor generators. [MinimalExtensions:1157](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1157), [MinimalExtensions:1162](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1162), [TerminalKernels:279](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L279), [TerminalKernels:360](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L360).

**Role in the proof:** These algebraic results precede the root-plane and coset specialization. The later pullback argument controls the surviving edges, while both localized edge images retain their common ambient module.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Present the selected kernel by one constraint map

The outgoing constraint
\[
\kappa_{x,F}:B^x\to\prod_{e\in F}B^e,\qquad
v\mapsto(\rho^-_e(v))_e
\]
has kernel \(K_x^B(F)\).

The edge set is finite, so \(F\) is finite. Tensoring its product gives the coordinate isomorphism
\[
\Psi_F:S\otimes_R\prod_{e\in F}B^e
\xrightarrow{\sim}\prod_{e\in F}(S\otimes_R B^e).
\]
It sends \(s\otimes(v_e)_e\) to \((s\otimes v_e)_e\); the inverse sums the tensor coordinate inclusions.

### Step 2. Compare the old and new constraints

The constraint of \(B_S\) satisfies
\[
\kappa^{B_S}_{x,F}=\Psi_F(1\otimes\kappa^B_{x,F}).
\]
For a pure tensor \(s\otimes v\), both sides have \(e\)-coordinate
\(s\otimes\rho^-_e(v)\). Additivity proves the identity for all tensors.

Since \(\Psi_F\) is injective, an element is killed by the new constraint exactly when it is killed by \(1\otimes\kappa^B_{x,F}\).

### Step 3. Apply the [[node:kl.algebra.flat_embedded_modules|embedded-kernel identity]]

Flatness gives
\[
(K_x^B(F))_S
=(\ker\kappa^B_{x,F})_S
=\ker(1\otimes\kappa^B_{x,F}).
\]
Step 2 identifies the last kernel with \(\ker\kappa^{B_S}_{x,F}\), which is \(K_x^{B_S}(F)\). Every equality takes place in \(S\otimes_R B^x\).

### Step 4. Commute each edge image with scalar extension

The [[node:kl.algebra.flat_embedded_modules|embedded-image theorem]] gives
\[
\bigl(\rho^{B,-}_e(K_x^B(F))\bigr)_S
=(1\otimes\rho^{B,-}_e)\bigl((K_x^B(F))_S\bigr).
\]
Insert Step 3 and the definition
\(\rho^{B_S,-}_e=1\otimes\rho^{B,-}_e\). This proves the lower-image formula.

Apply the same calculation to the upper restriction and \(K_y^B(H)\) to obtain the upper-image formula. The resulting submodules share the ambient edge tensor module.

### Step 5. Evaluate a unit-label edge

Under the upper-quotient hypothesis, the [[node:kl.sheaves.base_change_properties|base-change property theorem]] gives a surjective upper restriction with kernel \(\varphi(\alpha_e)B_S^y\).

If \(\varphi(\alpha_e)\) is a unit, every \(v\in B_S^y\) is
\(\varphi(\alpha_e)(\varphi(\alpha_e)^{-1}v)\), so the whole stalk lies in the kernel. The upper map is zero and surjective, forcing \(B_S^e=0\).

Every restriction to this zero module vanishes. Deleting that equation therefore leaves any selected outgoing kernel unchanged. Taking \(S\) to be the root-plane localization ring gives this algebraic transport on the full Bruhat graph. The next step restricts the resulting sheaf to a surviving coset.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.kernelConstraint_tensor`: [TerminalKernels.lean:330](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L330).

`OAI.KLInvariance.MomentGraph.Sheaf.baseChange_upwardKernel`: [TerminalKernels.lean:347](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L347).

`OAI.KLInvariance.MomentGraph.Sheaf.baseChange_lowerImage`: [TerminalKernels.lean:360](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L360).

`OAI.KLInvariance.MomentGraph.Sheaf.baseChange_upperImage`: [TerminalKernels.lean:367](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L367).

`OAI.KLInvariance.MomentGraph.Sheaf.edge_subsingleton_of_unit`: [PlaneLocalization.lean:534](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L534).
