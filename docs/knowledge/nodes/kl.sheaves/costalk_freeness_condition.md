---
id: kl.duality.costalk_freeness_condition
title: The full outgoing-kernel freeness condition
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.boundary_sheaf
- kl.sheaves.upward_kernel
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.BruhatGraph.CostalkFreeObligation
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:223
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.CostalkFreeObligation
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the CostalkFreeObligation definition with its interval/basis parameters.
    Explained the exact full outgoing map and finite-generation consequence; connected
    the established lower-interval duality and upper-restriction transport through
    existing proofs.
tags:
- Kazhdan-Lusztig
- graded-duality
---

# The full outgoing-kernel freeness condition

Fix a finite-generator Coxeter system, an interval \([u,b]\) with \(u\le b\), and the real polynomial coefficient algebra \(A\) of its extended realization. Let \(B_{u,b}\) be the chosen normalized boundary sheaf on this interval.

At each vertex \(x\), the combined outgoing restriction map is
\[
\partial_x:B_{u,b}^x\longrightarrow\prod_{e:x\to y}B_{u,b}^e,
\qquad
v\longmapsto(\rho^-_e(v))_e.
\]
The **full outgoing-kernel freeness condition**, named CostalkFreeObligation in Lean, is the proposition
\[
\forall x\in[u,b],\qquad \ker\partial_x
\text{ is a free }A\text{-module}.
\]

It quantifies over the full set of outgoing edges at each vertex. Equivalently, it asserts freeness of \(L_x(U_x)\), where \(U_x\) is that full outgoing set. Each kernel is finitely generated because it is a submodule of a finitely generated stalk over the Noetherian polynomial ring. Thus, when the condition holds, these are finite free modules.

## The constructed boundary family on a lower interval

On \([1,b]\), the actual section duality gives
\[
\ker\partial_x\simeq\operatorname{Hom}_A(B(b)^x,A).
\]
A finite free basis of the stalk has a finite dual basis; transport through this equivalence proves kernel freeness at each \(x\). The [[node:kl.duality.boundary_kernel_character|boundary kernel character theorem]] explains this construction and its grading. Quantifying over \(x\) yields the source's costalkFreeObligation theorem.

At the top vertex there are no outgoing edges, so \(\ker\partial_b=B^b=A\). In the one-edge congruence model \(x\to b\) with label \(\alpha\), the two full kernels are \(\alpha A\) and \(A\); multiplication by the nonzero \(\alpha\) identifies \(A\) with the first kernel.

The [[node:kl.sheaves.upper_interval_kernels|upper-interval kernel theorem]] transports these full kernels to the restricted boundary family. Boundary uniqueness then gives the same freeness property for the independently chosen normalized boundary sheaf on that upper interval.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Construction of the stated freeness property.**

**OpenAI notes:** The moment-graph sheaf theorem includes graded freeness of the kernel obtained by imposing all outgoing edge conditions. [bg:bmp](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

**Lean (primary):** CostalkFreeObligation expresses this property for the chosen boundary sheaf. On a lower interval, costalkFreeObligation proves it using the constructed actual section duality and free stalks. [SheafMorphisms:223](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L223), [PositiveTransfer:129](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L129), [PositiveTransfer:146](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L146).

**Role in the proof:** The full kernel is the image of the local intersection map and is linearly equivalent to the finite free stalk dual. Its induced grading is the one used in the kernel-character formula.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.CostalkFreeObligation`: [SheafMorphisms.lean:223](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L223).
