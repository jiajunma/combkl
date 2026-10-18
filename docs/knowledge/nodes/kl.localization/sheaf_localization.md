---
id: kl.notes.sheaf_localization
title: Localizing the sheaf at a root plane
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.sheaves.upward_kernel
- kl.notes.dihedral_models
- kl.detail.base_change
lean:
  repository: openai-kl
  modules:
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChange_upwardKernel
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChange_lowerImage
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChange_upperImage
source:
  spans:
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
  prompt: Are the mathematical hypotheses and scope retained from the referenced declarations?
  verdict: The exposition follows the fixed Lean source; worked calculations explain
    the constructions.
tags:
- Kazhdan-Lusztig
- localization
---

# Localizing the sheaf at a root plane

For a flat scalar extension, finite upward-kernel conditions and their edge images commute with base change. In particular, one may compute the kernel and its image first and then localize, or perform both constructions on the localized sheaf.

*Proof.*

### Step 1. Write the maps before localizing

Let \(S\) be the multiplicative set being inverted and \(A_S\) the localized ring. For a finite set \(F\) of outgoing conditions at \(x\), package the restrictions into one map
\[
r_F:B^x\longrightarrow\bigoplus_{e\in F}B^e,\qquad
v\longmapsto(\rho_{x,e}(v))_{e\in F}.
\]
Its kernel is precisely \(K_x(F)\).

Localization sends every stalk and edge module to its tensor product with \(A_S\), and sends each restriction to \(1\otimes\rho\). It also commutes with the finite direct sum: the map sends \(s^{-1}\otimes(v_e)_e\) to \((s^{-1}\otimes v_e)_e\), with inverse obtained by summing the component inclusions.

### Step 2. Identify the localized kernel

The sequence
\(0\to K_x(F)\to B^x\to\operatorname{im}r_F\to0\)
is exact. Localization is flat, so tensoring preserves its left injectivity and exactness at the middle. The inclusion \(\operatorname{im}r_F\to\bigoplus_{e\in F}B^e\) remains injective as well.

Therefore the kernel of the localized restriction map is exactly the image of \(A_S\otimes K_x(F)\). This gives the desired identification of partial kernels. Finiteness of \(F\) is what allowed the constraints to be put into the localized finite direct sum in Step 1.

### Step 3. Identify the localized images inside the localized edge module

For \(I=\rho_{x,e}(K_x(F))\), factor the restricted map as a surjection
\(K_x(F)\twoheadrightarrow I\)
followed by the inclusion \(I\hookrightarrow B^e\).
Tensoring preserves the surjection by right exactness and the inclusion by flatness. Its composite is the localized restriction on the localized kernel from Step 2. Hence its image, as an actual submodule of \(A_S\otimes B^e\), is \(A_S\otimes I\).

The identical argument for the upper endpoint proves the upper-image statement. Both images have been identified in the same localized edge module.

### Step 4. Remove the edges killed by root-plane localization

If an edge label becomes a unit, its quotient edge module becomes zero. Its localized kernel condition is then the equation \(0=0\) and imposes no restriction. Thus the localized partial kernels and images depend only on the surviving edges. This is the precise algebraic reason one can pass to a surviving dihedral coset.

## References

[4. Localization at a root plane](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L285).

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.baseChange_upwardKernel`: [TerminalKernels.lean:347](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L347).

`OAI.KLInvariance.MomentGraph.Sheaf.baseChange_lowerImage`: [TerminalKernels.lean:360](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L360).

`OAI.KLInvariance.MomentGraph.Sheaf.baseChange_upperImage`: [TerminalKernels.lean:367](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L367).
