---
id: kl.sheaves.flat_section_base_change
title: Sections commute with finite flat scalar extension
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.base_change
- kl.sheaves.section_constraints
- kl.detail.compatible_sections
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.tensorAssignments_bijective
  - OAI.KLInvariance.MomentGraph.Sheaf.constraint_tensorAssignments
  - OAI.KLInvariance.MomentGraph.Sheaf.tensorSections_surjective
  - OAI.KLInvariance.MomentGraph.Sheaf.tensorSections_injective
  - OAI.KLInvariance.MomentGraph.Sheaf.tensorSectionsEquiv
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1102
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.tensorAssignments_bijective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1107
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.constraint_tensorAssignments
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1121
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.tensorSections_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1147
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.tensorSections_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1157
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.tensorSectionsEquiv
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the finite assignment bijection, pure-tensor constraint identity,
    flat exactness and separate surjectivity/injectivity proofs. Kept the full ambient
    vertex product and the weaker finiteness requirement for injectivity.
tags:
- Kazhdan-Lusztig
- sheaf-operations
---

# Sections commute with finite flat scalar extension

Let \(R\to S\) be a homomorphism of commutative rings, and let \(B\) be an \(R\)-linear sheaf on an ordered graph with finite vertex and edge sets. Suppose \(S\) is flat as an \(R\)-module: tensoring with \(S\) preserves exact sequences.

For a vertex subset \(\Omega\), write \(E_\Omega=\{e:s(e),t(e)\in\Omega\}\). The natural map
\[
\Theta_\Omega:S\otimes_R\Gamma_\Omega(B)
\xrightarrow{\sim}\Gamma_\Omega(B_S)
\]
is an \(S\)-linear isomorphism. Its pure-tensor formula is
\[
\Theta_\Omega(s\otimes f)_x=s\otimes f_x.
\]
The injectivity assertion requires finiteness only of the vertex set; the surjectivity proof also uses the finite edge set.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit finite-flat construction.**

**OpenAI notes:** The localization discussion uses flat extension of kernels and images and then decomposes the localized sheaf over the local ring on a dihedral coset. [loc:models](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L125), [loc:decomposition](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L285).

**Lean (primary):** The scalar-extension lemmas first treat general commutative rings and graph sheaves. Finite product maps identify tensor constraints; flat exactness gives section and selected-kernel identities. Image commutation is proved separately by tensor generators. [MinimalExtensions:1157](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1157), [MinimalExtensions:1162](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1162), [TerminalKernels:279](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L279), [TerminalKernels:360](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L360).

**Role in the proof:** These algebraic results precede the root-plane and coset specialization. The later pullback argument controls the surviving edges, while both localized edge images retain their common ambient module.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Commute the finite assignment product with tensoring

Put \(P=\prod_{x\in V}B^x\). The assignment map
\[
\Phi:S\otimes_R P\to\prod_{x\in V}(S\otimes_R B^x)
\]
is bijective. Its inverse is the finite sum of the tensor maps induced by the coordinate inclusions \(\iota_x:B^x\to P\):
\[
(z_x)_x\longmapsto\sum_x(1\otimes\iota_x)(z_x).
\]

Projection onto a coordinate returns that coordinate, since the other coordinate inclusions project to zero. In the other direction, on \(s\otimes f\), the composite gives
\[
\sum_xs\otimes\iota_x(f_x)
=s\otimes\left(\sum_x\iota_x(f_x)\right)
=s\otimes f.
\]
Pure tensors generate the tensor product, so these are inverse linear maps.

The same construction for the finite set \(E_\Omega\) gives
\[
\Psi:S\otimes_R\prod_{e\in E_\Omega}B^e
\xrightarrow{\sim}\prod_{e\in E_\Omega}(S\otimes_R B^e).
\]

### Step 2. Compare the two constraint maps

Let \(\delta\) be the section constraint for \(B\), and \(\delta_S\) the constraint for \(B_S\). They satisfy
\[
\delta_S\Phi=\Psi(1\otimes\delta).
\]
On a pure tensor \(s\otimes f\), the \(e\)-coordinate of the left side is
\[
s\otimes\rho^-_e(f_{s(e)})
-s\otimes\rho^+_e(f_{t(e)})
=s\otimes\bigl(\rho^-_e(f_{s(e)})-\rho^+_e(f_{t(e)})\bigr),
\]
which is the right-hand coordinate. Additivity proves the identity on all tensors.

### Step 3. Tensor the kernel sequence

Let \(i:\Gamma_\Omega(B)\hookrightarrow P\) be the section inclusion. The [[node:kl.sheaves.section_constraints|constraint-kernel identity]] gives the exact sequence
\[
0\longrightarrow\Gamma_\Omega(B)\xrightarrow{i}P\xrightarrow{\delta}
\prod_{e\in E_\Omega}B^e.
\]
Exactness here says that \(i\) is injective and its image is \(\ker\delta\).

Flatness gives injectivity of \(1\otimes i\) and
\[
\operatorname{im}(1\otimes i)=\ker(1\otimes\delta).
\]

### Step 4. Lift an arbitrary section after base change

Take \(f\in\Gamma_\Omega(B_S)\). By Step 1 there is a tensor \(z\in S\otimes_R P\) with \(\Phi(z)=f\) as assignments.

Compatibility gives \(\delta_S(f)=0\). Step 2 then gives
\(\Psi((1\otimes\delta)z)=0\). Since \(\Psi\) is injective,
\((1\otimes\delta)z=0\).

Step 3 supplies \(w\in S\otimes_R\Gamma_\Omega(B)\) with
\((1\otimes i)w=z\). Therefore
\[
\Theta_\Omega(w)=\Phi((1\otimes i)w)=\Phi(z)=f.
\]
This proves surjectivity.

### Step 5. Prove injectivity and assemble the isomorphism

If \(\Theta_\Omega(w)=\Theta_\Omega(w')\), equality of their underlying assignments gives
\[
\Phi((1\otimes i)w)=\Phi((1\otimes i)w').
\]
Injectivity of \(\Phi\) gives equality after \(1\otimes i\), and flatness makes that map injective. Hence \(w=w'\).

This step uses the finite vertex-product map but not the edge-product map. Combining both directions gives tensorSectionsEquiv.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.tensorAssignments_bijective`: [MinimalExtensions.lean:1102](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1102).

`OAI.KLInvariance.MomentGraph.Sheaf.constraint_tensorAssignments`: [MinimalExtensions.lean:1107](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1107).

`OAI.KLInvariance.MomentGraph.Sheaf.tensorSections_surjective`: [MinimalExtensions.lean:1121](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1121).

`OAI.KLInvariance.MomentGraph.Sheaf.tensorSections_injective`: [MinimalExtensions.lean:1147](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1147).

`OAI.KLInvariance.MomentGraph.Sheaf.tensorSectionsEquiv`: [MinimalExtensions.lean:1157](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1157).
