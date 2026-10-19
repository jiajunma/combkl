---
id: kl.sheaves.lower_model_kernels
title: Stalks and kernels of the lower-supported Bruhat models
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.boundary_models_exist
- kl.sheaves.lower_extension_properties
- kl.sheaves.kernel_transport
- kl.detail.costalk_reciprocity
- kl.duality.stalk_character
- kl.detail.boundary_pairing
- kl.detail.costalk_duality
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  - Decomposition
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend_kernel_iff
  - OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtendKernelEquiv
  - OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtendKernelEquiv_graded
  - OAI.KLInvariance.BruhatGraph.lowerKernelEquiv
  - OAI.KLInvariance.BruhatGraph.boundaryModels_character
  - OAI.KLInvariance.BruhatGraph.boundaryModels_kernelFree
  - OAI.KLInvariance.BruhatGraph.boundaryModels_kernelCharacter
  - OAI.KLInvariance.BruhatGraph.lowerCharacter
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1847
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend_kernel_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1867
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtendKernelEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1877
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtendKernelEquiv_graded
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1922
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.lowerKernelEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:108
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.boundaryModels_character
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1936
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.boundaryModels_kernelFree
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1947
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.boundaryModels_kernelCharacter
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:104
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.lowerCharacter
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

# Stalks and kernels of the lower-supported Bruhat models

Fix a finite-generator Coxeter system, a lower interval \([1,b]\), and a real basis of the extended realization, giving its polynomial coefficient algebra. Let \(O_c\) be the boundary model centered at \(c\le b\), obtained from the actual boundary sheaf on \([1,c]\).

Every full outgoing kernel of \(O_c\) is free. For \(x\le c\), its stalk and kernel characters are
\[
C_{O_c}(x;q)=C_{x,c}(q),
\]
\[
K_{O_c}(x;q)
=q^{\ell(c)-\ell(x)}C_{x,c}(q^{-1}).
\]
For \(x\not\le c\), both characters are zero.

*Proof.*

### Step 1. Identify the stalk inside the lower ideal

At \(x\le c\), the lower-extension identification and the graph identification with \([1,c]\) give
\[
O_c^x\simeq B(c)^x
\]
as graded modules. Hence their characters are equal, giving the first formula.

### Step 2. Identify all outgoing kernel conditions

An outgoing edge from \(x\) whose target is at most \(c\) is exactly an outgoing reflection edge in the graph of \([1,c]\). Its restriction agrees with the corresponding restriction of \(B(c)\) under the stalk identification.

An outgoing edge with target outside the lower ideal has zero \(O_c\)-edge module. Its restriction is zero and imposes no additional condition.

Thus the same stalk identification restricts to a graded isomorphism
\[
K_x(O_c)\simeq K_x(B(c)).
\]

### Step 3. Use the boundary costalk duality

The [[node:kl.detail.boundary_pairing|boundary-pairing]] and [[node:kl.detail.costalk_duality|costalk-duality theorems]] make \(K_x(B(c))\) finite free. Its homogeneous basis degrees are
\[
\ell(c)-\ell(x)-d_i,
\]
where \(d_i\) are the basis degrees of \(B(c)^x\). The kernel is nonnegative, so these exponents are nonnegative.

Therefore
\[
\operatorname{ch}(K_x(B(c));q)
=\sum_iq^{\ell(c)-\ell(x)-d_i}
=q^{\ell(c)-\ell(x)}C_{x,c}(q^{-1}).
\]
This is a polynomial: the displayed sum writes all its exponents as nonnegative integers. Step 2 transfers its freeness and character to \(O_c\).

### Step 4. Evaluate outside the support

If \(x\not\le c\), the model support gives \(O_c^x=0\). Its outgoing kernel, a submodule of that stalk, is zero as well. Both are free of rank zero and have zero character.

The source packages the first piecewise formula as the lower character, assigning zero outside \(x\le c\), and packages the second by polynomial reflection.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend_kernel_iff`: [CharacterReciprocity.lean:1847](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1847).

`OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtendKernelEquiv`: [CharacterReciprocity.lean:1867](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1867).

`OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtendKernelEquiv_graded`: [CharacterReciprocity.lean:1877](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1877).

`OAI.KLInvariance.BruhatGraph.lowerKernelEquiv`: [CharacterReciprocity.lean:1922](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1922).

`OAI.KLInvariance.BruhatGraph.boundaryModels_character`: [Decomposition.lean:108](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L108).

`OAI.KLInvariance.BruhatGraph.boundaryModels_kernelFree`: [CharacterReciprocity.lean:1936](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1936).

`OAI.KLInvariance.BruhatGraph.boundaryModels_kernelCharacter`: [CharacterReciprocity.lean:1947](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1947).

`OAI.KLInvariance.BruhatGraph.lowerCharacter`: [Decomposition.lean:104](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L104).
