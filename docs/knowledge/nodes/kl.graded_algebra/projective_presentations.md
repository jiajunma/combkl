---
id: kl.algebra.projective_presentations
title: Projective modules, presentations and split maps
kind: definition
status: formalized
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses: []
lean:
  repository: openai-kl
  modules:
  - ModuleAlgebra
  declarations:
  - OAI.KLInvariance.LocalCover.splitEquiv
  - OAI.KLInvariance.ReverseFiltration.kernel_projective_of_presentation
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:184
    format: lean-location
    note: OAI.KLInvariance.LocalCover.splitEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:246
    format: lean-location
    note: OAI.KLInvariance.ReverseFiltration.kernel_projective_of_presentation
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the coefficient rings, module properties and actual maps explicit?
  verdict: Read splitEquiv and kernel_projective_of_presentation. Defined the lifting
    property, free-module lifts, split summands, exact presentations and the explicit
    splitting formulas used in the local source.
tags:
- Kazhdan-Lusztig
- module-algebra
---

# Projective modules, presentations and split maps

Let \(R\) be a commutative ring. An \(R\)-module \(P\) is projective when maps out of it lift through surjections: for a surjective linear map \(q:X\to Y\) and a linear map \(h:P\to Y\), there is \(\widetilde h:P\to X\) with \(q\widetilde h=h\).

A free module is projective. Choose a preimage under \(q\) of the image of each basis vector, then extend by linearity. Every vector has a finite basis expansion, so this defines the lift on the whole module.

## Sections and retractions

A section of a surjection \(g:B\to P\) is a linear map \(s:P\to B\) with \(gs=1_P\). Projectivity of \(P\) supplies such a section by lifting \(1_P\) through \(g\).

More generally, maps
\[
i:K\to E,\qquad r:E\to K,\qquad ri=1_K
\]
make \(K\) a direct summand of \(E\). If \(E\) is projective, then so is \(K\): extend a lifting problem from \(K\) to \(E\) by composing with \(r\), lift from \(E\), and restrict the lift along \(i\).

Finite direct sums of projective modules are projective. A map from the sum restricts to a map from each summand; lift each restriction and add the resulting maps.

## The explicit splitting of a surjection

Given \(g:B\to P\) and a section \(s\), the source constructs
\[
B\xrightarrow{\sim}P\oplus\ker g,\qquad
b\longmapsto(gb,b-sgb).
\]
The second component belongs to the kernel because \(g(b-sgb)=gb-gb=0\).

The inverse is \((p,k)\mapsto sp+k\). Its composite on \(b\) is \(sgb+b-sgb=b\). Its composite on \((p,k)\) is \((p,sp+k-sp)=(p,k)\), using \(gk=0\).

## Projective presentations

A surjection \(g:E\to I\), together with its kernel, gives the exact sequence
\[
0\longrightarrow\ker g\longrightarrow E\xrightarrow{g}I\longrightarrow0.
\]
If \(E\) and \(\ker g\) are projective, this is a length-one projective presentation of \(I\).

The [[node:kl.algebra.kernel_projectivity|two-presentation theorem]] compares this sequence with a second surjection \(f:F\to I\) from a projective module. It constructs a retraction proving that \(\ker f\) is projective. This is the algebraic step used to recover a kernel after an image equality.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.LocalCover.splitEquiv`: [ModuleAlgebra.lean:184](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L184).

`OAI.KLInvariance.ReverseFiltration.kernel_projective_of_presentation`: [ModuleAlgebra.lean:246](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L246).
