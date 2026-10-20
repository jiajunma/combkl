---
id: kl.local.model_sum_scaled_images
title: Scaled image equality in products and model sums
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.detail.scaled_images
- kl.local.model_sums
- kl.sheaves.upward_kernel
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.prod_upwardKernel_iff
  - OAI.KLInvariance.MomentGraph.Sheaf.pi_upwardKernel_iff
  - OAI.KLInvariance.MomentGraph.Sheaf.prod_scaledImages
  - OAI.KLInvariance.MomentGraph.Sheaf.pi_scaledImages
  - OAI.KLInvariance.MomentGraph.Sheaf.zero_scaledImages
  - OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.scaledImages
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:480
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.prod_upwardKernel_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:497
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.pi_upwardKernel_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:508
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.prod_scaledImages
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:526
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.pi_scaledImages
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:542
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.zero_scaledImages
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:548
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.scaledImages
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the binary and arbitrary-product kernel equivalences, both witness
    directions in prod/pi_scaledImages, zero_scaledImages and the ModelSum induction.
    Retained the same scalar in every summand and the general family statement, with
    finiteness only in the actual ModelSum construction.
tags:
- Kazhdan-Lusztig
- embedded-images
---

# Scaled image equality in products and model sums

Let \(R\) be a commutative ring and \(G\) an ordered graph. Fix an edge \(e:x\to y\), outgoing selections \(F,H\) at its endpoints, and a scalar \(r\in R\).

If every \(R\)-module sheaf \(B_i\) in a family on \(G\) satisfies
\[
L_e^{B_i}(F)=rU_e^{B_i}(H),
\]
then their product sheaf satisfies the same equality, with the same scalar \(r\). In particular this holds for finite sums.

More generally, let \(O_c\) be a family of such sheaves and \(C\) a finite ungraded model sum with centers in a vertex set \(U\). If every \(O_c\), \(c\in U\), satisfies this scaled image equality, then so does \(C\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The same embedded images through one edge component.**

**OpenAI notes:** The model decomposition carries both localized kernels and their endpoint images into the model summands. Its single edge component carries both comparison submodules, and linearity carries the correction scalar through that same map. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** Selected-kernel membership and both image equalities are proved for arbitrary sheaf isomorphisms over a commutative ring. ScaledImages is an elementwise witness equivalence, identified with submodule equality. Coordinatewise witness transport proves the product and model-sum statements with one common scalar. [PositiveTransfer:362](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L362), [PositiveTransfer:366](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L366), [CharacterReciprocity:443](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L443), [GradedSheaves:631](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L631), [GradedSheaves:639](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L639), [TerminalKernels:19](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L19), [CharacterReciprocity:548](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L548).

**Role in the proof:** The Blueprint defines the actual submodules and witnesses before transporting them. The generic ungraded transport is the one applied to the local model decomposition.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Read the selected kernel coordinatewise

In the product sheaf \(\prod_iB_i\), restrictions act on each coordinate. A stalk tuple \(v=(v_i)_i\) satisfies every selected lower restriction exactly when
\[
\rho^{B_i,-}_f(v_i)=0
\qquad\text{for every }i\text{ and every selected }f.
\]
Therefore
\[
v\in K_x^{\prod_iB_i}(F)
\quad\Longleftrightarrow\quad
v_i\in K_x^{B_i}(F)\text{ for every }i.
\]
The same statement holds for the selection \(H\) at \(y\). The two-factor version uses the two coordinate projections; the general product uses all coordinate projections.

### Step 2. Transport a lower witness to upper witnesses

Take an edge tuple \(z=(z_i)_i\) in the lower image of the product sheaf. It has a lower witness \(v=(v_i)_i\), with
\[
v_i\in K_x^{B_i}(F),\qquad
\rho^{B_i,-}_e(v_i)=z_i.
\]
The scaled equality in \(B_i\) supplies \(w_i\in K_y^{B_i}(H)\) with
\[
r\rho^{B_i,+}_e(w_i)=z_i.
\]

Choose these witnesses in each coordinate and form \(w=(w_i)_i\). Step 1 places \(w\) in the product's upper selected kernel, and the coordinate equations give
\[
r\rho^+_e(w)=z.
\]
Thus \(z\) belongs to the scaled upper image.

### Step 3. Prove the reverse containment

Start with an upper witness \(w=(w_i)_i\) in the product, with
\(r\rho^+_e(w)=z\). Each coordinate gives a scaled upper witness in \(B_i\).

Use the reverse direction of the scaled equality in \(B_i\) to choose a lower witness \(v_i\). Their tuple lies in the lower selected kernel by Step 1 and has lower edge value \(z\). This proves the reverse containment.

The source's pi theorem permits an arbitrary index type; classical choice assembles the coordinate witnesses. Finite products give the finite-sum case used in decomposition.

### Step 4. Check the zero sheaf

The zero sheaf has only the edge value \(0\). Both selected images are zero, and zero stalk vectors are witnesses on both sides for every scalar \(r\).

### Step 5. Induct on the model-sum construction

The zero constructor is covered by Step 4.

For the addition constructor, assume the statement for a model sum \(C_0\), choose \(c\in U\), and add \(n\) copies of \(O_c\). The product result gives scaled equality in \(O_c^n\), because \(O_c\) satisfies it. The two-factor result then gives it in
\[
C_0\oplus O_c^n.
\]
Induction proves the assertion for the whole model sum.

In the local comparison, the correction scalar is fixed by the current edge and is the same for every model center. This is the common scalar required by the theorem.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.prod_upwardKernel_iff`: [CharacterReciprocity.lean:480](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L480).

`OAI.KLInvariance.MomentGraph.Sheaf.pi_upwardKernel_iff`: [CharacterReciprocity.lean:497](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L497).

`OAI.KLInvariance.MomentGraph.Sheaf.prod_scaledImages`: [CharacterReciprocity.lean:508](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L508).

`OAI.KLInvariance.MomentGraph.Sheaf.pi_scaledImages`: [CharacterReciprocity.lean:526](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L526).

`OAI.KLInvariance.MomentGraph.Sheaf.zero_scaledImages`: [CharacterReciprocity.lean:542](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L542).

`OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.scaledImages`: [CharacterReciprocity.lean:548](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L548).
