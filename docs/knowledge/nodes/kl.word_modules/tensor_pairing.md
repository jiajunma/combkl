---
id: kl.notes.tensor_pairing
title: Transporting a perfect pairing through tensor induction
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.tensor_induction
- kl.word.trace_restriction_duality
- kl.word.tensor_dual_base_change
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.FrobeniusDuality.restrictionBasis
  - OAI.KLInvariance.FrobeniusDuality.inducedModule
  - OAI.KLInvariance.FrobeniusDuality.inducedModule_pairing_tmul
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:263
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.restrictionBasis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:270
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedModule
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:276
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedModule_pairing_tmul
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; bg:normalization
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Replaced the old basis-dual shortcut by the exact restrictPairing then
    extendPairing route. Checked the product-basis argument, inverse functional reconstruction,
    algebraMap in the formula and explicit one-letter pairing.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Transporting a perfect pairing through tensor induction

Let \(\eta:R\to A\) be an algebra map between commutative rings, with \(A\) finite free over \(R\). Suppose \(t:A\to R\) is \(R\)-linear and
\[
D:A\xrightarrow{\sim}\operatorname{Hom}_R(A,R),
\qquad D(a)(b)=t(ab).
\]
Let \(N\) be a finite free paired \(A\)-module with perfect pairing \(B_N\). Then \(A\otimes_R N\) is finite free over \(A\) and carries the perfect pairing
\[
B'(a\otimes m,b\otimes n)=ab\,\eta(t(B_N(m,n))).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit tensor construction underlying the duality.**

**OpenAI notes:** The grading-normalization proof starts from a normalized self-dual projective, uses the cited moment-graph/Soergel equivalence and character theorem, and translates doubled degrees back to the degree-one convention. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The local construction begins with the simple reflection fixed algebra and the trace extracting the root coefficient, normalized by t(alpha)=1. It recovers linear functionals through the trace, extends the resulting duality by tensor product, and proves a one-degree pairing shift for each letter. [Decomposition:1588](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1588), [Frobenius:168](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L168), [Frobenius:270](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L270), [Frobenius:602](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L602).

**Role in the proof:** These nodes supply the actual word-module pairing and its homogeneous basis calculation. The boundary-pairing construction subsequently transports this pairing to a boundary summand. The source uses roots of degree one throughout this tensor calculation.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Construct a finite basis over the smaller ring

Choose a finite \(R\)-basis \((a_i)\) of \(A\) and a finite \(A\)-basis \((n_j)\) of \(N\). Every vector of \(N\) has a unique expression
\[
m=\sum_j c_j n_j,\qquad c_j=\sum_i r_{ij}a_i,\quad r_{ij}\in R.
\]
Substitution gives \(m=\sum_{i,j}r_{ij}a_i n_j\), proving spanning over \(R\).

If this sum vanishes, independence of the \(n_j\) over \(A\) first gives \(\sum_i r_{ij}a_i=0\) for each \(j\). Independence of the \(a_i\) over \(R\) then gives every \(r_{ij}=0\). Thus \((a_i n_j)\) is an \(R\)-basis, and it is finite.

### Step 2. Restrict the perfect pairing through the trace

The [[node:kl.word.trace_restriction_duality|trace-restriction theorem]] gives an \(R\)-linear isomorphism
\[
\operatorname{Hom}_A(N,A)\xrightarrow{\sim}
\operatorname{Hom}_R(N,R),\qquad \lambda\mapsto t\circ\lambda.
\]
Compose it with the original pairing map \(p_N\), viewed over \(R\). The resulting perfect \(R\)-pairing has value
\[
b_R(m,n)=t(B_N(m,n)).
\]

To locate the representing vector of an arbitrary \(R\)-functional \(f\), form the \(A\)-functional
\(c_f(m)=D^{-1}(a\mapsto f(am))\), as proved in the restriction theorem. Then \(p_N^{-1}(c_f)\) represents \(f\) for \(b_R\). This identifies the inverse used in the composition.

### Step 3. Extend the restricted pairing

Step 1 supplies the finite freeness required by the [[node:kl.word.tensor_dual_base_change|tensor-dual base-change theorem]]. Apply that theorem to the perfect \(R\)-pairing \(b_R\). Its composite isomorphism is
\[
A\otimes_R N
\longrightarrow A\otimes_R\operatorname{Hom}_R(N,R)
\longrightarrow\operatorname{Hom}_A(A\otimes_R N,A).
\]
It sends the first tensor \(a\otimes m\), evaluated on \(b\otimes n\), to
\[
ab\,\eta(b_R(m,n))=ab\,\eta(t(B_N(m,n))).
\]
This proves both the formula and perfection. The same base-change theorem transports the finite basis from Step 1 to \(1\otimes a_i n_j\), proving finite freeness over \(A\).

### Step 4. Calculate the first reflection step

Take \(A=k[X]\), \(R=k[X^2]\), the reflection trace \(t\), and \(N=A\) with multiplication pairing. The induced module has basis
\[
u=1\otimes1,\qquad v=1\otimes X.
\]
The formula gives
\[
B'(u,u)=t(1)=0,\quad
B'(u,v)=B'(v,u)=t(X)=1,\quad
B'(v,v)=t(X^2)=0.
\]
Thus for \(a,b,c,d\in A\),
\[
B'(au+bv,cu+dv)=ad+bc.
\]
The pairing matrix is the same invertible cross matrix as the trace pairing. This calculation gives the one-letter word pairing before iterating the construction.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.FrobeniusDuality.restrictionBasis`: [Frobenius.lean:263](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L263).

`OAI.KLInvariance.FrobeniusDuality.inducedModule`: [Frobenius.lean:270](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L270).

`OAI.KLInvariance.FrobeniusDuality.inducedModule_pairing_tmul`: [Frobenius.lean:276](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L276).
