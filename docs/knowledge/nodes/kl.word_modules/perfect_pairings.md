---
id: kl.notes.perfect_pairings
title: Perfect pairings and balanced bimodules
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses: []
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.FrobeniusDuality.PairedModule
  - OAI.KLInvariance.FrobeniusDuality.PairedBimodule
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:226
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.PairedModule
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:295
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.PairedBimodule
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; bg:normalization
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the mathematical hypotheses and scope retained from the referenced declarations?
  verdict: The exposition follows the fixed Lean source; worked calculations explain
    the constructions.
tags:
- Kazhdan-Lusztig
- background
---

# Perfect pairings and balanced bimodules

For a module \(M\) over a commutative ring \(A\), write
\[
M^*=\operatorname{Hom}_A(M,A)
\]
for its \(A\)-linear dual. A perfect pairing is specified by an \(A\)-linear isomorphism
\[
d:M\xrightarrow{\sim}M^*,\qquad
\langle m,n\rangle=d(m)(n).
\]
The two linearities make this an \(A\)-bilinear pairing. Perfection says that every functional on \(M\) has a unique representative in the first argument.

## Finite free paired modules

The paired-module data used in tensor induction consist of an underlying additive group with its \(A\)-module structure, finite freeness over \(A\), and the isomorphism \(d\).

For a basis \(b_1,\ldots,b_r\), the pairing is represented by the matrix \(G_{ij}=\langle b_i,b_j\rangle\). It is perfect exactly when this matrix is invertible over \(A\).

For \(M=A\) with \(\langle a,b\rangle=cab\), the adjoint map is multiplication by \(c\) after identifying \(A^*\) with \(A\) by evaluation at one. Thus the pairing is perfect exactly when \(c\) is a unit. In particular, multiplication pairing with \(c=1\) is perfect.

## A commuting right action

A paired bimodule also has a right \(A\)-action commuting with the left action. Equivalently, each \(a\in A\) acts by an \(A\)-linear endomorphism \(R_a\), and the assignment \(a\mapsto R_a\) is a unital ring homomorphism. Write \(m\cdot a=R_a(m)\).

Since \(A\) is commutative, the right operators commute with each other and satisfy the usual right-module laws. Their \(A\)-linearity gives
\[
b(m\cdot a)=(bm)\cdot a.
\]

The pairing satisfies balance and symmetry:
\[
\langle m\cdot a,n\rangle=\langle m,n\cdot a\rangle,
\qquad
\langle m,n\rangle=\langle n,m\rangle.
\]
Balance moves the right action from one argument to the other. Symmetry exchanges the two arguments.

For \(M=A\), the usual right multiplication and \(\langle m,n\rangle=mn\) satisfy both equations. Tensor induction extends this datum through a reflection's Frobenius extension.

## References

The local definitions and constructions are listed below.

## Lean formalization

PairedModule fields `carrier`, `add`, `module`, `free`, `finite`, `pairing` record the module and perfect pairing. PairedBimodule adds `obj`, `right`, `balanced`, `symmetric` for the underlying paired module, commuting right action, balance, and symmetry.

`OAI.KLInvariance.FrobeniusDuality.PairedModule`: [Frobenius.lean:226](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L226).

`OAI.KLInvariance.FrobeniusDuality.PairedBimodule`: [Frobenius.lean:295](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L295).
