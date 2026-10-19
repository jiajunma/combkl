---
id: kl.sheaves.edge_coefficient_module
title: The actual edge module over its coefficient ring
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.algebra.edge_coefficient_ring
- kl.detail.upper_quotient
- kl.algebra.scalar_quotient_basis
- kl.sheaves.boundary_sheaf
lean:
  repository: openai-kl
  modules:
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.BruhatGraph.edgeTorsion
  - OAI.KLInvariance.BruhatGraph.edgeModule
  - OAI.KLInvariance.BruhatGraph.edgeModule_tower
  - OAI.KLInvariance.BruhatGraph.edgeModule_free
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:665
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edgeTorsion
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:669
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edgeModule
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:674
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edgeModule_tower
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:681
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edgeModule_free
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read edge annihilation, the quotient-module instance, scalar-tower compatibility
    and the free-of-presentation application. Explained the action on representatives
    and the actual descended basis, using only the constructed upper stalk and quotient
    rule.
tags:
- Kazhdan-Lusztig
- coefficient-rings
---

# The actual edge module over its coefficient ring

Fix a finite-generator Coxeter system, a polynomial coefficient algebra \(A\) from a finite real basis of the extended realization, and a normalized boundary sheaf \(B\) on \([u,b]\), with \(u\le b\).

Write \(\lambda:V_0\to A\) for the linear-label map from the original root space. Let \(e:x\to y\) have canonical positive root \(a\), so its polynomial label is \(r_a=\lambda(a)\). Put \(E_a=A/(r_a)\).

The edge module \(B^e\) has the \(E_a\)-action
\[
[f]\cdot v=fv.
\]
This action is compatible with its existing \(A\)-action and makes \(B^e\) finite free over \(E_a\). If \((m_i)\) is an \(A\)-basis of the upper stalk \(B^y\), then
\[
\bigl(\rho^+_e(m_i)\bigr)_i
\]
is an \(E_a\)-basis of \(B^e\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Coordinate construction of the edge coefficient module.**

**OpenAI notes:** The upper-end quotient rule presents the edge module as the upper stalk modulo its root label. The edge comparison regards it as a free module over the corresponding coefficient quotient. [bg:bmp](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225), [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The root label first annihilates the edge module, defining its quotient-ring action and scalar compatibility. Coordinate reduction of a finite upper-stalk basis has the same scalar kernel as the upper restriction, and the quotient comparison gives a basis of the actual edge module. [TerminalKernels:516](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L516), [TerminalKernels:573](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L573), [TerminalKernels:595](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L595), [TerminalKernels:669](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L669), [TerminalKernels:681](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L681).

**Role in the proof:** Both the coefficient ring and its module action are fixed before comparing lower and upper images. Their elements remain in the original edge module with its induced quotient-ring scalars.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Prove that the edge label annihilates the edge module

The upper-quotient rule gives a surjection \(\rho^+_e:B^y\to B^e\) with kernel \(r_aB^y\).

Given \(v\in B^e\), choose \(w\in B^y\) with \(\rho^+_e(w)=v\). Then
\[
r_av=r_a\rho^+_e(w)=\rho^+_e(r_aw)=0.
\]
This is edgeTorsion.

### Step 2. Descend the scalar action

If \(f-f'=r_ag\), then
\[
fv-f'v=(r_ag)v=g(r_av)=0.
\]
Thus \([f]\cdot v=fv\) is independent of the representative of \([f]\).

Addition, multiplication and the unit law follow from the corresponding \(A\)-module laws. This defines edgeModule. For \(f\in A\), the class of \(f\) acts exactly as \(f\) already acted, which is the compatibility recorded by edgeModule_tower.

### Step 3. Apply the [[node:kl.algebra.scalar_quotient_basis|scalar-kernel basis theorem]]

The actual upper stalk is finite free over \(A\). Choose its finite basis \((m_i)\).

The map \(q=\rho^+_e\) is \(A\)-linear and surjective, and its kernel is exactly \(r_aB^y\). Step 2 gives the required compatible \(A/(r_a)\)-module action on the target. The [[node:kl.algebra.scalar_quotient_basis|scalar-kernel basis theorem]] therefore applies and gives the asserted basis \((q(m_i))\) over \(E_a\).

This proves edgeModule_free and finite generation over the edge coefficient ring.

### Step 4. Evaluate the rank-one congruence model

If \(B^y=A\) and the upper map is the quotient \(A\to A/(r_a)\), the source basis is \((1)\). Its image \(([1])\) is the resulting one-element basis of the edge module over \(E_a\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.edgeTorsion`: [TerminalKernels.lean:665](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L665).

`OAI.KLInvariance.BruhatGraph.edgeModule`: [TerminalKernels.lean:669](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L669).

`OAI.KLInvariance.BruhatGraph.edgeModule_tower`: [TerminalKernels.lean:674](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L674).

`OAI.KLInvariance.BruhatGraph.edgeModule_free`: [TerminalKernels.lean:681](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L681).
